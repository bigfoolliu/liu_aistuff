#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


import hashlib
import json
import time
from urllib.parse import urlparse
from uuid import uuid4

from flask import Flask, jsonify, request


class BlockChain(object):

    def __init__(self):
        self.chains = []  # 储存区块链
        self.current_transactions = []  # 储存交易
        self.new_block(proof=100, previous_hash=1)  # 初始区块，创世块
        self.nodes = set()  # 每一个节点都要保存一份包含网络中其他节点的记录,但是要避免节点重复
    
    def new_block(self, proof, previous_hash=None):
        """
        创建一个新的区块,每一个新的区块都会包含上一个区块的hash值
        """
        block = {
            "index": len(self.chains)+1,
            "timestamp": time.time(),
            "transactions": self.current_transactions,
            "proof": proof,
            "previous_hash": previous_hash or self.hash(self.chains[-1]),
        }
        self.current_transactions = []
        self.chains.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        创建一笔新的交易
        :param sender: <str> 发送者的地址
        :param recipient: <str> 接受者的地址
        :param amount: <int> 发送的金额数量
        :return: <int> 持有该交易区块的索引
        """
        self.current_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        })
        return self.last_block["index"] + 1

    @staticmethod
    def hash(block):
        """将一个区块哈希化,并加密"""
        block_str = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_str).hexdigest()

    @property
    def last_block(self):
        """返回区块链中的最后一个区块"""
        return self.chains[-1]
    
    def proof_of_work(self, last_proof):
        """
        工作量证明算法，通过计算的工作量来获取奖励
        此处规则：寻找一个数p,使得它与前一个区块的proof拼接而成的字符串的hash值前4位为0
        """
        proof = 0
        while self.is_valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def is_valid_proof(last_proof, proof):
        """验证proof是否合法"""
        guess = f"{last_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
    
    def register_node(self, address):
        """注册新的节点,并将其添加到链中"""
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)
    
    def is_valid_chain(self, chain):
        """判断区块链是否合规,规定最长的合规的链就是最有效的链"""
        last_block = chain[0]
        current_index = 1

        # 循环验证所有的区块都是合法的
        while current_index < len(chain):
            block = chain[current_index]
            print("last block: {}\nblock: {}".format(last_block, block))
            if not block["previous_hash"] == self.hash(last_block):
                return False
            if not self.is_valid_proof(last_block["proof"], block["proof"]):
                return False
            last_block = block
            current_index += 1
        return True
    
    def resolve_conflicts(self):
        """解决冲突"""
        neighbors = self.nodes
        new_chain = None

        max_length = len(self.chains)
        for node in neighbors:
            response = request.get(f"http://{node}/chain")
            if response.status_code == 200:
                length = response.json()["length"]
                chain = response.json()["chain"]
                if length > max_length and self.is_valid_chain(chain):
                    new_length = length
                    new_chain = chain
        if new_chain:
            self.chains = new_chain
            return True
        return False


app = Flask(__name__)  # 初始化该节点，一台主机就是一个节点

node_identifier = str(uuid4()).replace("-", "")  # 为该节点创建一个全局唯一的标识
block_chain = BlockChain()


@app.route("/mine", methods=["GET"])
def mine():
    # 获取到最后一个区块的proof,然后计算出新的proof
    last_block = block_chain.last_block()
    last_proof = last_block["proof"]
    proof = block_chain.proof_of_work(last_proof)

    # 找到新的proof会有奖励，sender是0表示这个节点获得了一枚比特币
    block_chain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1
    )

    # 将新节点加入区块链
    block = block_chain.new_block(proof)

    response = {
        "message": "new block forged",
        "index": block["index"],
        "transaction": block["transaction"],
        "proof": block["proof"],
        "previous_hash": block["previous_hash"]
    }
    return jsonify(response), 200


@app.route("/transactions/new", methods=["POST"])
def new_transaction():
    values = request.get_json()
    print(values)
    required = ["sender", "recipient", "amount"]
    if not all([k in values for k in required]):
        return "missing values", 400
    
    index = block_chain.new_transaction(values["sender"], values["recipient"], values["amount"])
    response = {"message": f"transaction will be added to block {index}"}
    return jsonify(response), 201


@app.route("/chains", methods=["GET"])
def full_chain():
    response = {
        "chains": block_chain.chains,
        "length": len(block_chain.chains)
    }
    return jsonify(response), 200


@app.route("/")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

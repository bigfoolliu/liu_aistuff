#!/usr/bin/env python
#!coding:utf-8


# TODO: not finished.
"""
fer2013.csv文件内容
emotions,pixels,Usage
"""


import string, os, sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import random
import tensorflow as tf
import pandas as pd
import datetime


# 文件位置
FILE_PATH = "../dataset/fer2013/fer2013.csv"


def show_time():
    """显示当前时间"""
    return datetime.datetime.now().isoformat()

def read_file(file_path):
    """读取csv文件"""
    print("[INFO]{}:Begin to read csv file: {}".format(show_time(), file_path))
    data = pd.read_csv(file_path, dtype='a')
    label = np.array(data['emotion'])
    img_data = np.array(data['pixels'])
    N_sample = label.size
    print("[INFO]{}:The size of the sample: {}".format(show_time(), N_sample))

    Face_data = np.zeros((N_sample, 48 * 48))
    Face_label = np.zeros((N_sample, 7), dtype=int)
    temp = np.zeros((7), dtype= int)
    # 遍历读取样本
    for i in range(N_sample):
        x = img_data[i]
        x = np.fromstring(x, dtype=float, sep=" ")
        x_max = x.max()
        x = x / (x_max + 0.0001)

        Face_data[i] = x
        Face_label[i, int(label[i])] = 1
        if i <10:
            print("[INFO]{}:i {} {}\t".format(show_time(), i, Face_label[i]))


read_file(FILE_PATH)


train_num = 30000
test_num = 5000
train_x = Face_data[0:train_num, :]
train_y = Face_label[0:train_num, :]
test_x = Face_data[train_num: train_num + test_num, :]
test_y = Face_label[train_num: train_num + test_num, :]
print("All is well")


batch_size = 50
train_batch_num = train_num / batch_size
test_batch_num = test_num / batch_size
train_epoch = 100
learning_rate = 0.001
# Network Parameters
n_input = 2304  # data input (img shape: 48*48)
n_classes = 7  # total classes
dropout = 0.5  # Dropout, probability to keep units
# tf Graph input
x = tf.placeholder(tf.float32, [None, n_input])
y = tf.placeholder(tf.float32, [None, n_classes])
keep_prob = tf.placeholder(tf.float32)  # dropout (keep probability)
 
 
# Create some wrappers for simplicity
def conv2d(x, W, b, strides=1):
    # Conv2D wrapper, with bias and relu activation
    x = tf.nn.conv2d(x, W, strides=[1, strides, strides, 1], padding='SAME')
    x = tf.nn.bias_add(x, b)
    return tf.nn.relu(x)
 
 
def maxpool2d(x, k=2):
    # MaxPool2D wrapper
    return tf.nn.max_pool(x, ksize=[1, k, k, 1], strides=[1, k, k, 1], padding='VALID')


# Create model
def conv_net(x, weights, biases, dropout):
    # Reshape input picture
    x = tf.reshape(x, shape=[-1, 48, 48, 1])
    # Convolution Layer
    conv1 = conv2d(x, weights['wc1'], biases['bc1'])
    # Max Pooling (down-sampling)
    conv1 = maxpool2d(conv1, k=2)
    # Convolution Layer
    conv2 = conv2d(conv1, weights['wc2'], biases['bc2'])
    # Max Pooling (down-sampling)
    conv2 = maxpool2d(conv2, k=2)
    # Convolution Layer
    conv3 = conv2d(conv2, weights['wc3'], biases['bc3'])
    # Max Pooling (down-sampling)
    conv3 = maxpool2d(conv3, k=2)
    # Fully connected layer
    # Reshape conv2 output to fit fully connected layer input
    fc1 = tf.reshape(conv3, [-1, weights['wd1'].get_shape().as_list()[0]])
    fc1 = tf.add(tf.matmul(fc1, weights['wd1']), biases['bd1'])
    fc1 = tf.nn.relu(fc1)
    # Apply Dropout
    fc1 = tf.nn.dropout(fc1, dropout)
    # Output, class prediction
    out = tf.add(tf.matmul(fc1, weights['out']), biases['out'])
    return out
 
 
# Store layers weight & bias
weights = {
    # 3x3 conv, 1 input, 128 outputs
    'wc1': tf.Variable(tf.random_normal([3, 3, 1, 128])),
    # 3x3 conv, 128 inputs, 64 outputs
    'wc2': tf.Variable(tf.random_normal([3, 3, 128, 64])),
    # 3x3 conv, 64 inputs, 32 outputs
    'wc3': tf.Variable(tf.random_normal([3, 3, 64, 32])),
    # fully connected,
    'wd1': tf.Variable(tf.random_normal([6 * 6 * 32, 200])),
    # 1024 inputs, 10 outputs (class prediction)
    'out': tf.Variable(tf.random_normal([200, n_classes]))
}
 
biases = {
    'bc1': tf.Variable(tf.random_normal([128])),
    'bc2': tf.Variable(tf.random_normal([64])),
    'bc3': tf.Variable(tf.random_normal([32])),
    'bd1': tf.Variable(tf.random_normal([200])),
    'out': tf.Variable(tf.random_normal([n_classes]))
}
# Construct model
pred = conv_net(x, weights, biases, keep_prob)
# Define loss and optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)
# Evaluate model
correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
# Initializing the variables
init = tf.initialize_all_variables()
Train_ind = np.arange(train_num)
Test_ind = np.arange(test_num)

with tf.Session() as sess:
    sess.run(init)
    for epoch in range(0, train_epoch):
        Total_test_loss = 0
        Total_test_acc = 0
        for train_batch in range(0, int(train_batch_num)):
            sample_ind = Train_ind[train_batch * batch_size:(train_batch + 1) * batch_size]
            batch_x = train_x[sample_ind, :]
            batch_y = train_y[sample_ind, :]
            # Run optimization op (backprop)
            sess.run(optimizer, feed_dict={x: batch_x, y: batch_y,
                                           keep_prob: dropout})
            if train_batch % batch_size == 0:
                # Calculate loss and accuracy
                loss, acc = sess.run([cost, accuracy], feed_dict={x: batch_x,
                                                                  y: batch_y,
                                                                  keep_prob: 1.})
                print("Epoch: " + str(epoch + 1) + ", Batch: " + str(train_batch) + ", Loss= " + "{:.3f}".format(loss) + ", Training Accuracy= " + "{:.3f}".format(acc))
        
        # Calculate test loss and test accuracy
        for test_batch in range(0, int(test_batch_num)):
            sample_ind = Test_ind[test_batch * batch_size:(test_batch + 1) * batch_size]
            batch_x = test_x[sample_ind, :]
            batch_y = test_y[sample_ind, :]
            test_loss, test_acc = sess.run([cost, accuracy], feed_dict={x: batch_x, y: batch_y, keep_prob: 1.})
            Total_test_lost = Total_test_loss + test_loss
            Total_test_acc = Total_test_acc + test_acc
 
        Total_test_acc = Total_test_acc / test_batch_num
        Total_test_loss = Total_test_lost / test_batch_num
        print("Epoch: " + str(epoch + 1) + ", Test Loss= " + "{:.3f}".format(Total_test_loss) + ", Test Accuracy= " + "{:.3f}".format(Total_test_acc))

plt.subplot(2, 1, 1)
plt.ylabel('Test loss')
plt.plot(Total_test_loss, 'r')
plt.subplot(2, 1, 2)
plt.ylabel('Test Accuracy')
plt.plot(Total_test_acc, 'r')
 
print("All is well")
plt.show()


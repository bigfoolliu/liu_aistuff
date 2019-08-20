/*
Pig是由两个玩家掷6面骰子的游戏。在每一轮中，你可能掷骰或停留。
如果你掷出了1，就会失去你在这轮中的所有点数，并交由你的对手玩。 掷出的其它值都将计入你这轮的分数中。
如果你停留了，你这轮的分数就会计入你的总分中，并交由你的对手玩。
总点数先达到100的人胜出。 

score 类型存储了当前的分数与对手玩家，还有当前这一轮中累积的点数。
*/


package main

import (
	"fmt"
	"math/rand"
)


// 声明常量
const (
	win = 100  // 得到100分则赢
	gamesPerSeries = 10  // 每次模拟连续游戏的数量
)

// 声明,得分包括玩家前几轮的得分和本轮中当前玩家的得分
type score struct {
	player, opponent, thisTurn int
}


// 声明action,其将一个动作随机转换为一个分数
type action func(current score) (result score, turnIsOver bool)

// rooll函数返回模拟一次掷骰子产生的(result, turnIsOver)
func roll(s score) (score, bool) {
	outcome := rand.Intn(6) + 1  // 生成一个[1, 6]的整数
	if outcome == 1 {
		return score{s.opponent, s.player, 0}, true
	}
	return score{s.player, s.opponent, outcome + s.thisTurn}, false
}


// stay函数返回停留时候产生的结果,这一轮 thisTurn 的分数会计入该玩家的总分中，然后玩家的角色互换。
func stay(s score) (score, bool) {
	return score{s.opponent, s.player + s.thisTurn, 0}, true
}


type strategy func(score) action


// strategy 为任何给定的分数 score 返回一个动作 action
// 该策略继续掷骰直到这一轮 thisTurn 至少为 k，然后停留
func stayAtK(k int) strategy {
	return func(s score) action {
		if s.thisTurn >= k {
			return stay
		}
		return roll
	}
}


// TODO:add more from http://docscn.studygolang.com/doc/codewalk/functions/

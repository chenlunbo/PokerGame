#!/usr/bin/python
# -*- coding: UTF-8 -*-

class BowlingScorer:
    totalScore = 0
    totalTimes = 0

    def __init__(self):
        self.totalScore = 0
        self.totalTimes = 0
        self.bonusTimes = 0

    def addRecord(self, firstScore, secondScore):
        p1 = firstScore
        p2 = secondScore
        if secondScore == '-':
            p2 = 0
        if secondScore == '/':
            p2 = 10
        if firstScore == 'X':
            p1 = 10
            p2 = 0
        self.totalScore += p1 + p2
        self.totalTimes += 1
        self.bonus(firstScore, secondScore)

    def bonus(self, firstScore, secondScore):
        if self.bonusTimes > 0:
            self.bonusTimes = self.bonusTimes - 1
            self.addRecord(firstScore, secondScore)
        if firstScore == 'X' and self.totalTimes == 10:
            self.bonusTimes = 2
        if firstScore == 'X' and self.totalTimes < 10:
            self.bonusTimes = 1




    def displayCount(self):
        print("current count is " + str(self.totalTimes))

    def displayScore(self):
        print("current score is " + str(self.totalScore))

    def getScore(self):
        return self.totalScore

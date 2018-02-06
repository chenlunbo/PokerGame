#!/usr/bin/python
# -*- coding: UTF-8 -*-

class BowlingScorer:
    totalScore = 0
    totalTimes = 0

    def __init__(self):
        self.totalScore = 0
        self.totalTimes = 0

    def addRecord(self, firstScore, secondScore):
        if (secondScore == '-'):
            secondScore = 0
        if (secondScore == '/'):
            secondScore = 10
        self.totalScore += firstScore + secondScore
        self.totalTimes += 1

    def displayCount(self):
        print("current count is " + str(self.totalTimes))

    def displayScore(self):
        print("current score is " + str(self.totalScore))

    def getScore(self):
        return self.totalScore

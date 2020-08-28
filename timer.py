#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 17:06:21 2020

@author: dpaul891
"""

import time

class MyTimer:
    def __init__(self):
        self.unit = ['year', 'month', 'day', 'hour', 'minute', 'second']
        self.prompt = "not started"
        self.lasted = []
        # self.start = 0 #变量和函数名重合，变量会覆盖函数
        # self.stop = 0
        self.begin = 0
        self.end = 0
        
    def __str__(self):
        return self.prompt + 'str'
    
    def __repr__(self):
        return self.prompt + 'repr'
    
    def __add__(self, other):
        prompt = 'Total time is: '
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += str(result[index]) + self.unit[index]
        return prompt
    
    # 开始计时
    def start(self):
        self.begin = time.localtime()
        print("timer begins")
        self.prompt = 'Please run stop() to end timer firstly !'
    
    # 停止计时
    def stop(self):
        if not self.begin:
            print('Please run sratr() firstly')
        else:
            self.end = time.localtime()
            self._calc()
            print("timer stopped")
        
    # 内部方法计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = "The total time is:"
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]) + self.unit[index] + ' '
        # prepare for next turn
        self.begin = 0
        self.end = 0
            
    
    
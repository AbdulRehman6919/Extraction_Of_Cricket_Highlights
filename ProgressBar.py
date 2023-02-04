# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 08:36:46 2020

@author: Abdul Rehman
"""

import sys

class ProgressBar(object):
    DEFAULT_BAR_LENGTH = 60
    DEFAULT_CHAR_ON  = '>'
    DEFAULT_CHAR_OFF = ' '
    prog = 0

    def __init__(self, end, start=0):
        self.end    = end
        self.start  = start
        self._barLength = self.__class__.DEFAULT_BAR_LENGTH

        self.setLevel(self.start)
        self._plotted = False

    def setLevel(self, level):
        self._level = level
        if level < self.start:  self._level = self.start
        if level > self.end:    self._level = self.end

        self._ratio = float(self._level - self.start) / float(self.end - self.start)
        self._levelChars = int(self._ratio * self._barLength)

    def plotProgress(self):
        global prog
        self.prog = int(self._ratio * 100.0)
        sys.stdout.write("\r  %3i%% [%s%s]" %(
        int(self._ratio * 100.0),
        self.__class__.DEFAULT_CHAR_ON  * int(self._levelChars),
        self.__class__.DEFAULT_CHAR_OFF * int(self._barLength - self._levelChars),
        ))
        sys.stdout.flush()
        self._plotted = True

    def setAndPlot(self, level):
        oldChars = self._levelChars
        self.setLevel(level)
        if (not self._plotted) or (oldChars != self._levelChars):
            self.plotProgress()

    def __add__(self, other):
        assert type(other) in [float, int], "can only add a number"
        self.setAndPlot(self._level + other)
        return self
    def __sub__(self, other):
        return self.__add__(-other)
    def __iadd__(self, other):
        return self.__add__(other)
    def __isub__(self, other):
        return self.__add__(-other)

    def __del__(self):
        sys.stdout.write("\n")
        
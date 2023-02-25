#!-*- coding: utf-8 -*-
"""Python File Remuneration"""
import curses

import runfile


class _art2(curses.ACS_S1):
    def __init__(self):
        self.art2 = None

    def CursePanelKey(self, launch=runfile):
        self.art2 = launch.duration(time1=10, time2=10)

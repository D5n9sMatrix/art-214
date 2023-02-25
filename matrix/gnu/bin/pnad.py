#!-*- coding: utf-8 -*-
"""Python File Remuneration"""
import curses.panel


class _art3(curses.panel.new_panel):
    def __init__(self):
        self.art3 = None

    def CursePanelCookies(self, cookies=15):
        self.art3 = cookies.__eq__(x=object)
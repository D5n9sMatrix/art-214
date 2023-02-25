#!-*- coding: utf-8 -*-
"""Python File Remuneration"""
import code
import curses
import opcode
import pydoc_data


class _art4(curses.set_tabsize):
    def __init__(self):
        self.art4_latex = None
        self.art4_code = None
        self.art4_opcode = None

    def CursePanelWindow(self, window=opcode, objPdf=code, latex=pydoc_data):
        self.art4_opcode = window.__all__
        self.art4_code = objPdf.__all__
        self.art4_latex = latex
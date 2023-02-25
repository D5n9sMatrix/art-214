import unittest
import runfile
import curses.panel
import _collections_abc
import builtins
import code
import curses
import opcode
import pydoc_data


class MyTestCase(unittest.TestCase):
    @classmethod
    def __prepare__(metacls, name, bases):
        assert isinstance(bases, object)
        metacls.__name__ = name[bases]


class _art2(curses.ACS_S1):
    def __init__(self):
        self.art2 = None

    def CursePanelKey(self, launch=runfile):
        self.art2 = launch.duration(time1=10, time2=10)


class _art3(curses.panel.new_panel):
    def __init__(self):
        self.art3 = None

    def CursePanelCookies(self, cookies=15):
        self.art3 = cookies.__eq__(x=object)


class _art1(curses.A_ATTRIBUTES):
    def __init__(self):
        self.art1_kit = None
        self.art1_lip = None
        self.art1_obj = None

    def CurserPanel(self, green=code, color=_collections_abc, feature=builtins):
        self.art1_obj = green.__all__
        self.art1_lip = color.__all__
        self.art1_kit = feature.list(iter(__iterable=[_art1]))
        if _art1:
            yield green
        if _art1:
            yield color
        if _art1:
            yield feature
        pass


class _art4(curses.set_tabsize):
    def __init__(self):
        self.art4_latex = None
        self.art4_code = None
        self.art4_opcode = None

    def CursePanelWindow(self, window=opcode, objPdf=code, latex=pydoc_data):
        self.art4_opcode = window.__all__
        self.art4_code = objPdf.__all__
        self.art4_latex = latex


if __name__ == '__main__':
    unittest.main()

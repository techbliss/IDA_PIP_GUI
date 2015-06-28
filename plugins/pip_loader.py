import re
import idaapi
import idc
from idc import *
from idaapi import *
import PySide
from PySide import QtCore, QtGui
import idautils

class pork(idaapi.plugin_t):
    flags = idaapi.PLUGIN_FIX
    comment = "This is a comment"

    help = "PIP Loader"
    wanted_name = "PIP Gui"
    wanted_hotkey = ""



    def init(self):
        idaapi.msg("PIP Plugin Is Found \ Go To edit >> Plugins\n")
        return idaapi.PLUGIN_OK

    def run(self, arg):
        idaapi.msg("run() called with %d!\n" % arg)

    def term(self):
        idaapi.msg("")

    def AddMenuElements(self):
        idaapi.add_menu_item("View/", "PIP", "", 0, self.Toast, ())




    def run(self, arg = 0):
        idaapi.msg("PIP GUI is Found\nAfter its Loaded\nFind It Under View Menu")

        self.AddMenuElements()

    def Toast(self):
        g = globals()
        idahome = idaapi.idadir("QTApps\\Pips")
        IDAPython_ExecScript(idahome +  "\\pips.py", g)



def PLUGIN_ENTRY():
    return pork()
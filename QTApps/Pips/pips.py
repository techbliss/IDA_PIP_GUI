# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pip.ui'

# Created: Storm Shoadow http://techbliss.org


from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName(_fromUtf8("TabWidget"))
        TabWidget.resize(833, 939)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/ico/mind.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TabWidget.setWindowIcon(icon)
        TabWidget.setStyleSheet(_fromUtf8("QWidget { \n"
"    background-color: #363636;\n"
"    color: #ddd;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: #2d2d2d;\n"
"    border: 1px solid #363636;\n"
"}\n"
"\n"
"QMenuBar, QMenuBar::item {\n"
"    background-color: #444444;\n"
"    color: #ddd;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #474747;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QLineEdit:hover, QLineEdit:focus {\n"
"    border: 1px solid #00aaaa;    \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #555555, stop: 1 #444444);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #777777;\n"
"}\n"
"\n"
"QTreeView::item {\n"
"    font-size: 8px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #444;\n"
"    border-left: 3px solid #666;\n"
"\n"
"}\n"
"\n"
"QTableView {\n"
"    border: 1px solid #474747;\n"
"}\n"
"\n"
"QTableView {\n"
"    background-color: #2d2d2d;\n"
"}\n"
"\n"
"IDAView, hexview_t, CustomIDAMemo {\n"
"    font-family: \"Consolas\";\n"
"    font-size: 9pt;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar {\n"
"    background-color: #363636;\n"
"    width: 20px;\n"
"    margin: 0 0 0 0;\n"
"}\n"
"\n"
"QScrollBar::sub-line, QScrollBar::add-line {\n"
"    background: none;\n"
"}\n"
"\n"
"/*\n"
"QScrollBar:horizontal {\n"
"    padding: 0 20px 0 20px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    padding: 20px 0 20px 0;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    image: url(%down-arrow.png%);\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"    width: 20px;\n"
"}*/\n"
"\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background-color: #585858;\n"
"    margin: 3px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QToolBar {\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 1px solid #077;\n"
"    text-align: center;\n"
"    min-height: 20px;\n"
"    min-width: 50px;\n"
"    \n"
"    padding: 0 6px 0 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 1px solid #0aa;\n"
"}\n"
"\n"
"QPushButton::text {\n"
"    background-color: red;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid #474747;\n"
"}\n"
"\n"
"GraphQObject {\n"
"    background-color: red;\n"
"    padding: 100px;\n"
"}\n"
"\n"
"ChooserContainer {\n"
"    border: 1px solid green;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 6px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"min-width: 80px;\n"
"}\n"
" \n"
"QPushButton:hover {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb);\n"
"}\n"
" \n"
"QPushButton:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}\n"
""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.textEdit_install = QtGui.QTextEdit(self.tab)
        self.textEdit_install.setGeometry(QtCore.QRect(0, 0, 681, 451))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit_install.setFont(font)
        self.textEdit_install.setObjectName(_fromUtf8("textEdit_install"))
        self.search_btr = QtGui.QPushButton(self.tab)
        self.search_btr.setGeometry(QtCore.QRect(710, 20, 94, 34))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setBold(False)
        font.setWeight(50)
        self.search_btr.setFont(font)
        self.search_btr.setObjectName(_fromUtf8("search_btr"))
        self.install_pipbtr = QtGui.QPushButton(self.tab)
        self.install_pipbtr.setGeometry(QtCore.QRect(710, 70, 94, 34))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setBold(False)
        font.setWeight(50)
        self.install_pipbtr.setFont(font)
        self.install_pipbtr.setObjectName(_fromUtf8("install_pipbtr"))
        self.textEdit_helpinstall = QtGui.QTextEdit(self.tab)
        self.textEdit_helpinstall.setGeometry(QtCore.QRect(0, 480, 701, 421))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Black"))
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_helpinstall.setFont(font)
        self.textEdit_helpinstall.setObjectName(_fromUtf8("textEdit_helpinstall"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(0, 450, 821, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.install_commandbtr = QtGui.QPushButton(self.tab)
        self.install_commandbtr.setGeometry(QtCore.QRect(710, 120, 94, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setBold(False)
        font.setWeight(50)
        self.install_commandbtr.setFont(font)
        self.install_commandbtr.setObjectName(_fromUtf8("install_commandbtr"))
        self.install_box = QtGui.QTextEdit(self.tab)
        self.install_box.setGeometry(QtCore.QRect(680, 210, 141, 31))
        self.install_box.setObjectName(_fromUtf8("install_box"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(700, 190, 131, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        TabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(0, 450, 821, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textEdit_helplist = QtGui.QTextEdit(self.tab_2)
        self.textEdit_helplist.setGeometry(QtCore.QRect(0, 480, 701, 431))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        self.textEdit_helplist.setFont(font)
        self.textEdit_helplist.setObjectName(_fromUtf8("textEdit_helplist"))
        self.textEdit_list = QtGui.QTextEdit(self.tab_2)
        self.textEdit_list.setGeometry(QtCore.QRect(3, 0, 681, 451))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(10)
        self.textEdit_list.setFont(font)
        self.textEdit_list.setObjectName(_fromUtf8("textEdit_list"))
        self.List_packagebtr = QtGui.QPushButton(self.tab_2)
        self.List_packagebtr.setGeometry(QtCore.QRect(710, 20, 94, 34))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setItalic(False)
        self.List_packagebtr.setFont(font)
        self.List_packagebtr.setObjectName(_fromUtf8("List_packagebtr"))
        self.List_commandbtr = QtGui.QPushButton(self.tab_2)
        self.List_commandbtr.setGeometry(QtCore.QRect(710, 70, 94, 34))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setItalic(False)
        self.List_commandbtr.setFont(font)
        self.List_commandbtr.setObjectName(_fromUtf8("List_commandbtr"))
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(700, 190, 131, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.install_box_2 = QtGui.QTextEdit(self.tab_2)
        self.install_box_2.setGeometry(QtCore.QRect(680, 210, 141, 31))
        self.install_box_2.setObjectName(_fromUtf8("install_box_2"))
        TabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.textEdit_uninstall = QtGui.QTextEdit(self.tab1)
        self.textEdit_uninstall.setGeometry(QtCore.QRect(-7, 0, 691, 451))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(10)
        self.textEdit_uninstall.setFont(font)
        self.textEdit_uninstall.setObjectName(_fromUtf8("textEdit_uninstall"))
        self.Uninstall_btr = QtGui.QPushButton(self.tab1)
        self.Uninstall_btr.setGeometry(QtCore.QRect(710, 20, 94, 34))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setBold(False)
        font.setWeight(50)
        self.Uninstall_btr.setFont(font)
        self.Uninstall_btr.setObjectName(_fromUtf8("Uninstall_btr"))
        self.textEdit_helpuninstall = QtGui.QTextEdit(self.tab1)
        self.textEdit_helpuninstall.setGeometry(QtCore.QRect(0, 480, 701, 431))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        self.textEdit_helpuninstall.setFont(font)
        self.textEdit_helpuninstall.setObjectName(_fromUtf8("textEdit_helpuninstall"))
        self.label_2 = QtGui.QLabel(self.tab1)
        self.label_2.setGeometry(QtCore.QRect(0, 450, 821, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.Uninstall_commandbtr = QtGui.QPushButton(self.tab1)
        self.Uninstall_commandbtr.setGeometry(QtCore.QRect(710, 70, 94, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setBold(False)
        font.setWeight(50)
        self.Uninstall_commandbtr.setFont(font)
        self.Uninstall_commandbtr.setObjectName(_fromUtf8("Uninstall_commandbtr"))
        self.label_8 = QtGui.QLabel(self.tab1)
        self.label_8.setGeometry(QtCore.QRect(700, 190, 131, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.uninstall_box = QtGui.QTextEdit(self.tab1)
        self.uninstall_box.setGeometry(QtCore.QRect(680, 210, 141, 31))
        self.uninstall_box.setObjectName(_fromUtf8("uninstall_box"))
        TabWidget.addTab(self.tab1, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.textEdit_helpshow = QtGui.QTextEdit(self.tab_3)
        self.textEdit_helpshow.setGeometry(QtCore.QRect(0, 480, 701, 431))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        self.textEdit_helpshow.setFont(font)
        self.textEdit_helpshow.setObjectName(_fromUtf8("textEdit_helpshow"))
        self.textEdit_show = QtGui.QTextEdit(self.tab_3)
        self.textEdit_show.setGeometry(QtCore.QRect(3, 0, 681, 451))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(10)
        self.textEdit_show.setFont(font)
        self.textEdit_show.setObjectName(_fromUtf8("textEdit_show"))
        self.Show_packagebtr = QtGui.QPushButton(self.tab_3)
        self.Show_packagebtr.setGeometry(QtCore.QRect(710, 20, 94, 34))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        self.Show_packagebtr.setFont(font)
        self.Show_packagebtr.setObjectName(_fromUtf8("Show_packagebtr"))
        self.Show_commandbtr = QtGui.QPushButton(self.tab_3)
        self.Show_commandbtr.setGeometry(QtCore.QRect(710, 70, 94, 34))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        self.Show_commandbtr.setFont(font)
        self.Show_commandbtr.setObjectName(_fromUtf8("Show_commandbtr"))
        self.label_4 = QtGui.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(0, 450, 821, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_10 = QtGui.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(700, 190, 131, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.show_box = QtGui.QTextEdit(self.tab_3)
        self.show_box.setGeometry(QtCore.QRect(680, 210, 141, 31))
        self.show_box.setObjectName(_fromUtf8("show_box"))
        TabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.bt_Intieets = QtGui.QPushButton(self.tab_4)
        self.bt_Intieets.setGeometry(QtCore.QRect(170, 80, 111, 41))
        self.bt_Intieets.setObjectName(_fromUtf8("bt_Intieets"))
        self.label_5 = QtGui.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(40, 30, 111, 51))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.bt_Githubs = QtGui.QPushButton(self.tab_4)
        self.bt_Githubs.setGeometry(QtCore.QRect(170, 32, 111, 41))
        self.bt_Githubs.setObjectName(_fromUtf8("bt_Githubs"))
        self.label_6 = QtGui.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(40, 90, 111, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        TabWidget.addTab(self.tab_4, _fromUtf8(""))

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(_translate("TabWidget", "PIP Gui", None))
        self.search_btr.setToolTip(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://pip.pypa.io/en/latest/reference/pip_search.html#id2\"><span style=\" font-size:xx-large; font-weight:600; text-decoration: underline; color:#0000ff;\">pip search</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"contents\"></a>Contents</p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\"\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id2\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_search.html#pip-search\"><span style=\" text-decoration: underline; color:#0000ff;\">p</span></a><span style=\" text-decoration: underline; color:#0000ff;\">ip search</span></li></ul>\n"
"<ul type=\"circle\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\"><li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id3\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_search.html#usage\"><span style=\" text-decoration: underline; color:#0000ff;\">U</span></a><span style=\" text-decoration: underline; color:#0000ff;\">sage</span></li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id4\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_search.html#description\"><span style=\" text-decoration: underline; color:#0000ff;\">D</span></a><span style=\" text-decoration: underline; color:#0000ff;\">escription</span></li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id5\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_search.html#options\"><span style=\" text-decoration: underline; color:#0000ff;\">O</span></a><span style=\" text-decoration: underline; color:#0000ff;\">ptions</span></li>\n"
"<li style=\"\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id6\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_search.html#examples\"><span style=\" text-decoration: underline; color:#0000ff;\">E</span></a><span style=\" text-decoration: underline; color:#0000ff;\">xamples</span></li></ul>\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"usage\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_search.html#id3\"><span style=\" font-size:x-large; font-weight:600; text-decoration: underline; color:#0000ff;\">U</span></a><span style=\" font-size:x-large; font-weight:600; text-decoration: underline; color:#0000ff;\">sage</span></p>\n"
"<pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">pip search [options] &lt;query&gt;</span></pre>\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"description\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_search.html#id4\"><span style=\" font-size:x-large; font-weight:600; text-decoration: underline; color:#0000ff;\">D</span></a><span style=\" font-size:x-large; font-weight:600; text-decoration: underline; color:#0000ff;\">escription</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Search for PyPI packages whose name or summary contains &lt;query&gt;.</p>\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"options\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_search.html#id5\"><span style=\" font-size:x-large; font-weight:600; text-decoration: underline; color:#0000ff;\">O</span></a><span style=\" font-size:x-large; font-weight:600; text-decoration: underline; color:#0000ff;\">ptions</span></p>\n"
"<p style=\" margin-top:8px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"search-index\"></a><span style=\" font-family:\'Courier New,courier\';\">-</span><span style=\" font-family:\'Courier New,courier\';\">-index</span><span style=\" font-family:\'Courier New,courier\';\"> &lt;url&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Base URL of Python Package Index (default <a href=\"https://pypi.python.org/pypi\"><span style=\" text-decoration: underline; color:#0000ff;\">https://pypi.python.org/pypi</span></a>) </p>\n"
"<p style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"examples\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_search.html#id6\"><span style=\" font-size:x-large; font-weight:600; text-decoration: underline; color:#0000ff;\">E</span></a><span style=\" font-size:x-large; font-weight:600; text-decoration: underline; color:#0000ff;\">xamples</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\"\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Search for &quot;peppercorn&quot;</li></ol>\n"
"<pre style=\" margin-top:12px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">$ pip search peppercorn</span></pre>\n"
"<pre style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">pepperedform    - Helpers for using peppercorn with formprocess.</span></pre>\n"
"<pre style=\" margin-top:0px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">peppercorn      - A library for converting a token stream into [...]</span></pre></body></html>", None))
        self.search_btr.setText(_translate("TabWidget", "Search PIP", None))
        self.install_pipbtr.setToolTip(_translate("TabWidget", "<html><head/><body><p>Search PIP<br/>Then copy paste and install.</p></body></html>", None))
        self.install_pipbtr.setText(_translate("TabWidget", "Install PIP", None))
        self.textEdit_helpinstall.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto Black\'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id14\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">pip install</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"contents\"></a><span style=\" font-size:16pt; font-weight:400;\">C</span><span style=\" font-size:16pt; font-weight:400;\">ontents</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id14\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#pip-install\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">p</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">ip install</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id15\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#usage\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">U</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">sage</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id16\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#description\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">D</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">escription</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id17\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#overview\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">O</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">verview</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id18\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#installation-order\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">I</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">nstallation Order</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id19\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#requirements-file-format\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">R</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">equirements File Format</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id20\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#requirement-specifiers\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">R</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">equirement Specifiers</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id21\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#per-requirement-overrides\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">P</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">er-requirement Overrides</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id22\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#pre-release-versions\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">P</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">re-release Versions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id23\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#externally-hosted-files\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">E</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">xternally Hosted Files</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id24\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#vcs-support\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">V</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">CS Support</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id25\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#git\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">G</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">it</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id26\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#mercurial\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">M</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">ercurial</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id27\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#subversion\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">S</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">ubversion</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id28\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#bazaar\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">B</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">azaar</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id29\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#finding-packages\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">F</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">inding Packages</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id30\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#ssl-certificate-verification\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">S</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">SL Certificate Verification</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id31\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#caching\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">C</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">aching</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id32\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#wheel-cache\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">W</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">heel cache</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id33\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#hash-verification\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">H</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">ash Verification</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id34\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#editable-installs\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">&quot;</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">Editable&quot; Installs</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id35\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#controlling-setup-requires\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">C</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">ontrolling setup_requires</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id36\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#build-system-interface\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">B</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">uild System Interface</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id37\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#options\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">O</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">ptions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id38\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#examples\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">E</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">xamples</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"usage\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id15\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">U</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">sage</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">pip install [options] &lt;requirement specifier&gt; [package-index-options] ...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">pip install [options] -r &lt;requirements file&gt; [package-index-options] ...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">pip install [options] [-e] &lt;vcs project url&gt; ...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">pip install [options] [-e] &lt;local project path&gt; ...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">pip install [options] &lt;archive url/path&gt; ...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"description\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id16\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">D</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">escription</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Install packages from:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PyPI (and other indexes) using requirement specifiers.</li>\n"
"<li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">VCS project urls.</li>\n"
"<li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Local project directories.</li>\n"
"<li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Local or remote source archives.</li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">pip also supports installing from &quot;requirements files&quot;, which provide an easy way to specify a whole environment to be installed.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"overview\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id17\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">O</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">verview</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Pip install has several stages:</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Resolve dependencies. What will be installed is determined here.</li>\n"
"<li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Build wheels. All the dependencies that can be are built into wheels.</li>\n"
"<li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Install the packages (and uninstall anything being upgraded/replaced).</li></ol>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"installation-order\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id18\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">I</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">nstallation Order</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">As of v6.1.0, pip installs dependencies before their dependents, i.e. in &quot;topological order&quot;. This is the only commitment pip currently makes related to order. While it may be coincidentally true that pip will install things in the order of the install arguments or in the order of the items in a requirements file, this is not a promise.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">In the event of a dependency cycle (aka &quot;circular dependency&quot;), the current implementation (which might possibly change later) has it such that the first encountered member of the cycle is installed last.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">For instance, if quux depends on foo which depends on bar which depends on baz, which depends on foo:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">pip install quux</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">Installing collected packages baz, bar, foo, quux</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">pip install bar</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">Installing collected packages foo, baz, bar</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Prior to v6.1.0, pip made no commitments about install order.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">The decision to install topologically is based on the principle that installations should proceed in a way that leaves the environment usable at each step. This has two main practical benefits:</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Concurrent use of the environment during the install is more likely to work.</li>\n"
"<li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A failed install is less likely to leave a broken environment. Although pip would like to support failure rollbacks eventually, in the mean time, this is an improvement.</li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Although the new install order is not intended to replace (and does not replace) the use of </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">setup_requires</span><span style=\" font-size:16pt; font-weight:400;\"> to declare build dependencies, it may help certain projects install from sdist (that might previously fail) that fit the following profile:</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">They have build dependencies that are also declared as install dependencies using <span style=\" font-family:\'Courier New,courier\';\">install_requires</span>.</li>\n"
"<li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">python setup.py egg_info</span> works without their build dependencies being installed.</li>\n"
"<li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For whatever reason, they don\'t or won\'t declare their build dependencies using <span style=\" font-family:\'Courier New,courier\';\">setup_requires</span>.</li></ol>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"requirements-file-format\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id19\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">R</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">equirements File Format</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Each line of the requirements file indicates something to be installed, and like arguments to </span><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#pip-install\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">pip install</span></a><span style=\" font-size:16pt; font-weight:400;\">, the following forms are supported:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[[--option]...]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">&lt;requirement specifier&gt; [; markers] [[--option]...]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">&lt;archive url/path&gt;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] &lt;local project path&gt;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] &lt;vcs project url&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">For details on requirement specifiers, see </span><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#requirement-specifiers\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">Requirement Specifiers</span></a><span style=\" font-size:16pt; font-weight:400;\">.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">See the </span><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#pip-install-examples\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">pip install Examples</span></a><span style=\" font-size:16pt; font-weight:400;\"> for examples of all these forms.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">A line that begins with </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">#</span><span style=\" font-size:16pt; font-weight:400;\"> is treated as a comment and ignored. Whitespace followed by a </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">#</span><span style=\" font-size:16pt; font-weight:400;\"> causes the </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">#</span><span style=\" font-size:16pt; font-weight:400;\"> and the remainder of the line to be treated as a comment.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">A line ending in an unescaped </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">\\</span><span style=\" font-size:16pt; font-weight:400;\"> is treated as a line continuation and the newline following it is effectively ignored.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Additionally, the following Package Index Options are supported:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://pip.pypa.io/en/latest/reference/pip_wheel.html#index-url\"><span style=\" text-decoration: underline; color:#ff0000;\">-i, --index-url</span></a></li>\n"
"<li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://pip.pypa.io/en/latest/reference/pip_wheel.html#extra-index-url\"><span style=\" text-decoration: underline; color:#ff0000;\">--extra-index-url</span></a></li>\n"
"<li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://pip.pypa.io/en/latest/reference/pip_wheel.html#no-index\"><span style=\" text-decoration: underline; color:#ff0000;\">--no-index</span></a></li>\n"
"<li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://pip.pypa.io/en/latest/reference/pip_wheel.html#find-links\"><span style=\" text-decoration: underline; color:#ff0000;\">-f, --find-links</span></a></li>\n"
"<li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://pip.pypa.io/en/latest/reference/pip_wheel.html#allow-external\"><span style=\" text-decoration: underline; color:#ff0000;\">--allow-external</span></a></li>\n"
"<li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://pip.pypa.io/en/latest/reference/pip_wheel.html#allow-external\"><span style=\" text-decoration: underline; color:#ff0000;\">--allow-all-external</span></a></li>\n"
"<li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://pip.pypa.io/en/latest/reference/pip_wheel.html#allow-unverified\"><span style=\" text-decoration: underline; color:#ff0000;\">--allow-unverified</span></a></li>\n"
"<li style=\" font-size:16pt; font-weight:400; color:#ff0000;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#install-no-binary\"><span style=\" text-decoration: underline; color:#0000ff;\">--no-binary</span></a></li>\n"
"<li style=\" font-size:16pt; font-weight:400; color:#ff0000;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#install-only-binary\"><span style=\" text-decoration: underline; color:#0000ff;\">--only-binary</span></a></li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">For example, to specify </span><a href=\"https://pip.pypa.io/en/latest/reference/pip_wheel.html#no-index\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">--no-index</span></a><span style=\" font-size:16pt; font-weight:400;\"> and 2 </span><a href=\"https://pip.pypa.io/en/latest/reference/pip_wheel.html#find-links\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">--find-links</span></a><span style=\" font-size:16pt; font-weight:400;\"> locations:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">--no-index</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">--find-links /my/local/archives</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">--find-links http://some.archives.com/archives</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Lastly, if you wish, you can refer to other requirements files, like this:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-r more_requirements.txt</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"requirement-specifiers\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id20\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">R</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">equirement Specifiers</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">pip supports installing from a package index using a </span><a href=\"https://packaging.python.org/en/latest/glossary.html#term-requirement-specifier\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">requirement specifier</span></a><span style=\" font-size:16pt; font-weight:400;\">. Generally speaking, a requirement specifier is composed of a project name followed by optional </span><a href=\"https://packaging.python.org/en/latest/glossary.html#term-version-specifier\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">version</span></a><a href=\"https://packaging.python.org/en/latest/glossary.html#term-version-specifier\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#0000ff;\"> </span></a><a href=\"https://packaging.python.org/en/latest/glossary.html#term-version-specifier\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">specifiers</span></a><span style=\" font-size:16pt; font-weight:400; color:#ff0000;\">. </span><a href=\"https://pypa.io/en/latest/peps/#pep440s\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">PEP440</span></a><span style=\" font-size:16pt; font-weight:400;\"> contains a </span><a href=\"https://www.python.org/dev/peps/pep-0440/#version-specifiers\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">full specification</span></a><span style=\" font-size:16pt; font-weight:400;\"> of the currently supported specifiers.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Some examples:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">SomeProject</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">SomeProject == 1.3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">SomeProject &gt;=1.2,&lt;.2.0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">SomeProject[foo, bar]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">SomeProject~=1.4.2</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Since version 6.0, pip also supports specifers containing </span><a href=\"https://www.python.org/dev/peps/pep-0426/#environment-markers\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">environment markers</span></a><span style=\" font-size:16pt; font-weight:400;\"> like so:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">SomeProject ==5.4 ; python_version &lt; \'2.7\'</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">SomeProject; sys.platform == \'win32\'</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Environment markers are supported in the command line and in requirements files.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Note</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Use quotes around specifiers in the shell when using </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">&gt;</span><span style=\" font-size:16pt; font-weight:400;\">, </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">&lt;</span><span style=\" font-size:16pt; font-weight:400;\">, or when using environment markers. Don\'t use quotes in requirement files. </span><a name=\"id4\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id13\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">[</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">1]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"per-requirement-overrides\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id21\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">P</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">er-requirement Overrides</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Since version 7.0 pip supports controlling the command line options given to </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">setup.py</span><span style=\" font-size:16pt; font-weight:400;\"> via requirements files. This disables the use of wheels (cached or otherwise) for that package, as </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">setup.py</span><span style=\" font-size:16pt; font-weight:400;\"> does not exist for wheels.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">The </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">--global-option</span><span style=\" font-size:16pt; font-weight:400;\"> and </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">--install-option</span><span style=\" font-size:16pt; font-weight:400;\"> options are used to pass options to </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">setup.py</span><span style=\" font-size:16pt; font-weight:400;\">. For example:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">FooProject &gt;= 1.2 --global-option=&quot;--no-user-cfg&quot; \\</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">                  --install-option=&quot;--prefix=\'/usr/local\'&quot; \\</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">                  --install-option=&quot;--no-compile&quot;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">The above translates roughly into running FooProject\'s </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">setup.py</span><span style=\" font-size:16pt; font-weight:400;\"> script as:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">python setup.py --no-user-cfg install --prefix=\'/usr/local\' --no-compile</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Note that the only way of giving more than one option to </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">setup.py</span><span style=\" font-size:16pt; font-weight:400;\"> is through multiple </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">--global-option</span><span style=\" font-size:16pt; font-weight:400;\"> and </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">--install-option</span><span style=\" font-size:16pt; font-weight:400;\"> options, as shown in the example above. The value of each option is passed as a single argument to the </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">setup.py</span><span style=\" font-size:16pt; font-weight:400;\"> script. Therefore, a line such as the following is invalid and would result in an installation error.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\"># Invalid. Please use \'--install-option\' twice as shown above.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">FooProject &gt;= 1.2 --install-option=&quot;--prefix=/usr/local --no-compile&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"pre-release-versions\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id22\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">P</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">re-release Versions</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Starting with v1.4, pip will only install stable versions as specified by </span><a href=\"http://www.python.org/dev/peps/pep-0426\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">PEP426</span></a><span style=\" font-size:16pt; font-weight:400;\"> by default. If a version cannot be parsed as a compliant </span><a href=\"http://www.python.org/dev/peps/pep-0426\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">PEP426</span></a><span style=\" font-size:16pt; font-weight:400;\"> version then it is assumed to be a pre-release.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">If a Requirement specifier includes a pre-release or development version (e.g. </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">&gt;=0.0.dev0</span><span style=\" font-size:16pt; font-weight:400;\">) then pip will allow pre-release and development versions for that requirement. This does not include the != flag.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">The </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">pip install</span><span style=\" font-size:16pt; font-weight:400;\"> command also supports a </span><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#install-pre\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">--pre</span></a><span style=\" font-size:16pt; font-weight:400;\"> flag that will enable installing pre-releases and development releases.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"externally-hosted-files\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id23\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">E</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">xternally Hosted Files</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Starting with v1.4, pip will warn about installing any file that does not come from the primary index. As of version 1.5, pip defaults to ignoring these files unless asked to consider them.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">The </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">pip install</span><span style=\" font-size:16pt; font-weight:400;\"> command supports a </span><a href=\"https://pip.pypa.io/en/latest/reference/pip_wheel.html#allow-external\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">--allow-external PROJECT</span></a><span style=\" font-size:16pt; font-weight:400;\"> option that will enable installing links that are linked directly from the simple index but to an external host that also have a supported hash fragment. Externally hosted files for all projects may be enabled using the </span><a href=\"https://pip.pypa.io/en/latest/reference/pip_wheel.html#allow-all-external\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">--allow-all-external</span></a><span style=\" font-size:16pt; font-weight:400;\"> flag to the </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">pip install</span><span style=\" font-size:16pt; font-weight:400;\"> command.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">The </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">pip install</span><span style=\" font-size:16pt; font-weight:400;\"> command also supports a </span><a href=\"https://pip.pypa.io/en/latest/reference/pip_wheel.html#allow-unverified\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">--allow-unverified PROJECT</span></a><span style=\" font-size:16pt; font-weight:400;\"> option that will enable installing insecurely linked files. These are either directly linked (as above) files without a hash, or files that are linked from either the home page or the download url of a package.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">These options can be used in a requirements file. Assuming some fictional </span><span style=\" font-size:16pt; font-weight:400; font-style:italic;\">ExternalPackage</span><span style=\" font-size:16pt; font-weight:400;\"> that is hosted external and unverified, then your requirements file would be like so:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">--allow-external ExternalPackage</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">--allow-unverified ExternalPackage</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">ExternalPackage</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"vcs-support\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id24\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">V</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">CS Support</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">pip supports installing from Git, Mercurial, Subversion and Bazaar, and detects the type of VCS using url prefixes: &quot;git+&quot;, &quot;hg+&quot;, &quot;bzr+&quot;, &quot;svn+&quot;.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">pip requires a working VCS command on your path: git, hg, svn, or bzr.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">VCS projects can be installed in </span><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#editable-installs\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">editable mode</span></a><span style=\" font-size:16pt; font-weight:400;\"> (using the </span><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#install-editable\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">--editable</span></a><span style=\" font-size:16pt; font-weight:400;\"> option) or not.</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For editable installs, the clone location by default is &quot;&lt;venv path&gt;/src/SomeProject&quot; in virtual environments, and &quot;&lt;cwd&gt;/src/SomeProject&quot; for global installs. The <a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#install-src\"><span style=\" text-decoration: underline; color:#ff0000;\">--src</span></a> option can be used to modify this location.</li>\n"
"<li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For non-editable installs, the project is built locally in a temp dir and then installed normally.</li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">The &quot;project name&quot; component of the url suffix &quot;egg=&lt;project name&gt;-&lt;version&gt;&quot; is used by pip in its dependency logic to identify the project prior to pip downloading and analyzing the metadata. The optional &quot;version&quot; component of the egg name is not functionally important. It merely provides a human-readable clue as to what version is in use.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"git\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id25\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">G</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">it</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">pip currently supports cloning over </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">git</span><span style=\" font-size:16pt; font-weight:400;\">, </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">git+https</span><span style=\" font-size:16pt; font-weight:400;\"> and </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">git+ssh</span><span style=\" font-size:16pt; font-weight:400;\">:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Here are the supported forms:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] git+git://git.myproject.org/MyProject#egg=MyProject</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] git+https://git.myproject.org/MyProject#egg=MyProject</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] git+ssh://git.myproject.org/MyProject#egg=MyProject</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-e git+git@git.myproject.org:MyProject#egg=MyProject</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Passing branch names, a commit hash or a tag name is possible like so:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] git://git.myproject.org/MyProject.git@master#egg=MyProject</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] git://git.myproject.org/MyProject.git@v1.0#egg=MyProject</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] git://git.myproject.org/MyProject.git@da39a3ee5e6b4b0d3255bfef95601890afd80709#egg=MyProject</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"mercurial\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id26\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">M</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">ercurial</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">The supported schemes are: </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">hg+http</span><span style=\" font-size:16pt; font-weight:400;\">, </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">hg+https</span><span style=\" font-size:16pt; font-weight:400;\">, </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">hg+static-http</span><span style=\" font-size:16pt; font-weight:400;\"> and </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">hg+ssh</span><span style=\" font-size:16pt; font-weight:400;\">.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Here are the supported forms:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] hg+http://hg.myproject.org/MyProject#egg=MyProject</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] hg+https://hg.myproject.org/MyProject#egg=MyProject</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] hg+ssh://hg.myproject.org/MyProject#egg=MyProject</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">You can also specify a revision number, a revision hash, a tag name or a local branch name like so:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] hg+http://hg.myproject.org/MyProject@da39a3ee5e6b#egg=MyProject</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] hg+http://hg.myproject.org/MyProject@2019#egg=MyProject</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] hg+http://hg.myproject.org/MyProject@v1.0#egg=MyProject</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] hg+http://hg.myproject.org/MyProject@special_feature#egg=MyProject</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"subversion\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id27\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">S</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">ubversion</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">pip supports the URL schemes </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">svn</span><span style=\" font-size:16pt; font-weight:400;\">, </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">svn+svn</span><span style=\" font-size:16pt; font-weight:400;\">, </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">svn+http</span><span style=\" font-size:16pt; font-weight:400;\">, </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">svn+https</span><span style=\" font-size:16pt; font-weight:400;\">, </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">svn+ssh</span><span style=\" font-size:16pt; font-weight:400;\">.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">You can also give specific revisions to an SVN URL, like so:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] svn+svn://svn.myproject.org/svn/MyProject#egg=MyProject</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] svn+http://svn.myproject.org/svn/MyProject/trunk@2019#egg=MyProject</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">which will check out revision 2019. </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">@{20080101}</span><span style=\" font-size:16pt; font-weight:400;\"> would also check out the revision from 2008-01-01. You can only check out specific revisions using </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-e svn+...</span><span style=\" font-size:16pt; font-weight:400;\">.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"bazaar\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id28\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">B</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">azaar</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">pip supports Bazaar using the </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">bzr+http</span><span style=\" font-size:16pt; font-weight:400;\">, </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">bzr+https</span><span style=\" font-size:16pt; font-weight:400;\">, </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">bzr+ssh</span><span style=\" font-size:16pt; font-weight:400;\">, </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">bzr+sftp</span><span style=\" font-size:16pt; font-weight:400;\">, </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">bzr+ftp</span><span style=\" font-size:16pt; font-weight:400;\"> and </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">bzr+lp</span><span style=\" font-size:16pt; font-weight:400;\"> schemes.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Here are the supported forms:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] bzr+http://bzr.myproject.org/MyProject/trunk#egg=MyProject</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] bzr+sftp://user@myproject.org/MyProject/trunk#egg=MyProject</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] bzr+ssh://user@myproject.org/MyProject/trunk#egg=MyProject</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] bzr+ftp://user@myproject.org/MyProject/trunk#egg=MyProject</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] bzr+lp:MyProject#egg=MyProject</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Tags or revisions can be installed like so:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] bzr+https://bzr.myproject.org/MyProject/trunk@2019#egg=MyProject</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[-e] bzr+http://bzr.myproject.org/MyProject/trunk@v1.0#egg=MyProject</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"finding-packages\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id29\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">F</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">inding Packages</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">pip searches for packages on </span><a href=\"http://pypi.python.org/pypi/\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">PyPI</span></a><span style=\" font-size:16pt; font-weight:400;\"> using the </span><a href=\"http://pypi.python.org/simple\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">http simple interface</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">pip offers a number of Package Index Options for modifying how packages are found.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">See the </span><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#pip-install-examples\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">pip install Examples</span></a><span style=\" font-size:16pt; font-weight:400;\">.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"ssl-certificate-verification\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id30\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">S</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">SL Certificate Verification</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Starting with v1.3, pip provides SSL certificate verification over https, for the purpose of providing secure, certified downloads from PyPI.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"caching\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id31\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">C</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">aching</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Starting with v6.0, pip provides an on by default cache which functions similarly to that of a web browser. While the cache is on by default and is designed do the right thing by default you can disable the cache and always access PyPI by utilizing the </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">--no-cache-dir</span><span style=\" font-size:16pt; font-weight:400;\"> option.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">When making any HTTP request pip will first check it\'s local cache to determine if it has a suitable response stored for that request which has not expired. If it does then it simply returns that response and doesn\'t make the request.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">If it has a response stored, but it has expired, then it will attempt to make a conditional request to refresh the cache which will either return an empty response telling pip to simply use the cached item (and refresh the expiration timer) or it will return a whole new response which pip can then store in the cache.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">When storing items in the cache pip will respect the </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">CacheControl</span><span style=\" font-size:16pt; font-weight:400;\"> header if it exists, or it will fall back to the </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">Expires</span><span style=\" font-size:16pt; font-weight:400;\"> header if that exists. This allows pip to function as a browser would, and allows the index server to communicate to pip how long it is reasonable to cache any particular item.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">While this cache attempts to minimize network activity, it does not prevent network access all together. If you want a fast/local install solution that circumvents accessing PyPI, see </span><a href=\"https://pip.pypa.io/en/latest/user_guide.html#fast-local-installs\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">Fast &amp; Local Installs</span></a><span style=\" font-size:16pt; font-weight:400;\">.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">The default location for the cache directory depends on the Operating System:</span></p>\n"
"<p style=\" margin-top:8px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Unix</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">~/.cache/pip</span><span style=\" font-size:16pt; font-weight:400;\"> and it respects the </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">XDG_CACHE_HOME</span><span style=\" font-size:16pt; font-weight:400;\"> directory.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">OS X</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">~/Library/Caches/pip</span><span style=\" font-size:16pt; font-weight:400;\">.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Windows</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:8px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">&lt;CSIDL_LOCAL_APPDATA&gt;\\pip\\Cache</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"wheel-cache\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id32\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">W</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">heel cache</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Pip will read from the subdirectory </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">wheels</span><span style=\" font-size:16pt; font-weight:400;\"> within the pip cache dir and use any packages found there. This is disabled via the same </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">no-cache-dir</span><span style=\" font-size:16pt; font-weight:400;\"> option that disables the HTTP cache. The internal structure of that cache is not part of the Pip API. As of 7.0 pip uses a subdirectory per sdist that wheels were built from, and wheels within that subdirectory.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Pip attempts to choose the best wheels from those built in preference to building a new wheel. Note that this means when a package has both optional C extensions and builds </span><span style=\" font-size:16pt; font-weight:400; font-style:italic;\">py</span><span style=\" font-size:16pt; font-weight:400;\"> tagged wheels when the C extension can\'t be built that pip will not attempt to build a better wheel for Python\'s that would have supported it, once any generic wheel is built. To correct this, make sure that the wheel\'s are built with Python specific tags - e.g. pp on Pypy.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">When no wheels are found for an sdist, pip will attempt to build a wheel automatically and insert it into the wheel cache.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"hash-verification\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id33\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#0000ff;\">H</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#0000ff;\">ash Verification</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">PyPI provides md5 hashes in the hash fragment of package download urls.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">pip supports checking this, as well as any of the guaranteed hashlib algorithms (sha1, sha224, sha384, sha256, sha512, md5).</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">The hash fragment is case sensitive (i.e. sha1 not SHA1).</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">This check is only intended to provide basic download corruption protection. It is not intended to provide security against tampering. For that, see </span><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#ssl-certificate-verification\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">SSL Certificate Verification</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"editable-installs\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id34\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">&quot;</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">Editable&quot; Installs</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">&quot;Editable&quot; installs are fundamentally </span><a href=\"http://packages.python.org/setuptools/setuptools.html#development-mode\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">&quot;setuptools develop mode&quot;</span></a><span style=\" font-size:16pt; font-weight:400;\"> installs.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">You can install local projects or VCS projects in &quot;editable&quot; mode:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install -e path/to/SomeProject</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install -e git+http://repo/my_project.git#egg=SomeProject</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">(See the </span><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#vcs-support\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#0000ff;\">VCS Support</span></a><span style=\" font-size:16pt; font-weight:400;\"> section above for more information on VCS-related syntax.)</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">For local projects, the &quot;SomeProject.egg-info&quot; directory is created relative to the project path. This is one advantage over just using </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">setup.py develop</span><span style=\" font-size:16pt; font-weight:400;\">, which creates the &quot;egg-info&quot; directly relative the current working directory.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"controlling-setup-requires\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id35\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">C</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">ontrolling setup_requires</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Setuptools offers the </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">setup_requires</span><span style=\" font-size:16pt; font-weight:400;\"> </span><a href=\"http://pythonhosted.org/setuptools/setuptools.html#new-and-changed-setup-keywords\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">setup() keyword</span></a><span style=\" font-size:16pt; font-weight:400;\"> for specifying dependencies that need to be present in order for the </span><span style=\" font-size:16pt; font-weight:400; font-style:italic;\">setup.py</span><span style=\" font-size:16pt; font-weight:400;\"> script to run. Internally, Setuptools uses </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">easy_install</span><span style=\" font-size:16pt; font-weight:400;\"> to fulfill these dependencies.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">pip has no way to control how these dependencies are located. None of the Package Index Options have an effect.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">The solution is to configure a &quot;system&quot; or &quot;personal&quot; </span><a href=\"http://docs.python.org/2/install/index.html#distutils-configuration-files\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">Distutils configuration file</span></a><span style=\" font-size:16pt; font-weight:400;\"> to manage the fulfillment.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">For example, to have the dependency located at an alternate index, add this:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[easy_install]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">index_url = https://my.index-mirror.com</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">To have the dependency located from a local directory and not crawl PyPI, add this:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">[easy_install]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">allow_hosts = \'\'</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">find_links = file:///path/to/local/archives</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"build-system-interface\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id36\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">B</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">uild System Interface</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">In order for pip to install a package from source, </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">setup.py</span><span style=\" font-size:16pt; font-weight:400;\"> must implement the following commands:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">setup.py egg_info [--egg-base XXX]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">setup.py install --record XXX [--single-version-externally-managed] [--root XXX] [--compile|--no-compile] [--install-headers XXX]</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">The </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">egg_info</span><span style=\" font-size:16pt; font-weight:400;\"> command should create egg metadata for the package, as described in the setuptools documentation at </span><a href=\"http://pythonhosted.org/setuptools/setuptools.html#egg-info-create-egg-metadata-and-set-build-tags\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">http://pythonhosted.org/setuptools/setuptools.html#egg-info-create-egg-metadata-and-set-build-tags</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">The </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">install</span><span style=\" font-size:16pt; font-weight:400;\"> command should implement the complete process of installing the package to the target directory XXX.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">To install a package in &quot;editable&quot; mode (</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">pip install -e</span><span style=\" font-size:16pt; font-weight:400;\">), </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">setup.py</span><span style=\" font-size:16pt; font-weight:400;\"> must implement the following command:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">setup.py develop --no-deps</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">This should implement the complete process of installing the package in &quot;editable&quot; mode.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">All packages will be attempted to built into wheels:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">setup.py bdist_wheel -d XXX</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">One further </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">setup.py</span><span style=\" font-size:16pt; font-weight:400;\"> command is invoked by </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">pip install</span><span style=\" font-size:16pt; font-weight:400;\">:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">setup.py clean</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">This command is invoked to clean up temporary commands from the build. (TODO: Investigate in more detail when this command is required).</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">No other build system commands are invoked by the </span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">pip install</span><span style=\" font-size:16pt; font-weight:400;\"> command.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Installing a package from a wheel does not invoke the build system at all.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"options\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id37\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">O</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">ptions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"install-editable\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">e, --editable &lt;path/url&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Install a project in editable mode (i.e. setuptools &quot;develop mode&quot;) from a local project path or a VCS url. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption-r\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">r, --requirement &lt;file&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Install from the given requirements file. This option can be used multiple times. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption-b\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">b, --build &lt;dir&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Directory to unpack packages into and build in. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption-t\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">t, --target &lt;dir&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Install packages into &lt;dir&gt;. By default this will not replace existing files/folders in &lt;dir&gt;. Use --upgrade to replace existing packages in &lt;dir&gt; with new versions. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption-d\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">d, --download &lt;dir&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Download packages into &lt;dir&gt; instead of installing them, regardless of what\'s already installed. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--src\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-src &lt;dir&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Directory to check out editable projects into. The default in a virtualenv is &quot;&lt;venv path&gt;/src&quot;. The default for global installs is &quot;&lt;current dir&gt;/src&quot;. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption-U\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">U, --upgrade</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Upgrade all specified packages to the newest available version. This process is recursive regardless of whether a dependency is already satisfied. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--force-reinstall\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-force-reinstall</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">When upgrading, reinstall all packages even if they are already up-to-date. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption-I\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">I, --ignore-installed</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Ignore the installed packages (reinstalling instead). </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--no-deps\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-no-deps</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Don\'t install package dependencies. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--install-option\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-install-option &lt;options&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Extra arguments to be supplied to the setup.py install command (use like --install-option=&quot;--install-scripts=/usr/local/bin&quot;). Use multiple --install-option options to pass multiple options to setup.py install. If you are using an option with a directory path, be sure to use absolute path. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--global-option\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-global-option &lt;options&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Extra global options to be supplied to the setup.py call before the install command. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--user\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-user</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Install to the Python user install directory for your platform. Typically ~/.local/, or %APPDATA%Python on Windows. (See the Python documentation for site.USER_BASE for full details.) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--egg\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-egg</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Install packages as eggs, not \'flat\', like pip normally does. This option is not about installing </span><span style=\" font-size:16pt; font-weight:400; font-style:italic;\">from</span><span style=\" font-size:16pt; font-weight:400;\"> eggs. (WARNING: Because this option overrides pip\'s normal install logic, requirements files may not behave as expected.) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--root\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-root &lt;dir&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Install everything relative to this alternate root directory. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--compile\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-compile</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Compile py files to pyc </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--no-compile\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-no-compile</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Do not compile py files to pyc </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--no-use-wheel\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-no-use-wheel</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Do not Find and prefer wheel archives when searching indexes and find-links locations. DEPRECATED in favour of --no-binary. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--no-binary\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-no-binary &lt;format_control&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Do not use binary packages. Can be supplied multiple times, and each time adds to the existing value. Accepts either :all: to disable all binary packages, :none: to empty the set, or one or more package names with commas between them. Note that some packages are tricky to compile and may fail to install when this option is used on them. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--only-binary\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-only-binary &lt;format_control&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Do not use source packages. Can be supplied multiple times, and each time adds to the existing value. Accepts either :all: to disable all source packages, :none: to empty the set, or one or more package names with commas between them. Packages without binary distributions will fail to install when this option is used on them. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--pre\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-pre</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Include pre-release and development versions. By default, pip only finds stable versions. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--no-clean\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-no-clean</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Don\'t clean up build directories. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"index-url\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">i, --index-url &lt;url&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Base URL of Python Package Index (default </span><a href=\"https://pypi.python.org/simple\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">https://pypi.python.org/simple</span></a><span style=\" font-size:16pt; font-weight:400;\">). </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--extra-index-url\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-extra-index-url &lt;url&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Extra URLs of package indexes to use in addition to --index-url. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--no-index\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-no-index</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Ignore package index (only looking at --find-links URLs instead). </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption-f\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">f, --find-links &lt;url&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">If a url or path to an html file, then parse for links to archives. If a local path or </span><a href=\"file://\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">file://</span></a><span style=\" font-size:16pt; font-weight:400;\"> url that\'s a directory,then look for archives in the directory listing. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--allow-external\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-allow-external &lt;package&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Allow the installation of a package even if it is externally hosted </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--allow-all-external\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-allow-all-external</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Allow the installation of all packages that are externally hosted </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--allow-unverified\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-allow-unverified &lt;package&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Allow the installation of a package even if it is hosted in an insecure and unverifiable way </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--process-dependency-links\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">-process-dependency-links</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Enable the processing of dependency links. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"examples\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#id38\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">E</span></a><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">xamples</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Install <span style=\" font-style:italic;\">SomePackage</span> and its dependencies from <a href=\"http://pypi.python.org/pypi/\"><span style=\" text-decoration: underline; color:#ff0000;\">PyPI</span></a><span style=\" color:#ff0000;\"> </span>using <a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#requirement-specifiers\"><span style=\" text-decoration: underline; color:#ff0000;\">Requirement Specifiers</span></a></li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install SomePackage            # latest version</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install SomePackage==1.0.4     # specific version</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install \'SomePackage&gt;=1.0.4\'     # minimum version</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Install a list of requirements specified in a file. See the <a href=\"https://pip.pypa.io/en/latest/user_guide.html#requirements-files\"><span style=\" text-decoration: underline; color:#ff0000;\">Requirements files</span></a>.</li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install -r requirements.txt</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Upgrade an already installed <span style=\" font-style:italic;\">SomePackage</span> to the latest from PyPI.</li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install --upgrade SomePackage</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Install a local project in &quot;editable&quot; mode. See the section on <a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#editable-installs\"><span style=\" text-decoration: underline; color:#ff0000;\">Editable Installs</span></a>.</li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install -e .                     # project in current directory</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install -e path/to/project       # project in another directory</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Install a project from VCS in &quot;editable&quot; mode. See the sections on <a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#vcs-support\"><span style=\" text-decoration: underline; color:#ff0000;\">VCS Support</span></a> and <a href=\"https://pip.pypa.io/en/latest/reference/pip_install.html#editable-installs\"><span style=\" text-decoration: underline; color:#ff0000;\">Editable Installs</span></a>.</li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install -e git+https://git.repo/some_pkg.git#egg=SomePackage          # from git</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install -e hg+https://hg.repo/some_pkg.git#egg=SomePackage            # from mercurial</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install -e svn+svn://svn.repo/some_pkg/trunk/#egg=SomePackage         # from svn</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install -e git+https://git.repo/some_pkg.git@feature#egg=SomePackage  # from \'feature\' branch</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install -e git+https://git.repo/some_repo.git#egg=subdir&amp;subdirectory=subdir_path # install a python package from a repo subdirectory</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Install a package with <a href=\"http://packages.python.org/setuptools/setuptools.html#declaring-extras-optional-features-with-their-own-dependencies\"><span style=\" text-decoration: underline; color:#ff0000;\">setuptools extras</span></a>.</li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install SomePackage[PDF]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install SomePackage[PDF]==3.0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install -e .[PDF]==3.0  # editable project in current directory</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Install a particular source archive file.</li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install ./downloads/SomePackage-1.0.4.tar.gz</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install http://my.package.repo/SomePackage-1.0.4.zip</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Install from alternative package repositories.</li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Install from a different index, and not </span><a href=\"http://pypi.python.org/pypi/\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">PyPI</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install --index-url http://my.package.repo/simple/ SomePackage</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Search an additional index during install, in addition to </span><a href=\"http://pypi.python.org/pypi/\"><span style=\" font-size:16pt; font-weight:400; text-decoration: underline; color:#ff0000;\">PyPI</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install --extra-index-url http://my.package.repo/simple SomePackage</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:400;\">Install from a local flat directory containing archives (and don\'t scan indexes):</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install --no-index --find-links=file:///local/dir/ SomePackage</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install --no-index --find-links=/local/dir/ SomePackage</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install --no-index --find-links=relative/dir/ SomePackage</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:16pt; font-weight:400;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Find pre-release and development versions, in addition to stable versions. By default, pip only finds stable versions.</li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:16pt; font-weight:400;\">$ pip install --pre SomePackage</span></p></body></html>", None))
        self.label.setText(_translate("TabWidget", "  HELP", None))
        self.install_commandbtr.setToolTip(_translate("TabWidget", "<html><head/><body><p>Your own command. Dont type pip in the begining</p></body></html>", None))
        self.install_commandbtr.setText(_translate("TabWidget", "PIP \n"
" Command", None))
        self.install_box.setToolTip(_translate("TabWidget", "<html><head/><body><p>Enter here waht to search for</p></body></html>", None))
        self.label_7.setText(_translate("TabWidget", "Enter package name", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "install", None))
        self.label_3.setText(_translate("TabWidget", "  HELP", None))
        self.textEdit_helplist.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Adobe Arabic\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://pip.pypa.io/en/latest/reference/pip_list.html#id2\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">PIP list</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"contents\"></a><span style=\" font-size:18pt; font-weight:600;\">C</span><span style=\" font-size:18pt; font-weight:600;\">ontents</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id2\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_list.html#pip-list\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">p</span></a><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">ip list</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id3\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_list.html#usage\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">U</span></a><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">sage</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id4\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_list.html#description\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">D</span></a><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">escription</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id5\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_list.html#options\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">O</span></a><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">ptions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id6\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_list.html#examples\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">E</span></a><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">xamples</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"usage\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_list.html#id3\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">U</span></a><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">sage</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">pip list [options]</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"description\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_list.html#id4\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">D</span></a><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">escription</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">List installed packages, including editables.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Packages are listed in a case-insensitive sorted order.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"options\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_list.html#id5\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">O</span></a><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">ptions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"list-outdated\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">o, --outdated</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">List outdated packages (excluding editables) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption-u\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">u, --uptodate</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">List uptodate packages (excluding editables) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption-e\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">e, --editable</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">List editable projects. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption-l\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">l, --local</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">If in a virtualenv that has global access, do not list globally-installed packages. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--user\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">-user</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Only output packages installed in user-site. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--pre\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">-pre</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Include pre-release and development versions. By default, pip only finds stable versions. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"index-url\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">i, --index-url &lt;url&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Base URL of Python Package Index (default </span><a href=\"https://pypi.python.org/simple\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#0000ff;\">https://pypi.python.org/simple</span></a><span style=\" font-size:18pt; font-weight:600;\">). </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--extra-index-url\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">-extra-index-url &lt;url&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Extra URLs of package indexes to use in addition to --index-url. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--no-index\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">-no-index</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Ignore package index (only looking at --find-links URLs instead). </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption-f\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">f, --find-links &lt;url&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">If a url or path to an html file, then parse for links to archives. If a local path or </span><a href=\"file://\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#0000ff;\">file://</span></a><span style=\" font-size:18pt; font-weight:600;\"> url that\'s a directory,then look for archives in the directory listing. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--allow-external\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">-allow-external &lt;package&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Allow the installation of a package even if it is externally hosted </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--allow-all-external\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">-allow-all-external</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Allow the installation of all packages that are externally hosted </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--allow-unverified\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">-allow-unverified &lt;package&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Allow the installation of a package even if it is hosted in an insecure and unverifiable way </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption--process-dependency-links\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">-process-dependency-links</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Enable the processing of dependency links. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"examples\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_list.html#id6\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#0000ff;\">E</span></a><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#0000ff;\">xamples</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:18pt; font-weight:600;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">List installed packages.</li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">$ pip list</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">docutils (0.10)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">Jinja2 (2.7.2)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">MarkupSafe (0.18)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">Pygments (1.6)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">Sphinx (1.2.1)</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:18pt; font-weight:600;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">List outdated packages (excluding editables), and the latest version available</li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">$ pip list --outdated</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">docutils (Current: 0.10 Latest: 0.11)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt; font-weight:600;\">Sphinx (Current: 1.2.1 Latest: 1.2.2)</span></p></body></html>", None))
        self.List_packagebtr.setToolTip(_translate("TabWidget", "<html><head/><body><p>List installed packages.</p></body></html>", None))
        self.List_packagebtr.setText(_translate("TabWidget", "List Packages", None))
        self.List_commandbtr.setToolTip(_translate("TabWidget", "<html><head/><body><p>Your own list command. Dont type pip in the begining</p></body></html>", None))
        self.List_commandbtr.setText(_translate("TabWidget", "List Command", None))
        self.label_9.setText(_translate("TabWidget", "Enter package name", None))
        self.install_box_2.setToolTip(_translate("TabWidget", "<html><head/><body><p>Enter here what to search for.</p></body></html>", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_2), _translate("TabWidget", "List", None))
        self.Uninstall_btr.setToolTip(_translate("TabWidget", "<html><head/><body><p>Uninstall pip package</p></body></html>", None))
        self.Uninstall_btr.setText(_translate("TabWidget", "Uninstall", None))
        self.textEdit_helpuninstall.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Adobe Arabic\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\"><br /></span><a href=\"https://pip.pypa.io/en/latest/reference/pip_uninstall.html#id2\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">pip uninstall</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"contents\"></a><span style=\" font-size:18pt;\">C</span><span style=\" font-size:18pt;\">ontents</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id2\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_uninstall.html#pip-uninstall\"><span style=\" font-size:18pt; text-decoration: underline; color:#ff0000;\">p</span></a><span style=\" font-size:18pt; text-decoration: underline; color:#ff0000;\">ip uninstall</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id3\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_uninstall.html#usage\"><span style=\" font-size:18pt; text-decoration: underline; color:#ff0000;\">U</span></a><span style=\" font-size:18pt; text-decoration: underline; color:#ff0000;\">sage</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id4\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_uninstall.html#description\"><span style=\" font-size:18pt; text-decoration: underline; color:#ff0000;\">D</span></a><span style=\" font-size:18pt; text-decoration: underline; color:#ff0000;\">escription</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id5\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_uninstall.html#options\"><span style=\" font-size:18pt; text-decoration: underline; color:#ff0000;\">O</span></a><span style=\" font-size:18pt; text-decoration: underline; color:#ff0000;\">ptions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id6\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_uninstall.html#examples\"><span style=\" font-size:18pt; text-decoration: underline; color:#ff0000;\">E</span></a><span style=\" font-size:18pt; text-decoration: underline; color:#ff0000;\">xamples</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"usage\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_uninstall.html#id3\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">U</span></a><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">sage</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt;\">pip uninstall [options] &lt;package&gt; ...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt;\">pip uninstall [options] -r &lt;requirements file&gt; ...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"description\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_uninstall.html#id4\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">D</span></a><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">escription</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Uninstall packages.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">pip is able to uninstall most installed packages. Known exceptions are:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:18pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pure distutils packages installed with <span style=\" font-family:\'Courier New,courier\';\">python setup.py install</span>, which leave behind no metadata to determine what files were installed.</li>\n"
"<li style=\" font-size:18pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Script wrappers installed by <span style=\" font-family:\'Courier New,courier\';\">python setup.py develop</span>.</li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"options\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_uninstall.html#id5\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">O</span></a><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">ptions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"uninstall-requirement\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:18pt;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:18pt;\">r, --requirement &lt;file&gt;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Uninstall all the packages listed in the given requirements file. This option can be used multiple times. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cmdoption-y\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:18pt;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:18pt;\">y, --yes</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Don\'t ask for confirmation of uninstall deletions. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"examples\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_uninstall.html#id6\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">E</span></a><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">xamples</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:18pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Uninstall a package.</li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt;\">$ pip uninstall simplejson</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt;\">Uninstalling simplejson:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt;\">  /home/me/env/lib/python2.7/site-packages/simplejson</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt;\">  /home/me/env/lib/python2.7/site-packages/simplejson-2.2.1-py2.7.egg-info</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt;\">Proceed (y/n)? y</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt;\">  Successfully uninstalled simplejson</span></p></body></html>", None))
        self.label_2.setText(_translate("TabWidget", "  HELP", None))
        self.Uninstall_commandbtr.setToolTip(_translate("TabWidget", "<html><head/><body><p>You own unistall command.</p></body></html>", None))
        self.Uninstall_commandbtr.setText(_translate("TabWidget", "Uninstall \n"
" Command", None))
        self.label_8.setText(_translate("TabWidget", "enter package name", None))
        self.uninstall_box.setToolTip(_translate("TabWidget", "<html><head/><body><p>Enter here waht to search for.</p></body></html>", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "Uninstall", None))
        self.textEdit_helpshow.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Adobe Arabic\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://pip.pypa.io/en/latest/reference/pip_show.html#id2\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">pip show</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"contents\"></a><span style=\" font-size:18pt;\">C</span><span style=\" font-size:18pt;\">ontents</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id2\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_show.html#pip-show\"><span style=\" font-size:18pt; text-decoration: underline; color:#ff0000;\">p</span></a><span style=\" font-size:18pt; text-decoration: underline; color:#ff0000;\">ip show</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id3\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_show.html#usage\"><span style=\" font-size:18pt; text-decoration: underline; color:#ff0000;\">U</span></a><span style=\" font-size:18pt; text-decoration: underline; color:#ff0000;\">sage</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id4\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_show.html#description\"><span style=\" font-size:18pt; text-decoration: underline; color:#ff0000;\">D</span></a><span style=\" font-size:18pt; text-decoration: underline; color:#ff0000;\">escription</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id5\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_show.html#options\"><span style=\" font-size:18pt; text-decoration: underline; color:#ff0000;\">O</span></a><span style=\" font-size:18pt; text-decoration: underline; color:#ff0000;\">ptions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"id6\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_show.html#examples\"><span style=\" font-size:18pt; text-decoration: underline; color:#ff0000;\">E</span></a><span style=\" font-size:18pt; text-decoration: underline; color:#ff0000;\">xamples</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"usage\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_show.html#id3\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">U</span></a><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">sage</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt;\">pip show [options] &lt;package&gt; ...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"description\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_show.html#id4\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">D</span></a><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">escription</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Show information about one or more installed packages.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"options\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_show.html#id5\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">O</span></a><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">ptions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"show-files\"></a><span style=\" font-family:\'Courier New,courier\'; font-size:18pt;\">-</span><span style=\" font-family:\'Courier New,courier\'; font-size:18pt;\">f, --files</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:30px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Show the full list of installed files for each package. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"examples\"></a><a href=\"https://pip.pypa.io/en/latest/reference/pip_show.html#id6\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">E</span></a><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">xamples</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:18pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Show information about a package:</li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt;\">$ pip show sphinx</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt;\">---</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt;\">Name: Sphinx</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt;\">Version: 1.1.3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt;\">Location: /my/env/lib/pythonx.x/site-packages</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\'; font-size:18pt;\">Requires: Pygments, Jinja2, docutils</span></p></body></html>", None))
        self.Show_packagebtr.setToolTip(_translate("TabWidget", "<html><head/><body><p>Show information about installed packages.</p></body></html>", None))
        self.Show_packagebtr.setText(_translate("TabWidget", "Show Package", None))
        self.Show_commandbtr.setText(_translate("TabWidget", "Show Command", None))
        self.label_4.setText(_translate("TabWidget", "  HELP", None))
        self.label_10.setText(_translate("TabWidget", "Enter package name", None))
        self.show_box.setToolTip(_translate("TabWidget", "<html><head/><body><p>Enter here waht to search for.</p></body></html>", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_3), _translate("TabWidget", "Show", None))
        self.bt_Intieets.setText(_translate("TabWidget", "Twitter", None))
        self.label_5.setText(_translate("TabWidget", "        Visit Github", None))
        self.bt_Githubs.setText(_translate("TabWidget", "Techbliss github", None))
        self.label_6.setText(_translate("TabWidget", "    Storm Shadow \n"
"         on Twitter", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_4), _translate("TabWidget", "Author", None))

        '''buttons yeah'''

        self.search_btr.clicked.connect(self.searchpip)
        self.install_pipbtr.clicked.connect(self.innpip)
        self.install_commandbtr.clicked.connect(self.compip)
        self.List_packagebtr.clicked.connect(self.lispip)
        self.List_commandbtr.clicked.connect(self.listcompip)
        self.Uninstall_btr.clicked.connect(self.unpip)
        self.Uninstall_commandbtr.clicked.connect(self.uncompip)
        self.Show_packagebtr.clicked.connect(self.shopip)
        self.Show_commandbtr.clicked.connect(self.shocopip)
        self.bt_Githubs.clicked.connect(self.gitauth)
        self.bt_Intieets.clicked.connect(self.tweetu)



    '''commands yihhaaa'''
    def searchpip(self):
        import os
        import sys
        import ma
        import subprocess
        from subprocess import Popen, PIPE
        ff = self.install_box.toPlainText()
        dog1 = subprocess.Popen('pip search ' + str(ff), stdout=subprocess.PIPE, shell=True)
        self.textEdit_install.setText(dog1.stdout.read())

    def innpip(self):
        import os
        import sys
        import ma
        import subprocess
        from subprocess import Popen, PIPE
        ff = self.install_box.toPlainText()
        dog2 = subprocess.Popen('pip install ' + str(ff), stdout=subprocess.PIPE, shell=True)
        self.textEdit_install.setText(dog2.stdout.read())

    def compip(self):
        import os
        import sys
        import ma
        import subprocess
        from subprocess import Popen, PIPE
        ff = self.install_box.toPlainText()
        dog3 = subprocess.Popen('pip ' + str(ff), stdout=subprocess.PIPE, shell=True)
        self.textEdit_install.setText(dog3.stdout.read())

    def lispip(self):
        import os
        import sys
        import ma
        import subprocess
        from subprocess import Popen, PIPE
        ff = self.install_box_2.toPlainText()
        dog4 = subprocess.Popen('pip list', stdout=subprocess.PIPE, shell=True)
        self.textEdit_list.setText(dog4.stdout.read())

    def listcompip(self):
        import os
        import sys
        import ma
        import subprocess
        from subprocess import Popen, PIPE
        ff = self.install_box_2.toPlainText()
        dog5 = subprocess.Popen('pip ' + str(ff), stdout=subprocess.PIPE, shell=True)
        self.textEdit_list.setText(dog5.stdout.read())

    def unpip(self):
        import os
        import sys
        import ma
        import subprocess
        from subprocess import Popen, PIPE
        ff = self.uninstall_box.toPlainText()
        dog6 = subprocess.Popen('pip uninstall -y ' + str(ff), stdout=subprocess.PIPE, shell=True)
        self.textEdit_uninstall.setText(dog6.stdout.read())

    def uncompip(self):
        import os
        import sys
        import ma
        import subprocess
        from subprocess import Popen, PIPE
        ff = self.uninstall_box.toPlainText()
        dog7 = subprocess.Popen('pip ' + str(ff), stdout=subprocess.PIPE, shell=True)
        self.textEdit_uninstall.setText(dog7.stdout.read())

    def shopip(self):
        import os
        import sys
        import ma
        import subprocess
        from subprocess import Popen, PIPE
        ff = self.show_box.toPlainText()
        dog5 = subprocess.Popen('pip show ' + str(ff), stdout=subprocess.PIPE, shell=True)
        self.textEdit_show.setText(dog5.stdout.read())

    def shocopip(self):
        import os
        import sys
        import ma
        import subprocess
        from subprocess import Popen, PIPE
        ff = self.show_box.toPlainText()
        dog8 = subprocess.Popen('pip ' + str(ff), stdout=subprocess.PIPE, shell=True)
        self.textEdit_show.setText(dog8.stdout.read())

    def gitauth(self):
        import webbrowser

        webbrowser.open('https://github.com/techbliss')

    def tweetu(self):
        import webbrowser

        webbrowser.open('https://twitter.com/zadow28')




import ico
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication.instance()
    if not app:
        app = QtGui.QApplication([])
    TabWidget = QtGui.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    app.exec_()



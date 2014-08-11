# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created: Mon Aug 11 18:18:02 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(1001, 945)
        main_window.setMinimumSize(QtCore.QSize(0, 0))
        main_window.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtGui.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.load_map_button = QtGui.QPushButton(self.centralwidget)
        self.load_map_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.load_map_button.setObjectName("load_map_button")
        self.horizontalLayout.addWidget(self.load_map_button)
        self.settings_button = QtGui.QPushButton(self.centralwidget)
        self.settings_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.settings_button.setObjectName("settings_button")
        self.horizontalLayout.addWidget(self.settings_button)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_19 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setTextFormat(QtCore.Qt.AutoText)
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_19.setWordWrap(False)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 2, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setTextFormat(QtCore.Qt.AutoText)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)
        self.label_17 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setTextFormat(QtCore.Qt.AutoText)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 1, 0, 1, 1)
        self.ang_vel_label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ang_vel_label.sizePolicy().hasHeightForWidth())
        self.ang_vel_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(9)
        self.ang_vel_label.setFont(font)
        self.ang_vel_label.setTextFormat(QtCore.Qt.AutoText)
        self.ang_vel_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ang_vel_label.setObjectName("ang_vel_label")
        self.gridLayout_2.addWidget(self.ang_vel_label, 2, 1, 1, 1)
        self.pose_label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pose_label.sizePolicy().hasHeightForWidth())
        self.pose_label.setSizePolicy(sizePolicy)
        self.pose_label.setMinimumSize(QtCore.QSize(170, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(9)
        self.pose_label.setFont(font)
        self.pose_label.setTextFormat(QtCore.Qt.AutoText)
        self.pose_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.pose_label.setObjectName("pose_label")
        self.gridLayout_2.addWidget(self.pose_label, 0, 1, 1, 1)
        self.velocity_label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.velocity_label.sizePolicy().hasHeightForWidth())
        self.velocity_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(9)
        self.velocity_label.setFont(font)
        self.velocity_label.setTextFormat(QtCore.Qt.AutoText)
        self.velocity_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.velocity_label.setObjectName("velocity_label")
        self.gridLayout_2.addWidget(self.velocity_label, 1, 1, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.zoom_in_button = QtGui.QPushButton(self.centralwidget)
        self.zoom_in_button.setMaximumSize(QtCore.QSize(25, 16777215))
        self.zoom_in_button.setObjectName("zoom_in_button")
        self.horizontalLayout_4.addWidget(self.zoom_in_button)
        self.zoom_out_button = QtGui.QPushButton(self.centralwidget)
        self.zoom_out_button.setMaximumSize(QtCore.QSize(25, 16777215))
        self.zoom_out_button.setObjectName("zoom_out_button")
        self.horizontalLayout_4.addWidget(self.zoom_out_button)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)
        self.label_24 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(9)
        self.label_24.setFont(font)
        self.label_24.setTextFormat(QtCore.Qt.AutoText)
        self.label_24.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_24.setWordWrap(False)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 3, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.graphics_view_zoom = PlotGraphicsViewZoom(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphics_view_zoom.sizePolicy().hasHeightForWidth())
        self.graphics_view_zoom.setSizePolicy(sizePolicy)
        self.graphics_view_zoom.setMinimumSize(QtCore.QSize(300, 0))
        self.graphics_view_zoom.setMaximumSize(QtCore.QSize(300, 16777215))
        self.graphics_view_zoom.setFrameShadow(QtGui.QFrame.Sunken)
        self.graphics_view_zoom.setLineWidth(2)
        self.graphics_view_zoom.setObjectName("graphics_view_zoom")
        self.gridLayout.addWidget(self.graphics_view_zoom, 3, 0, 1, 1)
        self.graphics_view = PlotGraphicsView(self.centralwidget)
        self.graphics_view.setMinimumSize(QtCore.QSize(0, 0))
        self.graphics_view.setLineWidth(2)
        self.graphics_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphics_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphics_view.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.graphics_view.setObjectName("graphics_view")
        self.gridLayout.addWidget(self.graphics_view, 0, 1, 4, 1)
        self.logo_label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_label.sizePolicy().hasHeightForWidth())
        self.logo_label.setSizePolicy(sizePolicy)
        self.logo_label.setMinimumSize(QtCore.QSize(259, 113))
        self.logo_label.setMaximumSize(QtCore.QSize(259, 113))
        self.logo_label.setText("")
        self.logo_label.setScaledContents(True)
        self.logo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_label.setObjectName("logo_label")
        self.gridLayout.addWidget(self.logo_label, 0, 0, 1, 1)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1001, 23))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QtGui.QApplication.translate("main_window", "MSL Sim", None, QtGui.QApplication.UnicodeUTF8))
        self.load_map_button.setText(QtGui.QApplication.translate("main_window", "Load map...", None, QtGui.QApplication.UnicodeUTF8))
        self.settings_button.setText(QtGui.QApplication.translate("main_window", "Settings...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("main_window", "Angular velocity:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("main_window", "Pose:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("main_window", "Velocity:", None, QtGui.QApplication.UnicodeUTF8))
        self.ang_vel_label.setText(QtGui.QApplication.translate("main_window", "4 deg/s", None, QtGui.QApplication.UnicodeUTF8))
        self.pose_label.setText(QtGui.QApplication.translate("main_window", "0.00 m, 0.00 m, -178 deg", None, QtGui.QApplication.UnicodeUTF8))
        self.velocity_label.setText(QtGui.QApplication.translate("main_window", "0.4 m/s", None, QtGui.QApplication.UnicodeUTF8))
        self.zoom_in_button.setText(QtGui.QApplication.translate("main_window", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.zoom_out_button.setText(QtGui.QApplication.translate("main_window", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("main_window", "Zoom:", None, QtGui.QApplication.UnicodeUTF8))

from sim.controller import PlotGraphicsViewZoom, PlotGraphicsView

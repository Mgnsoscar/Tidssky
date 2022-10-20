from PyQt5 import QtCore, QtGui, QtWidgets
import Bakgrunnsbilde
import datetime


class Room(QtWidgets.QFrame):
    def __init__(self, *args, **kwargs):

        #### Timer global values

        self.timer_counter_num = 0
        self.stopwatch_counter_num = 0
        self.stopwatch_running = False
        self.timer_running = False


        ###########

        QtWidgets.QFrame.__init__(self, *args, **kwargs)

        self.setObjectName("MainWindow")

        self.setGeometry(QtCore.QRect(0, 0, 259, 316))
        self.setMinimumSize(QtCore.QSize(250, 0))
        self.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.setStyleSheet("background:none;")
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.roomlabel = QtWidgets.QFrame(self)
        self.roomlabel.setMinimumSize(QtCore.QSize(0, 25))
        self.roomlabel.setMaximumSize(QtCore.QSize(16777215, 25))
        self.roomlabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.539773, y1:1, x2:0.523, y2:0, stop:0.676136 rgba(0, 0, 0, 120), stop:0.881356 rgba(112, 112, 112, 60), stop:1 rgba(255, 255, 255, 0));\n"
"border-radius:2px;\n"
"border-bottom-left-radius:15px;\n"
"border-bottom-right-radius:15px;")
        self.roomlabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.roomlabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.roomlabel.setObjectName("roomlabel")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.roomlabel)
        self.verticalLayout_6.setContentsMargins(0, 4, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.roomlabel)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_4.addWidget(self.roomlabel)
        self.pasientstatus = QtWidgets.QFrame(self)
        self.pasientstatus.setMinimumSize(QtCore.QSize(0, 85))
        self.pasientstatus.setMaximumSize(QtCore.QSize(16777215, 85))
        self.pasientstatus.setStyleSheet("border-radius:15px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"background-color: rgba(0, 0, 0, 120);")
        self.pasientstatus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pasientstatus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pasientstatus.setObjectName("pasientstatus")
        self.gridLayout = QtWidgets.QGridLayout(self.pasientstatus)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setHorizontalSpacing(1)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.pasientframe = QtWidgets.QFrame(self.pasientstatus)
        self.pasientframe.setStyleSheet("border-radius:0px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;")
        self.pasientframe.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pasientframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pasientframe.setObjectName("pasientframe")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.pasientframe)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pasientlabel = QtWidgets.QLabel(self.pasientframe)
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPointSize(10)
        self.pasientlabel.setFont(font)
        self.pasientlabel.setStyleSheet("background:none;\n"
"color: rgb(217, 217, 217);")
        self.pasientlabel.setObjectName("pasientlabel")
        self.verticalLayout_7.addWidget(self.pasientlabel, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.pasientframe, 0, 0, 1, 1)
        self.pasientsvarframe = QtWidgets.QFrame(self.pasientstatus)
        self.pasientsvarframe.setStyleSheet("border-radius:0px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;")
        self.pasientsvarframe.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pasientsvarframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pasientsvarframe.setObjectName("pasientsvarframe")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.pasientsvarframe)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pasientsvarlabel = QtWidgets.QLabel(self.pasientsvarframe)
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPointSize(10)
        self.pasientsvarlabel.setFont(font)
        self.pasientsvarlabel.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.pasientsvarlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pasientsvarlabel.setObjectName("pasientsvarlabel")
        self.verticalLayout_8.addWidget(self.pasientsvarlabel)
        self.gridLayout.addWidget(self.pasientsvarframe, 0, 1, 1, 1)
        self.statusframe = QtWidgets.QFrame(self.pasientstatus)
        self.statusframe.setStyleSheet("border-radius:15px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;")
        self.statusframe.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.statusframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.statusframe.setObjectName("statusframe")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.statusframe)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.statuslabel = QtWidgets.QLabel(self.statusframe)
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPointSize(10)
        self.statuslabel.setFont(font)
        self.statuslabel.setStyleSheet("background:none;\n"
"color: rgb(217, 217, 217);")
        self.statuslabel.setObjectName("statuslabel")
        self.verticalLayout_9.addWidget(self.statuslabel, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.statusframe, 1, 0, 1, 1)
        self.statussvarframe = QtWidgets.QFrame(self.pasientstatus)
        self.statussvarframe.setStyleSheet("border-radius:0px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;")
        self.statussvarframe.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.statussvarframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.statussvarframe.setObjectName("statussvarframe")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.statussvarframe)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.statussvarlabel = QtWidgets.QLabel(self.statussvarframe)
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPointSize(10)
        self.statussvarlabel.setFont(font)
        self.statussvarlabel.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.statussvarlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statussvarlabel.setObjectName("statussvarlabel")
        self.verticalLayout_10.addWidget(self.statussvarlabel)
        self.gridLayout.addWidget(self.statussvarframe, 1, 1, 1, 1)
        self.nestebeh = QtWidgets.QFrame(self.pasientstatus)
        self.nestebeh.setStyleSheet("border-radius:0px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;")
        self.nestebeh.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.nestebeh.setFrameShadow(QtWidgets.QFrame.Raised)
        self.nestebeh.setObjectName("nestebeh")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.nestebeh)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.nestebehlabel = QtWidgets.QLabel(self.nestebeh)
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPointSize(10)
        self.nestebehlabel.setFont(font)
        self.nestebehlabel.setStyleSheet("background:none;\n"
"color: rgb(217, 217, 217);")
        self.nestebehlabel.setObjectName("nestebehlabel")
        self.verticalLayout_11.addWidget(self.nestebehlabel, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.nestebeh, 2, 0, 1, 1)
        self.nestebehsvarframe = QtWidgets.QFrame(self.pasientstatus)
        self.nestebehsvarframe.setStyleSheet("border-radius:0px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;")
        self.nestebehsvarframe.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.nestebehsvarframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.nestebehsvarframe.setObjectName("nestebehsvarframe")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.nestebehsvarframe)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.nestebehsvarlabel = QtWidgets.QLabel(self.nestebehsvarframe)
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPointSize(10)
        self.nestebehsvarlabel.setFont(font)
        self.nestebehsvarlabel.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.nestebehsvarlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nestebehsvarlabel.setObjectName("nestebehsvarlabel")
        self.verticalLayout_12.addWidget(self.nestebehsvarlabel)
        self.gridLayout.addWidget(self.nestebehsvarframe, 2, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.pasientstatus)
        self.timer = QtWidgets.QFrame(self)
        self.timer.setStyleSheet("border-radius:0px;\n"
"background-color: rgba(0, 0, 0, 120);\n"
"border-bottom-left-radius:15px;\n"
"border-bottom-right-radius:15px;")
        self.timer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.timer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.timer.setObjectName("timer")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.timer)
        self.verticalLayout_44.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_44.setSpacing(4)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.timerframe = QtWidgets.QFrame(self.timer)
        self.timerframe.setMinimumSize(QtCore.QSize(250, 80))
        self.timerframe.setMaximumSize(QtCore.QSize(250, 80))
        self.timerframe.setStyleSheet("border-radius:40px;\n"
"background:none;\n"
"border:2px solid;\n"
"border-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1, y2:0, stop:0 rgba(255, 2, 2, 255), stop:1 rgba(255, 120, 120, 255));")
        self.timerframe.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.timerframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.timerframe.setObjectName("timerframe")
        self.verticalLayout_49 = QtWidgets.QVBoxLayout(self.timerframe)
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.lcdtime = QtWidgets.QLCDNumber(self.timerframe)
        self.lcdtime.setStyleSheet("background:none;\n"
"border:none;\n"
"color: rgba(255, 255, 255, 200);")
        self.lcdtime.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdtime.setDigitCount(6)
        self.lcdtime.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdtime.setObjectName("lcdtime")

        self.verticalLayout_49.addWidget(self.lcdtime)
        self.verticalLayout_44.addWidget(self.timerframe, 0, QtCore.Qt.AlignHCenter)
        self.startstopframe = QtWidgets.QFrame(self.timer)
        self.startstopframe.setMinimumSize(QtCore.QSize(0, 30))
        self.startstopframe.setMaximumSize(QtCore.QSize(16777215, 30))
        self.startstopframe.setStyleSheet("background:none;")
        self.startstopframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.startstopframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.startstopframe.setObjectName("startstopframe")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.startstopframe)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.start = QtWidgets.QPushButton(self.startstopframe)
        self.start.setMinimumSize(QtCore.QSize(50, 30))
        self.start.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setStyleSheet("QPushButton{\n"
"border:1px solid;\n"
"border-color: rgb(39, 39, 39);\n"
"border-radius:0px;\n"
"border-radius:15px;\n"
"background-color: rbg(0,0,0,80);\n"
"    color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(0, 0, 0, 120);\n"
"}")
        self.start.setObjectName("start")
        self.horizontalLayout_11.addWidget(self.start)
        self.stop = QtWidgets.QPushButton(self.startstopframe)
        self.stop.setMinimumSize(QtCore.QSize(50, 30))
        self.stop.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.stop.setFont(font)
        self.stop.setStyleSheet("QPushButton{\n"
"border:1px solid;\n"
"border-color: rgb(39, 39, 39);\n"
"border-radius:0px;\n"
"border-radius:15px;\n"
"background-color: rbg(0,0,0,80);\n"
"    color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(0, 0, 0, 120);\n"
"}")
        self.stop.setObjectName("stop")
        self.horizontalLayout_11.addWidget(self.stop)
        self.reset = QtWidgets.QPushButton(self.startstopframe)
        self.reset.setMinimumSize(QtCore.QSize(50, 30))
        self.reset.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.reset.setFont(font)
        self.reset.setStyleSheet("QPushButton{\n"
"border:1px solid;\n"
"border-color: rgb(39, 39, 39);\n"
"border-radius:0px;\n"
"border-radius:15px;\n"
"background-color: rbg(0,0,0,80);\n"
"    color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(0, 0, 0, 120);\n"
"}")
        self.reset.setObjectName("reset")
        self.horizontalLayout_11.addWidget(self.reset)
        self.verticalLayout_44.addWidget(self.startstopframe)
        self.addtimeframe = QtWidgets.QFrame(self.timer)
        self.addtimeframe.setMinimumSize(QtCore.QSize(0, 30))
        self.addtimeframe.setMaximumSize(QtCore.QSize(16777215, 30))
        self.addtimeframe.setStyleSheet("background:none")
        self.addtimeframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.addtimeframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.addtimeframe.setObjectName("addtimeframe")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.addtimeframe)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.minus = QtWidgets.QPushButton(self.addtimeframe)
        self.minus.setMinimumSize(QtCore.QSize(30, 30))
        self.minus.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.minus.setFont(font)
        self.minus.setStyleSheet("QPushButton{\n"
"border:1px solid;\n"
"border-color: rgb(39, 39, 39);\n"
"border-radius:0px;\n"
"border-radius:15px;\n"
"background-color: rbg(0,0,0,80);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 2, 2, 100);\n"
"}")
        self.minus.setObjectName("minus")
        self.horizontalLayout_6.addWidget(self.minus)
        self.textenter = QtWidgets.QLineEdit(self.addtimeframe)
        self.textenter.setMinimumSize(QtCore.QSize(0, 30))
        self.textenter.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPointSize(10)
        self.textenter.setFont(font)
        self.textenter.setStyleSheet("border-radius:5px;\n"
"background-color: rgba(0, 0, 0, 120); \n"
"color: rgb(255, 255, 255);")
        self.textenter.setAlignment(QtCore.Qt.AlignCenter)
        self.textenter.setObjectName("textenter")
        self.horizontalLayout_6.addWidget(self.textenter)
        self.plus = QtWidgets.QPushButton(self.addtimeframe)
        self.plus.setMinimumSize(QtCore.QSize(30, 30))
        self.plus.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.plus.setFont(font)
        self.plus.setStyleSheet("QPushButton{\n"
"border:1px solid;\n"
"border-color: rgb(39, 39, 39);\n"
"border-radius:0px;\n"
"border-radius:15px;\n"
"background-color: rgb(0,0,0,80);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(0, 255, 0, 100);\n"
"};")
        self.plus.setAutoRepeatDelay(0)
        self.plus.setObjectName("plus")
        self.horizontalLayout_6.addWidget(self.plus)
        self.verticalLayout_44.addWidget(self.addtimeframe)
        self.verticalLayout_4.addWidget(self.timer)
        #self.centrawidget.setCentralWidget(self.Room1)


        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("MainWindow", "Injeksjonsrom 1"))
        self.pasientlabel.setText(_translate("MainWindow", "Pasient:"))
        self.pasientsvarlabel.setText(_translate("MainWindow", "Magnus Støleggen"))
        self.statuslabel.setText(_translate("MainWindow", "Status"))
        self.statussvarlabel.setText(_translate("MainWindow", "Under behandling"))
        self.nestebehlabel.setText(_translate("MainWindow", "Neste behandling"))
        self.nestebehsvarlabel.setText(_translate("MainWindow", "PET-Scan - 14:45"))
        self.start.setText(_translate("MainWindow", "START"))
        self.stop.setText(_translate("MainWindow", "STOP"))
        self.reset.setText(_translate("MainWindow", "RESET"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.plus.setText(_translate("MainWindow", "+"))

        ########### Set start button

        self.start.clicked.connect(lambda:timer('start'))
        self.lcdtime.setDigitCount(12)



        def timer_counter(self,):
                def count():

                        if self.timer_running:

                                if self.timer_counter_num == 0:

                                        self.timer_running = False
                                        self.timer('reset')
                                        display = 'Time Is Up'

                                else:
                                        tt = datetime.timedelta(seconds=self.timer_counter_num)
                                        display = tt
                                        self.timer_counter_num -= 1

                                label.display(display)
                                self.timer = QtCore.QTimer()
                                self.timer.timeout.connect(count)
                                self.timer.setInterval(1000)  # 1000ms = 1s
                                self.timer.start()

                count()

        def timer(self, work):

                #### Define what to do if the start button is pressed:

                if work == 'start':

                        self.timer_running = True

                        if self.timer_counter_num == 0:

                                timer_time_str = '00:15:20'
                                hours, minutes, seconds = timer_time_str.split(':')
                                minutes = int(minutes) + (int(hours) * 60)
                                seconds = int(seconds) + (minutes * 60)
                                self.timer_counter_num = self.timer_counter_num + seconds

                        self.timer_counter()

                elif work == 'stop':
                        self.timer_running = False
                        self.start.configure(state='normal')
                        self.stop.configure(state='disabled')
                        self.reset.configure(state='normal')

                elif work == 'reset':
                        self.timer_running = False
                        self.timer_counter_num = 84000


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Room()
    ui.show()
    sys.exit(app.exec_())

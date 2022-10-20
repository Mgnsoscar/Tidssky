from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Bakgrunnsbilde
from room import Room

#### The main structure of the Graphical User Interface

class GUI(object):

    def setupUi(self, MainWindow):

#### Set the initial size of the main window and remove the window frames

        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        MainWindow.resize(1340, 768)

########################################################################################################################
# Since PyQt5 originally is written for CSS we need to format strings to be displayed correctly in python
# Here we create a variable with a shorter name for that process.
########################################################################################################################

        _translate = QtCore.QCoreApplication.translate

########################################################################################################################
# Make the frame that is going to serve as the main window
########################################################################################################################

        self.centrawidget = QtWidgets.QWidget(MainWindow)
        self.centrawidget.setStyleSheet("background:none;")

        #### Making the grid layout of the frame

        self.drop_shadow_layout = QtWidgets.QVBoxLayout(self.centrawidget)
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)

########################################################################################################################
# Making the frame that is going to serve as the application window
########################################################################################################################

        self.mainwindow = QtWidgets.QFrame(self.centrawidget)

        #### Set corner roundness and background image

        self.mainwindow.setStyleSheet("border-image: url(:/images/Background3.jpg);border-radius: 15px;")

        #### Create the grid layout of the application window. The window is divided into
        #### three frames stacked on topof each other

        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainwindow)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)

########################################################################################################################
# Creating the top frame
########################################################################################################################

        self.top = QtWidgets.QFrame(self.mainwindow)

        #### Set size constraints

        self.top.setMinimumSize(QtCore.QSize(0, 50))
        self.top.setMaximumSize(QtCore.QSize(16777215, 50))

        #### Unable backgrounds so that the main background image is not repeated within this frame

        self.top.setStyleSheet("border-image:none; background:none;")

        #### Create the grid layout of the frame

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.top)
        self.horizontalLayout_3.setContentsMargins(4, 4, 0, 0)
        self.horizontalLayout_3.setSpacing(0)

        ################################################################################################################
        # Creating the frame with the application title
        ################################################################################################################

        self.frame = QtWidgets.QFrame(self.top)
        self.frame.setStyleSheet("background:none;")

        #### Creating the grid layout inside this frame

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)

        #### Creating the label (text box) to display the application title

        self.title = QtWidgets.QLabel(self.frame)

        #### Set size constraints

        self.title.setMinimumSize(QtCore.QSize(300, 0))
        self.title.setMaximumSize(QtCore.QSize(400, 16777215))

        #### Set text to be displayed

        self.title.setText(_translate("MainWindow", "    SUPERLOGISTIKKPROGRAM SATURN 3000X-i"))

        #### Set fonts

        font = QtGui.QFont()
        font.setFamily("Roboto Cn")

        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(False)
        self.title.setFont(font)
        self.title.setStyleSheet(       "border-bottom-right-radius:15px;"      "border-bottom-left-radius:5px;"        "color: rgb(255, 255, 255);"            
                                        "background-color:rgba(0, 0, 0, 120);"  "border-bottom-right-radius:15px;"      "border-top-right-radius:15px;"
                                        "border-bottom-left-radius:0px; font-size:20px;")

        #### Creating yet another layout in the frame so that the title is displayed in the middle verticaly

        self.verticalLayout_2.addWidget(self.title)
        self.horizontalLayout_3.addWidget(self.frame)

########################################################################################################################
# Creating a frame to hold the open, close, and minimize buttons
########################################################################################################################

        self.open_close = QtWidgets.QFrame(self.top)

        #### Size constraints

        self.open_close.setMinimumSize(QtCore.QSize(130, 50))
        self.open_close.setMaximumSize(QtCore.QSize(130, 50))

        #### Set transparent background

        self.open_close.setStyleSheet("background:none")

        ### Set a grid layout

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.open_close)
        self.horizontalLayout_4.setContentsMargins(50, 5, 0, -1)
        self.horizontalLayout_4.setSpacing(0)

        ################################################################################################################
        # Create the minimize button
        ################################################################################################################

        self.minimize = QtWidgets.QPushButton(self.open_close)
        self.minimize.setMinimumSize(QtCore.QSize(16, 16))
        self.minimize.setMaximumSize(QtCore.QSize(16, 16))
        self.minimize.setStyleSheet(""" QPushButton{border-radius:8px;      background-color: rgb(255, 255, 0);}
                                        QPushButton:hover{background-color:rgb(236, 236, 0);}""")

        #### Set the text of the button to nothing

        self.minimize.setText("")

        #### Set alignment within the frame

        self.horizontalLayout_4.addWidget(self.minimize, 0, QtCore.Qt.AlignTop)

        ################################################################################################################
        # Create the maximize button
        ################################################################################################################

        self.maximize = QtWidgets.QPushButton(self.open_close)
        self.maximize.setMinimumSize(QtCore.QSize(16, 16))
        self.maximize.setMaximumSize(QtCore.QSize(16, 16))
        self.maximize.setStyleSheet(""" QPushButton{border-radius:8px;     background-color: rgb(2, 255, 2);}
                                        QPushButton:hover{background-color:rgb(1, 211, 1);}""")

        #### Set the button text to nothing

        self.maximize.setText("")

        #### Set the alignment within the frame

        self.horizontalLayout_4.addWidget(self.maximize, 0, QtCore.Qt.AlignTop)

        ################################################################################################################
        # Create the close button
        ################################################################################################################

        self.close = QtWidgets.QPushButton(self.open_close)
        self.close.setMinimumSize(QtCore.QSize(16, 16))
        self.close.setMaximumSize(QtCore.QSize(16, 16))
        self.close.setStyleSheet("""    QPushButton{border-radius:8px;        background-color: rgb(255, 2, 2);}
                                        QPushButton:hover{background-color:rgb(225, 1, 1);}                     """)

        #### Set button text to nothing

        self.close.setText("")

        #### Set the alignment inside the frame

        self.horizontalLayout_4.addWidget(self.close, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_3.addWidget(self.open_close, 0, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.top)

########################################################################################################################
# Create the middle frame of the application. This is the frame that will contain the main contents of the application
########################################################################################################################

        self.middle = QtWidgets.QFrame(self.mainwindow)
        self.middle.setStyleSheet("border-image:none;   background:none;")

        #### Set the grid layout of the middle frame

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.middle)
        self.verticalLayout_3.setContentsMargins(4, 0, 4, 0)
        self.verticalLayout_3.setSpacing(0)

        ################################################################################################################
        # Create the frame that will contain all of the five room() objects
        ################################################################################################################

        self.Rooms = QtWidgets.QFrame(self.middle)

        #### Set size constraints

        self.Rooms.setMinimumSize(QtCore.QSize(1300, 340))
        self.Rooms.setMaximumSize(QtCore.QSize(16777215, 500))

        #### Set transparent background

        self.Rooms.setStyleSheet("background-color:none;")

        #### Set the grid layout

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Rooms)
        self.horizontalLayout_5.setContentsMargins(0, 20, 0, 4)
        self.horizontalLayout_5.setSpacing(4)
        self.verticalLayout_3.addWidget(self.Rooms)

        ################################################################################################################
        # Create five rooms. The room object is imported from it's own class.
        ################################################################################################################

        #### Make separate variables for each room so they can be modified independently

        self.room1 = Room()
        self.room2 = Room()
        self.room3 = Room()
        self.room4 = Room()
        self.room5 = Room()

        #### Add each room to the layout of self.Rooms

        self.horizontalLayout_5.addWidget(self.room1)
        self.horizontalLayout_5.addWidget(self.room2)
        self.horizontalLayout_5.addWidget(self.room3)
        self.horizontalLayout_5.addWidget(self.room4)
        self.horizontalLayout_5.addWidget(self.room5)

        #### Change the titles of each room (Room nr. 1 already has the correct title)

        self.room2.label_2.setText(_translate("MainWindow", "Injeksjonsrom 2"))
        self.room3.label_2.setText(_translate("MainWindow", "Injeksjonsrom 3"))
        self.room4.label_2.setText(_translate("MainWindow", "Injeksjonsrom 4"))
        self.room5.label_2.setText(_translate("MainWindow", "PET-Scan"))

        #### Countdown display



        ################################################################################################################
        # Create the frame that will contain the other contents in the application
        ################################################################################################################

        self.overview = QtWidgets.QFrame(self.middle)
        self.overview.setMaximumSize(QtCore.QSize(16777215, 8765))

        #### Set background color to be semi-transparent

        self.overview.setStyleSheet("background-color: rgba(0, 0, 0, 80);")

        ### Set grid layout

        self.verticalLayout_3.addWidget(self.overview)
        self.verticalLayout.addWidget(self.middle)

########################################################################################################################
# Create the bottom of the three main frames. This frame will contain the credits and the widget to resize the frame
########################################################################################################################

        self.bottom = QtWidgets.QFrame(self.mainwindow)

        #### Set size constraints

        self.bottom.setMinimumSize(QtCore.QSize(0, 20))
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 20))

        #### Set transparent background

        self.bottom.setStyleSheet("border-image:none;   background:none")

        #### Set grid layout

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bottom)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        #### Create the frame that will contain the credits label

        self.creditframe = QtWidgets.QFrame(self.bottom)

        #### Set transparent background

        self.creditframe.setStyleSheet("border-image:none; background:none;")

        #### Set grid layout

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.creditframe)
        self.horizontalLayout_2.setContentsMargins(7, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        ################################################################################################################
        # Create the text label
        ################################################################################################################

        self.credits = QtWidgets.QLabel(self.creditframe)

        #### Set text to be displayed

        self.credits.setText(_translate("MainWindow", "Av: Silnes, Chewiejczak, Nore, Singh Sidhu, Gripsgård, Støleggen"))

        #### Set font

        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.credits.setFont(font)
        self.credits.setStyleSheet("border-image:none;  background:none; font-size:10px;" "color:rgb(0,0,0,120);")

        ### Set grid of the text label for the text to be aligned properly

        self.horizontalLayout_2.addWidget(self.credits)
        self.horizontalLayout.addWidget(self.creditframe)

        ################################################################################################################
        # Create the frame that will hold the stretching widget
        ################################################################################################################

        self.stretch = QtWidgets.QFrame(self.bottom)

        #### Size constraints

        self.stretch.setMinimumSize(QtCore.QSize(30, 30))
        self.stretch.setMaximumSize(QtCore.QSize(30, 30))

        #### Set transparent background

        self.stretch.setStyleSheet("border-image:none;  background:none;")

        #### Set grid layout

        self.horizontalLayout.addWidget(self.stretch)
        self.verticalLayout.addWidget(self.bottom)

########################################################################################################################
# Something i'm not quite sure what does, but needs to be here for everything to work
########################################################################################################################

        #### I think this adds the mainframe to the application window. Edit: Yes, it does. If this is not activated
        #### Every widget will try to fit into the same spot in the application window

        self.drop_shadow_layout.addWidget(self.mainwindow)

        #### I think this sets the centrawidget as the main widget, the one to contain all other widgets

        MainWindow.setCentralWidget(self.centrawidget)

        #### I searched up this one and had no clue what it meant. It is propably needed is all i could understand

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


def timer_counter(self, label):
        def count():

                if self.timer_running:

                        #### Set color of the frame depending on time left. Green=much time, yellow=less time, red=little time.

                        if self.timer_counter_num <= (60 * 5):
                                self.imgpresized = (Image.open('Images\Red.png'))
                                self.img1 = self.imgpresized.resize((200, 80), Image.ANTIALIAS)
                                self.img = ImageTk.PhotoImage(self.img1)
                                self.timerlabel.configure(image=self.img)

                        if self.timer_counter_num >= (60 * 5):
                                self.imgpresized = (Image.open('Images\yellow.png'))
                                self.img1 = self.imgpresized.resize((200, 80), Image.ANTIALIAS)
                                self.img = ImageTk.PhotoImage(self.img1)
                                self.timerlabel.configure(image=self.img)

                        if self.timer_counter_num >= (60 * 10):
                                self.imgpresized = (Image.open('Images\green.png'))
                                self.img1 = self.imgpresized.resize((200, 80), Image.ANTIALIAS)
                                self.img = ImageTk.PhotoImage(self.img1)
                                self.timerlabel.configure(image=self.img)

                        if self.timer_counter_num == 0:

                                self.timer_running = False
                                self.timer('reset')
                                display = 'Time Is Up'
                                self.timerframe.configure(fg_color='')



                        else:
                                tt = datetime.timedelta(seconds=self.timer_counter_num)
                                display = tt
                                self.timer_counter_num -= 1

                        label.configure(text=display)
                        label.after(1000, count)

        count()
def timer(self, work):

    #### Define what to do if the start button is pressed:

        if work == 'start':

            self.timer_running = True

            if self.timer_counter_num == 0:

                timer_time_str = self.entry.get()
                hours, minutes, seconds = timer_time_str.split(':')
                minutes = int(minutes) + (int(hours) * 60)
                seconds = int(seconds) + (minutes * 60)
                self.timer_counter_num = self.timer_counter_num + seconds

            self.timer_counter(self.timerlabel)
            self.reset.configure(state='disabled')
            self.entry.delete(0, tk.END)
            self.entry.configure(state='disabled')
            self.timerframe.grid_rowconfigure((0,1,2), weight=1)
            self.timerframe.grid_columnconfigure((0,1,2), weight=1)
            self.timerlabel.grid(row=1,column=1)
            self.timerlabel.grid_propagate(False)



            #### Replace start button with stop button upon starting, as well as the starting label

            self.start.grid_forget()
            self.timerlab.grid_forget()
            self.entryframe.grid_forget()
            self.entry.grid_forget()


        elif work == 'stop':
            self.timer_running = False
            self.start.configure(state='normal')
            self.stop.configure(state='disabled')
            self.reset.configure(state='normal')

            #### Replace stop button with start button upon stopping

            self.stop.grid_forget()
            self.start.grid(row=0, column=2, padx=5)

        elif work == 'reset':
            self.timer_running = False
            self.timer_counter_num = 84000
            self.reset.configure(state='disabled')
            self.entry.configure(state='normal')
            self.entry.insert(0, '00:00:00')
            self.timerlabel.configure(text='Timer')


            self.stop.grid_forget()
            self.start.grid(row=0, column=2, padx=5)



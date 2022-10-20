from gui import *
from room import *
from main import *
from gui import *

GLOBAL_STATE = 0

class Ui_Functions(MainWindow):
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        if status == 0:

            self.showMaximized()

            GLOBAL_STATE = 1

            #self.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            self.ui.centrawidget.setStyleSheet("border-radius: 0px;")


        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            #self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
            #self.ui.centrawidget.setStyleSheet("border-radius: 15px;")


    def Ui_definitions(self):

        self.ui.maximize.clicked.connect(lambda: Ui_Functions.maximize_restore(self))






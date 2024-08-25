from PyQt5 import QtCore, QtGui, QtWidgets

import administration_login
# import admin_login
# import driver_login

class Ui_start_here(object):

    # Constructor used to call screen
def __init__(self, Dialog):
    self.Dialog = QtWidgets.QDialog()

    self.start_here_setupUi(self.Dialog)

# Constructor used to show screen
def make_Visible(self):
    self.Dialog.show()

# Constructor used to close screen
def lets_close(self):
    self.Dialog.close()
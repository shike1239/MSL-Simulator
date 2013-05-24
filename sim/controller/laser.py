from PySide import QtGui

class LaserWidget(QtGui.QWidget):
    """This widget allows the user to configure the laser scanner."""
    def __init__(self, parent):
        super(LaserWidget, self).__init__(parent)
        self.loadGUI()

    def loadGUI(self):
        """Load the GUI from the .py file that was generated by the .ui file
        using the pyside-uic tool."""
        # import generated .py file here to prevent circular reference
        from sim.view.laser import Ui_laser
        ui = Ui_laser()
        ui.setupUi(self)


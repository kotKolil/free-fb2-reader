from PyQt6.QtWidgets import QApplication, QWidget

# Only needed for access to command line arguments
import sys


class application(object):

    def __init__(self):
        # You need one (and only one) QApplication instance per application.
        # Pass in sys.argv to allow command line arguments for your app.
        # If you know you won't use command line arguments QApplication([]) works too.
        self.app = QApplication(sys.argv)

        # Create a Qt widget, which will be our window.
        window = QWidget()
        window.show()  # IMPORTANT!!!!! Windows are hidden by default.

    def start(self):
        # Start the event loop.
        self.app.exec()
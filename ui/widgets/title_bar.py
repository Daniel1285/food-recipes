from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout
from PySide6.QtGui import QIcon, QFont, QPixmap, QPalette, QColor
from PySide6.QtCore import Qt, QPoint, QRect


class CustomTitleBar(QWidget):
    """
    Custom title bar widget for the application window.
    """

    def __init__(self, parent=None):
        """
        Initialize the CustomTitleBar widget.

        Args:
            parent: The parent widget. Defaults to None.
        """
        super().__init__(parent)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor("#29323c"))
        self.setStyleSheet("background-color: #29323c;")
        self.setPalette(palette)
        self.setStyleSheet("color: #29323c;")
        self.setFixedHeight(20)
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setWindowFlags(Qt.WindowType.CustomizeWindowHint)

        # Spacer
        self.layout.addStretch()

        style_btn = "background-color: #29323c; color:#fff;"

        # Minimize button
        self.minimize_button = QPushButton("_")
        self.minimize_button.setStyleSheet(style_btn)
        self.minimize_button.clicked.connect(parent.showMinimized)
        self.layout.addWidget(self.minimize_button)

        # Maximize button
        self.maximize_button = QPushButton("□")
        self.maximize_button.setStyleSheet(style_btn)
        self.maximize_button.clicked.connect(self.toggle_maximized)
        self.layout.addWidget(self.maximize_button)

        # Close button
        self.close_button = QPushButton("X")
        self.close_button.setStyleSheet(style_btn)
        self.close_button.clicked.connect(parent.close)
        self.layout.addWidget(self.close_button)

        # Make the title bar draggable
        self.draggable = True
        self.mouse_pos = None

    def mousePressEvent(self, event):
        """Handle mouse press event."""
        if event.button() == Qt.LeftButton and self.draggable:
            self.mouse_pos = event.globalPos() - self.parent().pos()
            event.accept()

    def mouseMoveEvent(self, event):
        """ Handle mouse move event."""
        if event.buttons() == Qt.LeftButton and self.mouse_pos is not None and self.draggable:
            self.parent().move(event.globalPos() - self.mouse_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        """Handle mouse release event."""
        self.mouse_pos = None

    def toggle_maximized(self):
        """Toggle the maximized state of the window."""
        if self.parent().isMaximized():
            self.parent().showNormal()
        else:
            self.parent().showMaximized()

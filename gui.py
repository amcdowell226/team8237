import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox,QLineEdit)
from PySide6.QtCore import Slot  
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from qt_material import apply_stylesheet
from __feature__ import snake_case, true_property


our_app = QApplication([])

class OurWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.set_layout(layout)
        # window_title = "Juicy Jams Maker"
        our_image = QLabel()
        our_image.alignment = Qt.AlignCenter
        # pixmap = QPixmap("images/musical_notes.png")
        pixmap = QPixmap("images/musical_notes.png")

        scaled_pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        our_image.pixmap = scaled_pixmap
        our_image.alignment = Qt.AlignCenter

        our_title = QLabel("<h1>Juicy Jams</h1>")
        our_title.alignment = Qt.AlignCenter
        our_title.style_sheet = "QLabel { color:#2e3d7f; }"

        ent_note = QLineEdit("Enter a Note Value")
        ent_note.minimum_width = 250
        ent_note.select_all()

        play_btn1 = QPushButton("Play")
            # play_btn1.clicked.connect(self.on_play1)

        our_list = ["Choose a effect", "effect1", "effect2", "effect3"]
        our_combo_box = QComboBox()
        our_combo_box.add_items(our_list)

        play_btn2 = QPushButton("Play")
            # play_btn2.clicked.connect(self.on_play2)
        save_btn = QPushButton("Save")
            # save_btn.clicked.connect(self.on_save)

        layout.add_widget(our_image)
        layout.add_widget(our_title)
        layout.add_widget(ent_note)
        layout.add_widget(play_btn1)
        layout.add_widget(our_combo_box)
        layout.add_widget(play_btn2)
        layout.add_widget(save_btn)

        self.resize(500,500)

        # apply_stylesheet(our_app, theme='light_blue.xml')

        extra = {
            'dark_blue': '#2e3d7f',
            'lighter_blue': '#3e51a9 ',
            'light_blue': '#5d72d2 ',
            'font_family': 'Calibri',
        }

        apply_stylesheet(our_app, 'light_blue.xml', invert_secondary=True, extra=extra)
        play_btn1.set_property('class', 'dark_blue')
        play_btn2.set_property('class', 'lighter_blue')
        save_btn.set_property('class', 'light_blue')


# functions for play_btn1,play_btn2, and save_btn
# @Slot()
#     def on_play1(self):
    
# @Slot()
#     def on_play2(self):

# @Slot()
#     def on_save(self):




our_window = OurWindow()
our_window.show()
sys.exit(our_app.exec())
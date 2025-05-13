import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QLineEdit, QFileDialog, QMessageBox)
from PySide6.QtCore import Slot
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QSoundEffect
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt, QUrl
from qt_material import apply_stylesheet
from __feature__ import snake_case, true_property
import audio_effects
import audio
import shutil
import os


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

        self.note_input_container = QVBoxLayout()
        self.num_of_notes = QLineEdit()
        self.num_of_notes.placeholder_text = "How many notes would you like in your jingle? (Minumum: 3, Maximum: 10)"

        submit_btn = QPushButton("Submit")
        submit_btn.clicked.connect(self.create_note_inputs)

        self.note_inputs = []
        save_notes_btn = QPushButton("Save Notes")
        save_notes_btn.clicked.connect(self.save_notes)
        self.saved_notes = []

        self.saved_notes_label = QLabel()

        #maybe not needed but leaving this here in case it is
        ent_note = QLineEdit("Enter a Note Value")
        ent_note.minimum_width = 250
        ent_note.select_all()

        play_btn1 = QPushButton("Play Jingle")
        play_btn1.clicked.connect(self.on_play1)

        our_list = ["Choose an effect", "Flanger", "Wahwah", "Tremolo", "Distortion", "Chorus", "High Pitch", "Low Pitch", "Griffin", "Slow Down", "Speed Up"]
        self.our_combo_box = QComboBox()
        self.our_combo_box.add_items(our_list)

        play_btn2 = QPushButton("Play Affected Jingle")
        play_btn2.clicked.connect(self.on_play2)
        
        save_btn = QPushButton("Save Jingle")
        save_btn.clicked.connect(self.on_save)

        layout.add_widget(our_image)
        layout.add_widget(our_title)
        layout.add_widget(self.num_of_notes)
        layout.add_widget(submit_btn)
        layout.add_layout(self.note_input_container)
        layout.add_widget(save_notes_btn)
        layout.add_widget(self.saved_notes_label)
        #layout.add_widget(ent_note)
        layout.add_widget(play_btn1)
        layout.add_widget(self.our_combo_box)
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
    
    @Slot()
    def create_note_inputs(self):

        while self.note_input_container.count():
            child = self.note_input_container.take_at(0)
            if child.widget():
                child.widget().delete_later()
        self.note_inputs.clear()

        try:
            count = int(self.num_of_notes.text)
            if count < 3 or count > 10:
                self.try_again_label = QLabel()
                self.try_again_label.text = "Please enter a number between 3 and 10."
                self.try_again_label.style_sheet = "color: red;"
                self.note_input_container.add_widget(self.try_again_label)
                return
        except ValueError:
            self.try_again_label = QLabel()
            self.try_again_label.text = "Please enter a valid number only."
            self.try_again_label.style_sheet = "color: red;"
            self.note_input_container.add_widget(self.try_again_label)
            return

        for _ in range(count):
            note_input = QLineEdit()
            note_input.placeholder_text = "Enter a note value"
            self.note_input_container.add_widget(note_input)
            self.note_inputs.append(note_input)

    @Slot()
    def save_notes(self):
        try:
            self.saved_notes = [int(box.text) for box in self.note_inputs]
            self.saved_notes_label.text = f"Saved Notes: {self.saved_notes}"
            self.saved_notes_label.style_sheet = "color: black;"
        except ValueError:
            self.saved_notes_label.text = "Please enter valid integers only."
            self.saved_notes_label.style_sheet = "color: red;"
        #do a check to see if all boxes are filled out




    # functions for play_btn1,play_btn2, and save_btn
    @Slot()
    def on_play1(self):
        if (len(self.saved_notes) == 0):
            return
        else:
            audio.new_wav(1, 'jingle', self.saved_notes)
            self.player = QSoundEffect()
            self.player.source = QUrl.from_local_file("jingle.wav")
            self.player.volume = 0.3
            self.player.play()
            self.last_played_file = "jingle.wav"
    
    @Slot()
    def on_play2(self):
        selection = self.our_combo_box.current_text

        match selection:
            case "Choose an effect":
                self.player.play()
            case "Flanger":
                audio_effects.flanger(audio_effects.x, audio_effects.sr, audio_effects.fx)
                self.player = QSoundEffect()
                self.player.source = QUrl.from_local_file("altered_jingle.wav")
                self.player.volume = 0.3
                self.player.play()
                self.last_played_file = "altered_jingle.wav"
            case "Wahwah":
                audio_effects.wahwah(audio_effects.x, audio_effects.sr, audio_effects.fx)
                self.player = QSoundEffect()
                self.player.source = QUrl.from_local_file("altered_jingle.wav")
                self.player.volume = 0.3
                self.player.play()
                self.last_played_file = "altered_jingle.wav"
            case "Tremolo":
                audio_effects.tremolo(audio_effects.x, audio_effects.sr, audio_effects.fx)
                self.player = QSoundEffect()
                self.player.source = QUrl.from_local_file("altered_jingle.wav")
                self.player.volume = 0.3
                self.player.play()
                self.last_played_file = "altered_jingle.wav"
            case "Distortion":
                audio_effects.distortion(audio_effects.x, audio_effects.sr, audio_effects.fx)
                self.player = QSoundEffect()
                self.player.source = QUrl.from_local_file("altered_jingle.wav")
                self.player.volume = 0.3
                self.player.play()
                self.last_played_file = "altered_jingle.wav"
            case "Chorus":
                audio_effects.chorus(audio_effects.x, audio_effects.sr, audio_effects.fx)
                self.player = QSoundEffect()
                self.player.source = QUrl.from_local_file("altered_jingle.wav")
                self.player.volume = 0.3
                self.player.play()
                self.last_played_file = "altered_jingle.wav"
            case "High Pitch":
                audio_effects.high_pitch(audio_effects.x, audio_effects.sr, audio_effects.fx)
                self.player = QSoundEffect()
                self.player.source = QUrl.from_local_file("altered_jingle.wav")
                self.player.volume = 0.3
                self.player.play()
                self.last_played_file = "altered_jingle.wav"
            case "Low Pitch":
                audio_effects.low_pitch(audio_effects.x, audio_effects.sr, audio_effects.fx)
                self.player = QSoundEffect()
                self.player.source = QUrl.from_local_file("altered_jingle.wav")
                self.player.volume = 0.3
                self.player.play()
                self.last_played_file = "altered_jingle.wav"
            case "Griffin":
                audio_effects.griffin(audio_effects.x, audio_effects.sr, audio_effects.fx)
                self.player = QSoundEffect()
                self.player.source = QUrl.from_local_file("altered_jingle.wav")
                self.player.volume = 0.3
                self.player.play()
                self.last_played_file = "altered_jingle.wav"
            case "Slow Down":
                audio_effects.timestretch_slow(audio_effects.x, audio_effects.sr, audio_effects.fx)
                self.player = QSoundEffect()
                self.player.source = QUrl.from_local_file("altered_jingle.wav")
                self.player.volume = 0.3
                self.player.play()
                self.last_played_file = "altered_jingle.wav"
            case "Speed Up":
                audio_effects.timestretch_fast(audio_effects.x, audio_effects.sr, audio_effects.fx)
                self.player = QSoundEffect()
                self.player.source = QUrl.from_local_file("altered_jingle.wav")
                self.player.volume = 0.3
                self.player.play()
                self.last_played_file = "altered_jingle.wav"

    @Slot()
    def on_save(self):
        if not hasattr(self, "last_played_file"):
            QMessageBox.warning(self, "No file", "No jingle has been created yet.")
            return

        file_path, _ = QFileDialog.get_save_file_name(
            self,
            "Save WAV File",
            self.last_played_file,
            "WAV Files (*.wav);;All Files (*)"
        )

        if file_path:
            try:
                shutil.copy(self.last_played_file, file_path)
                QMessageBox.information(self, "Success", "WAV file saved successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not save WAV file:\n{e}")


our_window = OurWindow()
our_window.show()
sys.exit(our_app.exec())
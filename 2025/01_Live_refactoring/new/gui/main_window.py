from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QLineEdit, QFrame, QSpinBox, QListWidget, QSizePolicy, QSpacerItem,
    QComboBox, QMessageBox
)
from PyQt5.QtGui import QFont

import control.person_management as pm

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.title_font = QFont()
        self.title_font.setBold(True)
        self.title_font.setPointSize(16)

        self.setup_ui()

    def create_left_layout(self) -> QVBoxLayout:
        left_side = QVBoxLayout()

        left_title = QLabel("Add Persons")
        left_title.setFont(self.title_font)
        left_side.addWidget(left_title)

        name_input_layout = QHBoxLayout()
        name_input_layout.addWidget(QLabel("Name:"))
        self.name_input = QLineEdit()
        name_input_layout.addWidget(self.name_input)

        age_input_layout = QHBoxLayout()
        age_input_layout.addWidget(QLabel("Age:"))
        self.age_input = QSpinBox()
        age_input_layout.addWidget(self.age_input)

        add_button = QPushButton("Add")
        add_button.pressed.connect(self.add)
        
        left_side.addLayout(name_input_layout)
        left_side.addLayout(age_input_layout)
        left_side.addWidget(add_button)
        horizontal_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        left_side.addItem(horizontal_spacer)

        return left_side

    def create_right_layout(self) -> QVBoxLayout:
        right_side = QVBoxLayout()
        
        right_title = QLabel("Show Persons")
        right_title.setFont(self.title_font)
        right_side.addWidget(right_title, stretch=0)

        self.person_list = QListWidget()
        right_side.addWidget(self.person_list)

        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel("Name:"))
        self.name_filter = QLineEdit()
        filter_layout.addWidget(self.name_filter)
        filter_layout.addWidget(QLabel("Age:"))
        self.operator_filter = QComboBox()
        self.operator_filter.addItems(["Minimum", "Maximum", "Equals"])
        filter_layout.addWidget(self.operator_filter)
        self.age_filter = QSpinBox()
        filter_layout.addWidget(self.age_filter)
        filter_button = QPushButton("Filter")
        filter_button.pressed.connect(self.filter)
        filter_layout.addWidget(filter_button)
        reset_button = QPushButton("Reset")
        reset_button.pressed.connect(self.reset)
        filter_layout.addWidget(reset_button)

        right_side.addLayout(filter_layout)

        return right_side
        
    def setup_ui(self) -> None:
        main_layout = QHBoxLayout()
        
        left_side = self.create_left_layout()
        right_side = self.create_right_layout()

        self.persons = pm.read()
        self.show_persons()
        
        main_layout.addLayout(left_side)
        sep = QFrame()
        sep.setFrameShape(QFrame.VLine)
        sep.setFrameShadow(QFrame.Plain)
        main_layout.addWidget(sep)
        main_layout.addLayout(right_side)
        self.setLayout(main_layout)

    def show_persons(self, persons: list | None = None):
        self.person_list.clear()

        persons_to_gui = self.persons
        if persons is not None:
            persons_to_gui = persons

        for person in persons_to_gui:
            self.person_list.addItem(f"{person.name}\t{person.age}")

    def add(self) -> None:
        name = self.name_input.text()
        age = self.age_input.value()

        try:
            pm.add(name, age)
            pm.save()
        except pm.NameNotGiven:
            self.create_popup("Wrong input", "Name is empty!")
            return
        except pm.AgeNotGiven:
            self.create_popup("Wrong input", "Age cannot be 0!")
            return
        
        self.name_input.clear()
        self.age_input.setValue(0)

        self.persons = pm.read()
        self.show_persons()

    def filter(self) -> None:
        name_filter = self.name_filter.text()
        age_filter = self.age_filter.value()
        operator_filter = self.operator_filter.currentText()
        
        if name_filter.strip() == "":
            name_filter = None
        if age_filter == 0:
            age_filter = None
        
        filtered_persons = []
        for person in self.persons:
            if name_filter is not None and not person.name.startswith(name_filter):
                continue
            if operator_filter == "Minimum":
                if age_filter is not None and person.age < age_filter:
                    continue
            elif operator_filter == "Maximum":
                if age_filter is not None and person.age > age_filter:
                    continue
            elif operator_filter == "Equals":
                if age_filter is not None and person.age != age_filter:
                    continue
            filtered_persons.append(person)

        self.show_persons(filtered_persons)

    def reset(self) -> None:
        self.name_filter.clear()
        self.age_filter.setValue(0)
        self.operator_filter.setCurrentText("Minimum")
        
        self.show_persons()

    def create_popup(self, title: str, message: str) -> None:
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Critical)
        msg.exec()

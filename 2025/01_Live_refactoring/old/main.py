import os
import sys
import json

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QFrame, QSpinBox, QListWidget, QSizePolicy, QSpacerItem, QComboBox
from PyQt5.QtGui import QFont


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.persons = []

        self.title_font = QFont()
        self.title_font.setBold(True)
        self.title_font.setPointSize(16)

        self.setup_ui()
        self.read_persons()
        
    def setup_ui(self) -> None:
        main_layout = QHBoxLayout()
        
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
        
        main_layout.addLayout(left_side)
        sep = QFrame()
        sep.setFrameShape(QFrame.VLine)
        sep.setFrameShadow(QFrame.Plain)
        main_layout.addWidget(sep)
        main_layout.addLayout(right_side)
        self.setLayout(main_layout)

    def add(self) -> None:
        self.persons.append(
            {
                "Name": self.name_input.text(),
                "Age": self.age_input.value()
            }
        )
        self.name_input.clear()
        self.age_input.setValue(0)

        self.person_list.clear()

        for person in self.persons:
            self.person_list.addItem(f"{person['Name']}\t{person['Age']}")

        self.save_persons()

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
            if name_filter is not None and not person["Name"].startswith(name_filter):
                continue
            if operator_filter == "Minimum":
                if age_filter is not None and person["Age"] < age_filter:
                    continue
            elif operator_filter == "Maximum":
                if age_filter is not None and person["Age"] > age_filter:
                    continue
            elif operator_filter == "Equals":
                if age_filter is not None and person["Age"] != age_filter:
                    continue
            filtered_persons.append(person)

        self.person_list.clear()

        for person in self.persons:
            self.person_list.addItem(f"{person['Name']}\t{person['Age']}")

    def reset(self) -> None:
        self.name_filter.clear()
        self.age_filter.setValue(0)
        self.operator_filter.setCurrentText("Minimum")
        
        self.person_list.clear()

        for person in self.persons:
            self.person_list.addItem(f"{person['Name']}\t{person['Age']}")

    def read_persons(self) -> list:
        if not os.path.exists("persons.json"):
            with open("persons.json", "w") as f:
                json.dump({"Persons": []}, f, indent=4)

        with open("persons.json", "r") as f:
            data = json.load(f)
            self.persons = data["Persons"]

        self.person_list.clear()

        for person in self.persons:
            self.person_list.addItem(f"{person['Name']}\t{person['Age']}")
            
    def save_persons(self) -> None:
        with open("persons.json", "w") as f:
            json.dump({"Persons": self.persons}, f, indent=4)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

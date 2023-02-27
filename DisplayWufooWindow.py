import sys

import requests
from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QListWidget,
    QApplication,
    QListWidgetItem,
    QHBoxLayout,
    QVBoxLayout,
    QLayout,
    QGridLayout,
    QPlainTextEdit,
    QLabel,
    QLineEdit,
    QCheckBox,
)

data_url = " http://127.0.0.1:8000"  # you can put yours in your secrets file so that people don't hit your server to test their programs


class WuFooEntriesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.data = self.get_data(data_url)
        self.list_control: QListWidget = None
        self.data_window = None
        self.prefix_box: QLineEdit = None
        self.fname_box: QLineEdit = None
        self.lname_box: QLineEdit = None
        self.title_box: QLineEdit = None
        self.org_box: QLineEdit = None
        self.email_box: QLineEdit = None
        self.website_box: QLineEdit = None
        self.project_check: QCheckBox = None
        self.speaker_check: QCheckBox = None
        self.visit_check: QCheckBox = None
        self.shadow_check: QCheckBox = None
        self.internship_check: QCheckBox = None
        self.panel_check: QCheckBox = None
        self.network_even_check: QCheckBox = None
        self.subject: QLineEdit = None
        self.description_box: QPlainTextEdit = None
        self.funding: QLineEdit = None
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("GUI Demo for Capstone")
        main_layout = QHBoxLayout()
        self.list_control = QListWidget()
        left_pane = QVBoxLayout()
        main_layout.addLayout(left_pane)
        left_pane.addWidget(self.list_control)
        right_pane = self.build_right_pane()
        self.list_control.resize(400, 400)
        self.list_control.currentItemChanged.connect(self.wufoo_entry_selected)
        self.put_data_in_list(self.data)
        quit_button = QPushButton("Quit")
        quit_button.clicked.connect(QApplication.instance().quit)
        left_pane.addWidget(quit_button)
        main_layout.addLayout(right_pane)
        self.setLayout(main_layout)
        self.show()

    def build_right_pane(self) -> QLayout:
        right_pane = QVBoxLayout()
        one_liners_pane = QGridLayout()
        right_pane.addLayout(one_liners_pane)
        one_liners_pane.addWidget(QLabel("Prefix:"), 0, 0)
        self.prefix_box = QLineEdit()
        self.prefix_box.setReadOnly(True)
        one_liners_pane.addWidget(self.prefix_box, 0, 1)
        one_liners_pane.addWidget(QLabel("Name:"), 0, 2)
        self.fname_box = QLineEdit()
        self.fname_box.setReadOnly(True)
        one_liners_pane.addWidget(self.fname_box, 0, 3)
        self.lname_box = QLineEdit()
        self.lname_box.setReadOnly(True)
        one_liners_pane.addWidget(self.lname_box, 0, 4)
        one_liners_pane.addWidget(QLabel("Title:"), 0, 5)
        self.title_box = QLineEdit()
        self.title_box.setReadOnly(True)
        one_liners_pane.addWidget(self.title_box, 0, 6)
        one_liners_pane.addWidget(QLabel("Organization:"), 1, 0)
        self.org_box = QLineEdit()
        self.org_box.setReadOnly(True)
        one_liners_pane.addWidget(self.org_box, 1, 1)
        one_liners_pane.addWidget(QLabel("email and Website:"), 1, 2)
        self.email_box = QLineEdit()
        self.email_box.setReadOnly(True)
        self.website_box = QLineEdit()
        self.website_box.setReadOnly(True)
        one_liners_pane.addWidget(self.email_box, 1, 3)
        one_liners_pane.addWidget(self.website_box, 1, 4)
        self.project_check = QCheckBox("Course Project")
        self.project_check.setAttribute(Qt.WA_TransparentForMouseEvents)  # don't accept editing
        self.project_check.setFocusPolicy(Qt.NoFocus)  # or keyboard focus
        one_liners_pane.addWidget(self.project_check, 2, 0)
        self.speaker_check = QCheckBox("Guest Speaker")
        self.speaker_check.setAttribute(Qt.WA_TransparentForMouseEvents)  # don't accept editing
        one_liners_pane.addWidget(self.speaker_check, 2, 1)
        self.visit_check = QCheckBox("Site Visit")
        self.visit_check.setAttribute(Qt.WA_TransparentForMouseEvents)  # don't accept editing
        one_liners_pane.addWidget(self.visit_check, 2, 5)
        self.shadow_check = QCheckBox("Job Shadow")
        self.shadow_check.setAttribute(Qt.WA_TransparentForMouseEvents)  # don't accept editing
        one_liners_pane.addWidget(self.shadow_check, 2, 3)
        self.internship_check = QCheckBox("Internship")
        self.internship_check.setAttribute(Qt.WA_TransparentForMouseEvents)  # don't accept editing
        one_liners_pane.addWidget(self.internship_check, 2, 4)
        self.panel_check = QCheckBox("Career Panel")
        self.panel_check.setAttribute(Qt.WA_TransparentForMouseEvents)  # don't accept editing
        one_liners_pane.addWidget(self.panel_check, 2, 2)
        self.network_even_check = QCheckBox("Networking Event")
        self.network_even_check.setAttribute(Qt.WA_TransparentForMouseEvents)  # don't accept editing
        one_liners_pane.addWidget(self.network_even_check, 2, 6)
        one_liners_pane.addWidget(QLabel("Funding:"), 3, 0)
        self.funding = QLineEdit()
        self.funding.setReadOnly(True)
        one_liners_pane.addWidget(self.funding, 3, 1)
        one_liners_pane.addWidget(QLabel("Subject Area:"), 3, 2)
        self.subject = QLineEdit()
        self.subject.setReadOnly(True)
        one_liners_pane.addWidget(self.subject, 3, 3)
        bottom_pane = QHBoxLayout()
        self.description_box = QPlainTextEdit()
        self.description_box.setReadOnly(True)
        self.description_box.resize(200, 400)
        bottom_pane.addWidget(QLabel("Course Project Description:"))
        bottom_pane.addWidget(self.description_box)
        right_pane.addLayout(bottom_pane)
        return right_pane

    def get_data(self, server_url):
        """This is the grad version, for the undergrad version
        For the undergrad version, look at get_cubes_data_from_db() in cubes-api.py
        that is how you would get the data for the list for the undergrads"""
        response = requests.get(server_url)
        if response.status_code != 200:  # if we don't get an ok response we have trouble
            print(
                f"Failed to get data, response code:{response.status_code} and error message: {response.reason} "
            )
            sys.exit(-1)
        jsonresponse = response.json()
        return jsonresponse

    def put_data_in_list(self, data_to_add):
        for item in data_to_add:
            display_text = f"{item['first_name']}  {item['last_name']} : {item['org']}"
            list_item = QListWidgetItem(display_text, listview=self.list_control)
            list_item.setData(1, item)  # lets put the dictionary for later use

    def wufoo_entry_selected(self, current: QListWidgetItem, previous: QListWidgetItem):
        selected_data = current.data(1)  # we put the full record in data role 1
        self.prefix_box.setText(selected_data["prefix"])
        self.fname_box.setText(selected_data["first_name"])
        self.lname_box.setText(selected_data["last_name"])
        self.title_box.setText(selected_data["title"])
        self.org_box.setText(selected_data["org"])
        self.email_box.setText(selected_data["email"])
        self.website_box.setText(selected_data["website"])
        self.project_check.setChecked(selected_data["course_project"])
        self.speaker_check.setChecked(selected_data["guest_speaker"])
        self.visit_check.setChecked(selected_data["site_visit"])
        self.shadow_check.setChecked(selected_data["job_shadow"])
        self.internship_check.setChecked(selected_data["internship"])
        self.panel_check.setChecked(selected_data["career_panel"])
        self.network_even_check.setChecked(selected_data["networking_event"])
        self.subject.setText(selected_data["subject_area"])
        self.description_box.setPlainText(selected_data["description"])
        self.funding.setText(selected_data["funding"])

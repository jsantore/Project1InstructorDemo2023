import sys

import requests
from PySide6.QtWidgets import QWidget, QPushButton, QListWidget, QApplication, QListWidgetItem, \
    QHBoxLayout,QVBoxLayout, QLayout, QGridLayout, QPlainTextEdit, QLabel, QLineEdit, QCheckBox

data_url = " http://127.0.0.1:8000" #you can put yours in your secrets file so that people don't hit your server to test their programs
class WuFooEntriesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.data = self.get_data(data_url)
        self.list_control = None
        self.setup_window()
        self.data_window = None
        self.prefix_box = None
        self.fname_box = None
        self.lname_box = None
        self.title_box = None
        self.org_box = None
        self.email_box = None
        self.website_box = None
        self.project_check = None
        self.speaker_check = None
        self.visit_check = None
        self.shadow_check = None
        self.internship_check = None
        self.panel_check = None
        self.network_even_check = None
        self.subject = None
        self.description_box = None
        self.funding = None

    def setup_window(self):
        self.setWindowTitle("GUI Demo for Capstone")
        main_layout = QHBoxLayout()
        self.list_control = QListWidget()
        left_pane = QVBoxLayout()
        main_layout.addLayout(left_pane)
        left_pane.addWidget(self.list_control)
        #list_size = QSizePolicy()
        #list_size.setVerticalStretch(4)
        #self.list_control.setSizePolicy(list_size)
        self.list_control.resize(400, 400)
        self.put_data_in_list(self.data)
        quit_button  = QPushButton("Quit")
        quit_button.clicked.connect(QApplication.instance().quit)
        left_pane.addWidget(quit_button)
        right_pane = self.build_right_pane()
        main_layout.addLayout(right_pane)
        self.setLayout(main_layout)
        self.show()


    def build_right_pane(self)->QLayout:


        right_pane = QVBoxLayout()
        one_liners_pane = QGridLayout()
        right_pane.addLayout(one_liners_pane)
        one_liners_pane.addWidget(QLabel("Prefix:"),0,0)
        self.prefix_box = QLineEdit()
        one_liners_pane.addWidget(self.prefix_box, 0,1)
        one_liners_pane.addWidget(QLabel("Name:"), 0,2)
        self.fname_box = QLineEdit()
        one_liners_pane.addWidget(self.fname_box, 0,3)
        self.lname_box = QLineEdit()
        one_liners_pane.addWidget(self.lname_box, 0,4)
        one_liners_pane.addWidget(QLabel("Title:"),0,5)
        self.title_box = QLineEdit()
        one_liners_pane.addWidget(self.title_box, 0,6)
        one_liners_pane.addWidget(QLabel("Organization:"),1,0)
        self.org_box = QLineEdit()
        one_liners_pane.addWidget(self.org_box, 1,1)
        one_liners_pane.addWidget(QLabel("email and Website:"), 1,2)
        self.email_box = QLineEdit()
        self.website_box = QLineEdit()
        one_liners_pane.addWidget(self.email_box, 1,3)
        one_liners_pane.addWidget(self.website_box, 1,4)
        self.project_check = QCheckBox("Course Project")
        one_liners_pane.addWidget(self.project_check,2,0)
        self.speaker_check = QCheckBox("Guest Speaker")
        one_liners_pane.addWidget(self.speaker_check, 2,1)
        self.visit_check = QCheckBox("Site Visit")
        one_liners_pane.addWidget(self.visit_check, 2,5)
        self.shadow_check = QCheckBox("Job Shadow")
        one_liners_pane.addWidget(self.shadow_check, 2,3)
        self.internship_check = QCheckBox("Internship")
        one_liners_pane.addWidget(self.internship_check,2,4)
        self.panel_check = QCheckBox("Career Panel")
        one_liners_pane.addWidget(self.panel_check, 2,2)
        self.network_even_check = QCheckBox("Networking Event")
        one_liners_pane.addWidget(self.network_even_check, 2,6)
        one_liners_pane.addWidget(QLabel("Funding:"), 3,0)
        self.funding = QLineEdit()
        one_liners_pane.addWidget(self.funding, 3,1)
        one_liners_pane.addWidget(QLabel("Subject Area:"), 3,2)
        self.subject = QLineEdit()
        one_liners_pane.addWidget(self.subject, 3,3)
        bottom_pane = QHBoxLayout()
        self.description_box = QPlainTextEdit()
        self.description_box.resize(200, 400)
        bottom_pane.addWidget(QLabel("Course Project Description:"))
        bottom_pane.addWidget(self.description_box)
        right_pane.addLayout(bottom_pane)
        return right_pane


    def get_data(self, server_url):
        '''This is the grad version, for the undergrad version
         For the undergrad version, look at get_cubes_data_from_db() in cubes-api.py
         that is how you would get the data for the list for the undergrads'''
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


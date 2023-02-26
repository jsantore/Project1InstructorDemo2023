import sys

import requests
from PySide6.QtWidgets import QWidget, QPushButton, QListWidget, QApplication, QListWidgetItem, QHBoxLayout,QVBoxLayout, QLayout, QGridLayout

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
        right_pane = QGridLayout()

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


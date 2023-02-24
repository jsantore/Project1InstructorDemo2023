import sys

import requests
from PySide6.QtWidgets import QWidget, QPushButton, QListWidget, QApplication, QListWidgetItem, QMessageBox

data_url = " http://127.0.0.1:8000"
class WuFooEntriesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.data = self.get_data(data_url)
        self.list_control = None
        self.setup_window()
        self.data_window = None

    def setup_window(self):
        self.setWindowTitle("GUI Demo for Capstone")
        self.list_control = QListWidget(self)
        self.put_data_in_list(self.data)
        self.show()

    def get_data(self, server_url):
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


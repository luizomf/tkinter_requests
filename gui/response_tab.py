import json
from gui.main_window import MainWindow
from gui.tk_frame import TkFrame
from gui.tkinter_helpers import grid_element
# from infra.requests_adapter import RequestsAdapter
# import tkinter.messagebox


class ResponseTab:
    def __init__(self, main_window: MainWindow):
        self.main_window = main_window

    def start(self):
        self.tkFrame: TkFrame = TkFrame(self.main_window, 'Resposta')

    def show(self, response):
        row = 0
        grid_element(
            self.tkFrame.add_label('Response:'),
            row=row,
            column=0
        )
        grid_element(
            self.tkFrame.add_label(response.status_code),
            row=row,
            column=1
        )

        row += 1
        grid_element(
            self.tkFrame.add_label('Reason:'),
            row=row,
            column=0
        )
        grid_element(
            self.tkFrame.add_label(response.reason),
            row=row,
            column=1
        )

        row += 1
        grid_element(
            self.tkFrame.add_label('Text:'),
            row=row,
            column=0
        )
        text = self.tkFrame.add_text()
        text.insert('1.0', response.text)
        grid_element(
            text,
            row=row,
            column=1
        )

        try:
            row += 1
            grid_element(
                self.tkFrame.add_label('JSON:'),
                row=row,
                column=0
            )
            rjson = self.tkFrame.add_text()
            response_json = json.dumps(response.json(), indent=2)
            rjson.insert('1.0', response_json)
            rjson.configure(height=20)
            grid_element(
                rjson,
                row=row,
                column=1
            )
        except Exception:
            ...

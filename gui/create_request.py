import tkinter.messagebox
import json
from gui.tkinter_helpers import grid_element
from gui.main_window import MainWindow
from gui.tk_frame import TkFrame
from infra.requests_adapter import RequestsAdapter


class CreateRequest:
    def __init__(self, main_window: MainWindow, response_tab=None):
        self.main_window = main_window
        self.response_tab = response_tab

    def start(self):
        self.tkFrame: TkFrame = TkFrame(
            self.main_window, 'Cria requisição')
        self._last_files_row = 0
        self.setup()
        self.add_fields()

    def setup(self):
        self.tkFrame.frame.grid_columnconfigure(1, weight=1)

    def _add_files(self, row, column, parent=None):
        row = self._last_files_row

        entry_campo, entry_campo_str = self.tkFrame.add_entry(
            parent=parent
        )
        grid_element(entry_campo, row=row, column=column)

        entry_caminho, entry_caminho_str = self.tkFrame.add_entry(
            parent=parent
        )
        grid_element(entry_caminho, row=row, column=column + 1)

        button, button_string_var = self.tkFrame.add_file_dialog(
            text='Buscar', parent=parent
        )
        grid_element(button, row=row, column=column + 2)

        button_string_var.trace(
            'w',
            lambda *_: entry_caminho_str.set(button_string_var.get())
        )

        self._last_files_row += 1

    def add_fields(self):
        row = 0
        url_label = self.tkFrame.add_label('URL:')
        url, url_string_var = self.tkFrame.add_entry()
        grid_element(url_label, row=row, column=0)
        grid_element(url, row=row, column=1)

        row = row + 1
        data_label = self.tkFrame.add_label('Campos (JSON): ')
        data = self.tkFrame.add_text()
        grid_element(data_label, row=row, column=0)
        grid_element(data, row=row, column=1)

        row = row + 1
        headers_label = self.tkFrame.add_label('Headers: ')
        headers = self.tkFrame.add_text()
        grid_element(headers_label, row=row, column=0)
        grid_element(headers, row=row, column=1)

        row = row + 1
        options = ['GET', 'POST', 'PUT', 'DELETE']
        method_label = self.tkFrame.add_label('Método: ')
        method, method_string_var = self.tkFrame.add_dropdown(options=options)
        grid_element(method_label, row=row, column=0)
        grid_element(method, row=row, column=1)

        row = row + 1
        options = ['application/json', 'multipart/form-data']
        content_type_label = self.tkFrame.add_label('Content-Type: ')
        content_type, content_type_stringvar = self.tkFrame.add_dropdown(
            options=options
        )
        grid_element(content_type_label, row=row, column=0)
        grid_element(content_type, row=row, column=1)

        row = row + 1
        files_label = self.tkFrame.add_label('Arquivo(s): ')
        grid_element(files_label, row=row, column=0)

        files_frame = self.tkFrame.add_frame()
        files_frame.configure(background='#FFF')
        files_frame.grid_columnconfigure(1, weight=1)
        grid_element(files_frame, row=row, column=0, columnspan=2)

        self._add_files(row=1, column=0, parent=files_frame)

        row = row + 1
        more_fields = self.tkFrame.add_button(
            'Adicionar mais campos de arquivos'
        )
        grid_element(
            more_fields, row=row, column=0,
            columnspan=2, sticky='we'
        )
        more_fields.configure(
            command=lambda: self._add_files(2, 0, files_frame)
        )

        row = row + 1
        send_request = self.tkFrame.add_button('Enviar Requisição')
        grid_element(
            send_request, row=row, column=0,
            columnspan=2, sticky='e'
        )
        send_request.configure(
            command=lambda: self._send_request_comand(
                url_string_var.get(), data.get('1.0', 'end'),
                method_string_var.get(), content_type_stringvar.get(),
                headers.get('1.0', 'end'),
                files_frame, send_request
            )
        )

        url_string_var.set('http://192.168.0.111:3001/')
        data.insert('1.0', '{\n  "nome": "luiz"\n}')
        headers.insert('1.0', '{\n  "authorization": "Bearer luiz"\n}')

    def _send_request_comand(
        self, url, data, method, content_type, headers, files_frame, button
    ):
        paths = []
        files_frame_children = list(files_frame.children.values())

        files_frame_children = [
            x for x in files_frame_children if 'button' not in str(x)
        ]

        for index, entry in enumerate(files_frame_children):
            if index % 2 == 0:
                paths.append(
                    (
                        files_frame_children[index].get(),
                        files_frame_children[index + 1].get()
                    )
                )

        try:
            request = RequestsAdapter(
                url, data, method, content_type, headers, paths
            )
            self.response_tab.show(request.response)
            self.main_window.tab_parent.select(1)
        except (ValueError, json.decoder.JSONDecodeError) as e:
            tkinter.messagebox.showerror(title='Erro', message=e)

from gui.main_window import MainWindow
from gui.create_request import CreateRequest
from gui.response_tab import ResponseTab

if __name__ == "__main__":
    mw = MainWindow('Requests Testing')
    response_tab = ResponseTab(mw)
    create_request = CreateRequest(mw, response_tab)

    create_request.start()
    response_tab.start()

    mw.mainloop()

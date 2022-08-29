import PySimpleGUI as sg

class err(BaseException):
    def __init__(self, msg,code):
        self.msg = msg
        self.code = code
    def notify(self):
        sg.popup(self.msg, title='Exception', auto_close=True, auto_close_duration=7)
        return self.code

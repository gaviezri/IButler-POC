import PySimpleGUI as sg

class Performance_Tester_Layout_container:
#WIP - not working yet
    coarselayout = [
        [sg.Text("Choose the solution"), sg.Text("Choose the compiler")],
        [sg.InputCombo("", size=(15,2)), sg.InputCombo("", size=(15,2))],
        [sg.Checkbox("flag1")],
        [sg.Checkbox("flag2")],
        [sg.Checkbox("flag2")],
        [sg.Checkbox("flag4")],
        [sg.Button("Build"), sg.Button("Rebuild"), sg.Button("Clean")],
        [sg.HorizontalSeparator()]
    ]
    def getlayout():
        return Performance_Tester_Layout_container.coarselayout
import PySimpleGUI as sg

sg.theme("Black")
#layout container for Executer tab
class Executer_Layout_container:
    task_settings = [
        [sg.Text("Choose the solution",text_color='#02f0b9'), sg.Text("Choose the compiler",text_color='#02f0b9'), sg.Text("Choose build type",text_color='#02f0b9')],
        [sg.InputCombo("", size=(15,2),key='exec_solution_choice'), sg.InputCombo(["IBconsole","MSBuild"], size=(15,2),key ='exec_compiler_choice',enable_events=True),sg.InputCombo(["Release","Debug"], size=(15,2),key ='exec_build_type_choice')],
        [sg.HorizontalSeparator()] 
        ]
    task_definition = [   
        [sg.Button("Build",key='exec_Build'), sg.Button("Rebuild",key='exec_Rebuild'), sg.Button("Clean",key='exec_Clean'), sg.Button("Cancel",key='exec_Cancel')],
        [sg.HorizontalSeparator()]
    ]
    command_box = [
        [sg.Text("Command line",text_color='#02f0b9',key='exec_command_line')],
        [sg.InputText(size=(50,30),key='exec_command_line_input')],
    ]

    def getlayout():
       
        return Executer_Layout_container.task_settings+Executer_Layout_container.task_definition+Executer_Layout_container.command_box
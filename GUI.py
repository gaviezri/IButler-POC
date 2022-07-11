import GUIcontainer as GUI
import Executer
import PySimpleGUI as sg
import sys 

#IB_CommandLine = r'https://docs.incredibuild.com/win/v9/windows/ibconsole_cli_options.html?Highlight=command'

# [sg.Button("Click for More details about IBconsole")]


window = sg.Window("IButler",GUI.tab_group,icon='.\\pics_fonts\\IBicon.ico')

def generateCLIstring():
    #cmdstring will be the input for cmdline as the return value of this function
    cmdstring =''
    #events comes from both tabs (no differentiating between the active one)
    #differentiate by prefix - exec_blabla or perf_blabla
    #
    while True:
        event, values = window.read(timeout=100)
        if event == 'Exit':
            return None
        if event == 'exec_compiler_choice':
            compiler = values['exec_compiler_choice']
            cmdstring = Executer.choose_flags(compiler+'.exe')
        if event == 'build_type_choice':
            return

generateCLIstring()




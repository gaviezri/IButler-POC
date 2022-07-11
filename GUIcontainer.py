from Executer_Layout import Executer_Layout_container as Executer
from Performance_Tester_Layout import Performance_Tester_Layout_container as PerfTest 
import PySimpleGUI as sg\
    
#container for both tabs
tab_group = [
                [sg.TabGroup(
                    [[sg.Tab('Executer',Executer.getlayout(), background_color='#709053',element_justification='center',key='executer_tab')],
                    [sg.Tab('Performance Tester', PerfTest.getlayout(), background_color='Red',key='perf_tab')]],
                    tab_location='centertop',
                    title_color='Red', tab_background_color='Purple', selected_title_color='Green',
                    selected_background_color='Gray', border_width=5), sg.Button('Exit')]
]
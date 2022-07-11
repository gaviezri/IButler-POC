from msilib.schema import Icon
import PySimpleGUI as PSG # wink for all soccer fans

PSG.theme('Black')
PSG.Titlebar(title = 'IButler v1.0',text_color='#02f0b9',background_color='Black')


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
layout = [[PSG.Text('Welcome, Incredibuilder. \n let\'s do something Incredible'
,text_color='#02f0b9',font='../IButler_UI/pics_fonts/KdamThmorPro-Regular.ttf',auto_size_text=True)]element_justification='center']
"""
divide into columns
need a designated file for each column
   
"""
def set_layout(layout):
    window = PSG.Window('IButler',layout,size=(1200,500),resizable=True)
    window.set_icon('../IButler_UI/pics_fonts/IBicon.ico')
    return window

window = set_layout(layout)


while True :
    event, values = window.read()
    if event == PSG.WINDOW_CLOSED:
        break
    

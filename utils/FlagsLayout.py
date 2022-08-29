from turtle import back
import PySimpleGUI as sg

class FlagsLayout():
    def __init__():
        pass

    def generateTextInputBrowse(inptext:str,inptooltip:str,inputkey:str):
        return [
                sg.Text(inptext, tooltip=inptooltip, background_color='black', text_color='#02f0b9'),
                sg.Input('', key=inputkey),
                sg.FilesBrowse()
               ]

    def generateCheckBox(inptext:str,inptooltip:str,inputkey:str):
        return [
                sg.Checkbox(inptext, tooltip=inptooltip,key=inputkey,
                           background_color='black', text_color='#02f0b9')
               ]

    def generateRadioGroup(inptext:str,inptooltip:str,grptag:str,*titles_keys):
        group = [sg.Text(inptext,tooltip=inptooltip, background_color='black', text_color='#02f0b9')]
        for title,i_key in titles_keys:
            group.append(sg.Radio(title,group_id=grptag,key=i_key, background_color='black', text_color='#02f0b9'))
        
        return group

    def generateTextInput(inptext:str, inptooltip:str, inputkey:str):
        return [
                sg.Text(inptext,tooltip=inptooltip,background_color='black', text_color='#02f0b9'),
                sg.Input('',key=inputkey,size=(15,1))  
               ]

    def generateCheckBoxInput(inptext:str, inptooltip:str, checkboxkey:str,*titles_keys):
        group = [sg.Checkbox(inptext, tooltip=inptooltip,key=checkboxkey, background_color='black',text_color='#02f0b9')]
        for title,i_key in titles_keys:
            group.append(sg.Input(title,key=i_key,do_not_clear=False,size=(15,1)))
        return group
        
    def generateCheckBoxInputBrowse(inptext:str,inptooltip:str,checkboxkey:str,inpkey:str):
        return [
                sg.Checkbox(inptext, tooltip=inptooltip,key=checkboxkey, background_color='black', text_color='#02f0b9'),
                sg.Input('',size=(15,1), key=inpkey),
                sg.FilesBrowse()
               ]
    
    def generateTextSpin(inptext:str, inptooltip:str, spinkey:str, values:list):
        return [
                sg.Text(inptext, tooltip=inptooltip, background_color='black', text_color='#02f0b9'),
                sg.Spin(values,initial_value=values[0],size=(4,1),key=spinkey,background_color='black',text_color='#02f0b9')
               ]
            

    



from ExecutedCommandsKeeper import ExecutedCommandsKeeper as ECK
import PySimpleGUI as sg
from layouts import ExecuterLayout as EL,  IBFlagsLayout as IBF , \
                    RegistriesLayout as RL , MSBuildflagsLayout as MSF



from utils import Constants as C
sg.theme('Dark')

RunningCommandmainwindow = sg.Column([[sg.pin(sg.Multiline(size=(80, 30), echo_stdout_stderr=True,
                       key=C.EX_OUTPUT_KEY, visible=False, write_only=True,
                       do_not_clear=False, sbar_background_color='Black',
                       expand_y=True))]],element_justification='center')

TabGroup = sg.Frame('At Your Service',[[sg.TabGroup([
                            [sg.Tab('Exectuer', EL.layout,
                                   background_color='Black',
                                   element_justification='center')],\
                            # [sg.Tab('Performance Tester')],
                            [sg.Tab('Quick Registrator', RL.layout,
                                      background_color='Black',
                                        element_justification='left')],
                            [sg.Tab('Help', [[sg.Button('About')]])]],\
                                    tab_location='centertop',
                                    title_color='#02f0b9',
                                    tab_background_color='Black',
                                    selected_title_color='White',\
                                    selected_background_color='Black',
                                    border_width=2)
                       ]],element_justification='center',title_color='#02f0b9')

MainLayout = [  
                [TabGroup],
                [RunningCommandmainwindow]
             ]



# This class is required because the layout cannot be reused for multiple windows
# with this shitty framework (PySimpleGUI)

IBFL = IBF.IBFlagsLayout
# MSFL = MSF.MSBuildflagsLayout
class LayoutManager:
    def __init__(self):
        self.Mainlayout = MainLayout
   
    def generateLastExecutedCommandsLayout(self, ExecutedCommands:ECK):
        LastCommands =  [[sg.Column([[sg.Column([[sg.Text('Copy',text_color='#02f0b9')]],element_justification='left'),
                                      sg.Column([[sg.Text('Command',text_color='#02f0b9')]],expand_x=True,element_justification='center'),
                                      sg.Column([[sg.Text('Duration',text_color='#02f0b9')]],element_justification='right')]],
                                      element_justification='center',expand_x=True)],
                         [sg.HorizontalSeparator(pad=(10,10),color='DarkBlack')],
                         [sg.Column([[sg.Button(f'#{i}', tooltip=f'copy command #{i}',key=C.EX_COPY_KEY+f'{i}-',button_color=('#02f0b9','Black')),
                                      sg.Text(ExecutedCommands.getCommand(i-1).raw_cmd,key=C.EX_EXECUTED_COMMAND_KEY+f'{i}-',expand_x=True,text_color='#02f0b9'),
                                      sg.Text(ExecutedCommands.getCommand(i-1).duration if ExecutedCommands.getCommand(i-1).duration > 0
                                                                                        else 'Running...',
                                             key=C.EX_EXECUTED_DURATION_KEY+f'{i}-',text_color='#02f0b9')]
                                    for i in range(ExecutedCommands.getNumberOfCommands(), 0, -1)],   
                                    key=C.EX_EXEC_DUR_COL_KEY, element_justification='left',expand_x=True,expand_y=True)]]

        LastExecutedCommandsLayout = [sg.Column([[sg.Text('Last executed commands',text_color='#02f0b9',background_color='Black')],
                                     [sg.Column(LastCommands,element_justification='center')]],
                                         element_justification='center',background_color='Black',
                                         scrollable=True,sbar_background_color='Black',sbar_arrow_color='#02f0b9',expand_y=True)]

        return LastExecutedCommandsLayout

    def generateFlagsInterfaceLayout(self,Comp):
        LAYOUT = IBFL().getLayout() #if Comp == 'BuildConsole'
                                    #else MSBFL().getLayout()
        return [sg.Column([[sg.Button('Submit', key=C.EX_SUBMIT_KEY)],
                           [sg.HorizontalSeparator()],
                           [sg.Column(LAYOUT, visible=False,
                                      key=C.EX_IBFLAGS_KEY,
                                      scrollable=True, background_color='Black',
                                      sbar_background_color='Black',
                                      element_justification='left',
                                      expand_x=True, expand_y=True,
                                      vertical_scroll_only=True,size=(550, 300),sbar_arrow_color='#02f0b9'
                                      )],
                            [sg.Column([[sg.Button('placeholderMSBuild', size=(5, 5),
                                       key=C.EX_MSBUILDFLAGS_KEY,
                                       visible=False)]])]],
                          element_justification='center',
                          background_color='Black',
                          key=C.EX_FLAGS_INTERFACE_KEY,expand_y=True)]
        
        
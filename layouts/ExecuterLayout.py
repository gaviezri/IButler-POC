from cgitb import text
from utils import Constants as C, SlnHandlers as SF
import PySimpleGUI as sg

slnTitle = sg.Text("Solution", text_color='#02f0b9', background_color='black')
slnDropDown = sg.DropDown(values=list(SF.SlnFinder().Get_Sln_Dict().keys()),
                          button_background_color='Black',
                          expand_x=True, key=C.EX_SLN_DROP_KEY, enable_events=True,
                          button_arrow_color='#02f0b9',readonly=True)

slnBrowse = sg.FilesBrowse(key=C.EX_SLN_BROWSE_KEY, enable_events=True,
                           button_color=('#02f0b9','Black'))

compilerTitle = sg.Text("Compiler", text_color='#02f0b9',
                        background_color='black')
compilerDropDown = sg.DropDown(["BuildConsole", "MSBuild"],
                               button_background_color='black',
                               key=C.EX_COMP_KEY, expand_x=True,
                               enable_events=True, readonly=True,
                               button_arrow_color='#02f0b9')

buildtypeTitle = sg.Text("Build Type", text_color='#02f0b9',
                         background_color='black')
buildtypeDropDown = sg.DropDown([], button_background_color='black',
                                key=C.EX_BUILD_TYPE_KEY,
                                expand_x=True, enable_events=True,
                                readonly=True, disabled=True,
                                button_arrow_color='#02f0b9')


showHistoryBTN = sg.Button('Show History',
                           key=C.EX_SHOW_EXECUTED_COMMANDS_KEY,
                           button_color=('#02f0b9','Black'), enable_events=True,
                           visible=True)
buildBTN = sg.Button("Build", key=C.EX_BUILD_KEY, button_color=('#02f0b9','Black'),
                     disabled=True, enable_events=True)
rebuildBTN = sg.Button("Rebuild", key=C.EX_REBUILD_KEY, button_color=('#02f0b9','Black'),
                       disabled=True, enable_events=True)
cleanBTN = sg.Button("Clean", key=C.EX_CLEAN_KEY, button_color=('#02f0b9','Black'),
                     disabled=True, enable_events=True)
cancelBTN = sg.Button("Cancel", key=C.EX_CANCEL_KEY, button_color=('#02f0b9','Black'),
                      enable_events=True, disabled=True)
clearBTN = sg.Button("Clear", key=C.EX_CLEAR_KEY, button_color=('#02f0b9','Black'),
                     enable_events=True, disabled=True)
chooseFlagsBTN = sg.Button("Choose Flags", key=C.EX_CHOOSE_FLAGS_KEY,
                           button_color=('#02f0b9','Black'), enable_events=True,
                           disabled=True)
CLITitle = sg.Text("Command line", text_color='#02f0b9',
                   background_color='black')
CLIinput = sg.Input(size=(50, 30), key=C.EX_CLI_INPUT_KEY,
                    background_color='white', enable_events=True)
CLIEnter = sg.Button("Enter", key=C.EX_CLI_ENTER_KEY, button_color=('#02f0b9','Black'),
                     enable_events=True, disabled=True)
ToggleOutputBTN = sg.Button('Toggle Output',key=C.EX_TOGGLE_OUTPUT_KEY,
                            enable_events=True,button_color=('#02f0b9','Black'))

Controllers = sg.Column([[showHistoryBTN, clearBTN, chooseFlagsBTN, buildBTN,
                        rebuildBTN, cleanBTN, cancelBTN]],
                        key=C.EX_BUILD_CONTROLLERS_COL_KEY,
                        element_justification='right',
                        background_color='black')

layout = [
          [slnTitle, slnDropDown, slnBrowse],
          [compilerTitle, compilerDropDown],
          [buildtypeTitle, buildtypeDropDown],
          #[sg.HorizontalSeparator(color='#02ffb9')],
          [Controllers],
          [sg.HorizontalSeparator(color='#02ffb9')],
          [CLITitle],
          [CLIinput, CLIEnter],
          [ToggleOutputBTN]
          ]

# for elem in layout:
# sg.pin(elem,shrink=True)

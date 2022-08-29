import PySimpleGUI as sg
from utils import Constants as C

layout = [
                        [
                            sg.Button('set Dev = ', key=C.REG_DEV_KEY, button_color=('#02f0b9','Black'), pad=(10,20),
                                    tooltip='if Dev==1 \'Dev\' tab will appear in Agent\'s navigation bar.\nIf Dev==0 \'Dev\' tab will be hidden.',
                                    enable_events=True),
                            sg.Spin(values=[0,1], initial_value=1, key=C.REG_DEV_SPIN_KEY, size=(3,10), readonly=True)
                        ],
                        [
                            sg.HorizontalSeparator(pad=(10,10),color='#02ffb9')
                        ],
                        [
                            sg.Button('UAT EKS', key=C.REG_UAT_KEY, button_color=('#02f0b9','Black'), pad=(10,20),enable_events=True),
                            sg.Input(default_text='CoordID', text_color='black', key=C.REG_UAT_INPUT_KEY, size=(20,3)),
                            sg.Checkbox('Restart IB Coord service', key=C.REG_UAT_RESTART_KEY,background_color='black',text_color='#02f0b9')
                        ],
                        [
                            sg.HorizontalSeparator(pad=(10,10),color='#02ffb9')
                        ],
                        [
                            sg.Button('set ClangPathConvert = ', tooltip='to allow buildconsole execute Ninja builds, set to \'3\'', pad=(10,20),
                                      key=C.REG_CLANG_PATH_CONVERT_KEY, button_color=('#02f0b9','Black'), enable_events=True),
                            sg.Spin(values=[0,1,2,3], initial_value=0, key=C.REG_CLANG_PATH_CONVERT_SPIN_KEY, size=(3,10), readonly=True)
                        ]

                     
            ]

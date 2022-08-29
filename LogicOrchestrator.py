import os
from GUI import GUI
import PySimpleGUI as sg
import BuildDataCollector as Bd
import ExecutedCommandsKeeper as EC
from Executer import Executer as Exec
import RegistriesEditor as RE
from utils import Constants as C
import pyperclip as pc

class Orchestrator:
    def __init__(self):
        self.BuildDataCollector = Bd.BuildDataCollector()
        self.ExecutedCommandsKeeper = EC.ExecutedCommandsKeeper()
        self.RegEditor = RE.RegistriesEditor()
        self.GUI = GUI()
        self.Executer: Exec = Exec(self.ExecutedCommandsKeeper)
      

    def gatherInput(self):
        while True:
            event, values = self.GUI.mainwindow.read(timeout=self.GUI.timeout)
            if event == sg.TIMEOUT_EVENT:
                self.PrintOutput()
                if  self.Executer.isCLIThreadRunning is False:
                    self.GUI.enableExecutionControllers()
                    self.GUI.controllersShown = True
                    self.GUI.timeout = None
                    return None
                    

            elif event == sg.WIN_CLOSED:
                return C.QUIT

            elif '-EXEC-' in event:
                # orchestrator level exeuuter handler
                return self.ExecuterEventHandler(event, values)
            elif '-REG-' in event:
                return self.RegistriesEventHandler(event, values)

# execution related functions:
#------------------------------------------------------
    def ExecuterEventHandler(self, event, values):
        if event == C.EX_CANCEL_KEY:
            return self.Cancel()
        
        if event == C.EX_TOGGLE_OUTPUT_KEY:
            return self.GUI.toggleOutput()

        return self.collectInput_UpdateGUI(event, values)
        

    def collectInput_UpdateGUI(self, event, values):

        if event == C.EX_CLEAR_KEY:
            return self.clearCollectedDataAndGUI()

        if event in [C.EX_CLI_INPUT_KEY, C.EX_CLI_ENTER_KEY]:
            return self.ManualCompilationHandler(event, values)

        self.BuildDataCollector.Collect(event, values)
        if self.BuildDataCollector.newdataArrived:
            self.GUI.enableElementsAccordingCollectorData(self.BuildDataCollector)
            self.BuildDataCollector.newdataArrived = False

        if event == C.EX_SHOW_EXECUTED_COMMANDS_KEY:
            return self.OpenExecutedCommandsInterface()
        
        if event == C.EX_CHOOSE_FLAGS_KEY:
           self.handleFlagsSelection()

        if self.GUI.userRequestCompilation(event):
            self.BuildDataCollector.raw_cmd = ''
            return self.InitiateCompilerOperation(event)
            #assign target to BuildDataCollector and execute

    def handleFlagsSelection(self):
            flagmodal =  self.GUI.generateFlagsInterfaceModal(self.BuildDataCollector.compiler)
            GUI.setVisiblityOfDesignatedInterface(self.BuildDataCollector.compiler, flagmodal)
            event , values = flagmodal.read()
            flagmodal.close()
            self.BuildDataCollector.DigestFlags(flagmodal, values)
            del flagmodal



    def clearCollectedDataAndGUI(self):
        self.BuildDataCollector.reset()
        self.GUI.resetExecutionTab()
        return None
   
    def copyCommand(self, event, modal):
        cmd_idx = str(int(event[-2])) + '-'
       
        pc.copy(modal[C.EX_EXECUTED_COMMAND_KEY+cmd_idx].get() +
                 ' ### Time Elapsed: ' + str(modal[C.EX_EXECUTED_DURATION_KEY+cmd_idx].get()))
        sg.popup('Copied to clipboard', icon='./resources/IBicon.ico',
                 no_titlebar=True, auto_close=True,
                 auto_close_duration=3, background_color='grey',
                 text_color='Black', button_color='#02f0b9')
        return None

  
    def HideExecuted(self):
        self.GUI.mainwindow[C.EX_LAST_EXECUTED_COL_KEY].update(visible=False)
        self.GUI.mainwindow[C.EX_SHOW_EXECUTED_COMMANDS_KEY].update(visible=True)
        self.GUI.mainwindow.refresh()

    def ShowExecuted(self):
        self.GUI.mainwindow[C.EX_LAST_EXECUTED_COL_KEY].update(visible=True)
        self.GUI.mainwindow[C.EX_SHOW_EXECUTED_COMMANDS_KEY].update(visible=False)
        self.GUI.mainwindow.refresh()

    def OpenExecutedCommandsInterface(self):
        modal =  self.GUI.generateLastCommandsModal(self.ExecutedCommandsKeeper)
        event, values = modal.read(close = True)
        
        if event is not None and C.EX_COPY_KEY in event:
            self.copyCommand(event, modal)
        del modal
        

    def Execute(self):
        self.Executer.HandleExecution(self.BuildDataCollector)
        self.ExecutedCommandsKeeper.insert(self.BuildDataCollector)
        self.GUI.disableExecutionControllers()
        self.GUI.mainwindow[C.EX_CANCEL_KEY].update(disabled=False)
        self.GUI.timeout = 500
        self.GUI.mainwindow[C.EX_OUTPUT_KEY].update(self.Executer.CLIOutput)
        self.GUI.showOutput()
            
        self.GUI.mainwindow.refresh()
        
        # GUI Show CMD, enable the controllersG

    def PrintOutput(self):
        if self.Executer.gotnewcontent:
            self.GUI.printOutput(self.Executer.CLIOutput)
            self.Executer.CLIOutput = ''
            self.Executer.gotnewcontent = False
        if not self.Executer.isCLIThreadRunning:
            self.GUI.timeout = None

    def InitiateCompilerOperation(self,event):
        self.BuildDataCollector.setRawCmd(event)
        self.GUI.disableExecutionControllers()
        self.GUI.controllersShown = False
        self.GUI.timeout = 100
        return C.EXECUTE

    def Cancel(self):
        self.Executer.TerminateExecution()
        self.GUI.timeout = None
        self.GUI.hideOutput()
        self.GUI.mainwindow[C.EX_CANCEL_KEY].update(disabled=True)
        # mainwindow shrink
        self.GUI.enableExecutionControllers()
        # GUI Hide CMD, greyout the controllers

    def ManualCompilationHandler(self, event,values):
        if event == C.EX_CLI_ENTER_KEY:
            self.clearCollectedDataAndGUI()
            self.BuildDataCollector <= values[C.EX_CLI_INPUT_KEY]
            self.ExecutedCommandsKeeper.insert(self.BuildDataCollector)
            self.GUI.mainwindow[C.EX_CLI_INPUT_KEY].update('')
            self.GUI.disableElements(event)
            return self.InitiateCompilerOperation(event)

        elif event == C.EX_CLI_INPUT_KEY:
            self.GUI.enableElements(C.EX_CLI_ENTER_KEY)
            return None
#------------------------------------------------------------------------------

#dev reg
#------------------------------------------------------------------------------

    def RegistriesEventHandler(self, event, values):
        try:
            match event:
                case C.REG_DEV_KEY:
                    self.RegEditor.setDevRegToVal(values[C.REG_DEV_SPIN_KEY])

                case C.REG_UAT_KEY:
                    self.RegEditor.setUATEKS(values[C.REG_UAT_INPUT_KEY])
                    if values[C.REG_UAT_RESTART_KEY]:
                        RE.RegistriesEditor.restartService('CoordService.exe')
                    a = input()
                case C.REG_CLANG_PATH_CONVERT_KEY:
                    self.RegEditor.setClangPathConvertToVal(values[C.REG_CLANG_PATH_CONVERT_SPIN_KEY])
                    # sg.popup('successfully set \'ClangPathConvert\' registry to \'' + values[C.REG_DEV_SPIN_KEY] + '\'', icon='./resources/IBicon.ico')

    
        except Exception as E:
            sg.popup_error(str(E))                # if event == C.REG_DEV_KEY:
        #     # get value in spin, update regitrt accordingly
        #     # pop up message 
        #     pass
        # elif event == C.REG_UAT_KEY:
        #     # get value in input, check if REG_UAT_RESTART_KEY  and update regitrt accordingly
        #     # pop up message
        #     pass


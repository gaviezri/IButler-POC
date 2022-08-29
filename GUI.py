
import PySimpleGUI as sg
from layouts.GUILayout import LayoutManager as LM 
from utils import Constants as C
import BuildDataCollector as BD
import ExecutedCommandsKeeper as EC
from utils import SlnHandlers as SH
sg.theme('Dark')

class GUI():
    def __init__(self):
        self.LM: LM = LM()
        self.controllersShown = False
        self.mainwindow = sg.Window("IButler", layout=[self.LM.Mainlayout],
                                finalize=True,icon=C.ICON,
                                element_justification='center',
                                auto_size_buttons=True, auto_size_text=True)
        self.outputShown = False
        self.timeout = None

    def clearelementsvalue(self, *args):
        for elem in args:
            self.mainwindow[elem].update('')

    def clearinputfromGUI(self):
        self.clearelementsvalue(C.EX_SLN_DROP_KEY,
                                C.EX_COMP_KEY,
                                C.EX_BUILD_TYPE_KEY,
                                C.EX_BUILD_TYPE_KEY)
        # selfCLERAFLAGS!
        # clearOutput

    def enableElements(self, *args):
        for elem in args:
            self.mainwindow[elem].update(disabled=False)
        self.mainwindow.refresh()

    def disableElements(self, *args):
        for elem in args:

            self.mainwindow[elem].update(disabled=True)
        self.mainwindow.refresh()

    def hideElements(self, *args):
        for elem in args:
            self.mainwindow[elem].update(visible=False)
        self.mainwindow.refresh()

    def showElements(self, *args):
        for elem in args:
            self.mainwindow[elem].update(visible=True)
        self.mainwindow.refresh()

    def enableExecutionControllers(self) -> None:
        self.enableElements(C.EX_BUILD_KEY, C.EX_REBUILD_KEY, C.EX_CLEAN_KEY)

    def disableExecutionControllers(self) -> None:
        self.disableElements(C.EX_BUILD_KEY, C.EX_REBUILD_KEY, C.EX_CLEAN_KEY)

    def resetExecutionTab(self):
        self.disableExecutionControllers()
        self.ClearExecutionElements()
        self.disableElements(C.EX_BUILD_TYPE_KEY, C.EX_CHOOSE_FLAGS_KEY,
                             C.EX_CLEAR_KEY, C.EX_CANCEL_KEY)

    def ClearExecutionElements(self):
        self.clearinputfromGUI()
        self.controllersShown = False

    def allowuserToInitiateCompilation(self):
        self.enableExecutionControllers()
        self.controllersShown = True

    def userRequestCompilation(self, event):
        return event in [C.EX_BUILD_KEY, C.EX_REBUILD_KEY, C.EX_CLEAN_KEY]

    def enableElementsAccordingCollectorData(self, builddatacollector: BD):

        if not builddatacollector.any():
            if self.controllersShown:
                self.controllersShown = False
                self.resetExecutionTab()

          
        else:
            self.mainwindow[C.EX_CLEAR_KEY].update(disabled=False)

            if builddatacollector.sln != '':
                self.slnChosenHandler(builddatacollector)

            else:# if sln is not chosen
                self.disableElements(C.EX_BUILD_TYPE_KEY)
                self.mainwindow[C.EX_BUILD_TYPE_KEY].update('')

            if builddatacollector.compiler != '':
                self.enableElements(C.EX_CLEAR_KEY, C.EX_CHOOSE_FLAGS_KEY)

            else:
                self.disableElements(C.EX_CHOOSE_FLAGS_KEY)

            if builddatacollector.buildtype != '':
                self.mainwindow[C.EX_BUILD_TYPE_KEY].update(
                            builddatacollector.buildtype)
        
        if  builddatacollector.all():
            self.enableExecutionControllers()
            self.controllersShown = True

    def slnChosenHandler(self, bdc):
        buildtypes = SH.SlnBuildTypeExtractor(
                     bdc.sln).BuildTypes
        if  self.mainwindow[C.EX_BUILD_TYPE_KEY].Values != buildtypes:
            self.mainwindow[C.EX_BUILD_TYPE_KEY].update(values=buildtypes)
            self.clearelementsvalue(C.EX_BUILD_TYPE_KEY)
            bdc.buildtype = ''
        self.enableElements(C.EX_CLEAR_KEY, C.EX_BUILD_TYPE_KEY)

    def showOutput(self):
        self.showElements(C.EX_OUTPUT_KEY)
        self.outputShown = True

    def hideOutput(self):
        self.hideElements(C.EX_OUTPUT_KEY)
        self.outputShown = False

    def toggleOutput(self):
        if self.outputShown:
            self.hideOutput()
        else:
            self.showOutput()
           

    def printOutput(self, output):
        self.mainwindow[C.EX_OUTPUT_KEY].print(output)

    def generateLastCommandsModal(self,ECK: EC.ExecutedCommandsKeeper):
        return sg.Window('Executed Commands', [self.LM.generateLastExecutedCommandsLayout(ECK)],
                                icon=C.ICON,
                                button_color='Black', finalize=True,
                                element_justification='center',
                                auto_size_buttons=True, auto_size_text=True,
                                modal=True, resizable=True)
    
    def generateFlagsInterfaceModal(self,compiler):
        return sg.Window('Choose Flags', [self.LM.generateFlagsInterfaceLayout(compiler)],
                                icon=C.ICON,
                                button_color=('#02f0b9','Black'), finalize=True,
                                element_justification='left',
                                auto_size_buttons=True, auto_size_text=True,
                                modal=True)
    
    def setVisiblityOfDesignatedInterface(comp,modal):
        if comp == 'BuildConsole':
            modal[C.EX_IBFLAGS_KEY].update(visible=True)
            modal[C.EX_MSBUILDFLAGS_KEY].update(visible=False)
        elif comp == 'MSBuild':
            modal[C.EX_IBFLAGS_KEY].update(visible=False)
            modal[C.EX_MSBUILDFLAGS_KEY].update(visible=True)

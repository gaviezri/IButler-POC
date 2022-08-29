
from utils import Constants as C
import subprocess
import os
import PySimpleGUI as sg


class SlnFinder:
    def __init__(self):
        self.Sln_Dict = {}

        def Extract_All_Sln(self):

            try:
                pathToES = "\"" + os.getcwd() + C.EVERYTHING_API_PATH  # noqa: E501 
                raw_sln_paths = subprocess.check_output(pathToES + "\" *.sln\"").decode('utf-8').split('\r\n')
                for sln_path in raw_sln_paths:
                    sln_nickname = sln_path[sln_path.rfind("\\") + 1:-4]
                    if sln_nickname == '':
                        continue
                    self.Sln_Dict[sln_nickname] = sln_path
            except:  # noqa: E722
                sg.popup(C.EVERYTHINGERR, title="Error", background_color='black',text_color='#02f0b9',icon="./IBicon.ico",button_color='red',button_type=sg.POPUP_BUTTONS_OK)
                return False

        Extract_All_Sln(self)
    def Get_Sln_Dict(self):
        return self.Sln_Dict


class SlnBuildTypeExtractor:
    def __init__(self,pathToSln):
        self.BuildTypes = []
        self.ExtractBuildTypes(pathToSln)

    def reset(self):
        self.BuildTypes = []


    def ExtractBuildTypes(self,sln_path):
        slnfile = open(sln_path,'r')
        foundconfigsSectionStart = False
        foundconfigsSectionEnd = False

        while not foundconfigsSectionStart:
            line = slnfile.readline()
            if 'GlobalSection(SolutionConfigurationPlatforms)' in line:
                foundconfigsSectionStart = True

        while not foundconfigsSectionEnd:
            line = slnfile.readline()
            if 'EndGlobalSection' in line:
                foundconfigsSectionEnd = True
                continue
            self.extractBuildVal(line)
            
    def extractBuildVal(self,line:str):
        buildVal = line[line.find('=')+2:line.rfind('\n')]
        buildVal.replace('|','\x7C')
        self.BuildTypes.append(buildVal)



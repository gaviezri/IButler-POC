import win32serviceutil as W32SU 
from utils import Constants as C
import os

class RegistriesEditor():
    def __init__(self) -> None:
        pass
    
    def applyRegistry(self,regname:str) -> None:
        os.system(f'{os.getcwd()}\\resources\\registries\\{regname}')

    def ClangPathConv_suffix(selection:int) -> str:
        return C.REG_CLANG_PATH_CONVERT_PREFIX_NAME + str(selection) + '.reg'
        
    def setDevRegToVal(self, selection:int) -> None:
        match(selection):
            case 1:
                self.applyRegistry(C.REG_ADD_DEV_TO_REG_NAME)
            case 0:
                self.applyRegistry(C.REG_REM_DEV_FROM_REG_NAME)



    def setClangPathConvertToVal(self, selection:int) -> None:
        self.applyRegistry(RegistriesEditor.ClangPathConv_suffix(selection))

    def setUATEKS(self, coordID_input:str) -> None:
        self.modifyCoordIDLineInRegFile(coordID_input)
        self.applyRegistry(C.REG_UAT_EKS_NAME)

        
    def modifyCoordIDLineInRegFile(self,coordID_input:str) -> None:
        
        filepath = f'{os.getcwd()}\\resources\\registries\\{C.REG_UAT_EKS_NAME}'
        UAT_reg_file = open(filepath,'r')
        fileTolines = UAT_reg_file.readlines()
        UAT_reg_file.close()
        CoordIDPrefix = fileTolines[-1][:fileTolines[-1].find('=')+1]
        CoordIDLine = CoordIDPrefix +  f'\"{coordID_input}\"'
        fileTolines[len(fileTolines)-1] = CoordIDLine
        UAT_reg_file = open(filepath,'w')
        UAT_reg_file.writelines(fileTolines)
        UAT_reg_file.close()


    def restartService(servicename):
        try:
            W32SU.RestartService(servicename)
        except Exception as E:
            raise E
        
from utils import Constants as C
from utils import SlnHandlers as SF


class BuildDataCollector():    
    def __init__(self, clicmd: str | None = None):
        self.sln = ''
        self.compiler = ''
        self.buildtype = ''
        self.flags = []
        self.exec_method = None
        self.raw_cmd = clicmd
        self.newdataArrived = False
        self.startTime = 0
        self.endTime = 0
    
    def generateConfigByCompiler(self):
        # notice that |x64 is failing for MSBuild
        # since default Platform is chosen pre flags are added
        # remember to change
        config = self.buildtype
        match(self.compiler):
            case 'BuildConsole':
                return '\"/cfg='+config + '\" '
            case 'MSBuild':
                return '/p:Configuration='+config[:-4] + ' ' # remove '|x64' because if platform not specified, 
                                                             # '|x64' will be automatically added to the config                                          

    def setRawCmd(self,strategy) -> None:
            if self.raw_cmd is not '':
                return
            self.raw_cmd = self.compiler +\
                ' ' + self.generateConfigByCompiler() +\
                ' '.join([flg+' ' for flg in self.flags]) +\
                ' ' + self. generateStrategyByCompiler(strategy) +\
                '\"' + self.sln + '\"' 
    
    def generateStrategyByCompiler(self, strategy) -> str:
        match(strategy):
            case C.EX_BUILD_KEY:
                return '/t:build ' if self.compiler == 'MSBuild' \
                                  else '/build '
                    
            case C.EX_REBUILD_KEY:
                return '/t:rebuild ' if self.compiler == 'MSBuild' \
                                    else '/rebuild '

            case C.EX_CLEAN_KEY:
                return '/t:clean ' if self.compiler == 'MSBuild' \
                                  else '/clean ' 

    def argsToList(self):
        return [self.compiler, self.generateConfigByCompiler()] + self.flags +\
             ['\"' + self.sln + '\"']

    def __str__(self):
        return self.raw_cmd 

    def MethodStated(self) -> bool:
        return self.exec_method is not None

    def __le__(self, cmdline: str):
        self.reset()
        self.raw_cmd = cmdline

    def reset(self) -> None:
        self.sln = ''
        self.compiler = ''
        self.buildtype = ''
        self.flags.clear()
        self.exec_method = None
        self.raw_cmd = None

    def any(self) -> bool:
        return self.sln != '' or self.compiler != '' or \
            self.buildtype != '' or len(self.flags) != 0

    def all(self) -> bool:
        return self.sln != '' and self.compiler != '' and\
             self.buildtype != '' # and len(self.flags) != 0

    def isValid(self) -> bool:
        # Assuming compilers implemented default flags
        return self.sln != '' and self.compiler != ''\
                    and self.buildtype != ''

    def __repr__(self):
        return '[sln: ' + self.sln + ' | ' + 'compiler: ' + self.compiler +\
             ' | ' + 'buildtype: ' + self.buildtype + ']'

    def Collect(self, event, values):
        if event in [C.EX_SLN_DROP_KEY, C.EX_COMP_KEY,
                     C.EX_BUILD_TYPE_KEY, C.EX_SUBMIT_KEY]:

            self.newdataArrived = True
        match (event):
            case C.EX_SLN_DROP_KEY:
                self.assignSln(values)

            case C.EX_COMP_KEY:
                self.compiler = values[C.EX_COMP_KEY]

            case C.EX_BUILD_TYPE_KEY:
                self.buildtype = values[C.EX_BUILD_TYPE_KEY]
            case C.EX_SUBMIT_KEY:
                # assignFlags
                pass

    def assignSln(self, values):
        self.sln = SF.SlnFinder().Get_Sln_Dict()[values[C.EX_SLN_DROP_KEY]] \
            if values[C.EX_SLN_BROWSE_KEY] == '' else values[C.EX_SLN_BROWSE_KEY]

    def DigestFlags(self,modal,values):
        self.flags = self.FlagsDigestor(self.compiler).digest(modal,values)

    # end of buildcollector class
    # start of flagsdigestor class (nested)
    class FlagsDigestor():
        def __init__(self,comp):
            self.comp = comp

        def digest(self,modal,values) -> list[str]:
        
            if self.comp == 'MSBuild':
                return self.MSBuildFlagsDigestor.digest(modal,values)
            elif self.comp == 'BuildConsole':
                return self.BuildConsoleFlagsDigestor.digest(modal,values)


    # end of flagsdigestor class
    # start of MSBuildFlagsDigestor class (nested^2)
        class MSBuildFlagsDigestor():
            def __init__(self):
                pass
            def digest(modal,values) -> list[str]:
                
                if values is None:
                    return []

                digestedflags = []


              
    # end of MSBuildFlagsDigestor class
    # start of BuildConsoleFlagsDigestor class (nested^2)
        class BuildConsoleFlagsDigestor():
            def __init__(self):
                pass
            def digest(modal,values) -> list[str]:
                # This framework doesnt support any other way for this 
                # to be done other than hardcoding it
                
                if values is None:
                    return []
                
                digestedflags = []
                
                if values[C.IB_IMPORTEDSCRIPTINPUT_KEY] != '':
                    digestedflags.append(f'@\"{values[C.IB_IMPORTEDSCRIPTINPUT_KEY]}\"')

                # if values[C.IB_ATTACH_KEY]:
                #     digestedflags.append('/Attach')

                if values[C.IB_AVOIDLOCAL_ON_KEY]:
                    digestedflags.append('/AvoidLocal=On')
                
                if values[C.IB_AVOIDLOCAL_OFF_KEY]:
                    digestedflags.append('/AvoidLocal=Off')
                
                # if values[C.IB_BEEP_KEY]:
                #     digestedflags.append('/Beep')

                if values[C.IB_DISABLE_KEY]:
                    digestedflags.append('/Disable')

                if values[C.IB_ENABLE_KEY]:
                    digestedflags.append('/Enable')
                
                if values[C.IB_HELP_KEY]:
                    digestedflags.append('-help')
                
                if values[C.IB_LOGFILEINPUT_KEY] != '':
                    digestedflags.append(f'/Log={values[C.IB_LOGFILEINPUT_KEY]}')

                if values[C.IB_LOGLEVEL_BASIC_KEY]:
                    digestedflags.append('/LogLevel=Basic')
                    
                elif values[C.IB_LOGLEVEL_MINIMAL_KEY]:
                    digestedflags.append('/LogLevel=Minimal')
                
                elif values[C.IB_LOGLEVEL_INTERMEDIATE_KEY]:
                    digestedflags.append('/LogLevel=Intermediate')

                elif values[C.IB_LOGLEVEL_DETAILED_KEY]:
                    digestedflags.append('/LogLevel=Detailed')

                elif values[C.IB_LOGLEVEL_EXTENDED_KEY]:
                    digestedflags.append('/LogLevel=Extended')
                
                if values[C.IB_MAXCPUS_KEY] > 0:
                    digestedflags.append(f'/MaxCPUS={values[C.IB_MAXCPUS_KEY]}')

                if values[C.IB_MAXWINVER_KEY] != '':
                    digestedflags.append(f'/MaxWinVer={values[C.IB_MAXWINVER_KEY]}')

                if values[C.IB_MINWINVER_KEY] != '':
                    digestedflags.append(f'/MinWinVer={values[C.IB_MINWINVER_KEY]}')

                if values[C.IB_MON_KEY] != '':
                    digestedflags.append(f'/Mon={values[C.IB_MON_KEY]}')

                if values[C.IB_DONOTVIRT_KEY]:
                    digestedflags.append('/NO_DOTNET_VIRT')
                
                if values[C.IB_NOLOGO_KEY]:
                    digestedflags.append('/NoLogo')

                if values[C.IB_NOWAIT_KEY]:
                    digestedflags.append('/NoWait')
                
                if values[C.IB_OPENMONITOR_KEY]:
                    digestedflags.append('/OpenMonitor')
                    
                if values[C.IB_OUT_KEY]:
                    digestedflags.append(f'/out={values[C.IB_OUTINPUT_KEY]}')
                
                if values[C.IB_QUERYPACKAGE_KEY]:
                    digestedflags.append(f'/QueryPackage={values[C.IB_QUERYPACKAGEINPUT_KEY]}')

                if values[C.IB_QUERYLICENSE_KEY]:
                    digestedflags.append('/QueryLicense')

                if values[C.IB_RESET_KEY]:
                    digestedflags.append('/Reset')

                if values[C.IB_SETENV_KEY]:
                    digestedflags.append(f'/SetEnv=\"{values[C.IB_SETENVINPUT_KEY]}\"=\"{values[C.IB_SETENVINPUT2_KEY]}\"')    

                if values[C.IB_SHOWAGENT_KEY]:
                    digestedflags.append('/ShowAgent')
                
                if values[C.IB_SHOWTIME_KEY]:
                    digestedflags.append('/ShowTime')

                if values[C.IB_SILENT_KEY]:
                    digestedflags.append('/Silent')

                if values[C.IB_STOPINPUT_KEY] is not '':
                    digestedflags.append(f'/Stop={values[C.IB_STOPINPUT_KEY]}')
                
                if values[C.IB_STOPONERROR_KEY]:
                    digestedflags.append('/StopOnError')

                if values[C.IB_STOPALL_KEY]:
                    digestedflags.append('/StopAll')

                if values[C.IB_TITLE_KEY]:
                    digestedflags.append(f'/Title={values[C.IB_TITLEINPUT_KEY]}')

                if values[C.IB_USEIDEMON_KEY]:
                    digestedflags.append('/UseIDEmonitor')

                if values[C.IB_WAIT_KEY]:
                    digestedflags.append('/Wait')


                return digestedflags
                
                
        

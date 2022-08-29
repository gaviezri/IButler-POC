from utils import Constants as C, FlagsLayout as FL1

FL = FL1.FlagsLayout

class IBFlagsLayout():
    def __init__(self):
        pass
    
    def getLayout(self):
        return  [
            FL.generateTextInputBrowse('@',
                                          'Specifies a response file containing\nan IBConsole command line.',
                                          C.IB_IMPORTEDSCRIPTINPUT_KEY),
            FL.generateRadioGroup('AvoidLocal',
                                    'Overrides the Avoid task execution on local machine when\npossible option in the Agent Settings dialog box.',
                                    C.IB_AVOIDLOCAL_KEY,('On',C.IB_AVOIDLOCAL_ON_KEY),('Off',C.IB_AVOIDLOCAL_OFF_KEY)),
            FL.generateCheckBox('Enable','Enables Incredibuild Agent to participate as a Helper.',C.IB_ENABLE_KEY),
            
            FL.generateCheckBox('Disable','Disables Incredibuild Agent to participate as a Helper.',C.IB_DISABLE_KEY),
            
            FL.generateCheckBox('Help','Shows usage help and version information.',C.IB_HELP_KEY),
            
            FL.generateTextInputBrowse('Log','Writes process output to a file.',C.IB_LOGFILEINPUT_KEY),
            
            FL.generateRadioGroup('Log Level', 'Overrides the logging level for this build.',C.IB_LOGLEVEL_KEY,
                            ('Minimal',C.IB_LOGLEVEL_MINIMAL_KEY), ('Basic',C.IB_LOGLEVEL_BASIC_KEY), ('Intermediate',C.IB_LOGLEVEL_INTERMEDIATE_KEY),
                            ('Extended',C.IB_LOGLEVEL_EXTENDED_KEY), ('Detailed',C.IB_LOGLEVEL_DETAILED_KEY)),
            FL.generateTextSpin('MaxCPUs','Overrides the global maximum CPUs/Cores in the build setting.',C.IB_MAXCPUS_KEY,[i for i in range(0,0xFFFF)]),
            
            FL.generateTextInput('MaxWinVer','Specifies the maximal operating system required by remote\nAgents assigned to this build.',
                                C.IB_MAXWINVER_KEY),
            FL.generateTextInput('MinWinVer','Specifies the minimal required operating system required by\nremote Agents assigned to this build.',
                                C.IB_MINWINVER_KEY),
            FL.generateTextInputBrowse('Mon','Writes a copy of the build progress (.ib_mon) file to the specified\nlocation.',
                                          C.IB_MON_KEY),
            FL.generateCheckBox('No .NET Virtualization','Disables the Virtualization of .NET environment\non Helper machines.',
                                   C.IB_DONOTVIRT_KEY),
            FL.generateCheckBox('NoLogo','Suppresses the "Incredibuild" header in the build output.',C.IB_NOLOGO_KEY),
            
            FL.generateCheckBox('NoWait','When specified, if another process initiated by this Agent is already\nrunning, IBConsole exits with an "Another build already running" message.',
                                   C.IB_NOWAIT_KEY),
            FL.generateCheckBox('OpenMonitor','Opens the Build Monitor window that shows the execution progress.',
                                    C.IB_OPENMONITOR_KEY),
            FL.generateCheckBoxInputBrowse('out=filename','Writes the build output to the specified file.\nCheckbox must be checked.',
                                           C.IB_OUT_KEY,('',C.IB_OUTINPUT_KEY)),
            FL.generateCheckBox('QueryLicense','Displays information regarding the active license, allocated packages,\nand maintenance expiration date.',
                                   C.IB_QUERYLICENSE_KEY),
            FL.generateCheckBoxInput('QueryPackage','Checks whether a specific Incredibuild extension package is allocated\nto the Agent, and sets the exit code to 0 (allocated) or 1 (not allocated).',
                                   C.IB_QUERYPACKAGE_KEY,('',C.IB_QUERYPACKAGEINPUT_KEY)),
            FL.generateCheckBox('Reset','Clears the Agent\'s file cache content.',C.IB_RESET_KEY),
            
            FL.generateCheckBoxInput('SetEnv','Sets or overrides an environment variable for the context of the command execution.',
                                     C.IB_SETENV_KEY,('Name',C.IB_SETENVINPUT_KEY),('Value',C.IB_SETENVINPUT2_KEY)),
            FL.generateCheckBox('ShowAgent','Shows the Agent used for each task execution.',C.IB_SHOWAGENT_KEY),
            
            FL.generateCheckBox('ShowTime','Shows the Start and Finish time for each task.',C.IB_SHOWTIME_KEY),
            
            FL.generateCheckBox('Silent','Does not write anything to the standard output.',C.IB_SILENT_KEY),
            
            FL.generateTextInput('Stop','Specifies the task to execute.',C.IB_STOPINPUT_KEY),
            
            FL.generateCheckBox('StopOnError','When specified, the execution will stop as soon as an error is encountered.',C.IB_STOPONERROR_KEY),
            
            FL.generateCheckBox('StopAll','Stops all currently running builds',C.IB_STOPALL_KEY),

            FL.generateCheckBoxInput('Title','Specifies a custom header line which will be displayed in the beginning of the Execution output text. This title will also be used for the Execution History and Execution Monitor displays.',
                                    C.IB_TITLE_KEY,('',C.IB_TITLEINPUT_KEY)),
                                
            FL.generateCheckBox('UseIDEmonitor','When IBConsole is run from the Visual Studio IDE with this option, the integrated IDE Execution Monitor displays the execution progress.',
                                C.IB_USEIDEMON_KEY),
            FL.generateCheckBox('Wait','If another process initiated by this Agent is currently running,\nwaits until that process is finished and then starts the new process.\nThis is also the default behavior.',
                                C.IB_WAIT_KEY)
        ]































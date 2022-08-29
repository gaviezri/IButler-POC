from time import time
from datetime import datetime as dt
from BuildDataCollector import BuildDataCollector as bdc
from ExecutedCommandsKeeper import ExecutedCommandsKeeper as eck
from copy import deepcopy
import subprocess, threading, sys, os

class Executer():
    def __init__(self,eck_):
        self.myBuildDataCollector: bdc = None
        self.commandsQueue: list[bdc] = None
        self.executedcommandskeeper: eck = eck_
        self.processedBuildData = ''
        self.CLIThread = None
        self.CLIprocess = None
        self.isCLIThreadRunning = False
        self.CLIOutput = ''
        self.Terminate = False
        self.gotnewcontent = False

    def adjustCommandToPopenAPI(self):
        return self.myBuildDataCollector.argsToList()

    def HandleExecution(self, globalBuildDataCollector: bdc) -> None:
        globalBuildDataCollector.startTime = time()
        self.myBuildDataCollector = deepcopy(globalBuildDataCollector)
        self.runCommand()

    def runCommandInThread(self):
        # get arguments as list of args
        args = self.myBuildDataCollector.raw_cmd \
            if self.myBuildDataCollector.raw_cmd is not None \
            else self.adjustCommandToPopenAPI()
        running = True
        initiated = False

        while running:
            if not initiated:
                try:
                    if not (args.startswith('BuildConsole') or args.startswith('MSBuild')):
                        #TODO: insert to beggining an invoke to cmd w/ args as parameters.
                        args = 'cmd ' + args + '\n'
                # initiate the process
                    self.CLIprocess = subprocess.Popen(args,shell=True,
                                                      stdout=subprocess.PIPE,
                                                      stderr=subprocess.STDOUT)
                    
                    initiated = True
                # if the process has finished, then break
                except Exception as e:  
                    self.gotnewcontent = True             
                    self.CLIOutput = dt.now().strftime("%H:%M:%S") + ' ERR :' + e.strerror+'\n'
                    running = False
                    break
            if self.CLIprocess.poll() is not None:
                running = False
                self.CLIprocess.kill()
                self.isCLIThreadRunning = False
            
            for line in self.CLIprocess.stdout:
                line = line.decode(errors='replace'
                                   if (sys.version_info) < (3, 5)
                                   else 'backslashreplace').rstrip()
                self.CLIOutput += line.split('\r\n') \
                    if type(line) == list()\
                    else line
                self.CLIOutput += '\n' 
                self.gotnewcontent = True
                if  self.Terminate:
                    running = False
                    self.CLIprocess.kill()
                    self.isCLIThreadRunning = False
                    self.Terminate =  False
                    break
        self.executedcommandskeeper.summarizeRunTime()
        self.CLIThread = None
        
    def runCommand(self):
        self.Terminate = False
        if self.CLIThread is not None:
            self.TerminateExecution()
        self.CLIThread = threading.Thread(target=self.runCommandInThread)
        self.CLIThread.start()
        self.isCLIThreadRunning = True
        
    def TerminateExecution(self):
        self.TerminateCommand()
        self.CLIOutput = ''
        self.processedBuildData = ''

    def TerminateCommand(self) -> None:
        self.Terminate = True
        if self.isCLIThreadRunning:
            self.isCLIThreadRunning = False
            self.CLIThread = None

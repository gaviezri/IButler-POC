# keep last track of last commands that were executed.
# most recent command is at the end of the list.
from BuildDataCollector import BuildDataCollector as BDC
from time import time
from copy import deepcopy

class ExecutedCommandsKeeper():
    class EC_InANutShell():
        def __init__(self,bdc: BDC):
        
            self.raw_cmd = deepcopy(bdc.raw_cmd)
            self.startTime = bdc.startTime
            self.endTime = bdc.endTime
            self.duration = self.endTime - self.startTime

    def __init__(self):
        self.Commands = []

    def insert(self, bdc: BDC) -> None:
        self.Commands.append(self.EC_InANutShell(bdc)) 

    def getCommand(self, idx):
        return self.Commands[idx]
    
    def getNumberOfCommands(self) -> int:
        return len(self.Commands)

    def summarizeRunTime(self) :
        self.Commands[-1].endTime = time()
        self.Commands[-1].duration = \
            float('%.3f' % 
                (self.Commands[-1].endTime - \
                self.Commands[-1].startTime)
                )

        
    # return the upcoming command to execute
    def getUpcomingExecute(self) -> EC_InANutShell:
        return self.Commands[-1]

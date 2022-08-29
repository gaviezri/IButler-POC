from utils import Constants as C
from LogicOrchestrator import Orchestrator

        

# main DS that contains attribute of DS of each
orchestrator:Orchestrator = Orchestrator()

def main():
    butlerIsNeeded = True
    while butlerIsNeeded:
        # try:
        task = orchestrator.gatherInput()
        match task:
            case C.EXECUTE:
                orchestrator.Execute()

            case C.REGISTRIES:
                #notify user that registries are being edited
                pass
            case C.ABOUT:
                pass

            case C.QUIT:
                butlerIsNeeded = False

        # except exceptions.err as err:
        # return err.notify()

    return 0


if __name__ == "__main__":
    main()

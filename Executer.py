from matplotlib.pyplot import autoscale
import CONSTANTS
import PySimpleGUI as sg



#flags for IB console
IB_flags_layout = [sg.Column([
        [sg.Checkbox("@", key="@")],
        [sg.Checkbox("All", key="All")],
        [sg.Checkbox("Attach", key="Attach")],
        [sg.Checkbox("AvoidLocal", key="AvoidLocal"),sg.Radio("On", key="AvoidLocalOn",group_id="Avdlcl"),sg.Radio("Off", key="AvoidLocalOff",group_id="Avdlcl")],
        [sg.Checkbox("All", key="All")],
        [sg.Checkbox("Attach", key="Attach")],
        [sg.Checkbox("Beep", key="Beep")],
        [sg.Checkbox("BrowseInfo", key="BrowseInfo"),sg.Radio("On",key="BrowseInfoOn",group_id="brsinfo"),sg.Radio("Off",key="BrowseInfoOff",group_id="brsinfo")],
        [sg.Checkbox("CEconfig=", key="CEconfig="), sg.InputText("", size=(15,1), key="CEconfigInput")],
        [sg.Checkbox("Cfg", key="Cfg"), sg.InputText("", size=(15,1), key="CfgInput")],
        [sg.Checkbox("cl_add",key="cl_add"), sg.InputText("", size=(15,1), key="cl_addInput")],
        [sg.Checkbox("cl_rem",key="cl_rem"), sg.InputText("", size=(15,1), key="cl_remInput")],
        [sg.Checkbox("Clean", key="Clean")],
        [sg.Checkbox("compile", key="compile"), sg.InputText("", size=(15,1), key="compileInput")],
        [sg.Radio("Disable", key="Disable",group_id="agentmode"),sg.Radio("/Enable", key="Enable",group_id="agentmode")],
        [sg.Checkbox("DisablePdbForwarding", key="DisablePdbForwarding")],
        [sg.Checkbox("DumpSourceFiles", key="DumpSourceFiles"), sg.InputText("", size=(15,1), key="DumpSourceFilesInput")],
        [sg.Checkbox("Help", key="Help")],
        [sg.Checkbox("IncrediLink", key="IncrediLink")],
        [sg.Checkbox("IntelCLVersion",key="IntelCLVersion"),sg.Input("", size=(15,1), key="IntelCLVersionInput")],
        [sg.Checkbox("link_add",key="link_add"), sg.InputText("", size=(15,1), key="link_addInput")],
        [sg.Checkbox("link_rem",key="link_rem"), sg.InputText("", size=(15,1), key="link_remInput")],
        [sg.Checkbox("Log",key="Log"), sg.InputText("", size=(15,1), key="LogInput")],
        [sg.Checkbox("LogLevel",key="LogLevel"), sg.Radio("Minimal",key="LogLevelMinimal",group_id="loglvl"),sg.Radio("Basic",key="LogLevelBasic",group_id="loglvl"),
               sg.Radio("Detailed",key="LogLevelDetailed",group_id="loglvl"), sg.Radio("Intermediate",key="LogLevelIntermediate",group_id="loglvl")
               , sg.Radio("Extended",key="LogLevelExtended",group_id="loglvl")],
        [sg.Checkbox("MaxCPUS",key="MaxCPUS"), sg.InputText("", size=(15,1), key="MaxCPUSInput")],
        [sg.Checkbox("MaxWinVer",key="MaxWinVer"), sg.InputText("", size=(15,1), key="MaxWinVerInput")],
        [sg.Checkbox("MinWinVer",key="MinWinVer"), sg.InputText("", size=(15,1), key="MinWinVerInput")],
        [sg.Checkbox("Mon",key="Mon"), sg.InputText("filename.ib_mon", size=(15,1), key="MonInput")],
        [sg.Checkbox("msbuildargs",key="msbuildargs"), sg.InputText("", size=(15,1), key="msbuildargsInput")],
        [sg.Checkbox("NO_DOTNET_VIRT", key="NO_DOTNET_VIRT")],
        [sg.Checkbox("NoIncrediLink", key="NoIncrediLink")],
        [sg.Checkbox("NoLink", key="NoLink")],
        [sg.Checkbox("NoLogo", key="NoLogo")],
        [sg.Checkbox("NoRecurse", key="NoRecurse")],
        [sg.Checkbox("NoWait", key="NoWait")],
        [sg.Checkbox("OpenMonitor", key="OpenMonitor")],
        [sg.Checkbox("out",key="out"), sg.InputText("", size=(15,1), key="outInput")],
        [sg.Checkbox("Preset",key="Preset"), sg.InputText("", size=(15,1), key="PresetInput")],
        [sg.Checkbox("Prj",key="Prj"), sg.InputText("", size=(15,1), key="PrjInput")],
        [sg.Checkbox("QueryLicense", key="QueryLicense")],
        [sg.Checkbox("QueryPackage", key="QueryPackage"), sg.InputText("", size=(15,1), key="QueryPackageInput")],
        [sg.Checkbox("Rebuild", key="Rebuild")],
        [sg.Checkbox("Reset", key="Reset")],
        [sg.Checkbox("SETENV:", key="SETENV:"), sg.InputText("", size=(15,1), key="SETENV:Input")],
        [sg.Checkbox("ShowAgent", key="ShowAgent")],
        [sg.Checkbox("ShowCmd", key="ShowCmd")],
        [sg.Checkbox("ShowTime", key="ShowTime")],
        [sg.Checkbox("Silent", key="Silent")],
        [sg.Checkbox("Stop", key="Stop"), sg.InputText("", size=(15,1), key="StopInput")],
        [sg.Checkbox("StopOnErrors", key="StopOnErrors")],
        [sg.Checkbox("StopAll", key="StopAll")],
        [sg.Checkbox("Title", key="Title"), sg.InputText("", size=(15,1), key="TitleInput")],
        [sg.Checkbox("UseEnv", key="UseEnv")],
        [sg.Checkbox("UseIDEMonitor", key="UseIDEMonitor")],
        [sg.Checkbox("UseMSBuild", key="UseMSBuild")],
        [sg.Checkbox("VsVersion", key="VsVersion"), sg.InputText("", size=(15,1), key="VsVersionInput")],
        [sg.Checkbox("Wait", key="Wait")]

    ],scrollable=True),
    
    [sg.Button("Submit",key="Submit"), sg.Button("Cancel",key="Cancel")]]


#Popup window for the IB flags multiplexer
def IB_flags():
    window = sg.Window("Choose wisely...", layout=[IB_flags_layout],grab_anywhere=True,element_justification="center",icon='.\\pics_fonts\\IBicon.ico')
    while(True):
        event, values = window.read(timeout=100)


#Popup window for the MSBUILD flags multiplexer
def MSBuild_flags():
    return ""


def choose_flags(compiler):
    if compiler == CONSTANTS.IB:
        return CONSTANTS.IB + IB_flags()
    elif compiler == CONSTANTS.MSBuild:
        return CONSTANTS.MSBuild + MSBuild_flags()
    else:
        sg.popup_error("Unknown compiler")
        raise(Exception("Unknown compiler"))
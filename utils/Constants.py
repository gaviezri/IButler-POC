#GENERAL
EVERYTHINGERR = "Error: One of the following:\
                \r\n1) Cannot find es.exe (./Everything-CLI/) \
                \r\n2) \'Everything\' is not running in the background.\
                \r\nPlease run \'Everything\' and restart the program.\r\n\
                or browse manually for sln files."
QUIT = 0
UNEXPECTED = 1

#ACTIONS
EXECUTE = 3
REGISTRIES = 4
ABOUT = 5

#EXECUTION TASKS
BUILD = 6
REBUILD = 7
CLEAN = 8
CANCEL = 9
PRINTOUTPUT = 10

#EXECUTION DATA STATES
EX_STATE_EMPTY = 11
EX_STATE_GOTSLN = 12
EX_STATE_GOTSLN_AND_BUILDTYPE = 13
EX_STATE_GOTCOMPILER = 14
EX_STATE_GOTCOMPILER_AND_SLN = 15
EX_STATE_FILLED = 16

#EXECUTION HISTORY ENTRIES COPY IDs array

#EXECUTION LAYOUT ELEMENTS IDs
EX_OUTPUT_KEY = '-OUTPUT-'
EX_TOGGLE_OUTPUT_KEY = '-EXEC-TOGGLE-OUTPUT-'
EX_SLN_BROWSE_KEY = '-EXEC-SLN-BROWSE-'
EX_SLN_DROP_KEY = '-EXEC-SLN-DROP-'
EX_COMP_KEY = '-EXEC-COMPILER-CHOICE-'
EX_BUILD_TYPE_KEY = '-EXEC-BUILD-TYPE-'
EX_BUILD_KEY = '-EXEC-BUILD-'
EX_REBUILD_KEY = '-EXEC-REBUILD-'
EX_CLEAN_KEY = '-EXEC-CLEAN-'
EX_CANCEL_KEY = '-EXEC-CANCEL-'
EX_CLEAR_KEY = '-EXEC-CLEAR-'
EX_CLI_INPUT_KEY = '-EXEC-CLI-INPUT-'
EX_CLI_ENTER_KEY = '-EXEC-ENTER-'
EX_SUBMIT_KEY = '-EXEC-SUBMIT-'
EX_IBFLAGS_KEY = '-EXEC-IBFLAGS-'
EX_MSBUILDFLAGS_KEY = '-EXEC-MSBUILDFLAGS-'
EX_FLAGS_INTERFACE_KEY = '-EXEC-FLAGS-INTERFACE-'
EX_BUILD_CONTROLLERS_COL_KEY='-EXEC-BUILD-CONTROLLERS_COL-'
EX_CLEAR_CONTROLLERS_COL_KEY='-EXEC-CLEAR-CONTROLLERS_COL-'

EX_LAST_EXECUTED_COL_KEY = '-EXEC-LAST-EXECUTED-COL-'
EX_SHOW_EXECUTED_COMMANDS_KEY = '-EXEC-SHOW-EXECUTED-COMMANDS-'
EX_CHOOSE_FLAGS_KEY = '-EXEC-CHOOSE-FLAGS-'
#EXECUTION HISTORY ENTRIES IDs
EX_CPY_BTN_COL_KEY = '-COPY-BUTTONS-COL-'
EX_COPY_KEY = "-COPY-"
EX_EXEC_CMD_COL_KEY = '-EXECUTED-COMMANDS-COL-'
EX_EXECUTED_COMMAND_KEY = '-EXECUTED-COMMAND-'
EX_EXEC_DUR_COL_KEY = '-EXECUTED-COMMANDS-DURATIONS-COL-'
EX_EXECUTED_DURATION_KEY = '-EXECUTED-DURATION-'
#REGISTRIES LAYOUT ELEMENTS IDs
REG_DEV_KEY = '-REG-DEV-'
REG_DEV_SPIN_KEY = '-REG-DEV-SPIN-'
REG_UAT_KEY = '-REG-UAT-'
REG_UAT_INPUT_KEY = '-REG-UAT-INPUT-'
REG_UAT_RESTART_KEY = '-REG-UAT-RESTART-'
REG_CLANG_PATH_CONVERT_KEY = '-REG-CLANG-PATH-CONVERT-'
REG_CLANG_PATH_CONVERT_SPIN_KEY = '-REG-CLANG-PATH-CONVERT-SPIN-'
#REGISTRIES KEY PATHS
REG_ADD_DEV_TO_REG_NAME = 'Add_Dev_to_registry.reg'
REG_REM_DEV_FROM_REG_NAME = 'Rem_Dev_from_registry.reg'
REG_CLANG_PATH_CONVERT_PREFIX_NAME = 'ClangPathConvert'
REG_UAT_EKS_NAME = 'UAT_EKS.reg'

#IB FLAGS
IB_IMPORTEDSCRIPTFLAG_KEY = '-IB-IMPORTEDSCRIPTFLAG-',
IB_IMPORTEDSCRIPTINPUT_KEY = '-IB-IMPORTEDSCRIPTINPUT-'
IB_CONFIGINPUT_KEY = '-IB-CONFIGINPUT-'
IB_ATTACH_KEY = '-IB-ATTACH-'
IB_AVOIDLOCAL_KEY = '-IB-AVOIDLOCAL-'
IB_AVOIDLOCAL_ON_KEY = '-IB-AVOIDLOCAL-ON-'
IB_AVOIDLOCAL_OFF_KEY = '-IB-AVOIDLOCAL-OFF-'
IB_BEEP_KEY = '-IB-BEEP-'
IB_ENABLE_KEY = '-IB-ENABLE-'
IB_DISABLE_KEY = '-IB-DISABLE-'
IB_HELP_KEY = '-IB-HELP-'
IB_LOGFILE_KEY = '-IB-LOGFILE-'
IB_LOGFILEINPUT_KEY = '-IB-LOGFILEINPUT-'
IB_LOGLEVEL_KEY = '-IB-LOGLEVEL-'
IB_LOGLEVEL_MINIMAL_KEY = '-IB-LOGLEVEL-MINIMAL-'
IB_LOGLEVEL_BASIC_KEY = '-IB-LOGLEVEL-BASIC-'
IB_LOGLEVEL_DETAILED_KEY = '-IB-LOGLEVEL-DETAILED-'
IB_LOGLEVEL_INTERMEDIATE_KEY = '-IB-LOGLEVEL-INTERMEDIATE-'
IB_LOGLEVEL_EXTENDED_KEY = '-IB-LOGLEVEL-EXTENDED-'
IB_MAXCPUS_KEY = '-IB-MAXCPU-'
IB_MAXWINVER_KEY = '-IB-MAXWINVER-'
IB_MINWINVER_KEY = '-IB-MINWINVER-'
IB_MON_KEY = '-IB-MON-'
IB_MONINPUT_KEY = '-IB-MONINPUT-'
IB_DONOTVIRT_KEY = '-IB-DONOTVIRT-'
IB_NOLOGO_KEY = '-IB-NOLOGO-'
IB_NOWAIT_KEY = '-IB-NOWAIT-'
IB_OPENMONITOR_KEY = '-IB-OPENMONITOR-'
IB_OUT_KEY = '-IB-OUT-'
IB_OUTINPUT_KEY = '-IB-OUTINPUT-'
IB_QUERYLICENSE_KEY = '-IB-QUERYLICENSE-'
IB_QUERYPACKAGE_KEY = '-IB-QUERYPACKAGE-'
IB_QUERYPACKAGEINPUT_KEY = '-IB-QUERYPACKAGEINPUT-'
IB_RESET_KEY = '-IB-RESET-'
IB_SETENV_KEY = '-IB-SETENV-'
IB_SETENVINPUT_KEY = '-IB-SETENVINPUT-'
IB_SETENVINPUT2_KEY = '-IB-SETENVINPUT2-'
IB_SHOWAGENT_KEY = '-IB-SHOWAGENT-'
IB_SHOWTIME_KEY = '-IB-SHOWTIME-'
IB_SILENT_KEY = '-IB-SILENT-'
IB_STOP_KEY = '-IB-STOP-'
IB_STOPINPUT_KEY = '-IB-STOPINPUT-'
IB_STOPONERROR_KEY = '-IB-STOPONERROR-'
IB_STOPALL_KEY = '-IB-STOPALL-'
IB_TITLE_KEY = '-IB-TITLE-'
IB_TITLEINPUT_KEY = '-IB-TITLEINPUT-'
IB_USEIDEMON_KEY = '-IB-USEIDEMON-'
IB_WAIT_KEY = '-IB-WAIT-'

#total:41

# IB_allFlags = [
#                IB_IMPORTEDSCRIPTFLAG_KEY, IB_IMPORTEDSCRIPTINPUT_KEY, IB_CONFIGINPUT_KEY,
#                IB_ATTACH_KEY, IB_AVOIDLOCAL_KEY, IB_BEEP_KEY, IB_ENABLE_KEY, IB_DISABLE_KEY,
#                IB_HELP_KEY, IB_LOGFILE_KEY, IB_LOGFILEINPUT_KEY, IB_LOGLEVEL_KEY, IB_MAXCPUS_KEY,
#                IB_MAXWINVER_KEY, IB_MINWINVER_KEY, IB_MON_KEY, IB_MONINPUT_KEY, IB_DONOTVIRT_KEY,
#                IB_NOLOGO_KEY,IB_NOWAIT_KEY,IB_OPENMONITOR_KEY, IB_OUT_KEY, IB_QUERYLICENSE_KEY,
#                IB_QUERYPACKAGE_KEY, IB_RESET_KEY, IB_SETENV_KEY, IB_SETENVINPUT_KEY, IB_SETENVINPUT2_KEY,
#                IB_SHOWAGENT_KEY, IB_SHOWTIME_KEY, IB_SILENT_KEY, IB_STOP_KEY, IB_STOPINPUT_KEY,
#                IB_STOPONERROR_KEY, IB_STOPALL_KEY, IB_TITLE_KEY, IB_TITLEINPUT_KEY, IB_USEIDEMON_KEY,
#                IB_WAIT_KEY,IB_BUILDCONFIG_KEY
#             ]

ICON = "./resources/IBicon.ico"
EVERYTHING_API_PATH = "\\resources\\Everything-CLI\\es.exe"
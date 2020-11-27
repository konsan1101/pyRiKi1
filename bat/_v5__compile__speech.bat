@ECHO OFF
cd ".."

ECHO;
IF EXIST "build" RD "build" /s /q
IF EXIST "dist"  RD "dist"  /s /q
PAUSE

set pyname=_v5__main_speech
    echo;
    echo %pyname%.py
    pyinstaller %pyname%.py  -F --log-level ERROR  --icon="_icons/speech_start.ico"
IF EXIST "dist\%pyname%.exe"  ECHO "%pyname%.exe"
    copy "dist\%pyname%.exe"       "%pyname%.exe"
    del  "%pyname%.spec"
    copy "%pyname%.exe"        "C:\RiKi_v5_assistant\%pyname%.exe"
    copy "%pyname%.exe"        "C:\RiKi_v5_speech\%pyname%.exe"
    del  "%pyname%.exe"

set pyname=_v5_speech__gijiroku1
    echo;
    echo %pyname%.py
    pyinstaller %pyname%.py  -F --log-level ERROR  --icon="_icons/speech_start.ico"
IF EXIST "dist\%pyname%.exe"  ECHO "%pyname%.exe"
    copy "dist\%pyname%.exe"       "%pyname%.exe"
    del  "%pyname%.spec"
    copy "%pyname%.exe"        "C:\RiKi_v5_speech\%pyname%.exe"
    del  "%pyname%.exe"

set pyname=_v5_speech__gijiroku2
    echo;
    echo %pyname%.py
    pyinstaller %pyname%.py  -F --log-level ERROR  --icon="_icons/speech_start.ico"
IF EXIST "dist\%pyname%.exe"  ECHO "%pyname%.exe"
    copy "dist\%pyname%.exe"       "%pyname%.exe"
    del  "%pyname%.spec"
    copy "%pyname%.exe"        "C:\RiKi_v5_speech\%pyname%.exe"
    del  "%pyname%.exe"

set pyname=_v5_speech__narration1
    echo;
    echo %pyname%.py
    pyinstaller %pyname%.py  -F --log-level ERROR  --icon="_icons/speech_start.ico"
IF EXIST "dist\%pyname%.exe"  ECHO "%pyname%.exe"
    copy "dist\%pyname%.exe"       "%pyname%.exe"
    del  "%pyname%.spec"
    copy "%pyname%.exe"        "C:\RiKi_v5_speech\%pyname%.exe"
    del  "%pyname%.exe"

set pyname=_v5_speech__narration2
    echo;
    echo %pyname%.py
    pyinstaller %pyname%.py  -F --log-level ERROR  --icon="_icons/speech_start.ico"
IF EXIST "dist\%pyname%.exe"  ECHO "%pyname%.exe"
    copy "dist\%pyname%.exe"       "%pyname%.exe"
    del  "%pyname%.spec"
    copy "%pyname%.exe"        "C:\RiKi_v5_speech\%pyname%.exe"
    del  "%pyname%.exe"

ECHO;
IF EXIST "build" RD "build" /s /q
IF EXIST "dist"  RD "dist"  /s /q
PAUSE




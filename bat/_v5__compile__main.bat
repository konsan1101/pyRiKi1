@ECHO OFF
cd ".."

ECHO;
IF EXIST "build" RD "build" /s /q
IF EXIST "dist"  RD "dist"  /s /q
PAUSE

set pyname=_v5__main__kernel
    echo;
    echo %pyname%.py
    pyinstaller %pyname%.py  -F --log-level ERROR  --icon="_icons/RiKi_start.ico"
IF EXIST "dist\%pyname%.exe"  ECHO "%pyname%.exe"
    copy "dist\%pyname%.exe"       "%pyname%.exe"
    del  "%pyname%.spec"
    copy "%pyname%.exe"        "C:\RiKi_v5_assistant\%pyname%.exe"
    del  "%pyname%.exe"

set pyname=_v5__main_vision
    echo;
    echo %pyname%.py
    pyinstaller %pyname%.py  -F --log-level ERROR  --icon="_icons/cam_start.ico" --add-binary "C:/Python3/Lib/site-packages/pyzbar/*.dll;pyzbar"
IF EXIST "dist\%pyname%.exe"  ECHO "%pyname%.exe"
    copy "dist\%pyname%.exe"       "%pyname%.exe"
    del  "%pyname%.spec"
    copy "%pyname%.exe"        "C:\RiKi_v5_assistant\%pyname%.exe"
    copy "%pyname%.exe"        "C:\RiKi_v5_camera\%pyname%.exe"
    del  "%pyname%.exe"

set pyname=_v5__main_desktop
    echo;
    echo %pyname%.py
    pyinstaller %pyname%.py  -F --log-level ERROR  --icon="_icons/rec_start.ico" --add-binary "C:/Python3/Lib/site-packages/pyzbar/*.dll;pyzbar"
IF EXIST "dist\%pyname%.exe"  ECHO "%pyname%.exe"
    copy "dist\%pyname%.exe"       "%pyname%.exe"
    del  "%pyname%.spec"
    copy "%pyname%.exe"        "C:\RiKi_v5_assistant\%pyname%.exe"
    copy "%pyname%.exe"        "C:\RiKi_v5_recorder\%pyname%.exe"
    del  "%pyname%.exe"

ECHO;
IF EXIST "build" RD "build" /s /q
IF EXIST "dist"  RD "dist"  /s /q
PAUSE




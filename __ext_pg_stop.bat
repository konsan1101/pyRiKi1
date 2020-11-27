@ECHO OFF

ECHO ...‚T...
ping localhost -w 1000 -n 2 >nul
ECHO ...‚S...
ping localhost -w 1000 -n 2 >nul
ECHO ...‚R...
ping localhost -w 1000 -n 2 >nul
ECHO ...‚Q...
ping localhost -w 1000 -n 2 >nul
ECHO ...‚P...
ping localhost -w 1000 -n 2 >nul

ECHO;
rem ECHO taskkill /im msaccess.exe /f >nul
rem      taskkill /im msaccess.exe /f >nul

ping localhost -w 1000 -n 3 >nul
EXIT



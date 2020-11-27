@ECHO OFF

IF EXIST "C:\Python37"  GOTO PY
IF EXIST "C:\Python38"  GOTO PY

:DOS
ECHO;@%1@%2
GOTO ABORT

:PY
start /b python __ext_face.py %1 %2

:ABORT
rem ping localhost -w 1000 -n 3 >nul
EXIT

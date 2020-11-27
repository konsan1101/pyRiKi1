@ECHO OFF
rem CALL __setpath.bat

ECHO;
ECHO ----------
ECHO 2020/11/20
ECHO ----------
ECHO Python==3.7.9
ECHO setuptools==50.3.2
ECHO pyinstaller==4.1
ECHO numpy==1.19.0
ECHO psutil==5.7.3
ECHO mojimoji==0.0.11
ECHO websocket-client==0.48.0

ECHO;
ECHO -----
ECHO tools
ECHO -----
rem           pip  install --upgrade pip
    python -m pip  install --upgrade pip
    python -m pip  install --upgrade setuptools
    python -m pip  install --upgrade pyinstaller

ECHO;
ECHO Waiting...10s
ping localhost -w 1000 -n 10 >nul

rem  --------
rem  PAUSE
rem  --------



ECHO;
ECHO -------
ECHO etc
ECHO -------
    python -m pip  install --upgrade pywin32
    python -m pip  install --upgrade pyautogui
    python -m pip  install --upgrade rainbow-logging-handler
    python -m pip  install --upgrade pysimplegui
    python -m pip  install --upgrade pysimpleguiqt
    python -m pip  install --upgrade psutil
    python -m pip  install --upgrade pycryptodome
rem ↓ use vs code
    python -m pip  install --upgrade pylint

ECHO;
ECHO -------------
ECHO communication
ECHO -------------
    python -m pip  install --upgrade requests
    python -m pip  install --upgrade requests_toolbelt
    python -m pip  install --upgrade uuid
    python -m pip  install --upgrade bs4
    python -m pip  install --upgrade pyopenssl
    python -m pip  install --upgrade feedparser
    python -m pip  install --upgrade selenium
    python -m pip  install --upgrade flask
    python -m pip  install --upgrade flask-login

ECHO;
ECHO -----
ECHO audio
ECHO -----
    python -m pip  install --upgrade wave
    python -m pip  install --upgrade sounddevice
    python -m pip  install --upgrade speechrecognition

ECHO;
ECHO ------
ECHO vision
ECHO ------
    python -m pip  install --upgrade pillow
    python -m pip  install --upgrade numpy
    python -m pip  install --upgrade opencv-python
    python -m pip  install --upgrade pyqt5
    python -m pip  install --upgrade pyzbar

ECHO;
ECHO ----------
ECHO IBM Watson
ECHO ----------
rem python -m pip  install --upgrade watson-developer-cloud==1.0.2
rem python -m pip  install --upgrade watson-developer-cloud
    python -m pip  install --upgrade ibm-watson
    python -m pip  install --upgrade ibm_cloud_sdk_core

rem ECHO;
rem ECHO -------------------------
rem ECHO IBM Watson,version update
rem ECHO -------------------------
rem python -m pip  uninstall -y  websocket-client
rem python -m pip  install       websocket-client==0.48.0

ECHO;
ECHO ---------------
ECHO microsoft,azure
ECHO ---------------
rem python -m pip  install --upgrade mstranslator
    python -m pip  install --upgrade cognitive_face
rem python -m pip  install --upgrade azure-storage
    python -m pip  install --upgrade azure-storage-blob==2.1.0

ECHO;
ECHO ---------------
ECHO amazon,AWS
ECHO ---------------
    python -m pip  install --upgrade boto3

ECHO;
ECHO --------
ECHO google
ECHO --------
    python -m pip  install --upgrade google-cloud-core
    python -m pip  install --upgrade google-cloud-speech
    python -m pip  install --upgrade google-cloud-translate
    python -m pip  install --upgrade google-cloud-vision
    python -m pip  install --upgrade google-api-python-client
    python -m pip  install --upgrade gtts
    python -m pip  install --upgrade googletrans
    python -m pip  install --upgrade goslate
    python -m pip  install --upgrade ggtrans
    python -m pip  uninstall -y gtts-token
    python -m pip  install --upgrade gtts-token



rem  --------
     PAUSE
rem  --------

rem ECHO;
rem ECHO ---------------------------
rem ECHO pyinstaller compile setting
rem rem  setuptools==49.6.0, 44.0.0
rem ECHO ---------------------------
rem rem  python -m pip  install --upgrade numpy
rem      python -m pip  uninstall -y      numpy
rem      python -m pip  install           numpy==1.19
rem rem  python -m pip  install --upgrade setuptools
rem rem  python -m pip  uninstall -y      setuptools
rem rem  python -m pip  install           setuptools==49.6.0
rem rem  python -m pip  install --upgrade pyinstaller
rem rem  python -m pip  uninstall -y      pyinstaller
rem rem  python -m pip  install           pyinstaller==3.6



ECHO;
ECHO -------------------
ECHO pip list --outdated
ECHO -------------------
    python -m pip  list --outdated

ECHO;
ECHO Waiting...5s
ping localhost -w 1000 -n 5 >nul

ECHO;
ECHO --------
ECHO pip list
ECHO --------
    python -m pip  list

rem  --------
     PAUSE
rem  --------

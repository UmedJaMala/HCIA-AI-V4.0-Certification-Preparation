@echo off
title HCIA-AI ResNet-50 Flower Classifier UI
cd /d "%~dp0"
echo ========================================================
echo  Launching HCIA-AI ResNet-50 Flower Classifier Web UI
echo  GullNas - Interactive Deep Learning Vision System
echo ========================================================

:: Determine Python executable
set "PY_CMD=python"
if exist "%USERPROFILE%\miniconda3\envs\hcia_ai\python.exe" (
    set "PY_CMD=%USERPROFILE%\miniconda3\envs\hcia_ai\python.exe"
) else if exist "C:\Users\HC\miniconda3\envs\hcia_ai\python.exe" (
    set "PY_CMD=C:\Users\HC\miniconda3\envs\hcia_ai\python.exe"
)

:: Check if required libraries exist, install if missing
%PY_CMD% -c "import flask, torch, torchvision, PIL" >nul 2>&1
if errorlevel 1 (
    echo [!] Missing required packages. Installing automatically...
    %PY_CMD% -m pip install -r requirements.txt
)

echo [*] Starting web server...
%PY_CMD% app.py
pause

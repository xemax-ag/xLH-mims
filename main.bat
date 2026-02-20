@echo off
setlocal

cls

rem Get directory of this script and switch to it
set "shell_dir=%~dp0"
cd /d "%shell_dir%"

rem Activate virtual environment
call ".venv\Scripts\activate.bat"

rem Run uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8099 --reload --reload-dir "app"

endlocal
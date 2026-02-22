setlocal
@echo off
cls

call "%~dp0%.venv\Scripts\activate.bat"
call python "%~dp0%notebooks\settings\run_jupyterlab.py"
call "%~dp0%.venv\Scripts\deactivate.bat"

endlocal
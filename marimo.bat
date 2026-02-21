setlocal
@echo off
cls

call "%~dp0%.venv\Scripts\activate.bat"
cd notebooks\marimo\src
uv run marimo edit
call "%~dp0%.venv\Scripts\deactivate.bat"

endlocal
@echo off
REM Set the current directory as PYTHONPATH so Python resolves 'src' properly
set PYTHONPATH=%cd%
python simulation_runner.py
pause
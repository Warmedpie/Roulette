@echo off
setlocal
cd /d %~dp0
python3.exe roulette.py %*
pause
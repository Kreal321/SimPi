@echo off
for /f "tokens=4" %%a in ('route print^|findstr 0.0.0.0.*0.0.0.0') do (
    set IP=%%a
)

python Server/main.py remote %IP%

pause>nul
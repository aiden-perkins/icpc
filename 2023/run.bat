@echo off
set num=%1
set times=%2
if "%times%"=="" (
    set times=1
)
for /L %%i in (1, 1, %times%) do (
    python ./%num%/main.py < ./%num%/%%i.in
)

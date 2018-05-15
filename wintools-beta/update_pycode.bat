@echo off
title BITS-PyOS PyCode Updater
cls

echo If you started this script in the "wintools-beta" folder
echo press any key, otherwise, press CTRL+C or close this window.
pause>NUL

goto :getdrive

:getdrive
echo.
set /p "bpos_drive=Enter a drive letter (A-Z): "
if exist "%bpos_drive%:\" goto :driveok
echo Invalid!
goto :getdrive

:driveok
echo.
echo Changing directories . . .
cd ..
echo Checking if there is PyOS code on the %bpos_drive%: drive . . .
if exist "%bpos_drive%:\pyos\" goto :verifydeletion
goto :copyit

:verifydeletion
echo.
echo There is existing PyOS code on the %bpos_drive%: drive,
set /P "bpos_delete=would you like to replace it? [Y/N] "
if /I "%bpos_delete%" EQU "Y" goto :deleteit
if /I "%bpos_delete%" EQU "N" goto :cancelled
echo Invalid!
goto :verifydeletion

:deleteit
echo.
echo Deleting old code . . .
rmdir /s /q "%bpos_drive%:\pyos"
goto :copyit

:copyit
echo Copying new code . . .
echo.
xcopy /s pycode "%bpos_drive%:\pyos\"
goto :done

:done
echo.
echo Completed!
pause
goto :end

:cancelled
echo.
echo Cancelled.
pause
goto :end

:end
cls
exit
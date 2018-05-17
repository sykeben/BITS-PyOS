@echo off
title BITS-PyOS Bootable Disk Builder
cls

echo If you started this script in the "wintools-beta" folder
echo press any key, otherwise, press CTRL+C or close this window.
pause>NUL



echo.
::::::::::::::::::::::::::::::::::::::::::::
:: Elevate.cmd - Version 4
:: MODIFIED FOR BITS-PYOS DISK BUILDER
:: Automatically check & get admin rights
::::::::::::::::::::::::::::::::::::::::::::
 @echo off
 echo Checking for admin privilages . . .

:init
 setlocal DisableDelayedExpansion
 set cmdInvoke=1
 set winSysFolder=System32
 set "batchPath=%~0"
 for %%k in (%0) do set batchName=%%~nk
 set "vbsGetPrivileges=%temp%\OEgetPriv_%batchName%.vbs"
 setlocal EnableDelayedExpansion

:checkPrivileges
  NET FILE 1>NUL 2>NUL
  if '%errorlevel%' == '0' ( goto gotPrivileges ) else ( goto getPrivileges )

:getPrivileges
  if '%1'=='ELEV' (echo ELEV & shift /1 & goto gotPrivileges)
  ECHO.
  ECHO **************************************
  ECHO Invoking UAC for Privilege Escalation
  ECHO **************************************

  ECHO Set UAC = CreateObject^("Shell.Application"^) > "%vbsGetPrivileges%"
  ECHO args = "ELEV " >> "%vbsGetPrivileges%"
  ECHO For Each strArg in WScript.Arguments >> "%vbsGetPrivileges%"
  ECHO args = args ^& strArg ^& " "  >> "%vbsGetPrivileges%"
  ECHO Next >> "%vbsGetPrivileges%"

  if '%cmdInvoke%'=='1' goto InvokeCmd 

  ECHO UAC.ShellExecute "!batchPath!", args, "", "runas", 1 >> "%vbsGetPrivileges%"
  goto ExecElevation

:InvokeCmd
  ECHO args = "/c """ + "!batchPath!" + """ " + args >> "%vbsGetPrivileges%"
  ECHO UAC.ShellExecute "%SystemRoot%\%winSysFolder%\cmd.exe", args, "", "runas", 1 >> "%vbsGetPrivileges%"

:ExecElevation
 "%SystemRoot%\%winSysFolder%\WScript.exe" "%vbsGetPrivileges%" %*
 exit /B

:gotPrivileges
 setlocal & cd /d %~dp0
 if '%1'=='ELEV' (del "%vbsGetPrivileges%" 1>nul 2>nul  &  shift /1)

 ::::::::::::::::::::::::::::
 ::START
 ::::::::::::::::::::::::::::
 echo Finished.



goto :getdrive

:getdrive
echo.
set /p "bpos_drive=Enter a drive letter (A-Z): "
if /I "%bpos_drive%" EQU "%systemdrive%" goto :sysdisk
if exist "%bpos_drive%:\" goto :makesure
echo Invalid!
goto :getdrive

:sysdisk
echo You cannot modify your system drive like that!
echo Invalid!
goto :getdrive

:makesure
echo.
echo This will modify the selected drive in such a way that
echo all data on it will be lost, are you really sure that
set /P "bpos_doit=you want to continue? [Y/N] "
if /I "%bpos_doit%" EQU "Y" goto :doit
if /I "%bpos_doit%" EQU "N" goto :cancelled
echo Invalid!
goto :makesure

:doit
echo.
echo Formatting . . .
title BITS-PyOS Bootable Disk Builder - Formatting
echo.
format %bpos_drive%: /FS:FAT32 /V:BITS-PYOS /Q
echo.
echo Changing directories . . .
title BITS-PyOS Bootable Disk Builder - Changing Directories
cd ..
cd bits
echo Copying BITS system . . .
title BITS-PyOS Bootable Disk Builder - Copying BITS System
echo.
xcopy /s boot %bpos_drive%:\boot\
echo.
echo Copying BITS EFI loaders . . .
title BITS-PyOS Bootable Disk Builder - Copying BITS EFI Loaders
echo.
xcopy /s efi %bpos_drive%:\efi\
echo.
echo Changing directories . . .
title BITS-PyOS Bootable Disk Builder - Changing Directories
cd ..
cd syslinux
cd bios
cd win32
echo Installing syslinux onto the drive . . .
title BITS-PyOS Bootable Disk Builder - Installing Syslinux onto the Drive
syslinux.exe -m -a %bpos_drive%:
echo Changing directories . . .
title BITS-PyOS Bootable Disk Builder - Changing Directories
cd ..
cd ..
cd ..
echo Copying PyCode . . .
title BITS-PyOS Bootable Disk Builder - Copying PyCode
echo.
xcopy /s pycode %bpos_drive%:\pyos\
echo.
echo Copying DSL disk image . . .
title BITS-PyOS Bootable Disk Builder - Copying DSL Disk Image
echo.
copy /s dsl.iso %bpos_drive%:\dsl.iso
echo.
echo Generating build info . . .
title BITS-PyOS Bootable Disk Builder - Generating Build Info
echo BUILD INFO>%bpos_drive%:\info.txt
echo.>>%bpos_drive%:\info.txt
echo Built With:    BITS-PyOS Bootable Disk Builder>>%bpos_drive%:\info.txt
echo Date:          %date%>>%bpos_drive%:\info.txt
echo Time:          %time%>>%bpos_drive%:\info.txt
echo Windows User:  %username%>>%bpos_drive%:\info.txt
echo Computer Name: %computername%>>%bpos_drive%:\info.txt
echo Cleaning up . . .
title BITS-PyOS Bootable Disk Builder - Cleaning Up
cd wintools-beta
goto :done

:done
title BITS-PyOS Bootable Disk Builder
echo.
echo Completed!
pause
goto :end

:cancelled
title BITS-PyOS Bootable Disk Builder
echo.
echo Cancelled.
pause
goto :end

:end
cls
exit
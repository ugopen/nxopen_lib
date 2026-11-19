@echo off
rem ========================================================================= 
rem                                                                        
rem             Copyright 2018 Siemens Product Lifecycle Management Software Inc.
rem                     All Rights Reserved.
rem                                                                          
rem ========================================================================= 
rem
rem Script Name:  GRADE.BAT
rem
rem This script is used to start up GRADE.
rem
rem ========================================================================= 
rem  
rem
setlocal
set filename=%1
if [%1] == [] goto :skipfileset
call :setfile %1
 
:skipfileset
:: Set the fallback working directory location if no file is specified.
cd /d %SystemDrive%\users\default
:: Use a user specific working directory if no file is specified and this better directory exists.
if exist "%HOMEDRIVE%%HOMEPATH%" cd /d %HOMEDRIVE%%HOMEPATH%
:: Use the file directory if a valid file argument is passed.
if exist %file_dir% cd /d %file_dir%
set PATH=%~dp0..\nxbin;%PATH%
"%~dp0\grade.exe" "%filename%"
endlocal
goto :eof
:setfile
set file_dir=%~dp1
goto :eof
:eof
@echo on



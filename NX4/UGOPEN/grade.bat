@echo off
rem ========================================================================= 
rem                                                                        
rem       Copyright (c) 1996-2001 Unigraphics Solutions, Inc.
rem                  Unpublished - All rights reserved                      
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
set base=%1
set base_dir=%base:"=%
if exist "%HOMEDRIVE%%HOMEPATH%" cd /d %HOMEDRIVE%%HOMEPATH%
if not exist "%HOMEDRIVE%%HOMEPATH%" cd /d %SystemDrive%\users\default
set PATH=%base_dir%\ugii;%PATH%
"%base_dir%\ugopen\grade.exe"
endlocal
@echo on

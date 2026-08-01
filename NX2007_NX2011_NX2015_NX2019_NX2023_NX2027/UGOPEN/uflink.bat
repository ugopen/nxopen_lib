@echo off
rem ===========================================================================
rem 
rem           Copyright (c) 1996 Electronic Data Systems Corporation
rem                    Unpublished - All rights reserved
rem 
rem ===========================================================================
rem ###########################################################################
rem   NOTE: This script was written for the Windows NT DOS Shell Environment.
rem         To guarantee that this script will run correctly, the line
rem @echo off
rem         should be at the beginning of this script as line 1.
rem ###########################################################################
rem 
rem 
rem ###########################################################################

if "%1"=="AddNXOpenCppLib" goto AddLib
set TARGET=%1
set FILE=%2
if "%TARGET%"=="" goto :usage
if "%FILE%"=="" goto :usage

if "%UGII_USERFCN%"=="" goto :noenvvar
if not exist "%UGII_USERFCN%"\uflink.mak goto :nomkfile

set allNXOpenCppLibs=
for %%d in (%UGII_USERFCN%\libnxopencpp*.lib) do call %0 AddNXOpenCppLib %%~nxd


if "%TARGET%"=="ufdll" goto doit
if "%TARGET%"=="UFDLL" goto doit
if "%TARGET%"=="ufexe" goto doit
if "%TARGET%"=="UFEXE" goto doit
if "%TARGET%"=="ufobj" goto doit
if "%TARGET%"=="UFOBJ" goto doit
echo.
echo target = %target%
goto :usage

:doit

rem now accumulate the extra argument into variable UFEXTRA
shift
shift
set UFEXTRA=
if "%1"=="" goto :endloop
set UFEXTRA=%1
:loop
shift
if "%1"=="" goto :endloop
set UFEXTRA=%UFEXTRA% %1
goto :loop
:endloop

nmake -nologo -f "%UGII_USERFCN%\uflink.mak" %TARGET%=%FILE% "UFEXTRA=%UFEXTRA%" "allNXOpenCppLibs=%allNXOpenCppLibs%"
set allNXOpenCppLibs=
goto :end
:noenvvar
echo Environment variable UGII_USERFCN is not set.
:nomkfile
echo Makefile %UGII_USERFCN%\uflink.mak does not exist
goto :end
:AddLib
if not defined allNXOpenCppLibs (
 set allNXOpenCppLibs=%2
) else (
 if not "%2"=="" set allNXOpenCppLibs=%allNXOpenCppLibs% %2
)
goto end
:usage
echo.
echo Usage: uflink (TARGET)=(targetname) [optional object or libraries]
echo.
echo TARGET must assume one of the following values (case insensitive):
echo    UFDLL=(basename).dll
echo    UFEXE=(basename).exe
echo    UFOBJ=(basename).obj
echo.
echo A dll is an Internal User Function program.
echo An exe is an External User Function program.
echo.
echo If the environment variable NODEBUG is set then the target
echo will be compiled or linked with full optimization.  Else
echo the target will be compiled or linked for debug.
echo.
:end

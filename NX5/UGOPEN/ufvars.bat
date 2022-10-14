@echo off
rem ===========================================================================
rem 
rem                Copyright (c) 1996-1999 Unigraphics Solutions Inc.
rem                       Unpublished - All rights reserved
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

rem In order for ufcomp and uflink to work properly the environment variables
rem PATH, INCLUDE, and LIB must be set to include the locations of the
rem pertinent Microsoft Visual C++ directories, i.e.
rem 
rem 	PATH	%MSVCDir%\bin
rem 	INCLUDE	%MSVCDir%\include
rem 	LIB	%MSVCDir%\lib
rem 
rem where %MSVCDir% is the root of the Visual C++ installed files.
rem 
rem These variables may be set by invoking %MSVCDir%\bin\vcvars32.bat
rem or by selecting the "Register Environment Variables" option when
rem installing Microsoft Visual C++.  If doing the latter note that
rem installation must be done for each potential user.  Invoking vcvars32.bat
rem might best be done from %UGII_BASE_DIR%\ugopen\ufvars.bat once the 
rem value of %MSVCDir% is known.  If you choose, do that here by
rem removing the "rem" keyword and replacing %MSVCDir% with the proper
rem location.  The following is the default location for Visual C++ 6.0...
rem
rem set MSVCDir=C:\Program Files\Microsoft Visual Studio\VC98
rem set MSVCDir=C:\Program Files\Microsoft Visual Studio .NET\Vc7
rem set MSVCDir=C:\Program Files\Microsoft SDK
rem set MSVCDir=C:\Program Files\Microsoft Visual Studio 8\VC
rem set MSVCDir=C:\Program Files (x86)\Microsoft Visual Studio 8\VC

if "%MSVCDir%"=="" goto nomsdevdir
if "%processor_architecture%"=="" goto noprocarch
if "%processor_architecture%"=="AMD64" goto haveamd64
if "%processor_architew6432%"=="AMD64" goto haveamd64
rem
rem Set up the visual C++ environment
rem
if not exist "%MSVCDir%\bin\vcvars32.bat" goto novcvars32
call "%MSVCDir%\bin\vcvars32.bat" %processor_architecture%
set base=%1
set base_dir=%base:"=%
set UGII_USERFCN=%base_dir%\ugopen
set UGII_UGOPENPP=%base_dir%\ugopenpp
set PATH=%UGII_USERFCN%;%PATH%
set INCLUDE=%INCLUDE%;%UGII_USERFCN%;%UGII_UGOPENPP%
set CL=-c -EHsc /GR -nologo -MD
goto setdoskey
:haveamd64
rem
rem Set up the Visual C++ V8.0 SDK environment
rem
if not exist "%MSVCDir%\vcvarsall.bat" goto novcvars32
call "%MSVCDir%\vcvarsall.bat" AMD64
set base=%1
set base_dir=%base:"=%
set UGII_USERFCN=%base_dir%\ugopen
set UGII_UGOPENPP=%base_dir%\ugopenpp
set PATH=%UGII_USERFCN%;%PATH%
set INCLUDE=%INCLUDE%;%UGII_USERFCN%;%UGII_UGOPENPP%
set CL=-c -Ox /GR -nologo -MD -ZI -EHsc
:setdoskey
doskey UFCOMP=CL $*
echo Environment set for Unigraphics UG/Open
goto end
:novcvars32
echo The MSVCDir environment variable is not set correctly.
echo You must modify the ufvars.bat file to correct this.
goto abend
:nomsdevdir
echo The MSVCDir environment variable is not defined
echo You must modify the ufvars.bat file to define this
goto abend
:noprocarch
echo The processor_architecture environment variable is not defined
echo Check your system installation.
goto end
:end

echo UGII_USERFCN is %UGII_USERFCN%
echo PATH is %PATH%
echo INCLUDE is %INCLUDE%
echo LIB is %LIB%
echo CL is %CL%
:abend

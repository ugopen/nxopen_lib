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
rem location.  The following is the default location from the MS installs.
rem Your site might install them in a different location.
rem
rem set MSVCDir=C:\Program Files\Microsoft Visual Studio\VC98
rem set MSVCDir=C:\Program Files\Microsoft Visual Studio .NET\Vc7
rem set MSVCDir=C:\Program Files\Microsoft SDK
rem NX7
rem set MSVCDir=C:\Program Files\Microsoft Visual Studio 8\VC
rem set MSVCDir=C:\Program Files (x86)\Microsoft Visual Studio 8\VC
rem set MSVCDir=C:\Program Files\Microsoft Visual Studio 9\VC
rem set MSVCDir=C:\Program Files (x86)\Microsoft Visual Studio 9\VC
rem NX8.0/NX8.5 wntx64
rem set MSVCDir=C:\Program Files\Microsoft Visual Studio 10\VC
rem NX8.0/NX8.5 wntx32
rem set MSVCDir=C:\Program Files (x86)\Microsoft Visual Studio 10\VC
rem NX9.0/NX10 wntx64
rem set MSVCDir=C:\Program Files\Microsoft Visual Studio 11.0\VC
rem NX11.0 wntx64
rem set MSVCDir=C:\Program Files\Microsoft Visual Studio 12.0\VC
rem 
rem Usages:
rem        ufvars.bat [NX installation path] [platform]
rem        e.g.  
rem             ufvars.bat                        -- Setup build environment considering current directory as NX installation directory
rem             ufvars.bat %UGII_BASE_DIR%        -- Setup build environment considering %UGII_BASE_DIR% as NX installation directory for OS platform
rem             ufvars.bat %UGII_BASE_DIR% 32    -- Setup build environment considering %UGII_BASE_DIR% as NX installation directory for 32-bit platform
rem             ufvars.bat %UGII_BASE_DIR% 64  -- Setup build environment considering %UGII_BASE_DIR% as NX installation directory for 64-bit platform
rem             ufvars.bat 64                -- Setup build environment considering current directory as NX installation directory for 64-bit platform
set force32=
set force64=
set base=
for %%i in (%*) do (
	if exist %%i (
	set base=%%i
	) else if "%%i"=="32" (
	set force32=true
	) else if "%%i"=="64" (
	set force64=true
	)
)
if "%MSVCDir%"=="" goto nomsdevdir
if defined force64 goto haveamd64
if defined force32 goto haveX86
if "%processor_architecture%"=="" goto noprocarch
if "%processor_architecture%"=="AMD64" goto haveamd64
if "%processor_architew6432%"=="AMD64" goto haveamd64
:haveX86
rem
rem Set up the visual C++ environment
rem
if not exist "%MSVCDir%\bin\vcvars32.bat" goto novcvars32
call "%MSVCDir%\bin\vcvars32.bat" %processor_architecture%
set base_dir=%base:"=%
set UGII_USERFCN=%base_dir%\ugopen
set UGII_UGOPENPP=%base_dir%\ugopenpp
set PATH=%UGII_USERFCN%;%PATH%
set INCLUDE=%INCLUDE%;%UGII_USERFCN%;%UGII_UGOPENPP%
set CL=-c -EHsc /GR -nologo -MD -D_SECURE_SCL=0
goto setdoskey
:haveamd64
rem
rem Set up the Visual C++ V8.0 SDK environment
rem
if not exist "%MSVCDir%\vcvarsall.bat" goto novcvars32
call "%MSVCDir%\vcvarsall.bat" AMD64
set base_dir=%base:"=%
set UGII_USERFCN=%base_dir%\ugopen
set UGII_UGOPENPP=%base_dir%\ugopenpp
set PATH=%UGII_USERFCN%;%PATH%
set INCLUDE=%INCLUDE%;%UGII_USERFCN%;%UGII_UGOPENPP%
set CL=-c -Ox /GR -nologo -MD -ZI -EHsc -D_SECURE_SCL=0
goto setdoskey
:setdoskey
doskey UFCOMP=CL $*
echo Environment set for Unigraphics UG/Open
goto end
:novcvars32
echo The MSVCDir environment variable is not set correctly.
echo This variable is necessary only when using uflink or starting up Studio
echo from this window. You must modify the ufvars.bat file to correct this.
goto abend
:nomsdevdir
echo The MSVCDir environment variable is not defined
echo This variable is necessary only when using uflink or starting up Studio
echo from this window. You must modify the ufvars.bat file to define this.
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

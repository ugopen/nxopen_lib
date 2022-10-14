@echo off
rem ===========================================================================
rem 
rem           Copyright (c) 2012 Siemens PLM
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
if not defined UGII_JAVA_HOME (
@for /f "tokens=*" %%I in (' "%UGII_BASE_DIR%\nxbin\env_print" UGII_JAVA_HOME') do set UGII_JAVA_HOME=%%I
)

if defined UGII_JAVA_HOME (
"%UGII_JAVA_HOME%\bin\java" -jar "%UGII_BASE_DIR%\ugopen\SignJar.jar"  %*
) else (
echo UGII_JAVA_HOME must be defined
goto end_of_file
)
:end_of_file
@echo on


rem ===========================================================================
rem 
rem           Copyright (c) 2023 Siemens PLM
rem                    Unpublished - All rights reserved
rem 
rem ===========================================================================
rem ###########################################################################
rem   NOTE: Script to facilitate signing of dlls and the running of the NXOpen BomReporter
rem         in NXOpen visual studio templates
rem         
rem ###########################################################################
rem 
rem 
rem ###########################################################################



REM flag to indicate if this bat file is being called from a C++ or .NET project
set cppOrDotNet=%1
REM Visual Studio's $(TargetDir) variable
set TargetDirForBat=%2
REM Visual Studio's $(TargetFileName) variable
set TargetFileNameForBat=%3
REM Visual Studio's $(ProjectDir) variable
set ProjectDirForBat=%4
REM Visual Studio's $(ProjectName) variable
set ProjectNameForBat=%5



REM calling from a .NET project
IF "%cppOrDotNet%"=="DotNet" (
IF EXIST "%UGII_BASE_DIR%\nxbin\SignDotNet.exe" "%UGII_BASE_DIR%\nxbin\SignDotNet.exe" %TargetDirForBat%%TargetFileNameForBat%
IF EXIST "%DOTNETBOMGENERATOR_PATH%\bin\DotNetBomGenerator.exe" "%DOTNETBOMGENERATOR_PATH%\bin\DotNetBomGenerator.exe" -apps %TargetDirForBat% -outDir %TargetDirForBat%
) 

REM calling from a C++ project
IF "%cppOrDotNet%"=="CPP" (
IF EXIST "%UGII_BASE_DIR%\nxbin\signcpp.exe" "%UGII_BASE_DIR%\nxbin\signcpp.exe" %TargetDirForBat%%TargetFileNameForBat%
IF EXIST "%NXOPENREPORTER_PATH%\bin\CPPProjectReader.exe" "%NXOPENREPORTER_PATH%\bin\CPPProjectReader.exe" -apps %ProjectDirForBat% -outDir %ProjectDirForBat%  -autoyes
IF EXIST "%NXOPENREPORTER_PATH%\bin\CPPBomReporter.exe" "%NXOPENREPORTER_PATH%\bin\CPPBomReporter.exe" -d %ProjectDirForBat% -o %ProjectDirForBat%\%ProjectNameForBat%  -autoyes
) 



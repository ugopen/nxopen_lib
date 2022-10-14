@echo off
setlocal
:: ===========================================================================
::
:: Script Name:        install_nxopen_wizards.bat.
::
:: This script installs the nxopen_wizards with the following steps.
:: 1. Call :Reg_Query subroutine to find the INSTALLDIR for NX %NX_VER.
:: 2. Check that UGOPEN\vs_files folder exists, if not, exit this script.
:: 3. Call :Reg_query to get installed ProductDir for MS Visual Studio %VC_VER
:: 4. If VC is not found in Registry, may not be installed, exit this script.
:: 5. Check if VC ProductDir exists. May have been deleted. if not, exit.
:: 6. Xcopy the UGOPEN VS Wizard files into VS ProductDir.
::
:: ===========================================================================
::
:: Copyright 2014 Siemens Product Lifecycle Management Software Inc. All Rights Reserved.
::
:: ===========================================================================
:: 
:: ==========================================================================


:: Version control variables.__________________________________________________
:: The NX version containing UGOPEN\vs_files App Wizard folder.
set NX_VER=12.0
:: The Visual Studio C++ version to place the App Wizards.
set VC_VER=14.0



:: Find and check UGOPEN.______________________________________________________
:: Get NX version %NX_VER installed dir, then set and check %UGOPEN_VS_FILES.
:: Call :Reg_Query to get INSTALLDIR. The subroutine tries both 32 & 64 bit
:: Reg keys to set %VAL. The Product key (arg2) must be quoted.
::
call :Reg_Query INSTALLDIR "Unigraphics Solutions\NX\%NX_VER%"
::
Rem Check that we found an INSTALLDIR Registry key for NX %NX_VER.
if not defined VAL (
  Rem Got nothing for %VAL. That means we couldn't find a registry key.
  echo NX %NX_VER% is not installed. Registry Key was not found.
  set RETURN_CODE=2
  goto :END_SCRIPT
)
::
Rem Got the Installdir, now check UGOPEN was installed and vs_files exists.
if not exist "%VAL%\ugopen\vs_files" (
  echo NX %NX_VER% UGOPEN folder does not exist. It may not be installed.
  set RETURN_CODE=3
  goto :END_SCRIPT
)
::
Rem Got good value for NX INSTALLDIR, set %UGOPEN_VS_FILES for use in xcopy.
set UGOPEN_VS_FILES=%VAL%\ugopen\vs_files



:: Find and check VISUAL STUDIO.______________________________________________
:: Get VS version %VC_VER Product Directory. then set and check %MS_VS_DIR.
:: Call :Reg_Query to get ProductDir. The subroutine tries both 32 & 64 bit
:: Reg keys to set %VAL. The Product key (arg2) must be quoted.
::
call :Reg_Query ProductDir "Microsoft\VisualStudio\%VC_VER%\Setup\VS"
::
Rem Check that we found a Registry key for Visual Studio.
if not defined VAL (
  Rem Got nothing for %VAL. That means we couldn't find a registry key.
  echo. Visual Studio %VC_VER% is not installed. Registry Key was not found.
  set RETURN_CODE=2
  goto :END_SCRIPT
)
::
Rem Now make sure that the Product Dir still exists. May have been deleted.
if not exist "%VAL%" (
  echo Visual Studio Folder does not exist: %VAL%
  set RETURN_CODE=3
  goto :END_SCRIPT
)
::
Rem Got good value for the VS ProductDir, set %MS_VS_DIR for use in xcopy.
set MS_VS_DIR=%VAL%



:: COPY FILES.________________________________________________________________
:: We found the source folder and the destination folder - do the copy.
echo.Copying UGOPEN App Wizard files to Microsoft Visual Studio.
echo.
REM echo.    The following command would execute:
xcopy /i/e/k/h/r/y/q "%UGOPEN_VS_FILES%\*.*" "%MS_VS_DIR%"
if errorlevel 1 (
  set RETURN_CODE=%ERRORLEVEL%
  echo ERROR copying files to %MS_VS_DIR%
  goto :END_SCRIPT
) else (
  echo.
  echo Done. App Wizard files copied to Visual Studio.
  set RETURN_CODE=0
  goto :END_SCRIPT
)



:: Logical end of script.
goto :END_SCRIPT



:: REGISTER QUERY SUBROUTINE.__________________________________________________
:Reg_Query
  ::
  set VAL=
  set NAME=%1%
  set ARG2=%2%
  set ARG2=%ARG2:"=%
  ::
  :: Make 32 & 64 bit keys by prepending HKLM\Software... to arg2.
  set KEY32=HKLM\Software\%ARG2%
  set KEY64=HKLM\Software\wow6432node\%ARG2%
  ::
  :: The reg querys below return all the values in the KEY. Then findstr
  :: filters it down to the (1) line we want, which contains 3 or more fields.
  :: The 3rd field is a path which COULD contain imbedded spaces. 
  ::
  :: The for/f cmd performs the req query | findstr command but defines the
  :: output tokens (fields) we want to be #1, #2 and all remaining fields so
  :: it can include a path with spaces. The for/f EXplicity sets the named
  :: variable %%A to field #1 and then IMplicitly sets %B to field #2 and %C
  :: to all remaining fields - which will be the path we want.
  ::
  :: 1st Try 32 bit key. If it works do the for/f & findstr to get the value.
  :: Pre-test key before doing for/f cuz cant shut off errs inside for/f.
  reg query "%KEY32%" 1>nul 2>&1 && (
    for /F "tokens=1,2,*" %%A in ('reg query "%KEY32%" ^| findstr %NAME%') do (
      :: Found a value so set %VAL and return.
      set VAL=%%C
      goto :EOF
    )
  )
  ::
  :: Didn't find 32 bit key, or didnt find key name (%NAME). So try 64 bit key.
  ::
  :: Try 64 bit key. If it works do the for/f & findstr to get the value.
  :: Pre-test key before doing for/f cuz cant shut off errs inside for/f.
  reg query "%KEY64%" 1>nul 2>&1 && (
    for /F "tokens=1,2,*" %%A in ('reg query "%KEY64%" ^| findstr %NAME%') do (
      :: Found a value so set %VAL and return.
      set VAL=%%C
      goto :EOF
    )
  )
  :: If we got here we didn't find either key value, so return with nothing.
  goto :EOF
  ::
:: End of Reg_Query



:: END SCRIPT and exit with return status._____________________________________
:END_SCRIPT
::
:: Tunnel the return code thru the endlocal, then exit with return code.
endlocal & set RETURN_CODE=%RETURN_CODE%
exit /B %RETURN_CODE%
@echo on

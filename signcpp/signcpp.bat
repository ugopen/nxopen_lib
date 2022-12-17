@echo off
SET UGII_BASE_DIR=E:\Program Files\Siemens\NX1953
SET UGII_ROOT_DIR=E:\Program Files\Siemens\NX1953\UGII

for /f "tokens=*" %%i in ('dir/s/b *.dll') do move "%%i" "%UGII_BASE_DIR%\NXBIN\" & "%UGII_BASE_DIR%\NXBIN\signcpp.exe" "%UGII_BASE_DIR%\NXBIN\%%~ni%%~xi" & move "%UGII_BASE_DIR%\NXBIN\%%~ni%%~xi" "%%i"
for /f "tokens=*" %%i in ('dir/s/b *.exe') do move "%%i" "%UGII_BASE_DIR%\NXBIN\" & "%UGII_BASE_DIR%\NXBIN\signcpp.exe" "%UGII_BASE_DIR%\NXBIN\%%~ni%%~xi" & move "%UGII_BASE_DIR%\NXBIN\%%~ni%%~xi" "%%i"

PAUSE>nul
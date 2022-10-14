@echo off
SET UGII_BASE_DIR=D:\Program Files\Siemens\NX11.0
SET UGII_ROOT_DIR=D:\Program Files\Siemens\NX11.0\UGII

for /f "tokens=*" %%i in ('dir/s/b *.dll') do "%UGII_BASE_DIR%\NXBIN\signcpp.exe" "%%i"
for /f "tokens=*" %%i in ('dir/s/b *.exe') do "%UGII_BASE_DIR%\NXBIN\signcpp.exe" "%%i"

PAUSE
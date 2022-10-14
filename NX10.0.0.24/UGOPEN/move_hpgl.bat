@echo off
rem ===========================================================================
rem 
rem                Copyright (c) 2004 UGS PLM Solutions
rem                  Unpublished - All rights reserved
rem 
rem
rem     Invoke the move_hpgl perl script which is used with an NX Plotting
rem     "Render File Then Execute" queue. See the move_hpgl.pl script for
rem     details.
rem
rem     This script assumes that the perl script resides in the ugopen kit and 
rem     that the perl executable is accessible via the current PATH setting.
rem     You may need to modify this script in order to invoke the perl script
rem     correctly.
rem ===========================================================================
rem 
perl %UGII_BASE_DIR%\ugopen\move_hpgl.pl %*

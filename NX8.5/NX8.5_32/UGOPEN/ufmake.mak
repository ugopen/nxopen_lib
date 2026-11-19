#===============================================================================
#
#          Copyright (c) 1998 Unigraphics Solutions
#            Unpublished - All rights reserved
#
#===============================================================================
################################################################################
#  NOTE: This makefile was written for the Windows NT NMAKE Environment.
################################################################################
#
#
##############################################################################

!include <ntwin32.mak>

!ifndef UGII_USERFCN
!error  UGII_USERFCN must be defined
!endif

UGOpenLibs         = "$(UGII_USERFCN)\libufun.lib"
UGOpenInternalLibs = "$(UGII_USERFCN)\libugopenint.lib"

.obj.dll: 
	@echo....Creating $@
	$(link) -nologo $(ldebug) $(dlllflags) -out:$*.dll $** $(conlibsdll) $(UGOpenLibs) $(UGOpenInternalLibs)

.obj.exe: 
	@echo....Creating $@
	$(link) -nologo $(ldebug) $(conlflags) -out:$*.exe $** $(conlibsdll) $(UGOpenLibs)

CFLAGS = -nologo $(cflags) $(cdebug) $(cvarsdll) -I. -I"$(UGII_USERFCN)"

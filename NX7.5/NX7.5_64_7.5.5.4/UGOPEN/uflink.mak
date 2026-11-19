#===============================================================================
#
#              Copyright (c) 1998 Unigraphics Solutions Inc.
#          Copyright (c) 1996,1997 Electronic Data Systems Corporation
#                   Unpublished - All rights reserved
#
#===============================================================================
################################################################################
#  NOTE: This makefile was written for the Windows NT NMAKE Environment.
################################################################################
#
#
#
##############################################################################

!include <ntwin32.mak>

!ifndef UGII_USERFCN
!error  UGII_USERFCN must be defined
!endif

UGOpenLibs         = "$(UGII_USERFCN)\libufun.lib" "$(UGII_USERFCN)\libnxopencpp.lib" "$(UGII_USERFCN)\libopenpp.lib" "$(UGII_USERFCN)\libvmathpp.lib"
UGOpenInternalLibs = "$(UGII_USERFCN)\libugopenint.lib" "$(UGII_USERFCN)\libnxopenuicpp.lib" "$(UGII_USERFCN)\libopenintpp.lib"

# this target is for creating a .dll without a pre-existing .lib/.exp file
!ifdef UFDLL
$(UFDLL): $*.obj $(UFEXTRA) $(UGOpenLibs) $(UGOpenInternalLibs)
	@echo....Creating $@
	$(link) -nologo $(ldebug) $(dlllflags) $(uflinkflags) -out:$*.dll $** $(conlibsdll)
!endif

!ifdef UFEXE
$(UFEXE): $*.obj $(UFEXTRA) $(UGOpenLibs)
	@echo....Creating $@
	$(link) -nologo $(ldebug) $(conlflags) $(uflinkflags) -out:$*.exe $** $(conlibsdll)
!endif

CFLAGS = -nologo $(cflags) $(cdebug) $(cvarsdll) -I. -I"$(UGII_USERFCN)" $(UFEXTRA) -MD

!ifdef UFOBJ
$(UFOBJ): $*.c
!endif

notarget:
	@echo Must specify a make target

setcl:
	@set CL=$(CFLAGS)
	@echo CL environment variable set to "%CL%"

echo:
!ifdef UFDLL
	@echo UFDLL = $(UFDLL)
!endif
!ifdef UFEXE
	@echo UFEXE = $(UFEXE)
!endif
!ifdef UFEXTRA
	@echo UFEXTRA = $(UFEXTRA)
!endif
!ifdef NODEBUG
	@echo Debug is disabled.
!else
	@echo Debug is enabled.
!endif
	@echo INCLUDE is $(INCLUDE)
	@echo LIB is $(LIB)

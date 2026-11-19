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

!IF !DEFINED(CPU) || "$(CPU)" == ""
CPU = $(PROCESSOR_ARCHITECTURE)
!ENDIF # CPU

# if PROCESSOR_ARCHITECTURE was x86 or X86 change CPU to i386

!IF ( "$(CPU)" == "X86" ) || ( "$(CPU)" == "x86" )
CPU = i386
!ENDIF # CPU == X86

!IF "$(CPU)" != "i386"
!IF "$(CPU)" != "IA64"
!IF "$(CPU)" != "AMD64"
!ERROR  Must specify CPU environment variable ( CPU=i386, CPU=IA64, CPU=AMD64)
!ENDIF
!ENDIF
!ENDIF

!IFNDEF APPVER
APPVER = 5.0
!ENDIF

!IF "$(APPVER)" =="6.1"
!IFNDEF _WIN32_IE
_WIN32_IE = 0x0800
!ENDIF # _WIN32_IE
!ENDIF # APPVER == 6.1

!IF "$(APPVER)" =="6.0"
!IFNDEF _WIN32_IE
_WIN32_IE = 0x0700
!ENDIF # _WIN32_IE
!ENDIF # APPVER == 6.0

!IF "$(APPVER)" =="5.0"
!IFNDEF _WIN32_IE
_WIN32_IE = 0x0500
!ENDIF # _WIN32_IE
!ENDIF # APPVER == 5.0

!IF "$(APPVER)" =="5.01"
!IFNDEF _WIN32_IE
_WIN32_IE = 0x0600
!ENDIF # _WIN32_IE
!ENDIF # APPVER == 5.01

!IF "$(APPVER)" =="5.02"
!IFNDEF _WIN32_IE
_WIN32_IE = 0x0600
!ENDIF # _WIN32_IE
!ENDIF # APPVER == 5.02

!IFNDEF _WIN32_IE
_WIN32_IE = 0x0400
!ENDIF

link   = link

ccommon = -c -DCRTAPI1=_cdecl -DCRTAPI2=_cdecl -nologo -GS

!IFDEF SEHMAP
ccommon = $(ccommon) -FIsehmap.h
!ENDIF

!IF "$(TARGETLANG)" == "LANG_JAPANESE"
ccommon = $(ccommon) -DJAPAN -DDBCS -DFE_IME
!ENDIF

!IF "$(TARGETLANG)" == "LANG_CHINESE"
ccommon = $(ccommon) -DDBCS -DFE_IME
!ENDIF

!IF "$(TARGETLANG)" == "LANG_KOREAN"
ccommon = $(ccommon) -DDBCS -DFE_IME
!ENDIF

!IF "$(CPU)" == "i386"
cflags = $(ccommon) -D_X86_=1  -DWIN32 -D_WIN32 -W3
scall  = -Gz

!ELSEIF "$(CPU)" == "AMD64"
cflags = $(ccommon) -D_AMD64_=1 -DWIN64 -D_WIN64  -DWIN32 -D_WIN32
cflags = $(cflags) -W4
scall  =

!ENDIF

#The next line is for NX11/VS2013 only.  Remove for NX12
cflags = $(cflags) /d1scalableinclude-

!IF "$(APPVER)" == "4.0"
NMAKE_WINVER = 0x0400
!ELSEIF "$(APPVER)" == "5.0"
NMAKE_WINVER = 0x0500
!ELSEIF "$(APPVER)" == "5.01"
NMAKE_WINVER = 0x0501
!ELSEIF "$(APPVER)" == "5.02"
NMAKE_WINVER = 0x0502
!ELSEIF "$(APPVER)" == "6.0"
NMAKE_WINVER = 0x0600
!ELSEIF "$(APPVER)" == "6.1"
NMAKE_WINVER = 0x0601
!ENDIF

!IF "$(TARGETOS)" == "WINNT"
cflags = $(cflags) -D_WINNT -D_WIN32_WINNT=$(NMAKE_WINVER) -DNTDDI_VERSION=$(NMAKE_WINVER)0000
!ENDIF

cflags = $(cflags) -D_WIN32_IE=$(_WIN32_IE) -DWINVER=$(NMAKE_WINVER)

!IFDEF NODEBUG
cdebug = -Ox -DNDEBUG 
!ELSE IFDEF PROFILE
cdebug = -Gh -Ox -DNDEBUG
!ELSE IFDEF TUNE
cdebug = -Gh -Ox -DNDEBUG
!ELSE
cdebug = -Zi -Od -DDEBUG
!ENDIF

!IFDEF NO_ANSI
noansi = -DNULL=0
!ENDIF

!IFDEF NODEBUG
cvarsmt    = $(noansi) -D_MT -MT
cvars      = $(cvarsmt)
cvarsdll   = $(noansi) -D_MT -D_DLL -MD
!ELSE
cvarsmt    = $(noansi) -D_MT -MTd
cvars      = $(cvarsmt)
cvarsdll   = $(noansi) -D_MT -D_DLL -MDd
!ENDIF

lflags  = $(lflags) /INCREMENTAL:NO /NOLOGO /LIBPATH:"$(UGII_USERFCN)"

!IF "$(CPU)" == "i386"

!IFDEF NODEBUG
ldebug = /RELEASE
!ELSE
ldebug = /DEBUG /DEBUGTYPE:cv
!ENDIF

!ELSE

!IFDEF NODEBUG
ldebug = /RELEASE
!ELSE IFDEF PROFILE
ldebug = /DEBUG:mapped,partial /DEBUGTYPE:coff
!ELSE IFDEF TUNE
ldebug = /DEBUG:mapped,partial /DEBUGTYPE:coff
!ELSE
ldebug = /DEBUG /DEBUGTYPE:cv
!ENDIF

!ENDIF

!IF ("$(APPVER)" == "5.0") && (("$(TARGETOS)" == "BOTH") || ("$(TARGETOS)" == "WIN95"))
EXEVER = 4.10
!ELSE
EXEVER = $(APPVER)
!ENDIF

conlflags = $(lflags) -subsystem:console,$(EXEVER)
dlllflags = $(lflags) -entry:_DllMainCRTStartup$(DLLENTRY) -dll

!IFDEF PROFILE
optlibs =  cap.lib
!ELSE IFDEF TUNE
optlibs = wst.lib
!ELSE
optlibs =
!ENDIF

winsocklibs = ws2_32.lib mswsock.lib
baselibs    = kernel32.lib $(optlibs) $(winsocklibs) advapi32.lib
conlibs     = $(baselibs)
conlibsdll  = $(conlibs)

!ifndef UGII_USERFCN
!error  UGII_USERFCN must be defined
!endif

UGOpenLibs         = libufun.lib libufun_cae.lib libufun_cam.lib libufun_die.lib libufun_vdac.lib libufun_weld.lib $(allNXOpenCppLibs) libopenpp.lib libvmathpp.lib
UGOpenInternalLibs = libugopenint.lib libugopenint_cae.lib libugopenint_cam.lib libnxopenuicpp.lib libopenintpp.lib

# this target is for creating a .dll without a pre-existing .lib/.exp file
!ifdef UFDLL
$(UFDLL): $*.obj $(UFEXTRA)
    @echo....Creating $@
    $(link) -nologo $(ldebug) $(dlllflags) $(uflinkflags) -out:$*.dll $** $(UGOpenLibs) $(UGOpenInternalLibs) $(conlibsdll)
!endif

!ifdef UFEXE
$(UFEXE): $*.obj $(UFEXTRA)
    @echo....Creating $@
    $(link) -nologo $(ldebug) $(conlflags) $(uflinkflags) -out:$*.exe $** $(UGOpenLibs) $(conlibsdll)
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

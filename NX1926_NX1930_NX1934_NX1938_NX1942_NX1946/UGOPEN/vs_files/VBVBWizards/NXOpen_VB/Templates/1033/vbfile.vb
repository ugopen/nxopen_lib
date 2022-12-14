
Option Strict Off
Imports System
Imports NXOpen
[!if CHECKBOX_NXOPEN_UF]
Imports NXOpen.UF
[!endif]

Module Module1

[!if MAIN_ENTRY_POINT || EXE_APPLICATION ]
    '  Explicit Activation
    '      This entry point is used to activate the application explicitly
    Sub Main()

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

    End Sub

[!endif]
[!if STARTUP_ENTRY_POINT && !EXE_APPLICATION]
    '  NX Startup
    '      This entry point activates the application at NX startup

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_STARTUP or USER_DEFAULT

    'OR

    'Will also work if dll is at folder named "startup" under any folder listed in the 
    'text file pointed to by the environment variable UGII_CUSTOM_DIRECTORY_FILE.

    Function Startup(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if USER_EXITS && !EXE_APPLICATION]
[!if UFGET_ENTRY_POINT]
    '  Open Part
    '      This user exit is invoked after the following menu item is activated:
    '      "File->Open"  

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_RETRIEVE or USER_DEFAULT

    Function ufget(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFCRE_ENTRY_POINT]
    '  New Part
    '      This user exit is invoked after the following menu item is activated:
    '      "File->New"  

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_CREATE or USER_DEFAULT

    Function ufcre(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFPUT_ENTRY_POINT]
    '  Save Part
    '      This user exit is invoked after the following menu item is activated:
    '      "File->Save"  

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_FILE or USER_DEFAULT

    Function ufput(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFSVAS_ENTRY_POINT]
    '  Save Part As
    '      This user exit is invoked after the following menu item is activated:
    '      "File->Save As..."

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_SAVEAS or USER_DEFAULT

    Function ufsvas(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFMRG_ENTRY_POINT]
    '  Import Part
    '      This user exit is invoked after the following menu item is activated:
    '      "File->Import->Part"

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_MERGE or USER_DEFAULT

    Function ufmrg(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFGRP_ENTRY_POINT]
    '  Execute GRIP Program
    '      This user exit is invoked after the following menu item is activated:
    '      "File->Execute->GRIP"

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_GRIP or USER_DEFAULT

    Function ufgrp(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFRCP_ENTRY_POINT]
    '  Add Existing Part
    '      This user exit is invoked after the "Assemblies->Edit Structure->
    '      Add Existing Part" menu item is activated and before the
    '      "Select Part" dialog. 

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_RCOMP or USER_DEFAULT

    Function ufrcp(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFFCP_ENTRY_POINT]
    '  Export Part
    '      This user exit is invoked after the "File->Export->Part" menu item is
    '      activated and before the "Select Part" dialog. 

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_FCOMP or USER_DEFAULT

    Function uffcp(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFUSD_ENTRY_POINT]
    '  Component Where-Used
    '      This user exit is invoked after the "Assemblies->Reports->Where Used"
    '      menu item is activated and before the "Select Components" dialog.

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_WHERE_USED or USER_DEFAULT

    Function ufusd(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFPLT_ENTRY_POINT]
    '  Plot File
    '      This user exit is invoked after the following menu item is activated:
    '      "File->Plot..."

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_PLOT or USER_DEFAULT

    Function ufplt(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UF2DA_ENTRY_POINT]
    '  2D Analysis Using Curves
    '      This user exit is invoked after the following menu item is activated:
    '      "Info->Analysis...->AreaProperties - Using Curves" 

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_AREAPROPCRV or USER_DEFAULT

    Function uf2da(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFUDS_ENTRY_POINT]
    '  User Defined Symbols
    '      This user exit is invoked after the following menu item is activated:
    '      "Application->Drafting->Create->User Defined Symbols"

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_UDSYMBOL or USER_DEFAULT

    Function ufuds(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFCLSO_ENTRY_POINT]
    '  Open CLSF
    '      This user exit is invoked after the following menu item is activated:
    '      "Application->Manufacturing..." 

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_CLS_OPEN or USER_DEFAULT

    Function ufclso(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFCLSS_ENTRY_POINT]
    '  Save CLSF
    '      This user exit is invoked after any of the following actions:
    '      "File->Save->CLSF"
    '      "File->Save->CLSF As"
    '      "Preferences->Autofile CLSF"
    '      "Toolbox->Operation->Generate->OK"  

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_CLS_SAVE or USER_DEFAULT

    Function ufclss(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFCLSR_ENTRY_POINT]
    '  Rename CLSF
    '      This user exit is invoked after the following menu item is activated:
    '      "Application->Manufacturing->File->Save->CLSF As"

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_CLS_RENAME or USER_DEFAULT

    Function ufclsr(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFCLG_ENTRY_POINT]
    '  Generate CLF
    '      This user exit is invoked after the following menu item is activated:
    '      "Application->Manufacturing->Toolbox->Tool Path...->Postprocess->
    '      Generate CLF"  

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_CL_GEN or USER_DEFAULT

    Function ufclg(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFPOST_ENTRY_POINT]
    '  Postprocess CLSF
    '      This user exit is invoked after the following menu item is activated:
    '      "Application->Manufacturing->Toolbox->Tool Path...->Postprocess->
    '      Postprocess" 

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_POST or USER_DEFAULT

    Function ufpost(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFCCP_ENTRY_POINT]
    '  Create Component
    '      This user exit is invoked after the "Assemblies->Edit Structure->
    '      Create New Component->Add Object Methods" menu item is activated and
    '      before the "Select Part" dialog.

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_CCOMP or USER_DEFAULT

    Function ufccp(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFCDP_ENTRY_POINT]
    '  Change Displayed Part
    '      This user exit is invoked after the "File->Change->Displayed Part"
    '      menu item is activated and before the "Select Part" dialog.  

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_CDISP or USER_DEFAULT

    Function ufcdp(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFCWP_ENTRY_POINT]
    '  Change Work Part
    '      This user exit is invoked after the "Assemblies->Change Work Part..."
    '      menu item is activated and before the "Select Part" dialog.  

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_CWORK or USER_DEFAULT

    Function ufcwp(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFDCP_ENTRY_POINT]
    '  Remove Component
    '      This user exit is invoked after the "Assemblies->Edit Structure->
    '      Remove Component" menu item is activated and before the
    '      "Select Components" dialog.  

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_DCOMP or USER_DEFAULT

    Function ufdcp(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFMCP_ENTRY_POINT]
    '  Reposition Component
    '      This user exit is invoked after the "Assemblies->Edit Structure->
    '      Reposition Component" menu item is activated and before the
    '      "Select Components" dialog.  

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_MCOMP or USER_DEFAULT

    Function ufmcp(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFSCPO_ENTRY_POINT]
    '  Substitute Component Out
    '      This user exit is invoked after the "Assemblies->Edit Structure->
    '      Substitute Component" menu item is activated and before the
    '      "Select Components" dialog.

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_SCOMP1 or USER_DEFAULT

    Function ufscpo(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFSCPI_ENTRY_POINT]
    '  Substitute Component In
    '      This user exit is invoked after the "Assemblies->Edit Structure->
    '      Substitute Component->Choose" menu item is activated and before the
    '      "Select Components" dialog.  

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_SCOMP2 or USER_DEFAULT

    Function ufscpi(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFRRS_ENTRY_POINT]
    '  Replace Reference Set
    '      This user exit is invoked after the "Assemblies->Edit Structure->
    '      Replace Reference Set" menu item is activated and before the
    '      "Select Components" dialog. 

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_RRSET or USER_DEFAULT

    Function ufrrs(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFNCP_ENTRY_POINT]
    '  Rename Component
    '      This user exit is invoked after the "Assemblies->Edit Structure->
    '      Rename Component" menu item is activated and before the
    '      "Select Components" dialog.  

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_NCOMP or USER_DEFAULT

    Function ufncp(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFGEN_ENTRY_POINT]
    '  Access Genius Library Management System
    '      This user exit is invoked after the "Genius" push button is activated
    '      when creating or editing a tool in CAM.  

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_GENIUS or USER_DEFAULT

    Function ufgen(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFGENS_ENTRY_POINT]
    '  Access Genius Library Management System

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_GENIUS_ST or USER_DEFAULT

    Function ufgens(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFGRPD_ENTRY_POINT]
    '  Execute Debug GRIP
    '      This user exit is invoked after the following menu item is activated:
    '      "File->Execute->Debug GRIP" 

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_GRIPDEBUG or USER_DEFAULT

    Function ufgrpd(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFUFUN_ENTRY_POINT]
    '  Execute NX Open API
    '      This user exit is invoked after the following menu item is activated:
    '      "File->Execute-> NX Open"  

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_UFUN or USER_DEFAULT

    Function ufufun(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFSPOP_ENTRY_POINT]
    '  Open Spreadsheet
    '      This user exit is invoked after a spreadsheet executable is started
    '      and before any spreadsheets are loaded. Interactively, this occurs
    '      after the "Toolbox->Spreadsheet" menu item is activated.  

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_SPRD_OPN or USER_DEFAULT

    Function ufspop(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFSPCL_ENTRY_POINT]
    '  Close Spreadsheet
    '      This user exit is invoked when a spreadsheet is closed. Interactively,
    '      this occurs when either of the following menu items is selected from
    '      the spreadsheet menu bar:
    '      "File->Exit"
    '      "Connect->Disconnect"  

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_SPRD_CLO or USER_DEFAULT

    Function ufspcl(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFSPUP_ENTRY_POINT]
    '  Update Spreadsheet
    '      This user exit is invoked at the start of expression update.
    '      Interactively, this occurs after the "Tools->Update NX Part" menu item
    '      is activated.  

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_SPRD_UPD or USER_DEFAULT

    Function ufspup(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFSPUF_ENTRY_POINT]
    '  Finish Updating Spreadsheet
    '      This user exit is invoked at the completion of expression update. 

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_SPRD_UPF or USER_DEFAULT

    Function ufspuf(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UDOP_ENTRY_POINT]
    '  CAM User Defined Operation
    '      This user exit is invoked when a CAM User Defined Operation is created
    '      or edited.  

    Function udop(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if DPUD_ENTRY_POINT]
    '  CAM User Defined Drive Path
    '      This user exit is invoked when a CAM User Defined Drive Path is created
    '      or edited.  
    Function dpud(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFNOPR_ENTRY_POINT]
    '  CAM New Operation
    '      This user exit is invoked after a CAM operation is created or
    '      reinitialized via the following menu item:
    '      "Application->Manufacturing..."  

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_CREATE_OPER or USER_DEFAULT

    Function ufnopr(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!if UFCAMS_ENTRY_POINT]
    '  CAM Startup
    '      This user exit is invoked after the following menu item is activated:
    '      "Application->Manufacturing..."  

    'Will work when complete path of the dll is provided to Environment Variable 
    'USER_CAM_STARTUP or USER_DEFAULT

    Function ufcams(ByVal args As String()) As Integer

        Dim theSession As Session = Session.GetSession()
[!if CHECKBOX_NXOPEN_UI]
        Dim theUI As UI = UI.GetUI()
[!endif]
[!if CHECKBOX_NXOPEN_UF]
        Dim theUfSession As UFSession = UFSession.GetUFSession()
[!endif]

        ' TODO: Add your application code here 

        Return 0

    End Function

[!endif]
[!endif]
[!if UNLOAD_IMMEDIATELY && !EXE_APPLICATION]

    Public Function GetUnloadOption(ByVal dummy As String) As Integer

        'Unloads the image immediately after execution within NX
        GetUnloadOption = NXOpen.Session.LibraryUnloadOption.Immediately

        '----Other unload options-------
        'Unloads the image when the NX session terminates
        'GetUnloadOption = NXOpen.Session.LibraryUnloadOption.AtTermination

        'Unloads the image explicitly, via an unload dialog
        'GetUnloadOption = NXOpen.Session.LibraryUnloadOption.Explicitly
        '-------------------------------

    End Function
[!endif]
[!if UNLOAD_UG_TERMINATE && !EXE_APPLICATION]

    Public Function GetUnloadOption(ByVal dummy As String) As Integer

        'Unloads the image when the NX session terminates
        GetUnloadOption = NXOpen.Session.LibraryUnloadOption.AtTermination

        '----Other unload options-------
        'Unloads the image immediately after execution within NX
        'GetUnloadOption = NXOpen.Session.LibraryUnloadOption.Immediately

        'Unloads the image explicitly, via an unload dialog
        'GetUnloadOption = NXOpen.Session.LibraryUnloadOption.Explicitly
        '-------------------------------

    End Function
[!endif]
[!if UNLOAD_SEL_DIALOG && !EXE_APPLICATION]

    Public Function GetUnloadOption(ByVal dummy As String) As Integer

        'Unloads the image explicitly, via an unload dialog
        GetUnloadOption = NXOpen.Session.LibraryUnloadOption.Explicitly

        '----Other unload options-------
        'Unloads the image when the NX session terminates
        'GetUnloadOption = NXOpen.Session.LibraryUnloadOption.AtTermination

        'Unloads the image immediately after execution within NX
        'GetUnloadOption = NXOpen.Session.LibraryUnloadOption.Immediately
        '-------------------------------

    End Function
[!endif]

End Module


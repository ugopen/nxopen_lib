using System;
using NXOpen;
[!if CHECKBOX_NXOPEN_UF]
using NXOpen.UF;
[!endif]

public class Program
{
    // class members
    private static Session theSession;
    [!if CHECKBOX_NXOPEN_UI]
    private static UI theUI;
    [!endif]
    [!if CHECKBOX_NXOPEN_UF]
    private static UFSession theUfSession ;
    [!endif]
    public static Program theProgram;
    public static bool isDisposeCalled;

    //------------------------------------------------------------------------------
    // Constructor
    //------------------------------------------------------------------------------
    public Program()
    {
        try
        {
            theSession = Session.GetSession();
            [!if CHECKBOX_NXOPEN_UI]
            theUI = UI.GetUI();
            [!endif]
            [!if CHECKBOX_NXOPEN_UF]
            theUfSession = UFSession.GetUFSession();
            [!endif]
            isDisposeCalled = false;
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            // UI.GetUI().NXMessageBox.Show("Message", NXMessageBox.DialogType.Error, ex.Message);
        }
    }

[!if MAIN_ENTRY_POINT || EXE_APPLICATION ]
    //------------------------------------------------------------------------------
    //  Explicit Activation
    //      This entry point is used to activate the application explicitly
    //------------------------------------------------------------------------------
    public static int Main(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if STARTUP_ENTRY_POINT && !EXE_APPLICATION]
    //------------------------------------------------------------------------------
    //  NX Startup
    //      This entry point activates the application at NX startup

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_STARTUP or USER_DEFAULT

    //OR

    //Will also work if dll is at folder named "startup" under any folder listed in the 
    //text file pointed to by the environment variable UGII_CUSTOM_DIRECTORY_FILE.
    //------------------------------------------------------------------------------
    public static int Startup()
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();
            
            //TODO: Add your application code here 
           
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            // theUI.NXMessageBox.Show("UI Styler", NXMessageBox.DialogType.Error, ex.Message);
        }
        return retValue;
    }

[!endif]
[!if USER_EXITS && !EXE_APPLICATION]
[!if UFGET_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Open Part
    //      This user exit is invoked after the following menu item is activated:
    //      "File->Open"  

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_RETRIEVE or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufget(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }
    
[!endif]
[!if UFCRE_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  New Part
    //      This user exit is invoked after the following menu item is activated:
    //      "File->New"  

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_CREATE or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufcre(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }
    
[!endif]
[!if UFPUT_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Save Part
    //      This user exit is invoked after the following menu item is activated:
    //      "File->Save"  

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_FILE or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufput(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFSVAS_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Save Part As
    //      This user exit is invoked after the following menu item is activated:
    //      "File->Save As..."

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_SAVEAS or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufsvas(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFMRG_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Import Part
    //      This user exit is invoked after the following menu item is activated:
    //      "File->Import->Part"

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_MERGE or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufmrg(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFGRP_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Execute GRIP Program
    //      This user exit is invoked after the following menu item is activated:
    //      "File->Execute->GRIP"

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_GRIP or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufgrp(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFRCP_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Add Existing Part
    //      This user exit is invoked after the "Assemblies->Edit Structure->
    //      Add Existing Part" menu item is activated and before the
    //      "Select Part" dialog. 

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_RCOMP or USER_DEFAULT
    //------------------------------------------------------------------------------    
    public static int ufrcp(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFFCP_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Export Part
    //      This user exit is invoked after the "File->Export->Part" menu item is
    //      activated and before the "Select Part" dialog. 

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_FCOMP or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int uffcp(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFUSD_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Component Where-Used
    //      This user exit is invoked after the "Assemblies->Reports->Where Used"
    //      menu item is activated and before the "Select Components" dialog.

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_WHERE_USED or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufusd(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFPLT_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Plot File
    //      This user exit is invoked after the following menu item is activated:
    //      "File->Plot..."

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_PLOT or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufplt(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UF2DA_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  2D Analysis Using Curves
    //      This user exit is invoked after the following menu item is activated:
    //      "Info->Analysis...->AreaProperties - Using Curves" 

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_AREAPROPCRV or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int uf2da(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFUDS_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  User Defined Symbols
    //      This user exit is invoked after the following menu item is activated:
    //      "Application->Drafting->Create->User Defined Symbols"

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_UDSYMBOL or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufuds(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFCLSO_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Open CLSF
    //      This user exit is invoked after the following menu item is activated:
    //      "Application->Manufacturing..." 

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_CLS_OPEN or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufclso(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFCLSS_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Save CLSF
    //      This user exit is invoked after any of the following actions:
    //      "File->Save->CLSF"
    //      "File->Save->CLSF As"
    //      "Preferences->Autofile CLSF"
    //      "Toolbox->Operation->Generate->OK"  

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_CLS_SAVE or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufclss(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFCLSR_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Rename CLSF
    //      This user exit is invoked after the following menu item is activated:
    //      "Application->Manufacturing->File->Save->CLSF As"

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_CLS_RENAME or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufclsr(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFCLG_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Generate CLF
    //      This user exit is invoked after the following menu item is activated:
    //      "Application->Manufacturing->Toolbox->Tool Path...->Postprocess->
    //      Generate CLF"  

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_CL_GEN or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufclg(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFPOST_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Postprocess CLSF
    //      This user exit is invoked after the following menu item is activated:
    //      "Application->Manufacturing->Toolbox->Tool Path...->Postprocess->
    //      Postprocess" 

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_POST or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufpost(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFCCP_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Create Component
    //      This user exit is invoked after the "Assemblies->Edit Structure->
    //      Create New Component->Add Object Methods" menu item is activated and
    //      before the "Select Part" dialog.

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_CCOMP or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufccp(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFCDP_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Change Displayed Part
    //      This user exit is invoked after the "File->Change->Displayed Part"
    //      menu item is activated and before the "Select Part" dialog.  

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_CDISP or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufcdp(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFCWP_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Change Work Part
    //      This user exit is invoked after the "Assemblies->Change Work Part..."
    //      menu item is activated and before the "Select Part" dialog.  

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_CWORK or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufcwp(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFDCP_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Remove Component
    //      This user exit is invoked after the "Assemblies->Edit Structure->
    //      Remove Component" menu item is activated and before the
    //      "Select Components" dialog.  

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_DCOMP or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufdcp(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFMCP_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Reposition Component
    //      This user exit is invoked after the "Assemblies->Edit Structure->
    //      Reposition Component" menu item is activated and before the
    //      "Select Components" dialog.  

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_MCOMP or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufmcp(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFSCPO_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Substitute Component Out
    //      This user exit is invoked after the "Assemblies->Edit Structure->
    //      Substitute Component" menu item is activated and before the
    //      "Select Components" dialog.

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_SCOMP1 or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufscpo(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFSCPI_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Substitute Component In
    //      This user exit is invoked after the "Assemblies->Edit Structure->
    //      Substitute Component->Choose" menu item is activated and before the
    //      "Select Components" dialog.  

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_SCOMP2 or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufscpi(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFRRS_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Replace Reference Set
    //      This user exit is invoked after the "Assemblies->Edit Structure->
    //      Replace Reference Set" menu item is activated and before the
    //      "Select Components" dialog. 

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_RRSET or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufrrs(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFNCP_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Rename Component
    //      This user exit is invoked after the "Assemblies->Edit Structure->
    //      Rename Component" menu item is activated and before the
    //      "Select Components" dialog.  

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_NCOMP or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufncp(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFGEN_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Access Genius Library Management System
    //      This user exit is invoked after the "Genius" push button is activated
    //      when creating or editing a tool in CAM.  

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_GENIUS or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufgen(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFGRPD_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Execute Debug GRIP
    //      This user exit is invoked after the following menu item is activated:
    //      "File->Execute->Debug GRIP" 

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_GRIPDEBUG or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufgrpd(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFUFUN_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Execute NX Open API
    //      This user exit is invoked after the following menu item is activated:
    //      "File->Execute-> NX Open"  

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_UFUN or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufufun(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFSPOP_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Open Spreadsheet
    //      This user exit is invoked after a spreadsheet executable is started
    //      and before any spreadsheets are loaded. Interactively, this occurs
    //      after the "Toolbox->Spreadsheet" menu item is activated.  

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_SPRD_OPN or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufspop(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFSPCL_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Close Spreadsheet
    //      This user exit is invoked when a spreadsheet is closed. Interactively,
    //      this occurs when either of the following menu items is selected from
    //      the spreadsheet menu bar:
    //      "File->Exit"
    //      "Connect->Disconnect"  

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_SPRD_CLO or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufspcl(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFSPUP_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Update Spreadsheet
    //      This user exit is invoked at the start of expression update.
    //      Interactively, this occurs after the "Tools->Update NX Part" menu item
    //      is activated.  

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_SPRD_UPD or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufspup(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFSPUF_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  Finish Updating Spreadsheet
    //      This user exit is invoked at the completion of expression update. 

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_SPRD_UPF or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufspuf(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UDOP_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  CAM User Defined Operation
    //      This user exit is invoked when a CAM User Defined Operation is created
    //      or edited. 
    //------------------------------------------------------------------------------ 
    public static int udop(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if DPUD_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  CAM User Defined Drive Path
    //      This user exit is invoked when a CAM User Defined Drive Path is created
    //      or edited.
    //------------------------------------------------------------------------------  
    public static int dpud(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFNOPR_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  CAM New Operation
    //      This user exit is invoked after a CAM operation is created or
    //      reinitialized via the following menu item:
    //      "Application->Manufacturing..."  

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_CREATE_OPER or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufnopr(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFCAMS_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  CAM Startup
    //      This user exit is invoked after the following menu item is activated:
    //      "Application->Manufacturing..."  

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_CAM_STARTUP or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufcams(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!if UFGENS_ENTRY_POINT]
    //------------------------------------------------------------------------------
    //  UFGENS Startup

    //Will work when complete path of the dll is provided to Environment Variable 
    //USER_GENIUS_ST or USER_DEFAULT
    //------------------------------------------------------------------------------
    public static int ufgens(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
        
            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
        return retValue;
    }

[!endif]
[!endif]
    //------------------------------------------------------------------------------
    // Following method disposes all the class members
    //------------------------------------------------------------------------------
    public void Dispose()
    {
        try
        {
            if (isDisposeCalled == false)
            {
                //TODO: Add your application code here 
            }
            isDisposeCalled = true;
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            
        }
    }

[!if !EXE_APPLICATION]
    public static int GetUnloadOption(string arg)
    {
        [!if UNLOAD_IMMEDIATELY]
        //Unloads the image explicitly, via an unload dialog
        //return System.Convert.ToInt32(Session.LibraryUnloadOption.Explicitly);
        
        //Unloads the image immediately after execution within NX
         return System.Convert.ToInt32(Session.LibraryUnloadOption.Immediately);

        //Unloads the image when the NX session terminates
        // return System.Convert.ToInt32(Session.LibraryUnloadOption.AtTermination);
        [!endif]
        [!if UNLOAD_UG_TERMINATE]
        //Unloads the image explicitly, via an unload dialog
        //return System.Convert.ToInt32(Session.LibraryUnloadOption.Explicitly);
        
        //Unloads the image immediately after execution within NX
        // return System.Convert.ToInt32(Session.LibraryUnloadOption.Immediately);

        //Unloads the image when the NX session terminates
         return System.Convert.ToInt32(Session.LibraryUnloadOption.AtTermination);
        [!endif]
        [!if UNLOAD_SEL_DIALOG]
        //Unloads the image explicitly, via an unload dialog
        return System.Convert.ToInt32(Session.LibraryUnloadOption.Explicitly);
        
        //Unloads the image immediately after execution within NX
        // return System.Convert.ToInt32(Session.LibraryUnloadOption.Immediately);

        //Unloads the image when the NX session terminates
         //return System.Convert.ToInt32(Session.LibraryUnloadOption.AtTermination);
        [!endif]
    }

[!endif]  
}


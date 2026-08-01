/****************************************************************************

          Copyright (c) 1998,2000  Unigraphics Solutions Corporation
                          Unpublished - All rights reserved

 *

File Description:

This file describes:

.    what user exits are and how to use them
.    the environment variable you must define
.    entry point subroutine names; you must code a Fortran
     subroutine or C function (without a main())
.    special C considerations
.    the return codes for each exit


*/

/*

For all user exits the following applies:
If the operation is "object-action", i.e. the object being operated on is selected before 
the function is chosen then any part name supplied by the user exit will not be used.

The following environment variables are used to point to user exit executables.

    User Exit                   Environment Variable        Entry Point

    Open Part                   USER_RETRIEVE               ufget

    New Part                    USER_CREATE                 ufcre

    Save Part                   USER_FILE                   ufput

    Save Part As                USER_SAVEAS                 ufsvas

    Import Part                 USER_MERGE                  ufmrg

    Execute GRIP Program        USER_GRIP                   ufgrp

    Add Existing Part           USER_RCOMP                  ufrcp

    Export Part                 USER_FCOMP                  uffcp

    Component Where-used        USER_WHERE_USED             ufusd

    Plot File                   USER_PLOT                   ufplt

    2D Analysis Using Curves    USER_AREAPROPCRV            uf2da

    User Defined Symbols        USER_UDSYMBOL               ufuds

    Open CLSF                   USER_CLS_OPEN               ufclso

    Save CLSF                   USER_CLS_SAVE               ufclss

    Rename CLSF                 USER_CLS_RENAME             ufclsr

    Generate CLF                USER_CL_GEN                 ufclg

    Postprocess CLSF            USER_POST                   ufpost

    Create Component            USER_CCOMP                  ufccp

    Change Displayed Part       USER_CDISP                  ufcdp

    Change Work Part            USER_CWORK                  ufcwp

    Remove Component            USER_DCOMP                  ufdcp

    Reposition Component        USER_MCOMP                  ufmcp

    Substitute Component Out    USER_SCOMP1                 ufscpo

    Substitute Component In     USER_SCOMP2                 ufscpi

    Open Spreadsheet            USER_SPRD_OPN               ufspop

    Close Spreadsheet           USER_SPRD_CLO               ufspcl

    Update Spreadsheet          USER_SPRD_UPD               ufspup

    Finish Updating Spreadsheet USER_SPRD_UPF               ufspuf

    Replace Reference Set       USER_RRSET                  ufrrs

    Rename Component            USER_NCOMP                  ufncp

    NX Startup                  USER_STARTUP                ufsta

    Access Genius Library Management System 
                                USER_GENIUS                 ufgen

    Execute Debug GRIP          USER_GRIPDEBUG              ufgrpd

    Execute User Function       USER_UFUNC                  ufufun

    Initialize new operation    USER_CREATE_OPER            ufnopr
    Re-initialize an existing 
    operation

    CAM Startup                 USER_CAM_STARTUP            ufcams
*****************************************************************************/

#ifndef UF_EXIT_INCLUDED
#define UF_EXIT_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>


#ifdef __cplusplus
extern "C" {
#endif


/*
    Open Part

    The open part (retrieve) user exit is invoked after the File->Open menu.

    If no User Function program error is returned and an active part exists,
    control  is returned to the current module.

    If no active part exists, the next interactive step is determined by the
    return  code as follows:

    Return :
    Return Code/Description 

    1   Gateway menu

    2   Choose part name file selection dialog with the string (from param)
        as the  default.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufget(char *param, int *retcode, int rlen);

/*
    New Part

    The new part user exit is invoked after the File->New menu.

    If no User Function program error is returned and an active part exists,
    control  is returned to the current module.

    If no active part exists, the next interactive step is determined by the
    return  code as follows:

    Return :
    Return Code/Description

    1   Gateway menu

    2   Choose part name file selection dialog with the string (from param)
        as the  default.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufcre(char *param, int *retcode, int rlen);

/*
    Save Part

    The save part user exit occurs after the File->Save menu.

    If no User Function program error occurs and an active part exists, the
    next  interactive step is to continue with the last main menu (Gateway
    menu).

    Return :
    Return Code/Description

    0   NX should go ahead and file the part
    1   Gateway menu, user exit filed the part

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufput(char *param, int *retcode, int rlen);

/*
    Save Part As

    The save part user exit occurs after the File->Save As... menu.
    
    When the mode is Design in Context and the work part to save is not
    the displayed part, then for each level of the assembly that contains
    the work part, the full file specification of the current part name is
    passed as the string parameter (param) to the user exit. This enables
    you to identify which part is to be "saved as"


    If no User Function program error occurs and an active part exists, the
    next  interactive step is is determined by the return code as follows:

    Return :
    Return Code/Description

    1   Gateway menu. Control passes back to the Gateway menu after  going
        through the warnings and clean up routines of the normal NX dialogs
         if required.

    2   Choose part name file selection dialog with the string (from param)
        as the  default. For Design in Context, control passes to the normal
        NX dialogs for each level of the assembly above the work part
        (occurrence in an assembly tree) but with a default string for the
        new part name as specified by the string from param.

    n   File->Save As dialog with no default string. n not equal to 1 or 2.
        For Design in Context, control passes to the normal NX dialogs
        for each level of the assembly above the work part  (occurrence
        in an assembly tree).

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufsvas(char *param, int *retcode, int rlen);

/*
    Import Part

    The import (merge) part user exit occurs after the File->Import->Part
    menu.

    If an active part exists, the next interactive step is determined by the
    return  code as follows:

    Return :
    Return Code/Description

    0   Import Part dialog

    2   Import Part dialog with the string (from param) as the default filename
        This filename will be used when the file selection box is brought up
        after leaving the Import Part dialog.

    Environment : Internal
    See Also :
    History : 
 */

extern DllExport void ufmrg(char *param, int *retcode, int rlen);

/*
    Execute GRIP

    The execute GRIP user exit occurs after the File->Execute->GRIP menu.

    The next interactive step is determined by the return code as follows:

    Return :
    Return Code/Description

    1   Runs the GRIP program using the string passed from param. The Motif
        file dialog  is not displayed

    2   Disables the Execute GRIP option. The system adminstrator has the
        option of  making this option (and the use of a GRIP license)
        unavailable.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufgrp(char *param, int *retcode, int rlen);

/*
    Add Existing Part

    The add existing part (retrieve component) user exit occurs after the 
    Assemblies->Components->Add Existing menu and before the select part dialog.

    The next interactive step is determined by the return code as follows:

    Return :
    Return Code/Description

    1   Cancel current assembly operation

    2   Select Part dialog with the string (from param) as the default provided the 
        part exists so that it can be loaded.

    3   Component Parameters dialog with the part (from param) as the part to be added 
        provided the part exists so it can be loaded.

    n   Normal operation with no default strings.  "n" is any other return
        code except  1, 2 or 3.


    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufrcp(char *param, int *retcode, int rlen);

/*
    Export Part

    The export part user exit occurs after the File->Export->Part menu.

    The next interactive step is determined by the return code as follows:

    Return :
    Return Code/Description

    1   Cancel current assembly operation

    2   If the user opts to specify part from the Export Part menu, the value returned
        in param will be used for the default part name.

    3   Reserved for future use

    n   Normal operation with no default strings.  "n" is any other return
        code except  1, 2 or 3.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void uffcp(char *param, int *retcode, int rlen);

/*
    Component Where-Used

    The component where-used user exit occurs after the
    Assemblies->Reports->Where  Used menu and before the select components
    dialog.

    If no User Function program error is returned and no active part exists,
    the  file menu displays.

    If an active part exists, the next interactive step is determined by the
    return  code as follows:

    Return :
    Return Code/Description

    1   Assemblies->Reports->Where Used dialog with displayed part name as
        default.

    2   Assemblies->Reports->Where Used dialog with the string (from param)
        as the default  component name.

    3   Assemblies->Reports->Where Used dialog with the string (from param)
        as the default  directory path name.

    n   Assemblies->Reports->Where Used dialog with no default string. "n"
        is any other  code exept 1, 2, or 3.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufusd(char *param, int *retcode, int rlen);

/*
    Plot File

    The plot file user exit occurs at File->Plot... menu. There is no input
    or output  exit string.

    If an active part exists, the next interactive step is determined by the
    return  code as follows:

    Return :
    Return Code/Description

    1   Gateway menu

    n   Plot dialog. "n" is any other code except 1.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufplt(char *param, int *retcode, int rlen);

/*
    2D Analysis Using Curves

    The 2D analysis using curve user exit occurs after the
    Info->Analysis...->Area  Properties - Using Curves menu. This user exit
    bypasses the curve analysis  routine and substitutes your user exit
    program. There are no return codes associated  with this exit.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void uf2da(char *param, int *retcode, int rlen);

/*
    User Defined Symbols

    The user defined symbols user exit occurs after the
    Application->Drafting->Create->User  Defined Symbols menu. There are no
    return codes for this option. If the user  exit exists, your routine
    executes and then the User Defined Symbol dialog  displays. if the user
    exit does not exist, the User Defined Symbol dialog displays.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufuds(char *param, int *retcode, int rlen);

/*
    CLSF Open

    The CLSF open user exit occurs after the Application->Manufacturing...
    menu. 


    If an active part exists, the next interactive step is determined by the
    return  code as follows:

    Return :
    Return Code/Description

    0   No CLSF returned

    1   CLSF returned, awaiting acceptance

    2   CLSF returned and accepted. Select File dialog with the string (from
        param)  as the default.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufclso(char *param, int *retcode, int rlen);

/*
    CLSF Save

    The CLSF save exit is activated by any of the following actions:

    1.  File->Save->CLSF

    2.  File->Save->CLSF As You use this exit in succession with the
    USER_CLS_RENAME exit.

    3.  Tool Path Acceptance: Preferences->Autofile CLSF
    Toolbox->Operation->Generate->OK

    You can pass the CLSF name through the param argument.

    If no User Function program error is returned and no active part exists,
    the  File Main menu displays.

    If an active part exists, the next interactive step is determined by the
    return  code as follows:

    Return :
    Return Code/Description

   -1   User Exit Error

    0   User Exit does not exist.

    1   Successful User Exit execution


    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufclss(char *param, int *retcode, int rlen);

/*
    CLSF Rename

    The CLSF rename exit occurs after
    Application->Manufacturing->File->Save->CLSF  As. Selecting this option
    executes both the USER_CLS_RENAME and USER_CLS_SAVE  exits in
    succession.

    You can pass the CLSF name through the param argument.

    If no User Function program error is returned and no active part exists,
    the  File Main menu displays.

    If an active part exists, the next interactive step is determined by the
    return  code as follows:

    Return :
    Return Code/Description

   -1   User Exit Error

    0   User Exit does not exist.

    1   Successful User Exit execution

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufclsr(char *param, int *retcode, int rlen);

/*
    CLF Generate

    The CLF Generate exit occurs after Application->Manufacturing->Toolbox-> 
    Tool Path...->Postprocess->Generate CLF. Selecting  this option executes
    the USER_CL_GEN (CLF generation) exit.

    You can pass the CLF name through the param argument.

    If no User Function program error is returned and no active part exists,
    the  File Main menu displays.

    If an active part exists, the next interactive step is determined by the
    return  code as follows:

    Return :
    Return Code/Description

   -1   User Exit Error

    0   User Exit does not exist.

    1   Successful User Exit execution

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufclg(char *param, int *retcode, int rlen);

/*
    CLSF Postprocess
    The CLSF postprocess exit occurs after
    Application->Manufacturing->Toolbox->   Tool
    Path...->Postprocess->Postprocess.  Selecting this option executes both
    the USER_CL_GEN (CLF generation)  and USER_POST  (CLSF postprocessing)
    exits in succession.

    You can pass the CLSF name through the param argument.

    If no User Function program error is returned and no active part exists,
    the  File Main menu displays.

    If an active part exists, the next interactive step is determined by the
    return  code as follows:

    Return :
    Return Code/Description

   -1   User Exit Error

    0   User Exit does not exist.

    1   Successful User Exit execution

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufpost(char *param, int *retcode, int rlen);

/*
    Access Genius System

    This exit accesses the Genius Library Management System. Genius is an
    external product used by the Manufacturing Module for Tool Data
    Management. The  Genius exit occurs after 
    Application->Manufacturing->Toolbox->Tool->Genius.  There  are no return
    codes associated with this exit.

    This is a legacy application that is no longer supported.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufgen(char *param, int *retcode, int rlen);

/*
    Create Component

    The create component user exit occurs after the 
    Assemblies->Components->Create  New Component->Add Object Methods menu 
    and before the select part dialog.

    The next interactive step is determined by the return  code as follows:

    Return :
    Return Code/Description

    1   Cancel current assembly operation

    2   Select Part dialog with the string (from param) as the default.
        Note: The full pathname must be specified in the param argument 
        in order for this to work.

    3   Reserved for future use

    n   Select Part dialog with no default string. "n" is any other return
        code except  1, 2 or 3.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufccp(char *param, int *retcode, int rlen);

/*
    Change Displayed Part

    The change displayed part user exit occurs before the displayed part is about to 
    be changed explicitly from any user interface entry point, e.g. from the Windows main menu.

    It is not possible to provide a default name for the operation.

    The next interactive step is determined by the return code as follows:


    Return :
    Return Code/Description

    1   Cancel current assembly operation

    3   Reserved for future use

    n   Select Part dialog with no default string. "n" is any other return
        code except  1 or 3.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufcdp(char *param, int *retcode, int rlen);

/*
    Change Work Part

    The change work part user exit occurs after the Assemblies->Context Control->Set Work Part 
    before a Component is chosen or when the work part is about to be changed from any other 
    explicit user interface entry point

    The next interactive step is determined by the return code as follows:

    Return :
    Return Code/Description

    1   Cancel current assembly operation

    2   Select Component dialog with the string (from param) as the default.

    3   Reserved for future use

    n   Normal operation with no default strings.  "n" is any other return
        code except  1, 2 or 3.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufcwp(char *param, int *retcode, int rlen);

/*
    Remove Component

    The remove component user exit occurs after Edit->Delete after a component 
    has been selected.
    It is not called after a Cut operation.

    It is not possible to provide a default name for the operation.
 
    The next interactive step is determined by the return code as follows:

    Return :
    Return Code/Description

    1   Cancel current assembly operation

    3   Reserved for future use

    n   Normal operation with no default strings.  "n" is any other return
        code except  1 or 3.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufdcp(char *param, int *retcode, int rlen);

/*
    Reposition Component

    The reposition component user exit occurs after the Assemblies->Components->Reposition Component 
    menu and after the component has been selected or when a component is about to be 
    repositioned from any other explicit user interface entry point.

    It is not possible to provide a default name for the operation.

    The next interactive step is determined by the return code as follows:


    Return :
    Return Code/Description

    1   Cancel current assembly operation

    3   Reserved for future use

    n   Normal operation with no default strings.  "n" is any other return
        code except  1 or 3.

    Environment : Internal
    See Also :
    History : 
 */

extern DllExport void ufmcp(char *param, int *retcode, int rlen);
/*
    Substitute Component Out

    The substitute component out user exit occurs after the Assemblies->Components->Substitute Component 
    menu and after the component has been selected or when a component is about to be substituted 
    out from any other explicit user interface entry point.

    It is not possible to provide a default name for the operation.

    The next interactive step is determined by the return code as follows:

    Return :
    Return Code/Description

    1   Cancel current assembly operation

    3   Reserved for future use

    n   Normal operation with no default strings.  "n" is any other return
        code except  1 or 3.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufscpo(char *param, int *retcode, int rlen);

/*
    Substitute Component In

    The substitute component in user exit occurs after the Assemblies->Components->Substitute Component 
    menu. It is called before the component that is to be substituted in is selected.

    The next interactive step is determined by the return code as follows:

    Return :
    Return Code/Description

    1   Cancel current assembly operation

    2   Select Components dialog with the string (from param) as the
        default.

    3   Substitute component parameters menu with the part (from param) in case of the 
        Open As function. 
        In case of the Substitute function it will behave as return code 1.

    n   Normal operation with no default strings.  "n" is any other return
        code except  1,2 or 3.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufscpi(char *param, int *retcode, int rlen);

/*
    Open Spreadsheet

    The open spreadsheet user exit occurs when you activate the spreadsheet
    from NX.  You must be in the modeling or gateway application with
    an active part and you must be using a full licensed version of the 
    spreadsheet.  This event occurs interactively when a spreadsheet is 
    activated by selecting Toolbox->Spreadsheet from menubar.  Return codes 
    are ignored with this exit.
    In order to use the full licensed version of the Xess spreadsheet along with 
    the integrated NX/XESS customized applications, you must do the following
    prior to invoking NX:
    1) Set the UGII_SPREADSHEET variable in the .ugii_env file to point to the 
    directory which includes the 'xess4' binary executable.
    2) Set the environment variable, XESS_FULL, to anything (e.g. setenv XESS_FULL 1).

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufspop(char *param, int *retcode, int rlen);

/*
    Close Spreadsheet

    The close spreadsheet user exit occurs when you exit the spreadsheet
    and return control to NX.  You must be in the modeling
    application and you must be using a full licensed version of the 
    spreadsheet.  This event occurs interactively when a spreadsheet is
    active by selecting either File->Exit or Connections->Disconnect from
    the spreadsheet menubar.  Return codes are ignored with this exit.
    In order to use the full licensed version of the Xess spreadsheet along with 
    the integrated NX/XESS customized applications, you must do the following
    prior to invoking NX:
    1) Set the UGII_SPREADSHEET variable in the .ugii_env file to point to the 
    directory which includes the 'xess4' binary executable.
    2) Set the environment variable, XESS_FULL, to anything (e.g. setenv XESS_FULL 1).
    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufspcl(char *param, int *retcode, int rlen);

/*
    Update Spreadsheet

    The update spreadsheet user exit occurs at the start of updating
    expressions into the NX part file.  You must be in the modeling
    application.  First, you need to call Tools->Spreadsheet and
    then, in the Spreadsheet menu call Tools->Extract Expr in
    order to have some expressions.  The interactive entry point is
    Tools->Update Part.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufspup(char *param, int *retcode, int rlen);

/*
    Finish Updating Spreadsheet

    The finish updating spreadsheet exit occurs at the completion of 
    updating expressions.  You must be in the modeling application.  

    Return :
    Return Code/Description
       
    1   Perform a spreadsheet recalc after returning from the user
        exit.

    n   No spreadsheet recalc. "n" is any other return code except 1

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufspuf(char *param, int *retcode, int rlen);

/*
    Replace Reference Set

    The replace reference set user exit occurs after the Format->Reference Sets 
    dialog has been invoked and the "Set Current" button has been pushed or when 
    the Reference Set is about to be changed from any other explicit user 
    interface entry point.

    It is not possible to provide a default name for the operation.

    The next interactive step is determined by the return code as follows:


    Return :
    Return Code/Description

    1   Cancel current assembly operation

    3   Reserved for future use

    n   Normal operation with no default strings.  "n" is any other return
        code except  1 or 3.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufrrs(char *param, int *retcode, int rlen);

/*
    Rename Component

    The rename component user exit occurs after the Component Name 
    has been changed on the Parameters tab on the Component Properties 
    dialog and the user has pushed either OK or Apply.

    It is not possible to provide a default name for the operation.

    The next interactive step is determined by the return code as follows:

    Return :
    Return Code/Description

    1   Cancel current assembly operation

    3   Reserved for future use

    n   Normal operation with no default strings.  "n" is any other return
        code except  1 or 3.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufncp(char *param, int *retcode, int rlen);

/*
    NX Startup

    The NX startup  user exit occurs when you invoke NX. There are
    no  return codes for this option. If the user exit exists, your routine
    executes.  if the user exit does not exist, then NX starts as it
    normally would.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufsta(char *param, int *retcode, int rlen);

/*
    Debug GRIP

    The execute Debug GRIP user exit occurs after the File->Execute->Debug
    GRIP menu.

    The next interactive step is determined by the return code as follows:

    Return :
    Return Code/Description

    1   Runs the Debug GRIP program using the string passed from param. The
        Motif file  dialog is not displayed.

    2   Disables the Execute Debug GRIP option. The system adminstrator has
        the option  of making this option (and the use of a GRIP license)
        unavailable.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufgrpd(char *param, int *retcode, int rlen);

/*
    User Function

    The execute User Function user exit occurs after the File->Execute->User
    Function  menu.

    The next interactive step is determined by the return code as follows:

    Return :
    Return Code/Description

    1   Runs the User Function program using the string passed from param.
        The Motif  file dialog is not displayed.

    2   Disables the Execute User Function option. The system adminstrator
        has the  option of making this option (and the use of a User
        Function license) unavailable.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufufun(char *param, int *retcode, int rlen);


/*
    CAM New Operation:

    User Function

    (1) The 'new operation' exit occurs after
      - Application->Manufacturing
      - Select the desired Operation Template Type and SubType,
      - press 'NEW' button.
      The user exit number for new operation creation is 15.
OR
    (2) The operation re-initialization from an Operation Template 
    user exit occurs after
      - Application->Manufacturing
      - Select existing operation(s) to be re-initialized
      - press 'REINIT' button.
      The user exit number for operation re-initialization is 67.

    Selecting either of the above actions executes the USER_CREATE_OPER 
    user exit.

    The user's GRIP program will use &UENUM to retrieve the user exit number.
    Based on the user exit number returned by &UENUM, the user program will 
    know if this exit is currently invoked by new operation creation or 
    existing operation re-initialization.

    The name of the operation is passed through the oper_name argument.
    In GRIP, the user can use &UESTR to retrieve the operation name. 
    Use &UEXERR to set the return code upon exit from a GRIP program.
    If there are more than one operation selected for re-initialization,
    the user exit will be called once for each operation to be re-initialized.


    Return :
    Return Code/Description

   -1   User Exit Error, abort operation action and return to CAM Operation 
        Manager dialog

    0   Successful User Exit execution, proceed normally.

    1   Successful User Exit execution, return to CAM Operation Manager dialog.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufnopr(
    char *oper_name,      /* <I> - operation name */ 
    int *return_code,     /* <O> - return code */
    int oper_name_length  /* <I> - the length of the new operation name */
);

/*
    CAM Startup

    The CAM startup user exit occurs after the Application->Manufacturing...
    menu. 


    Return :
    Return Code/Description
    -1   User Exit Error, abort and return to Gateway

    0   Successful User Exit execution, proceed normally.

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void ufcams(char *param, int *retcode, int rlen);


/*
  CAM exit udop

  This cam exit will be invoked when creating/editing a CAM User-Defined 
  Operation in an interactive NX session.

  The "char *param" argument must be converted to a CAM exit id by
  type casting. For example, the following line of code performs the
  conversion:
  UF_CAM_exit_id_t  exit_id = (UF_CAM_exit_id_t)param;

    Return :
    Return Code/Description 

   -1   User Exit Error

    0   Successful User Exit execution

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void udop(
    char *param,       /* <I> - A parameter used to convert Open API param
                                to CAM exit id. */
    int *return_code,  /* <O> - return code */
    int parm_len       /* <I> - length of input "param" */
);

/*
  CAM exit udopcopy

  This cam exit will be invoked when creating/copying a CAM User-Defined 
  Operation in an interactive NX session.

  The "char *param" argument must be converted to a CAM exit id by
  type casting. For example, the following line of code performs the
  conversion:
  UF_CAM_exit_id_t  exit_id = (UF_CAM_exit_id_t)param;

    Return :
    Return Code/Description 

   -1   User Exit Error

    0   Successful User Exit execution

    Environment : Internal
    See Also :
    History : 
*/

extern DllExport void udopcopy(
    char *param,       /* <I> - A parameter used to convert Open API param
                                to CAM exit id. */
    int *return_code,  /* <O> - return code */
    int parm_len       /* <I> - length of input "param" */
);

/*
  CAM exit udopdelete

  This cam exit will be invoked when deleting a CAM User-Defined 
  Operation in an interactive NX session.

  The "char *param" argument must be converted to a CAM exit id by
  type casting. For example, the following line of code performs the
  conversion:
  UF_CAM_exit_id_t  exit_id = (UF_CAM_exit_id_t)param;

    Return :
    Return Code/Description 

   -1   User Exit Error

    0   Successful User Exit execution

    Environment : Internal
    See Also :
    History : 
*/

extern DllExport void udopdelete(
    char *param,       /* <I> - A parameter used to convert Open API param
                                to CAM exit id. */
    int *return_code,  /* <O> - return code */
    int parm_len       /* <I> - length of input "param" */
);

/*
  CAM exit dpud

  This cam exit will be invoked when creating/editing a CAM User-Defined 
  Drive Path in an interactive NX session.

  The "char *param" argument must be converted to a CAM exit id by
  type casting. For example, the following line of code performs the
  conversion:
  UF_CAM_exit_id_t  exit_id = (UF_CAM_exit_id_t)param;

    Return :
    Return Code/Description 

   -1   User Exit Error

    0   Successful User Exit execution

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void dpud(
    char *param,       /* <I> - A parameter used to convert Open API param
                              to CAM exit id. */
    int *return_code,  /* <O> - return code */
    int parm_len       /* <I> - length of input "param" */
);

/*
  SMD exit uffpud

  This exit will be invoked when creating or updating a sheet metal 
  flat pattern.

  The "char *param" argument must be converted from character string
  to tag_t (integer) form. For example, the following code performs the
  conversion:
  tag_t  fp_group_id;
  sscanf(param,"%d", &fp_group_tag); 

    Return :
    Return Code/Description 

   -1   User Exit Error

    0   Successful User Exit execution

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void uffpud(
    char *param,       /* <I> - Flat pattern group id. (as character string) */
    int *return_code,  /* <O> - return code */
    int parm_len       /* <I> - length of input "param" */
);

/*
  CAM exit wetd

  This cam exit will be invoked when setting technology data for geometry or
  operation of WEDM in an interactive NX session.

  In the new API the exit object can be obtained by calling GetCamExitObject method on the CAMSetup 

    Return :
    Return Code/Description 

   -1   User Exit Error

    0   Successful User Exit execution

    Environment : Internal
    See Also :
    History : 
 */
extern DllExport void wetd(
    char *param,       /* <I> - A parameter used to convert Open API param
                                to CAM exit id. */
    int *return_code,  /* <O> - return code */
    int parm_len       /* <I> - length of input "param" */
);

#ifdef __cplusplus
}
#endif

#endif /* UF_EXIT_INCLUDED */

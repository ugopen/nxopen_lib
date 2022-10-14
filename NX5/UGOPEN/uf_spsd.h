/*****************************************************************************
             Copyright (c) 2004 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved



File description:
    Open C API routines to run Simulation Process Studio Wizards.

*****************************************************************************/

#ifndef UF_SPSD_H_INCLUDED
#define UF_SPSD_H_INCLUDED
#include <libugopenint_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/*==========================================================================

  ==========================================================================*/


/****************************************************************************
UF_SPSD_run_wizard :

Runs a Simulation Process Studio wizard from a User Function program.
The input to this function is the full file name of the xml wizard file.

The wizard will act upon the current work part.

Each wizard is designed to run on top of certain work part files. Many
Wizards run on Master Model files. Some run on Scenario files having certain
Environments. If an attempt is made to run a wizard on the wrong type of 
part file, an error code will be returned.

Return: int  error code  any detected error is returned through the error code. 
                         Use UF_get_fail_message to decode the error code.

Environment: Internal only
See Also:
 UF_get_fail_message  
History: This function was originally released in NX3.
  
 ***************************************************************************/
extern UGOPENINTEXPORT int UF_SPSD_run_wizard(
const char* xml_filename /* <I>
                            The full file name of the wizard.
                          */
);

/****************************************************************************
UF_SPSD_callback_data_p_t :
  Information structure for the SPSD Logic Step Choice Callback.
  
  Reserved for future use.

Environment: Internal only
See Also:
None

History: This function was originally released in NX3.
  
 ***************************************************************************/
typedef void*  UF_SPSD_callback_data_p_t;


/****************************************************************************
UF_SPSD_choice_cb_f_t :
  Callback prototype for the SPSD Logic Step Choice.
 
  Input: 
    xml_param –       An optional character string found in the XML param
                      element. 
                      The wizard author may place any character string 
                      in the XML element.

    callback_data_p – Reserved for future definition.
                      Intended to contain information about the wizard
   Output:
    None
   Returns: 
    Logical  -  True  == Choose this Choice for the Logic Step.
                False == Skip this choice for the Logic Step. 

Environment: Internal only
See Also:
None

History: This function was originally released in NX3.
  
 ***************************************************************************/
typedef int (*UF_SPS_choice_cb_f_t)( 
    const char* xml_param ,
    UF_SPSD_callback_data_p_t callback_data_p );

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_SPSD_H_INCLUDED  */

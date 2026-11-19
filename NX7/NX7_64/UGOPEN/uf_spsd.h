/*****************************************************************************
             Copyright (c) 2004 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved



File description:
    Open C API routines to run Simulation Process Studio Wizards.

*****************************************************************************/

#ifndef UF_SPSD_H_INCLUDED
#define UF_SPSD_H_INCLUDED
#include <libugopenint_exports.h>
#include <uf_retiring_ugopenint.h>

#ifdef __cplusplus
extern "C" {
#endif

/*==========================================================================

  ==========================================================================*/



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

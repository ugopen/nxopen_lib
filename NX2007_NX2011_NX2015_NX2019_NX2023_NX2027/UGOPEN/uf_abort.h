
/******************************************************************************

             Copyright (c) 1999 - 2001 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved

 

  File description:  

  This UF_ABORT API provides a mechanism to trap either the UNIX 
  <CTRL>+<SHIFT>+<L> abort signal or detect a user press of the "Ok" button 
  on the Work In Progress dialog on Windows.  This is accomplished by 
  periodically making calls to UF_ABORT_ask_flag_status in your application.

*****************************************************************************/

#ifndef UF_ABORT_H_INCLUDED
#define UF_ABORT_H_INCLUDED


/***************************************************************************

  ***************************************************************************/


#include <uf_defs.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif


/*****************************************************************************
  This routine is used to check whether the user has signaled an abort request 
  by pressing the key sequence CTRL+SHIFT+L or selecting OK in the Work
  In Progress dialog if NX has not had a chance to act on the signal.

  But if NX has already processed the abort request by the time this function 
  is called, then the return code is FALSE as the abort signal is already reset.

  Return:

  Return code  = 0 : successful
               > 0 : failing error number
               < 0 : failing error number

  Environment: Internal and External
  See Also:
  History:     Introduced in V16.0.3
  ***************************************************************************/
extern UFUNEXPORT int UF_ABORT_ask_flag_status(
    logical *flag        /* <O> when set to TRUE, indicates an abort signal */
);

/*****************************************************************************
  This routine is used to clear any pending abort requests.  It should be 
  called if the abort request is handled.

  Return:

  Return code  = 0 : successful
               > 0 : failing error number
               < 0 : failing error number

  Environment: Internal and External
  See Also:
  History:     Introduced in V16.0.3
  ***************************************************************************/
extern UFUNEXPORT int UF_ABORT_clear_abort(
    void
);


/*****************************************************************************
  This routine is used to disable the abort handler. It must be re-enabled with
  the function, UF_ABORT_enable_abort.  

  Return:

  Return code  = 0 : successful
               > 0 : failing error number
               < 0 : failing error number

  Environment: Internal and External
  See Also:
  History:     Introduced in V18.0
  ***************************************************************************/
extern UFUNEXPORT int UF_ABORT_disable_abort(
    void
);

/*****************************************************************************
  This routine is used to enable the abort handler.  It is used in conjunction
  with UF_ABORT_disable_abort.

  Return:

  Return code  = 0 : successful
               > 0 : failing error number
               < 0 : failing error number

  Environment: Internal and External
  See Also:
  History:     Introduced in V18.0
  ***************************************************************************/
extern UFUNEXPORT int UF_ABORT_enable_abort(
    void
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_ABORT_H_INCLUDED */

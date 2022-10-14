/******************************************************************************

      Copyright (c) 1993-2002 Electronic Data Systems Corporation
                    Unpublished - All rights reserved

******************************************************************************



File description :

   This include file contains routines that enable you to interact with 
   run objects. Using the routines you can:
       
       - Ask all run objects in a given part
       
       - Ask all from, to and member items of a run

       - Ask run id and and run type of a given run
*******************************************************************************/

#ifndef UF_ROUTE_RUN_INCLUDED
#define UF_ROUTE_RUN_INCLUDED

#include <uf_defs.h>
#include <libufun_exports.h>


#ifdef __cplusplus
extern "C" {
#endif

/***********************************************************************
Retrieves the run id and run type of a given run. Caller must free the 
memory.

Return:
       
Environment: Internal  and  External

See Also:  UF_free() 

History: Released in NX3.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_RUN_ask_run_id_and_type(
    tag_t      run,         /* <I>  Run object to inquire*/
    char       **run_id,    /* <OF> run_id of the run object, must be
                                    freed with UF_free()*/
    char       **run_type   /* <OF> run_type of run, must be
                                    freed with UF_free*/    
);

/***********************************************************************
Retrieves the from items of a run. All from items are extracted ports. 
Caller should free the array of from items

Return:
     
Environment: Internal  and  External

See Also:  UF_free() 

History: Released in NX3.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_RUN_ask_from_items(
    tag_t   run,            /* <I>  Run object to inquire*/
    int     *n_from_items,  /* <O> number of from items*/
    tag_t   **from_items    /* <OF,len:n_from_items> array of from items. 
                                    All from items are extracted
                                    ports. Must be freed with UF_free() */    
);

/***********************************************************************
Retrieves the to items of a run. All to items are extracted ports. 
Caller should free the array of to items

Return:
     
Environment: Internal  and  External

See Also:  UF_free() 

History: Released in NX3.0
 ***********************************************************************/
extern UFUNEXPORT int UF_ROUTE_RUN_ask_to_items(
    tag_t   run,          /* <I>  Run object to inquire*/
    int     *n_to_items,  /* <O> number of to items*/
    tag_t   **to_items    /* <OF,len:n_to_items> array of to items.
                                  All to items are extracted
                                  ports. Must be freed with UF_free() */    
);

/*************************************************************************
Retrieves the member items of a run. All member items are either extracted
ports or route segments. Caller should free the array of member items.

Return:
     
Environment: Internal  and  External

See Also:  UF_free() 

History: Released in NX3.0
 ************************************************************************/
extern UFUNEXPORT int UF_ROUTE_RUN_ask_member_items(
    tag_t   run,              /* <I>  Run object to inquire*/
    int     *n_member_items,  /* <O> number of member items*/
    tag_t   **member_items    /* <OF,len:n_member_items> array of member items.
                                      All member items are either
                                      extracted ports or route segments
                                      Must be freed with UF_free() */    
);

/*************************************************************************
Retrieves all run objects in given part. Caller should free the run array. 
If input part is NULL_TAG, current work part is assumed. 

Return:
     
Environment: Internal  and  External

See Also:  UF_free() 

History: Released in NX3.0
 ************************************************************************/
extern UFUNEXPORT int UF_ROUTE_RUN_ask_runs_in_part(
    tag_t     part,       /* <I>  Part to ask the run objects, if NULL_TAG,
                                  current work part is assumed*/
    int*      n_runs,     /* <O> number of runs in the given part*/
    tag_t**   runs        /* <OF,len:n_runs> array of runs. Must be freed with UF_free()*/
);

/**************************************************************************
Set the run id of given run. 

Return:

Environment: Internal and External

History: Released in NX3.0.2.3
****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_RUN_set_run_id(
    tag_t       run,         /* <I> Run to change the run id of */
    char*       run_id       /* <I> New run id of the run */
);

/***************************************************************************
Set the run type of given run. 

Return:

Environment: Internal and External

History: Released in NX3.0.2.3
****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_RUN_set_run_type(
    tag_t       run,         /* <I> Existing valid run */
    char*       run_type     /* <I> New run type of the run */
);

/****************************************************************************
Edit a given run. From and To items must be extracted ports or rcps. 
Member items must be extracted ports or route segments. 

Return:

Environment: Internal and External

History: Released in NX3.0.2.3
****************************************************************************/
extern UFUNEXPORT int UF_ROUTE_RUN_edit_run(
    tag_t         run,             /* <I> Run object to edit */
    char*         run_id,          /* <I> Run id of the run after edit */
    char*         run_type,        /* <I> Run type of the run after edit */
    int           n_from_items,    /* <I> Number of From items */
    tag_t*        from_items,      /* <I, len:n_from_items> Array of From items */
    int           n_to_items,      /* <I> Number of To items */
    tag_t*        to_items,        /* <I, len:n_to_items> Array of To items */
    int           n_member_items,  /* <I> Number of Member items */
    tag_t*        member_items     /* <I, len:n_member_items> Array of Member items */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif  /* END UF_ROUTE_RUN_INCLUDED */


/*******************************************************************************
             Copyright (c) 1998-2001,2006 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved

  

File Description:
   This file is the Open API interface to the UNDO_UG module. The UNDO_UG
   module does not own any NX data and, therefore, does not actually do any
   marking or undoing of data. UNDO_UG serves as an interface between the
   various NX applications and the various NX data managers. If an application
   wants a mark to be set, it only needs to make a single request of the UNDO_UG
   module. It is the purpose of UNDO_UG to instruct each of the NX data
   managers to set a mark. In the same fashion, if an application wishes
   to UNDO to a mark, it makes that single request of the UNDO_UG module. The
   UNDO_UG module insures that each data manager returns to the state it was
   in at the time the requested mark was set.

   NOTE:  There is a maximum limit of 100 undo marks that can be created in
   using an Open API program.

   We have added the notion of the Next Visible Mark and Miscellaneous
   callbacks. For a definition of the Next Visible Mark see the documentation
   for  UF_UNDO_undo_to_next_vis_mark.
   This was added primarily so that UNDO_UG can help manage the Edit->Undo
   function on the Menubar.

   Miscellaneous callbacks are fully described in the documentation for
    UF_UNDO_register_misc_cb.
   They can perform pre/post functions when setting/undoing marks. These are
   optional. These can be logged by anyone at anytime, can be flagged to be
   called only for particular marks or types of marks, and can be unlogged.
   Miscellaneous callbacks were added for display and Edit->Undo.

This file contains functions that enable you to:
 . Set a mark.
 . Undo or rollback to a particular mark.
 . Undo to the last mark of specified visibility.
 . Undo to the last mark of a specified visibility that occurs before a
   particular mark.
 . Get the visibility of a previously set mark
 . Set the visibility of a mark.
 . Ask if a particular mark exists.
 . Inquire how many marks of visibility exist.
 . Ask if any marks exist.
 . Flag a specified mark for deletion.
 . Delete all marks.
 . Delete a range of marks from the last mark set to a specified mark


An application can set a mark with a single request to the UNDO_UG module.
UNDO_UG instructs each of the NX data managers to set a mark. Similarly, an
application can UNDO to a mark with a single request of the UNDO_UG module. The
UNDO_UG module insures that each data manager returns to the state it was in at
the time the requested mark was set.  Two possible uses for UF_UNDO in your
programs are to perform error cleanup and iterative experimentation.

Error Cleanup:
For error cleanup, a program can set a mark upon entry and then if an
error occurs the program can return NX to the state it was in at entry
time by requesting a single UNDO. This is usually more efficient than
coding your program to determine what sequence of individual
operations are necessary to perform to return NX to its original state.

Iterative experimentation:
For iterative experimentation, your program can set a mark, execute a
set of operations, and then test the final results. If the results are not
as desired, the program can request an UNDO and then try an
alternate set of operations. Since the original mark still exists, the
program can experiment, check results, and UNDO any number of
times without setting a new mark. This saves both time and space.

******************************************************************************/
#ifndef UF_UNDO_H_INCLUDED
#define UF_UNDO_H_INCLUDED


/***************************************************************************

  ***************************************************************************/


/************************** Include Files ************************************/
#include <uf_defs.h>
#include <libufun_exports.h>

/***************************** Defines ***************************************/

#ifdef __cplusplus
extern "C" {
#endif

/*
 * This is the 'mark_id' to use when you want to identity an existing mark
 * by it's 'mark_name' instead of mark_id.
 */
#define   UF_UNDO_USE_NAME_ID          (-1)

/* This is the mark id to use when registering a misc cb that
 * should be executed for any mark, not just one particular mark.
 */
#define   UF_UNDO_MISC_CB_ANY_MARK     (-2)

/* The mark id of the next visible mark when there are no
 * more visible marks.
 */
#define   UF_UNDO_NO_VIS_MARK_PRESENT   0

/**************************** Typedefs ***************************************/

/* UF_UNDO_mark_id_t - the identifier for an UF_UNDO mark
 * This must match the return type of UNDO_set_markpoint.
 */
typedef int   UF_UNDO_mark_id_t;

/*
 * UF_UNDO_user_visibility_t - this feature allows for applications to
 * distinguish between two types of marks:
 *         1) UF_UNDO_visible - those the user can get to when
 *            they select the UNDO option, and
 *         2) UF_UNDO_invisible - those that were set by an application for
 *            algorithmic purposes but do NOT represent a state that
 *            the application wants the user going to when they select the
 *            UNDO option. The application will probably request to go to this
 *            mark as part of an algorithm.
 */
enum UF_UNDO_user_visibility_e
{
    UF_UNDO_visible,   /* Only perform function on visible marks. */
    UF_UNDO_invisible, /* Only perform function on invisible marks. */
    UF_UNDO_any_vis,   /* Perform function regardless of the visibility
                          of the mark. */
    UF_UNDO_visibility_2_big   /* Must be last. Only used for testing
                               purpose
                               */
};

typedef enum UF_UNDO_user_visibility_e UF_UNDO_user_visibility_t;

/*
 * UF_UNDO_mark_name_t - optional name that an application can tell
 * UF_UNDO to attach to a new mark when it is set and then used later in
 * place of the mark_id to identify the mark. This must be a '\0' terminated
 * array of chars if not NULL.
 */
typedef       char *    UF_UNDO_mark_name_t;
typedef const char *    UF_UNDO_mark_name_c_t;


/* Miscellaneous Callbacks type; see UF_UNDO_register_misc_cb() for details.
 * This is the value returned by your miscellaneous callback. It is used by the
 * PRE and POST callbacks to stop either the setting of a mark or the undoing
 * of a mark. Extreme caution should be used if using UF_UNDO_misc_cb_stop with
 * POST (and CHG_VIS) callbacks as the operation will be largely complete and
 * stopping the operation could cause a corruption of the session.
 */
enum UF_UNDO_misc_cb_ret_e
{
    UF_UNDO_misc_cb_continue,   /* Allow the operation */
    UF_UNDO_misc_cb_stop,       /* Don't allow the operation */
    UF_UNDO_misc_cb_2_big
};

typedef enum UF_UNDO_misc_cb_ret_e UF_UNDO_misc_cb_ret_t;

typedef UF_UNDO_misc_cb_ret_t   (*UF_UNDO_misc_cb_f_t)
(
   UF_UNDO_mark_id_t   mark_id, /* <I> mark_id - in the case of:
                                   UF_UNDO_misc_cb_set_pre
                                      The mark_id is not used
                                   UF_UNDO_misc_cb_set_post
                                      The mark_id of the mark just set
                                   UF_UNDO_misc_cb_undo_pre
                                      The mark_id of the mark we are about
                                      to undo to;
                                   UF_UNDO_misc_cb_undo_post
                                      The mark_id of the mark we just undid to.
                                   UF_UNDO_misc_cb_chg_vis
                                      The mark_id whose visibility just changed
                                 */
   void               *closure   /* <I> The closure argument passed in when this
                                    function was registered. */
);

/* The id returned by UF_UNDO_register_misc_cb() */
typedef int   UF_UNDO_misc_cb_id_t;

/* These are the miscellaneous callback types */
enum UF_UNDO_misc_cb_e
{
    UF_UNDO_misc_cb_set_pre = 0, /* To call func just before any
                                 mark is set. Definition: the passed
                                 mark_id  is the mark id we pass to
                                 the callback when we call it. It is
                                 not  the mark_id given here when you
                                 register  the callback. In the case of
                                 the current  cb_type, the passed mark_id
                                 is is not useful.
                                 */
    UF_UNDO_misc_cb_set_post,  /* to call func just after any mark is set
                               but before UF_UNDO returns back to the
                               application that set the mark. The passed
                               mark_id is the mark id of the mark just set.
                               */
    UF_UNDO_misc_cb_undo_pre,  /* to call func just before UF_UNDO performs
                               an undo to mark. The passed mark_id is the
                               mark id of the mark we are about to undo to.
                               */
    UF_UNDO_misc_cb_undo_post, /* to call func just after UF_UNDO performs
                               an undo to mark but before UF_UNDO returns
                               to the application that requested the undo.
                               The passed mark_id is the mark id of the mark
                               we just undid to.
                               */
    UF_UNDO_misc_cb_chg_vis,   /* to call func just after a mark has its
                               visibility changed. The passed mark_id is
                               the mark id of the mark whose visibility
                               just changed.
                               */
    UF_UNDO_misc_cb_type_2_big
};

typedef enum UF_UNDO_misc_cb_e UF_UNDO_misc_cb_t;
/************************* Public Functions **********************************/

/*****************************************************************************
Instructs every data manager which is logged on to set a mark.
Returns an identifier which the application can use to identify the
state of the data managers at the time the mark is set. Additionally,
the application can register a name by which this mark can later be
referenced.

Note:  The maximum number of undo marks in an Open API program is 100.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_UNDO_set_mark(
UF_UNDO_user_visibility_t visibility ,/* <I>
                                      The user visibility of this mark.
                                      */
UF_UNDO_mark_name_c_t mark_name ,/* <I>
                               optional name for this mark. If NULL
                               then not used. If not NULL then must
                               be '\0' terminated. UF_UNDO copies this
                               name to some space of its own, therefore,
                               the caller may do whatever it wants with
                               'mark_name' after the call.
                               */
UF_UNDO_mark_id_t * mark_id  /* <O>
                             identifier associated with this mark.
                             */
);


/*****************************************************************************
Performs an undo to a specific mark that was previously set by
UF_UNDO_set_mark. It instructs all data managers that are logged on
to return to their state associated with the specified mark.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_UNDO_undo_to_mark(
UF_UNDO_mark_id_t mark_id ,/* <I>
                           id of mark to undo to if != UF_UNDO_USE_NAME_ID
                           */
UF_UNDO_mark_name_c_t mark_name  /* <I>
                               name of mark to undo to if
                               mark_id == UF_UNDO_USE_NAME_ID
                               */
);

/*****************************************************************************
Performs an undo to the last mark of the specified visibility that was
previously set by UF_UNDO_set_mark. It instructs all data managers
that are logged on to return to their state associated with that mark.
The visibility referred to is the mark's current visibility which may
differ from the mark's original visibility (see UF_UNDO_set_mark_visibility).

Environment: Internal  and  External

See Also: UF_UNDO_set_mark_visibility

History:
******************************************************************************/
extern UFUNEXPORT int UF_UNDO_undo_to_last_mark(
UF_UNDO_user_visibility_t visibility ,/* <I>
                                      The desired visibility of the mark to
                                      undo to.
                                      */
UF_UNDO_mark_id_t *mark_id  /* <O>
                            id of mark undone to
                            */
);


/*****************************************************************************
Performs an undo to the last mark of the specified visibility that was
set before the previous_to mark. E.g., if previous_to is ID 4 and the
desired visibility is visible then this function finds the last visible mark
that appears before mark 4.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int   UF_UNDO_undo_to_prev_mark(
UF_UNDO_user_visibility_t visibility ,/* <I>
                                      The desired visibility of the mark to
                                      undo to.
                                      */
UF_UNDO_mark_id_t previous_to ,/* <I>
                               find the last mark of "visibility"
                               appearing before this mark
                               */
UF_UNDO_mark_id_t * mark_id  /* <O>
                             The ID of the mark undone to.
                             */
);

/*****************************************************************************
Finds the visibility of a previously set mark.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int   UF_UNDO_ask_mark_visibility(
UF_UNDO_mark_id_t mark_id ,/* <I>
                           Mark id to get the visibility of or
                           UF_UNDO_USE_NAME_ID
                           */
UF_UNDO_mark_name_c_t mark_name ,/* <I>
                               Mark name to get visibility of.  This is used
                               when mark_id is set to UF_UNDO_USE_NAME_ID.
                               */
UF_UNDO_user_visibility_t * visibility  /* <O>
                                        The visibility of the specified mark.
                                        */
);


/*****************************************************************************
Changes the visibility of a previously set mark to visibility.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int  UF_UNDO_set_mark_visibility(
UF_UNDO_mark_id_t mark_id ,/* <I>
                           Mark to change the visibility of or
                           UF_UNDO_USE_NAME_ID
                           */
UF_UNDO_mark_name_c_t mark_name ,/* <I>
                               Mark name to set visibility of.  This is used
                               when mark_id is set to UF_UNDO_USE_NAME_ID.
                               */
UF_UNDO_user_visibility_t visibility  /* <I>
                                      The new visibility for specified mark.
                                      */
);

/*****************************************************************************
An application calls this function to change the visibility of all existing
marks from the current mark to the specified "to_mark", inclusively.
The visibility of these marks is set to "visibility".

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_UNDO_set_to_mark_visibility(
UF_UNDO_mark_id_t to_mark ,/* <I>
                           The "to_mark" to change the visibility of, or
                           UF_UNDO_USE_NAME_ID
                           */
UF_UNDO_mark_name_c_t mark_name ,/* <I>
                               The mark name of the "to mark" to set visibility.
                               Only used when to_mark is UF_UNDO_USE_NAME_ID.
                               */
UF_UNDO_user_visibility_t visibility  /* <I>
                                             The new visibility for "to mark".
                                             */
);

/*****************************************************************************
Queries whether a mark exists.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_UNDO_ask_mark_exist(
UF_UNDO_mark_id_t mark_id ,/* <I>
                           id of mark to inquire or UF_UNDO_USE_NAME_ID
                           */
UF_UNDO_mark_name_c_t mark_name ,/* <I>
                               Mark name to inquire.  Only used when mark_id
                               is set to UF_UNDO_USE_NAME_ID.
                               */
int * exists  /* <O>
              Is 0 if mark_id DOES NOT exist, 1 otherwise
              */
);


/*****************************************************************************
Queries whether at least one mark of visibility exists.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_UNDO_ask_any_mark_exist(
UF_UNDO_user_visibility_t visibility ,/* <I>
                                      visibility of mark of interest
                                      */
int * any_exists  /* <O>
                  if at least 1 mark of 'visibility' exists then
                  1 else 0
                  */
);


/*****************************************************************************
Finds the number of marks for the specified visibility.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int   UF_UNDO_ask_number_of_marks(
UF_UNDO_user_visibility_t visibility ,/* <I>
                                      The visibility of the specified mark.
                                      */
int *how_many  /* <O>
               Number of marks that exist with the specified visibility.
               */
);


/*****************************************************************************
Flags the specified mark as deleted. It does not always remove the
mark. The mark is logically deleted from UF_UNDO and therefore
no one can call any UF_UNDO function with the mark id of this
deleted mark successfully.

Since this function does free up some mark space (and sometimes all mark
space) it is useful to call if one is trying to conserve space.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int  UF_UNDO_delete_mark(
UF_UNDO_mark_id_t mark_id ,/* <I>
                           Mark to delete or UF_UNDO_USE_NAME_ID
                           */
UF_UNDO_mark_name_c_t mark_name /* <I>
                              Mark name to delete.  This is used
                              when mark_id is set to UF_UNDO_USE_NAME_ID.
                              */
);


/*****************************************************************************
Deletes all marks. It instructs all logged on data managers to delete
their marks associated with each mark. It deals with each data
manager in the appropriate way. This function frees up all mark space.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_UNDO_delete_all_marks( void );


/*****************************************************************************
Performs a delete to a specific mark (inclusively) that was previously
set by UF_UNDO_set_mark. It instructs all data managers that are
logged on to delete their marks associated with the deleted
UF_UNDO marks. It deletes from the last mark set to the specified mark.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_UNDO_delete_to_mark(
UF_UNDO_mark_id_t mark_id ,/* <I>
                           Mark to delete to or UF_UNDO_USE_NAME_ID
                           */
UF_UNDO_mark_name_c_t mark_name /* <I>
                              Mark name to delete to.  This is used
                              when mark_id is set to UF_UNDO_USE_NAME_ID.
                              */
);

/*****************************************************************************
Passes back the mark_id of the Next Visible Mark. This is the mark
that is undone to, on a call to UF_UNDO_undo_to_next_vis_mark.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_UNDO_ask_next_vis_mark(
UF_UNDO_mark_id_t *mark_id  /* <O>
                            The mark id of the next visible mark.  This may
                            also be the value UF_UNDO_NO_VIS_MARK_PRESENT
                            in which case there are no more visible marks
                            to undo to.
                            */
);

/*****************************************************************************
UNDO to the Next Visible Mark. The Next Visible Mark (NVM) can
be described as follows:
1. Whenever a new mark is set AND that mark is visible,
   then it becomes the NVM.
2. If the NVM is undone to or over (i.e. the NVM is mark j
   and  we undo to mark i, i <= j) then the first visible mark
   prior to mark undone to becomes the NVM.
3. Same as 2 except for deleting marks instead of undoing to
   marks.
4. If the NVM is made invisible then the first visible mark
   previous to that NVM is made the new NVM.
5. If an existing invisible mark is made visible, then it is made
   the NVM if it was set after the previous NVM.
   UF_UNDO's NVM is updated upon a successful call to this function.
   Therefore, you may step back thru the visible marks by successive
   calls to this function. For example:
   while( UF_UNDO_undo_to_next_vis_mark() == UF_UNDO_REQ_OK )

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_UNDO_undo_to_next_vis_mark( void );

/*****************************************************************************
This function allows the Open API programmer to register a callback to be
executed before or after the setting/undoing of a mark.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_UNDO_register_misc_cb(
UF_UNDO_misc_cb_t cb_type ,/* <I>
                           Call back types:
                           UF_UNDO_misc_cb_set_pre to call the function just
                           before a mark is set. The function will always 
                           be passed a mark_id of -2.

                           UF_UNDO_misc_cb_set_post to call the function
                           just after any mark is set but before UF_UNDO
                           returns back to the application that set the mark.
                           The passed mark_id is the mark id of the mark just
                           set.

                           UF_UNDO_misc_cb_undo_pre to call the function
                           just before UF_UNDO performs an undo to mark.
                           The passed mark_id is the mark id of the mark we
                           are about to undo to.

                           UF_UNDO_misc_cb_undo_post to call the function
                           just after UF_UNDO performs an undo to mark
                           but before UF_UNDO returns to the application
                           that requested the undo. The passed mark_id is the
                           mark id of the mark we just undid to.

                           UF_UNDO_misc_cb_chg_vis to call the function just
                           after a mark has its visibility changed. The passed
                           mark_id is the mark id of the mark whose visibility
                           just changed.
                           */
UF_UNDO_mark_id_t mark_id ,/* <I>
                           If registering a function that should only be called
                           if processing a particular mark then enter that
                           mark_id here. If its a SET_PRE or SET_POST then
                           this argument is ignored. If you want a function
                           called whenever any mark is processed then enter
                           UF_UNDO_MISC_CB_ANY_MARK here.

                           If you enter a mark here and UF_UNDO is
                           requested to undo over that mark then the callback is
                           not called. It is only called if the given mark_id is
                           the one undone to.
                           */
UF_UNDO_user_visibility_t visibility ,/* <I>
                                      Take action based on the specific
                                      visibility:

                                      UF_UNDO_visible
                                        Only execute the given function if the
                                        mark being set or undone to is user
                                        visible or a mark was just made visible.
                                      UF_UNDO_invisible
                                        Only execute the given function if the
                                        mark being set or undone to is user
                                        invisible or a mark was just made
                                        invisible.
                                      UF_UNDO_any_vis to execute the function
                                      regardless of the mark's visibility.
                                      */
UF_UNDO_misc_cb_f_t func ,/* <I>
                          The function to call.
                          When this function is executed, the UF text mode will
                          be set to whatever the mode is when the function is registered.
                          If your SET_PRE or UNDO_PRE callback returns
                          UF_UNDO_misc_cb_stop when called then no further
                          callbacks are called and the setting or undoing of
                          the mark is not done.
                          If other callbacks return UF_UNDO_misc_cb_stop when
                          called then the operation will be partly complete and
                          an error will be returned. This action is not recommended.
                          */
void * closure ,/* <I>
                The argument to pass to the function when the function
                is called.
                */
UF_UNDO_misc_cb_id_t  * id  /* <O>
                            The identifier assigned to this registration. This
                            identifier can be used to remove this registration
                            via UF_UNDO_unregister_misc_cb().
                            */
);

/*****************************************************************************
Removes a registration previously made by UF_UNDO_register_misc_cb.

Environment: Internal  and  External

See Also:  UF_UNDO_register_misc_cb

History:
******************************************************************************/
extern UFUNEXPORT int UF_UNDO_unregister_misc_cb(
UF_UNDO_misc_cb_id_t cb_id  /* <I>
                            The id to remove.
                            */
);

/*****************************************************************************
Deletes all the miscellaneous callbacks currently registered.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_UNDO_delete_all_misc_cbs( void );

/*****************************************************************************
Disables all miscellaneous callbacks. That is, no miscellaneous
callback is called by UF_UNDO after this function is called until
UF_UNDO_enable_misc_cbs is called.  Miscellaneous callbacks are enabled
when UF_UNDO starts up.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_UNDO_disable_misc_cbs( void );

/*****************************************************************************
Enables miscellaneous callbacks. That is, all miscellaneous callbacks are
called by UF_UNDO after this function is called until
UF_UNDO_disable_misc_cbs is called.  Miscellaneous callbacks are enabled
when UF_UNDO starts up.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_UNDO_enable_misc_cbs( void );

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /* UF_UNDO_H_INCLUDED */

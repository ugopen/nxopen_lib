/*******************************************************************************
             Copyright (c) 1998-2003 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved

  

FILE DESCRIPTION:

This file describes the Open C API interface to the UIStyler for creating
NX like dialogs. The functions in this file enable you to :

   . Query a single item or dialog attribute.
   . Query item or dialog attributes.
   . Set an item or dialog attribute.
   . Create an NX (Styler generated) dialog.
   . Free all memory allocated for the specified value structure.
   . Query the dialog id from a selection callback

*******************************************************************************/

#ifndef UF_STYLER_INCLUDED
#define UF_STYLER_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_ui.h>
#include <libugopenint_exports.h>


#ifdef __cplusplus
extern "C" {
#endif


#define UF_STYLER_NULL_OBJECT        "UF_STYLER_NULL_OBJECT"
#define UF_STYLER_DIALOG_INDEX       "UF_STYLER_DIALOG_INDEX"
#define UF_STYLER_NAV_INDEX          "UF_STYLER_NAV_INDEX"
#define UF_STYLER_NO_INDEX           "UF_STYLER_NO_INDEX"

#define UF_STYLER_OK_INDEX           ( 0 )
#define UF_STYLER_APPLY_INDEX        ( 1 )
#define UF_STYLER_BACK_INDEX         ( 2 )
#define UF_STYLER_CANCEL_INDEX       ( 3 )

#define UF_STYLER_NO_SUB_INDEX       (-1)

/* Callback types */
#define UF_STYLER_NO_CB                ( -1 )
#define UF_STYLER_ACTIVATE_CB          (  0 )
#define UF_STYLER_VALUE_CHANGED_CB     (  1 )
#define UF_STYLER_DRAG_CB              (  2 )
#define UF_STYLER_DOUBLE_CLICK_CB      (  3 )
#define UF_STYLER_OK_CB                (  4 )
#define UF_STYLER_APPLY_CB             (  5 )
#define UF_STYLER_BACK_CB              (  6 )
#define UF_STYLER_CANCEL_CB            (  7 )
#define UF_STYLER_CONSTRUCTOR_CB       (  8 )
#define UF_STYLER_DESTRUCTOR_CB        (  9 )
#define UF_STYLER_FILEOP_CB            ( 10 )
#define UF_STYLER_SWITCH_CB            ( 11 )

#define UF_STYLER_MAX_CB_TYPES         ( 13 )

/* Callback reason */
#define UF_STYLER_NO_REASON            ( -1 )
#define UF_STYLER_ACTIVATE_REASON      (  0 )
#define UF_STYLER_VALUE_CHANGED_REASON (  1 )
#define UF_STYLER_DRAG_REASON          (  2 )
#define UF_STYLER_DOUBLE_CLICK_REASON  (  3 )
#define UF_STYLER_OK_REASON            (  4 )
#define UF_STYLER_APPLY_REASON         (  5 )
#define UF_STYLER_BACK_REASON          (  6 )
#define UF_STYLER_CANCEL_REASON        (  7 )
#define UF_STYLER_CONSTRUCT_REASON     (  8 )
#define UF_STYLER_DESTRUCT_REASON      (  9 )
#define UF_STYLER_FILEOP_REASON        ( 10 )
#define UF_STYLER_SWITCH_REASON        ( 11 )

/* Dialog & Item attributes */
#define UF_STYLER_NO_ATTR              ( -1 )
#define UF_STYLER_SENSITIVITY          (  0 )
#define UF_STYLER_VISIBILITY           (  1 )
#define UF_STYLER_VALUE                (  2 )
#define UF_STYLER_LABEL                (  3 )
#define UF_STYLER_BITMAP               (  4 )
#define UF_STYLER_FOCUS                (  5 )
#define UF_STYLER_SUBITEM_VALUES       (  6 )
#define UF_STYLER_DEFAULT_ACTION       (  7 )
#define UF_STYLER_DIALOG_WIDTH         (  8 )
#define UF_STYLER_DIALOG_RESIZE        (  9 )
#define UF_STYLER_SCALE_PRECISION      ( 10 )
#define UF_STYLER_ITEM_TYPE            ( 11 )
#define UF_STYLER_LIST_DESELECT        ( 12 )
#define UF_STYLER_LIST_INSERT          ( 13 )
#define UF_STYLER_LIST_DELETE          ( 14 )
#define UF_STYLER_LIST_SHOW            ( 15 )
#define UF_STYLER_SELECTION            ( 16 )
#define UF_STYLER_ACTIVE_PAGE          ( 17 )
#define UF_STYLER_ATTACHMENTS          ( 18 )
#define UF_STYLER_SCALE_LINE_INCREMENT ( 19 )

/* Item's value type */
#define UF_STYLER_NO_VALUE             ( -1 )
#define UF_STYLER_STRING_VALUE         (  0 )
#define UF_STYLER_STRING_PTR_VALUE     (  1 )
#define UF_STYLER_INTEGER_VALUE        (  2 )
#define UF_STYLER_INTEGER_PTR_VALUE    (  3 )
#define UF_STYLER_REAL_VALUE           (  4 )
#define UF_STYLER_REAL_PTR_VALUE       (  5 )
#define UF_STYLER_SELECTION_VALUE      (  6 )
#define UF_STYLER_OPTION_TOGGLE_VALUE  (  7 )

/* Item types */
#define UF_STYLER_INVALID_TYPE         ( -1 )
#define UF_STYLER_LABEL_TYPE           (  0 )
#define UF_STYLER_INTEGER_TYPE         (  1 )
#define UF_STYLER_REAL_TYPE            (  2 )
#define UF_STYLER_STRING_TYPE          (  3 )
#define UF_STYLER_WIDE_STRING_TYPE     (  4 )
#define UF_STYLER_ACTION_BUTTON_TYPE   (  5 )
#define UF_STYLER_TOGGLE_TYPE          (  6 )
#define UF_STYLER_BITMAP_TYPE          (  7 )
#define UF_STYLER_BUTTON_LAYOUT_TYPE   (  8 )
#define UF_STYLER_OPTION_MENU_TYPE     (  9 )
#define UF_STYLER_RADIO_BOX_TYPE       ( 10 )
#define UF_STYLER_TOOL_PALETTE_TYPE    ( 11 )
#define UF_STYLER_SCALE_REAL_TYPE      ( 12 )
#define UF_STYLER_SCALE_INTEGER_TYPE   ( 13 )
#define UF_STYLER_SINGLE_LIST_TYPE     ( 14 )
#define UF_STYLER_MULTI_LIST_TYPE      ( 15 )
#define UF_STYLER_SELECTION_BOX_TYPE   ( 16 )
#define UF_STYLER_SEPARATOR_TYPE       ( 17 )
#define UF_STYLER_SCROLLED_WINDOW_TYPE ( 18 )
#define UF_STYLER_MULTI_LINE_TEXT_TYPE ( 19 )
#define UF_STYLER_DIALOG_TYPE          ( 20 )
#define UF_STYLER_COLOR_TOOL_TYPE      ( 21 )
#define UF_STYLER_OPTION_TOGGLE_TYPE   ( 22 )
#define UF_STYLER_BEGIN_GROUP_TYPE     ( 23 )
#define UF_STYLER_END_GROUP_TYPE       ( 24 )


typedef int UF_STYLER_dialog_id_t;

#define UF_STYLER_ENTER_FILE_OPERATION (1)
#define UF_STYLER_EXIT_FILE_OPERATION  (0)

/*
   The following structure is used for file operation callback.
   The id field is set to one of the file operation types defined in uf_ui_types.h, e.g.
   UF_UI_FILE_NEW. State field indicates if we are entering a file
   operation (UF_STYLER_ENTER_FILE_OPERATION) or exiting a file operation
   (UF_STYLER_EXIT_FILE_OPERATION).
*/
struct UF_STYLER_fileop_s
{
    int id;
    int state;
};
typedef struct UF_STYLER_fileop_s UF_STYLER_fileop_t, *UF_STYLER_fileop_p_t;

/*
   The following structure is used for property page switch callback.
*/
struct UF_STYLER_page_switch_s
{
    int activated_page;      /* Activated page index */
    int deactivated_page;    /* Deactivated page index */
};
typedef struct UF_STYLER_page_switch_s UF_STYLER_page_switch_t, *UF_STYLER_page_switch_p_t;

/*
   The following union is used for notification callbacks.
*/
union UF_STYLER_notification_u
{
    UF_STYLER_fileop_t fileop;            /* File operation data */
    UF_STYLER_page_switch_t page_switch;  /* Property page switch data */
};
typedef union UF_STYLER_notification_u UF_STYLER_notification_t, *UF_STYLER_notification_p_t;

/*
   This is a union of all possible data types that attributes can have.
   Depending on the indicator, the value field can represent a single string,
   an array of strings, an integer, an array of integers, a double, an array
   of doubles, a selection structure or a notification structure.  When
   requesting an attribute modification, the Open API program must set
   this field to the desired appropriate value(s).  When the UIStyler returns
   from the attribute query or callback data, it sets this field to proper
   value(s) with the indicator field correctly set to indicate the data type
   of this field.  If this field contains data returned from the UIStyler,
   it must be freed by the Open API program when it is no longer needed.
   This can be done by calling UF_STYLER_free_value.
*/
union UF_STYLER_value_u
{
    char    *string;                      /* A string value */
    char   **strings;                     /* An array of strings */
    int      integer;                     /* An integer value */
    int     *integers;                    /* An array of integers */
    double   real;                        /* A double value */
    double  *reals;                       /* An array of doubles */
    UF_UI_selection_p_t  selection;       /* A pointer to a selection structure */
    UF_STYLER_notification_p_t notify;    /* A pointer to the notification structure */
    UF_UI_attachment_t attach;            /* Attachments structure */
    UF_UI_option_toggle_t option_toggle;  /* Option toggle structure */
};

typedef union UF_STYLER_value_u UF_STYLER_value_t;

/*
   The following structure is used for callbacks and Ask/Set methods. Reason,
   item_id, subitem_index, and item_attr are used as descriptive fields to
   describe the ownership of the attribute. Count, indicator, and value are
   used to represent the value of the attribute. Note that not all fields in
   this structure are relevant at one time. Depending on the item type and
   attribute type, zero or more additional fields may become relevant.
*/
struct UF_STYLER_item_value_type_s {
    int     reason;         /* Used in callback data, this is output from
                               UF_STYLER functions.  This indicates the type of
                               action, that triggers the callback, e.g.
                               UF_STYLER_ACTIVATE_CB.  Open API callbacks
                               can rely on this field to determine what user
                               interaction has occurred.  Programs should not
                               modify this value. */
    const char    *item_id; /* This is the most important field in the
                               structure.  It indicates the UIObject identifier
                               that is associated with any interactions
                               between the UIStyler and the Open API program.
                               If the structure is used as callback data, this
                               field is set by the UIStyler to indicate the
                               UIObject that triggered the callback.  This field
                               can also be set by the Open API program when
                               it makes any requests to the UIStyler for any
                               attribute queries or modifications.  The
                               UIObject identifiers to use for this field
                               by the Open API program are supplied by the
                               creator of the dialog when constructing the
                               dialog.  These values are placed in the header
                               file that is generated by the UIStyler for the
                               dialog. */
    int     subitem_index;  /* This field is to be used only by the Open API
                               program to set attributes of objects that have
                               subitems or entries.  This includes Button
                               Layout, Option Menu, Radio Box, Tool Palette,
                               Single-selection LIst, Multiple-selection List,
                               Selection Box and Navigation Buttons.  It will
                               be a zero based index to indicate which subitem
                               within this object is to be modified. */
    int     count;          /* This indicates the number of data values in the
                               union part of this structure.  The count is 1
                               except when more than one integer, string or real
                               values are present.  The count is set by the
                               UIStyler in callback data, or on an attribute
                               query.  This must be specified by the Open
                               API program only when it requests the UIStyler
                               to replace subitem values for an Option Menu,
                               Single-selection List, Multiple-selection List
                               and Selection Box. */

    int     item_attr;      /* This is the second most important piece of data
                               in the structure.  It indicates the attribute
                               that is associated with the interaction between
                               the UIStyler and the Open API program.  When
                               requesting any attribute modifications or
                               querying on any attribute values, the Open
                               API program should set this to the desired
                               attribute.  The attribute names are included in
                               uf_styler.h.  This field is set by the UIStyler
                               only when it dispatches a callback, and the
                               callback has valid data, in which case it sets
                               this field to UF_STYLER_VALUE. */
    int     indicator;      /* Indicates the data type of the value or values
                               that are associated with the indicated
                               attribute.  The UIStyler sets this field
                               when dispatching a callback, or when an
                               attribute query is made from the Open API
                               program.  The Open API program needs this
                               field to determine the proper data type for the
                               union in the structure.  When setting or
                               querying attributes, the Open API program
                               normally doesn't need to set this field, unless
                               there is an ambiguity.  Currently, only the
                               lists (Single-selection, Multiple-selection, and
                               Selection Box) require this field to be set to
                               indicate whether a string or an array of strings
                               is to be added to the list, or that an array of
                               names or indices is to be returned from the
                               query. */
    UF_STYLER_value_t value; /* union of all possible data types that
                                attributes can have.
                                See  UF_STYLER_value_t
                             */
};

typedef struct UF_STYLER_item_value_type_s UF_STYLER_item_value_type_t,
                                          *UF_STYLER_item_value_type_p_t;

/* Callback prototype - All callbacks for the UIStyler contain the
   same argument list.
   dialog_id   - Indicates the dialog that the callback is associated with
   client_data - Specified user defined data associated with your dialog.
   call_data   - Information specific to the UIStyler object type and
                 callback type.
*/
typedef int (*UF_STYLER_cb_f_t)(int dialog_id, /* <I> */
                            void *client_data, /* <I> */
                            UF_STYLER_item_value_type_p_t call_data /* <I> */ );

/*
   Callback information is stored in the following structure.

   A list of callbacks associated with your dialog is automatically
   generated for you in your template file.
*/

struct UF_STYLER_callback_info_s {
        char              *object_id; /* Indicates the specific object that
                                         the callback is associated with. */
        int                cb_type;   /* Indicates the type of callback, e.g.
                                         UF_STYLER_ACTIVATE_CB.  See the
                                         #defines in uf_styler.h for the
                                         complete list of callback types. */
        int is_dialog_launching_cb;   /* Informs the UIStyler that this callback
                                         will construct a dialog. */
        UF_STYLER_cb_f_t   callback_proc; /* The callback function */
};

typedef struct UF_STYLER_callback_info_s UF_STYLER_callback_info_t,
                                        *UF_STYLER_callback_info_p_t;

/*----------- prototypes ----------------*/

/******************************************************************************
Queries a single item or dialog attribute. You can only use this
function from within a UIStyler dialog callback.

Environment: Internal

See Also:

History:
 ******************************************************************************/
extern UGOPENINTEXPORT int UF_STYLER_ask_value(
int dialog_id ,/* <I>
               Identifier of the dialog. Associates the
               requested values to the correct dialog.
               */
UF_STYLER_item_value_type_p_t value /* <IOF,free:UF_STYLER_free_value>
                                     Value structure. Input the item number and
                                     attribute to query.
                                     The structure returns the requested data.
                                     you must deallocate memory for all strings,
                                     array of strings, or array of integers. Use
                                     UF_STYLER_free_value.
                                     */
);

/******************************************************************************
Queries multiple items or dialog attributes in one batch and returns
the requested data. You can only use this function from within a
UIStyler dialog callback.

Environment: Internal

See Also:

History: Original release was in V13.0.
 ******************************************************************************/
extern UGOPENINTEXPORT int UF_STYLER_ask_values(
int dialog_id ,/* <I>
               Identifier of the dialog. Associates the
               requested values to the correct dialog.
               */
int num_values ,/* <I>
                Size of the array of values.
                */
UF_STYLER_item_value_type_p_t values ,/* <IOF>
                                      Array of Value structures. The calling
                                      program must allocate an array of value
                                      structures, and initialize the item
                                      number and attribute to query fields for
                                      each structure.  Eachstructure in the
                                      array returns the requested data.
                                      The memory allocated in each structure
                                      must be freed by the caller.  This can
                                      be done by calling UF_STYLER_free_value,
                                      for each structure in the array.
                                       */
int *count  /* <O>
           A count of the number of values in the
           array that are successfully obtained. If this
           variable is NULL, UF_err_bad_parameter_number_4 is returned.
           */
);


/******************************************************************************
Sets an item or dialog attribute. You can only use this function from
within a UIStyler dialog callback.

Environment: Internal

See Also:

History: Original release was in V13.0.
 ******************************************************************************/
extern UGOPENINTEXPORT int UF_STYLER_set_value(
int dialog_id ,/* <I>
               Identifier of the dialog. Associates the
               requested values to the correct dialog.
               */
UF_STYLER_item_value_type_p_t value  /* <I>
                                     Value structure. The structure must contain
                                     at least the item number and attribute to
                                     set. Additional data may be required
                                     depending on the type of item and
                                     attribute.
                                     */
);

/******************************************************************************
Creates and displays an NX (UIStyler generated) "bottom" dialog.  This
dialog is generated and displayed to NX, if it is provided with
a valid ".dlg" file. The ".dlg" file can only be generated from the
Open UIStyler.

Environment: Internal

See Also:

History: Original release was in V13.0.
 ******************************************************************************/
extern UGOPENINTEXPORT int UF_STYLER_create_dialog (
const char * dialog_file ,/* <I>
                    UIStyler dialog file name with a .dlg file
                    extension.
                    */
UF_STYLER_callback_info_t * cbs ,/* <I,len:number_of_cbs>
                                 UIStyler dialog file callback list. This list
                                 is automatically generated by the UIStyler
                                 and placed in the template file associated
                                 with your ".dlg" file. This list should NOT
                                 be modified directly. If you wish to alter
                                 your callback list, you must regenerate your
                                 template file from the UIStyler.
                                 */
int number_of_cbs ,/* <I>
                   Number of entries in the dialog's callback
                   list. This list is automatically generated by
                   the UIStyler and placed in the template file
                   associated with your ".dlg" file. This list
                   should NOT be modified directly. If you
                   wish to alter your callback list, you must
                   regenerate your template file from the
                   UIStyler.
                   */
void * client_data ,/* <I>
                    Dialog client data passed via callbacks.
                    Your client data is passed to all of your
                    callback functions when they are called.
                    Client data is technically the address of any
                    value, for example, pointers to variables,
                    data structures, arrays, etc.
                    */
int *response /* <O>
              Response value upon dialog termination.
              UF_UI_OK
              UF_UI_CANCEL
              UF_UI_BACK
              UF_UI_PICK_RESPONSE
              UF_UI_CB_TERMINATE
              */
);

/******************************************************************************
Frees all memory allocated for the specified value structure.  If a structure
is passed that has no data to be freed, this function will take no action
and return a successful completion.

Environment: Internal

See Also:

History: Original release was in V13.0.
 ******************************************************************************/
extern UGOPENINTEXPORT int UF_STYLER_free_value (
UF_STYLER_item_value_type_p_t data  /* <I>
                                    Value structure to free.
                                    */
);

/******************************************************************************
This function provides the dialog id associated with a dialog.  It
should be used within selection callbacks if the selection callback
needs to modify any UIObjects in a UIStyler dialog.

Environment: Internal

See Also:

History: Original release was in V13.0.
 ******************************************************************************/
extern UGOPENINTEXPORT int UF_STYLER_ask_select_dialog_id (
UF_UI_selection_p_t selection_data ,/* <I>
                                    Selection data.
                                    */
UF_STYLER_dialog_id_t * dialog_id  /* <O>
                                   Dialog id of dialog that contains
                                   selection_data
                                   */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /*  UF_STYLER_INCLUDED  */

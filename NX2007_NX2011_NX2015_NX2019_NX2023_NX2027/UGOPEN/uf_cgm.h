/*****************************************************************************

                   Copyright (c) 2003 UGS PLM Solutions Inc.
                      Unpublished - All Rights Reserved                       



File description: 

The functions in this and other uf_cgm_*.h files allow you to perform
CGM-related operations, including functions for:

exporting CGMs from parts
importing CGMs to parts
inquiring information about CGM import and export options

*****************************************************************************/

#ifndef UF_CGM_H_INCLUDED
#define UF_CGM_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_cgm_types.h>
#include <uf_part_types.h>        /* For UF_PART_METRIC and UF_PART_ENGLISH */
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif


/****************************************************************************
Returns the default CGM export custom colors.

Environment: Internal  and  External

See Also:  UF_CGM_custom_colors_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_CGM_ask_default_custom_colors
(
    UF_CGM_custom_colors_p_t        custom_colors /* <O>
                                                     The custom colors
                                                  */
);

/****************************************************************************
Returns the current CGM export custom colors for the session.

Environment: Internal  and  External

See Also:  UF_CGM_custom_colors_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_CGM_ask_session_custom_colors
(
    UF_CGM_custom_colors_p_t        custom_colors /* <O>
                                                     The custom colors
                                                  */
);

/****************************************************************************
Modifies the current CGM export custom colors for the session. Call 
one of the following functions to initialize the UF_CGM_custom_colors_t 
structure before setting structure fields.

    UF_CGM_ask_default_custom_colors
    UF_CGM_ask_session_custom_colors 
    UF_PLOT_ask_drawing_sheet_colors
    UF_PLOT_read_custom_colors_from_cdf

Environment: Internal  and  External

See Also:  UF_CGM_custom_colors_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_CGM_set_session_custom_colors
(
    UF_CGM_custom_colors_p_t        custom_colors /* <I>
                                                     The custom colors
                                                  */
);

/****************************************************************************
Returns the default CGM export custom widths.

Environment: Internal  and  External

See Also:  UF_CGM_custom_widths_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_CGM_ask_default_custom_widths
(
    UF_CGM_custom_widths_p_t        custom_widths /* <O>
                                                     The custom widths
                                                  */
);

/****************************************************************************
Returns the current CGM export custom widths for the session.

Environment: Internal  and  External

See Also:  UF_CGM_custom_widths_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_CGM_ask_session_custom_widths
(
    UF_CGM_custom_widths_p_t        custom_widths /* <O>
                                                     The custom widths
                                                  */
);

/****************************************************************************
Modifies the current CGM export custom widths for the session. Call
one of the following functions to initialize the UF_CGM_custom_widths_t 
structure before setting structure fields.

    UF_CGM_ask_default_custom_widths
    UF_CGM_ask_session_custom_widths 
    UF_PLOT_ask_drawing_sheet_widths
    UF_PLOT_read_custom_widths_from_wdf

Environment: Internal  and  External

See Also:  UF_CGM_custom_widths_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_CGM_set_session_custom_widths
(
    UF_CGM_custom_widths_p_t        custom_widths /* <I>
                                                     The custom widths
                                                  */
);
 
/****************************************************************************
Returns the default CGM export option settings.

Environment: Internal  and  External

See Also:  UF_CGM_export_options_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_CGM_ask_default_export_options
(
    UF_CGM_export_options_p_t      export_options /* <O>
                                                     The options
                                                  */
);

/****************************************************************************
Returns the current CGM export option settings for the session.

Environment: Internal  and  External

See Also:  UF_CGM_export_options_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_CGM_ask_session_export_options
(
    UF_CGM_export_options_p_t      export_options /* <O>
                                                     The options
                                                  */
);

/****************************************************************************
Modifies the current CGM export option settings for the session. Call
UF_CGM_ask_default_export_options or UF_CGM_ask_session_export_options 
to initialize the UF_CGM_export_options_t structure before setting 
structure fields.

Environment: Internal  and  External

See Also:  UF_CGM_export_options_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_CGM_set_session_export_options
(
    UF_CGM_export_options_p_t      export_options /* <I>
                                                     The options
                                                  */
);
 
/****************************************************************************
Exports a CGM file with the specified name. Suffix .cgm is appended to 
the name if not present. If a CGM file of the same name already exists, 
it is overwritten.  The drawing sheet provided must be in the displayed
part.

Environment: Internal  and  External

See Also:  UF_CGM_export_options_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_CGM_export_cgm
(
    tag_t                     drawing_sheet,  /* <I> The tag of the drawing
                                                 sheet to export. If set to
                                                 NULL_TAG, the current display
                                                 image is exported instead. */
    UF_CGM_export_options_p_t export_options, /* <I> Specifies export options.
                                              If NULL, current session export 
                                              options are used instead. If 
                                              non-NULL, call 
                                              UF_CGM_ask_default_export_options 
                                              or 
                                              UF_CGM_ask_session_export_options 
                                              to initialize the structure before
                                              setting structure fields. Current 
                                              session export options are not 
                                              modified by structure values. */
    const char                *file_name      /* <I> The CGM filename */
);

/****************************************************************************
Initializes the fields of a UF_CGM_import_options_t structure to default 
values. Call this function before setting structure fields in preparation 
to call UF_CGM_import_cgm.

Environment: Internal  and  External

See Also:  UF_CGM_import_options_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_CGM_init_import_options
(
    UF_CGM_import_options_p_t      import_options /* <O>
                                                     The options
                                                  */
);

/****************************************************************************
Imports the CGM file with the specified name.

Environment: Internal  and  External

See Also:  UF_CGM_import_options_t

History: Originally released in NX3.0.
****************************************************************************/
extern UFUNEXPORT int UF_CGM_import_cgm
(
    char                      *file_name,     /* <I> The CGM filename */
    UF_CGM_import_options_p_t import_options  /* <I> Specifies import options.
                                                If NULL, default import 
                                                options are used instead. If 
                                                non-NULL, call 
                                                UF_CGM_init_import_options 
                                                to initialize the structure 
                                                before setting structure 
                                                fields. */ 
);

/****************************************************************************
Registers functions to be called when exporting a CGM starts or stops.

Environment: Internal  and  External

See Also: 

History: Originally released in NX6.0.4
****************************************************************************/
extern UFUNEXPORT int UF_CGM_register_callbacks
(
    UF_CGM_pre_export_f_t pre_export,   /* <I> The function to be called when
                                          a CGM export is started.
                                        */
    UF_CGM_post_export_f_t post_export, /* <I> The function to be called when
                                           a CGM export is finished.
                                        */
    UF_CGM_export_error_f_t export_error /* <I> The function to be called when
                                            a CGM export gets an error.
                                         */
);

/****************************************************************************
Unregisters functions to be called when exporting a CGM starts or stops.

Environment: Internal  and  External

See Also: 

History: Originally released in NX6.0.4
****************************************************************************/
extern UFUNEXPORT int UF_CGM_unregister_callbacks
(
    UF_CGM_pre_export_f_t pre_export,   /* <I> The function previously registered
                                           to be called when a CGM export is started.
                                        */
    UF_CGM_post_export_f_t post_export, /* <I> The function previously registered
                                           to be called when a CGM export is finished.
                                        */
    UF_CGM_export_error_f_t export_error /* <I> The function previously registered
                                            to be called when a CGM export gets an error.
                                         */
);
#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_CGM_H_INCLUDED */

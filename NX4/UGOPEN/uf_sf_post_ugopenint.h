/******************************************************************************

                        Copyright (c) 2003 EDS PLM Solutions
                        Unpublished - All rights reserved
====================================================================================================


File description: 
    Open C API scenario post processor interface

*****************************************************************************/

#ifndef UF_SF_POST_UGOPENINT_H_INCLUDED
#define UF_SF_POST_UGOPENINT_H_INCLUDED
/*****************************************************************************

******************************************************************************/

#include <uf_defs.h>
#include <uf_sf_post_datatypes.h>
#include <libugopenint_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/*****************************************************************************
This function initialises the post processor session. It is necessary to call
this function before invoking any other post processing functionality.
 
Environment:  Internal

See Also:

History:  Released in NX3
 
******************************************************************************/
extern UGOPENINTEXPORT int UF_SF_POST_initialize_post_processor(void);

/*****************************************************************************
This function quits the post processor session. It is necessary to call  
this function to close the post processing functionality.  

Environment:  Internal

See Also:

History:  Released in NX3
******************************************************************************/
extern UGOPENINTEXPORT int UF_SF_POST_quit_post_processor(void);

/*****************************************************************************
This function applies template file to post processing session.
Will initialize post processor if already not done.

Environment:  Internal

See Also:

History:  Released in NX3
******************************************************************************/
extern UGOPENINTEXPORT int UF_SF_POST_apply_template( 
const char *filename_text_data            /* <I> Name of the template file to be applied
                                    */
);

/*****************************************************************************
This function save a XML template from current post processing session.

Environment:  Internal

See Also:

History:  Released in NX3
******************************************************************************/
extern UGOPENINTEXPORT int UF_SF_POST_save_template( 
UF_SF_POST_template_type_t template_type,/*<I> Type of template to save
                                          UF_SF_TEMPLATE_TYPE_LAYOUT
                                          UF_SF_TEMPLATE_TYPE_POSTVIEW
                                    */
int post_view_id,                   /*<I> ID of the postview to be saved
                                          equal to -1 if template_type is set to
                                          UF_SF_TEMPLATE_TYPE_LAYOUT
                                    */
char *xml_filename,                 /*<I> Name of the file to store
                                    */
char *name_text_data,               /*<I> Name of the template
                                    */
int use_icon,                       /*<I> Option for using captured image
                                          as icon for thumbnail in Post processing
                                          template palette 
                                          0 for default icon (camera)
                                          1 for using captured image
                                    */
int is_default                      /*    1 to save this template as a default
                                            template. The settings stored in this 
                                            template will then be used for creating new
                                            postviews
                                          0 otherwise
                                    */
);

/*****************************************************************************
This function verifies the solution to which XML template file will be applied 
in the current post processing session. Needed to be called before UF_SF_POST_apply_template

Environment:  Internal

See Also:

History:  Released in NX3
******************************************************************************/
extern UGOPENINTEXPORT int UF_SF_verify_and_set_solution_name(
const char *solution_name           /*<I> Name of the solution to apply
                                          template to
                                    */
);

#undef EXPORTLIBRARY

#ifdef __cplusplus
}
#endif

#endif     /* UF_MOTION_UGOPENINT_H_INCLUDED */

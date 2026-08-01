/*******************************************************************************
 *
 *       Copyright (c) 1998  Unigraphics Solutions Corporation
 *                  Unpublished - All rights reserved
 *
 *******************************************************************************
 *  File description:
 *
 *  This is part of a demo program to associate notes with drawing views
 *  using User Defined Objects (UDOs).  There are two other source files
 *  that are used with this file: ufx_udo_methods.c and ufx_udo_application.c
 *  In addition, there are two UG/Open MenuScript files (assoc_notes.men and
 *  add_assoc_notes.men) that add this functionality into Unigraphics in 
 *  a seamless fashion.  The two .men files add a custom button to the 
 *  Drafting Module's View menubar.  
 * 
 *  Before discussing the functionality of the demo the udo, startup and
 *  application directories must be created in a location pointed to by
 *  one of the following environment variables (UGII_SITE_DIR,
 *  UGII_VENDOR_DIR, and UGII_USER_DIR).
 *
 *  For example, if UGII_USER_DIR=/my_custom_code the directory 
 *  structure for my_custom_code would contain udo/, application/, and 
 *  startup/ as the three subdirectories.
 *                 
 *  The "udo/" directory contains the shared image obtained by compiling and
 *  linking ufx_udo_methods.c. The "application/" directory should contain
 *  the assoc_notes.men and the shared image produced by compiling and linking
 *  ufx_udo_application.c. The startup/ directory contains the 
 *  add_assoc_notes.men file which begins the menubar customization.
 *  The .ugii_env file needs to be customized with the 
 *  following line:
 *
 *      UGII_USER_DIR=<the parent directory of the udo, application, 
 *                     and startup directories>
 *
 *  And the add_assoc_notes.men file should be edited to contain
 *
 *      LIBRARIES ufx_udo_application.sl
 *
 *  Where the appropriate file extension for each particular platform is 
 *  as follows.
 *
 *      HP - .sl
 *      SUN, SGI, Digital Unix, AIX - so.
 *      VMS - .exe
 *      Windows NT - .dll
 *
 *  The user should refer to the documentation in the UDO chapter 
 *  of the UG/Open API (User Function) Reference Manual which describes the 
 *  use of the above directories in detail.
 *
 *  The Unigraphics image executes all shared images found in udo/
 *  directory once during Unigraphics startup. Thus the shared 
 *  image corresponding to ufx_udo_methods.c is executed 
 *  and registers the UDO methods (described below).  
 *  The other shared image corresponding to ufx_udo_application.c which 
 *  contains the dialog and application code to associate notes with views
 *  is executed by the user when a view note association is desired. The user
 *  selects the Associate Note button which is found within the Drafting module
 *  under the menubar pulldown labeled Views. The Associate Note custom button
 *  was added to the menubar Views pulldown by using the UG/Open MenuScript 
 *  files add_assoc_notes.men and assoc_notes.men.  The add_assoc_notes.men 
 *  file specifies the placement of the new custom button and the the name of 
 *  the shared image (i.e ufx_udo_application) to execute when the button 
 *  is pressed.  The assoc_notes.men file provides the name of the 
 *  button and the entry point (i.e. ug_demo_assoc_notes)
 *  to begin execution within the ufx_udo_application shared image.
 *
 *  The demo was written to show the use of UDO's in solving the
 *  following requests:
 *
 *      1. To associate notes with drawing member views such that the
 *         when the view moves the associated notes move with the view.
 *
 *      2. To allow the user to select a view using single selection
 *         in user function.
 *
 *  The following paragraphs described the various UDO methods which
 *  have been registered at startup of Unigraphics.
 *
 *  The demo uses the UDO assignments of links to couple each view
 *  and related notes with a UDO.  An update callback for the UDO's is
 *  registered which is executed by Unigraphics each time the view is moved.
 *  Within the body of the update callback the view's new position is obtained
 *  via user function queries and each associated note is moved by
 *  the indicated value.
 *
 *  The selection of views via user function single selection is accomplished
 *  by constructing four lines directly on top of each member view bounds.
 *  This gives the illusion of selecting a view via user function.
 *  Once the selection of views is completed the UDOs used for
 *  the selection are deleted and the methods are de-registered.
 *
 *  The demo allows the user to break the association of notes and views and
 *  to recreate new associations with other views.  If a note is already
 *  associated with a view a temporary marker is placed over the note to
 *  indicate an association.
 *
 *  The user should save the part with the desired association so when
 *  the part is loaded the associations will be preserved.
 *
 *  ******************************************************************
 *  ******************************************************************
 *  INSTRUCTIONS FOR WINDOWS/NT:
 *  1)  The file ufx_udo_methods.c needs to be compiled and linked as
 *  a DLL. (It needs to link against libufun.lib)
 *  2)  The file ufx_udo_application.c needs to be compiled and linked
 *  as a DLL. (It needs to link against libufun.lib *_AND_* the lib
 *  file created in the link of the ufx_udo_methods.dll above)
 *  ******************************************************************
 *  ******************************************************************
 *
 *

 *
 ****************************************************************************
*/

#ifndef UFX_UDO_H_INCLUDED
#define UFX_UDO_H_INCLUDED

#include <uf_defs.h>
#include <uf_udobj.h>
#include <uf_obj_types.h>


/* Max number of views in a drawing */
#define MAX_DRAW_VIEWS 50


/****************************************************************************
 *
 *  STRUCTURE:  UFX_UDO_view_info_s
 *
 *
 *  DESCRIPTION: Contains the information for a drawing member view 
 *
 *
 *
 ****************************************************************************/

typedef struct UFX_UDO_view_info_s
{
    /*
     *   The data below is NOT persistent and is reset  via
     *   the database when refinding the view information
     *
    */
  
                       /* The tag of the view */
    tag_t view_tag;
                       /* The view name null terminated */
    char view_name[ UF_OBJ_NAME_BUFSIZE ];
                      /* View center in Absolute coordinates*/
    double view_cntr[3];
                      /* The view borders in Drawing coordinates */
    double view_borders[4];

                      /* View Scale */
    double view_scale;

    /*
     *   The data below is persistent and is copied when refinding 
     *   the view information
     *
    */
                       /* The tag of the udo associated with this view */
    tag_t udo_tag;      

}UFX_UDO_view_info_t, *UFX_UDO_view_info_p_t;

/****************************************************************************
 *
 *  FUNCTION:  UFX_UDO_set_Metric
 *
 *
 *  DESCRIPTION:  Sets the metric or english value for drawings.  Is exported
 *                so it can access static data from the library loaded
 *                at startup time
 *
 *
 *
 ****************************************************************************/
DllExport extern void UFX_UDO_set_Metric(double  metric);
/****************************************************************************
 *
 *  FUNCTION:  UFX_UDO_get_note_vw_class
 *
 *
 *  DESCRIPTION:  Get the view class data.  Is exported
 *                so it can access static data from the library loaded
 *                at startup time
 *
 *
 *
 ****************************************************************************/
DllExport extern UF_UDOBJ_class_t UFX_UDO_get_note_vw_class(void);


/****************************************************************************
 *
 *  FUNCTION:  UFX_UDO_ask_view_center_dll
 *
 *
 *  DESCRIPTION:  Returns the view center at time of update. Is exported
 *                so it can access static data from the library loaded
 *                at startup time
 *
 *
 *
 ****************************************************************************/
DllExport extern void UFX_UDO_ask_view_center_dll(
tag_t view_tag,               /* I - The view tag */
double view_center[3]         /* O - The views center */
);

/****************************************************************************
 *
 *  FUNCTION: UFX_UDO_ask_all_view_data_dll
 *
 *
 *  DESCRIPTION: Finds all the view data at the time of inquiry and updates
 *               the view array.  Also returns memory for the view array.
 *               The view_array must be NULL on the first call and
 *               the pointer returned must be input on subsequent calls.
 *               It is exported so can access static data from the 
 *               library loaded at startup time
 *
 *
 ****************************************************************************/
DllExport extern void UFX_UDO_ask_all_view_data_dll(
    UFX_UDO_view_info_p_t *view_array,  /* I/O  - The pointer to the array */
    int *view_numb              /* O - The number of elements in the array */
);




#endif

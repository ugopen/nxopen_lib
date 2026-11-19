/*******************************************************************************
             Copyright (c) 1998-2000 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved                       



File Description:
   Open API interface to layouts.
   The routines in this file pertains to
   .    Create a view in a layout.
   .    Read/set view borders in a layout.
   .    Replace a view in a layout.
   .    Read the current layout name and work view name.
   .    Save the current layout.
   .    Retrieve/delete/rename a layout.
   .    Cycle layouts in a part.
   .    Read the number of views in a layout.
   .    Cycle views in a layout.   

*******************************************************************************/

#ifndef UF_LAYOUT_INCLUDED 
#define UF_LAYOUT_INCLUDED 

#include <uf_obj_types.h>

/***************************************************************************

  ***************************************************************************/


#include <uf_defs.h>
#include <uf_obj_types.h>
#include <uf_retiring.h>
#include <libufun_exports.h>


#ifdef __cplusplus
extern "C" {
#endif


/***************************************************************************
Create a layout.  view_names must be dimensioned to the number of views 
(or greater) specified in option layout_style. If any array value of view_names
is blank, the default view for that position is used. The first view
becomes the work view. The default views are:

layout_style    Default Views
        1       Top
        2       Front, Right
        3       Top, Front
        4       Top, Front, TFR-ISO, Right
        5       TFR-TRI, Left, Top, Front, TFR-ISO, Right

Return:
         Return Code
         0 = OK
         1 = View Does Not Exist
         2 = Invalid View Name
        12 = Invalid Layout Name
        14 = Layout Already Exists
        31 = Invalid Scale
        32 = Invalid Scale Option
        33 = Invalid Layout Style
        34 = A sketch view may not exist in a layout
                   more than one time.
        35 = Operation Not Allowed In Drafting

Environment: Internal  and  External

See Also:

History:
  ***************************************************************************/
extern UFUNEXPORT int uc6460(
const char * layout_name ,/* <I>
                          Layout Name (UF_OBJ_NAME_NCHARS char max)
                          */
int layout_style ,/* <I>
                  Layout Style
                  1 = Single View
                  2 = Side By Side
                  3 = Upper And Lower
                  4 = Four Views
                  5 = Six Views
                  */
const char view_names[][ UF_OBJ_NAME_BUFSIZE ] ,/* <I,len:layout_style>
                             View Names (UF_OBJ_NAME_NCHARS char max)
                             "" = Default Views
                             */
int scale_option ,/* <I>
                  Scale Option
                  1 = Retrieve As Saved
                  2 = Fit All Views
                  3 = Apply Scale parameter To All Views
                  */
double scale  /* <I>
              View Scale  (If scale_option=3)
              */
);

/***************************************************************************
Read view borders in a layout.  Border values range from 0,0 (bottom-left 
corner of the layout) to 1,1 (top-right corner of the layout).

Return:
         Return Code
        0       = OK
        1       = View Does Not Exist
        2       = Invalid View Name
        10      = View Not On Layout
        11      = Layout Does Not Exist
        12      = Invalid Layout Name
        19      = No Current Layout

Environment: Internal  and  External

See Also:

History:
  ***************************************************************************/
extern UFUNEXPORT int uc6462(
const char * layout_name ,/* <I>
                          Layout Name (UF_OBJ_NAME_NCHARS char max)
                          "" = Current Layout
                          */
const char * view_name ,/* <I>
                        View Name (UF_OBJ_NAME_NCHARS char max)
                        "" = Work View
                        */
double * border  /* <O>
                 View Borders On Layout (4 element array)
                 [0] Left Border
                 [1] Bottom Border
                 [2] Right Border
                 [3] Top Border
                 */
);

/***************************************************************************
Set view borders in a layout.  The borders argument is any two diagonal 
corners (X1,Y1,X2,Y2) of the view on the layout. The values range from 
0,0 (bottom-left corner of the layout) to 1,1 (top-right corner of the layout).

Return:
         Return Code
         0      = OK
         1      = View Does Not Exist
         2      = Invalid View Name
         3      = Cannot Modify View On Drawing
        10      = View Not On Layout
        11      = Layout Does Not Exist
        12      = Invalid Layout Name
        31      = Invalid View Border
        32      = Invalid Border Option

Environment: Internal  and  External

See Also:

History:
 ***************************************************************************/
extern UFUNEXPORT int uc6463(
const char * layout_name ,/* <I>
                          Layout Name (UF_OBJ_NAME_NCHARS char max)
                          "" = Current Layout
                          */
const char * view_name ,/* <I>
                        View Name (UF_OBJ_NAME_NCHARS char max)
                        "" = Work View
                        */
const int option ,/* <I>
                  Border Option
                  0 = Use View Borders In borders parameter
                  1 = Reserved For Future Use
                  */
const double * borders  /* <I>
                        View Borders On Layout (4 element array)
                        [0] Left Border
                        [1] Bottom Border
                        [2] Right Border
                        [3] Top Border
                        */
);

/***************************************************************************
Replace view in layout.  If the layout_name parameter is blank, the current 
layout is updated.  If the old_view_name parameter is blank, the work view is 
replaced. If the new_view_name parameter is blank, the view is duplicated on 
the layout. If both old_view_name and new_view_name are blank, the work
view is updated.  If the work view is replaced, the new view becomes 
the work view.

Return:
         Return Code
         0      = OK
         1      = View Does Not Exist
         2      = Invalid View Name
         4      = Can Not Replace View On Drawing
        10      = Old View Not In Layout
        11      = Layout Does Not Exist
        12      = Invalid Layout Name
        19      = Drafting Layout Not Valid
        23      = Current Drawing Contains Work View
        34      = A sketch view may not exist in a layout
                     more than one time.

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int uc6464(
const char * layout_name ,/* <I>
                          Layout Name (UF_OBJ_NAME_NCHARS char max)
                          "" = Current Layout
                          */
const char * old_view_name ,/* <I>
                            Old View Name (UF_OBJ_NAME_NCHARS char max)
                            "" = Work View
                            */
const char * new_view_name  /* <I>
                            New View Name (UF_OBJ_NAME_NCHARS char max)
                           "" = Work View
                            */
);

/****************************************************************************
Read current layout name and work view name.

Environment: Internal  and  External

See Also:

History:
 ****************************************************************************/
extern UFUNEXPORT int uc6466(
char cr1[ UF_OBJ_NAME_BUFSIZE ] ,/* <O>
            Layout Name 
            */
char cr2[ UF_OBJ_NAME_BUFSIZE ]  /* <O>
            Work View Name 
            */
);

/***************************************************************************
Save the current layout.  The new_name parameter is the name to use when you 
save the layout. If new_name is blank, the current layout name is used. A new
layout is created if new_name specifies a new name and a layout of
that name does not exist. An error is returned if new_name specifies a
new name and a layout with that name already exists.

Return:
         Return Code
         0 = OK
        12 = Invalid Layout Name
        14 = New Layout Already Exists

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int uc6467(
const char * new_name  /* <I>
                       Name To Save Layout (UF_OBJ_NAME_NCHARS char max)
                       "" = Use Current Name
                       */
);

/***************************************************************************
Retrieve a layout.  The view_scale parameter must be positive. In addition, 
you cannot retrieve a layout if all of its views were deleted.

Return:
         Return Code
         0 = OK
        11 = Layout Does Not Exist
        12 = Invalid Layout Name
        13 = Layout Has No Views
        31 = Invalid Scale
        32 = Invalid Scale Option
        35 = Operation Not Allowed In Drafting

Environment: Internal  and  External

See Also: 

History: 
 **************************************************************************/
extern UFUNEXPORT int uc6468(
const char * layout_name ,/* <I>
                          Layout Name (UF_OBJ_NAME_NCHARS char max)
                          */
const int option ,/* <I>
                  Scale Option
                  1 = Retrieve As Saved
                  2 = Fit All Views
                  3 = Apply view_scale To All Views
                  */
const double view_scale  /* <I>
                         View Scale  (If option=3)
                         */
);

/***************************************************************************
Delete a layout.  You cannot delete the current layout, any
canned layout, or the GFEM post layout.

Return:
         Return Code
         0 = OK
        11 = Layout Does Not Exist
        12 = Invalid Layout Name
        13 = Can Not Delete Canned Layout
        14 = Can Not Delete Current Layout
        15 = Can Not Delete GFEM Post Layout

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int uc6469(
const char * layout_name  /* <I>
                          Layout Name (UF_OBJ_NAME_NCHARS char max)
                          */
);

/***************************************************************************
Rename a layout.  If old_name is blank, the current layout is renamed. A 
canned layout cannot be renamed.

Return:
         Return Code
         0 = OK
        11 = Old Layout Does Not Exist
        12 = Invalid Layout Name
        13 = Can Not Rename Canned Layout
        14 = New Layout Already Exists

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int uc6470(
const char * old_name ,/* <I>
                       Old Layout Name (UF_OBJ_NAME_NCHARS char max)
                       "" = Current Layout
                       */
const char * new_name  /* <I>
                       New Layout Name (UF_OBJ_NAME_NCHARS char max)
                       */
);

/***************************************************************************
Cycle layouts in the work part.  This routine cycles the displayed part and 
returns one layout name per cycle. To start the cycle, set ca1 to the null 
string ("") before calling uc6471. The first layout name is returned in ca1. 
The next call returns the second layout name in ca1. When ca1 returns with a 
blank, all layout names have been returned.
NOTE: The cycle can continue even if the layout named in ca1 is
deleted during the cycle.

Return:
         Return Code
         0 = OK
        11 = Layout Does Not Exist
        12 = Invalid Layout Name

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int uc6471(
char ca1[ UF_OBJ_NAME_BUFSIZE ] /* <I/O>
            Layout Name 
            On input the last layout name found. "" will start cycling.  
            On output the next layout name found.  "" will be returned
            when the cycle is done.
            */
);

/***************************************************************************
Read the number of views in a layout.

Return:
         Return Code
         0 = OK
        11 = Layout Does Not Exist
        12 = Invalid Layout Name

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int uc6472(
const char * layout_name ,/* <I>
                          Layout Name (UF_OBJ_NAME_NCHARS char max)
                          "" = Current Layout
                          */
int * number_of_views  /* <O>
                       Number Of Views In Layout
                       */
);


/***************************************************************************
This routine cycles the layout and returns one view name per cycle. To
start the cycle, set ca2 to an empty string("") before calling uc6473. The 
first view name returns in ca2. The next call returns the second view name
in ca2. When ca2 returns with an empty string, all view names have been
returned.

Return:
         Return Code
         0 = OK
         1 = View Does Not Exist
         2 = Invalid View Name
        10 = View Not On Layout
        11 = Layout Does Not Exist
        12 = Invalid Layout Name

Environment: Internal  and  External

See Also:

History:
 **************************************************************************/
extern UFUNEXPORT int uc6473(
char * cp1 ,/* <I>
            Layout Name (UF_OBJ_NAME_NCHARS char max)
            "" = Current Layout
            */
char ca2[ UF_OBJ_NAME_BUFSIZE ] /* <I/O>
            View Name 
            On input the last view name found.  Pass in "" to start cycling.
            On output the next view name found, "" when the cycle is complete.
            */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif

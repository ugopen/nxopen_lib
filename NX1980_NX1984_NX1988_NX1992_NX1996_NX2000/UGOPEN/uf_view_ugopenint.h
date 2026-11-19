/******************************************************************************
             Copyright (c) 2000 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved



File Description:
     This is the Open API interface to Views and view operations that are
     only accessible in internal Open API applications.  This includes:

         . View Operations and Edits
             The routines in this section enable you to:
                 . Get the tag of an existing view that you specify by name.
                 . Get all of the visualization data.
                 . Retrieve the zoom scale of the specified view.
                 . Delete a view.
                 . Expand the current work view.
                 . Fit the geometry to the view by the specified fraction.
                 . Check the expand state of the work view.
                 . Translates the specified view to the specified center.
                 . Restore the specified view.
                 . Rotate the specified view using the view center.
                 . Rotate the specified view using abs.
                 . Set all of the visualization data.
                 . Unexpand the current work view.
                 . Update the display of the specified view.
                 . Scale the specified view.

         . View Dependent Edits
             The routines in this section enable you to:
                 . Erase an object from a view.
                 . Convert a view dependent object to model.
                 . Convert model object to view dependent.
                 . Remove the view dependent edits from an object.
                 . Convert all view dependent objects to model.
                 . Remove all view dependent edits from a view.
                 . Modify the color/font/width of a curve in a view.
                 . Return count of object view dependent edits.
                 . Return view dependent edit data for an object.
                 . Verify view dependent status for an object.

         . Views
             The routines in this section enable you to:
                 . Auto max/min view(s)
                 . Read/Set the view matrix
                 . Rotate the view point around the view center
                 . Read/Set view clipping planes
                 . Read/Set view perspective
                 . Read/Set view display type
                 . Read/Set view drawing parameters
                 . Read/Set surface/solid display parameters
                 . Read/Set view layer visibility masks
                 . Read work view name
                 . Change work view
                 . Save view
                 . Save all active views
                 . Delete/Rename a view
                 . Cycle views in a part
                 . Cycle objects in the view

     You can convert an object to a view dependent object with uc6402. This
     removes the object from the display in all other views. This object
     can be displayed in all the views by converting it back to a model object
     (uc6401, uc6404).

     As an alternative, you can edit the color/font/width of an object in a
     view. (The font can be made "invisible").  These edits do not remove the
     object from other views. An object may be edited differently in several
     views. This can be done with two routines: uc6406 and uc6400. uc6406 allows
     modification of parts of an object, while uc6400 erases the object from the
     view. If a view modification (color or width) is made to an object (uc6406)
     then that object is erased (uc6400). Modifying the font of that object to
     something other than invisible still keeps the original view modification.

     You may remove a view edit (modification) with two routines: uc6403 and
     uc6405. uc6403 removes all edits from an object in a view. uc6405 removes
     all edits for all objects in a given view.

     NOTE: Making an object view dependent (uc6402) is exclusive from view
           dependent edits (uc6400, uc6406). Both can be done on an object
           independent of each other.

     NOTE: In routines that state: "" = Work View, there are no spaces between
           the quotes.



*****************************************************************************/

#ifndef UF_VIEW_UGOPENINT_INCLUDED
#define UF_VIEW_UGOPENINT_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <libugopenint_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/******************************************************************************
Retrieves the zoom scale of the specified view. This is the value
displayed on the Zoom View menu which is the current scale at which
the view is displayed. If there are multiple occurrences of the view in
the layout, only one arbitrary occurrence is retrieved.
The view must be on the current layout. On a drawing layout, the view
must be a drawing view or a member work view.

Environment: Internal

See Also:

History:
 ******************************************************************************/
extern UGOPENINTEXPORT int UF_VIEW_ask_zoom_scale(
tag_t view_tag ,/* <I>
                The view tag; if NULL_TAG, work view is used
                */
double * scale  /* <O>
                The scale for the view
                */
);

/******************************************************************************
Scales the specified view by the specified scale factor. This is the same
as changing the scale on the Zoom View menu and does not trigger a
regen. If there are multiple occurrences of the view in the layout, then
only one arbitrary occurrence is affected.

The view must be on the current layout. On a drawing layout, the view
must be a drawing view or a member work view.

Environment: Internal

See Also:

History:
******************************************************************************/
extern UGOPENINTEXPORT int UF_VIEW_zoom_view(
tag_t view_tag ,/* <I>
                The view tag; if NULL_TAG, work view is used
                */
double  scale  /* <I>
               A positive absolute scale factor
               */
);

/******************************************************************************
Translates the specified view to the specified center. This has the
effect of changing the view origin with the View pull down menu and
does not trigger a regen. If there are multiple occurrences of the view
in the layout, only one arbitrary occurrence is translated.
The view must be on the current layout. On a drawing layout, the view
must be a drawing view or a member work view.

Environment: Internal

See Also:

History:
******************************************************************************/
extern UGOPENINTEXPORT int UF_VIEW_pan_view(
tag_t view_tag ,/* <I>
                The view tag; if NULL_TAG, work view is used
                */
double  center[3]  /* <I>
                   Coordinates in absolute space of the new center
                   */
);

/******************************************************************************
Rotates the specified view using the view center as the origin of
rotation and about the axis specified in the view space.

It does not trigger a regen. Negative angle means clockwise direction.
If there are multiple occurrences of the view in the layout, only one
arbitrary occurrence is rotated.  The view must be on the current layout.
The layout cannot be a layout with drawing.

Environment: Internal

See Also:

History:
******************************************************************************/
extern UGOPENINTEXPORT int UF_VIEW_rotate_view(
tag_t view_tag ,/* <I>
                The view tag; if NULL_TAG, the work view is used
                */
double  axis[3] ,/* <I>
                 X,Y,Z axis components in view space
                 */
double  delta_angle ,/* <I>
                     The angle in degrees
                     */
int  count  /* <I>
            The number of times to rotate
            */
);

/******************************************************************************
Rotate the specified view using the specified center as origin of
rotation and about the specified axis. The center and the axis are
specified in absolute coordinates. This is the similar to
UF_VIEW_rotate_view but the user can specify the center in absolute
coordinates and the axis is in absolute coordinates. It does not trigger
a regen. A negative angle means rotation in the clockwise direction. If
there are multiple occurrences of the view in the layout, only one
arbitrary occurrence is rotated.

The view must be on the current layout. The layout cannot be a layout
with drawing.

Environment: Internal

See Also:

History:
*****************************************************************************/
extern UGOPENINTEXPORT int UF_VIEW_rotate_view_abs_csys(
tag_t view_tag ,/* <I>
                The view tag; if NULL_TAG, the work view is used.
                */
double center[3] ,/* <I>
                  point in abs space
                  */
double axis[3] ,/* <I>
                X,Y,Z axis components in abs space
                */
double  delta_angle ,/* <I>
                     The angle in degrees
                     */
int  count  /* <I>
            The number of times to rotate
            */
);


/******************************************************************************
Fits the geometry to the view by the specified fraction. A 1.00 fraction
means all geometry is fitted to the whole view (There is a small
fraction for padding). A 0.50 fraction is approximately a 1.00 fraction
fit plus a half scale. This is equivalent to changing the percentage on
the Display Preferences menu and doing a fit except the value is
specified differently. If there are multiple occurrences of the view in
the layout, only one arbitrary occurrence is changed.

The view must be on the current layout. On a drawing layout, the view
must be a drawing view or a member work view.

Environment: Internal

See Also:

History:
 ******************************************************************************/
extern UGOPENINTEXPORT int UF_VIEW_fit_view(
tag_t view_tag ,/* <I>
                The view tag; if NULL_TAG, work view is used
                */
double fraction  /* <I>
                 The fraction of the view from 0.0 to 1.0
                 */
);
/******************************************************************************
Restores the specified view to the parameters (original scale,
translation, and rotation) that were in effect at either the last reset of
restore data, the last view regen, the last fit, or view save operation.
This is the same as the restore option on the View menu. If there is
nothing to restore, the function is ignored. If there are multiple
occurrences of the view in the layout, only one arbitrary occurrence is
restored.

The view must be on the current layout. On a drawing layout, the view
must be a drawing view or a member work view.

Environment: Internal

See Also:

History:
******************************************************************************/
extern UGOPENINTEXPORT int UF_VIEW_restore_view(
tag_t view_tag  /* <I>
                The view tag; if NULL_TAG, work view is used
                */
);

/******************************************************************************
Updates the display of the specified view  when losses in resolution
occur due to zooming or any incorrect operations that may affect the
display. This is the same as the update option on the View menu. If
there is nothing to update, the function is ignored. If there are
multiple occurrences of the view in the layout, then only one arbitrary
occurrence is updated. The view must be on the current layout.

Environment: Internal

See Also:

History:
 ******************************************************************************/
extern UGOPENINTEXPORT int UF_VIEW_update_view(
tag_t view_tag  /* <I>
                The view tag; if NULL_TAG, work view is used
                */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif

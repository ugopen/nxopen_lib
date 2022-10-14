/***********************************************************************************
 *                                                                                 *
 *        Copyright 2005 Siemens Product Lifecycle Management Software Inc.        *
 *                               All Rights Reserved.                              *
 *                                                                                 *
 *=================================================================================*



File Description:
     This is the Open API interface to Views and view operations.  This includes:

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
                 . Fit the view(s)
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

#ifndef UF_VIEW_INCLUDED
#define UF_VIEW_INCLUDED


/***************************************************************************

  ***************************************************************************/



/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_view_ugopenint.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/****************************************************************************
                       General UF_VIEW Definitions
  **************************************************************************/


enum UF_VIEW_smooth_edges_e{
   UF_VIEW_SMOOTH_EDGES_ON = 1,
   UF_VIEW_SMOOTH_EDGES_OFF };

typedef enum UF_VIEW_smooth_edges_e UF_VIEW_smooth_edges_t;


enum UF_VIEW_type_e{
   UF_VIEW_MODEL_TYPE = 0,
   UF_VIEW_DRAWING_MEMBER_TYPE,
   UF_VIEW_DRAWING_SHEET_TYPE };

typedef enum UF_VIEW_type_e UF_VIEW_type_t;


enum UF_VIEW_subtype_e{
   UF_VIEW_INVALID_SUBTYPE = -1,
   UF_VIEW_SECTION_SUBTYPE,
   UF_VIEW_IMPORTED_SUBTYPE,
   UF_VIEW_BASE_MEMBER_SUBTYPE,
   UF_VIEW_ORTHOGONAL_SUBTYPE,
   UF_VIEW_AUXILIARY_SUBTYPE,
   UF_VIEW_DETAIL_SUBTYPE,
   UF_VIEW_BREAK_SUBTYPE };

typedef enum UF_VIEW_subtype_e UF_VIEW_subtype_t;

enum UF_VIEW_vde_type_e
{
    UF_VIEW_VDE_NON_EDIT = -1,
    UF_VIEW_VDE_ALL,
    UF_VIEW_VDE_USER,
    UF_VIEW_VDE_SYSTEM
};
typedef enum UF_VIEW_vde_type_e UF_VIEW_vde_type_t, *UF_VIEW_vde_type_p_t;

/* These fields correspond to the options on the view visualization dialog.
   The values are string defined constants that are found in the uf_view.h and
   uf_obj.h header files
*/
struct UF_VIEW_visualization_s
{
    int          display_mode;     /* Display mode for the view.
                                      The following constants are valid :
                                          UF_VIEW_NOT_SHADED,
                                          UF_VIEW_PARTIALLY_SHADED,
                                          UF_VIEW_FULLY_SHADED and
                                          UF_VIEW_ANALYSIS_SHADED
                                   */
    int          hidden_edge_mode; /* Hidden edge style for the view
                                      The following constants are valid :
                                          UF_VIEW_HIDDEN_EDGES_SOLID,
                                          UF_VIEW_HIDDEN_EDGES_INVIS,
                                          UF_VIEW_HIDDEN_EDGES_DASHED,
                                          UF_VIEW_HIDDEN_SURFACE and
                                          UF_VIEW_HIDDEN_EDGES_GRAY_THIN
                                   */
    int          silhouette_mode;  /* Silhouettes flag (on or off) in the view
                                      The following constants are valid :
                                          UF_VIEW_SILHOUETTES_ON and
                                          UF_VIEW_SILHOUETTES_OFF
                                   */
    UF_VIEW_smooth_edges_t            smooth_edges_mode;
                                   /* Smooth edges flag (on or off) in the view
                                      The following constants are valid :
                                          UF_VIEW_SMOOTH_EDGES_ON and
                                          UF_VIEW_SMOOTH_EDGES_OFF
                                   */
    int           smooth_edge_color;/* Smooth edges color in the view
                                      The following values are valid :
                                          UF_OBJ_COLOR_ORIGINAL,
                                          [ 1 - 216 ]
                                   */
    int           smooth_edge_font; /* Smooth edges font in the view
                                      The following constants are valid :
                                          UF_OBJ_FONT_ORIGINAL,
                                          UF_OBJ_FONT_SOLID,
                                          UF_OBJ_FONT_DASHED,
                                          UF_OBJ_FONT_PHANTOM,
                                          UF_OBJ_FONT_CENTERLINE,
                                          UF_OBJ_FONT_DOTTED,
                                          UF_OBJ_FONT_LONG_DASHED and
                                          UF_OBJ_FONT_DOTTED_DASHED
                                   */
    int           smooth_edge_width;/* Smooth edges width in the view
                                      The following constants are valid :
                                          UF_OBJ_WIDTH_ORIGINAL,
                                          UF_OBJ_WIDTH_THIN,
                                          UF_OBJ_WIDTH_NORMAL and
                                          UF_OBJ_WIDTH_THICK
                                   */
    int          fog_mode;         /* Fog mode in view
                                      The following constants are valid :
                                          UF_VIEW_FOG_OFF,
                                          UF_VIEW_FOG_LINEAR,
                                          UF_VIEW_FOG_LIGHT and
                                          UF_VIEW_FOG_HEAVY
                                   */
    double       fog_color[3];     /* Fog color
                                      [0] = red,
                                      [1] = green,
                                      [2] = blue

                                      Each color has a range from 0.0 to 1.0.
                                   */
    double       fog_front;        /* Front fog plane has a range from 0 to 100
                                      and is only valid for
                                      fog_mode = UF_VIEW_FOG_LINEAR
                                   */
    double       fog_back;         /* Back fog plane has a range from 0 to 100
                                      and is only valid for
                                      fog_mode = UF_VIEW_FOG_LINEAR.
                                   */
    double       fog_rate;         /* The fog density which has a range from 0
                                      to 100. This setting is only valid when
                                      the fog_mode is set to
                                      UF_VIEW_FOG_LIGHT or UF_VIEW_FOG_HEAVY.
                                   */
};

typedef struct UF_VIEW_visualization_s UF_VIEW_visualization_t;


/*******************************************************************************
   V12:  Note in V12 Light settings are no longer
   part of the system parameters.  Lights are now part
   of view attributes.  Each view may have different
   lights assigned to it.  New Open API routines have
   been written to support reading and setting of
   these attributes.  They are UF_VIEW_ask_view_light
   and UF_VIEW_set_view_light.
   light_source_angles in UF_DISP_system_params_t are removed.
   The following defines the typedefs and structures required
   for the new lighting routines.
*******************************************************************************/

#define UF_VIEW_MAX_VIEW_LIGHTS  8
#define UF_VIEW_MIN_VIEW_LIGHTS  0
#define UF_VIEW_MAX_LIGHT_NAME_LENGTH 40
#define UF_VIEW_MAX_SHININESS  1.0
#define UF_VIEW_MIN_SHININESS  0.0

enum UF_VIEW_two_sided_e{
   UF_VIEW_TWO_SIDED_OFF,
   UF_VIEW_TWO_SIDED_ON };

typedef enum UF_VIEW_two_sided_e UF_VIEW_two_sided_t;


enum UF_VIEW_light_mode_e{
   UF_VIEW_FIXED_TO_OBSERVER,
   UF_VIEW_FIXED_TO_THE_PART};

typedef enum UF_VIEW_light_mode_e UF_VIEW_light_mode_t;


enum UF_VIEW_light_type_e{
   UF_VIEW_AMBIENT_LIGHT,
   UF_VIEW_DISTANT_LIGHT,
   UF_VIEW_EYE_LIGHT,
   UF_VIEW_POINT_LIGHT,
   UF_VIEW_SPOT_LIGHT,
   UF_VIEW_NUM_LIGHT_TYPES};

typedef enum UF_VIEW_light_type_e UF_VIEW_light_type_t;

enum UF_VIEW_light_intensity_factor_e{
   UF_VIEW_INTENSITY_FACTOR_NONE,
   UF_VIEW_INTENSITY_FACTOR_10X,
   UF_VIEW_INTENSITY_FACTOR_100X,
   UF_VIEW_INTENSITY_FACTOR_1000X,
   UF_VIEW_NUM_INTENSITY_FACTOR};

typedef enum UF_VIEW_light_intensity_factor_e UF_VIEW_light_intensity_factor_t;

enum UF_VIEW_light_fall_off_e{
   UF_VIEW_FALL_OFF_CONSTANT,
   UF_VIEW_FALL_OFF_INVERSE_LINEAR,
   UF_VIEW_FALL_OFF_INVERSE_SQUARE,
   UF_VIEW_FALL_OFF_CONSTANT_INVERSE_LINEAR,
   UF_VIEW_FALL_OFF_CONSTANT_INVERSE_SQUARE,
   UF_VIEW_NUM_FALL_OFF};

typedef enum UF_VIEW_light_fall_off_e UF_VIEW_light_fall_off_t;

enum UF_VIEW_light_beam_fall_off_e{
   UF_VIEW_BEAM_FALL_OFF_NONE,
   UF_VIEW_BEAM_FALL_OFF_GRADUAL,
   UF_VIEW_BEAM_FALL_OFF_RAPID,
   UF_VIEW_NUM_BEAM_FALL_OFF};

typedef enum UF_VIEW_light_beam_fall_off_e UF_VIEW_light_beam_fall_off_t;

enum UF_VIEW_light_detail_e{
   UF_VIEW_DETAIL_COARSE,
   UF_VIEW_DETAIL_STANDARD,
   UF_VIEW_DETAIL_FINE,
   UF_VIEW_DETAIL_EXTRA_FINE,
   UF_VIEW_DETAIL_RAY_TRACED,
   UF_VIEW_NUM_DETAIL};

typedef enum UF_VIEW_light_detail_e UF_VIEW_light_detail_t;

enum UF_VIEW_light_edge_e{
   UF_VIEW_EDGE_HARD,
   UF_VIEW_EDGE_SOFT,
   UF_VIEW_EDGE_EXTRA_SOFT,
   UF_VIEW_EDGE_ULTRA_SOFT,
   UF_VIEW_NUM_EDGE};

typedef enum UF_VIEW_light_edge_e UF_VIEW_light_edge_t;

typedef char UF_VIEW_light_name_t[UF_VIEW_MAX_LIGHT_NAME_LENGTH];

typedef double UF_VIEW_light_source_t[3];


/*******************************************************************************
   The structure UF_VIEW_light_t below is used to define
   the light attributes.

   For fixed to the part light, the direction is Work Coordinate System based.
   For fixed to observer, the direction of light is based on screen space
   (which is defined as +x to the right, +y up and +z out of the screen).
 ******************************************************************************/
struct UF_VIEW_lights_s
{
  UF_VIEW_light_name_t light_name; /* Light name which is limited to 40
                                      characters. Can be either canned or
                                      user defined */
  UF_VIEW_light_type_t light_type; /* Lights may be of different types as
                                      defined in
 UF_VIEW_light_type_t
 */
  UF_VIEW_light_mode_t light_mode; /* Specifies whether the light is fixed to
                                      the observer or fixed to the part.  If
                                      fixed to the part, the light direction
                                      is based on the WCS.  For fixed to the
                                      observer, the direction of the light is
                                      based on the screen space (which is
                                      defined as +x to the right, +y up and
                                      +z out of the screen. */
  UF_VIEW_light_source_t location; /* Together with 'to', determines the
                                      direction of the light. */
  UF_VIEW_light_source_t to;       /* Together with 'location', determines the
                                      direction of the light. */
};

typedef struct UF_VIEW_lights_s  UF_VIEW_light_t,
                                *UF_VIEW_light_p_t;

/*******************************************************************************
   The structure UF_VIEW_light_attributes_t below is used to define
   the light attributes.
  ******************************************************************************/
struct UF_VIEW_light_attributes_s
{
    int red;   /* Amount of red color to put in the light. Must be one of the following values [0-255] */
    int green; /* Amount of green color to put in the light. Must be one of the following values [0-255] */
    int blue;  /* Amount of blue color to put in the light. Must be one of the following values [0-255] */
    double intensity; /* Intensity of light. Must be in the range from 0.0 to 1.0 */
    UF_VIEW_light_intensity_factor_t intensity_factor;  /* Intensity factor of light.
                                                           Only used for point light and spot light.
                                                           Only used when not constant fall off.
                                                           Settings are defined in
                                                            UF_VIEW_light_intensity_factor_t
                                                        */
    UF_VIEW_light_fall_off_t fall_off;  /* Fall off setting of light.
                                           Only used for point light and spot light.
                                           Settings are defined in
                                            UF_VIEW_light_fall_off_t
                                        */
    double cone_angle; /* Value of cone angle for spot light. Must be between 0.0 and 180.0. */
    double delta_angle; /* Value of delta angle for spot light. Must be between 0.0 and 180.0. */
    UF_VIEW_light_beam_fall_off_t beam_fall_off; /* Beam fall for spot light.
                                                    Settings are defined in
                                                     UF_VIEW_light_beam_fall_off_t
                                                 */
    logical scattering;  /* Spot light should use scattering or not. true if light is to use
                            scattering, false if not. */

    logical generate_shadows;  /* Light should generate shadows or not. true if light is to
                                  generate shadows, false if not. Not used if ambient light or
                                  eye light.
                               */
    UF_VIEW_light_detail_t detail; /* Detail setting for light. Not used if ambient light or
                                      eye light. Settings are defined in
                                       UF_VIEW_light_detail_t
                                   */

    UF_VIEW_light_edge_t edge; /* Edge setting for light. Not used if ambient light or
                                  eye light. Settings are defined in
                                   UF_VIEW_light_edge_t
                               */

};

typedef struct UF_VIEW_light_attributes_s  UF_VIEW_light_attributes_t,
                                *UF_VIEW_light_attributes_p_t;

/*******************************************************************************
   Each view is allowed a maximum of 8 lights.  Each view could have different
   shininess factor( ranging from 0.0(UF_VIEW_MIN_SHININESS) to
   1.0(UF_VIEW_MAX_SHININESS).  Each view could have lights two-sided or
   not(UF_VIEW_two_sided_t).  Two sided lighting is useful for entities such
   as sheet bodies to make sure both side of sheet bodies are lit correctly.
   The structure UF_VIEW_lighting_t below is used to define lighting for
   each view:
*******************************************************************************/
struct UF_VIEW_lighting_s
{
    int two_sided_light;  /* The valid values are :
                                 UF_VIEW_TWO_SIDED_OFF and
                                 UF_VIEW_TWO_SIDED_ON
                          */
    double shininess;     /* Shininess factor (range is from 0.0 - 1.0) */
    int light_count;      /* Total number of lights not to exceed a count of
                             8 lights. */
    UF_VIEW_light_t lights[UF_VIEW_MAX_VIEW_LIGHTS];
};

typedef struct UF_VIEW_lighting_s  UF_VIEW_lighting_t,
                                  *UF_VIEW_lighting_p_t;

/*
 This structure contains the view dependent edit data for an object.
*/
struct UF_VIEW_vde_data_s
{
        tag_t       view_tag;         /* View of modification */
        double      start_parameter;  /* Starting parameter of this
                                         modification (0.0 - 1.0) */
        double      end_parameter;    /* Ending parameter of this
                                         modification (0.0 - 1.0) */
        int         color;            /* Color of modification (see uf_obj.h
                                         for possible values ) */
        int         font;             /* Font of modification
                                         (see uf_obj.h for possible values ) */
        int         width;            /* Width of modification
                                         (see uf_obj.h for possible values ) */
};

typedef struct UF_VIEW_vde_data_s UF_VIEW_vde_data_t, *UF_VIEW_vde_data_p_t;

/* This structure contains the view dependent edit data and type for an object */
struct UF_VIEW_vde_data_and_type_s
{
    tag_t       view_tag;         /* View of modification */
    double      start_parameter;  /* Starting parameter of this
                                     modification (0.0 - 1.0) */
    double      end_parameter;    /* Ending parameter of this
                                     modification (0.0 - 1.0) */
    int         color;            /* Color of modification (see uf_obj.h
                                     for possible values ) */
    int         font;             /* Font of modification
                                     (see uf_obj.h for possible values ) */
    int         width;            /* Width of modification
                                     (see uf_obj.h for possible values ) */
    UF_VIEW_vde_type_t vde_type;  /* Type of modification */
};
typedef struct UF_VIEW_vde_data_and_type_s UF_VIEW_vde_data_and_type_t, *UF_VIEW_vde_data_and_type_p_t;

enum UF_VIEW_cycle_objects_e
{
    UF_VIEW_VISIBLE_OBJECTS = 1,
    UF_VIEW_DEPENDENT_OBJECTS,
    UF_VIEW_ERASED_OBJECTS,
    UF_VIEW_MODIFIED_OBJECTS
};
typedef enum UF_VIEW_cycle_objects_e UF_VIEW_cycle_objects_t, *UF_VIEW_cycle_objects_p_t;


enum UF_VIEW_standard_orientation_e {
    UF_VIEW_STANDARD_ORIENTATION_NONE = -1,
    UF_VIEW_STANDARD_ORIENTATION_TOP,
    UF_VIEW_STANDARD_ORIENTATION_FRONT,
    UF_VIEW_STANDARD_ORIENTATION_RIGHT,
    UF_VIEW_STANDARD_ORIENTATION_BACK,
    UF_VIEW_STANDARD_ORIENTATION_BOTTOM,
    UF_VIEW_STANDARD_ORIENTATION_LEFT,
    UF_VIEW_STANDARD_ORIENTATION_ISOMETRIC,
    UF_VIEW_STANDARD_ORIENTATION_TRIMETRIC,
    UF_VIEW_STANDARD_ORIENTATION_DIMETRIC,
    UF_VIEW_STANDARD_ORIENTATION_NUM_TYPES
};
typedef enum UF_VIEW_standard_orientation_e UF_VIEW_standard_orientation_t, *UF_VIEW_standard_orientation_p_t;


/* #define UF_VIEW_NO_CHANGE           (0)  **obsolete**  */

#define UF_VIEW_NOT_SHADED             (1)
#define UF_VIEW_PARTIALLY_SHADED       (2)
#define UF_VIEW_FULLY_SHADED           (3)
#define UF_VIEW_ANALYSIS_SHADED        (4)
#define UF_VIEW_STUDIO_SHADED          (5)

#define UF_VIEW_HIDDEN_EDGES_SOLID     (1)
#define UF_VIEW_HIDDEN_EDGES_INVIS     (2)
#define UF_VIEW_HIDDEN_EDGES_DASHED    (3)
#define UF_VIEW_HIDDEN_SURFACE         (4)
#define UF_VIEW_HIDDEN_EDGES_GRAY_THIN (5)

#define UF_VIEW_DEPTH_CUE_OFF          (1)
#define UF_VIEW_DEPTH_CUE_ON           (2)

/* Fog Modes */
#define UF_VIEW_FOG_OFF                (1)
#define UF_VIEW_FOG_LINEAR             (2)
#define UF_VIEW_FOG_HEAVY              (3)
#define UF_VIEW_FOG_LIGHT              (4)

/* Fog ranges */
#define UF_VIEW_FOG_MIN_RATE           (0.)
#define UF_VIEW_FOG_MAX_RATE           (100.)
#define UF_VIEW_FOG_MIN_BOUND          (0.)
#define UF_VIEW_FOG_MAX_BOUND          (100.)

#define UF_VIEW_SILHOUETTES_ON         (1)
#define UF_VIEW_SILHOUETTES_OFF        (2)


/*******************************************************************************

Type UF_VIEW_rendering_style_t enumerates rendering styles supported
for a view of type UF_VIEW_MODEL_TYPE.

Function
 UF_VIEW_ask_surface_display_options
returns the rendering style of a view, and function
 UF_VIEW_set_surface_display_options
modifies the rendering style of a view.

*******************************************************************************/

enum UF_VIEW_rendering_style_e
{
    UF_VIEW_SHADED_STYLE,
    UF_VIEW_WIREFRAME_STYLE,
    UF_VIEW_STUDIO_STYLE,
    UF_VIEW_FACE_ANALYSIS_STYLE,
    UF_VIEW_PARTIALLY_SHADED_STYLE,
    UF_VIEW_STATIC_WIREFRAME_STYLE
};

typedef enum UF_VIEW_rendering_style_e
             UF_VIEW_rendering_style_t,
            *UF_VIEW_rendering_style_p_t;


/*******************************************************************************

Type UF_VIEW_shaded_edge_style_t enumerates choices for display of
shaded face edges in a view of type UF_VIEW_MODEL_TYPE.

*******************************************************************************/

enum UF_VIEW_shaded_edge_style_e
{
    UF_VIEW_SHADED_EDGE_STYLE_SHADED_EDGE_COLOR = 0,
    UF_VIEW_SHADED_EDGE_STYLE_BODY_COLOR = 1,
    UF_VIEW_SHADED_EDGE_STYLE_OFF = 2
};

typedef enum UF_VIEW_shaded_edge_style_e
             UF_VIEW_shaded_edge_style_t,
            *UF_VIEW_shaded_edge_style_p_t;


/*******************************************************************************

Type UF_VIEW_hidden_edge_style_t enumerates choices for display
of hidden shaded face edges in a view of type UF_VIEW_MODEL_TYPE.

*******************************************************************************/

enum UF_VIEW_hidden_edge_style_e
{
    UF_VIEW_HIDDEN_EDGE_STYLE_INVISIBLE = 0,
    UF_VIEW_HIDDEN_EDGE_STYLE_HIDDEN_GEOMETRY_COLOR = 1,
    UF_VIEW_HIDDEN_EDGE_STYLE_DASHED_IN_BODY_COLOR = 2
};

typedef enum UF_VIEW_hidden_edge_style_e
             UF_VIEW_hidden_edge_style_t,
            *UF_VIEW_hidden_edge_style_p_t;


/*******************************************************************************

Structure UF_VIEW_shaded_edge_options_t specifies options that
control the display of edges of shaded faces in a view of type
UF_VIEW_MODEL_TYPE.

Function
 UF_VIEW_ask_shaded_edge_options
returns the shaded edge options of a view, and function
 UF_VIEW_set_shaded_edge_options
modifies the shaded edge options of a view.

See Also:
 UF_VIEW_shaded_edge_style_t
 UF_VIEW_hidden_edge_style_t

*******************************************************************************/

struct UF_VIEW_shaded_edge_options_s
{
    UF_VIEW_shaded_edge_style_t    shaded_edge_style;
    int                            shaded_edge_color;
    UF_VIEW_hidden_edge_style_t    hidden_edge_style;
};

typedef struct UF_VIEW_shaded_edge_options_s
               UF_VIEW_shaded_edge_options_t,
              *UF_VIEW_shaded_edge_options_p_t;


/*******************************************************************************

Structure UF_VIEW_fog_options_t specifies options that control the
application of fog in a view of type UF_VIEW_MODEL_TYPE.

Function
 UF_VIEW_ask_fog_options
returns the fog options of a view, and function
 UF_VIEW_set_fog_options
modifies the fog options of a view.

*******************************************************************************/

struct UF_VIEW_fog_options_s
{
    int          fog_mode;         /* Fog mode in view
                                      The following constants are valid :
                                          UF_VIEW_FOG_OFF,
                                          UF_VIEW_FOG_LINEAR,
                                          UF_VIEW_FOG_LIGHT and
                                          UF_VIEW_FOG_HEAVY
                                   */
    double       fog_color[3];     /* Fog color
                                      [0] = red,
                                      [1] = green,
                                      [2] = blue

                                      Each color has a range from 0.0 to 1.0.
                                   */
    double       fog_front;        /* Front fog plane has a range from 0 to 100
                                      and is only valid for
                                      fog_mode = UF_VIEW_FOG_LINEAR
                                   */
    double       fog_back;         /* Back fog plane has a range from 0 to 100
                                      and is only valid for
                                      fog_mode = UF_VIEW_FOG_LINEAR.
                                   */
    double       fog_rate;         /* The fog density which has a range from 0
                                      to 100. This setting is only valid when
                                      the fog_mode is set to
                                      UF_VIEW_FOG_LIGHT or UF_VIEW_FOG_HEAVY.
                                   */
};

typedef struct UF_VIEW_fog_options_s
               UF_VIEW_fog_options_t,
              *UF_VIEW_fog_options_p_t;


/*******************************************************************************

Structure UF_VIEW_edge_display_options_t specifies options that
control the display of hidden edges, silhouettes, and smooth edges
in a view of type UF_VIEW_MODEL_TYPE.

Function
 UF_VIEW_ask_surface_display_options
returns the edge display options of a view, and function
 UF_VIEW_set_surface_display_options
modifies the edge display options of a view.

See Also:
 UF_VIEW_smooth_edges_t

*******************************************************************************/

struct UF_VIEW_edge_display_options_s
{
    int          hidden_edge_mode; /* Hidden edge style for the view
                                      The following constants are valid :
                                          UF_VIEW_HIDDEN_EDGES_SOLID,
                                          UF_VIEW_HIDDEN_EDGES_INVIS,
                                          UF_VIEW_HIDDEN_EDGES_DASHED,
                                          UF_VIEW_HIDDEN_EDGES_GRAY_THIN
                                   */
    int          silhouette_mode;  /* Silhouettes flag (on or off) in the view
                                      The following constants are valid :
                                          UF_VIEW_SILHOUETTES_ON and
                                          UF_VIEW_SILHOUETTES_OFF
                                   */
    UF_VIEW_smooth_edges_t       smooth_edges_mode;
                                   /* Smooth edges flag (on or off) in the view
                                      The following constants are valid :
                                          UF_VIEW_SMOOTH_EDGES_ON and
                                          UF_VIEW_SMOOTH_EDGES_OFF
                                   */
    int          smooth_edge_color;/* Smooth edges color in the view
                                      The following values are valid :
                                          UF_OBJ_COLOR_ORIGINAL,
                                          [ 1 - 216 ]
                                   */
    int          smooth_edge_font; /* Smooth edges font in the view
                                      The following constants are valid :
                                          UF_OBJ_FONT_ORIGINAL,
                                          UF_OBJ_FONT_SOLID,
                                          UF_OBJ_FONT_DASHED,
                                          UF_OBJ_FONT_PHANTOM,
                                          UF_OBJ_FONT_CENTERLINE,
                                          UF_OBJ_FONT_DOTTED,
                                          UF_OBJ_FONT_LONG_DASHED and
                                          UF_OBJ_FONT_DOTTED_DASHED
                                   */
    int          smooth_edge_width;/* Smooth edges width in the view
                                      The following constants are valid :
                                          UF_OBJ_WIDTH_ORIGINAL,
                                          UF_OBJ_WIDTH_THIN,
                                          UF_OBJ_WIDTH_NORMAL and
                                          UF_OBJ_WIDTH_THICK
                                   */
};

typedef struct UF_VIEW_edge_display_options_s
               UF_VIEW_edge_display_options_t,
              *UF_VIEW_edge_display_options_p_t;


/****************************************************************************
 * Constants for error codes
  ***************************************************************************/

#define ERROR_UF_VIEW_base     1170000

/* The input view is not in the current layout                  */
#define UF_VIEW_ERR_VIEW_NOT_IN_LAYOUT       (ERROR_UF_VIEW_base + 0)

/* Function requires an active layout                           */
#define UF_VIEW_ERR_NO_ACTIVE_LAYOUT         (ERROR_UF_VIEW_base + 1)

/* No view exists with that name                                */
#define UF_VIEW_ERR_NO_SUCH_VIEW_NAME        (ERROR_UF_VIEW_base + 2)

/* The current layout is a drawing                              */
#define UF_VIEW_ERR_LAYOUT_IS_DRAWING        (ERROR_UF_VIEW_base + 3)

/* This is a drafting drawing but view is not a work view       */
#define UF_VIEW_ERR_ON_DRAWING_NOT_WORK_VIEW (ERROR_UF_VIEW_base + 4)

/* This display mode element of the structure is out of range   */
#define UF_VIEW_INVALID_DISPLAY_MODE         (ERROR_UF_VIEW_base + 5)

/* The hidden edge mode element of the struct is out of range   */
#define UF_VIEW_INVALID_HIDDEN_MODE          (ERROR_UF_VIEW_base + 6)

/* The silhouette element of the structure is out of range      */
#define UF_VIEW_INVALID_SILHOU_MODE          (ERROR_UF_VIEW_base + 7)

/* The smooth edge element of the structure is out of range     */
#define UF_VIEW_INVALID_SMOOTH_MODE          (ERROR_UF_VIEW_base + 8)

/* The depth cue mode element of the struct is out of range     */
#define UF_VIEW_INVALID_DEPTH_CUE_MODE       (ERROR_UF_VIEW_base + 9)

/* The fog mode element of the struct is out of range     */
#define UF_VIEW_FOG_UNSUPPORTED              (ERROR_UF_VIEW_base + 9)

/* Hardware shading is unsupported on the device                */
#define UF_VIEW_GOURAUD_UNSUPPORTED          (ERROR_UF_VIEW_base + 10)

/* Hidden Surface is unsupported on the device                  */
#define UF_VIEW_HIDDEN_SURF_UNSUPPORTED      (ERROR_UF_VIEW_base + 11)

/* Depth Cueing is unsupported on the device                    */
#define UF_VIEW_DEPTH_CUE_UNSUPPORTED        (ERROR_UF_VIEW_base + 12)

/* The view tag supplied is invalid for this operation          */
#define UF_VIEW_INVALID_VIEW_TAG             (ERROR_UF_VIEW_base + 13)

/* A drafting view is invalid for the specified operation       */
#define UF_VIEW_DRAFTING_VIEW_INVALID        (ERROR_UF_VIEW_base + 14)

/* The work view was not found in the current part (if exists)  */
#define UF_VIEW_NO_WORK_VIEW                 (ERROR_UF_VIEW_base + 15)

/* A null string was given as a view name where not allowed     */
#define UF_VIEW_ERR_NULL_VIEW_NAME           (ERROR_UF_VIEW_base + 16)

/* A view name has more than UF_OBJ_NAME_LEN characters         */
#define UF_VIEW_ERR_VIEW_NAME_TOO_LONG       (ERROR_UF_VIEW_base + 17)

/* A view name contains characters not allowed in view names    */
#define UF_VIEW_ERR_BAD_CHARS_IN_NAME        (ERROR_UF_VIEW_base + 18)

/* Trying to copy or save to a view which already exists        */
#define UF_VIEW_ERR_VIEW_ALREADY_EXISTS      (ERROR_UF_VIEW_base + 19)



/* lighting error code */


/* The two_sided_light element of the lighting struct is out of range */
#define UF_VIEW_INVALID_TWO_SIDED_LIGHT      (ERROR_UF_VIEW_base + 20)

/* The shininess element of the lighting struct is out of range */
#define UF_VIEW_INVALID_SHININESS            (ERROR_UF_VIEW_base + 21)

/* The light name element of the lighting struct is out of range*/
#define UF_VIEW_INVALID_LIGHT_NAME           (ERROR_UF_VIEW_base + 22)

/* The light type element of the lighting struct is out of range*/
#define UF_VIEW_INVALID_LIGHT_TYPE           (ERROR_UF_VIEW_base + 23)

/* The light type element of the lighting struct is out of range*/
#define UF_VIEW_INVALID_LIGHT_COUNT            (ERROR_UF_VIEW_base + 24)

/* The light type element of the lighting struct is out of range*/
#define UF_VIEW_INVALID_LIGHT_MODE             (ERROR_UF_VIEW_base + 25)



/*                 -- View Clipping Error Codes --              */


/* Curve type specified was invalid (see UF_VIEW_curve_type_e)  */
#define UF_VIEW_INVALID_CURVE_TYPE             (ERROR_UF_VIEW_base + 26)

/* The arc center was invalid                                   */
#define UF_VIEW_INVALID_ARC_CENTER             (ERROR_UF_VIEW_base + 27)

/* The arc radius was invalid (must be > .005)                  */
#define UF_VIEW_INVALID_ARC_RADIUS             (ERROR_UF_VIEW_base + 28)

/* The arc angles were invalid (start_angle must be less than end_angle) */
#define UF_VIEW_INVALID_ARC_ANGLES             (ERROR_UF_VIEW_base + 29)

/* The polyline definition was invalid (num_vertices or array was invalid) */
#define UF_VIEW_INVALID_POLYLINE_DEFINITION    (ERROR_UF_VIEW_base + 30)

/* Coincident polyline points found when there should not be any */
#define UF_VIEW_COINCIDENT_POLYLINE_POINTS     (ERROR_UF_VIEW_base + 31)

/* Point definition was invalid                                  */
#define UF_VIEW_INVALID_POINT_DEFINITION       (ERROR_UF_VIEW_base + 32)

/* The view passed is not a break line view.                     */
#define UF_VIEW_NON_BREAK_LINE_VIEW            (ERROR_UF_VIEW_base + 33)

/* An unknown error occurred while clipping the curve to the view*/
#define UF_VIEW_ERROR_CLIPPING                 (ERROR_UF_VIEW_base + 34)

/* UF_VIEW_begin_view_clipping was not called                    */
#define UF_VIEW_NOT_READY_FOR_CLIPPING         (ERROR_UF_VIEW_base + 35)

/* View information structure invalid - passed wrong view info ptr. */
#define UF_VIEW_VIEW_INFORMATION_INVALID       (ERROR_UF_VIEW_base + 36)

/* NULL TAG. */
#define UF_VIEW_PARAMETER_IS_NULL_TAG          (ERROR_UF_VIEW_base + 37)

/* NULL POINTER. */
#define UF_VIEW_PARAMETER_IS_NULL_POINTER      (ERROR_UF_VIEW_base + 38)

/* NON-POSITIVE PARAMETER. */
#define UF_VIEW_PARAMETER_IS_NOT_POSITIVE      (ERROR_UF_VIEW_base + 39)

/* OBJECT HAS FEWER VDE RECORDS THAN INPUT RECORD PARAMETER. */
#define UF_VIEW_TOO_FEW_VDE_RECORDS            (ERROR_UF_VIEW_base + 40)

/* OBJECT IS NOT A QUALIFIED ONE. */
#define UF_VIEW_INVALID_OBJECT                 (ERROR_UF_VIEW_base + 41)

/* The smooth edge color element of the structure is out of range     */
#define UF_VIEW_INVALID_SMOOTH_COLOR           (ERROR_UF_VIEW_base + 42)

/* The smooth edge font element of the structure is out of range     */
#define UF_VIEW_INVALID_SMOOTH_FONT            (ERROR_UF_VIEW_base + 43)

/* The smooth edge width element of the structure is out of range     */
#define UF_VIEW_INVALID_SMOOTH_WIDTH           (ERROR_UF_VIEW_base + 44)

/* The fog color element of the structure is out of range     */
#define UF_VIEW_INVALID_FOG_COLOR              (ERROR_UF_VIEW_base + 45)

/* The fog color of the struct is not supported     */
#define UF_VIEW_FOG_COLOR_UNSUPPORTED          (ERROR_UF_VIEW_base + 46)

/* The fog start plane element of the structure is out of range     */
#define UF_VIEW_INVALID_FOG_FRONT              (ERROR_UF_VIEW_base + 47)

/* The fog end plane element of the structure is out of range     */
#define UF_VIEW_INVALID_FOG_BACK               (ERROR_UF_VIEW_base + 48)

/* The fog start/end plane of the struct is not supported     */
#define UF_VIEW_FOG_BOUNDS_UNSUPPORTED         (ERROR_UF_VIEW_base + 49)

/* The fog density element of the structure is out of range     */
#define UF_VIEW_INVALID_FOG_RATE               (ERROR_UF_VIEW_base + 50)

/* The fog density element of the structure is not supported     */
#define UF_VIEW_FOG_RATE_UNSUPPORTED           (ERROR_UF_VIEW_base + 51)

/* Additional error codes for UF_VIEW_rename */
#define UF_VIEW_INVALID_NAME                   (ERROR_UF_VIEW_base + 52)
#define UF_VIEW_CANNOT_RENAME_CANNED           (ERROR_UF_VIEW_base + 53)
#define UF_VIEW_CANNOT_RENAME_DRAWING          (ERROR_UF_VIEW_base + 54)
#define UF_VIEW_CANNOT_RENAME_SKETCH           (ERROR_UF_VIEW_base + 55)

#define UF_VIEW_IS_NOT_DISPLAYED               (ERROR_UF_VIEW_base + 56)

#define UF_VIEW_NO_DISPLAYED_PART              (ERROR_UF_VIEW_base + 57)

#define UF_VIEW_NOT_IN_DISPLAYED_PART          (ERROR_UF_VIEW_base + 58)

#define UF_VIEW_INVALID_ORIENTATION_TYPE       (ERROR_UF_VIEW_base + 59)
#define UF_VIEW_CONFLICT_ORIENTATION_TYPE      (ERROR_UF_VIEW_base + 60)

#define UF_VIEW_INVALID_RENDERING_STYLE        (ERROR_UF_VIEW_base + 61)
#define UF_VIEW_INVALID_SHADED_EDGE_STYLE      (ERROR_UF_VIEW_base + 62)
#define UF_VIEW_INVALID_SHADED_EDGE_COLOR      (ERROR_UF_VIEW_base + 63)
#define UF_VIEW_INVALID_HIDDEN_EDGE_STYLE      (ERROR_UF_VIEW_base + 64)


/****************************************************************************
Gets all of the visualization data. If you pass a NULL_TAG to the
view argument, then the work view is used.

Please use
 UF_VIEW_ask_surface_display_options
and
 UF_VIEW_ask_fog_options
instead.

Environment: Internal  and  External

See Also:
 UF_VIEW_visualization_t

History: In the V15.0 release, new fields were added to the
         UF_VIEW_visualization_t data structure.
         In NX4.0, this function is superceded by
         UF_VIEW_ask_surface_display_options and UF_VIEW_ask_fog_options.

 ******************************************************************************/
extern UFUNEXPORT int UF_VIEW_ask_visualization(
tag_t view ,/* <I>
            View to retrieve data on
            */
UF_VIEW_visualization_t * view_data  /* <O>
                                     View visualization data
                                     */
);

/****************************************************************************
Sets all of the visualization data. If you pass a NULL_TAG to the view
argument, then the work view is used.  This is not intended to work
for drawing member views.  For drawing member views use UF_DRAW_set_view_display

Please use
 UF_VIEW_set_surface_display_options
and
 UF_VIEW_set_fog_options
instead.

Environment: Internal  and  External

See Also:
 UF_DRAW_set_view_display



History:In the V15.0 release, new fields were added to the
        UF_VIEW_visualization_s data structure.
        In NX4.0, this function is superceded by
        UF_VIEW_set_surface_display_options and UF_VIEW_set_fog_options.
 ****************************************************************************/
extern UFUNEXPORT int UF_VIEW_set_visualization(
tag_t view ,/* <I>
            View to set data for
            */
UF_VIEW_visualization_t * view_data  /* <I>
                                     View visualization data
                                     */
);

/****************************************************************************
Returns the X and Y clip boundaries of the given view.  The clip
boundaries define a rectangle on the Z = 0 plane of View Space.

This function is primarily intended for use by specialized
applications such as Translators. Please note the following:
The clip boundaries returned are those saved in the data base for
the view. If the view is in the current layout, has been changed in
the layout (by, for example, a Zoom), and has not been saved since
it was changed, then the clip boundaries returned by this function
do NOT reflect the changes.

If this is not what you need, consider using uc6431 (Read View
Center and Scale), which returns the current data for the view in
the layout, if it is in the layout, or otherwise returns the data for the
view from the data base.

This function is unusual in that, unlike most Open API
functions, the coordinate space is View Space. View Space is
parallel to the screen, with the center of the view at (0,0,0).  The
view center is mapped from Absolute Space to View Space by
applying first the view rotation, then the view translation to it. The
scale in View Space is the same as in Absolute Space.

Environment: Internal  and  External

See Also:
 UF_VIEW_set_xy_clip

History:
 ******************************************************************************/
extern UFUNEXPORT int UF_VIEW_ask_xy_clip(
tag_t view_tag ,/* <I>
                Tag of the view whose X-Y clip bounds are needed
                */
double xy_clip_bounds[4]  /* <O>
                          Array of the bounds of the view, in view space
                          (Minimum_X, Maximum_X, Minimum_Y, Maximum_Y)
                          */
);

/****************************************************************************
Returns the current X and Y clip boundaries of the given view.  The clip
boundaries define a rectangle on the Z = 0 plane of View Space.

Please note the following:
The clip boundary returned is different to the one returned by
UF_VIEW_ask_xy_clip. UF_VIEW_ask_xy_clip return the boundary saved 
in the data base for the view. UF_VIEW_ask_current_xy_clip return the
current boundary.

If the view is in the current layout, has been changed in
the layout (by, for example, a Zoom), and has not been saved since
it was changed, then the clip boundaries returned by this function
will reflect the changes.

This function is unusual in that, unlike most Open API
functions, the coordinate space is View Space. View Space is
parallel to the screen, with the center of the view at (0,0,0).  The
view center is mapped from Absolute Space to View Space by
applying first the view rotation, then the view translation to it. The
scale in View Space is the same as in Absolute Space.

Environment: Internal

See Also:
 UF_VIEW_ask_xy_clip

History: Original release was in NX5.0.
******************************************************************************/
extern UFUNEXPORT int UF_VIEW_ask_current_xy_clip(
tag_t view_tag ,/* <I>
                Tag of the view whose X-Y clip bounds are needed
                */
double xy_clip_bounds[4]  /* <O>
                          Array of the bounds of the view, in view space
                          (Minimum_X, Maximum_X, Minimum_Y, Maximum_Y)
                          */
);
/****************************************************************************
Sets the X and Y clip boundaries of the given view.  The clip boundaries
define a rectangle in on the Z = 0 rectangle of View Space.

This function is primarily intended for use by specialized applications such
as Translators.  It is a low-level access function which only modifies the
view's data base setting for the XY clip boundaries.

If the view is currently displayed, the display of the view is not modified by
this function, and if the view is later saved, the clip boundaries given to
this function are overwritten.  If this is not what you need, consider using
uc6431 (Set View Center and Scale), which, for displayed views, modifies the
displayed parameters of the view (and not the data base parameters), and for
non-displayed views modifies the data base parameters of the view.  Or,
consider using UF_VIEW_pan_view and/or UF_VIEW_zoom_view, which work only on
displayed views, without regenerating the display of the view.

This function is unusual in that, unlike most Open API functions, the
coordinate space is View Space.  View Space is parallel to the screen, with
the center of the view at (0,0,0).  The view center is mapped from Absolute
Space to View Space by applying first the view rotation, then the view
translation to it.  The scale in View Space is the same as in Absolute Space.

Environment: Internal  and  External

See Also:
 UF_VIEW_ask_xy_clip

History:
 *****************************************************************************/
extern UFUNEXPORT int UF_VIEW_set_xy_clip(
tag_t view_tag ,/* <I>
                Tag of the view whose X-Y clip bounds are to be set
                */
double xy_clip_bounds[4]  /* <I>
                          Array of the bounds of the view, in view space
                          (Minimum_X, Maximum_X, Minimum_Y, Maximum_Y)
                          */
);

/*****************************************************************************
Makes a copy of the given view, creating a new view.
The view_to_copy may or may not be currently displayed. The
new_view is NOT displayed by UF_VIEW_copy_view, but you can later
replace the new view into the layout, using uc6464.

The data for the copy is taken from the "saved" parameters of the
view, which are not necessarily the view parameters currently being
used for the view. For example, if UF_VIEW_rotate_view has been
used since the view was displayed, and the view has not been saved
since the call to UF_VIEW_rotate_view, then the saved parameters do
not include the effect of the rotation. If this is not what you want, you
might call uc6450 first, but note that uc6450 does not save a change to
the rotation of one of the eight "canned" views.

This function does not copy any view modifications made to objects in
view_to_copy to new_view. Any view-dependent objects defined in
view_to_copy are not moved to new_view but remain defined in
view_to_copy.

Environment: Internal  and  External

See Also:
 uc6464
 uc6450

History:
 *****************************************************************************/
extern UFUNEXPORT int UF_VIEW_copy_view(
tag_t view_to_copy ,/* <I>
                    The tag of the view which you want to copy.  This
                    view may not be a drawing view, nor may it be a
                    view on a drawing.
                    */
char * name_of_new_view ,/* <I>
                         The name of the new view.  Must contain valid
                         characters, must have no more than
                         UF_OBJ_NAME_LEN characters.  There must not
                         already be a view of this name in the Displayed
                         part.
                         */
tag_p_t new_view  /* <O>
                  The tag of the newly created view
                  */
);

/*****************************************************************************
Saves all "active" views (those in the current layout) and retains their
current names.

Environment: Internal  and  External

See Also:
 uc6450

History: Original release was in V14.0.
****************************************************************************/
extern UFUNEXPORT int UF_VIEW_save_all_active_views( void );

/****************************************************************************
This function returns the lighting attributes of a single specified view.
Each view can have different lights assigned to it. The lights are now
shared between the NX hardware shading and Photo shading.

If no lights were found with the part, the following 2 default lights are
turned on in each view to ensure that shaded display is lit:
1.      Light name:     Default 1 Ambient
        Light type:     UF_VIEW_AMBIENT_LIGHT
2.      Light name :    Default 2 Up-Front Dist
        Light type:     UF_VIEW_DISTANT_LIGHT
        Light mode:     UF_VIEW_FIXED_TO_OBSERVER
        Light Location: 0.8, 0.0, 0.4
        Light to:       0.0, 0.0, 0.0

Environment: Internal  and  External

See Also:
 UF_VIEW_set_view_light

History:
******************************************************************************/
extern UFUNEXPORT int UF_VIEW_ask_view_light(
tag_t  view ,/* <I>
             Tag of view
             */
UF_VIEW_lighting_t * view_light  /* <O>
                                 Data structure containing view lighting
                                 parameters
                                 */
);

/****************************************************************************
Sets the lighting attributes for a single specified view. The lights are now
shared between the NX hardware shading and Photo shading.

If no lights were found with the part, the following 2 default lights are
automatically turned on in each view to ensure shaded display
becomes lit:
1.      Light name:     Default 1 Ambient
        Light type:     UF_VIEW_AMBIENT_LIGHT
2.      Light name :    Default 2 Up-Front Dist
        Light type:     UF_VIEW_DISTANT_LIGHT
        Light mode:     UF_VIEW_FIXED_TO_OBSERVER
        Light Location: 0.8, 0.0, 0.4
        Light to:       0.0, 0.0, 0.0

Environment: Internal  and  External

See Also:
 UF_VIEW_ask_view_light

History:
******************************************************************************/
extern UFUNEXPORT int UF_VIEW_set_view_light(
tag_t  view_tag ,/* <I>
                 Tag of view.
                 NULL_TAG = Work View
                 */
UF_VIEW_lighting_t * view_light  /* <I>
                                 Data structure containing view lighting
                                 parameters
                                 */
);

/***************************************************************************
Deletes a view or returns an error code stating why view could not be
deleted.

Environment: Internal  and  External

See Also:

History:
****************************************************************************/
extern UFUNEXPORT void UF_VIEW_delete(
tag_t view_obj_id ,/* <I>
                   Object ID of view to delete
                   */
int * error_flag  /* <EC>
                  Status code:
                  0 = Success
                  1 = Can not delete canned view
                  2 = Can not delete work view
                  3 = Can not delete drawing view
                  4 = Can not delete last view in canned lay.
                  5 = Can not delete sketch view
                  6 = Can not delete view, view belongs to
                           at least one layout
                  */
);

/******************************************************************************
Checks the expand state of the work view. If the current layout is a
single view, the returned value for expanded is false. An active layout
must currently exist. The expanded view may be a drawing member
view. Checking the expanded state of a drawing member view is
equivalent to checking the Work In Member View mode.

Environment: Internal

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_VIEW_is_expanded(
logical * expanded  /* <O>
                    True if the work view is expanded, else false
                    */
);

/******************************************************************************
Makes the specified view the work view then expands the view. If the
view is already expanded or if the current layout is a single view, then
the request is ignored. An active layout must exist. The view may be a
member view in a drawing layout. Expanding a drawing member view
is equivalent to entering the Work In Member View mode.

Environment: Internal

See Also:


History:
 ******************************************************************************/
extern UFUNEXPORT int UF_VIEW_expand_view(
tag_t view_tag  /* <I>
                The view tag; if NULL_TAG, work view is used
                */
);

/******************************************************************************
Expands the current work view. If the view was already expanded or if
the current layout is a single view, then the request is ignored. An
active layout must already exist. The layout cannot be a layout with a
drawing.

Environment: Internal

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_VIEW_expand_work_view( void );

/******************************************************************************
Unexpands the current work view. If the view is already unexpanded
or if the current layout is a single view then the request is ignored. An
active layout must currently exist. The layout can contain a  drawing.
If the expanded view is a drawing member view, then the drawing is
restored. Unexpanding a drawing member view is  equivalent to
exiting the Work In Member View mode.

Environment: Internal

See Also:

History:
 ******************************************************************************/
extern UFUNEXPORT int UF_VIEW_unexpand_work_view( void );

/******************************************************************************
Gets the tag of an existing view that you specify by name.

Environment: Internal and External

See Also:

History:
 ******************************************************************************/
extern UFUNEXPORT int UF_VIEW_ask_tag_of_view_name(
char * view_name ,/* <I>
                  The view name (30 char max); if blank, work view is used.
                  */
tag_t * view_tag  /* <O>
                  The corresponding view tag
                  */
);

/****************************************************************************
Retrieves the number of view dependent edits for an object, and the
corresponding data for each modification.

Environment: Internal  and  External

See Also:


History:
*****************************************************************************/
extern UFUNEXPORT int UF_VIEW_ask_vde_data(
tag_t object ,/* <I>
              Tag of object
              */
int * number_edits ,/* <O>
                    Number of view dependent edits for the object.
                    */
UF_VIEW_vde_data_p_t * vde_data  /* <OF,len:number_edits>
                                 Array of vde structures containing the view,
                                 color, font, width, and range of each of the
                                 view dependent edits.  Use UF_free() to free
                                 the memory.
                                 */
);

/****************************************************************************
Retrieve the number of view dependent edits for an object and the
corresponding edit types

Environment: Internal and External

See Also:

History:
*****************************************************************************/
extern UFUNEXPORT int UF_VIEW_ask_vde_data_with_type
(
    tag_t object,                           /* <I> Tag of object                             */
    int  *number_edits,                     /* <O> Number of view dependent edits for object */
    UF_VIEW_vde_data_and_type_p_t *vde_data /* <OF,len:number_edits> Array of vde type of
                                                   each of the view dependent edits; use
                                                   UF_free () to free memory                 */
);

/****************************************************************************
This routine converts a view dependent object in the specified view
to the model.

Environment: Internal and External

Note:  This user function uses the same object filter as that of the view
       dependent edit functionality in interactive NX; you cannot change it.

See Also:


History: This function was originally released in V15.0.
****************************************************************************/
extern UFUNEXPORT int UF_VIEW_convert_to_model
(
    tag_t view_tag,     /* <I>
                        The tag of the view
                        */
    tag_t object_tag    /* <I>
                        Tag of the view dependent object
                        */
);

/****************************************************************************
Converts a model object to the view dependent object in the
specified view.

Note:  This user function uses the same object filter as that of the view
       dependent edit functionality in interactive NX; you cannot change it.

Environment: Internal and External

See also:


History: This function was originally released in V15.0.
*****************************************************************************/
extern UFUNEXPORT int UF_VIEW_convert_to_view
(
    tag_t view_tag,   /* <I>
                      The specified view tag.
                      */
    tag_t object_tag  /* <I>
                      The object tag.
                      */
);


/******************************************************************************
This routine retrieves the type of the specified view.

Environment: Internal  and  External

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_VIEW_ask_type
(
       tag_t              view_tag,       /* <I>
                                          The specified view tag.
                                          */
       UF_VIEW_type_t    *type,      /* <O>
                                     The view type.
                                     UF_VIEW_MODEL_TYPE           = 0,
                                     UF_VIEW_DRAWING_MEMBER_TYPE  = 1,
                                     UF_VIEW_DRAWING_SHEET_TYPE   = 2
                                     */
       UF_VIEW_subtype_t *subtype    /* <O>
                                     The view subtype - drawing member views
                                     only.
                                     UF_VIEW_INVALID_SUBTYPE      = -1,
                                     UF_VIEW_SECTION_SUBTYPE      = 0,
                                     UF_VIEW_IMPORTED_SUBTYPE     = 1,
                                     UF_VIEW_BASE_MEMBER_SUBTYPE  = 2,
                                     UF_VIEW_ORTHOGONAL_SUBTYPE   = 3,
                                     UF_VIEW_AUXILIARY_SUBTYPE    = 4,
                                     UF_VIEW_DETAIL_SUBTYPE       = 5,
                                     UF_VIEW_BREAK_SUBTYPE        = 6
                                     */
);

/*******************************************************************************
This routine retrieves the work view tag.

Environment: Internal  and  External

See Also:  uc6448

History:  This function was originally released in V16.0.
*******************************************************************************/
extern UFUNEXPORT int UF_VIEW_ask_work_view(
tag_t * work_view  /* <O>
                   Tag of work view
                   */
);

/****************************************************************************
Maps a point in absolute space to drawing coordinates. Vectors cannot
be mapped using this function. This function maps from drawing member views
only. If the units of the part file and drawing are different then scale
the mapped point to the units of the part file where required.

Environment: Internal  and  External

See Also:  UF_VIEW_map_drawing_to_model


History: Originally released in V16.0

******************************************************************************/
extern UFUNEXPORT int UF_VIEW_map_model_to_drawing(
 tag_t member_view,     /* <I>
                        A Member View on drawing
                        */
 double model_pt[3],    /* <I>
                        Point in absolute space
                        */
 double map_pt[2]       /* <O>
                        2-D point on the drawing
                        */
 );

/****************************************************************************
Maps a point in drawing space to absolute coordinates. Vectors cannot
be mapped using this function. This function maps from drawing member views
to model coordinates only. If the units of the part file and drawing are
different and the input point is in part units then scale the point to
the drawing units before calling this function.

Environment: Internal  and  External

See Also:  UF_VIEW_map_model_to_drawing


History: Originally released in V16.0

******************************************************************************/
extern UFUNEXPORT int UF_VIEW_map_drawing_to_model(
 tag_t member_view,     /* <I>
                        A Member View on drawing
                        */
 double drawing_pt[2],  /* <I>
                        2-D point on the drawing member view
                        */
 double model_pt[3]    /* <O>
                        Point in absolute space
                        */
 );

/****************************************************************************
Renames a view.

Environment: Internal  and  External

See Also:

History: Originally released in V17.0

******************************************************************************/
extern UFUNEXPORT int UF_VIEW_rename(
    tag_t view,  /* <I> The view that is to be renamed. */
    const char *name /* <I> The new name for the view. */
 );

/****************************************************************************
Cycle objects within a view.

If view is NULL_TAG, the work view is used.

A cycle type of UF_VIEW_VISIBLE_OBJECTS returns all objects which are
visible in the view; when using a cycle type of UF_VIEW_VISIBLE_OBJECTS,
objects which are outside of the view bounds are not returned. However,
non-rectangular boundaries of drafting member views are not considered
by UF_VIEW_cycle_objects. UF_VIEW_cycle_objects only works on the
rectangular boundary of the view - as though the breakline/detail
boundary was removed. If the desire is to obtain visible objects within a
drafting member view with non-rectangular borders and with respect to the
non-rectangular border itself, please refer to UF_VIEW_ask_visible_objects.

You must not delete, or un-erase objects, or add or remove view
modifications during a cycle as the resulting changes will cause the
outcome of the cycle to be unpredictable.

Do not attempt to delete objects when cycling the database in a loop.  Problems
can occur when trying to read the next object when the current object has been
deleted.  To delete objects, save an array with the objects in it, and then
when you have completed cycling, use UF_OBJ_delete_array_of_objects to delete
the saved array of objects.

Warning: This function will return curves that are used to display a
solid silhouette in a drawing member view.  Use UF_DRAW_ask_group_of_curve
on any curve returned to determine if the curve belongs to a
UF_solid_silhouette_type group.

Warning:  This function can return objects which are visible with the specified view
but which are layers other than the user-accessible layers of 1 - 256 inclusive.

Environment: Internal  and  External

See Also:
 UF_VIEW_ask_visible_objects

History: Originally released in V18.0

******************************************************************************/
extern UFUNEXPORT int UF_VIEW_cycle_objects(
    tag_t view,             /* <I> The view to cycle in
                             *       - if NULL_TAG, the work view is used
                             */
    UF_VIEW_cycle_objects_t type,  /* <I> Object Selection - one of:
                                    *     UF_VIEW_VISIBLE_OBJECTS
                                    *     UF_VIEW_DEPENDENT_OBJECTS
                                    *     UF_VIEW_ERASED_OBJECTS
                                    *     UF_VIEW_MODIFIED_OBJECTS
                                    */
    tag_t *object    /* <I/O>  On input, the last object found by this routine.
                      *    Pass in a NULL_TAG to start the cycle.
                      *    On output, is set to the next object.
                      *    A NULL_TAG is returned when the cycle is complete.
                      */
);

/****************************************************************************
Returns visible objects in a view broken down by those which are entirely
visible within the view and those which are visible but clipped by the view
boundary (i.e those which cross the view boundary).

Note that this function is primarily designed to work with drafting member
views. While it may be used with model views or drawing sheet views, the bounds
of those latter views are not considered in the outcome. The bounds of drafting
member views, including those with non-rectangular borders are considered.

If view is NULL_TAG, the work view is used.

Environment: Internal and External

See Also:
 UF_VIEW_cycle_objects

History: Originally released in V19.0

******************************************************************************/
extern UFUNEXPORT int UF_VIEW_ask_visible_objects(
    tag_t view,             /* <I> The view to cycle in
                             *       - if NULL_TAG, the work view is used
                             */
    int   *n_visible,       /* <O> The number of entirely visible objects
                             */
    tag_t **visible,        /* <OF,len:n_visible>
                               The list of entirely visible objects
                             */
    int   *n_clipped,       /* <O> The number of objects which cross the view
                             *     boundary, yet some portion is visible
                             */
    tag_t **clipped         /* <OF,len:n_clipped>
                               The list of clipped objects
                             */
);


/*******************************************************************************
Erases an object from a view.

Return:
         Flag
        0 = OK
        1 = View Does Not Exist
        2 = Invalid Character In View Name
        3 = Invalid Object Type

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUNEXPORT int uc6400(
char * cp1 ,/* <I>
            Name Of View (30 char max)
            ""= Work View
            */
tag_t  np2  /* <I>
            Object identifier Of Object
            */
);
/*******************************************************************************
Convert a view dependent object to model

NOTE: An individual ordinate dimension cannot be converted to a
model object by itself. You may however convert an ordinate origin
and all its associated ordinate dimensions to model objects by setting
np2 = object identifier of the ordinate origin.

This user function will convert more object types to model dependent objects than
UF_VIEW_convert_to_model().

Return:
         Flag
        0 = OK
        1 = View Does Not Exist
        2 = Invalid Character In View Name
        3 = Object Not View Dependent
        4 = Ordinate Dimension cannot be converted
                  to a model object.

Environment: Internal  and  External

See Also:
 UF_VIEW_convert_to_model

History:
*******************************************************************************/
extern UFUNEXPORT int uc6401(
char * cp1 ,/* <I>
            Name Of View (30 char max)
            ""= Work View
            */
tag_t np2  /* <I>
           Object identifier Of Object To Convert To Model
           */
);
/*******************************************************************************
Convert model object to view dependent

NOTE: An individual ordinate dimension cannot be converted to a
view dependent object  by itself. You may however convert an
ordinate origin and all its associated ordinate dimensions to view
dependent objects by setting np2 = object identifier of the ordinate
origin.

This user function will convert more object types to view dependent objects than
UF_VIEW_convert_to_view().

Return:
         Flag
        0 = OK
        1 = View Does Not Exist
        2 = Invalid Character In View Name
        3 = Object Already View Dependent
        4 = Object Not Eligible For View Dependence
        5 = Operation not available when work part
                 and display part are different
        6 = Ordinate Dimension cannot be converted
                  to a view dependent object.

Environment: Internal  and  External

See Also:
 UF_VIEW_convert_to_view

History:
 ******************************************************************************/
extern UFUNEXPORT int uc6402(
char * cp1 ,/* <I>
            Name Of View (30 char max)
            ""= Work View
            */
tag_t np2  /* <I>
           Object ID Of The Object To Convert To View
Dependent
           */
);
/*******************************************************************************
Removes the view dependent edits from an object.

Return:
         Flag
        0 = OK
        1 = View Does Not Exist
        2 = Invalid Character In View Name
        3 = Object Not View Modified

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6403(
char * cp1 ,/* <I>
            Name of View (30 char max)
            "" = Work View
            */
tag_t np2  /* <I>
           Object identifier of the object
           */
);
/*******************************************************************************
Converts all view dependent objects to model.

Note:  This user function uses the same object filter as that of the view
       dependent edit functionality in interactive NX.

Return:
         Flag
        0 = OK
        1 = View Does Not Exist
        2 = Invalid Character In View Name
        3 = Object Not View Modified

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6404(
char * cp1  /* <I>
            Name Of View (30 char max)
            ""= Work View
            */
);
/*******************************************************************************
Removes all view dependent edits from a view.

Return:
         Flag
        0 = OK
        1 = View Does Not Exist
        2 = Invalid Character In View Name
        3 = No View Modifications Exist

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6405(
char * cp1  /* <I>
            Name Of View (30 char max)
            "" = Work View
            */
);
/*******************************************************************************
Modify the COLOR/FONT/WIDTH of a curve in a view.

RP3 is the normalized start and stop parameters for the curve along
the normalized curve from 0.0 (beginning) to 1.0 (end). The curve
display is modified between the two specified limits.

Return  :
            Flag
            0 = OK
            1 = View Does Not Exist
            2 = Invalid Character In View Name
            3 = Invalid Color Number
            4 = Invalid Font Number
            5 = Invalid Width Number
            6 = Invalid Object Type
            7 = Data Base Limit ForObject View Mods Full
            8 = Attempt To Erase Curve On Full Parameter - Use uc6400

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUNEXPORT int uc6406(
char * cp1 ,/* <I>
            Name of the view (30 char max)
            ""  = Work View
            */
tag_t np2 ,/* <I>
           Object ID of The object to be modified
           */
double * rp3 ,/* <I>
              Start and end parameters of the modification
              0.0 <= RP3[0 ..1] <= 1.0
              */
int ip4 ,/* <I>
         Modification color
          -1 = Do not change color
         1-15 = Color number as defined in uf_obj.h
         */
int  ip5 ,/* <I>
          Modification font
        -1 = Do not change font
         0 = Invisible
         1-4 = Font number as defined in uf_obj.h
          */
int ip6 /* <I>
         Modification width
         -1 = Do not change width
         0-2 = Width Number as defined in uf_obj.h
         */
);

/*******************************************************************************
Returns view dependent edit data for an object.
Please use UF_VIEW_ask_vde_data rather than uc6408

Environment: Internal  and  External

See Also:
 UF_VIEW_ask_vde_data

History:
*******************************************************************************/
extern UFUNEXPORT int uc6408(
tag_t np1 ,/* <I>
           Object ID of view dependent object
           */
int ip2 ,/* <I>
         Record number of modification
         */
char *  cr3 ,/* <O>
             View name (30 char max)
             */
double * rr4 ,/* <O>
              Parameter Range Of Modification
              - Range (0.0,1.0) returns two doubles rr4[2]
              */
int * ir5 ,/* <O>
           Color value, see uf_obj.h for values
           */
int * ir6 ,/* <O>
           Font value, see uf_obj.h for values
           */
int * ir7  /* <O>
           Width value, see uf_obj.h for values
           */
);
/*******************************************************************************
Returns view dependent status of an object and the associated view name when
the object is view dependent.

Drafting views will have a @0 appended to the end of the name (ViewName@0).
Modeling views will just conatin the name (ViewName).

Return:
         Error Code
        0 = Success
        1 = Invalid Object Type

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6409(
tag_t   np1 ,/* <I>
             Object Identifier for view dependent status check
             */
int * ir2 ,/* <O>
           Status for the object
           0 = Not view dependent
           1 = View dependent
           */
char *  cr3  /* <O>
             View name.  This must be a buffer allocated to contain at least
             UF_OBJ_NAME_LEN + 1 characters.
             */
);/* <WRAPAS:UF_VIEW_ask_view_dependent_status> */
/*******************************************************************************
 Read View Center and Scale

If cp1 is blank, the work view is used.

Return:
         Return Code
        0 = OK
        1 = View Does Not Exist
        2 = Invalid View Name

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6430(
char * cp1 ,/* <I>
            View Name (30 char max)
            "" = Work View
            */
double * rr2 ,/* <O>
              View Center (Absolute CSYS) x,y and z coordinates.
              */
double * rr3  /* <O>
              View Scale
              */
);
/*******************************************************************************
Set View Center and Scale

If cp1 is blank, the work view is updated. The scale must be greater
than 0.0. An invalid scale is an error and does not change the view
center. uc6431 can edit a non-active view.

Return:
         Return Code
         0 = OK
         1 = View Does Not Exist
         2 = Invalid View Name
        31 = Invalid Scale

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6431(
char * cp1 ,/* <I>
            View Name (30 char max)
            "" = Work View
            */
double * rp2 ,/* <I>
              View Center (Absolute CSYS), in x,y, and z coordinates
              */
double rp3  /* <I>
            View Scale
            0.0 = Use Existing Scale
            */
);
/*******************************************************************************
Fit the View(s)

If cp1 is blank and ip2=1, the work view is updated. If ip2=2, the
value in cp1 is ignored.

Return:
         Return Code
        0 = OK
        1 = View Does Not Exist
        2 = Invalid View Name
        9 = View Not Active

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6432(
char * cp1 ,/* <I>
            View name (30 char max)
            "" = Work view
            */
int ip2  /* <I>
         Fit option
         1 = View named in cp1
         2 = All active views
         */
);
/*******************************************************************************
Read View Matrix

If cp1 is blank, the work view is used.

Return:
         Return Code
        0 = OK
        1 = View Does Not Exist
        2 = Invalid View Name

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6433(
char * cp1 ,/* <I>
            View name (30 char max)
            "" = Work view
            */
double * rr2  /* <O>
              View matrix (Nine element array)
              */
);
/*******************************************************************************
Set View Matrix

If cp1 is blank, the work view is updated. The object Identifier in np3
must reference an object that has a coordinate system associated with
it, such as an arc, conic, drafting object, CSYS, etc.

Return:
         Return Code
         0 = OK
         1 = View Does Not Exist
         2 = Invalid View Name
         3 = View is a Drawing View or Drawing Member View
         9 = View Not Active
        31 = Invalid Type Object In np3
        32 = Invalid Matrix In rp4
        33 = Invalid Matrix Option

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6434(
char * cp1 ,/* <I>
            View name (30 char max)
            "" = Work view
            */
int  ip2 ,/* <I>
          Matrix option
          1 = Absolute csys
          2 = WCS
          3 = Use CSYS of object in np3
          4 = Use matrix in rp4
          */
tag_t np3 ,/* <I>
           Object identifier (If ip2=3)
           */
double * rp4  /* <I>
              This argument is used when ip2 is 4.  In this case, this will
              be the X-axis and Y-axis of the matrix (6 element array).
              rp4[0..2] will be the X-axis values and rp4[3..5] will be the
              Y-Axis values.  The Z axis of the view matrix will be internally
              calculated by taking the cross product of the two input axis.
              */
);
/*******************************************************************************
Rotate View Point around View Center

If cp1 is blank, the work view is updated. A compound rotation can be
accomplished by setting several values of rp2 to non-zero. Negative
angles are valid. The rotations are executed in the order of rp2[0],
rp2[1], rp2[2].

Return:
         Return Code
        0 = OK
        1 = View Does Not Exist
        2 = Invalid View Name
        9 = View Not Active

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6435(
char * cp1 ,/* <I>
            View Name (30 char max)
            "" = Work View
            */
double * rp2  /* <I>
              Rotation angles in degrees.
              [0] Down
              [1] Right
              [2] Counter-clockwise
              */
);
/*******************************************************************************
Read View Clipping Planes

If cp1 is blank, the work view is used. The values of rr3 are not
returned if the corresponding values of IR2 = 1.
NOTE: "Clipping Enabled by System" means NX
automatically detects that clipping planes are required and turns them on.

Return:
         Return Code
        0 = OK
        1 = View Does Not Exist
        2 = Invalid View Name

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6436(
char * cp1 ,/* <I>
            View Name (30 char max)
            "" = Work View
            */
int * ir2 ,/* <O>
           Clipping Plane Status ir[2]
           [0] Front
                 1 = Clipping Disabled
                 2 = Clipping Enabled by User
                 3 = Clipping Enabled by System
           [1] Back
                 1 = Clipping Disabled
                 2 = Clipping Enabled by User
                 3 = Clipping Enabled by System
           */
double * rr3  /* <O>
              Clipping Plane Distance from the view origin
              [0] Front
              [1] Back
              */
);
/*******************************************************************************
Set View Clipping Planes

If cp1 is blank, the work view is updated. The values of rp3 are
ignored if the corresponding clipping plane is disabled (ip2) or
auto-set. Using auto-set calculates the plane to be the minimum (for
front plane) or maximum (for back plane) distance that displays all
objects.

You cannot disable clipping planes in a view that has 3D vectors (see
Uc6440 - Read view display type), and you cannot disable the front
clipping plane in perspective views (see uc6439 - Set view
perspective).

If the projection type is "PERSPECTIVE" and the front Z clipping
plane is in front of the EYE POINT (see uc6438 - Read view
perspective), the front Z clipping plane moves to the EYE POINT.
Return Codes of 33 and 34 are warnings only.

Return:
         Return Code
         0      = OK
         1      = View Does Not Exist
         2      = Invalid View Name
         3      = View Has 3D Vectors - Can Not
                  Remove Clipping Planes
         9      = View Not Active
        31      = Front Plane Behind Back Plane
        33      = Perspective View - Can Not Remove
                  Front Plane
        34      = Perspective View - Front Plane Moved
                  To Eye Point

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6437(
char * cp1 ,/* <I>
            View name (30 char max)
            "" = Work view
            */
int * ip2 ,/* <I>
           Clipping plane status
           [0] Front
           [1] Back
                0 = Do not change status/distance
                1 = Disable clipping
                2 = Enable clipping
                3 = Auto-set distance
           */
double * rp3  /* <I>
              Clipping plane distance
              (If ip2[x] = 2) (From view origin)
              [0] Front
              [1] Back
              */
);
/*******************************************************************************
Read View Perspective

If cp1 is blank, the work view is used. rr3 is modified only if the
projection type is "perspective" (ir2=2).

Return:
         Return Code
        0 = OK
        1 = View Does Not Exist
        2 = Invalid View Name

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6438(
char * cp1 ,/* <I>
            View name (30 char max)
            "" = Work View
            */
int *ir2 ,/* <O>
         Projection type
         1 = Parallel
         2 = Perspective
         */
double * rr3  /* <O>
              Perspective distance (If ir2 = 2)
              */
);
/*******************************************************************************
Set View Perspective

If cp1 is blank, the work view is updated. The value of rp3 is used only
if ip2=2. The value of rp4 is used only if ip2=3.
If projection type is "PERSPECTIVE" and the EYE POINT is set to
be behind the current front Z clipping plane, the front Z clipping
plane is moved equal to the EYE POINT.

Return:
         Return Code
         0      = OK
         1      = View Does Not Exist
         2      = Invalid View Name
         3      = Drafting View Not Valid
         9      = View Not Active
        31      = Invalid Distance
        32      = Invalid Projection Option

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6439(
char * cp1 ,/* <I>
            View name (30 char max)
            "" = Work View
            */
int ip2 ,/* <I>
         Projection Option
         1       = Make view parallel
         2       = Make view perspective
         3       = Change eye point
         */
double rp3 ,/* <I>
            Perspective distance (If ip2=2)
            */
double * rp4  /* <I>
              X, Y and Z coordinates of the Eye Point (Absolute CSYS) (If ip2=3)
              */
);
/*******************************************************************************
Read view display type

If cp1 is blank, the work view is used.

Return:
         Return Code
         0 = OK
         1 = View Does Not Exist
         2 = Invalid View Name

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6440(
char * cp1 ,/* <I>
            View name (30 char max)
            "" = Work view
            */
int * ir2  /* <O>
           Display type
           2 = 2D display vectors
           3 = 3D display vectors
           */
);
/*******************************************************************************
Read View Drawing Parameters

If cp1 is blank, the work view is used.

Return:
         Return Code
        0 = OK
        1 = View Does Not Exist
        2 = Invalid View Name
        3 = View Is A Drawing

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6442(
char * cp1 ,/* <I>
            View name (30 char max)
            "" = Work View
            */
double * rr2 ,/* <O>
              X, Y and Z of drawing reference point, (Absolute CSYS)
              */
double * rr3  /* <O>
              Drawing scale
              */
);
/*******************************************************************************
Set view drawing parameters

If cp1 is blank, the work view is updated. The reference point and
scale are  used to place a view on a drawing. The scale must be
greater than 0.0. UF6443 can edit a non-active view.

Return:
         Return Code
         0 = OK
         1 = View Does Not Exist
         2 = Invalid View Name
         3 = View Is A Drawing
         4 = Not allowed in "Work in member view"
                  mode
        31 = Invalid Scale

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6443(
char * cp1 ,/* <I>
            View name (30 char max)
            "" = Work View
            */
double * rp2 ,/* <I>
              X, Y and Z coordinates of the drawing reference point in
              absolute coordinates.
              */
double rp3  /* <I>
            Drawing scale
            0.0 = No change
            */
);
/*******************************************************************************
Read Surface/Solid Display Parameters

Please use
 UF_VIEW_ask_surface_display_options
and
 UF_VIEW_ask_fog_options
instead.

If cp1 is blank, the work view is used.

Return:
         Return Code
        0 = OK
        1 = View Does Not Exist
        2 = Invalid View Name

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6444(
char * cp1 ,/* <I>
            View Name (30 char max)
            "" = Work View
            */
int * ir2 ,/* <O>
           Surface/Solid Face Display
           1 = Grid Lines
           2 = Solid Fill
           3 = Flat Shading
           4 = Gouraud Shading
           5 = Phong Shading
           6 = Hidden Surface
           */
int * ir3 ,/* <O>
           Depth Cueing
           1 = Off
           2 = On
           */
int * ir4 ,/* <O>
           Solid Unfixed Blends
           1 = Visible
           2 = Invisible
           */
int * ir5 ,/* <O>
           Solid Smooth Edges
           1 = Visible
           2 = Invisible
           */
int * ir6 ,/* <O>
           Solid Silhouettes
           1 = Visible
           2 = Invisible
           */
int * ir7  /* <O>
           Solid Hidden Edges
           1 = Visible
           2 = Invisible
           3 = Dashed
           */
);

/*******************************************************************************
Set Surface/Solid Display Parameters

Please use
 UF_VIEW_set_surface_display_options
and
 UF_VIEW_set_fog_options
instead.

If cp1 is blank, the work view is updated.

Return:
         Return Code
         0 = OK
         1 = View Does Not Exist
         2 = Invalid View Name
         3 = Drafting View Not Valid
        31 = Invalid Parameter

Environment: Internal  and  External
See Also:
History:
*******************************************************************************/
extern UFUNEXPORT int uc6445(
char * cp1 ,/* <I>
            View Name (30 char max)
            "" = Work View
            */
int ip2 ,/* <I>
         Surface/Solid Face Display
         0 = Use Current Mode
         1 = Grid Lines
         2 = Solid Fill
         3 = Flat Shading
         4 = Gouraud Shading
         5 = Phong Shading
         6 = Hidden Surface
         */
int ip3 ,/* <I>
         Depth Cueing
         0 = Use Current Mode
         1 = Off
         2 = On
         */
int ip4 ,/* <I>
         Solid Unfixed Blends
         0 = Use Current Mode
         1 = Visible
         2 = Invisible
         */
int ip5 ,/* <I>
         Solid Smooth Edges
         0 = Use Current Mode
         1 = Visible
         2 = Invisible
         */
int ip6 ,/* <I>
         Solid Silhouettes
         0 = Use Current Mode
         1 = Visible
         2 = Invisible
         */
int ip7  /* <I>
         Solid Hidden Edges
         0 = Use Current Mode
         1 = Visible
         2 = Invisible
         3 = Dashed
         */
);
/*******************************************************************************
Read View Layer Visibility Mask

If cp1 is blank, the work view is used. ir3 is returned only if ir2=2. For
example, if an individual layer visibility mask exists for this view.
NOTE: This routine does not read the global layer mask.

Return:
         Return Code
        0 = OK
        1 = View Does Not Exist
        2 = Invalid View Name

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6446(
char * cp1 ,/* <I>
            View Name (30 char max)
            "" = Work View
            */
int * ir2 ,/* <O>
           Mask Status
           1 = Global
           2 = Individual
           */
int * ir3  /* <O>
           256 word layer mask, indexed by layer number +1.  So
           ir3[0] has the status of layer 1, ir3[1] has the status
           of layer 2 and so on.  Each element of the array can have
           one of the following two values.
           0 = Invisible In View
           1 = Visible In View
           */
);

/*******************************************************************************
Set View Layer Visibility Mask

If cp1 is blank, the work view is used. If ip2=1, any existing view layer
visibility mask is deleted for this view. If ip2=2, a new layer visibility
mask is created if none exists. ip3 is used only if ip2=2. For example,
if an individual layer visibility mask is to be used for this view.
UF6447 can edit a non-active view.
NOTE: This routine does not affect the global layer mask (see
routines UF500x).

Return:
         Return Code
         0 = OK
         1 = View Does Not Exist
         2 = Invalid View Name
        31 = Invalid Mask Status

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6447(
char * cp1 ,/* <I>
            View Name (30 char max)
            "" = Work View
            */
int ip2 ,/* <I>
         Mask Status
         1 = Global
         2 = Individual
         */
int *ip3  /* <I>
          256 word layer mask, indexed by layer number +1.  So
          ip3[0] has the status of layer 1, ip3[1] has the status
          of layer 2 and so on.  Each element of the array can have
          one of the following two values.
          0 = Invisible In View
          1 = Visible In View
         */
);


/*******************************************************************************
Read Work View Name
Please use UF_VIEW_ask_work_view rather than uc6448.
Return:
      work view name.

Environment: Internal  and  External
See Also:
History:
*******************************************************************************/
extern UFUNEXPORT void uc6448(
char * cr1  /* <O>
            View Name (30 char max)
            */
);
/*******************************************************************************
Change Work View

This function has no effect if a drawing is current.

Return:
         Return Code
        0 = OK
        1 = View Does Not Exist
        2 = Invalid View Name
        9 = View Not Active

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6449(
const char * cp1  /* <I>
                  View Name (30 char max)
                  */
);
/*******************************************************************************
Save View

cp1 is the name of the view to save. If cp1 is blank, the work view is
saved.
cp2 is the name to save the view as. If cp2 is blank, the view is saved
with the same name. If cp2 is not blank and a view of that name does
not exist, a new view is created. If cp2 is not blank and a view of that
name already exists, an error is returned.
ip3 and ip4 are used only if the view is saved with a new name (i.e.,
cp2 <>""  and cp2<>  cp1).
NOTE: The view orientation is not changed for a "canned" view.

Return:
         Return Code
        0 = OK
        1 = View Does Not Exist
        2 = Invalid View Name
        4 = View Already Exists
        9 = View Not Active
        10 = Operation Not Allowed in "Work in
                   member View" mode
        11 = Can't Save View because drawing is
                   currently displayed
        23 = Can't Save Drawing View With New
                   Name

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6450(
const char * cp1 ,/* <I>
                  View Name (30 char max)
                  "" = Work View
                  */
const char * cp2 ,/* <I>
                  Name To Save View As
                  "" = Current Name
                  */
const int ip3 ,/* <I>
               Copy View Modifications
               0 = No
               1 = Yes
               */
const int ip4  /* <I>
               Move View Dependent Objects
               0 = No
               1 = Move
               */
);

/*******************************************************************************
Delete View

Many views cannot be deleted. Among them are the "canned" views
and work view. If a view contains a drawing, it cannot be deleted. In
addition, any view that belongs to a layout cannot be deleted.

Return:
         Return Code
        0 = OK
        1 = View Does Not Exist
        2 = Invalid View Name
        3 = Cannot Delete Canned View
        4 = Cannot Delete Work View
        5 = Cannot Delete Drawing View
        6 = Cannot delete view. View belongs to at
               least one layout.
        8 = Cannot delete view. View belongs to at
               least one layout.

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6454(
char * cp1  /* <I>
            View Name (30 char max)
            */
);
/*******************************************************************************
Rename View
Please use UF_VIEW_rename rather than uc6455.
If cp1 is blank, the work view is renamed. The "canned" views cannot
be renamed. In addition, modeling views cannot be renamed as
drawing view names and vice versa.

Return:
         Return Code
        0 = OK
        1 = Old View Does Not Exist
        2 = Invalid View Name
        3 = Can Not Rename Canned View
        4 = New View Already Exists
        5 = Can Not Rename Drawing View

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6455(
char * cp1 ,/* <I>
            Old View Name (30 char max)
            ""= Work View
            */
char * cp2  /* <I>
            New View Name (30 char max)
            */
);
/*******************************************************************************
Cycle Views in Part
Please use UF_OBJ_cycle_objs_in_part with type UF_view_type rather than uc6456
This routine cycles the part and returns one view name per cycle. To
start the cycle, set CA1 to an empty string ("").  The first
view name is returned in CA1. The next call returns the second view
name in CA1. When CA1 is returned with an empty string (ca1 returns ""),
all view names have been returned. View or drawing names that are
28 characters or less are appended with an "@n" string (where n is
any positive integer including zero). If your view name is more than 28
characters, the "@n" string is truncated.
NOTE: The cycle can be continued even if the view named in CA1 is
deleted.

Return:
         Return Code
        0 = OK
        1 = View Does Not Exist
        2 = Invalid View Name

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6456(
char * ca1, /* <I/O>
            On input this is the view name returned by the last call to this
            routine.  Pass in an empty string, "", to start cycling.  On output
            this is the next view name.  When all view names have been cycled,
            and empty string, "", will be returned.  The calling program must
            allocation a 31 character buffer to hold the view name.
            */
int * ir2  /* <O>
           Active View Flag
           0 = View Inactive
           1 = View Active
           */
);
/*******************************************************************************
Cycle Objects in View
Please use UF_VIEW_cycle_objects rather than uc6457
If cp1 is blank, the work view is used. ip2=1 returns all objects which
are visible in the view. Objects which are out of the view bounds are
not returned.

Different types of cycles can be intermingled. For instance, while
cycling view dependent objects, you can also cycle objects erased in a
view. You cannot delete or un-erase objects or view modifications
during a cycle.

Warning: This function will return curves that are used to display a
solid silhouette in a drawing member view.  Use UF_DRAW_ask_group_of_curve
on any curve returned to determine if the curve belongs to a
UF_solid_silhouette_type group.

NOTE: return/IR4=9 is valid only if ip2=1.

Return:
         Return Code
        0       = OK
        1       = View Does Not Exist
        2       = Invalid View Name
        9       = View Not Active
        31      = Invalid Selection Option

Environment: Internal  and  External

See Also:

History:
*******************************************************************************/
extern UFUNEXPORT int uc6457(
char * cp1 ,/* <I>
            View Name (30 char max)
            "" Work View
            */
int ip2 ,/* <I>
         Object Selection
        1 = Visible Objects
        2 = View Dependent Objects
        3 = Objects Erased In View
        4 = Objects Modified In View
         */
tag_t * na3 /* <I/O>
             On input, the last object found by this routine.  Pass in a
             NULL_TAG to start the cycle.  On output the next object.  A
             NULL_TAG is returned when the cycle is complete.
             */
);

/***********************************************************************
 *
 * Routine -
 *   UF_VIEW_create_view_set
 *
 * Description -
 *   Create a view set from a base view and a list of orthographic view types.
 *   The view set created will reside in the same part as the base view does.
 *   The view set contains a list of orthographic user defined modeling views
 *   with one of the view as base view. All the other view's orientation are
 *   determined by the base view. When base view changes its orientation, all
 *   the other view's orientation will update accordingly.
 *
 * Note -
 *       The base_view_tag must be a user defined modeling view, it can not
 *       be any canned views. The base_view_type and other_view_types must
 *       be any one within UF_VIEW_standard_orientation_t
 *
 * Return Codes -
 *       ERROR_OK
 *       UF_VIEW_INVALID_VIEW_TAG
 *       UF_VIEW_INVALID_OBJECT
 *       UF_VIEW_INVALID_ORIENTATION_TYPE
 *       UF_VIEW_CONFLICT_ORIENTATION_TYPE
 *       UF_VIEW_INVALID_NAME
 *       UF_VIEW_NOT_IN_DISPLAYED_PART
 *
 * See Also -
 *       UF_VIEW_add_to_view_set
 *       UF_VIEW_remove_from_view_set
 *       UF_VIEW_ask_view_set_by_name
 *       UF_VIEW_ask_base_view_of_view_set
 *       UF_VIEW_set_base_view_of_view_set
 *       UF_VIEW_ask_views_of_view_set
 *       UF_VIEW_delete_view_set
 *
 * Environment: Internal and External
 *
 * History: This routine is originally created in release NX3.0
***********************************************************************/
extern UFUNEXPORT int UF_VIEW_create_view_set(
    const char * name,                                  /* <I> The view set name */
    tag_t base_view_tag,                                /* <I> The Base View in the Set */
    UF_VIEW_standard_orientation_t base_view_type,      /* <I> The Base View orthographic type */
    int num_other_views,                                /* <I> The number of other views to add to the set */
    UF_VIEW_standard_orientation_p_t other_view_types,  /* <I,len:num_other_views> A list of other view types to add in the set */
    tag_t *view_set_tag                                 /* <O> the view set object created */
);


/***********************************************************************
 *
 * Routine -
 *   UF_VIEW_add_to_view_set
 *
 * Description -
 *   Add an orthographic view to view set
 *
 * Return Codes -
 *       ERROR_OK
 *       UF_VIEW_INVALID_OBJECT
 *       UF_VIEW_INVALID_VIEW_TAG
 *       UF_VIEW_INVALID_ORIENTATION_TYPE
 *
 *
 * See Also -
 *       UF_VIEW_create_view_set
 *       UF_VIEW_remove_from_view_set
 *       UF_VIEW_ask_view_set_by_name
 *       UF_VIEW_ask_base_view_of_view_set
 *       UF_VIEW_set_base_view_of_view_set
 *       UF_VIEW_ask_views_of_view_set
 *       UF_VIEW_delete_view_set
 *
 * Environment: Internal and External
 *
 * History: This routine is originally created in release NX3.0
***********************************************************************/
 extern UFUNEXPORT int UF_VIEW_add_to_view_set(
     tag_t view_set_tag,                            /* <I> The view set to add */
     UF_VIEW_standard_orientation_t type            /* <I> The orthographic view type to add */
 );

/***********************************************************************
 *
 * Routine -
 *   UF_VIEW_remove_from_view_set
 *
 * Description -
 *   Remove an orthographic view from the view set
 *
 * Return Codes -
 *       ERROR_OK
 *       UF_VIEW_INVALID_OBJECT
 *       UF_VIEW_INVALID_VIEW_TAG
 *       UF_VIEW_INVALID_ORIENTATION_TYPE
 *
 * See Also -
 *       UF_VIEW_create_view_set
 *       UF_VIEW_add_to_view_set
 *       UF_VIEW_ask_view_set_by_name
 *       UF_VIEW_ask_base_view_of_view_set
 *       UF_VIEW_set_base_view_of_view_set
 *       UF_VIEW_ask_views_of_view_set
 *       UF_VIEW_delete_view_set
 *
 * Environment: Internal and External
 *
 * History: This routine is originally created in release NX3.0
***********************************************************************/
extern UFUNEXPORT int UF_VIEW_remove_from_view_set (
    tag_t view_set_tag,                             /* <I> The view set to add */
    UF_VIEW_standard_orientation_t type             /* <I> The view type to remove */
);


/***********************************************************************
 *
 * Routine -
 *   UF_VIEW_ask_view_set_by_name
 *
 * Description -
 *   Query the view set by the given name
 *
 * Note -
 *   The query is only against the current displayed part. If there is
 *   no view set with the given name, a NULL_TAG is returned.
 *
 * Return Codes -
 *       ERROR_OK
 *       UF_VIEW_INVALID_NAME
 *
 * See Also -
 *       UF_VIEW_create_view_set
 *       UF_VIEW_add_to_view_set
 *       UF_VIEW_remove_from_view_set
 *       UF_VIEW_ask_base_view_of_view_set
 *       UF_VIEW_set_base_view_of_view_set
 *       UF_VIEW_ask_views_of_view_set
 *       UF_VIEW_delete_view_set
 *
 * Environment: Internal and External
 *
 * History: This routine is originally created in release NX3.0
***********************************************************************/
extern UFUNEXPORT int UF_VIEW_ask_view_set_by_name(
    const char * name,                      /* <I> The view set name */
    tag_t *view_set                         /*<O> The view set match the name */
);

/***********************************************************************
 *
 * Routine -
 *   UF_VIEW_ask_base_view_of_view_set
 *
 * Description -
 *   Query the base view of the given a view set
 *
 * Return Codes -
 *       ERROR_OK
 *       UF_VIEW_INVALID_OBJECT
 *       UF_VIEW_INVALID_VIEW_TAG
 *
 * See Also -
 *       UF_VIEW_create_view_set
 *       UF_VIEW_add_to_view_set
 *       UF_VIEW_remove_from_view_set
 *       UF_VIEW_ask_view_set_by_name
 *       UF_VIEW_set_base_view_of_view_set
 *       UF_VIEW_ask_views_of_view_set
 *       UF_VIEW_delete_view_set
 *
 * Environment: Internal and External
 *
 * History: This routine is originally created in release NX3.0
***********************************************************************/
extern UFUNEXPORT int UF_VIEW_ask_base_view_of_view_set(
    tag_t view_set_tag,               /* <I> The view set */
    tag_t *base_view_tag              /* <O> The base view of the view set */
);

/***********************************************************************
 *
 * Routine -
 *   UF_VIEW_set_base_view_of_view_set
 *
 * Description -
 *   Set a new base view in the set.
 *
 * Return Codes -
 *       ERROR_OK
 *       UF_VIEW_INVALID_OBJECT
 *       UF_VIEW_INVALID_VIEW_TAG
 *       UF_VIEW_INVALID_ORIENTATION_TYPE
 *
 * See Also:
 *       UF_VIEW_create_view_set
 *       UF_VIEW_add_to_view_set
 *       UF_VIEW_remove_from_view_set
 *       UF_VIEW_ask_view_set_by_name
 *       UF_VIEW_ask_base_view_of_view_set
 *       UF_VIEW_ask_views_of_view_set
 *       UF_VIEW_delete_view_set
 *
 * Environment: Internal and External
 *
 * History: This routine is originally created in release NX3.0
***********************************************************************/
extern UFUNEXPORT int UF_VIEW_set_base_view_of_view_set(
    tag_t view_set_tag,                       /* <I> The view set */
    UF_VIEW_standard_orientation_t type       /* <I> The new base view type */
);

/***********************************************************************
 *
 * Routine -
 *   UF_VIEW_ask_views_of_view_set
 *
 * Description -
 *   Query the list of views in a view set
 *
 * Return Codes -
 *       ERROR_OK
 *       UF_VIEW_INVALID_OBJECT
 *       UF_VIEW_INVALID_VIEW_TAG
 *
 * See Also:
 *       UF_VIEW_create_view_set
 *       UF_VIEW_add_to_view_set
 *       UF_VIEW_remove_from_view_set
 *       UF_VIEW_ask_view_set_by_name
 *       UF_VIEW_ask_base_view_of_view_set
 *       UF_VIEW_set_base_view_of_view_set
 *       UF_VIEW_delete_view_set
 *
 * Environment: Internal and External
 *
 * History: This routine is originally created in release NX3.0
***********************************************************************/
extern UFUNEXPORT int UF_VIEW_ask_views_of_view_set(
    tag_t view_set_tag,        /* <I> The view set */
    int *num_views,            /* <O> The number of views in the set */
    tag_p_t *views_in_set      /* <OF,len:num_views> The list of views in the set */
);

/***********************************************************************
 *
 * Routine -
 *   UF_VIEW_delete_view_set
 *
 * Description -
 *   Delete the view set
 *
 * Return Codes -
 *       ERROR_OK
 *       UF_VIEW_INVALID_OBJECT
 *       UF_VIEW_INVALID_VIEW_TAG
 *
 * See Also:
 *       UF_VIEW_create_view_set
 *       UF_VIEW_add_to_view_set
 *       UF_VIEW_remove_from_view_set
 *       UF_VIEW_ask_view_set_by_name
 *       UF_VIEW_ask_base_view_of_view_set
 *       UF_VIEW_set_base_view_of_view_set
 *       UF_VIEW_ask_views_of_view_set
 *
 * Environment: Internal and External
 *
 * History: This routine is originally created in release NX3.0
***********************************************************************/
extern UFUNEXPORT int UF_VIEW_delete_view_set(
    tag_t view_set_tag         /* <I> The view set */
);


/*******************************************************************************
Returns the rendering style and the Edge display options of
the specified view. The view must have type UF_VIEW_MODEL_TYPE.

Environment: Internal and External

See Also:
 UF_VIEW_set_surface_display_options
 UF_VIEW_rendering_style_t
 UF_VIEW_edge_display_options_t

History: Originally released in NX4.0.
*******************************************************************************/
extern UFUNEXPORT int UF_VIEW_ask_surface_display_options(
    tag_t                          view_tag,
                                   /* <I> The view tag; if NULL_TAG,
                                          the work view is used. */
    UF_VIEW_rendering_style_p_t    rendering_style,
                                   /* <O> The rendering style of the view. */
    UF_VIEW_edge_display_options_p_t
                                   edge_display_options
                                   /* <O> The edge display options
                                          of the view. */
);


/*******************************************************************************
Sets the rendering style and the edge display options of the
specified view. The view must have type UF_VIEW_MODEL_TYPE.

Environment: Internal and External

See Also:
 UF_VIEW_ask_surface_display_options
 UF_VIEW_rendering_style_t
 UF_VIEW_edge_display_options_t

History: Originally released in NX4.0.
*******************************************************************************/
extern UFUNEXPORT int UF_VIEW_set_surface_display_options(
    tag_t                        view_tag,
                                 /* <I> The view tag; if NULL_TAG,
                                        the work view is used. */
    UF_VIEW_rendering_style_t    rendering_style,
                                 /* <I> The new rendering style for the
                                        view. */
    UF_VIEW_edge_display_options_p_t
                                 edge_display_options
                                 /* <I> New edge display options
                                        for the view. */
);


/*******************************************************************************
Returns the shaded edge options of the specified view. The view
must have type UF_VIEW_MODEL_TYPE.

Environment: Internal and External

See Also:
 UF_VIEW_set_shaded_edge_options
 UF_VIEW_shaded_edge_options_t

History: Originally released in NX4.0.
*******************************************************************************/
extern UFUNEXPORT int UF_VIEW_ask_shaded_edge_options(
    tag_t                        view_tag,
                                 /* <I> The view tag; if NULL_TAG,
                                        the work view is used. */
    UF_VIEW_shaded_edge_options_p_t
                                 shaded_edge_options
                                 /* <O> The shaded edge options of
                                        the view. */
);


/*******************************************************************************
Sets the shaded edge options of the specified view. The view must
have type UF_VIEW_MODEL_TYPE.

Environment: Internal and External

See Also:
 UF_VIEW_ask_shaded_edge_options
 UF_VIEW_shaded_edge_options_t

History: Originally released in NX4.0.
*******************************************************************************/
extern UFUNEXPORT int UF_VIEW_set_shaded_edge_options(
    tag_t                        view_tag,
                                 /* <I> The view tag; if NULL_TAG,
                                        the work view is used. */
    UF_VIEW_shaded_edge_options_p_t
                                 shaded_edge_options
                                 /* <O> New shaded edge options for
                                        the view. */
);


/*******************************************************************************
Returns the fog options of the specified view. The view must have type
UF_VIEW_MODEL_TYPE.

Environment: Internal and External

See Also:
 UF_VIEW_set_fog_options
 UF_VIEW_fog_options_t

History: Originally released in NX4.0.
*******************************************************************************/
extern UFUNEXPORT int UF_VIEW_ask_fog_options(
    tag_t                        view_tag,
                                 /* <I> The view tag; if NULL_TAG,
                                        the work view is used. */
    UF_VIEW_fog_options_p_t      fog_options
                                 /* <O> The fog options of the view. */
);


/*******************************************************************************
Sets the fog options of the specified view. The view must have type
UF_VIEW_MODEL_TYPE.

Environment: Internal and External

See Also:
 UF_VIEW_ask_fog_options
 UF_VIEW_fog_options_t

History: Originally released in NX4.0.
*******************************************************************************/
extern UFUNEXPORT int UF_VIEW_set_fog_options(
    tag_t                        view_tag,
                                 /* <I> The view tag; if NULL_TAG,
                                        the work view is used. */
    UF_VIEW_fog_options_p_t      fog_options
                                 /* <O> New fog options for the view. */
);

/****************************************************************************
Sets the lighting attributes of a single specified light.

You cannot change the light type, light mode, or direction of the light with
this function.

Environment: Internal  and  External

See Also:
 UF_VIEW_set_view_light
 UF_VIEW_ask_view_light

History: This routine is originally created in release NX3.0.3
******************************************************************************/
extern UFUNEXPORT int UF_VIEW_edit_view_light(
UF_VIEW_light_name_t light_name, /* <I>
                                 Name of light to edit
                                 */
UF_VIEW_light_attributes_p_t light_attrs  /* <I>
                                          Data structure containing light
                                          attributes
                                          */
);

/*******************************************************************************
Ask View Center

If view is NULL_TAG, the work view is used.

The view center returned by this function is a point on the view plane at the
center of the viewing volume. If the viewing volume is symmetric (as it usually
is), then this point is also the view origin. 

Return:
        Return Code
        0 = OK
        1 = View Does Not Exist
        2 = Invalid View Tag - can not find view object from given view tag
        3 = center pointer is NULL

Environment: Internal  and  External

See Also:
 UF_VIEW_set_center
 uc6430

History:
*******************************************************************************/
extern UFUNEXPORT int UF_VIEW_ask_center(
tag_t tag ,/* <I>
            view tag
            */
double* center /* <O>
             View Center (Absolute CSYS) x,y and z coordinates.
             */
);

/*******************************************************************************
Set View Center

If view is NULL_TAG, the work view is used.

The view center returned by this function is a point on the view plane at the
center of the viewing volume. If the viewing volume is symmetric (as it usually
is), then this point is also the view origin. 

Return:
        Return Code
        0 = OK
        1 = View Does Not Exist
        2 = Invalid View Tag - can not find view object from given view tag
        3 = center pointer is NULL

Environment: Internal  and  External

See Also:
 UF_VIEW_ask_center
 uc6431

History:
*******************************************************************************/
extern UFUNEXPORT int UF_VIEW_set_center(
tag_t tag ,/* <I>
            view tag
            */
double* center /* <I>
             View Center (Absolute CSYS) x,y and z coordinates.
             */
);

/******************************************************************************
Set View scale

If view is NULL_TAG, the work view is used.

Scales the specified view by the specified scale factor. This is the same
as changing the scale on the Zoom View menu and does not trigger a
re-gen. If there are multiple occurrences of the view in the layout, then
only one arbitrary occurrence is affected.

The view must be on the current layout. On a drawing layout, the view
must be a drawing view or a member work view.

Return:
        Return Code
        0 = OK 
        1 = View does not exist
        2 = Invalid view tag -- cannot find view object from given view tag
        31 = Input scale value is less than or equal to zero

Environment: Internal

See Also:

History:
******************************************************************************/
extern UFUNEXPORT int UF_VIEW_set_scale(
tag_t tag ,/* <I>
            The view tag; if NULL_TAG, work view is used
           */
double scale  /* <I>
               A positive absolute scale factor
               */
);

/*******************************************************************************
Ask View matrix

If view is NULL_TAG, the work view is used.

Return:
        Return Code
        0 = OK
        1 = View Does Not Exist
        2 = Invalid View Tag - can not find view object from given view tag
        3 = matrix pointer is NULL

Environment: Internal  and  External

See Also:
 UF_VIEW_set_rotation
 uc6433

History:
*******************************************************************************/
extern UFUNEXPORT int UF_VIEW_ask_rotation(
tag_t tag ,/* <I>
            view tag
            */
double * matrix /* <O>
                View rotation matrix (nine element array)
                matrix[0..2] will be the X-axis of the view
                matrix[3. 5] will be the Y-axis
                matrix[6..8] will be the Z-axis
                */
);

/*******************************************************************************
Set View matrix

If view is NULL_TAG, the work view is used.

The input axes do not have to be unit vectors. If the vectors are not 
perpendicular, they will be made so by adjusting the Y-axis. An error 
code = 32 will result if either of the input vectors is zero or if they 
are parallel.

Return:
        Return Code
        0 = OK
        1 = View Does Not Exist
        2 = Invalid View Tag - can not find view object from given view tag
        9 = View Not Active
        32 = Cross product of input X and Y axes is zero

Environment: Internal  and  External

See Also:
 UF_VIEW_ask_rotation
 uc6434

History:
*******************************************************************************/
extern UFUNEXPORT int UF_VIEW_set_rotation(
tag_t tag ,/* <I>
            view tag
            */
double * axes /* <I>
                 View x and y axes (six element array)
                 view_matrix[0..2] will be the X-axis values and
                 view_matrix[3..5] will be the Y-Axis values.
                 The Z axis of the view matrix will be internally calculated 
                 by taking the cross product of the two input axes.
                 */
);

/*******************************************************************************
Ask View Z-Clipping Planes

If view is NULL_TAG, the work view is used.
The values of distance are not returned if the corresponding values of status = 1. 
NOTE: "Clipping Enabled by System" means NX automatically detects that clipping
planes are required and turns them on. 

Return:
        Return Code
        0 = OK
        1 = View Does Not Exist
        2 = Invalid View Tag - can not find view object from given view tag
        3 = Either status or distance pointer is NULL

Environment: Internal  and  External

See Also:
 UF_VIEW_set_Z_clip
 uc6436

History:
*******************************************************************************/
extern UFUNEXPORT int UF_VIEW_ask_Z_clip(
tag_t tag ,/* <I>
            view tag
            */
int * status ,/* <O>
               Clipping Plane Status status[2]
               [0] Front
                     1 = Clipping Disabled
                     2 = Clipping Enabled by User
                     3 = Clipping Enabled by System
               [1] Back
                     1 = Clipping Disabled
                     2 = Clipping Enabled by User
                     3 = Clipping Enabled by System
               */
double * distances /* <O>
                    Clipping Plane Distance from the view origin
                    [0] Front
                    [1] Back
                    */
);

/*******************************************************************************
Set View Z-Clipping Planes

If view is NULL_TAG, the work view is used. The values of distance are
ignored if the corresponding clipping plane is disabled (status) or
auto-set. Using auto-set calculates the plane to be the minimum (for
front plane) or maximum (for back plane) distance that displays all
objects.

You cannot disable clipping planes in a view that has 3D vectors (see
Uc6440 - Read view display type), and you cannot disable the front
clipping plane in perspective views (see uc6439 - Set view
perspective).

If the projection type is "PERSPECTIVE" and the front Z clipping
plane is in front of the EYE POINT (see uc6438 - Read view
perspective), the front Z clipping plane moves to the EYE POINT.
Return Codes of 33 and 34 are warnings only.


Return:
        Return Code
        0 = OK
        1 = View Does Not Exist
        2 = Invalid View Tag - can not find view object from given view tag
        3 = View Has 3D Vectors - Can Not
             Remove Clipping Planes
        4 = Either status or distance pointer is NULL
        9 = View Not Active
       31 = Front Plane Behind Back Plane
       33 = Perspective View - Can Not Remove
            Front Plane
       34 = Perspective View - Front Plane Moved
            To Eye Point

Environment: Internal  and  External

See Also:
 UF_VIEW_ask_Z_clip
 uc6437

History:
*******************************************************************************/
extern UFUNEXPORT int UF_VIEW_set_Z_clip(
tag_t tag ,/* <I>
            view tag
            */
int * status ,/* <I>
               Clipping plane status
               [0] Front
               [1] Back
                    0 = Do not change status/distance
                    1 = Disable clipping
                    2 = Enable clipping
                    3 = Auto-set distance
               */
double * distances /* <I>
                    Clipping plane distance
                    (If status[i] = 2) (From view origin)
                    [0] Front
                    [1] Back
                    */
);

/*******************************************************************************
Ask View Perspective

If view is NULL_TAG, the work view is used. distance is modified only if the
projection type is "perspective" (type = 2).

Return:
        Return Code
        0 = OK
        1 = View Does Not Exist
        2 = Invalid View Tag - can not find view object from given view tag
        3 = Either type or distance pointer is NULL

Environment: Internal  and  External

See Also:
 UF_VIEW_set_perspective
 uc6438

History:
*******************************************************************************/
extern UFUNEXPORT int UF_VIEW_ask_perspective(
tag_t tag ,/* <I>
            view tag
            */
int *type ,/* <O>
             Projection type
             1 = Parallel
             2 = Perspective
             */
double * distance  /* <O>
                   Perspective distance (If type = 2)
                   */
);

/*******************************************************************************
Set View Perspective

If view is NULL_TAG, the work view is used. The value of distance is used only
if option = 2. The value of eye_point  is used only if option = 3.
If projection type is "PERSPECTIVE" and the EYE POINT is set to
be behind the current front Z clipping plane, the front Z clipping
plane is moved equal to the EYE POINT.

If the eye point is changed (option = 3), then the rotation matrix 
of the view will also be changed.

Return:
        Return Code
        0 = OK
        1 = View Does Not Exist
        2 = Invalid View Tag - can not find view object from given view tag
        3 = Drafting View Not Valid
        9 = View Not Active
       31 = Invalid Distance
       32 = Invalid Projection Option (not equal to 1, 2, or 3)

Environment: Internal  and  External

See Also:
 UF_VIEW_ask_perspective
 uc6439

History:
*******************************************************************************/
extern UFUNEXPORT int UF_VIEW_set_perspective(
tag_t tag ,/* <I>
            View tag
            */
int option ,/* <I>
             Projection Option
             1 = Make view parallel
             2 = Make view perspective
             3 = Change eye point
             */
double distance ,/* <I>
                Perspective distance (If option=2)
                */
double * eye  /* <I>
              X, Y and Z coordinates of the Eye Point (Absolute CSYS) (If option =3)
              */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif


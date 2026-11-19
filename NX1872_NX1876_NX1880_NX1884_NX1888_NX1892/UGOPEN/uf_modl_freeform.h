/*****************************************************************************
             Copyright (c) 1998-2004 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved



File description:
    Open API modeling routines to create, edit and inquire about features such as
    ruled, thru_curves, thru_curve_mesh, swept, section, extension, offset, bridge,
    trimmed sheet, quilt, midsurface, and etc
*****************************************************************************/

#ifndef UF_MODL_FREEFORM_H_INCLUDED
#define UF_MODL_FREEFORM_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/***************************************************************************
   Prototypes for Freeform modeling
  ***************************************************************************/

/*****************************************************************************
Creates a freeform sweep feature. The first segment curve of each guide/section/spine
is a starting curve. The output of this function is the object identifier
associated to the sweep.  Use UF_MODL_init_string_list and
UF_MODL_create_string_list to create input strings. Use UF_MODL_free_string_list
to free memory once this routine has been called, and the string list is no
longer needed.

Environment: Internal  and  External
See Also:
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_create_sweep(
UF_STRING_p_t s_guide ,/* <I>
                       Pointer to the guide list structure.
                       int     num     Total number of guide strings
                                       (min=1, max=3)
                       int string[ ]   Total number of segment curves/
                                       sketch identifier of each guide
                                       string
                                       (min=1, max =402)
                       int dir[ ]      Direction of each guide string
                                        1 = Start to end
                                       -1 = End to start
                       tag_t id[ ]     Identifier of guide curve
                       */
UF_STRING_p_t s_section ,/* <I>
                         Pointer to the section list structure.
                         int     num     Total number of section strings
                                         (min=1, max=150)
                         int string[ ]   Total number of segment curves/
                                         sketch/face of each section string
                                         (min=1, max=402)
                         int dir[ ]      Direction of each section string
                                          1 = Start to end
                                         -1 = End to start
                         tag_t id[ ]     Identifier of section curve
                         */
UF_STRING_p_t s_spine ,/* <I>
                       Pointer to the spine list structure.
                       int     num     Total number of section strings
                                       (min=0, max=1)
                       int string[ ]   Total number of segment curves/
                                       sketch/face of each section string
                                       (min=1, max=402)
                       int dir[ ]      Direction of each section string
                                        1 = Start to end
                                       -1 = End to start
                       tag_t id[ ]     Identifier of spine curve
                       */
UF_METHOD_p_t orientation ,/* <I>
                           Pointer to the orientation list structure.
                           int method      Orientation method
                                           (for s_guide-> num = 1)
                                           1 = Face normals
                                           2 = Vector direction
                                           3 = Another curve
                                           4 = Fixed (parallel sweep)
                                           5 = A point
                                           6 = Angular law
                                           7 = Forced direction
                           int inter       NOT USED
                           tag_t id        Base surface
                                           (for orientation->method =1)
                                           Datum axis
                                           (for orientation->method = 2,7)
                           double value[3] Orientation 3D vector
                                           (for orientation->method = 2,7)
                                           Orientation 3D point
                                           (for orientation->method = 5)
                                           Law Function Value
                                           (for orientation->method=6)
                                           [0] = Angle law function offset
                                           [1] = Angle law function scale
                           UF_STRING_p_t s_curve Pointer to curve
                              structure list (for orientation->method = 3 or 6)
                           */

UF_METHOD_p_t scaling ,/* <I>
                       Pointer to the scaling list structure.
                       int method      Scaling method
                                       (for s_guide-> num = 1)
                                       1 = Constant scale
                                       2 = Blended
                                       3 =  Another curve
                                       4 = A point
                                       5 = Area law
                                       (for s_guide-> num = 2)
                                       6 = Scale laterally
                                       7 = Scale uniformly
                       int inter       Scale blended interpolation
                                       (for scaling->method = 2)
                       tag_t id                NOT USED
                       double value[3] Scale values
                                       [0] = Scale factor
                                       (for scaling->method = 1)
                                       [0-1] = Scale range
                                       (for scaling->method = 2)
                                       [0-2] = 3D absolute point
                                       (for scaling->method = 4)
                                       Law Function Value
                                       (for scaling->method=5)
                                       [0] = Area law function offset
                                       [1] = Area law function scale
                                      UF_STRING_p_t s_curve Pointer to curve
                       structure list (for scaling->method = 3 or 5)
                       */
int * alignment ,/* <I>
                 Alignment method:
                 1 = Parameter
                 2 = Arc Length
                 */
int * inter ,/* <I>
             Interpolation method (for s_section->num > 1):
                1 = Linear
                2 = Cubic
             */
int * body_type ,/* <I>
                 Type of body:
                 0 = Sheet (Default)
                 1 = Solid
                 */
UF_FEATURE_SIGN boolean ,/* <I>
                         The sign of the operation to be performed.
                         UF_NULLSIGN = create new target solid
                         UF_POSITIVE = add to target solid
                         UF_NEGATIVE = subtract from target solid
                         UF_UNSIGNED = intersect with target solid
                         */
double tol[3] ,/* <I>
               Tolerances:
               [0] = Distance
               [1] = Angle (in degrees)
               [2] = Intersection
               */
tag_t * body_obj_id  /* <O>
                     Body object identifier of sweep
                     */
);

/*****************************************************************************
Returns the creation data for a freeform Sweep feature.

Environment: Internal  and  External
See Also:
History:Original release was in V13.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_sweep(
tag_t  feature_obj_id ,/* <I>
                       Feature object identifier of sweep
                       */
UF_STRING_p_t s_guide ,/* <OF>
                       Pointer to the string list structure containing the
                       data defining the guide curves used to create the
                       feature. See structure section of manual for details.
                       Use UF_MODL_free_string_list to deallocate
                       memory.
                       */
UF_STRING_p_t s_section ,/* <OF>
                         Pointer to the string list structure containing the
                         date defining the section curves used to create the
                         feature. See structure section of manual for details.
                         Use UF_MODL_free_string_list to deallocate
                         memory.
                         */
UF_STRING_p_t s_spine ,/* <OF>
                       Pointer to the string list structure for the spine
                       string.  Use UF_MODL_free_string_list to deallocate
                       memory.
                       */
UF_METHOD_p_t orientation ,/* <O>
                           Pointer to the orientation list structure.
                           int method      Orientation method
                               (for s_guide-> num = 1)
                               1 = Face normals
                               2 = Vector direction
                               3 = Another curve
                               4 = Fixed (parallel sweep)
                               5 = A point
                               6 = Angular law
                               7 = Forced direction
                            int inter               NOT USED
                            tag_t id
                               Base surface (for orientation->method =1)
                               Datum Axis (for orientation->method = 2,7)
                            double value[3]
                               Orientation 3D vector (for orientation->method =
                                                                           2,7)
                               Orientation 3D point (for orientation->method =
                                                                             5)
                               Law Function Value (for orientation->method=6)
                                   [0] = Angle law function offset
                                   [1] = Angle law function scale
                            UF_STRING_p_t s_curve Pointer to curve
                               structure list (for orientation->method = 3 or 6)
                           */
UF_METHOD_p_t scaling ,/* <O>
                       Pointer to the scaling list structure.
                       int method      Scaling method
                        (for s_guide-> num = 1)
                          1 = Constant scale
                          2 = Blended
                          3 =  Another curve
                          4 = A point
                          5 = Area law
                        (for s_guide->num = 2)
                          6 = Scale laterally
                          7 = Scale uniformly
                        int inter
                        Scale blended interpolation
                          ( for scaling->method = 2)
                        tag_t id                NOT USED
                        double value[3] Scale values
                          [0] = Scale factor
                          (for scaling->method = 1)
                          [0-1] = Scale range
                          (for scaling->method = 2)
                          [0-2] = 3D absolute point
                          (for scaling->method = 4)
                          Law Function Value
                          (for scaling->method=5)
                          [0] = Area law function offset
                          [1] = Area law function scale
                       UF_STRING_p_t s_curve Pointer to curve
                          structure list (for scaling->method = 3 or 5)
                       */
int * alignment ,/* <O>
                 Alignment method:
                        1 = Parameter
                        2 = Arc Length
                 */
int * inter ,/* <O>
             Interpolation method (for s_section->num > 1):
             1 = Linear
             2 = Cubic
             */
int * body_type ,/* <O>
                 Type of body:
                 0 = Sheet
                 1 = Solid
                 */
double tol[3]  /* <O>
               Tolerances:
               [0] = Distance
               [1] = Angle (in degrees)
               [2] = Intersection
               */
);


/****************************************************************************
Creates a quilt surface.

Environment: Internal  and  External
See Also: UF_MODL_ask_quilt
          UF_MODL_edit_quilt
          UF_MODL_free_quilt

History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_quilt(
UF_MODL_quilt_type_t quilt_data ,/* <I>
                                 Type of quilt surface
                                 UF_MODL_CURVE_MESH_ALONG_FIXED_VECTOR
                                 UF_MODL_CURVE_MESH_ALONG_DRIVER_NORMALS
                                 UF_MODL_B_SURFACE_ALONG_FIXED_VECTOR
                                 UF_MODL_B_SURFACE_ALONG_DRIVER_NORMALS
                                 UF_MODL_SELF_REFIT
                                 */
UF_MODL_quilt_data_structures_p_u quilt_structure_po ,/* <I>
                                                      Pointer to structure
                                                      containing the defining
                                                      data of the quilt surface.
                                                      */
tag_t * quilt_tag ,/* <O>
                   Object identifier of quilt surface to be created
                   */
int * tol_achieved  /* <O>
                    Flag indicating that the resultant face achieved the
                    tolerance requirements.
                    0 = No
                    1 = yes
                    */
);

/*****************************************************************************
Edits a quilt surface.

Environment: Internal  and  External
See Also: UF_MODL_ask_quilt
          UF_MODL_create_quilt
          UF_MODL_free_quilt

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_quilt(
UF_MODL_quilt_type_t quilt_data ,/* <I>
                                 Type of quilt surface
                                 UF_MODL_CURVE_MESH_ALONG_FIXED_VECTOR
                                 UF_MODL_CURVE_MESH_ALONG_DRIVER_NORMALS
                                 UF_MODL_B_SURFACE_ALONG_FIXED_VECTOR
                                 UF_MODL_B_SURFACE_ALONG_DRIVER_NORMALS
                                 UF_MODL_SELF_REFIT
                                 */
UF_MODL_quilt_data_structures_p_u quilt_structure_po ,/* <I>
                                                      Pointer to structure
                                                      containing the defining
                                                      data of the quilt surface.
                                                      */
tag_t  quilt_surface  /* <I>
                      Object identifier of quilt surface to be edited
                      */
);

/*****************************************************************************
Reads the creation parameters of a quilt surface. The following are
the valid defined constants for the type of quilt surface for the
quilt_data parameter:

UF_MODL_CURVE_MESH_ALONG_FIXED_VECTOR
UF_MODL_CURVE_MESH_ALONG_DRIVER_NORMALS
UF_MODL_B_SURFACE_ALONG_FIXED_VECTOR
UF_MODL_B_SURFACE_ALONG_DRIVER_NORMALS
UF_MODL_SELF_REFIT

Be careful how you manipulate the structures returned under
quilt_structure_pointer.  Many items are allocated in this code.  If you
change any items such as character strings or curve strings you may
run into trouble in UF_MODL_free_quilt.  The safest way to handle
this is to make sure all structures are in the same condition when
calling free as they were received from ask.

Environment: Internal  and  External
See Also:
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_quilt(
tag_t  quilt_tag ,/* <I>
                  Object identifier of quilt surface
                  to be read
                  */
UF_MODL_quilt_type_t * quilt_data ,/* <O>
                                   Type of quilt surface
                                   (see the description area).
                                   */
UF_MODL_quilt_data_structures_u * quilt_structure_pointer  /* <OF,free:UF_MODL_free_quilt>
                                       Pointer to structure containing the
                                       defining data of the quilt surface.  Use
                                       UF_MODL_free_quilt to free the memory
                                       allocated by this function.
                                       */
);

/*****************************************************************************
This function returns the type of quilt surface. The following are the
valid defined constants for the type of quilt surface for the
quilt_data parameter:

UF_MODL_CURVE_MESH_ALONG_FIXED_VECTOR
UF_MODL_CURVE_MESH_ALONG_DRIVER_NORMALS
UF_MODL_B_SURFACE_ALONG_FIXED_VECTOR
UF_MODL_B_SURFACE_ALONG_DRIVER_NORMALS
UF_MODL_SELF_REFIT

Environment: Internal  and  External
See Also:  UF_MODL_edit_quilt
           UF_MODL_create_quilt
           UF_MODL_free_quilt


History:
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_quilt_type(
tag_t  quilt_tag ,/* <I>
                  Object identifier of quilt surface
                  */
UF_MODL_quilt_type_t * quilt_data  /* <O>
                                   Type of quilt surface (see the
                                   description area).
                                   */
);

/*****************************************************************************
This routine should be called after a call to UF_MODL_ask_quilt in
order to free the space allocated by this routine.

Environment: Internal  and  External
See Also: UF_MODL_ask_quilt
          UF_MODL_create_quilt
          UF_MODL_edit_quilt

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_free_quilt(
UF_MODL_quilt_type_t  quilt_data ,/* <I>
                                  Type of quilt surface
                                  UF_MODL_CURVE_MESH_ALONG_FIXED_VECTOR
                                  UF_MODL_CURVE_MESH_ALONG_DRIVER_NORMALS
                                  UF_MODL_B_SURFACE_ALONG_FIXED_VECTOR
                                  UF_MODL_B_SURFACE_ALONG_DRIVER_NORMALS
                                  UF_MODL_SELF_REFIT
                                  */
UF_MODL_quilt_data_structures_u * quilt_structures_p  /* <I>
                                                      Pointer to structure
                                                      containing the defining
                                                      data of the quilt surface.
                                                      */
);

/*******************************************************************************
Modifies the input sheet body to the specified boundary and regional
conditions. The boundary conditions (faces, planes, edges, and curves)
are used to divide the input sheet body into regions by imprinting new
edges on the input sheet body. The regional conditions are employed
to classify the discarded and retained regions of the input sheet body.
The output sheet body is the retained region(s) of the input sheet body.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int  UF_MODL_create_trimmed_sheet(
tag_t  sheet_body_tag ,/* <I>
                       Tag of sheet body to be trimmed
                       */
int bounding_object_count ,/* <I>
                           Number of trimming boundary objects
                           */
tag_t * bounding_objects ,/* <I,len:bounding_object_count>
                          Array of NX eids of trimming objects
                          */
UF_MODL_vector_p_t projection_method ,/* <I>
                                      A variant record of the following
                                      int                     reverse_vector,
                                      UF_MODL_vector_type_t   vector_type,
                                      where vector_type  =

                                      UF_MODL_VECTOR_DIRECTION:
                                      project along a fixed vector,
                                      a vector, double[3], is required.

                                      UF_MODL_VECTOR_DIRECTION_EXACT_GEOMETRY:
                                      project along a fixed vector,
                                      a vector, double[3], is required,
                                      NX will produce exact geometry.

                                      UF_MODL_VECTOR_AXIS:
                                      project along a datum axis,
                                      an NX eid of the datum axis is required.

                                      UF_MODL_VECTOR_AXIS_EXACT_GEOMETRY:
                                      project along a datum axis,
                                      an NX eid of the datum axis is required,
                                      NX will produce exact geometry.

                                      UF_MODL_VECTOR_FACE_NORMALS
                                      project along face normals,
                                      no other input is needed.

                                      UF_MODL_VECTOR_FACE_NORMALS_EXACT_GEOMETRY
                                      project along face normals,
                                      no other input is needed, NX will produce
                                      exact geometry when ever possible.
                                      */
int key_pt ,/* <I>
            Points defining regions to: 1 = discard; 0 = keep
            */
int point_count ,/* <I>
                 Number of region points
                 */
double point_coords[] ,/* <I,len:3*point_count>
                       Array of region points on the sheet to be trimmed.
                       This array contains 3*point_count entries.
                       */
double tolerance ,/* <I>
                  Distance tolerance for approximations.
                  */
int * gap_point_count ,/* <O>
                       The number of gap points returned when there are
                       gaps between the edges produced by the bounding
                       objects. These points show where the gaps are.
                       */
double ** gap_points ,/* <OF,len:gap_point_count>
                      Array of points showing location of the gaps. This
                      array has 3*n_gap_points entries.  This array must
                      be freed by calling UF_free.
                      */
tag_t * feature_obj_eid  /* <O>
                         Feature object id of trimmed sheet.
                         */
);

/******************************************************************************
Returns the information stored in the record of the input trimmed sheet feature.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_trimmed_sheet(
tag_t  feature_obj_eid ,/* <I>
                        Feature object id of trimmed sheet.
                        */
tag_t * sheet_body_tag ,/* <O>
                        Tag of trimmed sheet
                        */
int * bounding_object_count ,/* <O>
                             Number of trimming boundary objects
                             */
tag_t ** bounding_objects ,/* <OF,len:bounding_object_count>
                           Array of NX eids of trimming objects.  This array
                           must be freed by calling UF_free.
                           */
UF_MODL_vector_p_t projection_method ,/* <O>
                                      A variant record of the following
                                      int                     reverse_vector,
                                      UF_MODL_vector_type_t   vector_type,
                                      where vector_type  =

                                      UF_MODL_VECTOR_DIRECTION:
                                      project along a fixed vector,
                                      a vector, double[3], is required.

                                      UF_MODL_VECTOR_DIRECTION_EXACT_GEOMETRY:
                                      project along a fixed vector,
                                      a vector, double[3], is required,
                                      NX will produce exact geometry.

                                      UF_MODL_VECTOR_AXIS:
                                      project along a datum axis,
                                      an NX eid of the datum axis is required.

                                      UF_MODL_VECTOR_AXIS_EXACT_GEOMETRY:
                                      project along a datum axis,
                                      an NX eid of the datum axis is required,
                                      NX will produce exact geometry.

                                      UF_MODL_VECTOR_FACE_NORMALS
                                      project along face normals,
                                      no other input is needed.

                                      UF_MODL_VECTOR_FACE_NORMALS_EXACT_GEOMETRY
                                      project along face normals,
                                      no other input is needed, NX will produce
                                      exact geometry when ever possible.
                                      */
int * point_key ,/* <O>
                 Points define regions to: 0 = retain; 1 = discard
                 */
int * point_count ,/* <O>
                   Number of region points
                   */
double ** point_coords ,/* <OF,len:point_count>
                        Array of region points on the sheet to be trimmed.
                        This array contains 3*point_count entries.  This
                        array must be freed by calling UF_free.
                        */
double * tolerance  /* <O>
                    Distance tolerance for approximations.
                    */
);

/******************************************************************************
Modifies data of the input trimmed sheet feature to the specified
boundary and regional conditions specified in the inputs.

Environment: Internal  and  External
See Also:
History: Original release was in V13.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_trimmed_sheet(
tag_t  feature_obj_eid ,/* <I>
                        Feature object id of trimmed sheet.
                        */
int bounding_object_count ,/* <I>
                           Number of trimming boundary objects
                           */
tag_t * bounding_objects ,/* <I,len:bounding_object_count>
                          Array of NX eids of trimming objects
                          */
UF_MODL_vector_p_t projection_method ,/* <I>
                                      A variant record of the following
                                      int                     reverse_vector,
                                      UF_MODL_vector_type_t   vector_type,
                                      where vector_type  =

                                      UF_MODL_VECTOR_DIRECTION:
                                      project along a fixed vector,
                                      a vector, double[3], is required.

                                      UF_MODL_VECTOR_DIRECTION_EXACT_GEOMETRY:
                                      project along a fixed vector,
                                      a vector, double[3], is required,
                                      NX will produce exact geometry.

                                      UF_MODL_VECTOR_AXIS:
                                      project along a datum axis,
                                      an NX eid of the datum axis is required.

                                      UF_MODL_VECTOR_AXIS_EXACT_GEOMETRY:
                                      project along a datum axis,
                                      an NX eid of the datum axis is required,
                                      NX will produce exact geometry.

                                      UF_MODL_VECTOR_FACE_NORMALS
                                      project along face normals,
                                      no other input is needed.

                                      UF_MODL_VECTOR_FACE_NORMALS_EXACT_GEOMETRY
                                      project along face normals,
                                      no other input is needed, NX will produce
                                      exact geometry when ever possible.
                                      */
int point_key ,/* <I>
               Points define regions to: 0 = retain; 1 = discard
               */
int point_count ,/* <I>
                 Number of region points
                 */
double point_coords[] ,/* <I,len:3*point_count>
                       Array of region points on the sheet to be trimmed.
                       This array contains 3*point_count entries.
                       */
double tolerance  /* <I>
                  Distance tolerance for approximations.
                  */
);

/*******************************************************************************
Creates a surface between 2 other surfaces. The resulting surface is
constrained by continuity type (either tangent continuous or curvature
continuous) and possibly by guides (either no guides, 1 or 2 guiding
side strings, or 1 or 2 guiding side surfaces). For each bridge surface,
at least 2 faces must be input, along with 2 edges indicating where on
the 2 surfaces the bridge surface should be connected.  Further input
depends on the option chosen for guide_type.


Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_bridge_face(
int continuity_type ,/* <I>
                     1 = tangent continuous, 2= curvature continuous
                     */
int guide_type ,/* <I>
                0 = no guides; 1= guide strings; 2= guide surfaces
                */
tag_t primary_faces[2] ,/* <I>
                      tags of 2 primary surfaces to be bridged
                      */
tag_t  primary_edges[2] ,/* <I>
                       tags of edges on primary surfaces where the bridge
                       should be attached.
                         */
int *primary_edges_dir ,/* <I>
                        direction of primary_edges (if continuity_type = 1)
                        1 =  forward
                        -1 = backward
                        */
UF_STRING_p_t side_string1 ,/* <I>
                            first guide string (if guide_type = 1)
                            */
UF_STRING_p_t side_string2 ,/* <I>
                            second guide string (if guide_type = 1)
                            */
tag_t side_faces[2] ,/* <I>
                   tags of 2 side guide surfaces (if guide_type = 2)
                   */
tag_t side_edges[2] ,/* <I>
                   tags of edges on side surfaces where bridge should
                   be attached (if guide_type = 2)
                   */
tag_t *result_tag  /* <O>
                  tag of resulting surface
                  */
);

/******************************************************************************
Creates a B-surface using a list of existing points. The points may
appear in any order. There must be enough points to define a surface
with the requested degree and patches and the points should cover the
area inside the specified boundaries.

The boundaries of the surface, projected onto the specified X-Y
plane, form a quadrilateral. The boundaries can be specified by the
optional bnd_corners parameter. These points, projected onto the
X-Y plane of the specified coordinate system must form a convex
quadrilateral.

The order of the points determine the U and V directions of the
resulting surface.

If the pointer to bnd_corners is NULL, the boundaries are the
smallest rectangle that encloses the cloud points in the specified X-Y
plane. The U direction of the surface is aligned with the X direction
and the V direction of the surface is aligned with the Y direction.
The X-Y plane may be specified by the optional csys_matrix
parameter.  If csys_matrix is NULL, the absolute X-Y plane is used.
In all cases the Z direction is assumed to be approximately normal to
the surface and the surface must not be ambiguous when viewed from
this direction.

Normals Z1, Z2, Z3, and other acceptable vectors all produce the
same best fit surface. However, Zn produces a dramatically different
surface. Other incorrect vectors produces different results, none
acceptable. The system cannot detect when this condition occurs.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_surf_from_cloud(
int point_cnt ,/* <I>
               Number of points in the cloud array.
               */
double cloud[][3] ,  /* <I,len:point_cnt>
                     Array of points [point_cnt][3]. The points may
                     appear in any order.  There must be enough points
                     to define a surface of the requested order an they
                     should cover the area within the boundaries
                     specified below. The points should not represent a
                     surface that is ambiguous in the surface normal
                     direction.
                     */
double   csys_matrix[2][3] ,/* <I>
                            Orientation - X-Y vectors, the U-V directions of
                            the surface correspond to these X-Y vectors.  The
                            surface must be unambiguous in the Z direction. If
                            this pointer is NULL, the absolute X-Y-Z of the
                            data is used.
                            */
double   bnd_corners[4][3] ,/* <I>
                            Boundary corners - 4 points specifying the corners
                            of the surface. The resulting surface boundaries,
                            projected onto the X-Y plane, specified above,
                            forms a quadrilateral with corners at the projection
                            of these points onto that plane. The U direction of
                            the surface lie in a direction approximately aligned
                            with the 1st and 3rd line segments and the V
                            direction aligned with the 2n and 4th. If this
                            pointer is NULL, the quadrilateral is the max-min
                            box of the input data in the specified X-Y plane.
                            */
int U_degree ,/* <I>
              Desired degree of the resulting surface in the U
              direction.  Valid values are 1 through 24.
              */
int V_degree ,/* <I>
              Desired degree of the resulting surface in the V
              direction.  Valid values are 1 through 24.
              */
int U_patches ,/* <I>
               Number of patches desired in the U direction of the
               resulting surface.
               */
int V_patches ,/* <I>
               Number of patches desired in the V direction of the
               resulting surface.
               */
int corner_switch ,/* <I>
                   Currently unused.
                   */
double * average_error ,/* <O>
                        The average distance, in the Z direction, between
                        all input points and the resulting surface.
                        */
double * max_error ,/* <O>
                    The maximum distance, in the Z direction, between
                    all input points and the resulting surface.
                    */
int * max_error_index ,/* <O>
                       The sequence number, within the cloud array, of
                       the point where the maximum error (max_error)
                       occurred.
                       */
tag_t * surface_tag  /* <O>
                     Object identifier for the resulting surface.
                     */
);


/******************************************************************************
Initializes the section surface Open API data structure. It is to be
used in conjunction with UF_MODL_create_section_surface and
UF_MODL_edit_section_surface.

Environment: Internal  and  External
See Also: UF_MODL_ask_section_surface
          UF_MODL_create_section_surface
          UF_MODL_edit_section_surface

History:V15.0 changes: The UF_MODL_secsrf_data_t structure was enhanced.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_init_section_surface(
UF_MODL_secsrf_data_p_t section_surface_data  /* <I/O>
                                              Section Surface Open API Data
                                              Structure
                                              */
);
/******************************************************************************
Creates a section surface feature from the section surface Open
API data structure.

Environment: Internal  and  External
See Also: UF_MODL_init_section_surface
         UF_MODL_ask_section_surface
         UF_MODL_edit_section_surface


History:V15.0 changes: The UF_MODL_secsrf_data_t structure was enhanced.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_section_surface(
UF_MODL_secsrf_data_p_t section_surface_data ,/* <I>
                                              Section Surface Open API Data
                                              Structure
                                              */
tag_p_t section_surface  /* <O>
                         Section Surface Feature object identifier.
                         */
);

/*******************************************************************************
Edits the section surface Open API data structure.

Environment: Internal  and  External
See Also: UF_MODL_init_section_surface
          UF_MODL_create_section_surface
          UF_MODL_edit_section_surface

History: V15.0 changes: The UF_MODL_secsrf_data_t structure was enhanced.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_section_surface(
UF_MODL_secsrf_data_p_t section_surface_data ,/* <I>
                                              Section Surface Open API Data
                                              Structure
                                              */
tag_t section_surface  /* <I>
                       Section Surface Feature object identifier.
                       */
);


/*******************************************************************************
Populates a section surface Open API data  structure of a section
surface feature.

Environment: Internal  and  External
See Also: UF_MODL_init_section_surface
          UF_MODL_create_section_surface
          UF_MODL_edit_section_surface


History: V15.0 changes: The UF_MODL_secsrf_data_t structure was enhanced.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_section_surface(
tag_t section_surface ,/* <I>
                       Section Surface Feature object identifier.
                       */
UF_MODL_secsrf_data_p_t section_surface_data  /* <O>
                                              Section Surface Open API Data
                                              Structure
                                              */
);

/******************************************************************************
Creates a midsurface feature.  The returned midsurface feature tag
can then be used to add face pair features.

Environment: Internal  and  External
See Also: UF_MODL_ask_midsrf_parms
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_midsrf_feature(
tag_t target_body ,/* <I>
                   Solid target body to place the Midsurface Feature
                   */
tag_p_t feature_obj_id  /* <O>
                        Midsurface Feature tag
                        */
);
/******************************************************************************
Automatically creates face pairs on a midsurface feature.

Environment: Internal  and  External
See Also:
History: The auto pairing has been modified for NX5 and a
         similar function below can be employed. This function will simply
         default to d/t > 2.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_auto_midsrf_feature(
tag_t feature_obj_id  /* <I>
                      Midsurface Feature tag
                      */
);
/******************************************************************************
Automatically creates face pairs on a midsurface feature.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_auto_midsrf_feature_w_opts(
tag_t feature_obj_id,  /* <I>
                      Midsurface Feature tag
                      */
int autopairoptions,/* <I> 0 for d/t or 1 for thickness option

                      */
double autoval/* <I>      The value of the autopair option
                          logical range of values are
                          1<=d/t<=5 &&
                          t>=0.0
                      */
);

/******************************************************************************
Reads the midsurface parameter data.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_midsrf_parms(
tag_t feature_obj_id ,/* <I>
                      Midsurface Feature tag
                      */
uf_list_p_t *facepair_list /* <OF,free:UF_MODL_delete_list>
                           List of Face Pair Feature tags in the Midsurface
                           Feature.  The space allocated for the list must be
                           freed by calling UF_MODL_delete_list.
                           */
);

/*******************************************************************************
Trims the face pair feature in a midsurface feature.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_trim_midsrf_feature(
tag_t midsrf_feature_obj_id  /* <I>
                             Midsurface Feature tag
                             */
);

/***************************************************************************
*   exports the midsurface data to a file
*
* Environment: Internal  and  External
*
* History: Originally released in NX5.0
 **************************************************************************/
extern UFUNEXPORT int UF_MODL_dump_midsurf_facepair_report
(
    const char *file_name_with_extn,              /*<I> Name of file with relevant extension*/
    tag_t midsrf_feature_obj_id                   /*<I> Midsurface Feature tag*/
);
/******************************************************************************
Asks the creation&trim method (either advanced or classic)

Environment: Internal  and  External
See Also:
History: Originally released in NX5.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_midsrf_feature_create_method(
tag_t feature_obj_id,  /* <I>
                        Midsurface Feature tag
                        */
int *adv_crt_and_trm   /*<O>*/
);
/******************************************************************************
Sets the creation&trim method (either advanced or classic)

Environment: Internal  and  External
See Also:
History: Originally released in NX5.0
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_set_midsrf_feature_create_method(
tag_t feature_obj_id,  /* <I>
                        Midsurface Feature tag
                        */
int adv_crt_and_trm /* <I> choice of advanced create and trim */
);

/*****************************************************************************
Creates a feature by assigning one-to-one correspondence between
points on two selected curves and then connecting the corresponding
points by straight lines. The following restrictions apply:

   1. The first segment curve of each section spine is a starting curve.
   2. Point
      a. Point object may be included but only as the one point of the
         first section string.
      b. Curve end point may be included but only as the one curve of
         the first section string.  s_section->dir[ ] indicates which end
         point should be used.

The output of this function is the object identifier associated to the
feature.

Environment: Internal  and  External
See Also: UF_MODL_create_ruled1
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_create_ruled(
UF_STRING_p_t s_section ,/* <I>
                         Pointer to the section list structure.
                         int     num     Total number of section string
                                         (min=2, max=2)
                         int string[ ]   Total number of segment curves/
                                         sketch identifier of each section
                                         string
                                         (min=1, max =402)
                         int dir[ ]      Direction of each section string
                                            1 = Start to end
                                           -1 = End to start
                         tag_t id[ ]     Identifier of section curve or
                                         the section builder object tags but not both
                         */
UF_STRING_p_t s_spine ,/* <I>
                       Pointer to the spine list structure.
                        (for alignment = 5)
                       int     num     Total number of spine string
                                       (min=0, max=1)
                       int string[ ]   Total number of segment curves/
                                       sketch identifier of each spine
                                       string
                                       (min=1, max=402)
                       int dir[ ]      Direction of each spine string
                                         1 : Start to end
                                        -1 : End to start
                       tag_t id[ ]     Identifier of spine curve or
                                       the section builder object tags but not both
                       */
int * alignment ,/* <I>
                 Alignment method:
                 1 = Parameter
                 2 = Arc length
                 3 = Distance
                 4 = Angles
                 5 = Spine curves
                 */
double  value[6] ,/* <I>
                  Data for alignment method:
                  [0-2] = 3D vector defining direction line (for
                          alignment = 3)
                  [0-5] = 3D start and end coordinates of line
                          defining the axis of revolution for
                          planes (for alignment = 4)
                  */
int * end_point ,/* <I>
                 Curve end point or point
                 0 = Do not use end point
                 1 = Curve/point of first section string
                 */
int * body_type ,/* <I>
                 Type of body:
                 0 = Sheet (Default)
                 1 = Solid
                 */
UF_FEATURE_SIGN boolean ,/* <I>
                         The sign of the operation to be performed.
                         UF_NULLSIGN = create new target solid
                         UF_POSITIVE = add to target solid
                         UF_NEGATIVE = subtract from target solid
                         UF_UNSIGNED = intersect with target solid
                         */
double tol[3] ,/* <I>
               Tolerances:
               [0] = Distance
               [1] = Angle (in radians)
               [2] = Intersection (not used)
               */
tag_t * body_obj_id  /* <O>
                     Body object identifier
                     */
);

/*****************************************************************************
Creates a feature by assigning one-to-one correspondence between points on two
selected curves and then connecting the corresponding points by straight lines.
This function behaves like UF_MODL_create_thru_curves with an extra input
for passing in the target body for the boolean operation.

If body_type is solid (1) and the sign of the operation to be performed is
not create, then the target body is required.

The following restrictions apply:

   1. The first segment curve of each section spine is a starting curve.
   2. Point
      a. Point object may be included but only as the one point of the
         first section string.
      b. Curve end point may be included but only as the one curve of
         the first section string.  s_section->dir[ ] indicates which end
         point should be used.

The output of this function is the object identifier associated to the
feature.

Environment: Internal  and  External
See Also:  UF_MODL_create_ruled
History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_create_ruled1(
UF_STRING_p_t s_section ,/* <I>
                         Pointer to the section list structure.
                         int     num     Total number of section string
                                         (min=2, max=2)
                         int string[ ]   Total number of segment curves/
                                         sketch identifier of each section
                                         string
                                         (min=1, max =402)
                         int dir[ ]      Direction of each section string
                                            1 = Start to end
                                           -1 = End to start
                         tag_t id[ ]     Identifier of section curve or
                                         the section builder object tags but not both
                         */
UF_STRING_p_t s_spine ,/* <I>
                       Pointer to the spine list structure.
                        (for alignment = 5)
                       int     num     Total number of spine string
                                       (min=0, max=1)
                       int string[ ]   Total number of segment curves/
                                       sketch identifier of each spine
                                       string
                                       (min=1, max=402)
                       int dir[ ]      Direction of each spine string
                                         1 : Start to end
                                        -1 : End to start
                       tag_t id[ ]     Identifier of spine curve or
                                         the section builder object tags but not both
                       */
int * alignment ,/* <I>
                 Alignment method:
                 1 = Parameter
                 2 = Arc length
                 3 = Distance
                 4 = Angles
                 5 = Spine curves
                 */
double  value[6] ,/* <I>
                  Data for alignment method:
                  [0-2] = 3D vector defining direction line (for
                          alignment = 3)
                  [0-5] = 3D start and end coordinates of line
                          defining the axis of revolution for
                          planes (for alignment = 4)
                  */
int * end_point ,/* <I>
                 Curve end point or point
                 0 = Do not use end point
                 1 = Curve/point of first section string
                 */
int * body_type ,/* <I>
                 Type of body:
                 0 = Sheet (Default)
                 1 = Solid
                 */
UF_FEATURE_SIGN boolean ,/* <I>
                         The sign of the operation to be performed.
                         UF_NULLSIGN = create new target solid
                         UF_POSITIVE = add to target solid
                         UF_NEGATIVE = subtract from target solid
                         UF_UNSIGNED = intersect with target solid
                         */
tag_t target_body,/* <I>
                   The target body for the boolean operation
                   */
double tol[3] ,/* <I>
               Tolerances:
               [0] = Distance
               [1] = Angle (in radians)
               [2] = Intersection (not used)
               */
tag_t * body_obj_id  /* <O>
                     Body object identifier
                     */
);

/******************************************************************************
Returns the creation data for a Ruled Feature.

Environment: Internal  and  External
See Also:
History:Original release was in V13.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_ruled(
tag_t  feature_obj_id ,/* <I>
                       Feature object identifier
                       */
UF_STRING_p_t s_section ,/* <OF>
                         Pointer to the string list structure for the section
                         strings used to create the feature.
                         Use UF_MODL_free_string_list to deallocate memory.
                         */
UF_STRING_p_t s_spine ,/* <OF>
                       Pointer to the string list structure for the spine
                       string. (for alignment = 5).
                       Use UF_MODL_free_string_list to deallocate memory.
                       */
int * alignment ,/* <O>
                 Alignment method:
                 1 = Parameter
                 2 = Arc length
                 3 = Distance
                 4 = Angles
                 5 = Spine curves
                 */
double  value[6] ,/* <O>
                  Data for alignment method:
                  [0-2] = 3D vector defining direction line (for alignment = 3)
                  [0-5] = 3D start and end coordinates of line
                  defining the axis of revolution for planes (for alignment = 4)
                  */
int * body_type ,/* <O>
                 Type of body:
                 0 = Sheet
                 1 = Solid
                 */
double tol[2]  /* <O>
               Tolerances:
               [0] = Distance
               [1] = Angle (in radians)
               */
);

/*****************************************************************************
Creates a feature through a collection of curves running in two
different directions. The following restrictions apply:

1. The first segment curve of each primary/cross/spine is a starting curve.
2. Points:
   a. A point object may be included, but only as the only one point of the
      first primary string and/or the only one point of the last primary string.

   b. Curve end point may be included but only as the only one point of the
      first primary string and/or the only one point of the last primary string.

   End point option and s_prim->dir[ ] indicates which end point should be used.

3. Spine is optional.  (s_spine->num = 0)
   a. The first/last primary must be planar.
   b. Spine must be perpendicular to the first/last primary.

4. If the Spline Points parameter is set to 1, the input sections must
   all be single B-curves with the same number of defining points.

The output of this function is the object identifier associated to the feature.

Environment: Internal  and  External
See Also: UF_MODL_create_curve_mesh1
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_create_curve_mesh(
UF_STRING_p_t s_prim ,/* <I>
                      Pointer to the primary list structure.
                      int     num     Total number of primary string
                                      (min=2, max=150)
                      int string[ ]   Total number of segment curves/
                                      sketch id of each primary string
                                      (min=1, max =402)
                      int dir[ ]      Direction of each primary string
                                      1 = Start to end
                                     -1 = End to start
                      tag_t id[ ]     Identifier of primary curve/point or
                                      the section builder object tags, but not both
                      */
UF_STRING_p_t s_cross ,/* <I>
                       Pointer to the cross list structure.
                      int     num     Total number of string cross
                                      (min=2, max=150)
                      int string[ ]   Total number of segment curves/
                                      sketch identifier of each string
                                      cross
                                      (min=1, max=402)
                      int dir[ ]      Direction of each string cross
                                      1 = Start to end
                                     -1 = End to start
                      tag_t id[ ]     Identifier of cross curve or
                                      the section builder object tags, but not both
                       */
UF_STRING_p_t s_spine ,/* <I>
                       Pointer to the spine list structure.
                      int     num     Total number of spine string
                                              (min=0, max=1)
                      int string[ ]   Total number of segment curves/
                                              sketch identifier of each spine
                                              string
                                              (min=1, max=402)
                      int dir[ ]      Direction of each spine string
                                              1 = Start to end
                                              -1 = End to start
                      tag_t id[ ]     Identifier of spine curve or
                                      the section builder object tags, but not both
                       */
int * end_point ,/* <I>
                 Curve end point.
                    0 = Do not use end point
                    1 = Curve of first primary string
                    2 = Curve of last primary string
                    3 = Both
                 */
int * emphasis ,/* <I>
                Emphasis flag
                   1 = Primary curves
                   2 = Cross curves
                   3 = Both
                */
int * body_type ,/* <I>
                 Type of body:
                    0 = Sheet (Default)
                    1 = Solid
                 */
int * spline_pts ,/* <I>
                  Spline points flag:
                    0 = Do not reparameterize curves
                    1 = Reparameterize through spline points
                  */
UF_FEATURE_SIGN boolean ,/* <I>
                         The sign of the operation to be performed.
                         UF_NULLSIGN = create new target solid
                         UF_POSITIVE = add to target solid
                         UF_NEGATIVE = subtract from target solid
                         UF_UNSIGNED = intersect with target solid
                         */
double tol[3] ,/* <I>
               Tolerances:
                  [0] = Distance
                  [1] = Angle (in degrees)
                  [2] = Intersection
               */
tag_t c_face_id[4] ,/* <I>
                    Object identifiers of neighbor surfaces or
                    4 collectors of the faces from which
                    constraints are obtained
                         [0] = first primary string
                         [1] = last primary string
                         [2] = first cross string
                         [3] = last cross string
                    No constraint is imposed on the corresponding
                    string if id = NULENT
                    */
int  c_flag[4] ,/* <I>
                Flags indicating constraint types:
                  0 = no constraint
                  1 = tangency constraint
                  2 = curvature constraint
                with
                  [0] = first primary string
                  [1] = last primary string
                  [2] = first cross string
                  [3] = last cross string
                */
tag_t * body_obj_id  /* <O>
                     Body object identifier
                     */
);

/*****************************************************************************
Creates a free form B-surface feature through a collection of curves
running in two different directions.
This function behaves like UF_MODL_create_curve_mesh with the following
enhancements.

1. An extra input for passing in the target body for the boolean operation.
   If body_type is solid (1) and the sign of the operation to be performed
   is not create, then the target body is required.
2. A "simple" option for lighter math representation with fewer poles and
   knots when possible.
3. Face constraints now support multiple faces to be used as constraints
   on all four sides of the body.

RESTRICTIONS -

1. The first segment curve of each primary/cross/spine should be a
        starting curve.
2. Point
  a) Point object may be substituted for the first and/or last primary string.
     This allows the surface to start or terminate at a point.
  b) A curve end point may also be substituted for the first and/or last
     primary string.
     The end_point parameter and s_prim->dir[] will indicate which end point
     is chosen.
3. Spine is optional.  The parameter s_spine->num = 0 indicates no spine.
   If spine is selected then
  a) The first and last primary must be planar.
  b) Spine must be perpendicular to the first and last primary.

Environment: Internal  and  External
See Also:  UF_MODL_create_curve_mesh
History: Originally released in V16.0
****************************************************************************/
extern UFUNEXPORT int UF_MODL_create_curve_mesh1(
UF_STRING_p_t s_prim ,/* <I>
                      Pointer to the primary list structure.

                      When simple option is 2 or 4, then the user supplied
                      template string for primary curves must be added as the
                      last item of this section string structure, but the number
                      of section strings will not be increased.  For example,
                      to create a feature using 3 primary section strings and
                      a user defined primary template (simple option = 2 or 4),
                      num would be 3, but string and dir would have 4
                      elements, string[3] would be the number of segment
                      curves for the user defined primary template, and dir[3]
                      would be the direction for the user defined template.  The
                      tags for the user defined template would be added onto
                      the end of the id array.

                      int num         Total number of primary string
                                      (min=2, max=150)
                      int string[ ]   Total number of segment curves/
                                      sketch id of each primary string
                                      (min=1, max =402)
                      int dir[ ]      Direction of each primary string
                                        1 = Start to end
                                       -1 = End to start
                      tag_t id[ ]     Identifier of primary curve/point or
                                         the section builder object tags, but not both

                      */
UF_STRING_p_t s_cross ,/* <I>
                       Pointer to the cross list structure.

                       When simple option is 3 or 4, then the user supplied
                       template string for cross curves must be added as the
                       last item of this section string structure, but the
                       number of section strings will not be increased.  For
                       example, to create a feature using 3 cross section
                       strings and a user defined cross template (simple option
                       = 3 or 4), num would be 3, but string and dir would have
                       4 elements, string[3] would be the number of segment
                       curves for the user defined cross template, and dir[3]
                       would be the direction for the user defined template.
                       The tags for the user defined template would be added
                       onto the end of the id array.

                       int num        Total number of string cross
                                      (min=2, max=150)
                       int string[ ]  Total number of segment curves/
                                      sketch identifier of each string
                                      cross
                                      (min=1, max=402)
                       int dir[ ]     Direction of each string cross
                                        1 = Start to end
                                       -1 = End to start
                       tag_t id[ ]    Identifier of cross curve or
                                         the section builder object tags, but not both
                       */
UF_STRING_p_t s_spine ,/* <I>
                       Pointer to the spine list structure.
                       int num        Total number of spine string
                                        (min=0, max=1)
                       int string[ ]  Total number of segment curves/
                                        sketch identifier of each spine
                                        string (min=1, max=402)
                       int dir[ ]     Direction of each spine string
                                         1 = Start to end
                                        -1 = End to start
                       tag_t id[ ]    Identifier of spine curve or
                                         the section builder object tags, but not both
                       */
int * end_point ,/* <I>
                 Curve end point.
                   0 = Do not use end point
                   1 = Curve of first primary string
                   2 = Curve of last primary string
                   3 = Both
                 */
int * emphasis ,/* <I>
                Emphasis flag
                  1 = Primary curves
                  2 = Cross curves
                  3 = Both
                */
int * spline_pts ,/* <I>
                  Spline points flag:
                    0 = Do not reparameterize curves
                    1 = Reparameterize through spline points
                  */
int simple ,/* <I>
            Simple math option
              0 : do not use simple creation
              1 : use simple creation with system defined templates
              2 : use simple creation with user supplied template for
                  primary curves.  The user supplied template string will be
                  passed at the end of the s_prim structure above.
              3 : use simple creation with user supplied template for cross
                  curves.  The user supplied template string will be passed
                  at the end of the s_cross structure above.
              4 : use simple creation with user supplied template for both
                  primary and cross curves.  In this case the user supplied
                  template for primary curves will be passed at the end of the
                  s_prim structure above, and the user supplied template for
                  cross curves will be passed at the end of the s_cross
                  structure above.
            */
int * body_type ,/* <I>
                 Type of body:
                    0 = Sheet (Default)
                    1 = Solid
                 */
UF_FEATURE_SIGN boolean ,/* <I>
                         The sign of the operation to be performed.
                           UF_NULLSIGN = create new target solid
                           UF_POSITIVE = add to target solid
                           UF_NEGATIVE = subtract from target solid
                           UF_UNSIGNED = intersect with target solid
                         */
tag_t target_body,  /* <I>
                    The target body for the boolean operation
                    */
double tols[3] ,/* <I>
                Tolerances:
                  [0] = Distance
                  [1] = Angle (in degrees)
                  [2] = Intersection
               */
int c_num[4] ,/* <I>
              Number of constraint faces or collectors of faces
                [0]: First primary string
                [1]: Last primary string
                [2]: First cross string
                [3]: Last cross string
              */
tag_t * c_face_id[4] ,/* <I>
                      Pointers to object identifiers of neighbor surfaces or
                       4 collectors of faces from which constraints are obtained
                        [0] = First primary string
                        [1] = Last primary string
                        [2] = First cross string
                        [3] = Last cross string
                      */
int  c_flag[4] ,/* <I>
                Flags indicating constraint types:
                  0 = No constraint
                  1 = Tangency constraint
                  2 = Curvature constraint
                with
                 [0] = First primary string
                 [1] = Last primary string
                 [2] = First cross string
                 [3] = Last cross string
                */
tag_t * body_obj_id  /* <O>
                     Body object identifier
                     */
);

/******************************************************************************
Returns the creation parameters with which a Curve Mesh feature was created.

Environment: Internal  and  External
See Also:
History:Original release was in V13.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_curve_mesh(
tag_t  feature_obj_id ,/* <I>
                       Feature object identifier
                       */
UF_STRING_p_t s_prim ,/* <OF>
                      Pointer to the string list structure, containing the
                      data defining the primary curves used to create the
                      feature. See structure section of manual for details.
                      Use UF_MODL_free_string_list to deallocate memory.
                      */
UF_STRING_p_t s_cross ,/* <OF>
                       Pointer to the string list structure, containing the
                       data defining the cross curves used to create the
                       feature. See structure section of manual for details.
                       Use UF_MODL_free_string_list to deallocate memory.
                       */
UF_STRING_p_t s_spine ,/* <OF>
                       Pointer to the string list structure for the spine
                       string. See structure section of manual for details.
                       Use UF_MODL_free_string_list to deallocate memory.
                       */
int * emphasis ,/* <O>
                Emphasis flag
                1 = Primary curves
                2 = Cross curves
                3 = Both
                */
int * body_type ,/* <O>
                 Type of body:
                 0 = Sheet
                 1 = Solid
                 */
int * spline_pts ,/* <O>
                  Spline points flag:
                  0 = Do not reparameterize curves
                  1 = Reparameterize through spline points
                  */
double tol[3] ,/* <O>
               Tolerances:
               [0] = Distance
               [1] = Angle (in degrees)
               [2] = Intersection
               */
tag_t c_face_id[4] ,/* <O>
                    Object identifiers of neighbor surfaces from which
                    constraints are obtained
                            [0] = first primary string
                            [1] = last primary string
                            [2] = first cross string
                            [3] = last cross string
                    No constraint is imposed on the corresponding
                    string if id = NULL_TAG
                    */
int  c_flag[4]  /* <O>
                [0] = first primary string constraint type
                [1] = last primary string constraint type
                [2] = first cross string constraint type
                [3] = last cross string constraint type

                The constraint types are as follows:
                   0 = no constraint
                   1 = tangency constraint
                   2 = curvature constraint
                */
);

/*****************************************************************************
Creates a feature through a collection of curves in one direction.  The
following restrictions apply:
   1. The first segment curve of each primary/cross/spine is a starting curve.
   2. If single patch, then vdegree = 0, vclose = 0 (open.) The output of this
      function is the object identifier associated to the feature.
   3. If alignment is set to Spline Points, the input sections must all be
      single B-curves with the same number of defining points.

Environment: Internal  and  External
See Also: UF_MODL_create_thru_curves1

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_create_thru_curves(
UF_STRING_p_t s_section ,/* <I>
                         Pointer to the section list structure.
                         int     num     Total number of section string
                                         (min=2, max=150)
                         int string[ ]   Total number of segment curves/
                                         sketch identifier of each section
                                         string
                                         (min=1, max =402)
                         int dir[ ]      Direction of each section string
                                            1 = Start to end
                                           -1 = End to start
                         tag_t id[ ]     Identifier of section curve or
                                         the section builder object tags, but not both
                         */
UF_STRING_p_t s_spine ,/* <I>
                       Pointer to the spine list structure.
                        (for alignment = 5)
                       int     num     Total number of spine string
                                       (min=0, max=1)
                       int string[ ]   Total number of segment curves/
                                       sketch identifier of each spine
                                       string
                                       (min=1, max=402)
                       int dir[ ]      Direction of each spine string
                                               1 = Start to end
                                              -1 = End to start
                       tag_t id[ ]     Identifier of spine curve or
                                         the section builder object tags, but not both
                       */
int * patch ,/* <I>
             Patch type
              1 = Single (Bezier)
              2 = Multiple (B-spline)
             */
int * alignment ,/* <I>
                 Alignment method
                   1 = Parameter
                   2 = Arc length
                   3 = Distance
                   4 = Angles
                   5= Spine curves
                   6 = Spline Points
                 */
double  value[6] ,/* <I>
                  Data for alignment method:
                    [0-2] = 3D vector defining direction line
                            (for alignment = 3)
                    [0-5] =  Coordinates of line defining the axis
                             of revolution for planes
                             (for alignment = 4)
                  */
int * vdegree ,/* <I>
               Degree of surface in V direction. For patch=2, 0 < vdegree <= (s_section.num-1)
               */
int * vstatus ,/* <I>
               Periodic status of surface in V direction:
                0 = Open
                1 = Closed
               (at least s_section->num > 2)
               */
int * body_type ,/* <I>
                 Type of body=
                      0 = Sheet (Default)
                      1 = Solid
                 */
UF_FEATURE_SIGN boolean ,/* <I>
                         The sign of the operation to be performed.
                         UF_NULLSIGN = create new target solid
                         UF_POSITIVE = add to target solid
                         UF_NEGATIVE = subtract from target solid
                         UF_UNSIGNED = intersect with target solid
                         */
double tol[3] ,/* <I>
               Tolerances:
               [0] = Distance
               [1] = Angle (in radians)
               [2] = Intersection
               */
tag_t c_face_id[2] ,/* <I>
                    Object identifiers of neighbor surfaces
                    or collectors of faces from which constraints are obtained
                    [0] = first section string
                    [1] = last section string
                    */
int c_flag[2] ,/* <I>
               Flags indicating constraint types:
                  0 = no constraint
                  1 = tangency constraint
                  2 = curvature constraint
               with
                  [0] = first primary string
                  [1] = last primary string
               */
tag_t * body_obj_id  /* <O>
                     Body object identifier
                     */
);

/*****************************************************************************
Creates a feature through a collection of curves in one direction.
This function behaves like UF_MODL_create_thru_curves with an extra input
for passing in the target body for the boolean operation.

If body_type is solid (1) and the sign of the operation to be performed is
not create, then the target body is required.

The following restrictions apply:
   1. The first segment curve of each primary/cross/spine is a starting curve.
   2. If single patch, then vdegree = 0, vclose = 0 (open.) The output of this
      function is the object identifier associated to the feature.
   3. If alignment is set to Spline Points, the input sections must all be
      single B-curves with the same number of defining points.

Environment: Internal  and  External
See Also: UF_MODL_create_thru_curves
History: Originally released in V16.0
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_create_thru_curves1(
UF_STRING_p_t s_section ,/* <I>
                         Pointer to the section list structure.

                         When simple option is 2, then the user supplied
                         template string must be added as the last item
                         of this section string structure, but the number of
                         section strings will not be increased.  For example,
                         to create a feature using 3 section strings and
                         a user defined template (simple option = 2),
                         num would be 3, but string and dir would have 4
                         elements, string[3] would be the number of segment
                         curves for the user defined template, and dir[3] would
                         be the direction for the user defined template.  The
                         tags for the user defined template would be added onto
                         the end of the id array.

                         int num         Total number of section strings
                                         (min=2, max=150)
                         int string[ ]   Total number of segment curves/
                                         sketch identifier of each section
                                         string (min=1, max =402)
                         int dir[ ]      Direction of each section string
                                            1 = Start to end
                                           -1 = End to start
                         tag_t id[ ]     Identifier of section curve or
                                         the section builder object tags, but not both
                         */

UF_STRING_p_t s_spine ,/* <I>
                       Pointer to the spine list structure (for alignment = 5).
                       int num         Total number of spine string
                                       (min=0, max=1)
                       int string[ ]   Total number of segment curves/
                                       sketch identifier of each spine string
                                       (min=1, max=402)
                       int dir[ ]      Direction of each spine string
                                          1 = Start to end
                                         -1 = End to start
                       tag_t id[ ]     Identifier of spine curve or
                                         the section builder object tags, but not both
                       */
int * patch ,/* <I>
             Patch type.
               1 = Single (Bezier)
               2 = Multiple (B-spline)
             */
int * alignment ,/* <I>
                 Alignment method.
                   1 = Parameter
                   2 = Arc length
                   3 = Distance
                   4 = Angles
                   5 = Spine curves
                   6 = Spline Points
                 */
double  value[6] ,/* <I>
                  Data for alignment method.
                    [0-2] = 3D vector defining direction line (alignment = 3)
                    [0-5] = Coordinates of line defining the axis of
                            revolution for planes (alignment = 4)
                  */
int * vdegree ,/* <I>
               Degree of surface in V direction. For patch=2, 0< vdegree <= (s_section.num-1)

               */
int * vstatus ,/* <I>
               Periodic status of surface in V direction.
                 0 = Open
                 1 = Closed (At least three section curves are required).
               */
int simple ,/* <I>
            Simple math option
              0 : do not use simple creation
              1 : use simple creation with system defined template
              2 : use simple creation with user supplied template.  The user
                  supplied template will be passed at the end of the s_section
                  structure above.
            */
int * body_type ,/* <I>
                 Type of body.
                   0 = Sheet (Default)
                   1 = Solid
                 */
UF_FEATURE_SIGN boolean ,/* <I>
                         The sign of the operation to be performed.
                           UF_NULLSIGN = create new target solid
                           UF_POSITIVE = add to target solid
                           UF_NEGATIVE = subtract from target solid
                           UF_UNSIGNED = intersect with target solid
                         */
tag_t target_body,/* <I>
                  The target body for the boolean operation.
                  */
double tols[3] ,/* <I>
                Tolerances.
                  [0] = Distance
                  [1] = Angle (in radians)
                  [2] = Intersection
                */
int c_num[2] , /* <I>
               Number of constraint faces or collectors of faces.
                 [0] = First section string
                 [1] = Last section string
               */
tag_t * c_face_id[2] ,/* <I>
                      Pointers to object identifiers of neighbor surfaces or
                        2 collectors of faces
                        from which constraints are obtained
                        [0] = First section string
                        [1] = Last section string
                      */
int c_flag[2] ,/* <I>
               Flags indicating constraint types.
                 0 = No constraint
                 1 = Tangency constraint
                 2 = Curvature constraint
                [0] = First section string
                [1] = Last section string
               */
int c_dir ,/* <I>
           Constraint direction.
             0 = Not specified
             1 = Isoparametric
             2 = Normal to the string
           */
tag_t * body_obj_id  /* <O>
                     Body object identifier.
                     */
);

/******************************************************************************
Returns the creation data for a Thru Curves feature.

Environment: Internal  and  External
See Also:
History: Original release was in V13.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_thru_curves(
tag_t  feature_obj_id ,/* <I>
                       Feature object identifier
                       */
UF_STRING_p_t s_section ,/* <OF>
                         Pointer to the string list structure, containing the
                         data for the section curves used to create the
                         feature. See structure section of manual for details.
                         Use UF_MODL_free_string_list to deallocate memory.
                         */
UF_STRING_p_t s_spine ,/* <OF>
                       Pointer to the string list structure for the spine
                       string. (for alignment = 5).
                       Use UF_MODL_free_string_list to deallocate memory.
                       */
int * patch ,/* <O>
             Patch type
             1 = Single (Bezier)
             2 = Multiple (B-spline)
             */
int * alignment ,/* <O>
                 Alignment method
                 1 = Parameter
                 2 = Arc length
                 3 = Distance
                 4 = Angles
                 5= Spine curves
                 6 = Spline Points
                 */
double  value[6] ,/* <O>
                  Data for alignment method:
                  [0-2] = 3D vector defining direction line
                             (for alignment = 3)
                  [0-5] =  Coordinates of line defining the axis
                             of revolution for planes
                             (for alignment = 4)
                  */
int * vdegree ,/* <O>
               Degree of surface in V direction
               */
int * vstatus ,/* <O>
               Periodic status of surface in V direction:
               0 = Open
               1 = Closed
                   (at least s_section->num > 2)
               */
int * body_type ,/* <O>
                 Type of body,  0 = Sheet, 1 = Solid
                 */
double tol[3] ,/* <O>
               Tolerances:
               [0] = Distance
               [1] = Angle (in radians)
               [2] = Intersection
               */
tag_t c_face_id[2] ,/* <O>
                    Object identifiers of neighbor surfaces from which
                    constraints are obtained
                            [0] = first section string
                            [1] = last section string
                    */
int c_flag[2]  /* <O>
               [0] = first primary string constraint type
               [1] = last primary string constraint type
               The constraint types are as follows:
                  0 = no constraint
                  1 = tangency constraint
                  2 = curvature constraint
               */
);


/*****************************************************************************
Allows you to create free form features by the variable offset method.
You need a base surface and four offset distances from four points on
the surface.

Environment: Internal  and  External
See Also:
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_create_variable_offset(
tag_t   base_sheet ,/* <I>
                    Face or body id of the base sheet
                    */
char * dist[4] ,/* <I>
                Variable offset distances
                */
double uv_param[8] ,/* <I>
                    uv parameters of four specified points
                    */
tag_t * varoff_sheet  /* <O>
                      Body id of the offset sheet
                      */
);

/******************************************************************************
Redefine the base face of a free form offset feature.

Environment:Internal and External
See Also:
History:
*******************************************************************************/
extern UFUNEXPORT int UF_MODL_change_offset_base_face
(
   tag_t offset_feature, /* <I>
                         Offset feature
                         */
   tag_t new_base_face   /* <I>
                         New base face
                         */
);
/*****************************************************************************
Trims or extends a B-surface depending on the trim parameter
values specified. The maximum values must be greater than the
minimum values.

The function trims when the parameter values lie in the range
between 0 and 1. The function extends when the parameter values are
outside the range 0 and 1 (e.g. Umin = -0.1 and Umax = 1.1 would
extend a B-surface in the U direction).  Some B-surfaces, when extended
with large trim parameter values, may give unpredictable results.

Environment: Internal  and  External
See Also:
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_isotrim_face(
tag_t  * sheet_id ,/* <I/O>
                   Face or body identifier of the sheet to be trimmed, on
                   output the identifier of the first face.
                   */
double trim_param[4]  /* <I>
                      Trim parameters:
                      trim_param[0] = U minimum value
                      trim_param[1] = U maximum value
                      trim_param[2] = V minimum value
                      trim_param[3] = V maximum value
                      */
);

/*****************************************************************************
Iso-divides a B-surface using the specified parameter and direction.


Environment: Internal  and  External
See Also:
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_MODL_isodivide_face(
tag_t  * sheet_id ,/* <I/O>
                   Input: Face or body identifier of the sheet to be divided
                   Output: First sheet identifier after division
                   */
double  div_param ,/* <I>
                   Division value:
                   0 < div_param < 1  divides the surface into two
                   pieces.
                   */
int div_dir ,/* <I>
             Division direction:
             0 = constant U
             1 = constant V
             */
tag_t * second_sheet_id  /* <O>
                         Second sheet identifier after division
                         */
);


/****************************************************************************
Creates a single, bicubic, b-surface, sheet body that approximates a
four-sided region of several existing faces. The driver curves or
B-surface must lie inside the boundary of the target surfaces.
Basically, points on a "driver" surface are projected along some given
vector or along the driver surface normal vectors onto the "target"
faces (the ones being approximated). These projected points are then
used to construct the approximating sheet body. You can think of the
projection as a process of emitting a ray from each original point to
hit the target faces.

The accuracy of the approximated sheet body depends on the supplied
tolerances. See the section on tolerances for more information.
Projection Type, Vector, and Size Limit (tol[4])

If the proj_type is set to use driver surface normal, then you do not
need to supply any data for the projection vector (it is ignored if you
do). Otherwise, a projection vector must be specified.

When using surface normal projections, you may supply a tolerance
value (tol[4]). This value helps the algorithm decide which point on
the approximating faces to use if the faces bend around and the
emitted ray finds two intersection points. A value of zero causes the
system to default to 10 times the interior distance tolerance. If your
driver is far from the target (more than 10 times the tolerance), then
you should adjust the projection size limits.

Driver Type
Internally, the driver is always a b-surface. However, for
convenience, we allow you to select a mesh of curves, instead of a
surface. We just build a b-surface internally from this mesh of curves.
Therefore, when you use curves as drivers, they must satisfy all the
conditions required for building a curve-mesh free form.

The last driver type option, self-refit, provides a short-cut way to
approximate a single untrimmed b-surface. You might do this if you are
given a surface of high degree and you want to approximate it with a lower
degree surface (the reparameterize function always outputs bicubic surfaces,
i.e. surfaces of degree 3 in both the U and V directions).

Overlap Checking
If this option is set to "Yes," then the system checks for and tries to
handle overlapping faces. The system tries to intersect each ray with
all nearby faces, and finds the "uppermost" projection point. This can
be a time exhaustive process. If the overlap option is set to "No," the
algorithm assumes that each emitted ray can only hit one target face,
so it stops and proceeds to the next ray as soon as it finds a hit. This is
less time exhaustive if the target faces do not actually overlap, or if
they are close together in the regions where they do overlap.

Curves
The primary and cross curves are only necessary if you indicate the
driver type to be curves. The number of primary and cross curves must
be at least two and less than 50. The number of curves and the curve
tags are ignored if you specify a driver type other than curve. The
curves are going to be used to build a curve-mesh free form.
Therefore, each primary curve must intersect each of the cross curves
once and only once. If you suspect your curves are inappropriate, you
might want to build the curve-mesh free form body yourself before
using the reparameterize function.

If you have specified a driver type of face or self-refit, than specify
the appropriate face tag. Obviously, using an existing driver surface is
much more convenient than using the same set of driving curves over
and over again. So, if you are using the function repeatedly in a loop,
it might be worth constructing the b-surface sheet body to use as a driver.

Tolerances
This allows you to specify the tolerances to be used in the
approximation process. The algorithm actually starts out with a very
simple approximating surface (which is unlikely to be within
tolerance) and then gradually makes it more complex until it is able to
replicate the original shape to within the specified tolerances. Using
tighter tolerances produces a more complex result, and this consumes
storage space and slows down all subsequent operations. Therefore,
the tolerances you use should not be any tighter than they need to be.
We expect the algorithm to be used with distance tolerances of around
.039 to 0.195 inches (1 to 5 mm) and angular tolerances of 2 to 20
degrees. If you use tight angular tolerances on very wavy surfaces, the
algorithm generates huge number of patches. If you set both angular
tolerances to 90 degrees, then angular deviation in not even checked,
which greatly speeds up processing.

To achieve reasonable performance, the algorithm does not rigorously
check the deviation between the approximating face and the originals.
We actually just check a small array of points on each patch of the
approximating face. Experience has shown that this is a reasonable
way to estimate the actual error in practical cases, though one could
certainly construct pathological examples where this approach would fail.

Tighter tolerances may be specified at the edges to assure better
alignment with adjacent faces. Looser tolerances in the interior may
be specified to allow a simpler face to be created.

Target Faces
Faces can lie on a single body or on multiple bodies. Only face tags
may be used. This parameter is ignored if you specified the self-refit
option for driver type.

Output
The function returns the tag of the created sheet body and a flag
stating where the surface was able to meet tolerance. The tolerance
flag has no meaning if a body was not created. The face created is a
bicubic b-surface with double knots, which means it is C1 continuous



In other words, the face is smooth, it does not have any sharp ridges
or cusps. The resulting body is not associative to the input data.

The sheet body may not reach tolerance if, during the approximation
process, one of the patches is found to be smaller in width or length
than the inside distance tolerance. This usually indicates a
perturbation or other anomaly in a region of one of the input faces.
You may wish to analyze the resulting face for deviations, validity, and
shape. The algorithm does not really make any attempt to preserve
the "character" of the input faces, it just tries to stay within tolerance.
Small features sometimes get smoothed away and extraneous wrinkles
may be introduced, especially in areas with tight curvature.

Tips and Techniques
The algorithm assumes that your input faces are reasonably clean. It is
designed to handle certain types of anomalies, such as small gaps
(up to approximately 1mm) overlaps, providing the overlapping faces are
roughly the same height, very thin faces (up to 0.1 mm wide) and duplicate
faces.

In all of the figures that follow in this tips and techniques section we show
a side view of the driver surface and target faces. The driver surface is
always shown above the target faces.  However, the approximation process has
difficulties handling input data in which there are extraneous faces that are
at different heights from the desired face.

For simple shapes, with loose tolerances, a brute force approach, using
just four drive curves, might work okay.  But taking some care in the
constructing drive curves is usually worth the extra effort. If your
target face includes feature lines like long ridges or valleys with
small radius of curvature in one direction, you should try to construct
driver curves that run roughly parallel to these.  This makes it much
easier for the algorithm to achieve tolerance using a reasonably small
number of patches.

It may be a good idea to build several approximating faces, and then sew
them together, instead of trying to approximate the entire area with a
single face. This often produces less data and smaller models. One reason
for this is the natural patch structure for b-surfaces. The "seams" between
patches on a single surface must always run all the way across the surface,
from one edge to the opposite edge. This means that any complexity that gets
introduced into the surface in one area propagates across the entire
surface. If you approximate different regions separately, you can sew
the approximating face together into a sheet body.


Environment: Internal  and  External
See Also: 
History:
 ***************************************************************************/
extern UFUNEXPORT int UF_MODL_create_reparam_sheet(
int proj_type ,/* <I>
               Type of projection
                0 = Use input vector
                1 = Use driver surface normal
               */
int drv_type ,/* <I>
              Type of drive
              0 = Curves
              1 = Face (B-surface type)
              2 = Self-refit (B-surface type)
              */
int check_overlap ,/* <I>
                   Flag for controlling the overlap checking
                   0 = No
                   1 = Yes
                   */
int num_primary ,/* <I>
                 Number of primary curves
                 */
tag_t * prim_cvs ,/* <I,len:num_primary>
                  Object identifiers of the primary curves (face object
                  identifier, if drv_typ != 0)
                  */
int num_cross ,/* <I>
               Number of cross curves
               */
tag_t * cros_cvs ,/* <I,len:num_cross>
                  Object identifiers of the cross curves
                  */
double * proj_vec ,/* <I>
                   Projection vector
                   */
int num_fs ,/* <I>
            Number of target faces
            */
tag_t * faces ,/* <I,len:num_fs>
               Object identifiers of the target faces
               */
double tols[5] ,/* <I>
                Tolerances:
                [0] = Distance tolerance in interior of surface
                [1] = Angular tolerance (in degrees) in interior of
                      surface
                [2] = Outside edge distance tolerance
                [3] = Outside edge angular tolerance (in degrees)
                [4] = Projection size limit (0 - if no limit)
                */
tag_t * new_face ,/* <O>
                  Object identifier of the resultant face
                  */
int * tol_achieved  /* <O>
                    Flag indicating that the resultant face achieved the
                    tolerance requirements.
                    0 = No
                    1 = Yes
                    */
);


/******************************************************************************
Sets the free form construction result preference.  This preference
controls free form feature creation in the Through Curves, Through
Curves Mesh, Swept, and Ruled functions.  If the free form
construction result is 0 and the selected curves are coplanar, a
bounded plane is created.  Otherwise, a B-surface is created.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_set_free_form_result(
int free_form_result  /* <I>
                      free form construction result preference
                      0 = create bounded plane, if selected curves are coplanar.
                      1 = always create B-surface.
                      */
);

/******************************************************************************
Returns the the current setting of the free form construction result
preference. This preference controls free form feature creation in
Through Curves, Through Curves Mesh, Swept, and Ruled functions.
If the free form construction result is 0 and the selected curves are
coplanar, a bounded plane is created. Otherwise, a B-surface is
created.

Environment: Internal  and  External
See Also:
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_free_form_result(
int * free_form_result  /* <O>
                        free form construction result preference
                        0 = create bounded plane, if selected curves are
                        coplanar.
                        1 = always create B-surface.
                        */
);

/*******************************************************************************
Creates the enlarged sheet to the specified type and percentage of based face.
Base face may not be periodic.

Environment: Internal  and  External
See Also:
History: This function is provided in v17 initially.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_enlarge(
tag_t  face,             /*  <I>  tag of the base face of the enlarged sheet  */
int    type,             /*  <I>  enlarge extension type: 0-linear extension; 1-natural extension */
char   *percent_size[4], /*  <I>  Array of the percent increase for the surface parameters.  These are character
                                    pointers to allow for input expressions.
                                    For linear type extensions, the range is from [0, 100], with 0 meaning no increase,
                                    and 100 meaning a 100% increase.
                                    For natural type extensions, the range is from [-99, +100], with -99 meaning a 99%
                                    decrease or shrinkage of the surface, and +100 meaning a 100% increase.

                                    percent_size[0] is the percent for U-min
                                    percent_size[1] is the percent for U-max
                                    percent_size[2] is the percent for V-min
                                    percent_size[3] is the percent for V-max  */

double tolerance,        /* <I>  Distance tolerance for approximations. */
tag_t  *feat_obj_tag    /* <O>  tag of the feature record of the enlarged sheet */
);

/*******************************************************************************
Modifies data of the input enlarged sheet feature to the specified type and size
conditions in the inputs.

Environment: Internal  and  External
See Also:
History: This function is provided in v17 initially.
********************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_enlarge(
tag_t feat_obj_tag,     /* <I>  tag of the feature record of the enlarged sheet */
int   type,             /* <I>  enlarge extension type: 0-linear extension; 1-natural extension */
char  *percent_size[4], /* <I>  Array of the percent increase for the surface parameters.  These are character
                                  pointers to allow for input expressions.
                                  For linear type extensions, the range is from [0, 100], with 0 meaning no increase,
                                  and 100 meaning a 100% increase.
                                  For natural type extensions, the range is from [-99, +100], with -99 meaning a 99%
                                  decrease or shrinkage of the surface, and +100 meaning a 100% increase.

                                  percent_size[0] is the percent for U-min
                                  percent_size[1] is the percent for U-max
                                  percent_size[2] is the percent for V-min
                                  percent_size[3] is the percent for V-max  */
double tolerance       /* <I>  Distance tolerance for approximations. */
);

/*******************************************************************************
Returns the information stored in the record of the input enlarged sheet feature.

Environment: Internal  and  External
See Also:
History: This function is provided in v17 initially.
********************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_enlarge(
tag_t feat_obj_tag,     /* <I> tag of the feature record of the enlarged sheet  */
tag_t *face,            /* <O> tag of the base face of the enlarged sheet */
int   *type,            /* <O> enlarge extension type: 0-linear extension; 1-natural extension */
char  *percent_size[4], /* <OF> Array of the percent increase for the surface parameters.  These are character
                                pointers to allow for input expressions.
                                For linear type extensions, the range is from [0 ,100], with 0 meaning no increase,
                                and 100 meaning a 100% increase.
                                For natural type extensions, the range is from [-99, +100], with -99 meaning a 99%
                                decrease or shrinkage of the surface, and +100 meaning a 100% increase.

                                percent_size[0] is the percent for U-min
                                percent_size[1] is the percent for U-max
                                percent_size[2] is the percent for V-min
                                percent_size[3] is the percent for V-max

                                This array must be free by calling
                                UF_free ( percent_size[0])
                                UF_free ( percent_size[1])
                                UF_free ( percent_size[2])
                                UF_free ( percent_size[3])  */
double *tolerance      /* <O> Distance tolerance for approximations */
);

/************************************************************************
  This function will create a rough offset feature.

  Environment : Internal  and  External
  See  Also:  UF_MODL_ask_rough_offset
              UF_MODL_edit_rough_offset
              UF_MODL_free_rough_offset
  History : Released in V18.0
 *************************************************************************/
extern UFUNEXPORT int UF_MODL_create_rough_offset (
    UF_MODL_rough_offset_p_t parms,          /* <I>  Parameters for a
                                                     Rough Offset feature*/
    tag_t                   *feature_tag     /* <O>  Rough Offset Feature */
);

/************************************************************************
  This function will edit a rough offset feature.

  Environment : Internal  and  External
  See  Also:  UF_MODL_ask_rough_offset
              UF_MODL_create_rough_offset
              UF_MODL_free_rough_offset
  History : Released in V18.0
 *************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_rough_offset (
    tag_t                    feature_tag,    /* <I> Feature to be queried */
    UF_MODL_rough_offset_p_t parms           /* <I> New parameters for changing
                                                    a Rough Offset feature*/
);

/************************************************************************
  This function will inquire and return parameters of a rough offset feature.

  Environment : Internal  and  External
  See  Also:  UF_MODL_create_rough_offset
              UF_MODL_edit_rough_offset
              UF_MODL_free_rough_offset
  History : Released in V18.0
 *************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_rough_offset (
    tag_t                    feature_tag,    /* <I>  Feature to be queried */
    UF_MODL_rough_offset_p_t parms           /* <OF>  Parameters for a
                                                     Rough Offset feature*/
);

/************************************************************************
  This function will free the entity list in the parameters data structure of a rough offset feature.

  Environment : Internal  and  External
  See  Also:  UF_MODL_create_rough_offset
              UF_MODL_ask_rough_offset
              UF_MODL_edit_rough_offset
  History : Released in V18.0
 *************************************************************************/
extern UFUNEXPORT void UF_MODL_free_rough_offset_data (
   UF_MODL_rough_offset_p_t parms           /* <I> parameters to be deleted */
);

/*****************************************************************************
Creates Law Extension feature from the Law Extension Open API data structure.

Environment: Internal  and  External
See Also:     UF_MODL_edit_law_extension
              UF_MODL_ask_law_extension
              UF_MODL_free_law_extension
History:
******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_law_extension
(
   UF_MODL_lawext_data_p_t law_extension_data, /* <I> Law Extension Open
                                                  API data structure. */
   tag_p_t law_extension                       /* <O> Law Extension feature
                                                  object identifier. */
);

/*****************************************************************************
Edits existing Law Extension feature based on the Law Extension Open API
data structure.

Environment: Internal  and  External
See Also:     UF_MODL_create_law_extension
              UF_MODL_ask_law_extension
              UF_MODL_free_law_extension
History:
******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_law_extension
(
   UF_MODL_lawext_data_p_t law_extension_data, /* <I> Law Extension Open
                                                  API data structure. */
   tag_t law_extension                         /* <I> Law Extension feature
                                                  object identifier. */
);

/*****************************************************************************
Inquires Law Extension feature and populates Law Extension Open API data
structure. A copy of length and angle law is provided in the data structure.
The memory allocated for the structure may be freed using
UF_MODL_free_law_extension().

This function will always return an array of faces no matter if that array
is defined by a collection.  See UF_MODL_ask_law_extension1() for the
collector enabled version of this function.

Environment: Internal  and  External
See Also:     UF_MODL_create_law_extension
              UF_MODL_edit_law_extension
              UF_MODL_free_law_extension
History:
******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_law_extension
(
   tag_t law_extension,                        /* <I> Law Extension feature
                                                  object identifier. */
   UF_MODL_lawext_data_p_t law_extension_data  /* <O> Law Extension Open
                                                  API data structure. */
);

/*****************************************************************************
Inquires Law Extension feature and populates Law Extension Open API data
structure. A copy of length and angle law is provided in the data structure.
The memory allocated for the structure may be freed using
UF_MODL_free_law_extension().

If this is a collector enabled Law Extension then the collection will be
retuned instead of the array of faces.  See UF_MODL_ask_law_extension() for
the non-collector enabled version of this function.

Environment: Internal  and  External
See Also:     UF_MODL_create_law_extension
              UF_MODL_edit_law_extension
              UF_MODL_free_law_extension
History:
******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_law_extension1
(
   tag_t law_extension,                        /* <I> Law Extension feature
                                                  object identifier. */
   UF_MODL_lawext_data_p_t law_extension_data  /* <O> Law Extension Open
                                                  API data structure. */
);

/******************************************************************************
Deallocates memory used for a Law Extension Open API data structure.
The flag free_laws, is used to decide if distance and angle laws are to be
freed. If the laws are not freed in this function, user may use
UF_MODL_free_law() to free the laws individually.

Environment: Internal  and  External
See Also:     UF_MODL_create_law_extension
              UF_MODL_edit_law_extension
              UF_MODL_ask_law_extension
History:
******************************************************************************/
extern UFUNEXPORT void UF_MODL_free_law_extension
(
   UF_MODL_lawext_data_p_t law_extension_data,  /* <I> Law Extension Open
                                                   API data structure to be
                                                   freed. */
   logical free_laws                            /* <I> If TRUE, frees
                                                   distance and angle law else
                                                   not */
);

/******************************************************************************
Returns the creation parameters with which a Curve Mesh feature was created.

Environment: Internal  and  External
See Also:
History:Original release was in NX2.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_curve_mesh1
(
tag_t  feature_obj_id ,/* <I>
                       Feature object identifier
                       */
UF_STRING_p_t s_prim ,/* <OF>
                      Pointer to the string list structure, containing the
                      section builder objects defining the primary curves
                      used to create the feature. See structure section of
                      manual for details.
                      Use UF_MODL_free_string_list to deallocate memory.
                      */
UF_STRING_p_t s_cross ,/* <OF>
                       Pointer to the string list structure, containing the
                       section builder objects defining the cross curves used to create the
                       feature. See structure section of manual for details.
                       Use UF_MODL_free_string_list to deallocate memory.
                       */
UF_STRING_p_t s_spine ,/* <OF>
                       Pointer to the string list structure for the spine
                       string. See structure section of manual for details.
                       Use UF_MODL_free_string_list to deallocate memory.
                       */
int * emphasis ,/* <O>
                Emphasis flag
                1 = Primary curves
                2 = Cross curves
                3 = Both
                */
int * body_type ,/* <O>
                 Type of body:
                 0 = Sheet
                 1 = Solid
                 */
int * spline_pts ,/* <O>
                  Spline points flag:
                  0 = Do not reparameterize curves
                  1 = Reparameterize through spline points
                  */
double tol[3] ,/* <O>
               Tolerances:
               [0] = Distance
               [1] = Angle (in degrees)
               [2] = Intersection
               */
tag_t c_collector_id[4] ,/* <O>
                    Collector containing the neighbor surfaces from which
                    constraints are obtained
                            [0] = first primary string
                            [1] = last primary string
                            [2] = first cross string
                            [3] = last cross string
                    No constraint is imposed on the corresponding
                    string if id = NULL_TAG
                    */
int  c_flag[4]  /* <O>
                [0] = first primary string constraint type
                [1] = last primary string constraint type
                [2] = first cross string constraint type
                [3] = last cross string constraint type

                The constraint types are as follows:
                   0 = no constraint
                   1 = tangency constraint
                   2 = curvature constraint
                */
);

/******************************************************************************
Returns the creation data for a Thru Curves feature.

Environment: Internal  and  External
See Also:
History: Original release was in NX2.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_thru_curves1
(
tag_t  feature_obj_id ,/* <I>
                       Feature object identifier
                       */
UF_STRING_p_t s_section ,/* <OF>
                         Pointer to the string list structure, containing the
                         section builder objects defining the section curves used to create the
                         feature. See structure section of manual for details.
                         Use UF_MODL_free_string_list to deallocate memory.
                         */
UF_STRING_p_t s_spine ,/* <OF>
                       Pointer to the string list structure for the spine
                       string. (for alignment = 5).
                       Use UF_MODL_free_string_list to deallocate memory.
                       */
int * patch ,/* <O>
             Patch type
             1 = Single (Bezier)
             2 = Multiple (B-spline)
             */
int * alignment ,/* <O>
                 Alignment method
                 1 = Parameter
                 2 = Arc length
                 3 = Distance
                 4 = Angles
                 5= Spine curves
                 6 = Spline Points
                 */
double  value[6] ,/* <O>
                  Data for alignment method:
                  [0-2] = 3D vector defining direction line
                             (for alignment = 3)
                  [0-5] =  Coordinates of line defining the axis
                             of revolution for planes
                             (for alignment = 4)
                  */
int * vdegree ,/* <O>
               Degree of surface in V direction
               */
int * vstatus ,/* <O>
               Periodic status of surface in V direction:
               0 = Open
               1 = Closed
                   (at least s_section->num > 2)
               */
int * body_type ,/* <O>
                 Type of body,  0 = Sheet, 1 = Solid
                 */
double tol[3] ,/* <O>
               Tolerances:
               [0] = Distance
               [1] = Angle (in radians)
               [2] = Intersection
               */
tag_t c_collector_id[2] ,/* <O>
                    Collector containing the neighbor surfaces from which
                    constraints are obtained
                            [0] = first section string
                            [1] = last section string
                    */
int c_flag[2]  /* <O>
               [0] = first primary string constraint type
               [1] = last primary string constraint type
               The constraint types are as follows:
                  0 = no constraint
                  1 = tangency constraint
                  2 = curvature constraint
               */
);

/******************************************************************************
Returns the creation data for a Ruled Feature.

Environment: Internal  and  External
See Also:
History:Original release was in V13.0.
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_ruled1
(
tag_t  feature_obj_id ,/* <I>
                       Feature object identifier
                       */
UF_STRING_p_t s_section ,/* <OF>
Pointer to the string list structure, containing the
                         section builder objects defining the section curves used to create the
                         feature. See structure section of manual for details.
                         Use UF_MODL_free_string_list to deallocate memory.
                         */
UF_STRING_p_t s_spine ,/* <OF>
                       Pointer to the string list structure for the spine
                       string. (for alignment = 5).
                       Use UF_MODL_free_string_list to deallocate memory.
                       */
int * alignment ,/* <O>
                 Alignment method:
                 1 = Parameter
                 2 = Arc length
                 3 = Distance
                 4 = Angles
                 5 = Spine curves
                 */
double  value[6] ,/* <O>
                  Data for alignment method:
                  [0-2] = 3D vector defining direction line (for alignment = 3)
                  [0-5] = 3D start and end coordinates of line
                  defining the axis of revolution for planes (for alignment = 4)
                  */
int * body_type ,/* <O>
                 Type of body:
                 0 = Sheet
                 1 = Solid
                 */
double tols[2]  /* <O>
               Tolerances:
               [0] = Distance
               [1] = Angle (in radians)
               */
);

/******************************************************************************
Creates Match Edge feature from the Match Edge Open API data structure.
The returned integer is error status: 0 for no error; 1 for no memory; 2 for creation failure; 3 for others.
The memory allocated for uf_data can be freed using UF_MODL_matchedge_free_data().

Enviroment: Internal and External.
See Also:     UF_MODL_matchedge_edit_feature
              UF_MODL_matchedge_ask_data
              UF_MODL_matchedge_free_data
              UF_MODL_matchedge_check
History: Original release was in NX2.0.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_matchedge_create_feature
(
    UF_MODL_matchedge_data_p_t uf_data,   /* <I> Match Edge Open API data structure */
    tag_t                      *frec_tag  /* <O> Match Edge feature object identifier */
);

/******************************************************************************
Edits existing Match Edge feature based on the Match Edge Open API data structure.
The returned integer is error status: 0 for no error; 1 for no memory; 2 for creation failure; 3 for others.
The memory allocated for uf_data can be freed using UF_MODL_matchedge_free_data().

Enviroment: Internal and External.
See Also:     UF_MODL_matchedge_create_feature
              UF_MODL_matchedge_ask_data
              UF_MODL_matchedge_free_data
              UF_MODL_matchedge_check
History: Original release was in NX2.0.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_matchedge_edit_feature
(
    UF_MODL_matchedge_data_p_t  uf_data,  /* <I> Match Edge Open API data structure */
    tag_t                       frec_tag  /* <I> Match Edge feature object identifier */
);

/******************************************************************************
Inquires Match Edge feature and populates Match Edge Open API data structure.
The memory allocated for the structure may be freed using UF_MODL_matchedge_free_data().

Enviroment: Internal and External.
See Also:     UF_MODL_matchedge_create_feature
              UF_MODL_matchedge_edit_feature
              UF_MODL_matchedge_free_data
              UF_MODL_matchedge_check
History: Original release was in NX2.0.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_matchedge_ask_data
(
    tag_t                       medge_tag, /* <I> Match Edge feature object identifier */
    UF_MODL_matchedge_data_p_t *uf_medge   /* <OF,free:UF_MODL_matchedge_free_data>
                                                Match Edge Open API data structure */
);

/******************************************************************************
Deallocates memory used for a Match Edge Open API data structure.

Enviroment: Internal and External.
See Also:     UF_MODL_matchedge_create_feature
              UF_MODL_matchedge_edit_feature
              UF_MODL_matchedge_ask_data
              UF_MODL_matchedge_check
History: Original release was in NX2.0.
******************************************************************************/
extern UFUNEXPORT void UF_MODL_matchedge_free_data
(
 UF_MODL_matchedge_data_p_t medge_data /* <I> Match Edge Open API data structure to be freed */
);/* <NON_NXOPEN> */


/******************************************************************************
Computes the edge/edeg deviations after using UF_MODL_matchedge_create_feature()
or UF_MODL_matchedge_edit_feature().

Enviroment: Internal and External.
See Also:     UF_MODL_matchedge_create_feature
              UF_MODL_matchedge_edit_feature
              UF_MODL_matchedge_free_data
              UF_MODL_matchedge_free_data
History: Original release was in NX2.0.
******************************************************************************/
extern UFUNEXPORT int UF_MODL_matchedge_check
(
    UF_MODL_matchedge_data_t* uf_data, /* <I> Match Edge Open API data structure */
    int continuity,                    /* <I> 0, 1, 2, or 3, for desired continuity check */
    int num_pnts,                      /* <I> number of points used in computing deviations */
    double* deviation                  /* <O,len:continuity+1> array of deviations, its length is 1 + continuity,
                                          deviation[0] for G0 deviation,
                                          deviation[1] for G1 deviation in degree,
                                          deviation[2] for relative G2 deviation,
                                          deviation[3] for relative G3 deviation*/
);



/*****************************************************************************
Creates Refit Face feature from the Refit Face Open API data structure.
This will always create a new feature rather than modifying the parent feature.
This works like interactive NXwhen Preferences -> Modeling -> Free Form has
the Associative Freeform Editing option toggled to ON.

Environment: Internal  and  External
See Also:     UF_MODL_edit_refit_face_feature
              UF_MODL_ask_refit_face_feature_data
              UF_MODL_free_refit_face_feature_data
History:
******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_refit_face_feature
(
   UF_MODL_refit_face_data_p_t refit_data, /* <I> Refit Face Open API data structure. */
   tag_p_t refit                      /* <O> Refit Face feature object identifier. */
);

/*****************************************************************************
Edits existing Refit Face feature based on the Refit Face Open API data
structure.

Environment: Internal  and  External
See Also:     UF_MODL_create_refit_face_feature
              UF_MODL_ask_refit_face_feature_data
              UF_MODL_free_refit_face_feature_data
History:
******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_refit_face_feature
(
   UF_MODL_refit_face_data_p_t refit_data, /* <I> Refit Face Open API data structure. */
   tag_t refit                        /* <I> Refit Face feature object identifier. */
);

/*****************************************************************************
Inquires Refit Face feature and populates Refit Face Open API data
structure.  The memory allocated for the structure may be freed using
UF_MODL_free_refit_face_feature_data().

Environment: Internal  and  External
See Also:     UF_MODL_create_refit_face_feature
              UF_MODL_edit_refit_face_feature
              UF_MODL_free_refit_face_feature_data
History:
******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_refit_face_feature_data
(
   tag_t refit,                       /* <I> Refit Face feature object identifier. */
   UF_MODL_refit_face_data_p_t refit_data  /* <O> Refit Face Open API data structure. */
);

/******************************************************************************
Deallocates memory used for a Refit Face Open API data structure.

Environment: Internal  and  External
See Also:     UF_MODL_create_refit_face_feature
              UF_MODL_edit_refit_face_feature
              UF_MODL_ask_refit_face_feature_data
History:
******************************************************************************/
extern UFUNEXPORT void UF_MODL_free_refit_face_feature_data
(
   UF_MODL_refit_face_data_p_t refit_data  /* <I> Refit Face Open API data structure. */
);

/*****************************************************************************
Creates a Snip Surface Feature using the Snip surface Open API data  structure.
Make sure the following items are initialized properly:
usr_data->edit_face != 0  
usr_data->project_method <= 3
usr_data->refit_method <= 3
usr_data->refit_degree > 0 
usr_data->refit_degree < 25 
usr_data->refit_patches > 0 
usr_data->refit_patches < 1000

Minimum five parameters are required to be specified as follows:
 1.Edit face
 2.One of the types of bounding objects
 3.Type of operation (snipping or divide)
 4.Region point
 5.Surface refitting method

Environment: Internal  and  External
See Also:     UF_MODL_create_snip_surface_feature
              UF_MODL_ask_snip_surface_feature_data
              UF_MODL_free_snip_surface_feature_data
History:    First released in NX2
******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_snip_surface_feature
(
    UF_MODL_snipsrf_feature_data_p_t usr_data, /* <I> */
    tag_p_t snip_tag /* <O> */
);


/******************************************************************************

Edits an existing Snip Surface feature based on a Open API data structure.
Environment: Internal  and  External

See Also:     UF_MODL_create_snip_surface_feature
              UF_MODL_ask_snip_surface_feature_data
              UF_MODL_free_snip_surface_feature_data

History:    First released in NX2
******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_snip_surface_feature
(
    UF_MODL_snipsrf_feature_data_p_t usr_data, /* <I> */
    tag_t snip /* <I> */
);


/******************************************************************************
Deallocates memory used for a Snip Surface Open API data structure.
Environment: Internal  and  External

See Also:     UF_MODL_create_snip_surface_feature
              UF_MODL_edit_snip_surface_feature
              UF_MODL_ask_snip_surface_feature_data

History:    First released in NX2
******************************************************************************/
extern UFUNEXPORT void UF_MODL_free_snip_surface_feature_data
(
    UF_MODL_snipsrf_feature_data_p_t usr_data_ptr /* <I> */
);


/******************************************************************************
Populates Snip Surface Open API data structure of a Snip Surface feature. The
memory allocated for the structure may be freed using UF_MODL_free_snip_surface
Environment: Internal  and  External

See Also:     UF_MODL_create_snip_surface_feature
              UF_MODL_edit_snip_surface_feature
              UF_MODL_free_snip_surface_feature_data

History:   First released in NX2
******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_snip_surface_feature_data
(
    tag_t snip, /* <I> */
    UF_MODL_snipsrf_feature_data_p_t ask_usr_data_ptr /* <O> */
);

/*****************************************************************************
Initializes Silhouette Flange Open API data structure.

Environment: Internal  and  External
See Also:     UF_MODL_edit_silhouette_flange
              UF_MODL_ask_silhouette_flange
              UF_MODL_free_silhouette_flange
History: First released in NX4
******************************************************************************/
extern UFUNEXPORT int UF_MODL_init_silhouette_flange_data
(
   UF_MODL_sflange_data_p_t sflange_data /* <O> Silhouette Flange Open API
                                                data structure. */
);

/*****************************************************************************
Creates Silhouette Flange feature from the Silhouette Flange Open API data structure.

Environment: Internal  and  External
See Also:     UF_MODL_edit_silhouette_flange
              UF_MODL_ask_silhouette_flange
              UF_MODL_free_silhouette_flange
History: First released in NX3
******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_silhouette_flange
(
   UF_MODL_sflange_data_p_t sflange_data, /* <I> Silhouette Flange Open API
                                                 data structure. */
   tag_t                    *sflange_tag  /* <O> Silhouette Flange feature
                                                 object identifier. */
);

/*****************************************************************************
Creates Pipe of Silhouette Flange from the Silhouette Flange Open API data structure.

Environment: Internal  and  External
See Also:     UF_MODL_edit_silhouette_flange
              UF_MODL_ask_silhouette_flange
              UF_MODL_free_silhouette_flange
History: First released in NX3
******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_silhouette_flange_pipe
(
   UF_MODL_sflange_data_p_t sflange_data,   /* <I> Silhouette Flange Open API
                                                   data structure. */
   tag_t                    *centerline_tag /* <O> Centerline curve object identifier
                                                   of the pipe of Silhouette Flange. */
);


/*****************************************************************************
Edits existing Silhouette Flange feature based on the Silhouette Flange Open API
data structure.

Environment: Internal  and  External
See Also:     UF_MODL_create_silhouette_flange
              UF_MODL_ask_silhouette_flange
              UF_MODL_free_silhouette_flange
History:  First released in NX3
******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_silhouette_flange
(
   UF_MODL_sflange_data_p_t sflange_data, /* <I> Silhouette Flange Open API
                                                 data structure. */
   tag_t                    sflange_tag   /* <I> Silhouette Flange feature
                                                   object identifier. */
);

/*****************************************************************************
Inquires Silhouette Flange feature and populates Silhouette Flange Open API data
structure. A copy of length and angle law is provided in the data structure.
The memory allocated for the structure may be freed using
UF_MODL_free_silhouette_flange().

This function will always return an array of faces no matter if that array
is defined by a collection.

Environment: Internal  and  External
See Also:     UF_MODL_create_silhouette_flange
              UF_MODL_edit_silhouette_flange
              UF_MODL_free_silhouette_flange
History:  First released in NX3
******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_silhouette_flange
(
   tag_t                   sflange_tag,   /* <I> Silhouette Flange feature
                                                 object identifier. */
   UF_MODL_sflange_data_p_t sflange_data  /* <O> Silhouette Flange Open API
                                                 data structure. */
);

/******************************************************************************
Deallocates memory used for a Silhouette Flange Open API data structure.

Environment: Internal  and  External
See Also:     UF_MODL_create_silhouette_flange
              UF_MODL_edit_silhouette_flange
              UF_MODL_ask_silhouette_flange
History:  First released in NX3
******************************************************************************/
extern UFUNEXPORT void UF_MODL_free_silhouette_flange
(
   UF_MODL_sflange_data_p_t sflange_data  /* <I> Silhouette Flange Open API
                                                 data structure to be freed. */
);


/*======================================================================
 Three (4) User Functions for the Styled Corner Surface Feature using
 its  NX Open API data  structure:
    UF_MODL_stycorner_data_p_t.

 1. To CREATE from data structure the Styled Corner Surface Feature, use
    UF_MODL_create_stycorner();

 2. To EDIT the Styled Corner Surface Feature, use
    UF_MODL_edit_stycorner();

 3. To GET DATA from the Styled Corner Surface Feature, use
    UF_MODL_ask_stycorner_data();


 4. To INITIALIZE DATA for a Styled Corner Surface Feature,

    use

    UF_MODL_init_stycorner_data().


======================================================================*/

/******************************************************************************
Creates an Styled Corner Surface Feature using its NX Open API data  structure.

Environment: Internal  and  External
See Also:     UF_MODL_create_stycorner
              UF_MODL_edit_stycorner
              UF_MODL_ask_stycorner_data
              UF_MODL_init_stycorner_data
History:     First released in NX3
***************************************************************************************/
extern UFUNEXPORT int UF_MODL_create_stycorner
(
 UF_MODL_stycorner_data_p_t   styled_corner_data,  /* <I> Styled corner NX Open
                                                          API data structure.         */
 tag_t                       *frec_tag             /* <O> the object identifier to be created    */
 );


/******************************************************************************
Edit an Styled Corner Surface Feature using its NX Open API data  structure.

Environment: Internal  and  External
See Also:     UF_MODL_create_stycorner
              UF_MODL_edit_stycorner
              UF_MODL_ask_stycorner_data
              UF_MODL_init_stycorner_data
History:     First released in NX3
**********************************************************************************/
extern UFUNEXPORT int  UF_MODL_edit_stycorner
(
 UF_MODL_stycorner_data_p_t styled_corner_data, /* <I> Styled corner NX Open
                                                       API data structure.       */
 tag_t                          frec_tag        /* <I> the object identifier to be edited */
);

/******************************************************************************
Get an Styled Corner Surface Feature data from its NX Open API data  structure.

Environment: Internal  and  External
See Also:     UF_MODL_create_stycorner
              UF_MODL_edit_stycorner
              UF_MODL_ask_stycorner_data
              UF_MODL_init_stycorner_data
History:     First released in NX3
*************************************************************************************/
extern UFUNEXPORT int  UF_MODL_ask_stycorner_data
(
 tag_t                       frec_tag,    /* <I> Styled corner feature
                                             object identifier. */
 UF_MODL_stycorner_data_p_t  styled_corner_data_out   /* <O> Styled corner NX Open
                                                           API data structure. */
 );


/********************************************************************************
Initialize data for Styled Corner Surface Feature  NX Open API data  structure.

The following values are set for the Styled Corner data:
--------------------------------------------------------
.num_base_faces   = 0;
.base_faces       = NULENT;

.blend_faces[3]   = NULTAG;

.is_rectangular   = 0;
.interior_opt     = 0;
.trim_attach_opt  = 0;

.boundary_conds[4]= 1;

.crv_opt[4].depth = .500;
.crv_opt[4].skew  = .500;

.crv_opt[4].start_tagmag    = 1.0;
.crv_opt[4].end_tagmag      = 1.0;

.crv_opt[4].shape_control   = 1;

.trim_curve_opt[2] = 2;

.interior_iso_u_crv_end_params[2]= 0.5;
.interior_iso_v_crv_end_params[2]= 0.5;

.dist_tol  =  0.001;
.angle_tol =  0.1;
--------------------------------------------------------

Environment: Internal  and  External
See Also:     UF_MODL_create_stycorner
              UF_MODL_edit_stycorner
              UF_MODL_ask_stycorner_data
              UF_MODL_init_stycorner_data
History:     First released in NX3
******************************************************************************/
extern UFUNEXPORT int  UF_MODL_init_stycorner_data
(
  UF_MODL_stycorner_data_p_t  styled_corner_data   /* <I/O> Styled corner NX Open
                                                           API data structure. */
 );


/*****************************************************************************
Creates Styled Sweep feature from the Styled Sweep Open API data structure.

Environment: Internal  and  External
See Also:     UF_MODL_edit_styled_sweep_feature
              UF_MODL_ask_styled_sweep_feature_data
              UF_MODL_free_styled_sweep_feature_data
History:
******************************************************************************/
extern UFUNEXPORT int UF_MODL_create_styled_sweep_feature
(
    UF_MODL_styled_sweep_data_p_t styled_sweep_data,  /* <I> Styled Sweep Open API data structure. */
    tag_p_t                       styswp  /* <O> Styled Sweep feature object identifier. */
);

/*****************************************************************************
Edits existing Styled Sweep feature based on the Styled Sweep Open API data
structure.

Environment: Internal  and  External
See Also:     UF_MODL_create_styled_sweep_feature
              UF_MODL_ask_styled_sweep_feature_data
              UF_MODL_free_styled_sweep_feature_data
History:
******************************************************************************/
extern UFUNEXPORT int UF_MODL_edit_styled_sweep_feature
(
    UF_MODL_styled_sweep_data_p_t styled_sweep_data,  /* <I> Styled Sweep Open API data structure. */
    tag_t                         styswp  /* <I> Styled Sweep feature object identifier. */
);

/*****************************************************************************
Inquires Styled Sweep feature and populates Styled Sweep Open API data
structure.  The memory allocated for the structure may be freed using
UF_MODL_free_styled_sweep_feature_data().

Environment: Internal  and  External
See Also:     UF_MODL_create_styled_sweep_feature
              UF_MODL_edit_styled_sweep_feature
              UF_MODL_free_styled_sweep_feature_data
History:
******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_styled_sweep_feature_data
(
    tag_t                         styswp,  /* <I> Styled Sweep feature object identifier. */
    UF_MODL_styled_sweep_data_p_t styled_sweep_data    /* <O> Styled Sweep Open API data structure. */
);

/******************************************************************************
Deallocates memory used for a Styled Sweep Open API data structure.

Environment: Internal  and  External
See Also:     UF_MODL_create_styled_sweep_feature
              UF_MODL_edit_styled_sweep_feature
              UF_MODL_ask_styled_sweep_feature_data
History:
******************************************************************************/
extern UFUNEXPORT void UF_MODL_free_styled_sweep_feature_data
(
    UF_MODL_styled_sweep_data_p_t styled_sweep_data  /* <I> Styled Sweep Open API data structure. */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_FREEFORM_H_INCLUDED */

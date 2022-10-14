/*******************************************************************************
             Copyright (c) 1998-2000 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved




File Description:

Open API interface to boundary representation routines.  This allows you
to extract and create NX solid and sheet bodies.

The UF_BREP module is the basis for NX application code requiring a high level
interface to create and inquire about topology and geometry for solid bodies
and trimmed surfaces.

For a non-trivial working Open API program that uses the UF_BREP module
see ufx_brep.c

The two main uses of UF_BREP are:

1.  Asking about BREP topology and geometry via:

    UF_BREP_ask_topology:
        Returns a Parasolid-like topology tree for a NX solid.  Face,
        edge, and vertex topology entities contain the NX entity tags
        for surfaces, curves, and points, respectively.

    UF_BREP_ask_geometry:
        Returns raw geometry data for a topology entity, which may not
        have a NX entity tag, e.g., a fin and the corresponding SP
        curve.

2.  Creating BREP topologies via:

    Topology structures:
        You malloc UF_BREP_topology_s C struct's that form the basis
        of the topology tree.  You build the topology `scaffolding' by
        assigning pointers from parents to children topologies.

    UF_BREP_attach_geometry:
        Creates underlying NX geometry entities from raw geometry data
        that you supply, and logically attaches the geometry to a
        topology entity.  E.g., attaching a .5 meter radius
        cylindrical surface to a face.

    UF_BREP_make_body:
        Creates a NX body from your topology tree and the corresponding
        geometry that UF_BREP_attach_geometry creates.

UF_BREP can also create and ask about trimmed surfaces.  The create
and ask methods for these sheet bodies are similar to those for solid
bodies.



You can use these routines for applications requiring low level control over
non-trivial solid body creation and extraction, e.g., translator applications.
Or for applications that previously created NX solids by creating sheet bodies
and then sewed the sheets together.

For geometry creation the Open UF_BREP API lets you create a topological
model of a NX solid or sheet body. You complete the boundary representation by
attaching geometry to the topological model, e.g., surfaces to faces, curves
to edges.

For extraction, the UF_BREP module returns a topological model, whose individual
entities, e.g., a face or an edge, can be queried for raw geometry and status
data.


Protocols and Tips

Protocols specify UF_BREP functionality and when to use it. A protocol summary
follows.

Since deciding which protocol to use requires some understanding of NX details,
those concepts are defined here. NX has the notion of Topology that can be
considered more or less separately from geometry. The former is the idea of
connecting things together without (necessarily) knowing where they are in
space. The latter is the idea of something specific that can exist in space. A
real object is formed by matching topology with geometry.

Faces (topology) are formed when given a set of loops (topology), each of which
has a list of edges (topology), each of which in turn has one or two vertices
(topology). A surface (geometry) is bounded by curves (geometry) which are in
turn bounded by points (geometry). The connections are defined by the topology.
The topology is given a 3D-space existence by attaching geometry to each of the
relevant topology elements.

A shell is a set of connected faces, e.g., the shell of a solid cube is the six
planar faces. And if the cube also has an internal void, another shell would
define the set of faces bounding the void.

A fin is the topology that connects a face to an edge. Thus where two faces
join there are two fins, one for the loop on each of the respective faces, that
"point to" the edge. Either the fins of the faces connecting to an edge may
have curves, or the edge may have a curve, but not both, in a NX body.
The former situation exists when an edge is made tolerant. In this case, there
is a curve on the fin that is defined as a spline in the parameter space of
the surface, which are the u and v values. These Surface Parameter curves are
called SP curves.

A periodic surface is one that closes on itself. Cylinders, cones, spheres,
and torii are periodic; a (non-degenerate) torus is bi-periodic. B-surfaces may
also be periodic or even bi-periodic. The latter must be smooth at the
closure(s).

A degeneracy is a place on a surface or curve where evaluating it at several
neighboring parameter values results in the same point. The derivatives cannot
be computed at such a point.

A singularity is a place on a surface where evaluating at a range of parameters
does not change the result, where this property is integral to the surface. It
is close kin to a degeneracy; one might say that a singularity is a legal
degeneracy. The tip of a cone is a singularity. It has no extent in 3D space,
but when a cone is represented in its U/V parameter space, it is rectangular;
in fact all NX surfaces have a rectangular parameter space. One entire side of
this parameter space corresponds to the tip of the cone. A bsurface may have a
singularity, as long as it is along one edge or at two opposing edges of the
parameter space.

Regardless of whether an edge is tolerant or not, SP curves for the fins
attached to an edge may be obtained, or a 3D curve for the edge may be obtained,
or both. If the requested data does not exist it is computed, by approximation
if necessary. It is the manner of checking the approximated curves and how well
they must correspond to the solid or sheet body that determines which protocol
to use. This checking primarily has to do with periodic surfaces.

We first concern ourselves with the means of extracting data from an existing
solid or sheet. There are several things to consider:

1.  Is a complete boundary representation of the body needed, or does each face
    stand alone? In other words, does the correspondence from the edge of one
    face to the edge of its adjacent face need to be known?

2.  In the treatment of periodic surfaces: must the SP curves be checked to
    make sure they represent a loop with constraints, e.g., the loop is closed
    and contained within a single period? Or may the SP curves be more loosely
    created while ensuring that when interpreted on periodic surfaces, they
    define the desired trimming?

3.  In the treatment of periodic surfaces and/or singularities are SP curves
    needed with a known correspondence to the edge curves of the body? Or may
    SP curves be defined as is convenient for NX, which might create more than
    one SP curve for a 3D curve?

4.  Do surfaces with singularities (spheres, cones) need SP curves to represent
    the edges of the parameter space corresponding to the singularity?

5.  In the treatment of periodic surfaces: are SP (and/or 3D) curves needed for
    the "seam", the line where the surface closes on itself? In particular, is
    it necessary that holes in the surface that straddle the seam be split and
    merged to make a single outer boundary?

The answers to these questions determine what sort of sequence is used to obtain
the data for a solid or sheet body, and what options are used.

If the body is not needed as a cohesive whole, but instead all faces stand
alone, periodics and singularities don't have much effect on the application's
processing. The recommended protocol is as follows:

1.  Obtain a list of the faces of the body and start with the first one.

2.  Call UF_BREP_ask_topology on the face. Specify any SP curve modification
    options needed.  The returned topology represents only the desired face.

3.  Call UF_BREP_ask_geometry as needed to get all the geometry.

4.  Call UF_BREP_release_topology on the topology returned in step 2.

5.  Get the next face and go to step 2.

If the face must be represented with a closed outer boundary contained within a
single period of the surface, specify the flattening with periphery option. If
it is permissible to represent the face without an outer boundary (if it is not
needed), and if it is permissible to represent the trimming without a closed SP
curve loop (the 3D loops will still be closed), specify the flattening option.
If no option is specified, fewer checks are made on the SP curves and it is
possible that some curves may be shifted by a period on periodic surfaces. This
does not harm the interpretation of the data in NX, but other systems
(such as may be used via a translator) may not be able to accommodate such data.

If the result contains more than one face, then it was necessary to divide the
face to obtain a representation meeting all the constraints on the SP curves.
You can either process them as several separate faces, or combine the curves to
represent one face in which the curves either extend outside one period.

If the body is needed as a cohesive whole, and either SP curves are not needed
or they may be output as is convenient for NX, use the following protocol:

1.  Call UF_BREP_ask_topology on the body (without any SP curve modifications).

2.  Repeatedly call UF_BREP_ask_geometry to obtain the surfaces, curves, and
    vertices.

3.  Call UF_BREP_release_topology on the topology returned in step 1.

If the body is needed as a cohensive whole (B-REP), but periodic faces must be
flattened with a periphery, you need to do extra work. Flattening is also
called seam-realizing; the curves are divided in the output, and where the face
closes are used to split any loops that straddle the seam.  The result
incorporates the loops defining the ends of the face, the curves of the seam,
and any holes straddling the seam, into one peripheral loop. Use the protocol:

1.  Call UF_BREP_ask_topology on the whole body. Flattening cannot be specified
    for this call.

2.  For each face, call UF_BREP_ask_topology. Specify the flattening options
    needed. The results contain the seam curves and the split holes, and
    combine several loops into the single peripheral loop. To produce your
    output, you need to search the children list and match up the identifiers.

Secondly, we concern ourselves with creating a body. Consider the following
questions:

    Is the body to be built from a complete boundary representation, or is it a
    sheet to be built by trimming with curves?

    Are vertices available?

If vertices are not available, and you do not want to compute them, then you
have to build a sheet with trimming curves. Other qualities necessary to build
a body as described above that may not be present in the data include
direction/sense data for the surfaces and edge curves. Lack of these data
also indicate that the sheet should be built with trimming curves even if
vertices are present.

To build a body from a complete boundary representation, use the following
protocol:

1.  Build the topology structure and optionally call UF_BREP_validate_topology
    to catch non-geometric problems.

2.  Repeatedly call UF_BREP_attach_geometry to create the geometry of the model.
    To replace geometry you have already created, use UF_BREP_delete_geometry
    and then call UF_BREP_attach_geometry again.

3.  You may extend the topology to add items, as determined from geometry
    states and any other examination you might do. Allocate, initialize, and
    link together any new topology structure elements. For debugging use
    UF_BREP_validate_topology to catch topology errors.

4.  Call UF_BREP_make_body to complete the process.

To build a sheet body from bounding curves, use the following protocol:

1.  Build the topology structure, set the body type to abbreviated (or begin
    with the face), and optionally call UF_BREP_validate_topology. You need not
    include vertices (they are ignored if present) and you need include only
    the type of curves that are used for trimming (SP curves or 3D curves); the
    others are ignored. The body and shell topology items may also be omitted.

2.  Repeatedly call UF_BREP_attach_geometry to create the geometry of the model.

3.  You may extend the topology to add items, as determined from geometry
    states and any other examination you do. Allocate, initialize, and link
    together any new topology structure elements.  For debugging use
    UF_BREP_validate_topology to catch topology errors.

4.  Call UF_BREP_make_body to complete the process.

    Normally, the values of the edge senses and attached curve orientations are
    not necessary to create the desired trimmed surface.  However, for a closed
    surface and one trim loop (i.e., no holes), UF_BREP does require the sense
    and orientation information.  For example, if a spherical surface has an
    equatorial trim curve, then is the desired face the southern or northern
    hemisphere?

    To decide in such cases, UF_BREP uses the `left hand' rule.  In the
    hemisphere example, if the edge sense and edge curve orientation are
    FORWARD and the equator curve parameterization increases in the westerly
    direction, then the resulting face is the southern hemisphere.

5.  Call UF_BREP_release_topology.

At times, it may be necessary to abort creation of a body. Use
UF_BREP_release_topology to do this, any time before UF_BREP_make_body is
called. After using UF_BREP_make_body, use UF_OBJ_delete_object with the body
tag. Don't use UF_BREP_release_topology.

It may be desired to create geometry for the purpose of evaluating and examining
it, without creating a body. Do this as follows:

1.  Create and initialize a topology, e.g., with the UF_BREP_INITIALIZE_TOPOLOGY
    macro. Set the type fields to the appropriate types for the geometry you
    wish to attach.

2.  You may then attach geometry to the topology entities and evalulate it with
    UF_BREP_ask_geometry.

3.  Use UF_BREP_delete_geometry to delete the geometry.

Memory Handling

All memory returned by UF_BREP_ask_topology must be freed with
UF_BREP_release_topology.  If you are creating your own topology, e.g., via
UF_BREP_make_body, you must free memory you allocate (including the oriented
children arrays), or you must supply UF_BREP_release_topology or
UF_BREP_free_geometry_data with a free function that can free the memory you
have allocated.

UF_BREP_ask_geometry allocates memory for various items. You can free the
memory with UF_free, or you can call UF_BREP_free_geometry_data with a NULL
free function argument.

For example, some geometry types contain data in arrays pointed to by members
of their structure.  The geometry structure itself is provided by the caller
(and therefore must not be freed with UF_free), but the arrays (like knots for
a spline) must be freed by UF_free when returned by the above functions.
Extruded and revolved surfaces have extra structures to represent the generators
that must be freed by UF_free.

*****************************************************************************/

/****************************************************************************
Example:  Tetrahedron with vertex and edge topology labels.
          Assume vertex V3 is farthest from the reader.

                          V2
                          /\
                         /  \\
                        /    \ \
                       /      \  \
                      /        \   \
                     /          \    \
                    /         E3 \     \
                E1 /              \      \  E4
                  /                \       \
                 /                  \        \
                /                    \V3       \
               /         E2    __--'' `--_       \
              /          __--''           `--_     \
             /     __--''                 E5  `--_   \
            /__--''                               `---_\
        V1 '--------------------------------------------` V4
                                E6

The corresponding topology tree follows with surface, curve, and point
geometry attached to face, edge, and vertex topology, respectively.
Note that each edge appears twice; once with a forward and once with a
reverse orientation with respect to the two owning loops.  Loop
directions follow the rule that the face is to the left of the loop
when `up' is in the direction of the face normal.

    SOLID
        SHELL
        |
        +-- FACE1 (plane)
        |       LOOP
        |           FIN
        |               EDGE1-forward (line)
        |                   VERTEX1 (point)
        |                   VERTEX2 (point)
        |           FIN
        |               EDGE3-forward (line)
        |                   VERTEX2 (point)
        |                   VERTEX3 (point)
        |           FIN
        |               EDGE2-forward (line)
        |                   VERTEX3 (point)
        |                   VERTEX1 (point)
        +-- FACE2 (plane)
        |       LOOP
        |           FIN
        |               EDGE1-reverse (line)
        |           FIN
        |               EDGE6-forward (line)
        |                   VERTEX1 (point)
        |                   VERTEX4 (point)
        |           FIN
        |               EDGE4-forward (line)
        |                   VERTEX4 (point)
        |                   VERTEX2 (point)
        +-- FACE3 (plane)
        |       LOOP
        |           FIN
        |               EDGE6-reverse (line)
        |           FIN
        |               EDGE2-reverse (line)
        |           FIN
        |               EDGE5-forward (line)
        |                   VERTEX3 (point)
        |                   VERTEX4 (point)
        +-- FACE4 (plane)
                LOOP
                    FIN
                        EDGE4-reverse (line)
                    FIN
                        EDGE5-reverse (line)
                    FIN
                        EDGE3-reverse (line)

In the brief example above, attached curve `senses' are unspecified
but essential to make a body.  Curve sense is forward if the curve
parameterization goes from the owning edge's 1st vertex to the 2nd
vertex.
*****************************************************************************/

/***************************************************************************

  ***************************************************************************/

#ifndef UF_BREP_INCLUDED
#define UF_BREP_INCLUDED

#include <uf_defs.h>         /* Common to all Open API, e.g., tag_t, NULL_TAG */

#include <uf_curve.h>        /* UF_CURVE_conic_s, UF_CURVE_spline_s, ... */
#include <uf_brep_types.h>   /* Only has UF_BREP-specific definitions */
#include <libufun_exports.h>


#ifdef __cplusplus
extern "C" {
#endif



/*****************************************************************************
This function returns the class numbers for the edge.

A ring edge is an edge, like the end of a cylinder, that has a curve but
no vertices. A closed edge is like a ring edge but has one vertex. An
open edge has two vertices. In topology structures, it is permissible for
a closed edge to have two vertices as children but they must be the
same vertex.

Environment: Internal  and  External

See Also:  UF_BREP_ask_geometry


History:
 ****************************************************************************/
extern UFUNEXPORT int UF_BREP_ask_edge_class (
const UF_BREP_topology_t *item ,/* <I>
                                Item of topology for which the edge class
                                numbers are to be returned.
                                */
int * edge_class ,/* <O>
                  Class number of edge:
                  UF_BREP_EDGE_OPEN
                  UF_BREP_EDGE_CLOSED
                  UF_BREP_EDGE_RING
                  */
int * geom_class  /* <O>
                  Class number of geometry on edge:
                  UF_BREP_EDGE_NORMAL: has 3D curve.
                  UF_BREP_EDGE_INTERSECTION: has 3D
                  curve derived from surfaces.
                  UF_BREP_EDGE_TOLERANT: has SP curve.
                  UF_BREP_EDGE_SP: not a tolerant edge but
                  represented with an SP curve.
                  */
);

/*****************************************************************************
The given geometry is queried from the model and returned in the
application-supplied structure. Any arrays needed (for example in
b-surfaces and extruded surfaces) are allocated by Open API and
must be freed with UF_free, or with UF_BREP_free_geometry_data.

For curves, geom_sense is forward if the curve tangent is pointing in
the same direction as traversing the edge from the start vertex to the
end vertex.  For surfaces, geom_sense is forward if the surface normal
points in the face normal direction (which the loop direction
determines).

Special attention is given to geometries that cannot be returned
without approximation. Blend surfaces, intersection edges, and
tolerant edges have no direct representation in available geometry
types. Therefore, when requesting data for a face or edge, the
mappings and tolerances must always be supplied in the respective
structures. Applications sometimes provide different tolerances for
faces and edges, or for different types of surfaces or curves.
This function's results are undefined if any function that changes the
body's topology is used between the time UF_BREP_ask_topology is
called and the time this function is called. This includes any feature
changes or any other modelling operation.

Geometry may be asked on a topology being used to create a body.
It is important to realize that when asking for fin geometry for a
tolerant edge, the SP curves returned were produced at the time the
edge was made tolerant (when it was modelled). Its accuracy was
determined at that time. Such curves are returned by this function as
they were constructed when made. Setting a smaller tolerance for this
function does not improve their accuracy. A smaller tolerance in this
function only improves the accuracy of curves or surfaces that must be
approximated by this function.

Environment: Internal  and  External

See Also:  UF_BREP_ask_topology

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_BREP_ask_geometry (
const UF_BREP_topology_t *topology ,/* <I>
                               Pointer to topology item structure defining
                               geometry to be returned
                               */
const UF_BREP_options_t *options ,/* <I>
                             Applicable options: All tolerances for edge
                             and fin curves, and for surfaces, should be
                             specified.
                             */
const UF_BREP_mapping_t *mapping ,/* <I>
                             Surface and curve type mappings to cause
                             output to be in b-spline geometry.
                             */
UF_BREP_geometry_t *geometry ,/* <I>
                               Pointer to geometry structure to receive
                               the description.
                               */
UF_BREP_orientation_t *geom_sense , /* <I/O>
                                    Input:
                                    Geometry orientation with respect to the
                                    topology entity.  For faces, fins, and
                                    edges:
                                    UF_BREP_ORIENTATION_FORWARD
                                    or
                                    UF_BREP_ORIENTATION_REVERSE.
                                    Otherwise
                                    UF_BREP_ORIENTATION_NONE.
                                    Output:
                                    Pointer to geometry structure to receive
                                    the description.
                                    */
int * num_states ,/* <O>
                  number of states in the states array
                  */
UF_BREP_state_t **states    /* <OF,len:num_states>
                            UF_BREP allocated array.  If the caller passes
                            in a NULL, UF_BREP does not allocate the array.
                            This should be freed by calling UF_free.
                            */
);


/*****************************************************************************
Returns a unique identifier within a body for topology elements that
do not have NX tags, viz., vertices, fins, and shells.  The identifier is
useful for Open API level algorithms that need to test for identical
topology elements, e.g., is a vertex on an edge the same as a vertex on
another edge?

Return: void
Environment: Internal  and  External
See Also:
History:
 ****************************************************************************/
extern UFUNEXPORT void UF_BREP_ask_identifier (
const UF_BREP_topology_t *body_topos ,/* <I>
                                       Topology entity for which to return an
                                       identifier.
                                       */
int *identifier  /* <O>
                Unique for all other topology identifiers within
                the same body.
                */
);


/*****************************************************************************
Returns a topological description of a body or face. The body_topos
list with the children pointer arrays defines the connections between
the entities of the body.

The topology for a face is returned as if it were a sheet body, unless
SP curve modifications are requested, in which case the vertices are
omitted.

The orientation of edges or fins in loops is indicated by the
orientation member of the oriented child structure.



Environment: Internal  and  External
See Also: See  UF_BREP_ask_geometry
               UF_BREP_release_topology
               UF_BREP_ask_edge_class
          

History:
 ****************************************************************************/
extern UFUNEXPORT int UF_BREP_ask_topology (
tag_t body ,/* <I>
            Tag of body for which to return topology
            */
const UF_BREP_options_t *options , /* <I>
                                   Options are specified as needed. Fin
                                   modifications (flattening, singularities) are
                                   specified here when requesting surface data
                                   for trimming.
                                   */
UF_BREP_topology_t **body_topos ,  /* <OF>
                                   Topology structures and arrays that describe
                                   the body.
                                   */
int *num_states ,/* <O>
                Number of states in the state array
                */
UF_BREP_state_t **states    /* <OF,len:num_states>
                            UF_BREP allocated array.  If the caller passes
                            in a NULL, UF_BREP does not allocate the array.
                            This should be freed by calling UF_free.
                            */
);

/*****************************************************************************
Returns the source of the specified topology.

Environment: Internal  and  External
See Also:  UF_BREP_validate_topology
History:
 ****************************************************************************/
extern UFUNEXPORT int UF_BREP_ask_topology_source (
const UF_BREP_topology_t *body_topos ,/* <I>
                                      Address of topology array whose state
                                      is to be returned
                                      */
UF_BREP_topo_source_t *topo_source  /* <O>
                                    Source of topology
                                    */
);

/*****************************************************************************
The given geometry is created and attached to the topology item
indicated. UF_BREP_attach_geometry returns an error if the geometry
already has attached geometry.

No geometry is permitted to be attached to a topology item not of the
correct type. Only edges and fins may have curves, only faces may
have surfaces, and only vertices may have points. You may attach 3D
curves to edges and SP curves to the fins of that edge. The additional
information is sometimes useful in creating a valid edge.
For curves, geom_sense is forward if the curve tangent is pointing in
the same direction as traversing the edge from the start vertex to the
end vertex.  For surfaces, geom_sense is forward if the surface normal
points in the face normal direction (which the loop direction
determines).

Simplifications performed on b-geometry are the following:
A bspline that is linear is converted to a line. This is done for
linear and quadratic spline data.

A bspline that represents a circle is converted to a circle.

A surface of revolution with a line as the generator is
converted to a cylinder or cone, if the generator is aligned
suitably.

A surface of revolution with an arc as the generator is
converted to a sphere or torus, if the generator is aligned
suitably. Even partial arcs are simplified to the complete
surface.

A bsurface that is planar is converted to a plane. This is done
for linear and quadratic bsurface data.

A bsurface that is linear in one direction and circular in the
other is converted to a cylinder or cone.

A bsurface that is circular in both directions is converted to a
sphere or torus.

Please note the following items:

Some configurations of spline data that represent analytic geometry
may not be simplified. This is because particular forms may not be
recognized by Open API.

If simplification is requested, and SP curves are to be used to
construct the face, it is necessary that the simplification introduce a
transformation of the surface parameterization that is linear in
nature. Any other transformation causes SP curves to assume an
incorrect shape. In particular, conversions of b-surfaces and
b-curves to their analytic equivalents may introduce
parameterization changes that are  incompatible with using SP
curves for face construction. If the latter is the case, a state that so
indicates is returned.

Environment: Internal  and  External
See Also:  UF_BREP_validate_topology
History:
****************************************************************************/
extern UFUNEXPORT int UF_BREP_attach_geometry (
UF_BREP_topology_t *topology  ,/* <I>
                               Pointer to topological structure containing
                               item to which the geometry is to be attached
                               */
const UF_BREP_geometry_t *geometry ,/* <I>
                               Pointer to geometry structure defining
                               geometry to be attached
                               */
const UF_BREP_orientation_t geom_sense ,/* <I>
                                        Geometry orientation with respect to the
                                        topology entity.  For faces, fins, and
                                        edges use:
                                        UF_BREP_ORIENTATION_FORWARD or
                                        UF_BREP_ORIENTATION_REVERSE.
                                        Otherwise use
                                        UF_BREP_ORIENTATION_NONE.
                                        */
const UF_BREP_options_t *options ,/* <I>
                                   Applicable options:
                                   Simplification, UF_BREP_simplify_option
                                   */
int * num_states ,/* <O>
                  number of states in the states array
                  */
UF_BREP_state_t **states    /* <OF,len:num_states>
                            UF_BREP allocated array.  If the caller passes
                            in a NULL, UF_BREP does not allocate the array.
                            This should be freed by calling UF_free.
                            */
);
/****************************************************************************
Deletes the geometry attached to the specified topology. Note that the
delete is permissible only on topologies that have not yet become a
NX body.  Typically a UF_BREP_attach_geometry call would follow
a UF_BREP_delete_geometry call, e.g., if the attach failed for a
known and correctable reason.

Environment: Internal  and  External

See Also:  UF_BREP_attach_geometry
           UF_BREP_release_topology
History:
****************************************************************************/
extern UFUNEXPORT int UF_BREP_delete_geometry (
const UF_BREP_topology_t *item   /* <I>
                                 Item for which geometry is to be deleted.
                                 */
);

typedef void (*UF_BREP_free_fn_t) (void * /* <O> */);

/****************************************************************************
All data structures allocated by Open API when UF_BREP_ask_geometry was called
are freed.

Environment: Internal  and  External
See Also:  UF_BREP_ask_geometry
History:
****************************************************************************/
extern UFUNEXPORT int UF_BREP_free_geometry_data (
UF_BREP_geometry_p_t geometry ,/* <I/O>
                               Data structures allocated by
                               UF_BREP_ask_geometry are freed.
                               */
UF_BREP_free_fn_t fn  /* <I>
                                UF_BREP_free_geometry_data calls
                                UF_BREP_free_fn_t to free geometry structure data,
                                e.g., B-curve and B-surface pole arrays. If
                                free_function is NULL, then this routine uses
                                UF_free.
                                */
);
/****************************************************************************
This routine fixes, or cleans up, a body created by other Open API
functions. It attempts to re-intersect edges, reposition vertices, and set
tolerances as designated by the level specified, to make the body pass
all checks. Any object (typically a face or edge) that cannot be fixed is
returned in the state list.

The tolerance value specified is an upper limit. Any entity that
requires a tolerance larger than this limit in order to pass checks is
returned in the states array.

Any given object may have more than one entry in the states array.
The healing levels cause the following fix ups to be attempted:
0       Report problems with the body in the state list.
1       For all problems fixable with tolerances, apply the smallest
        tolerance that alleviates the problem.
2       For any edge that must be tolerant at level 1, use
        surface-surface intersection to attempt to create an exact
        curve for the edge. Any that cannot be made exact are made
        tolerant.
3       For any edge that must be tolerant at level 1 and for all spline
        edges, use surface-surface intersection to attempt to create an
        exact curve for the edge. Any that cannot be made exact are
        made tolerant.
4       For all edges, use surface-surface intersection to attempt to
        create an exact curve for the edge. Any that cannot be made
        exact are made tolerant.

Environment: Internal  and  External
See Also:
History:
****************************************************************************/
extern UFUNEXPORT int UF_BREP_heal_body (
tag_t body ,/* <I>
            body to fix
            */
int level ,/* <I>
           healing level: any of 0 through 4
           */
double toler ,/* <I>
              maximum tolerance; fix up of entities requiring
              tolerances exceeding this are returned in the
              state list
              */
int * num_states ,/* <O>
                  number of states in the states array
                  */
UF_BREP_state_t **states    /* <OF,len:num_states>
                            UF_BREP allocated array.  If the caller passes
                            in a NULL, UF_BREP does not allocate the array.
                            This should be freed by calling UF_free.
                            */
);
/****************************************************************************
Creates a NX body from a UF_BREP topology hierarchy that defines the
body topology and geometry.  In addition to returning the NX body tag,
UF_BREP_make_body assigns the NX edge and face tags to the
corresponding input UF_BREP topology structures.  UF_BREP_make_body
also does the equivalent of UF_BREP_heal_body to help make the NX body
pass validity checks.

With solid topology input, the output is a NX solid body.  With face
topology input, the output is a NX sheet body.  For a multi-face sheet
topology, you must call UF_BREP_make_body for each face of the sheet,
and then use UF_MODL_create_sew to sew the sheets together.  You can
call UF_BREP_make_body with a sheet topology, but the resulting NX
sheet body represents only the first face of the input sheet topology.

Environment: Internal  and  External
See Also:  UF_BREP_heal_body
           UF_BREP_validate_topology
History:
****************************************************************************/
extern UFUNEXPORT int UF_BREP_make_body (
UF_BREP_topology_t * topology ,/* <I>
                               Topology that has all geometry attached. The
                               toplogy is made into a NX body. You can pass
                               a face topology element.
                               */
tag_t * body ,/* <O>
              NX tag of body
              */
int * num_states ,/* <O>
                  number of states in state array
                  */
UF_BREP_state_t **states    /* <OF,len:num_states>
                            UF_BREP allocated array.  If the caller passes
                            in a NULL, UF_BREP does not allocate the array.
                            This should be freed by calling UF_free.
                            */
);
/****************************************************************************
Frees the UF_BREP structures of a topology.  The structures include
the oriented children structure arrays.

If a is topology built by the user and not finished, UF_BREP_release_topology
must be called.

Environment: Internal  and  External

See Also:  UF_BREP_validate_topology
           UF_BREP_ask_topology

History:
****************************************************************************/
extern UFUNEXPORT int UF_BREP_release_topology (
const UF_BREP_topology_t *body_topos ,/* <I>
                                 Topology for body the application is done with
                                 */
UF_BREP_free_fn_t fn             /* <I>
                                 UF_BREP_free_geometry_data calls
                                 UF_BREP_free_fn_t to free geometry structure data,
                                 e.g., B-curve and B-surface pole arrays.
                                 If the free_function is NULL, then this
                                 routine uses UF_free.
                                 */
);
/****************************************************************************
Optional function to validate the body_topos tree. It validates the
children contents, i.e., shells must be the children of the body, faces
must be children of shells, loops the children of faces, fins (if present)
the children of loops, edges the children of fins (if present, children of
loops if not), and vertices the children of edges (if edges are present)
or fins (if edges are not present). Thus the type members must be set
to valid values and the children arrays must be set (but the children
arrays may be unspecified, when it is desirable to build the body in
stages.)

The extension fields are updated with a pointer for use by the
UF_BREP module. The application must not alter this value and
must use it only with the macros designated for that purpose.

Environment: Internal  and  External

See Also:  UF_BREP_attach_geometry

History:
****************************************************************************/
extern UFUNEXPORT int UF_BREP_validate_topology (
const UF_BREP_topology_t *body_topos ,/* <I>
                                 Topology structure array to initialize
                                 */
int * num_states ,/* <O>
                  Number of states in the state array
                  */
UF_BREP_state_t **states    /* <OF,len:num_states>
                            UF_BREP allocated array.  If the caller passes
                            in a NULL, UF_BREP does not allocate the array.
                            This should be freed by calling UF_free.
                            */
);


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif    /*  END UF_BREP_INCLUDED  */

/*****************************************************************************
             Copyright (c) 1998-2000 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved



File description:

These routines are the Modeling legacy routines. These routines are in 
the process of being replaced with other modeling functionality.

Work Part Restrictions

For those functions/subroutines that perform an operation on an
object, the object must not be an occurrence and the object must be in
the same part as the work part. If either one of these requirements are
not met, then a NULL_TAG is returned for the object on which the
operation is performed. These restrictions apply to the following older
solids routines:
UF6506
UF6507
UF6508
UF6511
UF6523
UF6524
UF6525
UF6526
UF6527
 
NOTE
  UF6560 does NOT return an error message in this case.

*****************************************************************************/

#ifndef UF_MODL_LEGACY_H_INCLUDED
#define UF_MODL_LEGACY_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/* uf5300 create cylinder */
extern UFUNEXPORT void FTN(uf5300)(double *ra1, double *ra2, double *rp3,
                        int *ip4, tag_t *nr5);

/* uf5301 read cylinder data */
extern UFUNEXPORT void FTN(uf5301)(tag_t *np1, double *rar2, double *rar3,
                        double *rr4);

/* uf5303 read cylinder endpoint and vector */
extern UFUNEXPORT void FTN(uf5303)(tag_t *np1, double *rar2, double *rar3);

/* uf5305 read cylinder radius */
extern UFUNEXPORT void FTN(uf5305)(tag_t *np1, double *rr2);

/* uf5309 read cylinder real data */
extern UFUNEXPORT void FTN(uf5309)(tag_t *np1, double *rar2);

/* uf5310 create cone */
extern UFUNEXPORT void FTN(uf5310)(double *rp1, double *rp2,
                        double *ra3, double *ra4, double *rp5,
                        int *ip6, tag_t *nr7);

/* uf5311 read cone data */
extern UFUNEXPORT void FTN(uf5311)(tag_t *np1, double *rr2, double *rr3,
                        double *rar4, double *rar5);

/* uf5313 read cone axis vector */
extern UFUNEXPORT void FTN(uf5313)(tag_t *np1, double *rar2);

/* uf5315 read cone vertex coordinate */
extern UFUNEXPORT void FTN(uf5315)(tag_t *np1, double *rar2);

/* uf5317 read cone angle */
extern UFUNEXPORT void FTN(uf5317)(tag_t *np1, double *rr2);

/* uf5319 read cone real data */
extern UFUNEXPORT void FTN(uf5319)(tag_t *np1, double *rar2);

/* uf5320 create sphere */
extern UFUNEXPORT void FTN(uf5320)(double *ra1, double *rp2,
                        int *ip3, tag_t *nr4);

/* uf5321 read sphere data */
extern UFUNEXPORT void FTN(uf5321)(tag_t *np1, double *rar2, double *rr3);

/* uf5323 read sphere axis vector */
extern UFUNEXPORT void FTN(uf5323)(tag_t *np1, double *rar2);

/* uf5325 read sphere center */
extern UFUNEXPORT void FTN(uf5325)(tag_t *np1, double *rar2);

/* uf5327 read sphere radius */
extern UFUNEXPORT void FTN(uf5327)(tag_t *np1, double *rr2);

/* uf5329 read sphere real data */
extern UFUNEXPORT void FTN(uf5329)(tag_t *np1, double *rar2);

/* uf5374 create plane
   Replaced by UF_MODL_create_plane */
extern UFUNEXPORT void FTN(uf5374)(double *rp1, double *rp2,
                        double *rp3, tag_t *nr4);

/* uf5375 read plane data
   Replaced by UF_MODL_ask_plane */
extern UFUNEXPORT void FTN(uf5375)(tag_t *np1, double *rr2, double *rr3);

/* uf5376 edit plane data
   Replaced by UF_MODL_edit_plane */
extern UFUNEXPORT void FTN(uf5376)(tag_t *np1, double *rp2, double *rp3);


/**  Face Modeling  **/

/* uf5400 read face grid counts
   Replaced by UF_MODL_ask_face_grid_count */
extern UFUNEXPORT void FTN(uf5400)(tag_t *np1, int *iar2);

/* uf5401 edit face grid counts
   Replaced by UF_MODL_edit_face_grid_count */
extern UFUNEXPORT void FTN(uf5401)(tag_t *np1, int *ia2);

/* uf5404 read face u-v minimum/maximum -- replaced by UF_MODL_ask_face_uv_minma
x */
extern UFUNEXPORT void FTN(uf5404)(tag_t *np1, double *rar2);

/* uf5406 read face normal direction */
extern UFUNEXPORT void FTN(uf5406)(tag_t *np1, int *ir2);

/* uf5407 edit face normal direction */
extern UFUNEXPORT void FTN(uf5407)(tag_t *np1, int *ip2);

/* uf5408 read face generating curve */
extern UFUNEXPORT void FTN(uf5408)(tag_t *np1, int *ip2, tag_t *nr3);

/* uf5409 trim sheet by loops */
extern UFUNEXPORT void FTN(uf5409)(tag_t *np1, double *rp2, int *ip3,
                        int *ip4, int *ip5, int *ip6,
                        tag_t *np7, int *ip8, int *ir9);

/* uf5410 remove face trim */
extern UFUNEXPORT void FTN(uf5410)(tag_t *np1, int *ir9);

/* uf5411 read face trim status */
extern UFUNEXPORT int FTN(uf5411)(tag_t *np1);

/* uf5412 trim face by curves and points */
extern UFUNEXPORT void FTN(uf5412)(tag_t *np1, double *rp2, int *ip3,
                        int *ip4, tag_t *np5, int *ip6,
                        int *ip7, double *rp8, int *ir9);


/**  Freeform Modeling  **/

/* uf5330 create body of revolution */
extern UFUNEXPORT void FTN(uf5330)(tag_t *np1, double *ra2, double *ra3,
                        double *ra4, tag_t *nr5);

/* uf5331 read body of revolution axis vector */
extern UFUNEXPORT void FTN(uf5331)(tag_t *np1, double *rar2);

/* uf5333 read body of revolution point on axis */
extern UFUNEXPORT void FTN(uf5333)(tag_t *np1, double *rar2);

/* uf5339 read body of revolution real data */
extern UFUNEXPORT void FTN(uf5339)(tag_t *np1, double *rar2);

/* uf5340 create tabulated cylinder */
extern UFUNEXPORT void FTN(uf5340)(tag_t *np1, double *ra2, double *ra3,
                        tag_t *nr4);

/* uf5341 read tabulated cylinder axis vector */
extern UFUNEXPORT void FTN(uf5341)(tag_t *np1, double *rar2);

/* uf5349 read tabulated cylinder real data */
extern UFUNEXPORT void FTN(uf5349)(tag_t *np1, double *rar2);

/* uf5350 create ruled sheet */
extern UFUNEXPORT void FTN(uf5350)(tag_t *np1, tag_t *np2,
                        int *ip3, tag_t *nr4);

/* uf5360 create bounded plane */
extern UFUNEXPORT void FTN(uf5360)(int *ip1, int ip2[], tag_t np3[],
                        double *rp4, tag_t *nr5, int *ir6);

/* uf5363 read face anchor counts */
extern UFUNEXPORT void FTN(uf5363)(tag_t *np1, int *ir2,
                        int *ir3, int *ir4);

/* uf5364 read face anchor object */
extern UFUNEXPORT void FTN(uf5364)(tag_t *np1, int *ip2,
                        tag_t *nr3, int *ir4);

/* uf5368 read face edge curve data */
extern UFUNEXPORT void FTN(uf5368)(tag_t *np1, int *ip2,
                        int *ip3, tag_t *nr4, double *rr5,
                        int *ir6, int *ir7);

/* uf5380 create curve mesh sheet */
extern UFUNEXPORT void FTN(uf5380)(tag_t *na1, tag_t *na2,
                        int *ip3, int *ip4,
                        tag_t *nr5);

/* uf5381 read curve mesh sheet primary and */
extern UFUNEXPORT void FTN(uf5381)(tag_t *np1, int *ir2, int *ir3);

/* uf5382 read curve mesh sheet primary curve */
extern UFUNEXPORT void FTN(uf5382)(tag_t *np1, int *ip2, tag_t *nr3);

/* uf5384 read curve mesh sheet cross curve */
extern UFUNEXPORT void FTN(uf5384)(tag_t *np1, int *ip2, tag_t *nr3);

/* uf5405 create bounding box for a face */
extern UFUNEXPORT void FTN(uf5405)(tag_t *np1, double *rr2, int *ir3);

/* uf5440 create b-surface sheet */
extern UFUNEXPORT void FTN(uf5440)(int *ip1, int *ip2, int *ip3,
                        int *ip4, int *ip5, int *ip6,
                        int *ip7, double *rp8, int *ip9,
                        double *rp10, double *rp11, double *rp12,
                        double *rp13, tag_t *nr14);

/* uf5441 read b-surface sheet data
   Replaced by UF_MODL_ask_bsurf */
extern UFUNEXPORT void FTN(uf5441)(tag_t *np1, int *ir2, int *ir3,
                        int *ir4, int *ir5, int *ir6,
                        int *ir7, int *ir8, double *rr9,
                        int *ir10, double *rr11, double *rr12,
                        double *rr13, double *rr14);

/* uf5442 create b-surface sheet from body of */
extern UFUNEXPORT void FTN(uf5442)(tag_t *np1, double *rp2, double *rp3,
                        double *rp4, tag_t *nr5);

/* uf5443 create b-surface sheet from list of curves */
extern UFUNEXPORT void FTN(uf5443)(int *ip1, tag_t *np2,
                        int *ip3, int *ip4,
                        int *ip5, tag_t *nr6);

/* uf5444 approximate a face with a b-surface */
extern UFUNEXPORT void FTN(uf5444)(tag_t *np1, double *rp2, double *rp3,
                        tag_t *nr4, int *ir5);

/* uf5448 create b-surface sheet from
   Replaced by UF_MODL_create_bsurf_thru_pts */
extern UFUNEXPORT void FTN(uf5448)(int *ip1, int *ip2,
                        int *ip3, int *ip4,
                        int *ip5, int *ip6,
                        int *ip7, double *rp8,
                        double *rp9, tag_t *nr10,
                        int *ir11);

/* uf5449 create free form feature by cubic fit from */
extern UFUNEXPORT void FTN(uf5449)(int *ip1, tag_t *np2, int *ip3,
                        int *ip4, double *rp5, tag_t *np6,
                        int *ip7, int *ip8, int *ip9,
                        double *rp10, tag_t *nr11, int *ir12);

/* uf5450 create offset face.  
   Edge curve tolerance controls how accurately the edge curves lie on
   the face.  The tolerance value cannot be less than .0001 inches or
   .00254 mm. The offset distance (RP2) must be nonzero.
   Geometry edits made to a base face are reflected in the associated
   offsets.  Therefore, be extremely careful when modifying base faces.
   If an error occurs, NR5 = NULL. Call UF/uc6560 to get the
   appropriate error message.

CAUTION:
   The option to create a non-associative offset surface
   with LP4 is no longer supported as of the V10 release. 
*/
extern UFUNEXPORT void FTN(uf5450)(
tag_t *np1,   /* <I> Object identifier of the base face */
double *rp2,  /* <I> Offset Distance */
double *rp3,  /* <I> Edge Curve Tolerance */
int *lp4,     /* <I> Not used.  */
tag_t *nr5    /* <O> Object identifier of the offset surface.  Set to 
                     NULL if the offset surface was unable to be created. */
);

/* uf5451 read offset distance */
extern UFUNEXPORT void FTN(uf5451)(tag_t *np1, double *rr2, int *ir3);

/* uf5452 edit offset distance */
extern UFUNEXPORT void FTN(uf5452)(tag_t *np1, double *rp2, double *rp3);

/* uf5453 base face type */
extern UFUNEXPORT void FTN(uf5453)(tag_t *np1, int *ir2);

/* uf5460 create free form feature using conic face */
extern UFUNEXPORT void FTN(uf5460)(int *ip1, tag_t *np2, tag_t *np3,
                        int *ip4, double *rp5, int *ip6,
                        int *ip7, double *rp8, int *ir9,
                        tag_t *nr10, tag_t *nr11, double *rr12);

/* uf5461 create free form feature using sweeping */
extern UFUNEXPORT void FTN(uf5461)(int *ip1, tag_t *np2, int *ip3,
                        int *ip4, tag_t *np5, int *ip6,
                        int *ip7, tag_t *np8, int *ip9,
                        int *ip10, tag_t *np11, int *ip12,
                        double *rp13, int *ip14, tag_t *np15,
                        int *ip16, int *ip17, double *rp18,
                        double *rp19, int *ir20, tag_t *nr21);

/* uf5462 create b-surface face */
extern UFUNEXPORT void FTN(uf5462)(int *ip1, tag_t *np2, int *ip3,
                        tag_t *np4, int *ip5, double *rp6,
                        int *ir7, tag_t *nr8);

/* uf5464 reads the count of poles */
extern UFUNEXPORT void FTN(uf5464)(tag_t *np1, int *ir2,
                        int *ir3, int *ir4, int *ir5);

/* uf5465 create a b-surface face from a face */
extern UFUNEXPORT void FTN(uf5465)(tag_t *np1, double *rp2, tag_t *nr3);

/* uf6500 create a block */
extern UFUNEXPORT void FTN(uf6500)(double *rp1, double *rp2, double *rp3,
                       tag_t *nr4);

/* uf6501 create a sphere */
extern UFUNEXPORT void FTN(uf6501)(double *rp1, double *rp2, tag_t *nr3);

/* uf6502 create a cylinder */
extern UFUNEXPORT void FTN(uf6502)(double *rp1, double *rp2, double *rp3,
                        double *rp4, tag_t *nr5);

/* uf6503 create a torus */
extern UFUNEXPORT void FTN(uf6503)(double *rp1, double *rp2,
                        double *rp3, tag_t *nr4);

/* uf6504 create a cone */
extern UFUNEXPORT void FTN(uf6504)(double *rp1, double *rp2,
                        double *rp3, double *rp4,
                        tag_t *nr5);

/* uf6505 create a prism */
extern UFUNEXPORT void FTN(uf6505)(double *rp1, double *rp2,
                        double *rp3, int *ip4, double *rp5,
                        tag_t *nr6);

/* uf6506 create a sewn solid from a series of sheets */
extern UFUNEXPORT void FTN(uf6506)(tag_t *np1, int *ip2, int *ip3,
                        tag_t *nr4);

/* uf6507 create an extruded body */
extern UFUNEXPORT void FTN(uf6507)(tag_t *np1, int *ip2, double *rp3,
                        double *rp4, tag_t *nr5);

/* uf6508 create a body of revolution */
extern UFUNEXPORT void FTN(uf6508)(tag_t *np1, int *ip2, double *rp3,
                        double *rp4, double *rp5, tag_t *nr6);

/* uf6509 convert a face to a sheet */
extern UFUNEXPORT void FTN(uf6509)(tag_t *np1, int *ip2,
                        double *rp3, tag_t *nr4);

/* uf6511 copy a body */
extern UFUNEXPORT void FTN(uf6511)(tag_t *np1, tag_t *nr2);

/* uf6520 unite, intersect, or subtract solids */
extern UFUNEXPORT void FTN(uf6520)(int *ip1, tag_t *np2,
                        tag_t *np3, int *ip4,
                        int *ip5, int *ir6,
                        int *ir7, tag_t *nr8);

/* uf6523 split solids
   Replaced by UF_MODL_split_body */
extern UFUNEXPORT void FTN(uf6523)(tag_t *np1, int *ip2,
                        tag_t *np3, int *ip4,
                        int *ir5, int *ir6, tag_t *nr7);

/* uf6524 section solids */
extern UFUNEXPORT void FTN(uf6524)(tag_t *np1, int *ip2,
                        tag_t *np3, int *ip4,
                        int *ir5, int *ir6, tag_t *nr7);

/* uf6525 cut solids
   uf6525 can be replaced by UF_MODL_split_bo
   Note: UF_MODL_split_body does similar work but uses a 
   different parasolid call.  It can handle the splitting of bodies
   other than solids or planes.
*/
extern UFUNEXPORT void FTN(uf6525)(tag_t *np1, int *ip2,
                        tag_t *np3, int *ip4,
                        int *ir5, int *ir6, tag_t *nr7,
                        int *ir8);

/* uf6526 add blends to a solid */
extern UFUNEXPORT void FTN(uf6526)(tag_t *np1, int *ip2,
                        double *rp3, tag_t *np4,
                        int *ip5, tag_t *np6,
                        int *ip7, int *ir8);

/* uf6540 inquire box containing the specified body
   Replaced by UF_MODL_ask_bounding_box */
extern UFUNEXPORT void FTN(uf6540)(tag_t *np1, int *ir2, double *rr3);

/* uf6541 inquire containment of the specified point
   Replaced by UF_MODL_ask_point_containment */
extern UFUNEXPORT void FTN(uf6541)(double *rp1, tag_t *np2,
                        int *ir3, int *ir4);

/* uf6542 check the validity of bodies
   Replaced by UF_MODL_validate_body */
extern UFUNEXPORT void FTN(uf6542)(tag_t *np1, int *ip2,
                        int *ir3, int *ir4);

/* uf6543 return the mass properties of a body */
extern UFUNEXPORT void FTN(uf6543)(tag_t *np1, double *rp2,
                        int *ip3, int *ir4,
                        double *rr5, double *rr6);

/* uf6544 check the interference of bodies
   Replaced by UF_MODL_check_inteference */
extern UFUNEXPORT void FTN(uf6544)(tag_t *np1, tag_t *np2,
                        int *ip3, int *ir4,
                        int *ir5);

/* uf6545 intersect a ray with a list of bodies
   Replaced by UF_MODL_trace_a_ray */
extern UFUNEXPORT void FTN(uf6545)(const tag_t *np1, const int *ip2,
                        const double *rp3, const double *rp4,
                        const int *ip5, const double *rp6,
                        const double *rp7, int *ir8,
                        int *ir9, double *rr10, double *rr11,
                        int *ir12);

/* uf6546 read number of faces */
extern UFUNEXPORT void FTN(uf6546)(tag_t *np1, int *ir2,
                        int *ir3);

/* uf6547 read density of solid */
extern UFUNEXPORT void FTN(uf6547)(tag_t *np1, int *ip2,
                        int *ir3, double *rr4);

/* uf6548 edit density of solid */
extern UFUNEXPORT void FTN(uf6548)(tag_t *np1, double *rp2,
                        int *ip3, int *ir4);

/* Read global (default) solid density
   Replaced by UF_MODL_ask_default_density */
extern UFUNEXPORT void FTN(uf6549)
         (int *ip1,   /* units of denisty
                                     * 1 - lb/cu in
                                     * 2 - lb/cu ft
                                     * 3 - g /cu cm
                                     * 4 - kg/cu m      */
          int *ir2,   /* error code
                                     * 0 - success
                                     * 1 - fail         */
          double    *rr3);  /* global solid
                                     * density          */

/* Edit global (default) solid density
   Replaced by UF_MODL_set_default_density */
extern UFUNEXPORT void FTN(uf6550)
         (double    *rp1,   /* new density      */
          int *ip2,   /* units of denisty
                                     * 1 - lb/cu in
                                     * 2 - lb/cu ft
                                     * 3 - g /cu cm
                                     * 4 - kg/cu m      */
          int *ir3);  /* error code
                                     * 0 - success
                                     * 1 - fail         */


/**************************************************************************
Error Handler:
Returns the Error message from the last call to a solids routine. The
error message from the previous solid routine called is lost if UF6560
is not called right after that solid routine.

Environment: Internal  and  External
See Also:
History:
 *************************************************************************/
extern UFUNEXPORT int uc6560(
char cr1[300] /* <O>
            Returned Error Message (40 char max)
            */
);


/********************************************************************
Gets the parameters of a torus.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_torus_parms(
    tag_t feature_tag,   /* <I>
                            Feature object identifier
                         */
    int   edit,          /* <I>
                            Unused flag
                         */
    char **major_diameter, /* <OF>
                              Torus major diameter.   This must be
                              freed by calling UF_free.
                           */
    char **minor_diameter   /* <OF>
                               Torus minor diameter   This must be
                               freed by calling UF_free.
                            */
);

/********************************************************************
Gets the parameters of a prism.

Environment: Internal  and  External
See Also:
History:
********************************************************************/
extern UFUNEXPORT int UF_MODL_ask_prism_parms(
    tag_t feature_tag,        /* <I>
                                 Feature object identifier
                              */
    int   edit,               /* <I>
                                 Unused flag
                              */
    char **diameter,          /* <OF>
                                 Prism diameter.  This must be freed
                                 by calling UF_free.
                              */
    char **height,            /* <OF>
                                 Prism height.  This must be freed
                                 by calling UF_free.
                              */
    char **number_of_sides  /* <OF>
                               Number of sides in prism .  This must
                               be freed by calling UF_free.
                            */
);



#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_LEGACY_H_INCLUDED */


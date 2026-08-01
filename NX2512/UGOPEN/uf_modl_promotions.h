/*****************************************************************************
             Copyright (c) 1998-2003-2000 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       



File description: 
      This file contains routines pertaining to Promotions in Modelling.

*****************************************************************************/

#ifndef UF_MODL_PROMOTIONS_H_INCLUDED
#define UF_MODL_PROMOTIONS_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <uf_modl_types.h>
#include <libufun_exports.h>

#ifdef __cplusplus
extern "C" {
#endif

/******************************************************************************
Creates a promotion feature using the input body occurrence. The promotion
feature is created in the work part. The occurrence must be a solid body
occurrence from either the work part or one of its superassemblies.
The occurrence is also used to determine which of the possibly many copies of
the base solid in the assembly to promote.

Note : The Part Navigator may be left out of date with this call.
       Need to call UF_MODL_update to update it.
Environment: Internal  and  External
See Also :

History:
 *****************************************************************************/
extern UFUNEXPORT int UF_MODL_create_promotion(
tag_t body_occ ,/* <I>
                Tag of the body occurrence to be promoted
                */
tag_t * feature_tag  /* <O>
                     Tag of the newly created promotion feature
                     */
);

/******************************************************************************
Finds the promoted version of the given base body, face, or edge on the
promoted version of the solid given by the feature record. If no such edge or
face exists then a NULL_TAG is returned. An example where this could happen is
if an edge is modeled away on the promotion. This routine expects prototypes,
not occurrences and maps across a single level of promotions.  This routine
needs to be called multiple times to map up multiple promotion levels.

Environment: Internal  and  External
See Also:

History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_prom_map_object_up(
tag_t base_tag ,/* <I>
                tag of a base body, face, or edge
                */
tag_t prom_feat_tag ,/* <I>
                     tag of a promotion feature record
                     */
tag_t * prom_tag  /* <O>
                  tag of the promoted version of the given body, face,
                  or edge in the given promotion
                  */
);

/******************************************************************************
Given a promoted solid body, face, or edge, maps this body, face, or
edge down to the corresponding object on the base body. Returns a
NULL_TAG if there is no such object. An example where this could
happen is if a face is created as part of creating a feature at the
assembly level. In this case, There is no base face corresponding to
the promoted face. This routine maps across a single level of
promotions. This routine needs to be called multiple times to map
down multiple promotion levels.

Environment: Internal  and  External
See Also :
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_prom_map_object_down(
tag_t prom_tag ,/* <I>
                tag of a promoted body, face, or edge.
                */
tag_t * base_tag  /* <O>
                  tag of the base body, face, or edge corresponding to
                  the given promoted geometry
                  */
);

/******************************************************************************
Finds the promotion feature corresponding to the given promoted solid body.
This routine expects the solid body prototype, not an occurrence.

Environment: Internal  and  External
See Also: 
 UF_MODL_ask_solid_of_prom_feat
 UF_MODL_create_promotion
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_prom_feat_of_solid(
tag_t prom_solid ,/* <I>
                  Promoted solid to be queried
                  */
tag_t * prom_feat  /* <O>
                   Promotion feature corresponding to the promoted
                   solid
                   */
);

/******************************************************************************
Finds the promoted solid body created when applying the given
promotion feature.

Environment: Internal  and  External
See Also:
 UF_MODL_ask_prom_feat_of_solid
 UF_MODL_create_promotion
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_solid_of_prom_feat(
tag_t prom_feat ,/* <I>
                 Promotion feature to be queried
                 */
tag_t * prom_solid  /* <O>
                    Promoted solid
                    */
);

/******************************************************************************
Determines the instances that the given solid was promoted along.
The given solid should not be an occurrence.

Environment: Internal  and  External
See Also:
 UF_MODL_create_promotion
History:
 ******************************************************************************/
extern UFUNEXPORT int UF_MODL_ask_promotion_path (
tag_t prom_solid ,/* <I>
                  Promoted solid body to be queried
                  */
logical full_path ,/* <I>
                   If false, the instance path to the next level promotion is
                   returned.  If true, the full instance path across promotion
                   stacks is returned.
                   */
tag_t  ** instance_path ,/* <OF,len:num_instances>
                         The instance path along which the given solid body
                         was promoted.  This is an array of instances, which
                         must be freed by calling UF_free.
                         */
int  * num_instances  /* <O>
                      Number of instances
                      */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif     /* UF_MODL_PROMOTIONS_H_INCLUDED */

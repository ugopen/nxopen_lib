/*******************************************************************************

               Copyright (c) 2005 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved


 *

 ****************************************************************************/


#ifndef UF_WAVE_TYPES_INCLUDED
#define UF_WAVE_TYPES_INCLUDED

/***************************************************************************

  ***************************************************************************/


#include <uf_defs.h>

#ifdef __cplusplus
extern "C" {
#endif

/********************************************************************
*  UF_WAVE_linked_feature_info_s is used to store inter part related names
*  for linked geometry. This includes its associated feature name,
*  its owning part name, and its source part(s) name.
*
********************************************************************/
struct UF_WAVE_linked_feature_info_s {
    char *feature_name;       /* The name of the associated feature */
    char *owning_part_name;   /* The name of the owning part */
    char *source_part_name;   /* The name of the source part(s) */
};

typedef struct UF_WAVE_linked_feature_info_s UF_WAVE_linked_feature_info_t,
*UF_WAVE_linked_feature_info_p_t;


#ifdef __cplusplus
}
#endif

#endif /* UF_WAVE_TYPES_INCLUDED */

/*******************************************************************************

               Copyright (c) 1998  Corporation
                             Unpublished - All rights reserved
***************************************************************************



File description:

   This file contains all the error codes raised by the UF_WEIGHT module.
**************************************************************************/

#ifndef UF_WEIGHT_ERRORS_H_INCLUDED
#define UF_WEIGHT_ERRORS_H_INCLUDED


/***************************************************************************

  ***************************************************************************/

/*    

 */
#define ERROR_UF_WEIGHT_base   1860000 

#ifdef __cplusplus
extern "C" {
#endif

#define UF_WEIGHT_ERROR_BASE                      ERROR_UF_WEIGHT_base
#define UF_WEIGHT_ERROR_RANGE                     5000
#define UF_WEIGHT_NO_ERRORS                       0

#define UF_WEIGHT_incompatible_units             (UF_WEIGHT_ERROR_BASE +  1)
#define UF_WEIGHT_bad_properties                 (UF_WEIGHT_ERROR_BASE +  2)
#define UF_WEIGHT_not_in_work_part               (UF_WEIGHT_ERROR_BASE +  3)
#define UF_WEIGHT_has_no_assertion               (UF_WEIGHT_ERROR_BASE +  4)
#define UF_WEIGHT_bad_accuracy                   (UF_WEIGHT_ERROR_BASE +  5)
#define UF_WEIGHT_bad_cache_state                (UF_WEIGHT_ERROR_BASE +  6)
#define UF_WEIGHT_bad_mass_state                 (UF_WEIGHT_ERROR_BASE +  7)
#define UF_WEIGHT_bad_density_state              (UF_WEIGHT_ERROR_BASE +  8)
#define UF_WEIGHT_bad_volume_state               (UF_WEIGHT_ERROR_BASE +  9)
#define UF_WEIGHT_bad_area_state                 (UF_WEIGHT_ERROR_BASE + 10)
#define UF_WEIGHT_bad_cofm_state                 (UF_WEIGHT_ERROR_BASE + 11)
#define UF_WEIGHT_bad_mofi_state                 (UF_WEIGHT_ERROR_BASE + 12)
#define UF_WEIGHT_mvd_incompatible               (UF_WEIGHT_ERROR_BASE + 13)
#define UF_WEIGHT_part_load_failed               (UF_WEIGHT_ERROR_BASE + 14)

#ifdef __cplusplus
}
#endif

#endif /* UF_WEIGHT_ERRORS_H_INCLUDED */

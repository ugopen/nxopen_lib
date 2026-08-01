/*************************************************************************
         Copyright (c) 1998-1999 Unigraphics Solutions Inc.
                    Unpublished - All rights reserved



File description:

   This file contains all the error codes raised by the UF_WAVE module.
*************************************************************************/

#ifndef UF_WAVE_ERRORS_H_INCLUDED
#define UF_WAVE_ERRORS_H_INCLUDED


/***************************************************************************

  ***************************************************************************/



 /*

 */

#define ERROR_UF_WAVE_base     1915000
#define ERROR_UF_WEIGHT_base   1860000

#ifdef __cplusplus
extern "C" {
#endif

#define UF_WAVE_ERROR_BASE                        ERROR_UF_WAVE_base
#define UF_WAVE_ERROR_RANGE                       5000
#define UF_WAVE_NO_ERRORS                         0

#define UF_WAVE_part_load_failed                 (UF_WAVE_ERROR_BASE +  1)
#define UF_WAVE_mirror_or_region                 (UF_WAVE_ERROR_BASE +  2)
#define UF_WAVE_not_a_region                     (UF_WAVE_ERROR_BASE +  3)
#define UF_WAVE_not_a_mirror                     (UF_WAVE_ERROR_BASE +  4)
#define UF_WAVE_data_not_loaded                  (UF_WAVE_ERROR_BASE +  5)
#define UF_WAVE_faces_not_on_same_body           (UF_WAVE_ERROR_BASE +  6)
#define UF_WAVE_not_interpart_link               (UF_WAVE_ERROR_BASE +  7)
#define UF_WAVE_link_not_broken                  (UF_WAVE_ERROR_BASE +  8)
#define UF_WAVE_not_a_point                      (UF_WAVE_ERROR_BASE +  9)
#define UF_WAVE_mirror_region_or_point           (UF_WAVE_ERROR_BASE + 10)
#define UF_WAVE_interpart_only                   (UF_WAVE_ERROR_BASE + 11)
#define UF_WAVE_err_wave_not_avail               (UF_WAVE_ERROR_BASE + 12)
#define UF_WAVE_err_cannot_map                   (UF_WAVE_ERROR_BASE + 13)

#ifdef __cplusplus
}
#endif

#endif /* UF_WEIGHT_ERRORS_H_INCLUDED */


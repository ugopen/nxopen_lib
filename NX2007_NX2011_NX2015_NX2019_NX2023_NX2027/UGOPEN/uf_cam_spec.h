/*****************************************************************************
              Copyright (c) 1998-1999 Unigraphics Solutions, Inc.
                        Unpublished - All Rights Reserved


File description:
   This file contains the documentation for the pre-v16 UF_CAM module.

   UF_CAM_exit_id_t is the identifier type that is passed between NX CAM and a
   User Exit. This identifier is only used upon the original call to the User
   Exit. After receiving this identifier the User Exit must call
   UF_<module>_ask_<module> to retrieve the identifier which will be used in
   further transactions with NX CAM via the User Function layer for a
   particular module.


******************************************************************************/

#ifndef UF_CAM_OLD_H
#define UF_CAM_OLD_H


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>

#ifdef __cplusplus
extern "C" {
#endif

/********************************** Defines ***********************************/

/********************************** TypeDefs **********************************/

/****************************************************************************

   This is the identifier type that is passed between NX CAM and a User
   Exit. This identifier is only used upon the original call to the User
   Exit. After receiving this identifier the User Exit must call
   UF_<module>_ask_<module> to retrieve the identifier which will be used in
   further transactions with NX CAM via the User Function layer for a
   particular module.

*****************************************************************************/
typedef void   *UF_CAM_exit_id_t;


/******************************* Prototypes **********************************/

#ifdef __cplusplus
}
#endif

#endif

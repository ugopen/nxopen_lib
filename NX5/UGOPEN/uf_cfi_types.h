/****************************************************************************
              Copyright (c) 2003 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       


    
File Description:

Contains Open C API typedefs and macros that are specific to the CFI module.

******************************************************************************/
  

#ifndef UF_CFI_TYPES_INCLUDED
#define UF_CFI_TYPES_INCLUDED

/***************************************************************************

  ***************************************************************************/

#ifdef __cplusplus
extern "C" {
#endif

/* 
   Number of bytes allowed in an NX filename.  The plans are to
   increase this in the near future, so programs should use this parameter for
   checking on the length of a filename.

   When allocating a buffer, use UF_CFI_MAX_FILE_NAME_SIZE, e.g.
   char file_name[UF_CFI_MAX_FILE_NAME_SIZE];

*/
#define UF_CFI_MAX_FILE_NAME_LEN 128
#define UF_CFI_MAX_FILE_NAME_SIZE (UF_CFI_MAX_FILE_NAME_LEN + 1)

/* 
   Number of bytes allowed in an NX file specification.  The plans are
   to increase this in the near future, so programs should use this parameter 
   for checking on the length of a file specification.

   When allocating a buffer, use UF_CFI_MAX_PATH_NAME_SIZE, e.g.
   char file_spec[UF_CFI_MAX_PATH_NAME_SIZE];

*/
#define UF_CFI_MAX_PATH_NAME_LEN MAX_FSPEC_SIZE
#define UF_CFI_MAX_PATH_NAME_SIZE (UF_CFI_MAX_PATH_NAME_LEN + 1)

/*
    Define values used to define the cmode variable in uc4567
*/
#define UF_CFI_NEVER_REPLACE      0   /* if the destination file exists,
                                         do not overwrite it */
#define UF_CFI_ALWAYS_REPLACE     1   /* if the destination file exists,
                                         overwrite it */
#define UF_CFI_REPLACE_IF_NEWER   2   /* if the destination file exists,
                                         overwrite it only if the source file
                                         is newer than the destination file */
#define UF_CFI_LEGACY             3   /* if the destination file exists,
                                         do not overwrite it
                                         same as UF_CFI_NEVER_REPLACE */

#define UF_CFI_COPY               0   /* copy the source file to the
                                         destination file */
#define UF_CFI_MOVE              32   /* move the source file to the
                                         destination file */

#define UF_CFI_COPY_NEVER_REPLACE       (UF_CFI_COPY | UF_CFI_NEVER_REPLACE)
#define UF_CFI_COPY_ALWAYS_REPLACE      (UF_CFI_COPY | UF_CFI_ALWAYS_REPLACE)
#define UF_CFI_COPY_REPLACE_IF_NEWER    (UF_CFI_COPY | UF_CFI_REPLACE_IF_NEWER)
#define UF_CFI_COPY_LEGACY              (UF_CFI_COPY | UF_CFI_LEGACY)

#define UF_CFI_MOVE_NEVER_REPLACE       (UF_CFI_MOVE | UF_CFI_NEVER_REPLACE)
#define UF_CFI_MOVE_ALWAYS_REPLACE      (UF_CFI_MOVE | UF_CFI_ALWAYS_REPLACE)
#define UF_CFI_MOVE_REPLACE_IF_NEWER    (UF_CFI_MOVE | UF_CFI_REPLACE_IF_NEWER)
#define UF_CFI_MOVE_LEGACY              (UF_CFI_MOVE | UF_CFI_LEGACY)

#ifdef __cplusplus
}
#endif

#endif

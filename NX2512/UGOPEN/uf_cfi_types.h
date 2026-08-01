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

#include <uf_defs.h>

#ifdef __cplusplus
extern "C" {
#endif

/***************************************************************************
 *         Limit definitions
 *
 *  UF_CFI_MAX_FILE_NAME_LEN, UF_CFI_MAX_FILE_NAME_SIZE, UF_CFI_MAX_PATH_NAME_LEN,
 *  UF_CFI_MAX_PATH_NAME_SIZE are all being deprecated because NX is moving to 
 *  support multibyte characters.  User written programs should start using the
 *  new definitions for file specifications and simple file names:
 *    CFI_MAX_FILE_NAME_BUFSIZE
 *    MAX_FSPEC_BUFSIZE        should be used for buffer allocations and memory
 *                             allocations, e.g. char my_fspec[MAX_FSPEC_BUFSIZE];
 *    CFI_MAX_FILE_NAME_NCHARS
 *    MAX_FSPEC_NCHARS         should be used to limit the number of characters
 *                             in a buffer.  NX code will enforce these limits.
 *
 *  MAX_FSPEC_BUFSIZE and MAX_FSPEC_NCHARS are defined in uf_defs.h.
 *
 *  New routines have been added which will help in this transition:
 *     UF_TEXT_count_characters() will count the number of characters in a
 *     buffer.
 *     UF_TEXT_terminate_chars() will terminate a C string after the given
 *     number of characters.
 *
 *  When allocating a buffer, use UF_CFI_MAX_FILE_NAME_BUFSIZE, e.g.
 *  char file_name[UF_CFI_MAX_FILE_NAME_BUFSIZE];
 */
#define UF_CFI_MAX_FILE_NAME_NCHARS 1148
#define UF_CFI_MAX_FILE_NAME_BUFSIZE (NX_BUFSIZE(UF_CFI_MAX_FILE_NAME_NCHARS))

/*  */


/*  */
#define UF_CFI_MAX_PATH_NAME_LEN (MAX_FSPEC_BUFSIZE-1)
#define UF_CFI_MAX_PATH_NAME_SIZE MAX_FSPEC_BUFSIZE
#define UF_CFI_MAX_FILE_NAME_LEN (UF_CFI_MAX_FILE_NAME_BUFSIZE-1)
#define UF_CFI_MAX_FILE_NAME_SIZE (UF_CFI_MAX_FILE_NAME_BUFSIZE)
/*  */

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

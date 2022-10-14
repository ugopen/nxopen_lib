/*******************************************************************************
             Copyright (c) 1998-2001 Unigraphics Solutions Inc.
                       Unpublished - All Rights Reserved                       
******************************************************************************

 *

File Description :

Open C API definitions.  These are general typedefs and macros required by
all Open C API interfaces.  Typedefs that are specific to a particular
module will be placed in a header file for that specific module.

*****************************************************************************/

#ifndef UF_DEFS_INCLUDED
#define UF_DEFS_INCLUDED

#ifdef USE_PRAGMA_ONCE
#pragma once
#endif

/***************************************************************************

  ***************************************************************************/


#ifdef __cplusplus
extern "C" {
#endif

/****************************************************************************
 *         Limit definitions                                                *
 *
****************************************************************************/

#define MAX_FSPEC_SIZE        256  /* filespec len (not including '\0')    */
#define MAX_ENTITY_NAME_SIZE   30  /* entity name len (not including '\0') */
#define MAX_LINE_SIZE         132  /* line len (not including '\0')        */

/****************************************************************************
 *  All typedefs will have the following suffixes to denote their type:     *
 *                                                                          *
 *      _t      Data type                                                   *
 *      _p_t    Pointer to type                                             *
 *      _s      Structure tag                                               *
 *                                                                          *
 ****************************************************************************/

/*  typedef for all tags used in User Function.  The new term "tag" is      *
 *  used instead of the old term "EID" (Entity ID).                         */

#ifndef TAG_T_DEFINED
#define TAG_T_DEFINED
typedef unsigned int tag_t;
typedef tag_t *tag_p_t;
#endif

#ifndef UF_LIST_T_DEFINED
#define UF_LIST_T_DEFINED
typedef struct uf_list_s *uf_list_p_t;
struct uf_list_s {
        tag_t                  eid ;  /* Object ID */
        struct uf_list_s      *next;  /* Pointer to the next OID in the list */
};

typedef struct uf_list_s uf_list_t;
#endif

#ifndef NULL_TAG
#define NULL_TAG      ((tag_t)0)
#endif
#ifndef null_tag
#define null_tag      ((tag_t)0)
#endif

#ifndef PI
#define PI     3.14159265358979324
#endif

#ifndef TWOPI
#define TWOPI  6.28318530717958648
#endif

#ifndef RADEG
#define RADEG 57.29577951308235
#define DEGRA   .01745329251994328
#endif

/*  typedef for a logical variable.  Its value can be "false" or "true".    */

#ifndef LOGICAL_DEFINED
#define LOGICAL_DEFINED
#if defined(__cplusplus)
typedef bool logical;
#else
typedef unsigned char logical;
#endif
#endif

#ifndef BYTE_DEFINED
#define BYTE_DEFINED
typedef unsigned char byte;
#endif

#if !defined(true) && !defined(__cplusplus)
#define true   1
#define false  0
#endif

#ifndef TRUE
#define TRUE   1
#define FALSE  0
#endif

/****************************************************************************
 *      Macro definitions                                                   *
 ****************************************************************************/


/*****************************************************************
 *  ERROR_OK  macro                                              *
 *****************************************************************/
#ifndef ERROR_OK
#define ERROR_OK 0
#endif

/*****************************************************************
 *  FTN()  macro                                                 *
 *  Takes care of platform dependent C references of Fortran     *
 *  symbols.  This macro postpends an '_' (if necessary) on the  *
 *  Fortran symbols referenced from C.                           *
 *****************************************************************/
#ifndef FTN
#define FTN(name) name
#endif /* FTN */

/*****************************************************************
 *  DllExport                                                    *
 *  This macro is used in function prototypes on Windows NT to   *
 *  indicate that the associated function is to be exported from *
 *  the containing dynamic link library.  On other platforms the *
 *  macro is null.                                               *
 *****************************************************************/

#if defined(_WIN32)
#define DllExport __declspec(dllexport)
#else
#define DllExport
#endif


#ifdef __cplusplus
}
#endif

#endif /* UF_DEFS_INCLUDED */

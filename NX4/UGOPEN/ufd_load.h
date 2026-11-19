/*****************************************************************************
             Copyright (c) 1998-1999 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved                       

              
                                                                       
File Description                                                        
    This header file is used in conjunction with the ufd_example_shlib.c
    example file.
 ******************************************************************************/


#ifndef UFD_LOAD_H_INCLUDED
#define UFD_LOAD_H_INCLUDED

#include <uf_defs.h>

#ifdef __cplusplus
extern "C" {
#endif

extern DllExport int ep_a(int argc, char *argv[]);
extern DllExport int ep_b(int argc, char *argv[]);

#ifdef __cplusplus
}
#endif

#endif /* UFD_LOAD_H_INCLUDED */

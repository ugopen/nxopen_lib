/******************************************************************************
             Copyright (c) 1998-1999 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved                       



File description:

The type definitions and enums for the Open API interface to the GEXP module.
*******************************************************************************/

#ifndef UF_GEXP_TYPES_H_INCLUDED
#define UF_GEXP_TYPES_H_INCLUDED

#include <uf_modl.h>

#ifdef __cplusplus
extern "C" {
#endif

enum UF_GEXP_qualifier_e{
    UF_GEXP_NONE = 0,
    UF_GEXP_START_POINT =  UF_MODL_ENDPOINT_1,
    UF_GEXP_END_POINT =    UF_MODL_ENDPOINT_2
};

typedef enum UF_GEXP_qualifier_e UF_GEXP_qualifier_t;
#ifdef __cplusplus
}
#endif

#endif /* UF_GEXP_TYPES_H_INCLUDED */

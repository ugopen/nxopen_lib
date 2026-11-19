/*****************************************************************************
 *                    Copyright (c) 1999-2006 UGS Corp.
 *                    Unpublished - All rights reserved
 *
 *============================================================================
 *
 * File Name: uf_ui_route.h
 *
 * 
 *
 * File description:
 *
 *    This file contains functions for the Routing interactive routines
 *    callable from Internal NX Open C programs. 
 *
 ******************************************************************************/
#ifndef UF_UI_ROUTE_H_INCLUDED
#define UF_UI_ROUTE_H_INCLUDED

#ifdef __cplusplus
extern "C" {
#endif

/***************************** Include Files **********************************/
#include <uf_defs.h>
#include <uf_retiring_ugopenint.h>
#include <libugopenint_exports.h>
    
/**************************** Retired Functions ********************************

Retired functions:
------------------
The following functions have been retired and replaced with newer NX Open classes and methods:

    UF_UI_route_invoke_callback                Routing::CustomManager...

*/

/***************************** Public Defines *********************************/

/*
 *  */
/*
    Routing specify item modes.
*/

#define UF_UI_ROUTE_PLV_INDEX_PARTS             0
#define UF_UI_ROUTE_PLV_INDEX_STOCK             1
#define UF_UI_ROUTE_PLV_INDEX_OUTLET            2
#define UF_UI_ROUTE_PLV_INDEX_ELBOWS            3
#define UF_UI_ROUTE_PLV_INDEX_CUT_ELBOWS        4
#define UF_UI_ROUTE_PLV_INDEX_REPLACE_PART      5
#define UF_UI_ROUTE_PLV_INDEX_WIRES             6
#define UF_UI_ROUTE_PLV_INDEX_CABLES            7
#define UF_UI_ROUTE_PLV_INDEX_SHIELDS           8
#define UF_UI_ROUTE_PLV_INDEX_SPACE_RESERVATION 9
#define UF_UI_ROUTE_PLV_INDEX_FILLERS           10
#define UF_UI_ROUTE_PLV_INDEX_OVERSTOCK         11
#define UF_UI_ROUTE_PLV_INDEX_CABLE_CONDUITS    12

/*  */
/* Index used for identifying node of platform plate */
#define UF_UI_ROUTE_PLV_INDEX_PLATFORM_PLATE    13 

/*  */
/* Index used for identifying node of duct reinforcement*/
#define UF_UI_ROUTE_PLV_INDEX_DUCT_REINFORCEMENT    14

/*  */
/* Index used for identifying node for connection post placement parts*/
#define UF_UI_ROUTE_PLV_INDEX_CONN_POST_PLACEMENT   15

#define UF_UI_ROUTE_PLV_INDEX_ENDFORMS              16

#define UF_UI_ROUTE_PLV_INDEX_HANGER                17


#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif /*UF_UI_ROUTE_H_INCLUDED*/

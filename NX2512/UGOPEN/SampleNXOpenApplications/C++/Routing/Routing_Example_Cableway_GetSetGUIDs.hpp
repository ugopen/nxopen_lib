/*==================================================================================================
                                       Copyright 2021 Siemens
====================================================================================================

    NOTE:  NX Development provides programming examples for illustration only.
    NX Development assumes you are familiar with the programming language
    demonstrated in these examples, and the tools used to create and debug NX/Open
    programs. GTAC support professionals can help explain the functionality of
    a particular procedure, but neither GTAC nor NX Development will modify
    these examples to provide added functionality or construction procedures.

File description:

    An example program that gets and sets Globally Unique Identifiers (GUID) on control points
    and cableway network point occurrences.

    See Routing_Example_Cableway_GetSetGUIDs.cpp for the implementation.


==================================================================================================*/
#ifndef CABLEWAY_IMPORTDATASET_HPP_INCLUDED
#define CABLEWAY_IMPORTDATASET_HPP_INCLUDED

#ifdef USE_PRAGMA_ONCE
#pragma once
#endif

#include <uf_defs.h>

// Prototype for ufusr
extern "C" DllExport void ufusr( char* param, int* returncode, int param_len );

#endif

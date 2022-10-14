#ifndef NXOpen_PID_PROPERTYTYPE_HXX_INCLUDED
#define NXOpen_PID_PROPERTYTYPE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PID_PropertyType.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PID
    {
        /** Represents the property type. 
         <br>  Created in NX1847.0.0.  <br>  
        */
        enum PropertyType
        {
            PropertyTypeNull/** Null type */,
            PropertyTypeIndex/** Index of object */,
            PropertyTypeUserAttribute/** User attribute */,
            PropertyTypeNeedAttribute/** Need attribute */,
            PropertyTypeFulfillmentAttribute/** Fulfillment attribute */,
            PropertyTypePipeStockAttribute/** Pipe stock attribute */,
            PropertyTypePidTag/** The tag of PID object */,
            PropertyTypeParentRun/** The parent run of pipe stock */,
            PropertyTypeQuantity/** The quantity of same object */ = 11,
            PropertyTypeSystem/** The system of object */ = 101,
            PropertyTypeRunAttribute/** The attibute of run object */,
            PropertyTypeEquipmentAttribute/** The attibute of equipment object */
        };

    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#endif
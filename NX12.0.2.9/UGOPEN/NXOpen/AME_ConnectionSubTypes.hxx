#ifndef NXOpen_AME_CONNECTIONSUBTYPES_HXX_INCLUDED
#define NXOpen_AME_CONNECTIONSUBTYPES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_ConnectionSubTypes.ja
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
    namespace AME
    {
        /** Represents electrical connection Pontential Types
            */
        enum AmeElectricalConnectionPotentialType
        {
            AmeElectricalConnectionPotentialTypeL/** l */ ,
            AmeElectricalConnectionPotentialTypeN/** n */ ,
            AmeElectricalConnectionPotentialTypePe/** pe */ ,
            AmeElectricalConnectionPotentialTypeLPlus/** lplus */ ,
            AmeElectricalConnectionPotentialTypeLDash/** ldash */ ,
            AmeElectricalConnectionPotentialTypeUndefined/** undefined */ ,
            AmeElectricalConnectionPotentialTypeInvalid/** invalid */ 
        };

        /** Represents optical connection fiber types
            */
        enum AmeOpticalConnectionFiberType
        {
            AmeOpticalConnectionFiberTypeSingleMode/** single mode */ ,
            AmeOpticalConnectionFiberTypeMultiMode/** multi mode */ ,
            AmeOpticalConnectionFiberTypeUndefined/** undefined */ ,
            AmeOpticalConnectionFiberTypeInvalid/** invalid */ 
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
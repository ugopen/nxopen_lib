#ifndef NXOpen_CAE_CONNECTIONS_TYPES_HXX_INCLUDED
#define NXOpen_CAE_CONNECTIONS_TYPES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Connections_Types.ja
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
    namespace CAE
    {
        namespace Connections
        {
            /** Material definition types */
            enum MaterialType
            {
                MaterialTypeUser/** User defined material */,
                MaterialTypeFromSupport/** Material defined from support */
            };

            /** Diameter definition types */
            enum DiameterType
            {
                DiameterTypeUser/** User defined diameter */,
                DiameterTypeFormula/** Formula defined diameter */
            };

            /** Types of height definitions */
            enum HeightType
            {
                HeightTypeUser/** User defined thickness */,
                HeightTypeMeanOfFlangesThickness/** Mean of flanges thickness */,
                HeightTypeDistanceBetweenFlanges/** Distance between flanges */,
                HeightTypeDistanceBetweenFlangesMeanOfFlangesThickness/** Distance between flanges - Mean of flanges thickness */,
                HeightTypeDistanceBetweenFlangesMaxOfFlangesThickness/** Distance between flanges - Max of flanges thickness */
            };

            /** Location type */
            enum LocationType
            {
                LocationTypeCoordinates/** Coordinates */,
                LocationTypePoint/** Point */,
                LocationTypeNode/** Node */
            };

            /** Connection type */
            enum ConnectionType
            {
                ConnectionTypeSpotWeld/** SpotWeld */,
                ConnectionTypeGlue/** Glue */,
                ConnectionTypeBolt/** Bolt */
            };

            /** Element type */
            enum ElementType
            {
                ElementTypeNone/** None */,
                ElementTypeEHex8/** Hex8 */,
                ElementTypeEHex8Spider/** Hex8 + Spider */,
                ElementTypeE1d/** 1D */,
                ElementTypeE1DSpider/** 1D + Spider */
            };

            /** Element status */
            enum ElementStatusType
            {
                ElementStatusTypeInvalid/** Invalid */,
                ElementStatusTypeNotUpdated/** Not updated */,
                ElementStatusTypeUpdated/** Updated */
            };

        }
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

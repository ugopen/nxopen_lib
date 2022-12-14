#ifndef NXOpen_MOTION_BEARINGPROPERTYBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_BEARINGPROPERTYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_BearingPropertyBuilder.ja
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
#include <NXOpen/Motion_EntityPropTableBuilder.hxx>
#include <NXOpen/libnxopencpp_motion_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Motion
    {
        class BearingPropertyBuilder;
    }
    namespace Motion
    {
        class EntityPropTableBuilder;
    }
    namespace Motion
    {
        class _BearingPropertyBuilderBuilder;
        class BearingPropertyBuilderImpl;
        /** Represents a @link Motion::BearingProperty Motion::BearingProperty@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Motion::BearingPropertyCollection::CreateBearingPropertyBuilder  NXOpen::Motion::BearingPropertyCollection::CreateBearingPropertyBuilder @endlink  <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  BearingPropertyBuilder : public NXOpen::Motion::EntityPropTableBuilder
        {
            /** Bearing Property bearing types */
            public: enum BearingType
            {
                BearingTypeStandard/** standard */ ,
                BearingTypeDeepGrooveBall/** deep groove ball */ ,
                BearingTypeAngularContactBall/** angular contact ball */ ,
                BearingTypeThrustBall/** thrust ball */ ,
                BearingTypeCylindricalRoller/** cylindrical roller */ ,
                BearingTypeTaperedRoller/** tapered roller */ 
            };

            /** Bearing Property reference ring */
            public: enum ReferenceRing
            {
                ReferenceRingInner/** inner */ ,
                ReferenceRingOuter/** outer */ 
            };

            /** Bearing Property local compliance type */
            public: enum LocalComplianceType
            {
                LocalComplianceTypeDry/** dry */ ,
                LocalComplianceTypeWet/** wet */ ,
                LocalComplianceTypeWetD/** wet d */ 
            };

            /** Bearing Property micro geometry type */
            public: enum MicrogeometryType
            {
                MicrogeometryTypeProfile2d/** profile2d */ ,
                MicrogeometryTypeFunction/** function */ 
            };

            /** Bearing Property diagonal damping value type */
            public: enum DiagonalDampingType
            {
                DiagonalDampingTypeAbsolute/** absolute */ ,
                DiagonalDampingTypeVariablePercentage/** variable percentage */ ,
                DiagonalDampingTypeConstantPercentage/** constant percentage */ 
            };

            private: BearingPropertyBuilderImpl * m_bearingpropertybuilder_impl;
            private: friend class  _BearingPropertyBuilderBuilder;
            protected: BearingPropertyBuilder();
            public: ~BearingPropertyBuilder();
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

#undef EXPORTLIBRARY
#endif

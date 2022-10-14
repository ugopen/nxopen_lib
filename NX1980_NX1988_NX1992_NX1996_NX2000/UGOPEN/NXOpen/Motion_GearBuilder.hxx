#ifndef NXOpen_MOTION_GEARBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_GEARBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_GearBuilder.ja
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
        class GearBuilder;
    }
    namespace Motion
    {
        class EntityPropTableBuilder;
    }
    namespace Motion
    {
        class _GearBuilderBuilder;
        class GearBuilderImpl;
        /** Represents a @link Motion::Gear Motion::Gear@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Motion::GearCollection::CreateGearBuilder  NXOpen::Motion::GearCollection::CreateGearBuilder @endlink  <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  GearBuilder : public NXOpen::Motion::EntityPropTableBuilder
        {
            /** Geometry Gear types */
            public: enum GeometryType
            {
                GeometryTypeInternal/** internal */ ,
                GeometryTypeExternal/** external */ 
            };

            /** Helix Hand Gear types */
            public: enum HelixHand
            {
                HelixHandLeft/** left */ ,
                HelixHandRight/** right */ 
            };

            /** Flanks Dependency Gear types */
            public: enum FlanksDependency
            {
                FlanksDependencyNone/** none */ ,
                FlanksDependencyRadial/** radial */ ,
                FlanksDependencyAxial/** axial */ ,
                FlanksDependencyBoth/** both */ 
            };

            private: GearBuilderImpl * m_gearbuilder_impl;
            private: friend class  _GearBuilderBuilder;
            protected: GearBuilder();
            public: ~GearBuilder();
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
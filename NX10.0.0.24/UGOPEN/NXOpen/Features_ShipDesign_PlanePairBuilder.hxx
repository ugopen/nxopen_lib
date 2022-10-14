#ifndef NXOpen_FEATURES_SHIPDESIGN_PLANEPAIRBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_PLANEPAIRBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_PlanePairBuilder.ja
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
#include <NXOpen/Features_ShipDesign_PlanePairBuilder.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace ShipDesign
        {
            class PlanePairBuilder;
        }
    }
    class NXObject;
    class Plane;
    namespace Features
    {
        namespace ShipDesign
        {
            class _PlanePairBuilderBuilder;
            class PlanePairBuilderImpl;
            /**
                This class is used to define a pair of planes in a list.
                
             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  PlanePairBuilder : public NXOpen::NXObject
            {
                private: PlanePairBuilderImpl * m_planepairbuilder_impl;
                private: friend class  _PlanePairBuilderBuilder;
                protected: PlanePairBuilder();
                public: ~PlanePairBuilder();
                /**Returns  the first plane in the plane pair list element. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Plane * Plane1
                (
                );
                /**Sets  the first plane in the plane pair list element. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetPlane1
                (
                    NXOpen::Plane * plane1 /** plane1 */ 
                );
                /**Returns  the second plane in the plane pair list element. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Plane * Plane2
                (
                );
                /**Sets  the second plane in the plane pair list element. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetPlane2
                (
                    NXOpen::Plane * plane2 /** plane2 */ 
                );
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

#undef EXPORTLIBRARY
#endif
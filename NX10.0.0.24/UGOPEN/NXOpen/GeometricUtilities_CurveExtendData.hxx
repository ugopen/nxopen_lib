#ifndef NXOpen_GEOMETRICUTILITIES_CURVEEXTENDDATA_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_CURVEEXTENDDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_CurveExtendData.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/GeometricUtilities_CurveExtendData.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_geometricutilities_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace GeometricUtilities
    {
        class CurveExtendData;
    }
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class SelectDisplayableObject;
    namespace GeometricUtilities
    {
        class _CurveExtendDataBuilder;
        class CurveExtendDataImpl;
        /** Represents a @link NXOpen::GeometricUtilities::CurveExtendData NXOpen::GeometricUtilities::CurveExtendData@endlink  
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  CurveExtendData : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** Represents the curve extend options for associative basic curves*/
            public: enum LimitOptions
            {
                LimitOptionsValue/** Value */,
                LimitOptionsAtPoint/** At Point */,
                LimitOptionsUntilSelected/** Until Selected */
            };

            private: CurveExtendDataImpl * m_curveextenddata_impl;
            private: friend class  _CurveExtendDataBuilder;
            protected: CurveExtendData();
            public: ~CurveExtendData();
            /**Returns  the limit option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::CurveExtendData::LimitOptions LimitOption
            (
            );
            /**Sets  the limit option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") OR cam_base ("CAM BASE") */
            public: void SetLimitOption
            (
                NXOpen::GeometricUtilities::CurveExtendData::LimitOptions limitOption /** limitoption */ 
            );
            /**Returns  the distance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Distance
            (
            );
            /**Returns  the until selected object 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObject * UntilSelectedObject
            (
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful 
             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: virtual bool Validate
            (
            );
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

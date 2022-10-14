#ifndef NXOpen_GEOMETRICUTILITIES_MODLALONGCURVEANGLE_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_MODLALONGCURVEANGLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_ModlAlongCurveAngle.ja
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
#include <NXOpen/GeometricUtilities_ModlAlongCurveAngle.hxx>
#include <NXOpen/GeometricUtilities_OnPathDimensionBuilder.hxx>
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
        class ModlAlongCurveAngle;
    }
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricUtilities
    {
        class OnPathDimensionBuilder;
    }
    class SelectCurve;
    namespace GeometricUtilities
    {
        class _ModlAlongCurveAngleBuilder;
        class ModlAlongCurveAngleImpl;
        /** This class @link NXOpen::GeometricUtilities::ModlAlongCurveAngle NXOpen::GeometricUtilities::ModlAlongCurveAngle@endlink  represents motion type in ModlMotion 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  ModlAlongCurveAngle : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: ModlAlongCurveAngleImpl * m_modlalongcurveangle_impl;
            private: friend class  _ModlAlongCurveAngleBuilder;
            protected: ModlAlongCurveAngle();
            public: ~ModlAlongCurveAngle();
            /**Returns  the curve on which doing the transform. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectCurve * Curve
            (
            );
            /**Returns  the value of angular transform. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * AlongCurveAngle
            (
            );
            /**Returns  the value of transform. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::OnPathDimensionBuilder * AlongCurve
            (
            );
            /**Returns  whether the direction of the curve to determine the transform should be reversed or not. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool ReverseCurveDirection
            (
            );
            /**Sets  whether the direction of the curve to determine the transform should be reversed or not. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void SetReverseCurveDirection
            (
                bool reverseCurveDirection /** reversecurvedirection */ 
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
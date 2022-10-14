#ifndef NXOpen_MOTION_BUSHINGSPHERICALCOEFFICIENTSCOMPONENT_HXX_INCLUDED
#define NXOpen_MOTION_BUSHINGSPHERICALCOEFFICIENTSCOMPONENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_BushingSphericalCoefficientsComponent.ja
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
#include <NXOpen/Motion.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class BushingSphericalCoefficientsComponent;
    }
    namespace CAE
    {
        class Function;
    }
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Motion
    {
        class SelectFieldData;
    }
    namespace Motion
    {
        class _BushingSphericalCoefficientsComponentBuilder;
        class BushingSphericalCoefficientsComponentImpl;
        /**
            Represents a Motion BushingSphericalCoefficientsComponent
            
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  BushingSphericalCoefficientsComponent : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: BushingSphericalCoefficientsComponentImpl * m_bushingsphericalcoefficientscomponent_impl;
            private: friend class  _BushingSphericalCoefficientsComponentBuilder;
            protected: BushingSphericalCoefficientsComponent();
            public: ~BushingSphericalCoefficientsComponent();
            /**Returns  the radial type 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Motion::ConnectorCoefficientTypes RadialType
            (
            );
            /**Sets  the radial type 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetRadialType
            (
                NXOpen::Motion::ConnectorCoefficientTypes radialType /** radialtype */ 
            );
            /**Returns  the radial function type 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::Function * RadialFunction
            (
            );
            /**Sets  the radial function type 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetRadialFunction
            (
                NXOpen::CAE::Function * radialFunction /** radialfunction */ 
            );
            /**Returns  the conical coefficient type 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Motion::ConnectorCoefficientTypes ConicalType
            (
            );
            /**Sets  the conical coefficient type 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetConicalType
            (
                NXOpen::Motion::ConnectorCoefficientTypes conicalType /** conicaltype */ 
            );
            /**Returns  the conical function type 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::Function * ConicalFunction
            (
            );
            /**Sets  the conical function type 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetConicalFunction
            (
                NXOpen::CAE::Function * conicalFunction /** conicalfunction */ 
            );
            /**Returns  the radial expression type 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RadialExpression
            (
            );
            /**Returns  the conical expression type 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ConicalExpression
            (
            );
            /**Returns  the conical curve profile. It is available only when 
                    @link Motion::BushingSphericalCoefficientsComponent::SetConicalType Motion::BushingSphericalCoefficientsComponent::SetConicalType@endlink  is set to @link Motion::ConnectorCoefficientTypesProfile2d Motion::ConnectorCoefficientTypesProfile2d@endlink  or
                    @link Motion::ConnectorCoefficientTypesExpressionAndProfile2d Motion::ConnectorCoefficientTypesExpressionAndProfile2d@endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::SelectFieldData * ConicalCurveProfile
            (
            );
            /**Returns  the radial curve profile. It is available only when 
                    @link Motion::BushingSphericalCoefficientsComponent::SetRadialType Motion::BushingSphericalCoefficientsComponent::SetRadialType@endlink  is set to @link Motion::ConnectorCoefficientTypesProfile2d Motion::ConnectorCoefficientTypesProfile2d@endlink  or
                    @link Motion::ConnectorCoefficientTypesExpressionAndProfile2d Motion::ConnectorCoefficientTypesExpressionAndProfile2d@endlink  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::SelectFieldData * RadialCurveProfile
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
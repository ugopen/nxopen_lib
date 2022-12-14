#ifndef NXOpen_MOTION_BUSHINGCYLINDRICALCOEFFICIENTSCOMPONENT_HXX_INCLUDED
#define NXOpen_MOTION_BUSHINGCYLINDRICALCOEFFICIENTSCOMPONENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_BushingCylindricalCoefficientsComponent.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/Motion.hxx>
#include <NXOpen/Motion_BushingCylindricalCoefficientsComponent.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class BushingCylindricalCoefficientsComponent;
    }
    namespace CAE
    {
        class Function;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Motion
    {
        class _BushingCylindricalCoefficientsComponentBuilder;
        class BushingCylindricalCoefficientsComponentImpl;
        /**
            Represents a Motion BushingCylindricalCoefficientsComponent
            */
        class NXOPENCPPEXPORT  BushingCylindricalCoefficientsComponent : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            private: BushingCylindricalCoefficientsComponentImpl * m_bushingcylindricalcoefficientscomponent_impl;
            private: friend class  _BushingCylindricalCoefficientsComponentBuilder;
            protected: BushingCylindricalCoefficientsComponent();
            public: ~BushingCylindricalCoefficientsComponent();
            /**Returns  the radial type  <br> License requirements : None */
            public: NXOpen::Motion::ConnectorCoefficientTypes RadialType
            (
            );
            /**Sets  the radial type  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetRadialType
            (
                NXOpen::Motion::ConnectorCoefficientTypes radialType /** radialtype */ 
            );
            /**Returns  the radial, it is available only when 
                    @link Motion::BushingCylindricalCoefficientsComponent::RadialType Motion::BushingCylindricalCoefficientsComponent::RadialType @endlink and @link Motion::BushingCylindricalCoefficientsComponent::SetRadialType Motion::BushingCylindricalCoefficientsComponent::SetRadialType @endlink  set to @link Motion::ConnectorCoefficientTypesConstant Motion::ConnectorCoefficientTypesConstant@endlink  case  <br> License requirements : None */
            public: double Radial
            (
            );
            /**Sets  the radial, it is available only when 
                    @link Motion::BushingCylindricalCoefficientsComponent::RadialType Motion::BushingCylindricalCoefficientsComponent::RadialType @endlink and @link Motion::BushingCylindricalCoefficientsComponent::SetRadialType Motion::BushingCylindricalCoefficientsComponent::SetRadialType @endlink  set to @link Motion::ConnectorCoefficientTypesConstant Motion::ConnectorCoefficientTypesConstant@endlink  case  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetRadial
            (
                double radial /** radial */ 
            );
            /**Returns  the longitudinal double value, it is available only when 
                    @link Motion::BushingCylindricalCoefficientsComponent::RadialType Motion::BushingCylindricalCoefficientsComponent::RadialType @endlink and @link Motion::BushingCylindricalCoefficientsComponent::SetRadialType Motion::BushingCylindricalCoefficientsComponent::SetRadialType @endlink  set to @link Motion::ConnectorCoefficientTypesConstant Motion::ConnectorCoefficientTypesConstant@endlink  case  <br> License requirements : None */
            public: double Longitudinal
            (
            );
            /**Sets  the longitudinal double value, it is available only when 
                    @link Motion::BushingCylindricalCoefficientsComponent::RadialType Motion::BushingCylindricalCoefficientsComponent::RadialType @endlink and @link Motion::BushingCylindricalCoefficientsComponent::SetRadialType Motion::BushingCylindricalCoefficientsComponent::SetRadialType @endlink  set to @link Motion::ConnectorCoefficientTypesConstant Motion::ConnectorCoefficientTypesConstant@endlink  case  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetLongitudinal
            (
                double longitudinal /** longitudinal */ 
            );
            /**Returns  the radial function tag, it is available only when 
                    @link Motion::BushingCylindricalCoefficientsComponent::RadialType Motion::BushingCylindricalCoefficientsComponent::RadialType @endlink and @link Motion::BushingCylindricalCoefficientsComponent::SetRadialType Motion::BushingCylindricalCoefficientsComponent::SetRadialType @endlink  set to @link Motion::ConnectorCoefficientTypesSpline Motion::ConnectorCoefficientTypesSpline@endlink  case  <br> License requirements : None */
            public: NXOpen::CAE::Function * RadialFunction
            (
            );
            /**Sets  the radial function tag, it is available only when 
                    @link Motion::BushingCylindricalCoefficientsComponent::RadialType Motion::BushingCylindricalCoefficientsComponent::RadialType @endlink and @link Motion::BushingCylindricalCoefficientsComponent::SetRadialType Motion::BushingCylindricalCoefficientsComponent::SetRadialType @endlink  set to @link Motion::ConnectorCoefficientTypesSpline Motion::ConnectorCoefficientTypesSpline@endlink  case  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetRadialFunction
            (
                NXOpen::CAE::Function * function /** function */ 
            );
            /**Returns  the longitudinal function tag, it is available only when 
                    @link Motion::BushingCylindricalCoefficientsComponent::RadialType Motion::BushingCylindricalCoefficientsComponent::RadialType @endlink and @link Motion::BushingCylindricalCoefficientsComponent::SetRadialType Motion::BushingCylindricalCoefficientsComponent::SetRadialType @endlink  set to @link Motion::ConnectorCoefficientTypesSpline Motion::ConnectorCoefficientTypesSpline@endlink  case  <br> License requirements : None */
            public: NXOpen::CAE::Function * LongitudinalFunction
            (
            );
            /**Sets  the longitudinal function tag, it is available only when 
                    @link Motion::BushingCylindricalCoefficientsComponent::RadialType Motion::BushingCylindricalCoefficientsComponent::RadialType @endlink and @link Motion::BushingCylindricalCoefficientsComponent::SetRadialType Motion::BushingCylindricalCoefficientsComponent::SetRadialType @endlink  set to @link Motion::ConnectorCoefficientTypesSpline Motion::ConnectorCoefficientTypesSpline@endlink  case  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetLongitudinalFunction
            (
                NXOpen::CAE::Function * function /** function */ 
            );
            /**Returns  the conical coefficient type  <br> License requirements : None */
            public: NXOpen::Motion::ConnectorCoefficientTypes ConicalType
            (
            );
            /**Sets  the conical coefficient type  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetConicalType
            (
                NXOpen::Motion::ConnectorCoefficientTypes conicalType /** conicaltype */ 
            );
            /**Returns  the conical coefficient, it is available only when 
                    @link Motion::BushingCylindricalCoefficientsComponent::ConicalType Motion::BushingCylindricalCoefficientsComponent::ConicalType @endlink and @link Motion::BushingCylindricalCoefficientsComponent::SetConicalType Motion::BushingCylindricalCoefficientsComponent::SetConicalType @endlink  set to @link Motion::ConnectorCoefficientTypesConstant Motion::ConnectorCoefficientTypesConstant@endlink  case  <br> License requirements : None */
            public: double Conical
            (
            );
            /**Sets  the conical coefficient, it is available only when 
                    @link Motion::BushingCylindricalCoefficientsComponent::ConicalType Motion::BushingCylindricalCoefficientsComponent::ConicalType @endlink and @link Motion::BushingCylindricalCoefficientsComponent::SetConicalType Motion::BushingCylindricalCoefficientsComponent::SetConicalType @endlink  set to @link Motion::ConnectorCoefficientTypesConstant Motion::ConnectorCoefficientTypesConstant@endlink  case  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetConical
            (
                double conical /** conical */ 
            );
            /**Returns  the torsional coefficient, it is available only when 
                    @link Motion::BushingCylindricalCoefficientsComponent::ConicalType Motion::BushingCylindricalCoefficientsComponent::ConicalType @endlink and @link Motion::BushingCylindricalCoefficientsComponent::SetConicalType Motion::BushingCylindricalCoefficientsComponent::SetConicalType @endlink  set to @link Motion::ConnectorCoefficientTypesConstant Motion::ConnectorCoefficientTypesConstant@endlink  case  <br> License requirements : None */
            public: double Torsional
            (
            );
            /**Sets  the torsional coefficient, it is available only when 
                    @link Motion::BushingCylindricalCoefficientsComponent::ConicalType Motion::BushingCylindricalCoefficientsComponent::ConicalType @endlink and @link Motion::BushingCylindricalCoefficientsComponent::SetConicalType Motion::BushingCylindricalCoefficientsComponent::SetConicalType @endlink  set to @link Motion::ConnectorCoefficientTypesConstant Motion::ConnectorCoefficientTypesConstant@endlink  case  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetTorsional
            (
                double torsional /** torsional */ 
            );
            /**Returns  the conical function tag, it is available only when 
                    @link Motion::BushingCylindricalCoefficientsComponent::ConicalType Motion::BushingCylindricalCoefficientsComponent::ConicalType @endlink and @link Motion::BushingCylindricalCoefficientsComponent::SetConicalType Motion::BushingCylindricalCoefficientsComponent::SetConicalType @endlink  set to @link Motion::ConnectorCoefficientTypesSpline Motion::ConnectorCoefficientTypesSpline@endlink  case  <br> License requirements : None */
            public: NXOpen::CAE::Function * ConicalFunction
            (
            );
            /**Sets  the conical function tag, it is available only when 
                    @link Motion::BushingCylindricalCoefficientsComponent::ConicalType Motion::BushingCylindricalCoefficientsComponent::ConicalType @endlink and @link Motion::BushingCylindricalCoefficientsComponent::SetConicalType Motion::BushingCylindricalCoefficientsComponent::SetConicalType @endlink  set to @link Motion::ConnectorCoefficientTypesSpline Motion::ConnectorCoefficientTypesSpline@endlink  case  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetConicalFunction
            (
                NXOpen::CAE::Function * function /** function */ 
            );
            /**Returns  the torsional function tag, it is available only when 
                    @link Motion::BushingCylindricalCoefficientsComponent::ConicalType Motion::BushingCylindricalCoefficientsComponent::ConicalType @endlink and @link Motion::BushingCylindricalCoefficientsComponent::SetConicalType Motion::BushingCylindricalCoefficientsComponent::SetConicalType @endlink  set to @link Motion::ConnectorCoefficientTypesSpline Motion::ConnectorCoefficientTypesSpline@endlink  case  <br> License requirements : None */
            public: NXOpen::CAE::Function * TorsionalFunction
            (
            );
            /**Sets  the torsional function tag, it is available only when 
                    @link Motion::BushingCylindricalCoefficientsComponent::ConicalType Motion::BushingCylindricalCoefficientsComponent::ConicalType @endlink and @link Motion::BushingCylindricalCoefficientsComponent::SetConicalType Motion::BushingCylindricalCoefficientsComponent::SetConicalType @endlink  set to @link Motion::ConnectorCoefficientTypesSpline Motion::ConnectorCoefficientTypesSpline@endlink  case  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetTorsionalFunction
            (
                NXOpen::CAE::Function * function /** function */ 
            );
            /** Returns true if the inputs to the component are sufficient for 
                        commit to be called.  For example, if the component requires
                        you to set some property, this method will return false if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful  <br> License requirements : None */
            public: virtual bool Validate
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif

#ifndef NXOpen_GEOMETRICUTILITIES_PATTERNCLOCKING_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_PATTERNCLOCKING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_PatternClocking.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/GeometricUtilities_PatternClocking.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricUtilities
    {
        class PatternClocking;
    }
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricUtilities
    {
        class _PatternClockingBuilder;
        class PatternClockingImpl;
        /**  enables the ability to apply delta transforms on individual instances of a pattern within the pattern feature */
        class NXOPENCPPEXPORT  PatternClocking : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            /** type of pattern clocking to transform individual instances */
            public: enum ClockingType
            {
                ClockingTypeWithinPatternDefinitionLinear/** within pattern definition linear */ ,
                ClockingTypeWithinPatternDefinitionCircular/** within pattern definition circular */ 
            };

            private: PatternClockingImpl * m_patternclocking_impl;
            private: friend class  _PatternClockingBuilder;
            protected: PatternClocking();
            public: ~PatternClocking();
            /**Returns  the clocking enum to determine if linear or angular clocking  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::PatternClocking::ClockingType ClockType
            (
            );
            /**Returns  the x direction delta for linear clocking  <br> License requirements : None */
            public: NXOpen::Expression * Direction1Delta
            (
            );
            /** Sets an x direction delta for linear clocking  <br> License requirements : None */
            public: void SetXDirectionDelta
            (
                const NXString & direction1Exp /** distance delta   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the y direction delta for linear clocking  <br> License requirements : None */
            public: NXOpen::Expression * Direction2Delta
            (
            );
            /** Sets a y direction delta for linear clocking  <br> License requirements : None */
            public: void SetYDirectionDelta
            (
                const NXString & direction2Exp /** distance delta   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the angular delta for circular clocking  <br> License requirements : None */
            public: NXOpen::Expression * AngularDelta
            (
            );
            /** Sets a angular delta for circular clocking  <br> License requirements : None */
            public: void SetAngularDelta
            (
                const NXString & angularDeltaExp /** angular delta in degrees   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the radial delta for circular clocking  <br> License requirements : None */
            public: NXOpen::Expression * RadialDelta
            (
            );
            /** Sets a radial delta for circular clocking  <br> License requirements : None */
            public: void SetRadialDelta
            (
                const NXString & radialDelta /** distance radial delta   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
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

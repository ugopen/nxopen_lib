#ifndef NXOpen_MOTION_NORMALMODEPROPERTY_HXX_INCLUDED
#define NXOpen_MOTION_NORMALMODEPROPERTY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_NormalModeProperty.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class NormalModeProperty;
    }
    class NXObject;
    namespace Motion
    {
        class _NormalModePropertyBuilder;
        class NormalModePropertyImpl;
        /** Represents the properties of one normal mode */
        class NXOPENCPPEXPORT  NormalModeProperty : public NXObject
        {
            private: NormalModePropertyImpl * m_normalmodeproperty_impl;
            private: friend class  _NormalModePropertyBuilder;
            protected: NormalModeProperty();
            public: ~NormalModeProperty();
            /**Returns  the mode ID  <br> License requirements : mechanisms ("MECHANISMS") */
            public: int ModeId
            (
            );
            /**Returns  the natural frequency of the normal mode  <br> License requirements : mechanisms ("MECHANISMS") */
            public: double Frequency
            (
            );
            /**Returns  the stiffness of the normal mode  <br> License requirements : mechanisms ("MECHANISMS") */
            public: double Stiffness
            (
            );
            /**Returns  the mass of the normal mode  <br> License requirements : mechanisms ("MECHANISMS") */
            public: double Mass
            (
            );
            /**Returns  the percent mass of X direction component  <br> License requirements : mechanisms ("MECHANISMS") */
            public: double XMass
            (
            );
            /**Returns  the percent mass of Y direction component  <br> License requirements : mechanisms ("MECHANISMS") */
            public: double YMass
            (
            );
            /**Returns  the percent mass of Z direction component  <br> License requirements : mechanisms ("MECHANISMS") */
            public: double ZMass
            (
            );
            /**Returns  the percent mass of Rx direction component  <br> License requirements : mechanisms ("MECHANISMS") */
            public: double RxMass
            (
            );
            /**Returns  the percent mass of Ry direction component  <br> License requirements : mechanisms ("MECHANISMS") */
            public: double RyMass
            (
            );
            /**Returns  the percent mass of Rz direction component  <br> License requirements : mechanisms ("MECHANISMS") */
            public: double RzMass
            (
            );
            /**Returns  the viscous factor  <br> License requirements : mechanisms ("MECHANISMS") */
            public: double Viscous
            (
            );
            /**Sets  the viscous factor  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetViscous
            (
                double viscous /** viscous */ 
            );
            /**Returns  the hysteretic factor  <br> License requirements : mechanisms ("MECHANISMS") */
            public: double Hysteretic
            (
            );
            /**Sets  the hysteretic factor  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetHysteretic
            (
                double hysteretic /** hysteretic */ 
            );
            /**Returns  the activate status for each normal mode  <br> License requirements : mechanisms ("MECHANISMS") */
            public: bool Active
            (
            );
            /**Sets  the activate status for each normal mode  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetActive
            (
                bool active /** active */ 
            );
            /**Returns  the physical viscous factor  <br> License requirements : mechanisms ("MECHANISMS") */
            public: double PhysicalViscous
            (
            );
            /**Returns  the physical hysteretic factor  <br> License requirements : mechanisms ("MECHANISMS") */
            public: double PhysicalHysteretic
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif

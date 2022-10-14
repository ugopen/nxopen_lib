#ifndef NXOpen_MOTION_HYDRODYNAMICBEARINGBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_HYDRODYNAMICBEARINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_HydrodynamicBearingBuilder.ja
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
        class HydrodynamicBearingBuilder;
    }
    namespace Motion
    {
        class EntityPropTableBuilder;
    }
    namespace Motion
    {
        class _HydrodynamicBearingBuilderBuilder;
        class HydrodynamicBearingBuilderImpl;

        /// \cond NX_NO_DOC 
        /** Represents a @link Motion::HydrodynamicBearing Motion::HydrodynamicBearing@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Motion::HydrodynamicBearingCollection::CreateHydrodynamicBearingBuilder  NXOpen::Motion::HydrodynamicBearingCollection::CreateHydrodynamicBearingBuilder @endlink  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  HydrodynamicBearingBuilder : public NXOpen::Motion::EntityPropTableBuilder
        {
            /** Cavitation Algorithm */

            /// \cond NX_NO_DOC 
            public: enum CavitationAlgorithm
            {
                CavitationAlgorithmQuasiStatic/** Quasi Static */,
                CavitationAlgorithmMassConserving/** Mass Conserving */,
                CavitationAlgorithmUpdateMassConserving/** Update Mass Conserving */
            };


            /// \endcond 
            /** File Units Length */

            /// \cond NX_NO_DOC 
            public: enum Length
            {
                LengthMillimeter/** Millimeter */,
                LengthCentimeter/** Centimeter */,
                LengthMeter/** Meter */,
                LengthInch/** Inch */,
                LengthFeet/** Feet */
            };


            /// \endcond 
            /** File Units Force */

            /// \cond NX_NO_DOC 
            public: enum Force
            {
                ForceNewton/** Newton */,
                ForceMicronewton/** Micronewton */,
                ForceKilogramForce/** Kilogram Force */,
                ForcePound/** Pound */,
                ForceDyne/** Dyne */
            };


            /// \endcond 
            /** File Units Mass */

            /// \cond NX_NO_DOC 
            public: enum Mass
            {
                MassGram/** Gram */,
                MassKilogram/** Kilogram */,
                MassMetricTonne/** Metric Tonne */,
                MassSlinch/** Slinch */,
                MassSlug/** Slug */
            };


            /// \endcond 
            /** Viscosity type */

            /// \cond NX_NO_DOC 
            public: enum ViscosityType
            {
                ViscosityTypeExpression/** Expression */,
                ViscosityTypeProfile2D/** Profile 2D */,
                ViscosityTypeTemperatureDependent/** Temperature Dependent */
            };


            /// \endcond 
            /** Lubricant */

            /// \cond NX_NO_DOC 
            public: enum Lubricant
            {
                LubricantPredefined/** Predefined */,
                LubricantProfile2D/** Profile 2D */
            };


            /// \endcond 
            /** Lubricant type */

            /// \cond NX_NO_DOC 
            public: enum LubricantType
            {
                LubricantTypeSae5w30/** SAE 5W-30 */,
                LubricantTypeSae10w30/** SAE 10W-30 */,
                LubricantTypeSae10w40/** SAE 10W-40 */,
                LubricantTypeSae15w40/** SAE 15W-40 */,
                LubricantTypeSae20w50/** SAE 20W-50 */,
                LubricantTypeSae10w/** SAE 10W */,
                LubricantTypeSae20w/** SAE 20W */,
                LubricantTypeSae20/** SAE 20 */,
                LubricantTypeSae30/** SAE 30 */,
                LubricantTypeSae40/** SAE 40 */,
                LubricantTypeSae50/** SAE 50 */
            };


            /// \endcond 
            private: HydrodynamicBearingBuilderImpl * m_hydrodynamicbearingbuilder_impl;
            private: friend class  _HydrodynamicBearingBuilderBuilder;
            protected: HydrodynamicBearingBuilder();
            public: ~HydrodynamicBearingBuilder();
        };

        /// \endcond 
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
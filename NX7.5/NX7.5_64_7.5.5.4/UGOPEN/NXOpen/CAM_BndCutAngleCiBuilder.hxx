#ifndef NXOpen_CAM_BNDCUTANGLECIBUILDER_HXX_INCLUDED
#define NXOpen_CAM_BNDCUTANGLECIBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_BndCutAngleCiBuilder.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class BndCutAngleCiBuilder;
    }
    namespace CAM
    {
        class _BndCutAngleCiBuilderBuilder;
        class BndCutAngleCiBuilderImpl;
        /** Represents a boundary cut angle ci Builder 
         @deprecated Deprecated in NX7.5.0 <br> 
        */
        class NXOPENCPPEXPORT  NX_DEPRECATED("Deprecated in NX7.5.0")  BndCutAngleCiBuilder : public TaggedObject
        {
            /** Available types for cut angle type in boundary cut angle customizable item */
            public: enum CutAngleTypes
            {
                CutAngleTypesAuto/** Automatic */,
                CutAngleTypesSpecify/** User Defined */,
                CutAngleTypesLongestLine/** Longest Line */
            };

            private: BndCutAngleCiBuilderImpl * m_bndcutanglecibuilder_impl;
            private: friend class  _BndCutAngleCiBuilderBuilder;
            protected: BndCutAngleCiBuilder();
            public: ~BndCutAngleCiBuilder();
            /**Returns  the Cut angle Type 
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") NXOpen::CAM::BndCutAngleCiBuilder::CutAngleTypes CutAngleType
            (
            );
            /**Sets  the Cut angle Type 
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") void SetCutAngleType
            (
                NXOpen::CAM::BndCutAngleCiBuilder::CutAngleTypes cutAngType /** the Cut Angle Type */
            );
            /**Returns  the Cut angle value 
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") double CutAngleValue
            (
            );
            /**Sets  the Cut angle value 
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") void SetCutAngleValue
            (
                double cutAng /** the Cut Angle Value */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
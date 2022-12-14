#ifndef NXOpen_FEATURES_SHEETMETAL_LIGHTENINGCUTOUTBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_LIGHTENINGCUTOUTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_LighteningCutoutBuilder.ja
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
#include <NXOpen/Features_SheetMetal_BendOptions.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Section.hxx>
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
        namespace SheetMetal
        {
            class LighteningCutoutBuilder;
        }
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class BendOptions;
        }
    }
    namespace Features
    {
        class SketchFeature;
    }
    class Section;
    namespace Features
    {
        namespace SheetMetal
        {
            class _LighteningCutoutBuilderBuilder;
            class LighteningCutoutBuilderImpl;
            /** Represents a @link Features::SheetMetal::LighteningCutout Features::SheetMetal::LighteningCutout@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Features::SheetMetal::SheetmetalManager::CreateLighteningCutoutBuilder  NXOpen::Features::SheetMetal::SheetmetalManager::CreateLighteningCutoutBuilder @endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            Angle.Value </td> <td> 
             
            45 </td> </tr> 

            <tr><td> 
             
            CheckClearance </td> <td> 
             
            1 </td> </tr> 

            <tr><td> 
             
            Clearance.Value </td> <td> 
             
            5 (millimeters part), 0.12 (inches part) </td> </tr> 

            <tr><td> 
             
            Diameter.Value </td> <td> 
             
            102 (millimeters part), 2.6 (inches part) </td> </tr> 

            <tr><td> 
             
            DieRadius.Value </td> <td> 
             
            8 (millimeters part), 0.2 (inches part) </td> </tr> 

            <tr><td> 
             
            Length.Value </td> <td> 
             
            6 (millimeters part), 0.125 (inches part) </td> </tr> 

            <tr><td> 
             
            NeutralFactor.Value (deprecated) </td> <td> 
             
            0.33 </td> </tr> 

            <tr><td> 
             
            SectionCornerRadius.Value </td> <td> 
             
            8 (millimeters part), 0.2 (inches part) </td> </tr> 

            <tr><td> 
             
            Type </td> <td> 
             
            UserDefined </td> </tr> 

            </table>  

             <br>  Created in NX11.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  LighteningCutoutBuilder : public NXOpen::Features::FeatureBuilder
            {
                /** Represents the type of Lightening Cutout */
                public: enum CutoutType
                {
                    CutoutTypeHole/** hole */ ,
                    CutoutTypeUserDefined/** user defined */ 
                };

                private: LighteningCutoutBuilderImpl * m_lighteningcutoutbuilder_impl;
                private: friend class  _LighteningCutoutBuilderBuilder;
                protected: LighteningCutoutBuilder();
                public: ~LighteningCutoutBuilder();
                /**Returns  the type 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::SheetMetal::LighteningCutoutBuilder::CutoutType Type
                (
                );
                /**Sets  the type 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN") */
                public: void SetType
                (
                    NXOpen::Features::SheetMetal::LighteningCutoutBuilder::CutoutType type /** type */ 
                );
                /**Returns  the hole center when the type is @link NXOpen::Features::SheetMetal::LighteningCutoutBuilder::CutoutTypeHole NXOpen::Features::SheetMetal::LighteningCutoutBuilder::CutoutTypeHole@endlink  
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Section * HoleCenter
                (
                );
                /**Returns  the section when the type is @link NXOpen::Features::SheetMetal::LighteningCutoutBuilder::CutoutTypeUserDefined NXOpen::Features::SheetMetal::LighteningCutoutBuilder::CutoutTypeUserDefined@endlink  
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Section * UserDefinedSection
                (
                );
                /**Returns  the Sketch used by Lightening Cutout 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::SketchFeature * Sketch
                (
                );
                /**Returns  the diameter when the type is @link NXOpen::Features::SheetMetal::LighteningCutoutBuilder::CutoutTypeHole NXOpen::Features::SheetMetal::LighteningCutoutBuilder::CutoutTypeHole@endlink  
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Diameter
                (
                );
                /**Returns  the length 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Length
                (
                );
                /**Returns  whether the bend direction is reversed 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: bool ReverseBendDirection
                (
                );
                /**Sets  whether the bend direction is reversed 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN") */
                public: void SetReverseBendDirection
                (
                    bool reverseBendDirection /** reversebenddirection */ 
                );
                /**Returns  the angle 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Angle
                (
                );
                /**Returns  whether to check the clearance 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: bool CheckClearance
                (
                );
                /**Sets  whether to check the clearance 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN") */
                public: void SetCheckClearance
                (
                    bool checkClearance /** checkclearance */ 
                );
                /**Returns  the clearance 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Clearance
                (
                );
                /**Returns  the section corner radius 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * SectionCornerRadius
                (
                );
                /**Returns  the die radius 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * DieRadius
                (
                );
                /**Returns  the neutral factor 
                 <br>  @deprecated Deprecated in NX12.0.0.  Obtain the bend options object using @link NXOpen::Features::SheetMetal::LighteningCutoutBuilder::BendOptions NXOpen::Features::SheetMetal::LighteningCutoutBuilder::BendOptions@endlink  and from bend options, get Neutral Factor using @link NXOpen::Features::SheetMetal::BendOptions::NeutralFactor NXOpen::Features::SheetMetal::BendOptions::NeutralFactor@endlink  <br>  

                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NX_DEPRECATED("Deprecated in NX12.0.0.  Obtain the bend options object using NXOpen::Features::SheetMetal::LighteningCutoutBuilder::BendOptions and from bend options, get Neutral Factor using NXOpen::Features::SheetMetal::BendOptions::NeutralFactor") NXOpen::Expression * NeutralFactor
                (
                );
                /** Returns the standard names available for the material selected 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: std::vector<NXString> GetStandards
                (
                );
                /**Returns  the standard name selected 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString StandardName
                (
                );
                /**Sets  the standard name selected 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN") */
                public: void SetStandardName
                (
                    const NXString & standardName /** standardname */ 
                );
                /**Sets  the standard name selected 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN") */
                void SetStandardName
                (
                    const char * standardName /** standardname */ 
                );
                /**Returns  the bend options 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::SheetMetal::BendOptions * BendOptions
                (
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

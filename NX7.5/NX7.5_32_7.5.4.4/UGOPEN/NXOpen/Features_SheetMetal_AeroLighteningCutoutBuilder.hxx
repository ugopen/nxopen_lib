#ifndef NXOpen_FEATURES_SHEETMETAL_AEROLIGHTENINGCUTOUTBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_AEROLIGHTENINGCUTOUTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_AeroLighteningCutoutBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_SheetMetal_AeroLighteningCutoutBuilder.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        namespace SheetMetal
        {
            class AeroLighteningCutoutBuilder;
        }
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class Point;
    class Section;
    class SelectFace;
    namespace Features
    {
        namespace SheetMetal
        {
            class _AeroLighteningCutoutBuilderBuilder;
            class AeroLighteningCutoutBuilderImpl;
            /**
                Represents a @link Features::SheetMetal::AeroLighteningCutoutBuilder Features::SheetMetal::AeroLighteningCutoutBuilder@endlink  
                 <br> To create a new instance of this class, use @link Features::SheetMetal::AeroSheetmetalManager::CreateAeroLighteningCutoutBuilder Features::SheetMetal::AeroSheetmetalManager::CreateAeroLighteningCutoutBuilder@endlink  <br> 
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
             
            true </td> </tr> 

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
             
            8 (millimeters part), 0.2 (inches part) </td> </tr> 

            <tr><td> 
             
            Type </td> <td> 
             
            UserDefined </td> </tr> 

            </table>  
            */
            class NXOPENCPPEXPORT  AeroLighteningCutoutBuilder : public Features::FeatureBuilder
            {
                /**Represents the cutout type. */
                public: enum Types
                {
                    TypesHole/** hole */ ,
                    TypesUserDefined/** user defined */ 
                };

                private: AeroLighteningCutoutBuilderImpl * m_aerolighteningcutoutbuilder_impl;
                private: friend class  _AeroLighteningCutoutBuilderBuilder;
                protected: AeroLighteningCutoutBuilder();
                public: ~AeroLighteningCutoutBuilder();
                /**Returns  the feature type  <br> License requirements : None */
                public: NXOpen::Features::SheetMetal::AeroLighteningCutoutBuilder::Types Type
                (
                );
                /**Sets  the feature type  <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: void SetType
                (
                    NXOpen::Features::SheetMetal::AeroLighteningCutoutBuilder::Types type /** type */ 
                );
                /**Returns  the hole face  <br> License requirements : None */
                public: NXOpen::SelectFace * HoleFace
                (
                );
                /**Returns  the hole center  <br> License requirements : None */
                public: NXOpen::Point * HoleCenter
                (
                );
                /**Sets  the hole center  <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: void SetHoleCenter
                (
                    NXOpen::Point * holeCenter /** holecenter */ 
                );
                /**Returns  the cutout profile  <br> License requirements : None */
                public: NXOpen::Section * CutoutProfile
                (
                );
                /**Returns  the diameter  <br> License requirements : None */
                public: NXOpen::Expression * Diameter
                (
                );
                /**Returns  the length  <br> License requirements : None */
                public: NXOpen::Expression * Length
                (
                );
                /**Returns  the angle  <br> License requirements : None */
                public: NXOpen::Expression * Angle
                (
                );
                /**Returns  the reverse bend direction  <br> License requirements : None */
                public: bool ReverseBendDirection
                (
                );
                /**Sets  the reverse bend direction  <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: void SetReverseBendDirection
                (
                    bool reverseBendDirection /** reversebenddirection */ 
                );
                /**Returns  the die radius  <br> License requirements : None */
                public: NXOpen::Expression * DieRadius
                (
                );
                /**Returns  the corner radius  <br> License requirements : None */
                public: NXOpen::Expression * CornerRadius
                (
                );
                /**Returns  the clearance  <br> License requirements : None */
                public: NXOpen::Expression * Clearance
                (
                );
                /**Returns  the check clearance  <br> License requirements : None */
                public: bool CheckClearance
                (
                );
                /**Sets  the check clearance  <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: void SetCheckClearance
                (
                    bool checkClearance /** checkclearance */ 
                );
                /** Returns the standard names  @return   <br> License requirements : None */
                public: std::vector<NXString> GetStandards
                (
                );
                /**Returns  the standard name  <br> License requirements : None */
                public: NXString StandardName
                (
                );
                /**Sets  the standard name  <br> License requirements : aero_sheet_metal ("Aerospace Sheet Metal") */
                public: void SetStandardName
                (
                    const NXString & standardName /** standardname */ 
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif

#ifndef NXOpen_FEATURES_RESIZECHAMFERBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_RESIZECHAMFERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ResizeChamferBuilder.ja
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
#include <NXOpen/Features_ResizeChamferBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class ResizeChamferBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class ScCollector;
    namespace Features
    {
        class _ResizeChamferBuilderBuilder;
        class ResizeChamferBuilderImpl;
        /**
            Represents a @link Features::ResizeChamfer Features::ResizeChamfer@endlink  builder
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateResizeChamferBuilder Features::FeatureCollection::CreateResizeChamferBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Angle.Value </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ChamferType </td> <td> 
         
        SymmetricOffset </td> </tr> 

        <tr><td> 
         
        Offset1.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        Offset2.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  ResizeChamferBuilder : public Features::FeatureBuilder
        {
            /** the chamfer section types */
            public: enum SectionType
            {
                SectionTypeSymmetricOffset/** symmetric offset */ ,
                SectionTypeAsymmetricOffset/** asymmetric offset */ ,
                SectionTypeOffsetandAngle/** offsetand angle */ 
            };

            private: ResizeChamferBuilderImpl * m_resizechamferbuilder_impl;
            private: friend class  _ResizeChamferBuilderBuilder;
            protected: ResizeChamferBuilder();
            public: ~ResizeChamferBuilder();
            /**Returns  the faces  <br> License requirements : None */
            public: NXOpen::ScCollector * Faces
            (
            );
            /**Returns  the chamfer type  <br> License requirements : None */
            public: NXOpen::Features::ResizeChamferBuilder::SectionType ChamferType
            (
            );
            /**Sets  the chamfer type  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetChamferType
            (
                NXOpen::Features::ResizeChamferBuilder::SectionType chamferType /** chamfertype */ 
            );
            /**Returns  the offset1  <br> License requirements : None */
            public: NXOpen::Expression * Offset1
            (
            );
            /**Returns  the offset2  <br> License requirements : None */
            public: NXOpen::Expression * Offset2
            (
            );
            /**Returns  the angle  <br> License requirements : None */
            public: NXOpen::Expression * Angle
            (
            );
            /**Returns  the flip flag  <br> License requirements : None */
            public: bool FlipChamferOffsets
            (
            );
            /**Sets  the flip flag  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetFlipChamferOffsets
            (
                bool flipChamferOffsets /** flipchamferoffsets */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
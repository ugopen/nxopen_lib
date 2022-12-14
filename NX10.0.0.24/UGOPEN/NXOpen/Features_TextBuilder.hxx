#ifndef NXOpen_FEATURES_TEXTBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_TEXTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_TextBuilder.ja
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
#include <NXOpen/Features_TextBuilder.hxx>
#include <NXOpen/GeometricUtilities_FrameOnPathBuilder.hxx>
#include <NXOpen/GeometricUtilities_RectangularFrameBuilder.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
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
        class TextBuilder;
    }
    class Direction;
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class FrameOnPathBuilder;
    }
    namespace GeometricUtilities
    {
        class RectangularFrameBuilder;
    }
    class Plane;
    class ScCollector;
    class Section;
    namespace Features
    {
        class _TextBuilderBuilder;
        class TextBuilderImpl;
        /**
            Represents a @link NXOpen::Features::Text NXOpen::Features::Text@endlink  builder
             <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateTextBuilder  NXOpen::Features::FeatureCollection::CreateTextBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        CanCreateBoundingBox </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CanJoinCurves </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        CanProjectCurves </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CanReferenceText </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        CanUseKerningSpaces </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        FontStyle </td> <td> 
         
        Regular </td> </tr> 

        <tr><td> 
         
        FrameOnPath.AnchorLocation </td> <td> 
         
        Center </td> </tr> 

        <tr><td> 
         
        FrameOnPath.Height.Value </td> <td> 
         
        10 (millimeters part), 1 (inches part) </td> </tr> 

        <tr><td> 
         
        FrameOnPath.Offset.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        FrameOnPath.WScale </td> <td> 
         
        100 </td> </tr> 

        <tr><td> 
         
        IsAssociative </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        OnFacePlacementMethod </td> <td> 
         
        CurvesOnFaces </td> </tr> 

        <tr><td> 
         
        OrientationMethod </td> <td> 
         
        Natural </td> </tr> 

        <tr><td> 
         
        PlanarFrame.AnchorLocation </td> <td> 
         
        BottomCenter </td> </tr> 

        <tr><td> 
         
        PlanarFrame.Height.Value </td> <td> 
         
        10 (millimeters part), 1 (inches part) </td> </tr> 

        <tr><td> 
         
        PlanarFrame.Shear.Value </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        PlanarFrame.WScale </td> <td> 
         
        100 </td> </tr> 

        </table>  

         <br>  Created in NX7.5.1.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  TextBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** Text placement type */
            public: enum Types
            {
                TypesPlanar/** Placement on a plane */,
                TypesOnCurve/** Placement on a profile */,
                TypesOnFace/** Placement on faces */
            };

            /** The placement options for @link NXOpen::Features::TextBuilder::TypesOnFace NXOpen::Features::TextBuilder::TypesOnFace@endlink  type */
            public: enum OnFacePlacementMethodOptions
            {
                OnFacePlacementMethodOptionsCurvesOnFaces/** Placement on curves or edges on the faces */,
                OnFacePlacementMethodOptionsSectionPlane/** Placement on intersection curve created by a plane and the faces */
            };

            /** The orientation options for @link NXOpen::Features::TextBuilder::TypesOnCurve NXOpen::Features::TextBuilder::TypesOnCurve@endlink  type */
            public: enum OrientationMethodOptions
            {
                OrientationMethodOptionsNatural/** Orientation along natural curve normals */,
                OrientationMethodOptionsVector/** Orientation along a vector */
            };

            /** Script or character set options */
            public: enum ScriptOptions
            {
                ScriptOptionsOther/** Specifies a default character set based on current system locale */,
                ScriptOptionsWestern/** Specifies the English character set */,
                ScriptOptionsBaltic/** Specifies the Baltic (Northeastern European) character set */,
                ScriptOptionsChineseBig5/** Specifies the "traditional" Chinese character set */,
                ScriptOptionsCentralEuropean/** Specifies a Eastern European character set */,
                ScriptOptionsGb2312/** Specifies the "simplified" Chinese character set  */,
                ScriptOptionsGreek/** Specifies the Greek character set */,
                ScriptOptionsHangul/** Specifies the Hangul Korean character set */,
                ScriptOptionsMac/** Specifies the Apple Macintosh character set */,
                ScriptOptionsOem/** Specifies a mapping to one of the OEM code pages, according to the current system locale setting */,
                ScriptOptionsCyrillic/** Specifies the Russian Cyrillic character set */,
                ScriptOptionsShiftJIS/** Specifies the Japanese character set */,
                ScriptOptionsSymbol/** Specifies a character set of symbols */,
                ScriptOptionsTurkish/** Specifies the Turkish character set */,
                ScriptOptionsVietnamese/** Specifies the Vietnamese character set */,
                ScriptOptionsJohab/** Specifies the Johab Korean character set */,
                ScriptOptionsArabic/** Specifies the Arabic character set */,
                ScriptOptionsHebrew/** Specifies the Hebrew character set */,
                ScriptOptionsThai/** Specifies the Thai character set */
            };

            /** Font style options */
            public: enum FontStyleOptions
            {
                FontStyleOptionsRegular/** Regular style */,
                FontStyleOptionsItalic/** Italic style */,
                FontStyleOptionsBold/** Bold style */,
                FontStyleOptionsBoldItalic/** Bold italic style */
            };

            private: TextBuilderImpl * m_textbuilder_impl;
            private: friend class  _TextBuilderBuilder;
            protected: TextBuilder();
            public: ~TextBuilder();
            /**Returns  the placement profile for @link NXOpen::Features::TextBuilder::TypesOnCurve NXOpen::Features::TextBuilder::TypesOnCurve@endlink  type 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * OnCurvePlacementProfile
            (
            );
            /**Returns  the placement faces for @link NXOpen::Features::TextBuilder::TypesOnFace NXOpen::Features::TextBuilder::TypesOnFace@endlink  type 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * PlacementFaces
            (
            );
            /**Returns  the placement method for @link NXOpen::Features::TextBuilder::TypesOnFace NXOpen::Features::TextBuilder::TypesOnFace@endlink  type 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::TextBuilder::OnFacePlacementMethodOptions OnFacePlacementMethod
            (
            );
            /**Sets  the placement method for @link NXOpen::Features::TextBuilder::TypesOnFace NXOpen::Features::TextBuilder::TypesOnFace@endlink  type 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetOnFacePlacementMethod
            (
                NXOpen::Features::TextBuilder::OnFacePlacementMethodOptions placementMethod /** placementmethod */ 
            );
            /**Returns  the placement profile for @link NXOpen::Features::TextBuilder::TypesOnFace NXOpen::Features::TextBuilder::TypesOnFace@endlink  type 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * OnFacePlacementProfile
            (
            );
            /**Returns  the section plane for @link NXOpen::Features::TextBuilder::TypesOnFace NXOpen::Features::TextBuilder::TypesOnFace@endlink  type 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Plane * SectionPlane
            (
            );
            /**Sets  the section plane for @link NXOpen::Features::TextBuilder::TypesOnFace NXOpen::Features::TextBuilder::TypesOnFace@endlink  type 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetSectionPlane
            (
                NXOpen::Plane * sectionPlane /** sectionplane */ 
            );
            /**Returns  the flag indicating if intersection curve can be reversed 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: bool CanReverseIntersectionCurve
            (
            );
            /**Sets  the flag indicating if intersection curve can be reversed 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetCanReverseIntersectionCurve
            (
                bool canReverse /** canreverse */ 
            );
            /**Returns  the orientation method for @link NXOpen::Features::TextBuilder::TypesOnCurve NXOpen::Features::TextBuilder::TypesOnCurve@endlink  type 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::TextBuilder::OrientationMethodOptions OrientationMethod
            (
            );
            /**Sets  the orientation method for @link NXOpen::Features::TextBuilder::TypesOnCurve NXOpen::Features::TextBuilder::TypesOnCurve@endlink  type 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetOrientationMethod
            (
                NXOpen::Features::TextBuilder::OrientationMethodOptions orientationMethod /** orientationmethod */ 
            );
            /**Returns  the orientation vector 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * OrientationVector
            (
            );
            /**Sets  the orientation vector 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetOrientationVector
            (
                NXOpen::Direction * orientationVector /** orientationvector */ 
            );
            /**Returns  the string expression representing the text 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Text
            (
            );
            /**Returns  the flag indicating if text feature can reference a string expression 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: bool CanReferenceText
            (
            );
            /**Sets  the flag indicating if text feature can reference a string expression 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetCanReferenceText
            (
                bool canReferenceText /** canreferencetext */ 
            );
            /**Returns  the font 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXString Font
            (
            );
            /** Selects the font along with appropriate character set 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SelectFont
            (
                const NXString & fontName /** Font */,
                NXOpen::Features::TextBuilder::ScriptOptions script /** Character set */
            );
            /** Selects the font along with appropriate character set 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            void SelectFont
            (
                const char * fontName /** Font */,
                NXOpen::Features::TextBuilder::ScriptOptions script /** Character set */
            );
            /**Returns  the script 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::TextBuilder::ScriptOptions Script
            (
            );
            /**Sets  the script 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetScript
            (
                NXOpen::Features::TextBuilder::ScriptOptions script /** script */ 
            );
            /**Returns  the font style 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::TextBuilder::FontStyleOptions FontStyle
            (
            );
            /**Sets  the font style 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetFontStyle
            (
                NXOpen::Features::TextBuilder::FontStyleOptions fontStyle /** fontstyle */ 
            );
            /**Returns  the flag indicating if kerning spaces can be used 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: bool CanUseKerningSpaces
            (
            );
            /**Sets  the flag indicating if kerning spaces can be used 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetCanUseKerningSpaces
            (
                bool canUseKerningSpaces /** canusekerningspaces */ 
            );
            /**Returns  the flag indicating if bounding box can be created 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: bool CanCreateBoundingBox
            (
            );
            /**Sets  the flag indicating if bounding box can be created 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetCanCreateBoundingBox
            (
                bool canCreateBoundingBox /** cancreateboundingbox */ 
            );
            /**Returns  the planar frame 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::RectangularFrameBuilder * PlanarFrame
            (
            );
            /**Returns  the frame on path 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::FrameOnPathBuilder * FrameOnPath
            (
            );
            /**Returns  the flag indicating if operation is associative 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: bool IsAssociative
            (
            );
            /**Sets  the flag indicating if operation is associative 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAssociative
            (
                bool isAssociative /** isassociative */ 
            );
            /**Returns  the flag indicating if curves can be joined 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: bool CanJoinCurves
            (
            );
            /**Sets  the flag indicating if curves can be joined 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetCanJoinCurves
            (
                bool canJoinCurves /** canjoincurves */ 
            );
            /**Returns  the flag indicating if curves can be projected 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: bool CanProjectCurves
            (
            );
            /**Sets  the flag indicating if curves can be projected 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetCanProjectCurves
            (
                bool canProjectCurves /** canprojectcurves */ 
            );
            /**Returns  the type 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::TextBuilder::Types Type
            (
            );
            /**Sets  the type 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetType
            (
                NXOpen::Features::TextBuilder::Types type /** type */ 
            );
            /** Updates the builder based on section plane 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void UpdateOnSectionPlane
            (
            );
            /** Updates the builder based on orientation vector sense 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void UpdateOnOrientationVectorReversal
            (
            );
            /**Returns  the string to be rendered 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : None */
            public: NXString TextString
            (
            );
            /**Sets  the string to be rendered 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetTextString
            (
                const NXString & textString /** Text to be rendered */
            );
            /**Sets  the string to be rendered 
             <br>  Created in NX7.5.3.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            void SetTextString
            (
                const char * textString /** Text to be rendered */
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

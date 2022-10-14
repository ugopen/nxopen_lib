#ifndef NXOpen_WELD_FILLETBUILDER_HXX_INCLUDED
#define NXOpen_WELD_FILLETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_FilletBuilder.ja
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
#include <NXOpen/GeometricUtilities_OnPathDimensionBuilder.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/Weld_CharacteristicsBuilder.hxx>
#include <NXOpen/Weld_FilletBuilder.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_weld_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Weld
    {
        class FilletBuilder;
    }
    class Expression;
    class Face;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class OnPathDimensionBuilder;
    }
    class NXObject;
    class ScCollector;
    class Section;
    namespace Weld
    {
        class CharacteristicsBuilder;
    }
    namespace Weld
    {
        class _FilletBuilderBuilder;
        class FilletBuilderImpl;
        /** Represents a @link NXOpen::Weld::Fillet NXOpen::Weld::Fillet@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Weld::WeldManager::CreateFilletBuilder  NXOpen::Weld::WeldManager::CreateFilletBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        AddCosmeticEnd </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        AllowBroken </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        AssignWeldPMI </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        Associative </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        ContourHeight.Value </td> <td> 
         
        1.875 (millimeters part), .073818 (inches part) </td> </tr> 

        <tr><td> 
         
        ContourType </td> <td> 
         
        None </td> </tr> 

        <tr><td> 
         
        EnumMethod </td> <td> 
         
        NumberLength </td> </tr> 

        <tr><td> 
         
        ExtendEdges </td> <td> 
         
        Manual </td> </tr> 

        <tr><td> 
         
        ExtensionDistance.Value </td> <td> 
         
        0.0254 (millimeters part), 0.001 (inches part) </td> </tr> 

        <tr><td> 
         
        ExtensionMethod </td> <td> 
         
        Automatic </td> </tr> 

        <tr><td> 
         
        FaceFillGapDistance </td> <td> 
         
        0.0 (millimeters part), 0.0 (inches part) </td> </tr> 

        <tr><td> 
         
        FieldWeld </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FilletType </td> <td> 
         
        T </td> </tr> 

        <tr><td> 
         
        FirstLeg.Value </td> <td> 
         
        6.25 (millimeters part), .246062 (inches part) </td> </tr> 

        <tr><td> 
         
        NumberOfWelds.Value </td> <td> 
         
        3 </td> </tr> 

        <tr><td> 
         
        SecondLeg.Value </td> <td> 
         
        6.25 (millimeters part), .246062 (inches part) </td> </tr> 

        <tr><td> 
         
        SegmentLength.Value </td> <td> 
         
        3 (millimeters part), .118110 (inches part) </td> </tr> 

        <tr><td> 
         
        Spacing.Value </td> <td> 
         
        3 (millimeters part), .118110 (inches part) </td> </tr> 

        <tr><td> 
         
        ThroatThickToggle </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ToggleCreateSkipWelds </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ToggleRecreateDeletedWelds </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_WELDEXPORT  FilletBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** the options for populating the edge selections. */
            public: enum EnumExtendEdges
            {
                EnumExtendEdgesManual/** manual */ ,
                EnumExtendEdgesAutomatic/** automatic */ 
            };

            /** the options for which construction method to use. */
            public: enum EnumConstructionMethod
            {
                EnumConstructionMethodDefault/** default */ ,
                EnumConstructionMethodRollAround/** roll around */ 
            };

            /** the Extension enum. */
            public: enum EnumExtensionMethod
            {
                EnumExtensionMethodAutomatic/** automatic */ ,
                EnumExtensionMethodByValue/** by value */ 
            };

            /** the Contour enum. */
            public: enum EnumContour
            {
                EnumContourNone/** none */ ,
                EnumContourConvex/** convex */ ,
                EnumContourFlush/** flush */ ,
                EnumContourConcave/** concave */ 
            };

            /** the Skipweld enum. */
            public: enum EnumSkipWeldMethod
            {
                EnumSkipWeldMethodNumberLength/** number length */ ,
                EnumSkipWeldMethodNumberSpacing/** number spacing */ ,
                EnumSkipWeldMethodSpacingLength/** spacing length */ 
            };

            /** the WeldingType enum. */
            public: enum EnumWeldingType
            {
                EnumWeldingTypeT/** t */ ,
                EnumWeldingTypeLap/** lap */ ,
                EnumWeldingTypeCorner/** corner */ 
            };

            private: FilletBuilderImpl * m_filletbuilder_impl;
            private: friend class  _FilletBuilderBuilder;
            protected: FilletBuilder();
            public: ~FilletBuilder();
            /**Returns  the value for how to populate the edge sets. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::FilletBuilder::EnumExtendEdges ExtendEdges
            (
            );
            /**Sets  the value for how to populate the edge sets. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetExtendEdges
            (
                NXOpen::Weld::FilletBuilder::EnumExtendEdges extendEdges /** extendedges */ 
            );
            /**Returns  the value for determining the construction method. Default method should be used for all conditions, unless you know the situation if for the roll around condition. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::FilletBuilder::EnumConstructionMethod ConstructionMethod
            (
            );
            /**Sets  the value for determining the construction method. Default method should be used for all conditions, unless you know the situation if for the roll around condition. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetConstructionMethod
            (
                NXOpen::Weld::FilletBuilder::EnumConstructionMethod constructionMethod /** constructionmethod */ 
            );
            /**Returns  the face set1. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * FaceSet1
            (
            );
            /**Returns  the face set2. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * FaceSet2
            (
            );
            /**Returns  the face normal direction. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool DirectionVector1
            (
            );
            /**Sets  the face normal direction. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetDirectionVector1
            (
                bool directionVector1 /** directionvector1 */ 
            );
            /**Returns  the face normal direction for the second face. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool DirectionVector2
            (
            );
            /**Sets  the face normal direction for the second face. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetDirectionVector2
            (
                bool directionVector2 /** directionvector2 */ 
            );
            /**Returns  the edge set1. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * EdgeSet1
            (
            );
            /**Returns  the edge set2. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * EdgeSet2
            (
            );
            /**Returns  the extension method. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::FilletBuilder::EnumExtensionMethod ExtensionMethod
            (
            );
            /**Sets  the extension method. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetExtensionMethod
            (
                NXOpen::Weld::FilletBuilder::EnumExtensionMethod extensionMethod /** extensionmethod */ 
            );
            /**Returns  the linear dimension extension distance. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ExtensionDistance
            (
            );
            /**Returns  the contour. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::FilletBuilder::EnumContour ContourType
            (
            );
            /**Sets  the contour. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetContourType
            (
                NXOpen::Weld::FilletBuilder::EnumContour contour /** contour */ 
            );
            /**Returns  the toggle throat thickness. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool ThroatThickToggle
            (
            );
            /**Sets  the toggle throat thickness. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetThroatThickToggle
            (
                bool throatThickToggle /** throatthicktoggle */ 
            );
            /**Returns  the linear dimension first leg. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * FirstLeg
            (
            );
            /**Returns  the linear dimension second leg. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * SecondLeg
            (
            );
            /**Returns  the linear dimension contour height. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ContourHeight
            (
            );
            /**Returns  the on path dimension start distance. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::OnPathDimensionBuilder * StartDist
            (
            );
            /**Returns  the on path dimension end distance. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::OnPathDimensionBuilder * EndDist
            (
            );
            /**Returns  the start direction reversed or not. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool StartVector
            (
            );
            /**Sets  the start direction reversed or not. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetStartVector
            (
                bool startVector /** startvector */ 
            );
            /**Returns  the end direction reversed or not. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool EndVector
            (
            );
            /**Sets  the end direction reversed or not. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetEndVector
            (
                bool endVector /** endvector */ 
            );
            /**Returns  the toggle to change direction. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool DirectToggle
            (
            );
            /**Sets  the toggle to change direction. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetDirectToggle
            (
                bool directToggle /** directtoggle */ 
            );
            /**Returns  the toggle to create skip welds. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool ToggleCreateSkipWelds
            (
            );
            /**Sets  the toggle to create skip welds. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetToggleCreateSkipWelds
            (
                bool toggleCreateSkipWelds /** togglecreateskipwelds */ 
            );
            /**Returns  the toggle to recreate deleted welds. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool ToggleRecreateDeletedWelds
            (
            );
            /**Sets  the toggle to recreate deleted welds. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetToggleRecreateDeletedWelds
            (
                bool toggleRecreateDeletedWelds /** togglerecreatedeletedwelds */ 
            );
            /**Returns  the enum method for skip welds. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::FilletBuilder::EnumSkipWeldMethod EnumMethod
            (
            );
            /**Sets  the enum method for skip welds. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetEnumMethod
            (
                NXOpen::Weld::FilletBuilder::EnumSkipWeldMethod enumMethod /** enummethod */ 
            );
            /**Returns  the expression number indicates number of welds in skip welds. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * NumberOfWelds
            (
            );
            /**Returns  the linear dimension length indicates segment length for each weld. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * SegmentLength
            (
            );
            /**Returns  the linear dimension spacing indicates distance between each weld. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Spacing
            (
            );
            /**Returns  the fillet type. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::FilletBuilder::EnumWeldingType FilletType
            (
            );
            /**Sets  the fillet type. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetFilletType
            (
                NXOpen::Weld::FilletBuilder::EnumWeldingType filletType /** fillettype */ 
            );
            /**Returns  the field weld. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool FieldWeld
            (
            );
            /**Sets  the field weld. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetFieldWeld
            (
                bool fieldWeld /** fieldweld */ 
            );
            /**Returns  the welding characteristics. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::CharacteristicsBuilder * WeldingCharacteristics
            (
            );
            /**Returns  the value identify if WAVE links should remain unbroken. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool Associative
            (
            );
            /**Sets  the value identify if WAVE links should remain unbroken. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetAssociative
            (
                bool associative /** associative */ 
            );
            /**Returns  the toggle to allow broken link. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool AllowBroken
            (
            );
            /**Sets  the toggle to allow broken link. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetAllowBroken
            (
                bool allowBroken /** allowbroken */ 
            );
            /**Returns  the value identify if a cosmtic end should be added to each end of the fillet. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool AddCosmeticEnd
            (
            );
            /**Sets  the value identify if a cosmtic end should be added to each end of the fillet. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetAddCosmeticEnd
            (
                bool addCosmeticEnd /** addcosmeticend */ 
            );
            /**Returns  the distance tolerance. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double DistTolerance
            (
            );
            /**Sets  the distance tolerance. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetDistTolerance
            (
                double distTolerance /** disttolerance */ 
            );
            /**Returns  the toggle to assign weld pmi. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool AssignWeldPMI
            (
            );
            /**Sets  the toggle to assign weld pmi. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetAssignWeldPMI
            (
                bool assignWeldPMI /** assignweldpmi */ 
            );
            /**Returns  the first seed face. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Face * SeedFace1
            (
            );
            /**Sets  the first seed face. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetSeedFace1
            (
                NXOpen::Face * seedFace1 /** seedface1 */ 
            );
            /**Returns  the point on the first face. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point3d SeedPoint1
            (
            );
            /**Sets  the point on the first face. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetSeedPoint1
            (
                const NXOpen::Point3d & seedPoint1 /** seedpoint1 */ 
            );
            /**Returns  the second seed face. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Face * SeedFace2
            (
            );
            /**Sets  the second seed face. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetSeedFace2
            (
                NXOpen::Face * seedFace2 /** seedface2 */ 
            );
            /**Returns  the point on the second face. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point3d SeedPoint2
            (
            );
            /**Sets  the point on the second face. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetSeedPoint2
            (
                const NXOpen::Point3d & seedPoint1 /** seedpoint1 */ 
            );
            /**Returns  the u parameter for first face. 
             <br>  @deprecated Deprecated in NX10.0.0.  Removed with no replacement. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Removed with no replacement.") double Uparameter1
            (
            );
            /**Sets  the u parameter for first face. 
             <br>  @deprecated Deprecated in NX10.0.0.  Removed with no replacement. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Removed with no replacement.") void SetUparameter1
            (
                double u1 /** u1 */ 
            );
            /**Returns  the v parameter for first face. 
             <br>  @deprecated Deprecated in NX10.0.0.  Removed with no replacement. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Removed with no replacement.") double Vparameter1
            (
            );
            /**Sets  the v parameter for first face. 
             <br>  @deprecated Deprecated in NX10.0.0.  Removed with no replacement. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Removed with no replacement.") void SetVparameter1
            (
                double v1 /** v1 */ 
            );
            /**Returns  the u parameter for second face. 
             <br>  @deprecated Deprecated in NX10.0.0.  Removed with no replacement. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Removed with no replacement.") double Uparameter2
            (
            );
            /**Sets  the u parameter for second face. 
             <br>  @deprecated Deprecated in NX10.0.0.  Removed with no replacement. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Removed with no replacement.") void SetUparameter2
            (
                double u2 /** u2 */ 
            );
            /**Returns  the v parameter for second face. 
             <br>  @deprecated Deprecated in NX10.0.0.  Removed with no replacement. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Removed with no replacement.") double Vparameter2
            (
            );
            /**Sets  the v parameter for second face. 
             <br>  @deprecated Deprecated in NX10.0.0.  Removed with no replacement. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Removed with no replacement.") void SetVparameter2
            (
                double v2 /** v2 */ 
            );
            /**Returns  the pmi symbol. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXObject * Pmi
            (
            );
            /**Sets  the pmi symbol. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetPmi
            (
                NXOpen::NXObject * pmi /** pmi */ 
            );
            /**Returns  the distance the fillet will span when there are gaps in the sheet definition. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double FaceFillGapDistance
            (
            );
            /**Sets  the distance the fillet will span when there are gaps in the sheet definition. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: void SetFaceFillGapDistance
            (
                double faceFillGapDistance /** facefillgapdistance */ 
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
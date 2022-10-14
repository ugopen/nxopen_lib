#ifndef NXOpen_TOOLING_SPECIALPIERCINGINSERTBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_SPECIALPIERCINGINSERTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_SpecialPiercingInsertBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_tooling_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Tooling
    {
        class SpecialPiercingInsertBuilder;
    }
    class Builder;
    class Curve;
    class Direction;
    class Edge;
    class Expression;
    class Face;
    class NXObject;
    class Part;
    class Section;
    class SelectEdgeList;
    class SelectFaceList;
    class SelectNXObjectList;
    namespace Tooling
    {
        class _SpecialPiercingInsertBuilderBuilder;
        class SpecialPiercingInsertBuilderImpl;
        /** Creates special piercing insert for progressive die.No entity is returned.  <br> To create a new instance of this class, use @link NXOpen::Tooling::ProgressiveDieManager::CreateSpecialPiercingInsertBuilder  NXOpen::Tooling::ProgressiveDieManager::CreateSpecialPiercingInsertBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        BoundBox </term> <description> 
         
        BoundedBlock </description> </item> 

        <item><term> 
         
        EndLimit.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        InsertPosition </term> <description> 
         
        Bottom </description> </item> 

        <item><term> 
         
        NormalBbpslug </term> <description> 
         
        Fillet </description> </item> 

        <item><term> 
         
        NormalCavity </term> <description> 
         
        TaperAngle </description> </item> 

        <item><term> 
         
        NormalClearance </term> <description> 
         
        0.05 </description> </item> 

        <item><term> 
         
        NormalDsslug </term> <description> 
         
        Fillet </description> </item> 

        <item><term> 
         
        NormalOffsetSide </term> <description> 
         
        DieSide </description> </item> 

        <item><term> 
         
        NormalSlugPara1 </term> <description> 
         
        3 </description> </item> 

        <item><term> 
         
        NormalSlugPara2 </term> <description> 
         
        -3 </description> </item> 

        <item><term> 
         
        NormalSlugPara3 </term> <description> 
         
        2 </description> </item> 

        <item><term> 
         
        NormalSlugPara4 </term> <description> 
         
        3 </description> </item> 

        <item><term> 
         
        OffsetLinearDimension.Value </term> <description> 
         
        3 (millimeters part), 0.12 (inches part) </description> </item> 

        <item><term> 
         
        ParentPart </term> <description> 
         
        ProjectDie </description> </item> 

        <item><term> 
         
        PlateClearanceFirst </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        PlateClearanceFourth </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        PlateClearanceSecond </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        PlateClearanceThird </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        PunchOrDie </term> <description> 
         
        Punch </description> </item> 

        <item><term> 
         
        RenameComponent </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        SlugHoleHeightLinearDimension.Value </term> <description> 
         
        100 (millimeters part), 4 (inches part) </description> </item> 

        <item><term> 
         
        StandardOrUserDefined </term> <description> 
         
        Standard </description> </item> 

        <item><term> 
         
        StartLimit.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        UsePlateClearanceFirst </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        UsePlateClearanceFourth </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        UsePlateClearanceSecond </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        UsePlateClearanceThird </term> <description> 
         
        0 </description> </item> 

        </list> 

         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  SpecialPiercingInsertBuilder : public NXOpen::Builder
        {
            /** Specifies the parent part type. */
            public: enum Types
            {
                TypesCreate/** create */ ,
                TypesEdit/** edit */ ,
                TypesDelete/** delete */ 
            };

            /** Specifies the parent part type. */
            public: enum ParentPartTypes
            {
                ParentPartTypesProjectDie/** project die */ ,
                ParentPartTypesProjectDieBase/** project die base */ ,
                ParentPartTypesProjectSubDieBase/** project sub die base */ 
            };

            /** Specifies the position of piercing inserts, for EDW only */
            public: enum InsertPositionTypes
            {
                InsertPositionTypesTop/** The position is top side */,
                InsertPositionTypesBottom/** The position is bottom side  */
            };

            /** Specifies the parent part type. */
            public: enum PunchOrDieTypes
            {
                PunchOrDieTypesPunch/** punch */ ,
                PunchOrDieTypesDie/** die */ ,
                PunchOrDieTypesDieCavityAndSlugHole/** die cavity and slug hole */ 
            };

            /** Specifies the parent part type. */
            public: enum StandardOrUserDefinedTypes
            {
                StandardOrUserDefinedTypesStandard/** standard */ ,
                StandardOrUserDefinedTypesUserDefined/** user defined */ 
            };

            /** Specifies the bounded box type block or cylinder. */
            public: enum BoundBoxType
            {
                BoundBoxTypeBoundedBlock/** bounded block */ ,
                BoundBoxTypeBoundedCylinder/** bounded cylinder */ 
            };

            /** Specifies the type of cavity. */
            public: enum NormalCavityType
            {
                NormalCavityTypeTaperAngle/** the taper angle type */,
                NormalCavityTypeStep/**        the step type */
            };

            /** Specifies the type of bottom plate slug. */
            public: enum NormalBottomBackingPlateSlugType
            {
                NormalBottomBackingPlateSlugTypeFillet/** Bottom backing plate slug type is fillet */,
                NormalBottomBackingPlateSlugTypeRectangle/** Bottom backing plate slug type is rectangle */,
                NormalBottomBackingPlateSlugTypeCircle/** Bottom backing plate slug type is circle */,
                NormalBottomBackingPlateSlugTypeMickey/** Bottom backing plate slug type is mickey */,
                NormalBottomBackingPlateSlugTypeClearance/** Bottom backing plate slug type is clearance */,
                NormalBottomBackingPlateSlugTypeSlotVer/** Bottom backing plate slug type is slot vertical */,
                NormalBottomBackingPlateSlugTypeSlotHor/** Bottom backing plate slug type is slot horizontal */,
                NormalBottomBackingPlateSlugTypeNone/** Bottom backing plate slug type is none */
            };

            /** Specifies the type of die shoe slug. */
            public: enum NormalDieShoeSlugType
            {
                NormalDieShoeSlugTypeFillet/** Die shoe slug type is fillet */,
                NormalDieShoeSlugTypeRectangle/** Die shoe slug type is rectangle */,
                NormalDieShoeSlugTypeCircle/** Die shoe slug type is circle */,
                NormalDieShoeSlugTypeMickey/** Die shoe slug type is mickey */,
                NormalDieShoeSlugTypeClearance/** Die shoe slug type is clearance */,
                NormalDieShoeSlugTypeSlotVer/** Die shoe slug type is slot vertical */,
                NormalDieShoeSlugTypeSlotHor/** Die shoe slug type is slot horizontal */,
                NormalDieShoeSlugTypeNone/** Die shoe slug type is none */
            };

            /** Specifies the offset side of normal pierce insert design. */
            public: enum NormalOffsetSideType
            {
                NormalOffsetSideTypePunchSide/** The offset side is punch */,
                NormalOffsetSideTypeDieSide/** The offset side is die */
            };

            private: SpecialPiercingInsertBuilderImpl * m_specialpiercinginsertbuilder_impl;
            private: friend class  _SpecialPiercingInsertBuilderBuilder;
            protected: SpecialPiercingInsertBuilder();
            public: ~SpecialPiercingInsertBuilder();
            /**Returns  the select face 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectFaceList * SelectFace
            (
            );
            /**Returns  the offset value linear dimension positive x 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OffsetValueLinearDimensionPositiveX
            (
            );
            /**Returns  the offset value linear dimension negative x 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OffsetValueLinearDimensionNegativeX
            (
            );
            /**Returns  the offset value linear dimension positive y 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OffsetValueLinearDimensionPositiveY
            (
            );
            /**Returns  the offset value linear dimension negative y 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OffsetValueLinearDimensionNegativeY
            (
            );
            /**Returns  the offset value linear dimension positive z 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OffsetValueLinearDimensionPositiveZ
            (
            );
            /**Returns  the offset value linear dimension negative z 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OffsetValueLinearDimensionNegativeZ
            (
            );
            /**Returns  the radial offset value for cylinder box
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RadialOffset
            (
            );
            /**Returns  the select curve 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectEdgeList * SelectEdges
            (
            );
            /**Returns  the select vector 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * SelectVector
            (
            );
            /**Sets  the select vector 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetSelectVector
            (
                NXOpen::Direction * selectVector /** selectvector */ 
            );
            /**Returns  the parent part 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::SpecialPiercingInsertBuilder::ParentPartTypes ParentPart
            (
            );
            /**Sets  the parent part 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetParentPart
            (
                NXOpen::Tooling::SpecialPiercingInsertBuilder::ParentPartTypes parentPart /** parentpart */ 
            );
            /**Returns  the punch or die 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::SpecialPiercingInsertBuilder::PunchOrDieTypes PunchOrDie
            (
            );
            /**Sets  the punch or die 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetPunchOrDie
            (
                NXOpen::Tooling::SpecialPiercingInsertBuilder::PunchOrDieTypes punchOrDie /** punchordie */ 
            );
            /**Returns  the standard or user defined 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::SpecialPiercingInsertBuilder::StandardOrUserDefinedTypes StandardOrUserDefined
            (
            );
            /**Sets  the standard or user defined 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetStandardOrUserDefined
            (
                NXOpen::Tooling::SpecialPiercingInsertBuilder::StandardOrUserDefinedTypes standardOrUserDefined /** standardoruserdefined */ 
            );
            /**Returns  the block or cylinder 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::SpecialPiercingInsertBuilder::BoundBoxType BoundBox
            (
            );
            /**Sets  the block or cylinder 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetBoundBox
            (
                NXOpen::Tooling::SpecialPiercingInsertBuilder::BoundBoxType boundBoxType /** boundboxtype */ 
            );
            /** The create datum plane 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void CreateDatumPlane
            (
            );
            /**Returns  the select curves 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * SelectCurves
            (
            );
            /**Returns  the select insert 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * SelectInsert
            (
            );
            /**Returns  the start limit 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * StartLimit
            (
            );
            /**Returns  the end limit 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * EndLimit
            (
            );
            /**Returns  the use plate clearance first 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool UsePlateClearanceFirst
            (
            );
            /**Sets  the use plate clearance first 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetUsePlateClearanceFirst
            (
                bool usePlateClearanceFirst /** useplateclearancefirst */ 
            );
            /**Returns  the plate clearance first 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: double PlateClearanceFirst
            (
            );
            /**Sets  the plate clearance first 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetPlateClearanceFirst
            (
                double plateClearanceFirst /** plateclearancefirst */ 
            );
            /**Returns  the use plate clearance second 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool UsePlateClearanceSecond
            (
            );
            /**Sets  the use plate clearance second 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetUsePlateClearanceSecond
            (
                bool usePlateClearanceSecond /** useplateclearancesecond */ 
            );
            /**Returns  the plate clearance second 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: double PlateClearanceSecond
            (
            );
            /**Sets  the plate clearance second 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetPlateClearanceSecond
            (
                double plateClearanceSecond /** plateclearancesecond */ 
            );
            /**Returns  the use plate clearance third 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool UsePlateClearanceThird
            (
            );
            /**Sets  the use plate clearance third 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetUsePlateClearanceThird
            (
                bool usePlateClearanceThird /** useplateclearancethird */ 
            );
            /**Returns  the plate clearance third 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: double PlateClearanceThird
            (
            );
            /**Sets  the plate clearance third 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetPlateClearanceThird
            (
                double plateClearanceThird /** plateclearancethird */ 
            );
            /**Returns  the use plate clearance fourth 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool UsePlateClearanceFourth
            (
            );
            /**Sets  the use plate clearance fourth 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetUsePlateClearanceFourth
            (
                bool usePlateClearanceFourth /** useplateclearancefourth */ 
            );
            /**Returns  the plate clearance fourth 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: double PlateClearanceFourth
            (
            );
            /**Sets  the plate clearance fourth 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetPlateClearanceFourth
            (
                double plateClearanceFourth /** plateclearancefourth */ 
            );
            /**Returns  the cavity type for normal pierce design. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::SpecialPiercingInsertBuilder::NormalCavityType NormalCavity
            (
            );
            /**Sets  the cavity type for normal pierce design. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetNormalCavity
            (
                NXOpen::Tooling::SpecialPiercingInsertBuilder::NormalCavityType normalCavity /** Indicates the cavity type for normal pierce design */
            );
            /**Returns  the H value of slug hole for normal pierce design. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: double NormalSlugPara1
            (
            );
            /**Sets  the H value of slug hole for normal pierce design. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetNormalSlugPara1
            (
                double normalSlugPara1 /** Indicates the H value of slug hole for normal pierce design */
            );
            /**Returns  the A value of slug hole for normal pierce design. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: double NormalSlugPara2
            (
            );
            /**Sets  the A value of slug hole for normal pierce design. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetNormalSlugPara2
            (
                double normalSlugPara2 /** Indicates A value of slug hole for normal pierce design */
            );
            /**Returns  the C1 value of slug hole for normal pierce design. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: double NormalSlugPara3
            (
            );
            /**Sets  the C1 value of slug hole for normal pierce design. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetNormalSlugPara3
            (
                double normalSlugPara3 /** Indicates C1 value of slug hole for normal pierce design */
            );
            /**Returns  the C2 value of slug hole for normal pierce design. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: double NormalSlugPara4
            (
            );
            /**Sets  the C2 value of slug hole for normal pierce design. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetNormalSlugPara4
            (
                double normalSlugPara4 /** Indicates the C2 value of slug hole for normal pierce design */
            );
            /**Returns  the slug hole height linear dimension 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * SlugHoleHeightLinearDimension
            (
            );
            /**Returns  the offset linear dimension 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OffsetLinearDimension
            (
            );
            /**Returns  the bottom plate slug type for normal pierce design. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::SpecialPiercingInsertBuilder::NormalBottomBackingPlateSlugType NormalBbpslug
            (
            );
            /**Sets  the bottom plate slug type for normal pierce design. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetNormalBbpslug
            (
                NXOpen::Tooling::SpecialPiercingInsertBuilder::NormalBottomBackingPlateSlugType normalBbpslug /** Indicates bottom plate slug type for normal pierce design */
            );
            /**Returns  the die shoe slug type for normal pierce design. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::SpecialPiercingInsertBuilder::NormalDieShoeSlugType NormalDsslug
            (
            );
            /**Sets  the die shoe slug type for normal pierce design. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetNormalDsslug
            (
                NXOpen::Tooling::SpecialPiercingInsertBuilder::NormalDieShoeSlugType normalDsslug /** Indicates die shoe slug type for normal pierce design */
            );
            /**Returns  the clearance value for normal pierce design. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: double NormalClearance
            (
            );
            /**Sets  the clearance value for normal pierce design. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetNormalClearance
            (
                double normalClearance /** Indicates the clearance value for normal pierce design */
            );
            /**Returns  the offset side option for normal pierce design. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::SpecialPiercingInsertBuilder::NormalOffsetSideType NormalOffsetSide
            (
            );
            /**Sets  the offset side option for normal pierce design. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetNormalOffsetSide
            (
                NXOpen::Tooling::SpecialPiercingInsertBuilder::NormalOffsetSideType normalOffsetSide /** Indicates the offset side option for normal pierce design */
            );
            /**Returns  the rename component 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool RenameComponent
            (
            );
            /**Sets  the rename component 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetRenameComponent
            (
                bool renameComponent /** renamecomponent */ 
            );
            /**Returns  the type 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::SpecialPiercingInsertBuilder::Types Type
            (
            );
            /**Sets  the type 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetType
            (
                NXOpen::Tooling::SpecialPiercingInsertBuilder::Types type /** type */ 
            );
            /**Returns  the wizard type 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: int WizardType
            (
            );
            /**Sets  the wizard type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetWizardType
            (
                int wizardType /** wizardtype */ 
            );
            /** Set work coordinate system for special piercing insert 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetWCSForSpecialPiercingInsert
            (
                bool needPrecisionValue /** needprecisionvalue */ 
            );
            /** Wave faces of selected curves 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void WaveFacesOfSelectedCurves
            (
                NXOpen::Part * rootPart /** rootpart */ ,
                NXOpen::NXObject * instanceTag /** instancetag */ 
            );
            /** Wave selected curves 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void WaveSelectedCurves
            (
            );
            /** Get wave linked curves 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void GetWaveLinkedCurves
            (
                std::vector<NXOpen::Curve *> & linkedCurves /** linkedcurves */ 
            );
            /** Create offset datum plane 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void CreateOffsetDatumPlane
            (
            );
            /** Get profiles 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void GetProfile
            (
                NXOpen::Section * sectionTag /** sectiontag */ ,
                std::vector<NXOpen::Curve *> & profiles /** profiles */ 
            );
            /** Get correct edge in new part 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::Edge * GetCorrectEdgeInNewPart
            (
                NXOpen::Part * partTag /** parttag */ ,
                NXOpen::Edge * sourceEdge /** sourceedge */ 
            );
            /** Wave faces and fill hole 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void WaveFacesAndFillHole
            (
                NXOpen::Part * rootPart /** rootpart */ ,
                NXOpen::NXObject * instanceTag /** instancetag */ 
            );
            /**Returns  the result whether the curves is three dimensional 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool Is3DCurves
            (
            );
            /**Sets  the result whether the curves is three dimensional 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetIs3DCurves
            (
                bool is3DCurves /** is3dcurves */ 
            );
            /** Get correct faces of extrac region feature. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void GetCorrectFacesOfExtractRegionFeature
            (
                std::vector<NXOpen::Face *> & faces /** faces */ 
            );
            /**Returns  the parent part name to create insert. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString ParentPartName
            (
            );
            /**Sets  the parent part name to create insert. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetParentPartName
            (
                const NXString & parentPart /** Specifies the parent part name */
            );
            /**Sets  the parent part name to create insert. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            void SetParentPartName
            (
                const char * parentPart /** Specifies the parent part name */
            );
            /**Returns  the reverse direction 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::SpecialPiercingInsertBuilder::InsertPositionTypes InsertPosition
            (
            );
            /**Sets  the reverse direction 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetInsertPosition
            (
                NXOpen::Tooling::SpecialPiercingInsertBuilder::InsertPositionTypes insertPosition /** insertposition */ 
            );
            /**Returns  the position of csys for box. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point3d BoxPosition
            (
            );
            /**Sets  the position of csys for box. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetBoxPosition
            (
                const NXOpen::Point3d & csysOrigin /** csysorigin */ 
            );
            /** Sets box csys matrix. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetBoxMatrixAndPosition
            (
                const NXOpen::Matrix3x3 & matrix /** matrix */ ,
                const NXOpen::Point3d & position /** position */ 
            );
            /** Calculate box size and set directions, edge length, lower point position. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void CalculateBoxSize
            (
            );
            /** Add insert part into assembly. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::NXObject * AddInsertPartIntoAssembly
            (
                NXOpen::NXObject * parentPart /** parentpart */ ,
                const NXString & templatePartName /** templatepartname */ ,
                const NXOpen::Point3d & origin /** origin */ 
            );
            /** Add insert part into assembly. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            NXOpen::NXObject * AddInsertPartIntoAssembly
            (
                NXOpen::NXObject * parentPart /** parentpart */ ,
                const char * templatePartName /** templatepartname */ ,
                const NXOpen::Point3d & origin /** origin */ 
            );
            /** Get hole boundary face and create patch openings. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::NXObject * GetHoleBoundaryFaceAndCreatePatchOpenings
            (
                const std::vector<NXOpen::NXObject *> & edges /** edges */ 
            );
            /** Create bound box. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::NXObject * CreateKFBoundBox
            (
                const NXOpen::Matrix3x3 & wcsMatrix /** wcsmatrix */ ,
                const std::vector<double> & clearance /** clearance */ ,
                const std::vector<NXOpen::NXObject *> & faces /** faces */ 
            );
            /** Create intersect. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void CreateIntersect
            (
                NXOpen::NXObject * targetBody /** targetbody */ ,
                NXOpen::NXObject * bodyOfKFBoundBox /** bodyofkfboundbox */ 
            );
            /** Wave intersect body to new die insert part. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void WaveIntersectBodyToNewDieInsertPart
            (
                const std::vector<NXOpen::NXObject *> & bodies /** bodies */ 
            );
            /** Delete selected insert and wave linked source feature. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void DeleteSelectedInsertAndWaveLinkedSource
            (
            );
            /** Suppress child feature. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SuppressAllFeatureAfter
            (
                NXOpen::NXObject * featureTag /** featuretag */ ,
                bool suppressChildren /** suppresschildren */ 
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
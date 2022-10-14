#ifndef NXOpen_TOOLING_INSERTBLOCKBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_INSERTBLOCKBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_InsertBlockBuilder.ja
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
        class InsertBlockBuilder;
    }
    namespace Assemblies
    {
        class SelectComponentList;
    }
    class Builder;
    class Direction;
    class Expression;
    class Section;
    class SelectBodyList;
    class TaggedObject;
    namespace Tooling
    {
        class _InsertBlockBuilderBuilder;
        class InsertBlockBuilderImpl;
        /**  Represents insert block builder.  <br> To create a new instance of this class, use @link NXOpen::Tooling::ProgressiveDieManager::CreateInsertBlockBuilder  NXOpen::Tooling::ProgressiveDieManager::CreateInsertBlockBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        BoundingBoxType </term> <description> 
         
        Block </description> </item> 

        <item><term> 
         
        ClearanceToggle </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        ConceptDesign </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        InsertBlockClearance </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        InsertBlockType </term> <description> 
         
        PunchBlock </description> </item> 

        <item><term> 
         
        InsertMode </term> <description> 
         
        StandardBlock </description> </item> 

        <item><term> 
         
        RenameDialog </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        UserDefinedInsertBlockHeight.Value </term> <description> 
         
        0 (millimeters part), 0 (inches part) </description> </item> 

        <item><term> 
         
        WithoutFalseBody </term> <description> 
         
        0 </description> </item> 

        </list> 

         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  InsertBlockBuilder : public NXOpen::Builder
        {
            /** Specifies the design ande edite insert block. */
            public: enum Types
            {
                TypesInsertBlock/** insert block */ ,
                TypesEditBlock/** edit block */ ,
                TypesDeleteBlock/** delete block */ 
            };

            /** Specifies the insert mode for insert block. */
            public: enum InsertModeItems
            {
                InsertModeItemsStandardBlock/** The block insert mode is standard insert */,
                InsertModeItemsSketchProfile/** The block insert mode is sketch profile */,
                InsertModeItemsBoundingBox/** The block insert mode is bounding box */
            };

            /** Insert Block Design Mode. */
            public: enum InsertBlockTypeItems
            {
                InsertBlockTypeItemsPunchBlock/** punch block */ ,
                InsertBlockTypeItemsBottomingBlock/** bottoming block */ ,
                InsertBlockTypeItemsStripperBlock/** stripper block */ 
            };

            /** Specifies the bounding box type. */
            public: enum BoundingBoxTypeItems
            {
                BoundingBoxTypeItemsBlock/** The bounding box type is Block */,
                BoundingBoxTypeItemsCylinder/** The bounding box type is Cylinder */
            };

            private: InsertBlockBuilderImpl * m_insertblockbuilder_impl;
            private: friend class  _InsertBlockBuilderBuilder;
            protected: InsertBlockBuilder();
            public: ~InsertBlockBuilder();
            /**Returns  the operation type of insert block. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::InsertBlockBuilder::Types InsertType
            (
            );
            /**Sets  the operation type of insert block. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetInsertType
            (
                NXOpen::Tooling::InsertBlockBuilder::Types type /** type */ 
            );
            /**Returns  the scrap select. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBodyList * FacesSelect
            (
            );
            /**Returns  the insert to edit 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Assemblies::SelectComponentList * InsertToEdit
            (
            );
            /**Returns  the insert to delete 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::Assemblies::SelectComponentList * InsertToDelete
            (
            );
            /**Returns  the parent part name to create insert. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ParentPartName
            (
            );
            /**Sets  the parent part name to create insert. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetParentPartName
            (
                const NXString & parentPartName /** Specifies the parent part name */
            );
            /**Sets  the parent part name to create insert. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            void SetParentPartName
            (
                const char * parentPartName /** Specifies the parent part name */
            );
            /**Returns  the new component names. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXString NewPartNames
            (
            );
            /**Sets  the new component names. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetNewPartNames
            (
                const NXString & newPartNames /** Specifies the new component names */
            );
            /**Sets  the new component names. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            void SetNewPartNames
            (
                const char * newPartNames /** Specifies the new component names */
            );
            /**Returns  the insert block mode 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::InsertBlockBuilder::InsertModeItems InsertMode
            (
            );
            /**Sets  the insert block mode 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetInsertMode
            (
                NXOpen::Tooling::InsertBlockBuilder::InsertModeItems insertMode /** insertmode */ 
            );
            /**Returns  the insert block design type 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::InsertBlockBuilder::InsertBlockTypeItems InsertBlockType
            (
            );
            /**Sets  the insert block design type 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetInsertBlockType
            (
                NXOpen::Tooling::InsertBlockBuilder::InsertBlockTypeItems insertBlockType /** insertblocktype */ 
            );
            /** Insert the standard insert block by invoking standard part management dialog
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void StandardInsertBlock
            (
            );
            /**Returns  the insert block instance tag. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TaggedObject * StandardInsertBlockTag
            (
            );
            /**Sets  the insert block instance tag. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetStandardInsertBlockTag
            (
                NXOpen::TaggedObject * standardInsertBlockTag /** Specifies the standard insert block instance */
            );
            /**Returns  the insert block shim distance 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: double BlockShimDistance
            (
            );
            /**Sets  the insert block shim distance 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetBlockShimDistance
            (
                double blockShimDistance /** blockshimdistance */ 
            );
            /**Returns  the clearance toggle 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool ClearanceToggle
            (
            );
            /**Sets  the clearance toggle 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetClearanceToggle
            (
                bool clearanceToggle /** clearancetoggle */ 
            );
            /**Returns  the insert block clearance 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: double InsertBlockClearance
            (
            );
            /**Sets  the insert block clearance 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetInsertBlockClearance
            (
                double insertBlockClearance /** insertblockclearance */ 
            );
            /**Returns  the select insert block outline 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * SelectInsertBlockOutline
            (
            );
            /**Returns  the user defined insert block height 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * UserDefinedInsertBlockHeight
            (
            );
            /** Create datum plane for user defined insert block outline. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void CreateUserDefinedInsertDatumPlane
            (
            );
            /** Create datum plane for user defined insert block outline. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void DeleteUnusedDatumAndSketch
            (
            );
            /** Add insert block part into assembly when creating user defined insert datum plane 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void AddInsertBlockPart
            (
            );
            /**Returns  the select vector 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * SelectVector
            (
            );
            /**Sets  the select vector 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetSelectVector
            (
                NXOpen::Direction * selectVector /** selectvector */ 
            );
            /**Returns  the bounding box type. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::InsertBlockBuilder::BoundingBoxTypeItems BoundingBoxType
            (
            );
            /**Sets  the bounding box type. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetBoundingBoxType
            (
                NXOpen::Tooling::InsertBlockBuilder::BoundingBoxTypeItems boundingBoxType /** boundingboxtype */ 
            );
            /** Sets box csys matrix. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetManipulatorToMatrixAndPosition
            (
                const NXOpen::Matrix3x3 & matrix /** matrix */ ,
                const NXOpen::Point3d & position /** position */ 
            );
            /** Calculate box size and set directions, edge length, lower point position. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void CalculateBoxSize
            (
            );
            /**Returns  the offset value linear dimension positive x. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OffsetValueLinearDimensionPositiveX
            (
            );
            /**Returns  the offset value linear dimension negative x. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OffsetValueLinearDimensionNegativeX
            (
            );
            /**Returns  the offset value linear dimension positive y. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OffsetValueLinearDimensionPositiveY
            (
            );
            /**Returns  the offset value linear dimension negative y. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OffsetValueLinearDimensionNegativeY
            (
            );
            /**Returns  the offset value linear dimension positive z. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OffsetValueLinearDimensionPositiveZ
            (
            );
            /**Returns  the offset value linear dimension negative z. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OffsetValueLinearDimensionNegativeZ
            (
            );
            /**Returns  the radial offset value for cylinder box. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RadialOffset
            (
            );
            /**Returns  the position of csys for box. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point3d BoxPosition
            (
            );
            /**Sets  the position of csys for box. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetBoxPosition
            (
                const NXOpen::Point3d & csysOrigin /** csysorigin */ 
            );
            /** Create user defined punch/bottoming/stripper insert block for selected scraps when creating insert block by user defined type. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void CreateUserDefinedInsertBlock
            (
            );
            /**Returns  the value indicating if the design is for a concept. True indicates it is a concept design. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool ConceptDesign
            (
            );
            /**Sets  the value indicating if the design is for a concept. True indicates it is a concept design. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetConceptDesign
            (
                bool conceptDesign /** Indicates whether it is a concept design */
            );
            /**Returns  the option of whether to create false body for die or backing insert. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool WithoutFalseBody
            (
            );
            /**Sets  the option of whether to create false body for die or backing insert. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetWithoutFalseBody
            (
                bool withoutFalseBody /** Indicates whether to create false body */
            );
            /**Returns  the rename dialog option for normal pierce design. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool RenameDialog
            (
            );
            /**Sets  the rename dialog option for normal pierce design. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetRenameDialog
            (
                bool renameDialog /** Indicates the rename dialog option for normal pierce design */
            );
            /**Returns  the user defined datum plane. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TaggedObject * UserDefBlockDatumPlane
            (
            );
            /**Sets  the user defined datum plane. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetUserDefBlockDatumPlane
            (
                NXOpen::TaggedObject * userDefBlockDatumPlane /** userdefblockdatumplane */ 
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
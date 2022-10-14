#ifndef NXOpen_TOOLING_WORKPIECEBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_WORKPIECEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_WorkpieceBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/Tooling_WorkPieceData.hxx>
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
        class WorkpieceBuilder;
    }
    class Builder;
    namespace Features
    {
        class FeatureBuilder;
    }
    class NXObject;
    class Point;
    class SelectBodyList;
    namespace Tooling
    {
        class WorkPieceData;
    }
    namespace Tooling
    {
        class _WorkpieceBuilderBuilder;
        class WorkpieceBuilderImpl;
        /** Mold Wizard work piece builder  <br> To create a new instance of this class, use @link NXOpen::Tooling::WorkpieceCollection::CreateWorkpieceBuilder  NXOpen::Tooling::WorkpieceCollection::CreateWorkpieceBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        BlockType </term> <description> 
         
        UserDefinedBlock </description> </item> 

        <item><term> 
         
        GenerateMethod </term> <description> 
         
        DistanceAllowance </description> </item> 

        <item><term> 
         
        RoundDimensionValue </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        RoundPrecision </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        ShowBoundbox </term> <description> 
         
        0 </description> </item> 

        </list> 

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  WorkpieceBuilder : public NXOpen::Builder
        {
            /** the unit type includes product and combined work piece type*/
            public: enum Types
            {
                TypesProductWorkPiece/** The old assembly of Mold wizard*/,
                TypesCombinedWorkPiece/** The new assembly of Mold wizard*/
            };

            /** the unit type includes the work piece create method*/
            public: enum WorkPieceType
            {
                WorkPieceTypeUserDefinedBlock/** The method defines the block by user*/,
                WorkPieceTypeCavityCore/** The method adds the standards of cavity and core*/,
                WorkPieceTypeCavityOnly/** The method adds the standards of cavity*/,
                WorkPieceTypeCoreOnly/** The method adds the standards of cavity*/
            };

            /** the unit type includes the work piece define method*/
            public: enum MethodType
            {
                MethodTypeDistanceAllowance/** Create block by define the distance allowance*/,
                MethodTypeReferencePoint/** Create block by define the reference point*/,
                MethodTypeSketch/** Create block by extrude the sketch*/,
                MethodTypeKfBox/** Create block by define the kf box*/
            };

            private: WorkpieceBuilderImpl * m_workpiecebuilder_impl;
            private: friend class  _WorkpieceBuilderBuilder;
            protected: WorkpieceBuilder();
            public: ~WorkpieceBuilder();
            /**Returns  the work piece shape type access functions 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::WorkpieceBuilder::WorkPieceType BlockType
            (
            );
            /**Sets  the work piece shape type access functions 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetBlockType
            (
                NXOpen::Tooling::WorkpieceBuilder::WorkPieceType blockType /** blocktype */ 
            );
            /**Returns  the generate method access functions 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::WorkpieceBuilder::MethodType GenerateMethod
            (
            );
            /**Sets  the generate method access functions 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetGenerateMethod
            (
                NXOpen::Tooling::WorkpieceBuilder::MethodType generateMethod /** generatemethod */ 
            );
            /** Resets workpiece sizes 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void ResetSizes
            (
            );
            /**Returns  the reference point to generate the work piece 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * ReferencePoint
            (
            );
            /**Sets  the reference point to generate the work piece 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetReferencePoint
            (
                NXOpen::Point * referencePoint /** referencepoint */ 
            );
            /**Returns  the work piece body selection 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBodyList * SelectWorkPieceBody
            (
            );
            /**Returns  the dimension round value 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool RoundDimensionValue
            (
            );
            /**Sets  the dimension round value 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRoundDimensionValue
            (
                bool roundDimensionValue /** rounddimensionvalue */ 
            );
            /**Returns  the round precision 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double RoundPrecision
            (
            );
            /**Sets  the round precision 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRoundPrecision
            (
                double roundPrecision /** roundprecision */ 
            );
            /**Returns  the setting to show the bounding box of the product or not 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowBoundbox
            (
            );
            /**Sets  the setting to show the bounding box of the product or not 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShowBoundbox
            (
                bool showBoundbox /** showboundbox */ 
            );
            /**Returns  the selection type to select the work piece 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::WorkpieceBuilder::Types Type
            (
            );
            /**Sets  the selection type to select the work piece 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetType
            (
                NXOpen::Tooling::WorkpieceBuilder::Types type /** type */ 
            );
            /**Gets workpiece data.
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::WorkPieceData * GetWorkPieceData
            (
            );
            /**Creates workpiece data.
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: NXOpen::Tooling::WorkPieceData * CreateWorkPieceData
            (
            );
            /**Sets the blank status of the workpiece part.
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetWorkpiecePartBlankStatus
            (
                NXOpen::NXObject * partTag /** parttag */ ,
                int blank /**Blank status  0 - Unblanked, 1 - Blanked*/
            );
            /**Initializes the data in old mold assemble.
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void InitWorkPieceData
            (
                NXOpen::Tooling::WorkpieceBuilder::MethodType* type /** the workpiece define method defined in @link NXOpen::Tooling::WorkpieceBuilder::MethodType NXOpen::Tooling::WorkpieceBuilder::MethodType@endlink  */,
                NXOpen::Tooling::WorkpieceBuilder::WorkPieceType* workpiecetype /** the workpiece create method defined in @link NXOpen::Tooling::WorkpieceBuilder::WorkPieceType NXOpen::Tooling::WorkpieceBuilder::WorkPieceType@endlink  */
            );
            /**Sets layout information.
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetLayoutInfo
            (
            );
            /**Changes the position and the dimension of the workpiece  
                      while creating workpiece with sketch method.
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void UpdateSketchCurves
            (
                NXOpen::NXObject * workpiece /** workpiece */ 
            );
            /**Changes the position and the dimension of the workpiece  
                      while creating workpiece with reference point method in new template.
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void UpdateSketchCurvesWhenUsingRefPoint
            (
                NXOpen::NXObject * sketchTag /** sketchtag */ ,
                const std::vector<double> & offset /**the minus and plus value of the XYZ direction distance offset*/
            );
            /**Links the sketch workpiece to shrink part.
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void LinkSketchWorkpieceToShrinkPart
            (
                NXOpen::Tooling::WorkpieceBuilder::WorkPieceType createType /** the workpiece create method defined in @link NXOpen::Tooling::WorkpieceBuilder::WorkPieceType NXOpen::Tooling::WorkpieceBuilder::WorkPieceType@endlink  */,
                NXOpen::NXObject * body /** the workpiece sketch*/
            );
            /** Sets extrude builder. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetExtrudeBuilder
            (
                NXOpen::Features::FeatureBuilder * extrude /** extrude */ 
            );
            /** Sets combined extrude builder. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetCombinedExtrudeBuilder
            (
                NXOpen::Features::FeatureBuilder * combinedExtrude /** combinedextrude */ 
            );
            /** Moves workpiece standard part to specified layer. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void MoveStandardWorkpieceToLayer
            (
                int newLayer /** newlayer */ 
            );
            /** Moves workpiece sketch to specified layer. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void MoveWorkpieceSketchToLayer
            (
                int newLayer /** newlayer */ 
            );
            /** Edits workpiece udo. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void EditWorkpieceUdo
            (
                NXOpen::NXObject * body /** the body linked to the workpiece UDO object, it can be NULL_TAG*/,
                const std::vector<double> & boxSize /** the size of box. It is shown by the coordinates of two diagonal points */
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
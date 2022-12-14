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
#include <NXOpen/Tooling_WorkpieceBuilder.hxx>
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
    class Point;
    class SelectBodyList;
    namespace Tooling
    {
        class _WorkpieceBuilderBuilder;
        class WorkpieceBuilderImpl;
        /** Mold Wizard work piece builder  <br> To create a new instance of this class, use @link Tooling::WorkpieceCollection::CreateWorkpieceBuilder  Tooling::WorkpieceCollection::CreateWorkpieceBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        BlockType </td> <td> 
         
        UserDefinedBlock </td> </tr> 

        <tr><td> 
         
        GenerateMethod </td> <td> 
         
        DistanceAllowance </td> </tr> 

        <tr><td> 
         
        RoundDimensionValue </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        RoundPrecision </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ShowBoundbox </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  WorkpieceBuilder : public Builder
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

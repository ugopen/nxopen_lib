#ifndef NXOpen_FEATURES_MOVEOBJECTBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_MOVEOBJECTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_MoveObjectBuilder.ja
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
#include <NXOpen/GeometricUtilities_ModlMotion.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class MoveObjectBuilder;
    }
    class Builder;
    namespace GeometricUtilities
    {
        class ModlMotion;
    }
    class SelectNXObjectList;
    namespace Features
    {
        class _MoveObjectBuilderBuilder;
        class MoveObjectBuilderImpl;
        /** Represents a @link NXOpen::Features::MoveObjectBuilder NXOpen::Features::MoveObjectBuilder@endlink .
                Inputs to this class can be convergent objects.  <br> To create a new instance of this class, use @link NXOpen::Features::BaseFeatureCollection::CreateMoveObjectBuilder  NXOpen::Features::BaseFeatureCollection::CreateMoveObjectBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        Associative </term> <description> 
         
        false </description> </item> 

        <item><term> 
         
        CreateTraceLines </term> <description> 
         
        false </description> </item> 

        <item><term> 
         
        Divisions </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        LayerOption </term> <description> 
         
        Original </description> </item> 

        <item><term> 
         
        MoveObjectResult </term> <description> 
         
        MoveOriginal </description> </item> 

        <item><term> 
         
        MoveParents </term> <description> 
         
        true </description> </item> 

        <item><term> 
         
        NumberOfCopies </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        TransformMotion.DeltaEnum </term> <description> 
         
        ReferenceWcsWorkPart </description> </item> 

        <item><term> 
         
        TransformMotion.DeltaXc.Value </term> <description> 
         
        0.0 </description> </item> 

        <item><term> 
         
        TransformMotion.DeltaYc.Value </term> <description> 
         
        0.0 </description> </item> 

        <item><term> 
         
        TransformMotion.DeltaZc.Value </term> <description> 
         
        0.0 </description> </item> 

        <item><term> 
         
        TransformMotion.Option </term> <description> 
         
        Dynamic </description> </item> 

        </list> 

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  MoveObjectBuilder : public NXOpen::Builder
        {
            /** Indicates whether to move or copy objects */
            public: enum MoveObjectResultOptions
            {
                MoveObjectResultOptionsMoveOriginal/** move objects */,
                MoveObjectResultOptionsCopyOriginal/** copy objects*/
            };

            /** Indicates the layer on which moved or copied objects will be placed*/
            public: enum LayerOptionType
            {
                LayerOptionTypeOriginal/** Original Layer */,
                LayerOptionTypeWork/** Work Layer */,
                LayerOptionTypeAsSpecified/** As Specified Layer */
            };

            private: MoveObjectBuilderImpl * m_moveobjectbuilder_impl;
            private: friend class  _MoveObjectBuilderBuilder;
            protected: MoveObjectBuilder();
            public: ~MoveObjectBuilder();
            /**Returns  the objects to move-rotate 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * ObjectToMoveObject
            (
            );
            /**Returns  the transform 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::ModlMotion * TransformMotion
            (
            );
            /**Returns  the move rotate result 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::MoveObjectBuilder::MoveObjectResultOptions MoveObjectResult
            (
            );
            /**Sets  the move rotate result 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMoveObjectResult
            (
                NXOpen::Features::MoveObjectBuilder::MoveObjectResultOptions moveObjectResult /** moveobjectresult */ 
            );
            /**Returns  the layer option 
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::MoveObjectBuilder::LayerOptionType LayerOption
            (
            );
            /**Sets  the layer option 
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : None */
            public: void SetLayerOption
            (
                NXOpen::Features::MoveObjectBuilder::LayerOptionType layerOptionType /** layeroptiontype */ 
            );
            /**Returns  the layer 
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : None */
            public: int Layer
            (
            );
            /**Sets  the layer 
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : None */
            public: void SetLayer
            (
                int layer /** layer */ 
            );
            /**Returns  the distance or angle divisions 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: int Divisions
            (
            );
            /**Sets  the distance or angle divisions 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDivisions
            (
                int distanceOrAngleDivisions /** distanceorangledivisions */ 
            );
            /**Returns  the number of copies 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: int NumberOfCopies
            (
            );
            /**Sets  the number of copies 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetNumberOfCopies
            (
                int numCopies /** numcopies */ 
            );
            /**Returns  the move parents flag. The parents of selected objects will be moved only when Associative flag is false. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool MoveParents
            (
            );
            /**Sets  the move parents flag. The parents of selected objects will be moved only when Associative flag is false. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMoveParents
            (
                bool moveParents /** moveparents */ 
            );
            /**Returns  the associative flag. A Move Object feature is created only when Move Parents flag is false. 
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : None */
            public: bool Associative
            (
            );
            /**Sets  the associative flag. A Move Object feature is created only when Move Parents flag is false. 
             <br>  Created in NX6.0.2.  <br>  
             <br> License requirements : None */
            public: void SetAssociative
            (
                bool associative /** associative */ 
            );
            /**Returns  the create trace lines flag 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool CreateTraceLines
            (
            );
            /**Sets  the create trace lines flag 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetCreateTraceLines
            (
                bool createTraceLines /** createtracelines */ 
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
#ifndef NXOpen_FEATURES_DRAWSHAPES_TRANSFORMDATA_HXX_INCLUDED
#define NXOpen_FEATURES_DRAWSHAPES_TRANSFORMDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_DrawShapes_TransformData.ja
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
#include <NXOpen/GeometricUtilities_TransformerData.hxx>
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
        namespace DrawShapes
        {
            class TransformData;
        }
    }
    class Builder;
    namespace GeometricUtilities
    {
        class TransformerData;
    }
    class SelectNXObjectList;
    namespace Features
    {
        namespace DrawShapes
        {
            class _TransformDataBuilder;
            class TransformDataImpl;
            /** Represents @link  NXOpen::Features::DrawShapes::TransformData   NXOpen::Features::DrawShapes::TransformData @endlink 
                    allowing user to delete strokes and curves.
                 <br> To create a new instance of this class, use @link NXOpen::Features::DrawShapes::DrawShapeCollection::CreateTransformData  NXOpen::Features::DrawShapes::DrawShapeCollection::CreateTransformData @endlink  <br> 
            Default values.
            <list type="table"> 
             
            <listheader><term> 
            Property</term>  <description> 
            Value</description> </listheader>
            <item><term> 
             
            CanRelocateToolToSelection </term> <description> 
             
            1 </description> </item> 

            <item><term> 
             
            CanReorientToolToSelection </term> <description> 
             
            1 </description> </item> 

            <item><term> 
             
            NumberOfCopies </term> <description> 
             
            1 </description> </item> 

            </list> 

             <br>  Created in NX1926.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  TransformData : public NXOpen::Builder
            {
                /** Scaling options */
                public: enum ScalingOptions
                {
                    ScalingOptionsLinear/** linear */ ,
                    ScalingOptionsPlanar/** planar */ ,
                    ScalingOptionsUniform/** uniform */ 
                };

                /** Transform operation result options */
                public: enum ResultOptions
                {
                    ResultOptionsMoveOriginal/** move original */ ,
                    ResultOptionsCopyOriginal/** copy original */ 
                };

                private: TransformDataImpl * m_transformdata_impl;
                private: friend class  _TransformDataBuilder;
                protected: TransformData();
                public: ~TransformData();
                /**Returns  the objects to be transformed 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectNXObjectList * ObjectsToTransform
                (
                );
                /**Returns  the transformation tool. The tool allows user to transform the pasted topology. 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::GeometricUtilities::TransformerData * Transformer
                (
                );
                /**Returns  the can move tool only 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: bool CanMoveToolOnly
                (
                );
                /**Sets  the can move tool only 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_draw_shape (" NX Draw Shape Functionality") */
                public: void SetCanMoveToolOnly
                (
                    bool canMoveToolOnly /** canmovetoolonly */ 
                );
                /**Returns  the can relocate tool to selection 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: bool CanRelocateToolToSelection
                (
                );
                /**Sets  the can relocate tool to selection 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_draw_shape (" NX Draw Shape Functionality") */
                public: void SetCanRelocateToolToSelection
                (
                    bool canRelocateToolToSelection /** canrelocatetooltoselection */ 
                );
                /**Returns  the can reorient tool to selection 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: bool CanReorientToolToSelection
                (
                );
                /**Sets  the can reorient tool to selection 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_draw_shape (" NX Draw Shape Functionality") */
                public: void SetCanReorientToolToSelection
                (
                    bool canReorientToolToSelection /** canreorienttooltoselection */ 
                );
                /**Returns  the scaling 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::DrawShapes::TransformData::ScalingOptions Scaling
                (
                );
                /**Sets  the scaling 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_draw_shape (" NX Draw Shape Functionality") */
                public: void SetScaling
                (
                    NXOpen::Features::DrawShapes::TransformData::ScalingOptions scaling /** scaling */ 
                );
                /**Returns  the result option 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::DrawShapes::TransformData::ResultOptions ResultOption
                (
                );
                /**Sets  the result option 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_draw_shape (" NX Draw Shape Functionality") */
                public: void SetResultOption
                (
                    NXOpen::Features::DrawShapes::TransformData::ResultOptions resultOption /** resultoption */ 
                );
                /**Returns  the number of copies 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : None */
                public: int NumberOfCopies
                (
                );
                /**Sets  the number of copies 
                 <br>  Created in NX1926.0.0.  <br>  
                 <br> License requirements : nx_draw_shape (" NX Draw Shape Functionality") */
                public: void SetNumberOfCopies
                (
                    int numberOfCopies /** numberofcopies */ 
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

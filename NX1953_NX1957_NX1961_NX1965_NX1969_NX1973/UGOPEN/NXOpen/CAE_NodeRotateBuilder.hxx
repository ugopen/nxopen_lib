#ifndef NXOpen_CAE_NODEROTATEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_NODEROTATEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_NodeRotateBuilder.ja
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
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class NodeRotateBuilder;
    }
    class Axis;
    class Builder;
    namespace CAE
    {
        class SelectFENodeList;
    }
    class Expression;
    namespace CAE
    {
        class _NodeRotateBuilderBuilder;
        class NodeRotateBuilderImpl;
        /**
            Represents a @link NXOpen::CAE::NodeRotateBuilder NXOpen::CAE::NodeRotateBuilder@endlink 
             <br> To create a new instance of this class, use @link NXOpen::CAE::NodeElementManager::CreateNodeRotateBuilder  NXOpen::CAE::NodeElementManager::CreateNodeRotateBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  NodeRotateBuilder : public NXOpen::Builder
        {
            /** the copy types */
            public: enum CopyType
            {
                CopyTypeRotateOnly/**rotate only */,
                CopyTypeCopyRotate/**copy rotate */
            };

            /** the distance types */
            public: enum DistanceType
            {
                DistanceTypePerCopy/**per copy */,
                DistanceTypeTotal/**total */
            };

            /** the label types */
            public: enum LabelType
            {
                LabelTypeLabelIncrement/**label increment */,
                LabelTypeByOffset/**by offset */
            };

            private: NodeRotateBuilderImpl * m_noderotatebuilder_impl;
            private: friend class  _NodeRotateBuilderBuilder;
            protected: NodeRotateBuilder();
            public: ~NodeRotateBuilder();
            /**Returns  the copy option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::NodeRotateBuilder::CopyType CopyOption
            (
            );
            /**Sets  the copy option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetCopyOption
            (
                NXOpen::CAE::NodeRotateBuilder::CopyType copyOption /** copyoption */ 
            );
            /**Returns  the node 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::SelectFENodeList * Node
            (
            );
            /**Returns  the num copy 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int NumCopy
            (
            );
            /**Sets  the num copy 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetNumCopy
            (
                int numCopy /** numcopy */ 
            );
            /**Returns  the distance option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::NodeRotateBuilder::DistanceType DistanceOption
            (
            );
            /**Sets  the distance option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetDistanceOption
            (
                NXOpen::CAE::NodeRotateBuilder::DistanceType distanceOption /** distanceoption */ 
            );
            /**Returns  the angle 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Angle
            (
            );
            /**Returns  the axis 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Axis * Axis
            (
            );
            /**Sets  the axis 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetAxis
            (
                NXOpen::Axis * axis /** axis */ 
            );
            /**Returns  the label option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::NodeRotateBuilder::LabelType LabelOption
            (
            );
            /**Sets  the label option 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetLabelOption
            (
                NXOpen::CAE::NodeRotateBuilder::LabelType labelOption /** labeloption */ 
            );
            /**Returns  the label 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int Label
            (
            );
            /**Sets  the label 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetLabel
            (
                int label /** label */ 
            );
            /**Returns  the increment 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int Increment
            (
            );
            /**Sets  the increment 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetIncrement
            (
                int increment /** increment */ 
            );
            /**Returns  the offset 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int Offset
            (
            );
            /**Sets  the offset 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetOffset
            (
                int offset /** offset */ 
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

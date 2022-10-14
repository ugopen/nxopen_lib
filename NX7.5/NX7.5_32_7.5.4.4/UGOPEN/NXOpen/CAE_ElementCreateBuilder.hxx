#ifndef NXOpen_CAE_ELEMENTCREATEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_ELEMENTCREATEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ElementCreateBuilder.ja
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
#include <NXOpen/CAE_ElementCreateBuilder.hxx>
#include <NXOpen/CAE_ElementTypeBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class ElementCreateBuilder;
    }
    class Builder;
    namespace CAE
    {
        class ElementTypeBuilder;
    }
    namespace CAE
    {
        class SelectFENodeList;
    }
    namespace CAE
    {
        class _ElementCreateBuilderBuilder;
        class ElementCreateBuilderImpl;
        /**
            Represents a @link CAE::ElementCreateBuilder CAE::ElementCreateBuilder@endlink  which allows you to manually create elements from existing nodes.
             <br>       
            The following element topologies are supported 
            <ul>
                <li>0D or Point elements, requires 1 node to define</li>
                <li>1D or Beam elements, requires 2 nodes to define</li>
                <li>2D or Shell elements</li>
                <ul>
                    <li>Linear Tria elements, requires 3 corner nodes to define. </li>
                    <li>Parabolic Tria elements, requires 6 nodes to define ( 3 corner and 3 mid nodes ). </li>
                    <li>Linear Quad elements, requires 4 corner nodes to define. </li>
                    <li>Parabolic Quad elements, requires 8 nodes to define ( 4 corner and 4 mid nodes ). </li>
                </ul>  
                <br/>When specifying nodes for Shell elements with mid nodes, the input order is sequential.  Corner, Mid, Corner, Mod, ... 
                 @code  
                3                       5                                                                           
               / \                     / \             
              /   \                   /   \            4---------------3    7-------6-------5
             /     \                 /     \           |               |    |               |
            /       \               6       4          |               |    |               |
           /         \             /         \         |               |    8               4
          /           \           /           \        |               |    |               |
         /             \         /             \       |               |    |               |
        1---------------2       1-------2-------3      1---------------2    1-------2-------3
             Tria(3)                  Tria(6)               Quad(4)              Quad(8)
                 @endcode  
                <li>3D or Solid elements, NOTE: not all of these Solid types can be created through the UI</li>
                <ul>
                    <li>Linear Tetra elements, requires 4 corner nodes to define. </li>
                    <li>Parabolic Tetra elements, requires 10 nodes to define ( 4 corner and 6 mid nodes ). </li>
                    <li>Linear Penta elements, requires 6 corner nodes to define. </li>
                    <li>Parabolic Penta elements, requires 15 nodes to define ( 6 corner and 9 mid nodes ). </li>
                    <li>Linear Hexa elements, requires 8 corner nodes to define. </li>
                    <li>Parabolic Hexa elements, requires 20 nodes to define ( 8 corner and 12 mid nodes ). </li>
                    <li>Linear Pyramid elements, requires 5 corner nodes to define. </li>
                    <li>Parabolic Pyramid elements, requires 13 nodes to define ( 5 corner and 8 mid nodes ). </li>
                </ul>  
                <br/>When specifying nodes for Solid elements, the input order(connectivity) is the same as is defined in Nastran.  All Corners first and then all Mid nodes. 
                <br/>
            </ul>    

             <br>   
            
             <br> To create a new instance of this class, use @link CAE::NodeElementManager::CreateElementCreateBuilder CAE::NodeElementManager::CreateElementCreateBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  ElementCreateBuilder : public Builder
        {
            /**  Dimension of the element to be created */
            public: enum ElemDimType
            {
                ElemDimTypePoint/** 0D element*/,
                ElemDimTypeBeam/** beam*/,
                ElemDimTypeShell/** shell*/,
                ElemDimTypeSolid/** solid, types currently supported through UI */,
                ElemDimTypeAnySolid/** any solid type */
            };

            /**  Option to create new mesh or add to existing mesh */
            public: enum NewMeshType
            {
                NewMeshTypeCreate/** create new mesh*/,
                NewMeshTypeExisting/** add to existing mesh*/
            };

            private: ElementCreateBuilderImpl * m_elementcreatebuilder_impl;
            private: friend class  _ElementCreateBuilderBuilder;
            protected: ElementCreateBuilder();
            public: ~ElementCreateBuilder();
            /**Returns  the element dimension option  <br> License requirements : None */
            public: NXOpen::CAE::ElementCreateBuilder::ElemDimType ElementDimensionOption
            (
            );
            /**Sets  the element dimension option  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetElementDimensionOption
            (
                NXOpen::CAE::ElementCreateBuilder::ElemDimType elementDimensionOption /** elementdimensionoption */ 
            );
            /**Returns  the element type builder.   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ElementTypeBuilder * ElementType
            (
            );
            /**Returns  the element neutral name  <br> License requirements : None */
            public: NXString NeutralName
            (
            );
            /**Sets  the element neutral name  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetNeutralName
            (
                const NXString & neutralName /** neutralname */ 
            );
            /**Returns  the mesh collector name  <br> License requirements : None */
            public: NXString CollectorName
            (
            );
            /**Sets  the mesh collector name  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetCollectorName
            (
                const NXString & collectorName /** collectorname */ 
            );
            /** Create mesh collector  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void CreateCollector
            (
            );
            /**Returns  the new mesh option  <br> License requirements : None */
            public: NXOpen::CAE::ElementCreateBuilder::NewMeshType NewMeshOption
            (
            );
            /**Sets  the new mesh option  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetNewMeshOption
            (
                NXOpen::CAE::ElementCreateBuilder::NewMeshType newMeshOption /** newmeshoption */ 
            );
            /**Returns  the mesh name  <br> License requirements : None */
            public: NXString MeshName
            (
            );
            /**Sets  the mesh name  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetMeshName
            (
                const NXString & meshName /** meshname */ 
            );
            /**Returns  the selected node <br> License requirements : None */
            public: NXOpen::CAE::SelectFENodeList * Node
            (
            );
            /**Returns  the label  <br> License requirements : None */
            public: int Label
            (
            );
            /**Sets  the label  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetLabel
            (
                int label /** label */ 
            );
            /**Returns  the increment  <br> License requirements : None */
            public: int Increment
            (
            );
            /**Sets  the increment  <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetIncrement
            (
                int increment /** increment */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
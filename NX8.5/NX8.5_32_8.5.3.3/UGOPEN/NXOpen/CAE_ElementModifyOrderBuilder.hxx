#ifndef NXOpen_CAE_ELEMENTMODIFYORDERBUILDER_HXX_INCLUDED
#define NXOpen_CAE_ELEMENTMODIFYORDERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ElementModifyOrderBuilder.ja
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
#include <NXOpen/CAE_ElementModifyOrderBuilder.hxx>
#include <NXOpen/CAE_ElementTypeBuilder.hxx>
#include <NXOpen/Expression.hxx>
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
        class ElementModifyOrderBuilder;
    }
    class Builder;
    namespace CAE
    {
        class ElementTypeBuilder;
    }
    namespace CAE
    {
        class Mesh;
    }
    class Expression;
    class SelectTaggedObjectList;
    namespace CAE
    {
        class _ElementModifyOrderBuilderBuilder;
        class ElementModifyOrderBuilderImpl;
        /**
            Represents a @link CAE::ElementModifyOrderBuilder CAE::ElementModifyOrderBuilder@endlink 
             <br> To create a new instance of this class, use @link CAE::NodeElementManager::CreateElementModifyOrderBuilder  CAE::NodeElementManager::CreateElementModifyOrderBuilder @endlink  <br> 
         <br>  Created in NX6.0.1.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ElementModifyOrderBuilder : public Builder
        {
            /**  Represents the options for type of operation */
            public: enum Operation
            {
                OperationOrder/** changes the order of a mesh from linear to parabolic or vice versa */,
                OperationMidnode/** changes the midnode option for a parabolic mesh to mixed, curved or linear */
            };

            /**  Represents the options for midnodes */
            public: enum Midnode
            {
                MidnodeMixed/** mixed midnodes */,
                MidnodeCurved/** curved midnodes */,
                MidnodeLinear/** linear midnodes */
            };

            private: ElementModifyOrderBuilderImpl * m_elementmodifyorderbuilder_impl;
            private: friend class  _ElementModifyOrderBuilderBuilder;
            protected: ElementModifyOrderBuilder();
            public: ~ElementModifyOrderBuilder();
            /**Returns  the selected mesh(es) 
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectTaggedObjectList * MeshSelection
            (
            );
            /**Returns  the operation option 
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::ElementModifyOrderBuilder::Operation OperationType
            (
            );
            /**Sets  the operation option 
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetOperationType
            (
                NXOpen::CAE::ElementModifyOrderBuilder::Operation operationType /** operationtype */ 
            );
            /**Returns  the midnode option 
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::ElementModifyOrderBuilder::Midnode MidnodeType
            (
            );
            /**Sets  the midnode option 
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetMidnodeType
            (
                NXOpen::CAE::ElementModifyOrderBuilder::Midnode midnodeType /** midnodetype */ 
            );
            /**Returns  the jacobian value to be used for creating mixed type midnodes
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Jacobian
            (
            );
            /**Returns  the element type to be created
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::ElementTypeBuilder * ElementType
            (
            );
            /** Commites the mesh.
                      @return  
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: std::vector<NXOpen::CAE::Mesh *> CommitMesh
            (
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

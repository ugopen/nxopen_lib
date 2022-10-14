#ifndef NXOpen_CAE_NODEELEMENTINFOMANAGER_HXX_INCLUDED
#define NXOpen_CAE_NODEELEMENTINFOMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_NodeElementInfoManager.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class NodeElementInfoManager;
    }
    namespace CAE
    {
        class CaePart;
    }
    namespace CAE
    {
        class AssignNodalCSBuilder;
    }
    namespace CAE
    {
        class Mesh;
    }
    namespace CAE
    {
        class NodeElementInfoBuilder;
    }
    namespace CAE
    {
        class ThicknessBuilder;
    }
    namespace CAE
    {
        class NodeElementInfoManagerImpl;
        /**  @brief  Provides method for creating  builder for 
            node element info operation commands in both sim and fem part  

           <br> To obtain an instance of this class, refer to @link CAE::CaePart CAE::CaePart@endlink  <br> */
        class NXOPENCPPEXPORT  NodeElementInfoManager
        {
            private: NodeElementInfoManagerImpl * m_nodeelementinfomanager_impl;
            private: NXOpen::CAE::CaePart* m_owner;
            /** Constructor */
            public: explicit NodeElementInfoManager(NXOpen::CAE::CaePart *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~NodeElementInfoManager();
            /** Creates a builder for node element info command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::NodeElementInfoBuilder * CreateNodeElementInfoBuilder
            (
            );
            /** Creates a builder for node element info command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ThicknessBuilder * CreateThicknessBuilder
            (
                NXOpen::CAE::Mesh * meshContext /**Mesh object for thickness data access*/
            );
            /** Creates a builder for assigning nodal cs @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::AssignNodalCSBuilder * CreateAssignNodalCsBuilder
            (
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
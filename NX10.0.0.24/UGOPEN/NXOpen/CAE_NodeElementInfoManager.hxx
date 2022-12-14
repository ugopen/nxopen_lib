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
        class ThicknessPlotContoursBuilder;
    }
    namespace CAE
    {
        class NodeElementInfoManagerImpl;
        /**  @brief  Provides method for creating  builder for 
            node element info operation commands in both sim and fem part  

           <br> To obtain an instance of this class, refer to @link NXOpen::CAE::CaePart  NXOpen::CAE::CaePart @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  NodeElementInfoManager
        {
            private: NodeElementInfoManagerImpl * m_nodeelementinfomanager_impl;
            private: NXOpen::CAE::CaePart* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit NodeElementInfoManager(NXOpen::CAE::CaePart *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~NodeElementInfoManager();
            /** Creates a builder for node element info command @return  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::NodeElementInfoBuilder * CreateNodeElementInfoBuilder
            (
            );
            /** Creates a builder for node element info command @return  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ThicknessBuilder * CreateThicknessBuilder
            (
                NXOpen::CAE::Mesh * meshContext /**Mesh object for thickness data access*/
            );
            /** Creates a builder for assigning nodal cs @return  
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::AssignNodalCSBuilder * CreateAssignNodalCsBuilder
            (
            );
            /** Creates a builder for plotting thickness contours  @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ThicknessPlotContoursBuilder * CreateThicknessPlotContoursBuilder
            (
            );
        }; //lint !e1712 default constructor not defined for class  

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

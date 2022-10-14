#ifndef NXOpen_CAE_ELEMENTDELETEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_ELEMENTDELETEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ElementDeleteBuilder.ja
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
#include <NXOpen/CAE_ElementDeleteBuilder.hxx>
#include <NXOpen/CAE_SelectElementsBuilder.hxx>
#include <NXOpen/Builder.hxx>
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
        class ElementDeleteBuilder;
    }
    class Builder;
    namespace CAE
    {
        class SelectElementsBuilder;
    }
    namespace CAE
    {
        class _ElementDeleteBuilderBuilder;
        class ElementDeleteBuilderImpl;
        /**
            Represents a @link NXOpen::CAE::ElementDeleteBuilder NXOpen::CAE::ElementDeleteBuilder@endlink 
             <br> To create a new instance of this class, use @link NXOpen::CAE::NodeElementManager::CreateDeleteElementBuilder  NXOpen::CAE::NodeElementManager::CreateDeleteElementBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ElementDeleteBuilder : public NXOpen::Builder
        {
            private: ElementDeleteBuilderImpl * m_elementdeletebuilder_impl;
            private: friend class  _ElementDeleteBuilderBuilder;
            protected: ElementDeleteBuilder();
            public: ~ElementDeleteBuilder();
            /**Returns  the selected elements to be deleted
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::SelectElementsBuilder * Element
            (
            );
            /**Returns  the delete dangling node flag, whether the dangling nodes to be deleted 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool DeleteDangling
            (
            );
            /**Sets  the delete dangling node flag, whether the dangling nodes to be deleted 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetDeleteDangling
            (
                bool deleteDangling /** deletedangling */ 
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
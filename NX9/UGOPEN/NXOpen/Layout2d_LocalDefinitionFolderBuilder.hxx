#ifndef NXOpen_LAYOUT2D_LOCALDEFINITIONFOLDERBUILDER_HXX_INCLUDED
#define NXOpen_LAYOUT2D_LOCALDEFINITIONFOLDERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Layout2d_LocalDefinitionFolderBuilder.ja
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
#include <NXOpen/Layout2d_LocalDefinitionFolderBuilder.hxx>
#include <NXOpen/libnxopencpp_layout2d_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Layout2d
    {
        class LocalDefinitionFolderBuilder;
    }
    class Builder;
    namespace Layout2d
    {
        class LocalDefinitionFolder;
    }
    namespace Layout2d
    {
        class _LocalDefinitionFolderBuilderBuilder;
        class LocalDefinitionFolderBuilderImpl;
        /**
            Represents a @link Layout2d::LocalDefinitionFolderBuilder Layout2d::LocalDefinitionFolderBuilder@endlink . A local definition folder contains 2D Component definitions stored in 
            the current part.
             <br> To create a new instance of this class, use @link Layout2d::LocalDefinitionFolderCollection::CreateLocalDefinitionFolderBuilder  Layout2d::LocalDefinitionFolderCollection::CreateLocalDefinitionFolderBuilder @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_LAYOUT2DEXPORT  LocalDefinitionFolderBuilder : public Builder
        {
            private: LocalDefinitionFolderBuilderImpl * m_localdefinitionfolderbuilder_impl;
            private: friend class  _LocalDefinitionFolderBuilderBuilder;
            protected: LocalDefinitionFolderBuilder();
            public: ~LocalDefinitionFolderBuilder();
            /**Returns  the current folder name
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            public: NXString FolderName
            (
            );
            /**Sets  the current folder name
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            public: void SetFolderName
            (
                const NXString & folderName /** folder name*/
            );
            /**Sets  the current folder name
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            void SetFolderName
            (
                const char * folderName /** folder name*/
            );
            /**Returns  the current folder's parent 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            public: NXOpen::Layout2d::LocalDefinitionFolder * Parent
            (
            );
            /**Sets  the current folder's parent 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            public: void SetParent
            (
                NXOpen::Layout2d::LocalDefinitionFolder * parentfolder /** parent local definition folder*/
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
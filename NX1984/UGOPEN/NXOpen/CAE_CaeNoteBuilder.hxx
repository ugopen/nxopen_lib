#ifndef NXOpen_CAE_CAENOTEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_CAENOTEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_CaeNoteBuilder.ja
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
#include <NXOpen/Annotations_DraftingNoteBuilder.hxx>
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
        class CaeNoteBuilder;
    }
    namespace Annotations
    {
        class DraftingNoteBuilder;
    }
    namespace Annotations
    {
        class NoteBase;
    }
    class SelectTaggedObjectList;
    namespace CAE
    {
        class _CaeNoteBuilderBuilder;
        class CaeNoteBuilderImpl;
        /** Represents a CAE note builder class  <br> To create a new instance of this class, use @link NXOpen::CAE::NoteManager::CreateCaeNoteBuilder  NXOpen::CAE::NoteManager::CreateCaeNoteBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  CaeNoteBuilder : public NXOpen::Annotations::DraftingNoteBuilder
        {
            private: CaeNoteBuilderImpl * m_caenotebuilder_impl;
            private: friend class  _CaeNoteBuilderBuilder;
            protected: CaeNoteBuilder();
            public: ~CaeNoteBuilder();
            /**Returns  the associated objects for the annotation 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectTaggedObjectList * AssociatedObjects
            (
            );
            /** Sets folder name into the builder 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetFolderName
            (
                const NXString & folderName /** foldername */ 
            );
            /** Sets folder name into the builder 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            void SetFolderName
            (
                const char * folderName /** foldername */ 
            );
            /** Covert CAE Label to Note 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void ConvertLabelToNote
            (
                NXOpen::Annotations::NoteBase * annotation /** annotation */ 
            );
            /** Covert CAE Note to Label 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void ConvertNoteToLabel
            (
                NXOpen::Annotations::NoteBase * annotation /** annotation */ 
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
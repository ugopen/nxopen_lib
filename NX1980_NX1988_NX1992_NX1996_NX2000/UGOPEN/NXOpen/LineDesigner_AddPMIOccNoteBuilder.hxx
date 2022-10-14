#ifndef NXOpen_LINEDESIGNER_ADDPMIOCCNOTEBUILDER_HXX_INCLUDED
#define NXOpen_LINEDESIGNER_ADDPMIOCCNOTEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     LineDesigner_AddPMIOccNoteBuilder.ja
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
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/liblinedesigneropencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace LineDesigner
    {
        class AddPMIOccNoteBuilder;
    }
    class Builder;
    class SelectDisplayableObjectList;
    namespace LineDesigner
    {
        class _AddPMIOccNoteBuilderBuilder;
        class AddPMIOccNoteBuilderImpl;
        /**Class for creating pmi occ note <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateAddPmiOccNoteBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateAddPmiOccNoteBuilder @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class LINEDESIGNEROPENCPPEXPORT  AddPMIOccNoteBuilder : public NXOpen::Builder
        {
            private: AddPMIOccNoteBuilderImpl * m_addpmioccnotebuilder_impl;
            private: friend class  _AddPMIOccNoteBuilderBuilder;
            protected: AddPMIOccNoteBuilder();
            public: ~AddPMIOccNoteBuilder();
            /**Returns  the component selection 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * ComponentSelection
            (
            );
            /** TODO: fill in a description for this 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void AddButton
            (
            );
            /** Sets the note text 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetNoteTextFromListBox
            (
                const std::vector<NXString> & noteText /** notetext */ 
            );
            /** Returns the note text 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetNoteTextFromListBox
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
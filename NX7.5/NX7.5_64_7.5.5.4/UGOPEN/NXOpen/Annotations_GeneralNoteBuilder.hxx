#ifndef NXOpen_ANNOTATIONS_GENERALNOTEBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_GENERALNOTEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_GeneralNoteBuilder.ja
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
#include <NXOpen/Annotations_GeneralNoteBuilder.hxx>
#include <NXOpen/Annotations_PmiAttributeBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class GeneralNoteBuilder;
    }
    namespace Annotations
    {
        class PmiAttributeBuilder;
    }
    namespace Annotations
    {
        class _GeneralNoteBuilderBuilder;
        class GeneralNoteBuilderImpl;
        /** Represents a @link Annotations::GeneralNote Annotations::GeneralNote@endlink  builder  <br> To create a new instance of this class, use @link Annotations::PmiAttributeCollection::CreateGeneralNoteBuilder Annotations::PmiAttributeCollection::CreateGeneralNoteBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  GeneralNoteBuilder : public Annotations::PmiAttributeBuilder
        {
            private: GeneralNoteBuilderImpl * m_generalnotebuilder_impl;
            private: friend class  _GeneralNoteBuilderBuilder;
            protected: GeneralNoteBuilder();
            public: ~GeneralNoteBuilder();
            /**Returns  the str title  <br> License requirements : None */
            public: NXString Title
            (
            );
            /**Sets  the str title  <br> License requirements : None */
            public: void SetTitle
            (
                const NXString & title /** title */ 
            );
            /**Returns  the category  <br> License requirements : None */
            public: NXString Category
            (
            );
            /**Sets  the category  <br> License requirements : None */
            public: void SetCategory
            (
                const NXString & category /** category */ 
            );
            /**Returns  the identifier  <br> License requirements : None */
            public: NXString Identifier
            (
            );
            /**Sets  the identifier  <br> License requirements : None */
            public: void SetIdentifier
            (
                const NXString & identifier /** identifier */ 
            );
            /**Returns  the revision  <br> License requirements : None */
            public: NXString Revision
            (
            );
            /**Sets  the revision  <br> License requirements : None */
            public: void SetRevision
            (
                const NXString & revision /** revision */ 
            );
            /** Returns the text  @return   <br> License requirements : None */
            public: std::vector<NXString> GetText
            (
            );
            /** Sets the text  <br> License requirements : None */
            public: void SetText
            (
                const std::vector<NXString> & text /** text */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif

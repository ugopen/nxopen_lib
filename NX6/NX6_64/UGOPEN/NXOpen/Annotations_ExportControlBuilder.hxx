#ifndef NXOpen_ANNOTATIONS_EXPORTCONTROLBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_EXPORTCONTROLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_ExportControlBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Annotations_ExportControlBuilder.hxx>
#include <NXOpen/Annotations_PmiAttributeBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class ExportControlBuilder;
    }
    namespace Annotations
    {
        class PmiAttributeBuilder;
    }
    namespace Annotations
    {
        class _ExportControlBuilderBuilder;
        /** Represents a @link Annotations::ExportControl Annotations::ExportControl@endlink  builder  <br> To create a new instance of this class, use @link Annotations::PmiAttributeCollection::CreateExportControlBuilder Annotations::PmiAttributeCollection::CreateExportControlBuilder@endlink  <br> */
        class NXOPENCPPEXPORT ExportControlBuilder : public Annotations::PmiAttributeBuilder
        {
            private: friend class  _ExportControlBuilderBuilder;
            protected: ExportControlBuilder();
            /**Returns  the title  <br> License requirements : None */
            public: NXString Title
            (
            );
            /**Sets  the title  <br> License requirements : None */
            public: void SetTitle
            (
                const NXString & title /** title */ 
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
            /** Returns the str text  @return   <br> License requirements : None */
            public: std::vector<NXString> GetStringText
            (
            );
            /** Sets the str text  <br> License requirements : None */
            public: void SetStringText
            (
                const std::vector<NXString> & stringText /** stringtext */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
#ifndef NXOpen_ANNOTATIONS_COMPOUNDDATUMREFERENCEBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_COMPOUNDDATUMREFERENCEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_CompoundDatumReferenceBuilder.ja
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
#include <NXOpen/Annotations_CompoundDatumReferenceBuilder.hxx>
#include <NXOpen/Annotations_DatumReferenceBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class CompoundDatumReferenceBuilder;
    }
    namespace Annotations
    {
        class DatumReferenceBuilder;
    }
    class Builder;
    namespace Annotations
    {
        class _CompoundDatumReferenceBuilderBuilder;
        /**
            Represents a @link Annotations::CompoundDatumReferenceBuilder Annotations::CompoundDatumReferenceBuilder@endlink 
             <br> To create a new instance of this class, use @link Annotations::AnnotationManager::CreateCompoundDatumReferenceBuilder Annotations::AnnotationManager::CreateCompoundDatumReferenceBuilder@endlink  <br> */
        class NXOPENCPPEXPORT CompoundDatumReferenceBuilder : public Builder
        {
            private: friend class  _CompoundDatumReferenceBuilderBuilder;
            protected: CompoundDatumReferenceBuilder();
            /** Clear the compound datum reference list  <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void ClearDatumReferenceBuilderList
            (
            );
            /** Add a datum reference entry to the datum reference list  <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void AddDatumReferenceBuilderToList
            (
                NXOpen::Annotations::DatumReferenceBuilder * datumReferenceBuilder /** datum reference builder to add */
            );
            /** Return the entire list of datum references  <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void DatumReferenceList
            (
                std::vector<NXOpen::Annotations::DatumReferenceBuilder *> & datumReferenceBuilders /** datum references */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
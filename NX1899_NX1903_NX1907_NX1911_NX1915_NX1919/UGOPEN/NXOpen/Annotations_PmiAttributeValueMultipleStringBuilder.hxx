#ifndef NXOpen_ANNOTATIONS_PMIATTRIBUTEVALUEMULTIPLESTRINGBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIATTRIBUTEVALUEMULTIPLESTRINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiAttributeValueMultipleStringBuilder.ja
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
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Annotations
    {
        class PmiAttributeValueMultipleStringBuilder;
    }
    class Builder;
    namespace Annotations
    {
        class _PmiAttributeValueMultipleStringBuilderBuilder;
        class PmiAttributeValueMultipleStringBuilderImpl;
        /** Represents a @link NXOpen::Annotations::PmiAttributeValueMultipleString NXOpen::Annotations::PmiAttributeValueMultipleString@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Annotations::PmiAttributeCollection::CreatePmiAttributeValueMultipleStringBuilder  NXOpen::Annotations::PmiAttributeCollection::CreatePmiAttributeValueMultipleStringBuilder @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiAttributeValueMultipleStringBuilder : public NXOpen::Builder
        {
            private: PmiAttributeValueMultipleStringBuilderImpl * m_pmiattributevaluemultiplestringbuilder_impl;
            private: friend class  _PmiAttributeValueMultipleStringBuilderBuilder;
            protected: PmiAttributeValueMultipleStringBuilder();
            public: ~PmiAttributeValueMultipleStringBuilder();
            /** Returns the text  @return  multiple string value
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetMultipleStringValue
            (
            );
            /** Sets the multiple string 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMultipleStringValue
            (
                const std::vector<NXString> & multipleStringValue /** multiple string value*/
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
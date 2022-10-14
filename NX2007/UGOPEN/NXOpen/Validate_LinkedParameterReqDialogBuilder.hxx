#ifndef NXOpen_VALIDATE_LINKEDPARAMETERREQDIALOGBUILDER_HXX_INCLUDED
#define NXOpen_VALIDATE_LINKEDPARAMETERREQDIALOGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Validate_LinkedParameterReqDialogBuilder.ja
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
#include <NXOpen/libnxopencpp_validate_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Validate
    {
        class LinkedParameterReqDialogBuilder;
    }
    class Builder;
    namespace Validate
    {
        class _LinkedParameterReqDialogBuilderBuilder;
        class LinkedParameterReqDialogBuilderImpl;
        /** Represents a Builder class for crating object of linked paramter requirements dialog   <br> To create a new instance of this class, use @link NXOpen::Validate::KeyPerformanceInterfaceCollection::CreateLinkedParameterRequirementsBuilder  NXOpen::Validate::KeyPerformanceInterfaceCollection::CreateLinkedParameterRequirementsBuilder @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_VALIDATEEXPORT  LinkedParameterReqDialogBuilder : public NXOpen::Builder
        {
            private: LinkedParameterReqDialogBuilderImpl * m_linkedparameterreqdialogbuilder_impl;
            private: friend class  _LinkedParameterReqDialogBuilderBuilder;
            protected: LinkedParameterReqDialogBuilder();
            public: ~LinkedParameterReqDialogBuilder();
            /** Appends measurable attribute to builder 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_sdpd_mpm_a (" NX Parameter Management Author") */
            public: void AppendMeasurableAttribute
            (
                const NXString & logicalItemId /** logicalitemid */ ,
                const NXString & logicalItemRevId /** logicalitemrevid */ ,
                const NXString & mesAttrName /** mesattrname */ ,
                const NXString & mesAttrRevId /** mesattrrevid */ 
            );
            /** Appends measurable attribute to builder 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_sdpd_mpm_a (" NX Parameter Management Author") */
            void AppendMeasurableAttribute
            (
                const char * logicalItemId /** logicalitemid */ ,
                const char * logicalItemRevId /** logicalitemrevid */ ,
                const char * mesAttrName /** mesattrname */ ,
                const char * mesAttrRevId /** mesattrrevid */ 
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
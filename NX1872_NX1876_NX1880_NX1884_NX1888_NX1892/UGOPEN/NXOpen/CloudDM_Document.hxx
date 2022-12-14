#ifndef NXOpen_CLOUDDM_DOCUMENT_HXX_INCLUDED
#define NXOpen_CLOUDDM_DOCUMENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CloudDM_Document.ja
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
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_clouddm_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CloudDM
    {
        class Document;
    }
    namespace CloudDM
    {
        class DocumentImpl;

        /// \cond NX_NO_DOC 
        /** JA interface for Cloud document
         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_CLOUDDMEXPORT  Document : public NXOpen::TransientObject
        {
            private: DocumentImpl * m_document_impl;
            /// \cond NX_NO_DOC 
            public: explicit Document(void *ptr);
            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Frees the memory associated with this object. After invocation of this method, the object is no longer valid.  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~Document();

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the document name 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the document date modified 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXString DateModified
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the document owner 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Owner
            (
            );

            /// \endcond 
        }; //lint !e1712 default constructor not defined for class  


        /// \endcond 
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

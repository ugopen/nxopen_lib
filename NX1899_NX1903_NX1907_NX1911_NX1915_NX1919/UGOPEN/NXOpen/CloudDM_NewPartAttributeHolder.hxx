#ifndef NXOpen_CLOUDDM_NEWPARTATTRIBUTEHOLDER_HXX_INCLUDED
#define NXOpen_CLOUDDM_NEWPARTATTRIBUTEHOLDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CloudDM_NewPartAttributeHolder.ja
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
#include <NXOpen/NXObject.hxx>
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
        class NewPartAttributeHolder;
    }
    class NXObject;
    namespace CloudDM
    {
        class _NewPartAttributeHolderBuilder;
        class NewPartAttributeHolderImpl;

        /// \cond NX_NO_DOC 
        /** A builder that holds specific parameters for a part being
                created and to be managed in Cloud  <br> Instances of this class can be accessed through various application specific builders  <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_CLOUDDMEXPORT  NewPartAttributeHolder : public NXOpen::NXObject
        {
            private: NewPartAttributeHolderImpl * m_newpartattributeholder_impl;
            private: friend class  _NewPartAttributeHolderBuilder;
            protected: NewPartAttributeHolder();
            public: ~NewPartAttributeHolder();
        };

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
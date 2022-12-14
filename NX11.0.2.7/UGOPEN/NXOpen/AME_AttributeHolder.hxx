#ifndef NXOpen_AME_ATTRIBUTEHOLDER_HXX_INCLUDED
#define NXOpen_AME_ATTRIBUTEHOLDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_AttributeHolder.ja
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
#include <NXOpen/libameopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace AME
    {
        class AttributeHolder;
    }
    class NXObject;
    namespace AME
    {
        class _AttributeHolderBuilder;
        class AttributeHolderImpl;
        /** JA class for the AttributeHolder object <br> This is an abstract class, and cannot be instantiated.  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  AttributeHolder : public NXOpen::NXObject
        {
            private: AttributeHolderImpl * m_attributeholder_impl;
            private: friend class  _AttributeHolderBuilder;
            protected: AttributeHolder();
            public: ~AttributeHolder();
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

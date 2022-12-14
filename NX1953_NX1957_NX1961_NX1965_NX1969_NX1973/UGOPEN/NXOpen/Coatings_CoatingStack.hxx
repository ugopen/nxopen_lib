#ifndef NXOpen_COATINGS_COATINGSTACK_HXX_INCLUDED
#define NXOpen_COATINGS_COATINGSTACK_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Coatings_CoatingStack.ja
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
#include <NXOpen/libcoatingsopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Coatings
    {
        class CoatingStack;
    }
    class NXObject;
    namespace Coatings
    {
        class _CoatingStackBuilder;
        class CoatingStackImpl;
        /** Represents a Coating Stack class.  <br> To create or edit an instance of this class, use @link NXOpen::Coatings::CoatingStackBuilder  NXOpen::Coatings::CoatingStackBuilder @endlink  <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class COATINGSOPENCPPEXPORT  CoatingStack : public NXOpen::NXObject
        {
            private: CoatingStackImpl * m_coatingstack_impl;
            private: friend class  _CoatingStackBuilder;
            protected: CoatingStack();
            public: ~CoatingStack();
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

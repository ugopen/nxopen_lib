#ifndef NXOpen_FEATURES_SUBDIVISION_PASTECAGEDATA_HXX_INCLUDED
#define NXOpen_FEATURES_SUBDIVISION_PASTECAGEDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Subdivision_PasteCageData.ja
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
#include <NXOpen/GeometricUtilities_TransformerData.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace Subdivision
        {
            class PasteCageData;
        }
    }
    class Builder;
    namespace GeometricUtilities
    {
        class TransformerData;
    }
    namespace Features
    {
        namespace Subdivision
        {
            class _PasteCageDataBuilder;
            class PasteCageDataImpl;
            /** Represents a @link NXOpen::Features::Subdivision::PasteCageData NXOpen::Features::Subdivision::PasteCageData@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreatePasteCageData  NXOpen::Features::Subdivision::SubdivisionBodyCollection::CreatePasteCageData @endlink  <br> 
             <br>  Created in NX11.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  PasteCageData : public NXOpen::Builder
            {
                private: PasteCageDataImpl * m_pastecagedata_impl;
                private: friend class  _PasteCageDataBuilder;
                protected: PasteCageData();
                public: ~PasteCageData();
                /**Returns  the transformation tool. The tool allows user to transform the pasted topology. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::GeometricUtilities::TransformerData * Transformer
                (
                );
                /**Returns  the flag indicating if transformer tool can be moved without transforming the selected cage topology. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: bool CanMoveToolOnly
                (
                );
                /**Sets  the flag indicating if transformer tool can be moved without transforming the selected cage topology. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_subdivision (" NX SUBDIVISION") */
                public: void SetCanMoveToolOnly
                (
                    bool canMove /** canmove */ 
                );
            };
        }
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
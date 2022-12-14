#ifndef NXOpen_FEATURES_SUBDIVISION_SUBDIVISIONBRIDGEFACEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SUBDIVISION_SUBDIVISIONBRIDGEFACEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Subdivision_SubdivisionBridgeFaceBuilder.ja
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
#include <NXOpen/Features_Subdivision_SelectCageObjectData.hxx>
#include <NXOpen/Features_Subdivision_SubdivisionBridgeFaceBuilder.hxx>
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
            class SubdivisionBridgeFaceBuilder;
        }
    }
    class Builder;
    namespace Features
    {
        namespace Subdivision
        {
            class SelectCageObjectData;
        }
    }
    namespace Features
    {
        namespace Subdivision
        {
            class _SubdivisionBridgeFaceBuilderBuilder;
            class SubdivisionBridgeFaceBuilderImpl;
            /** Represents a @link Features::Subdivision::SubdivisionBridgeFaceBuilder Features::Subdivision::SubdivisionBridgeFaceBuilder@endlink  builder.   <br> To create a new instance of this class, use @link Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionBridgeFaceBuilder  Features::Subdivision::SubdivisionBodyCollection::CreateSubdivisionBridgeFaceBuilder @endlink  <br> 
             <br>  Created in NX9.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  SubdivisionBridgeFaceBuilder : public Builder
            {
                private: SubdivisionBridgeFaceBuilderImpl * m_subdivisionbridgefacebuilder_impl;
                private: friend class  _SubdivisionBridgeFaceBuilderBuilder;
                protected: SubdivisionBridgeFaceBuilder();
                public: ~SubdivisionBridgeFaceBuilder();
                /**Returns  the first face set. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::Subdivision::SelectCageObjectData * FaceSet1
                (
                );
                /**Returns  the second face set. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::Subdivision::SelectCageObjectData * FaceSet2
                (
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

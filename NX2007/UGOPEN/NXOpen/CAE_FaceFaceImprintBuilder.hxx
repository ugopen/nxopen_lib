#ifndef NXOpen_CAE_FACEFACEIMPRINTBUILDER_HXX_INCLUDED
#define NXOpen_CAE_FACEFACEIMPRINTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_FaceFaceImprintBuilder.ja
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
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class FaceFaceImprintBuilder;
    }
    class Builder;
    class SelectDisplayableObjectList;
    namespace CAE
    {
        class _FaceFaceImprintBuilderBuilder;
        class FaceFaceImprintBuilderImpl;
        /** Builder for creating Face Face Imprint   <br> To create a new instance of this class, use @link NXOpen::CAE::AbstractionManager::CreateFaceFaceImprintBuilder  NXOpen::CAE::AbstractionManager::CreateFaceFaceImprintBuilder @endlink  <br> 
         <br>  @deprecated Deprecated in NX11.0.0.  Use @link CAE::ImprintBuilder CAE::ImprintBuilder@endlink . <br>  

         <br>  Created in NX11.0.0.  <br>  
        */
        class NX_DEPRECATED("Deprecated in NX11.0.0.  Use CAE::ImprintBuilder.") NXOPENCPP_CAEEXPORT  FaceFaceImprintBuilder : public NXOpen::Builder
        {
            private: FaceFaceImprintBuilderImpl * m_facefaceimprintbuilder_impl;
            private: friend class  _FaceFaceImprintBuilderBuilder;
            protected: FaceFaceImprintBuilder();
            public: ~FaceFaceImprintBuilder();
            /**Returns  the geom selection for intersection curve
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link CAE::ImprintBuilder CAE::ImprintBuilder@endlink . <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use CAE::ImprintBuilder.") NXOpen::SelectDisplayableObjectList * GeomSelection
            (
            );
            /**Returns  the output stitch option 
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link CAE::ImprintBuilder CAE::ImprintBuilder@endlink . <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use CAE::ImprintBuilder.") bool StitchOption
            (
            );
            /**Sets  the output stitch option 
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link CAE::ImprintBuilder CAE::ImprintBuilder@endlink . <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use CAE::ImprintBuilder.") void SetStitchOption
            (
                bool stitchOption /** stitchoption */ 
            );
            /**Returns  the output stitch option 
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link CAE::ImprintBuilder CAE::ImprintBuilder@endlink . <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use CAE::ImprintBuilder.") double ToleranceDistance
            (
            );
            /**Sets  the output stitch option 
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link CAE::ImprintBuilder CAE::ImprintBuilder@endlink . <br>  

             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use CAE::ImprintBuilder.") void SetToleranceDistance
            (
                double dToleranceDistance /** dtolerancedistance */ 
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

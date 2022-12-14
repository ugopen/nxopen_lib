#ifndef NXOpen_ANNOTATIONS_DATUMFEATURESYMBOLBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_DATUMFEATURESYMBOLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_DatumFeatureSymbolBuilder.ja
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
#include <NXOpen/Annotations_LeaderBuilder.hxx>
#include <NXOpen/Annotations_OriginBuilder.hxx>
#include <NXOpen/Annotations_StyleBuilder.hxx>
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
        class DatumFeatureSymbolBuilder;
    }
    namespace Annotations
    {
        class BaseDatum;
    }
    namespace Annotations
    {
        class LeaderBuilder;
    }
    namespace Annotations
    {
        class OriginBuilder;
    }
    namespace Annotations
    {
        class StyleBuilder;
    }
    class Builder;
    namespace Annotations
    {
        class _DatumFeatureSymbolBuilderBuilder;
        class DatumFeatureSymbolBuilderImpl;
        /** Represents a Base Datum Feature Symbol Builder for all types of datum feature symbols  <br> This is an abstract class, and cannot be instantiated.  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  DatumFeatureSymbolBuilder : public NXOpen::Builder
        {
            private: DatumFeatureSymbolBuilderImpl * m_datumfeaturesymbolbuilder_impl;
            private: friend class  _DatumFeatureSymbolBuilderBuilder;
            protected: DatumFeatureSymbolBuilder();
            public: ~DatumFeatureSymbolBuilder();
            /**Returns  the datum feature symbol origin 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::OriginBuilder * Origin
            (
            );
            /**Returns  the @link NXOpen::Annotations::LeaderBuilder NXOpen::Annotations::LeaderBuilder@endlink  for the annotation 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::LeaderBuilder * Leader
            (
            );
            /**Returns  the datum feature string 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Letter
            (
            );
            /**Sets  the datum feature string 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetLetter
            (
                const NXString & datumFeatureLetter /** datumfeatureletter */ 
            );
            /**Sets  the datum feature string 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") OR geometric_tol ("GDT") */
            void SetLetter
            (
                const char * datumFeatureLetter /** datumfeatureletter */ 
            );
            /**Returns  the datum feature  style 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::StyleBuilder * Style
            (
            );
            /** The datum feature symbol is inherited form the given datum feature symbol. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void InheritFrom
            (
                NXOpen::Annotations::BaseDatum * inheritTag /** inherittag */ 
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

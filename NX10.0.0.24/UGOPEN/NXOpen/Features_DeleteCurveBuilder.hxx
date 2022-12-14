#ifndef NXOpen_FEATURES_DELETECURVEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_DELETECURVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_DeleteCurveBuilder.ja
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
#include <NXOpen/Features_DeleteCurveBuilder.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
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
        class DeleteCurveBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class ScCollector;
    namespace Features
    {
        class _DeleteCurveBuilderBuilder;
        class DeleteCurveBuilderImpl;
        /**
            Represents a @link NXOpen::Features::DeleteCurve NXOpen::Features::DeleteCurve@endlink  builder
             <br> To create a new instance of this class, use @link NXOpen::Features::SynchronousCurveCollection::CreateDeleteCurveBuilder  NXOpen::Features::SynchronousCurveCollection::CreateDeleteCurveBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Heal </td> <td> 
         
        1 </td> </tr> 

        </table>  

         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  DeleteCurveBuilder : public NXOpen::Features::FeatureBuilder
        {
            private: DeleteCurveBuilderImpl * m_deletecurvebuilder_impl;
            private: friend class  _DeleteCurveBuilderBuilder;
            protected: DeleteCurveBuilder();
            public: ~DeleteCurveBuilder();
            /**Returns  the section 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * Section
            (
            );
            /**Sets  the section 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetSection
            (
                NXOpen::ScCollector * section /** section */ 
            );
            /**Returns  the heal 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool Heal
            (
            );
            /**Sets  the heal 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetHeal
            (
                bool heal /** heal */ 
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

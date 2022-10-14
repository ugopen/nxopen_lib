#ifndef NXOpen_FEATURES_PAINTPARAMETERSBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_PAINTPARAMETERSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_PaintParametersBuilder.ja
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
#include <NXOpen/Features_PaintParametersBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class PaintParametersBuilder;
    }
    namespace Assemblies
    {
        class SelectComponentList;
    }
    class Builder;
    namespace Features
    {
        class SelectFeature;
    }
    namespace Features
    {
        class SelectFeatureList;
    }
    namespace Features
    {
        class _PaintParametersBuilderBuilder;
        class PaintParametersBuilderImpl;
        /** Represents a paint feature parameters builder. The paint parameters does not
                create a feature, but assists to copy parameters from one feature, called source feature, and 
                apply them to other features, called target features. Features Parameters would be copied from
                the source feature to the target features. If @link PaintParametersBuilder::TargetComponentSelection PaintParametersBuilder::TargetComponentSelection @endlink and @link PaintParametersBuilder::SetTargetComponentSelection PaintParametersBuilder::SetTargetComponentSelection @endlink 
                is set to true, all the features in the components,
                @link PaintParametersBuilder::TargetComponents PaintParametersBuilder::TargetComponents @endlink and @link PaintParametersBuilder::SetTargetComponents PaintParametersBuilder::SetTargetComponents @endlink  that are compatible 
                for parameter painting with the source feature, @link PaintParametersBuilder::SourceFeature PaintParametersBuilder::SourceFeature @endlink and @link PaintParametersBuilder::SetSourceFeature PaintParametersBuilder::SetSourceFeature @endlink 
                would also be set as the target features.
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreatePaintParametersBuilder  Features::FeatureCollection::CreatePaintParametersBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        TargetComponentSelection </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  PaintParametersBuilder : public Builder
        {
            private: PaintParametersBuilderImpl * m_paintparametersbuilder_impl;
            private: friend class  _PaintParametersBuilderBuilder;
            protected: PaintParametersBuilder();
            public: ~PaintParametersBuilder();
            /**Returns  the source feature 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::SelectFeature * SourceFeature
            (
            );
            /**Returns  the target features 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::SelectFeatureList * TargetFeatures
            (
            );
            /**Returns  the target component selection. When this property is set to true, all the features in the components,
                        @link PaintParametersBuilder::TargetComponents PaintParametersBuilder::TargetComponents @endlink and @link PaintParametersBuilder::SetTargetComponents PaintParametersBuilder::SetTargetComponents @endlink  that are compatible 
                        for parameter painting with the source feature, @link PaintParametersBuilder::SourceFeature PaintParametersBuilder::SourceFeature @endlink and @link PaintParametersBuilder::SetSourceFeature PaintParametersBuilder::SetSourceFeature @endlink 
                        would also be set as the target features.
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool TargetComponentSelection
            (
            );
            /**Sets  the target component selection. When this property is set to true, all the features in the components,
                        @link PaintParametersBuilder::TargetComponents PaintParametersBuilder::TargetComponents @endlink and @link PaintParametersBuilder::SetTargetComponents PaintParametersBuilder::SetTargetComponents @endlink  that are compatible 
                        for parameter painting with the source feature, @link PaintParametersBuilder::SourceFeature PaintParametersBuilder::SourceFeature @endlink and @link PaintParametersBuilder::SetSourceFeature PaintParametersBuilder::SetSourceFeature @endlink 
                        would also be set as the target features.
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetTargetComponentSelection
            (
                bool targetComponentSelection /** targetcomponentselection */ 
            );
            /**Returns  the target components that contain the target features. 
                        If @link PaintParametersBuilder::TargetComponentSelection PaintParametersBuilder::TargetComponentSelection @endlink and @link PaintParametersBuilder::SetTargetComponentSelection PaintParametersBuilder::SetTargetComponentSelection @endlink 
                        is set to true, all the features in these components,
                        that are compatible for parameter painting with the source feature, @link PaintParametersBuilder::SourceFeature PaintParametersBuilder::SourceFeature @endlink and @link PaintParametersBuilder::SetSourceFeature PaintParametersBuilder::SetSourceFeature @endlink 
                        would also be set as the target features.
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Assemblies::SelectComponentList * TargetComponents
            (
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
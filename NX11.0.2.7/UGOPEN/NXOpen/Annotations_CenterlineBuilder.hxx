#ifndef NXOpen_ANNOTATIONS_CENTERLINEBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_CENTERLINEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_CenterlineBuilder.ja
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
#include <NXOpen/Annotations_CenterlineBuilder.hxx>
#include <NXOpen/Annotations_BaseSymbolBuilder.hxx>
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
        class CenterlineBuilder;
    }
    namespace Annotations
    {
        class BaseSymbolBuilder;
    }
    namespace Annotations
    {
        class _CenterlineBuilderBuilder;
        class CenterlineBuilderImpl;
        /** Represents a Base Centerline Builder for all types of centerlines  <br> This is an abstract class, and cannot be instantiated.  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  CenterlineBuilder : public NXOpen::Annotations::BaseSymbolBuilder
        {
            private: CenterlineBuilderImpl * m_centerlinebuilder_impl;
            private: friend class  _CenterlineBuilderBuilder;
            protected: CenterlineBuilder();
            public: ~CenterlineBuilder();
            /** Adds extension based on select object index 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void AddExtension
            (
                int index /** Index of the selected object */,
                double defaultValue /** Default extension value */
            );
            /** Removes extension based on select object index 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void RemoveExtension
            (
                int index /** Index of the selected object */
            );
            /** Adds extensions only at ends 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void AddEndExtensions
            (
                double start /** Default start extension value */,
                double end /** Default end extension value */
            );
            /** Removes extensions only at ends 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void RemoveEndExtensions
            (
            );
            /** Modifies extensions based on select object index 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetIndividualExtensions
            (
                int index /** Index of the selected object */,
                double value1 /** New extension value at one end */,
                double value2 /** New extension value at other end */
            );
            /** Modifies end extensions only 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetEndExtensions
            (
                double start /** New extension value at one end */,
                double end /** New extension value at one end */
            );
            /** Returns end extensions only. The first and the last extension of the centerline.  
                    
                    If the builder is a @link NXOpen::Annotations::BoltCircleCenterlineBuilder NXOpen::Annotations::BoltCircleCenterlineBuilder@endlink  or  @link NXOpen::Annotations::CircularCenterlineBuilder NXOpen::Annotations::CircularCenterlineBuilder@endlink  and 
                    @link NXOpen::Annotations::CircleCenterlineSettingsBuilder::IndividualDistance NXOpen::Annotations::CircleCenterlineSettingsBuilder::IndividualDistance@endlink  is false, this will method will return no extensions.
                    
                     @return  Extension values as output
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: std::vector<double> GetEndExtensions
            (
            );
            /** Returns individual extensions. This method is applicable only for @link NXOpen::Annotations::CenterMark NXOpen::Annotations::CenterMark@endlink  and @link NXOpen::Annotations::CircleCenterline NXOpen::Annotations::CircleCenterline@endlink .
                
                        If the builder is a @link NXOpen::Annotations::BoltCircleCenterlineBuilder NXOpen::Annotations::BoltCircleCenterlineBuilder@endlink  or  @link NXOpen::Annotations::CircularCenterlineBuilder NXOpen::Annotations::CircularCenterlineBuilder@endlink  and 
                    @link NXOpen::Annotations::CircleCenterlineSettingsBuilder::IndividualDistance NXOpen::Annotations::CircleCenterlineSettingsBuilder::IndividualDistance@endlink  is false, this will method will return no extensions.    
                
                     @return  Extension values as output
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: std::vector<double> GetAllIndividualExtensions
            (
            );
            /** Sets all individual extensions 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetAllIndividualExtensions
            (
                const std::vector<double> & extensionValues /** Extension values as input*/
            );
            /** Returns all extensions. 
                    
                        If the builder is a @link NXOpen::Annotations::BoltCircleCenterlineBuilder NXOpen::Annotations::BoltCircleCenterlineBuilder@endlink  or  @link NXOpen::Annotations::CircularCenterlineBuilder NXOpen::Annotations::CircularCenterlineBuilder@endlink  and 
                    @link NXOpen::Annotations::CircleCenterlineSettingsBuilder::IndividualDistance NXOpen::Annotations::CircleCenterlineSettingsBuilder::IndividualDistance@endlink  is false, this will method will return no extensions.    
                     @return  Extension values as output
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: std::vector<double> GetAllExtensions
            (
            );
            /** Reset all extensions by the supplied defaultValue 
             <br>  Created in NX6.0.1.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void ResetAllExtensions
            (
                double defaultValue /** New extension value */
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

#ifndef NXOpen_FEATURES_ENLARGEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_ENLARGEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_EnlargeBuilder.ja
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
#include <NXOpen/GeometricUtilities_SurfaceRangeBuilder.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class EnlargeBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class SurfaceRangeBuilder;
    }
    class SelectFace;
    namespace Features
    {
        class _EnlargeBuilderBuilder;
        class EnlargeBuilderImpl;
        /** Represents a @link NXOpen::Features::Enlarge NXOpen::Features::Enlarge@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::Features::FeatureCollection::CreateEnlargeBuilder  NXOpen::Features::FeatureCollection::CreateEnlargeBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        ExtensionType </td> <td> 
         
        Natural </td> </tr> 

        <tr><td> 
         
        IsCopy </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ResizeParameters.AnchorPosition </td> <td> 
         
        Vertex1 </td> </tr> 

        </table>  

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  EnlargeBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** Extension types */
            public: enum ExtensionTypes
            {
                ExtensionTypesLinear/** Linear extension */,
                ExtensionTypesNatural/** Natural extension */
            };

            private: EnlargeBuilderImpl * m_enlargebuilder_impl;
            private: friend class  _EnlargeBuilderBuilder;
            protected: EnlargeBuilder();
            public: ~EnlargeBuilder();
            /**Returns  the face 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_freeform_2 ("advanced freeform modeling") */
            public: NXOpen::SelectFace * Face
            (
            );
            /**Returns  the resize parameters 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_freeform_2 ("advanced freeform modeling") */
            public: NXOpen::GeometricUtilities::SurfaceRangeBuilder * ResizeParameters
            (
            );
            /**Returns  the extension type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_freeform_2 ("advanced freeform modeling") */
            public: NXOpen::Features::EnlargeBuilder::ExtensionTypes ExtensionType
            (
            );
            /**Sets  the extension type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_freeform_2 ("advanced freeform modeling") */
            public: void SetExtensionType
            (
                NXOpen::Features::EnlargeBuilder::ExtensionTypes extensionType /** extensiontype */ 
            );
            /**Returns  whether the enlarge operation is applied to a copy of the face 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_freeform_2 ("advanced freeform modeling") */
            public: bool IsCopy
            (
            );
            /**Sets  whether the enlarge operation is applied to a copy of the face 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_freeform_2 ("advanced freeform modeling") */
            public: void SetCopy
            (
                bool isCopy /** iscopy */ 
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

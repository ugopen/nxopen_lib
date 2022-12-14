#ifndef NXOpen_GEOMETRICANALYSIS_LOCALRADIUSANALYSISBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICANALYSIS_LOCALRADIUSANALYSISBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricAnalysis_LocalRadiusAnalysisBuilder.ja
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
#include <NXOpen/Features_GeometricConstraintDataManager.hxx>
#include <NXOpen/GeometricAnalysis_LocalRadiusAnalysisBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_geometricanalysis_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace GeometricAnalysis
    {
        class LocalRadiusAnalysisBuilder;
    }
    class Builder;
    namespace Features
    {
        class GeometricConstraintDataManager;
    }
    namespace GeometricAnalysis
    {
        class _LocalRadiusAnalysisBuilderBuilder;
        class LocalRadiusAnalysisBuilderImpl;
        /** Represents a @link NXOpen::GeometricAnalysis::LocalRadiusAnalysis NXOpen::GeometricAnalysis::LocalRadiusAnalysis@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateLocalRadiusAnalysisBuilder  NXOpen::GeometricAnalysis::AnalysisObjectCollection::CreateLocalRadiusAnalysisBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        VisibilityCoordinates </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        VisibilityMaxRadius </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        VisibilityMinMaxRadiusTangent </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        VisibilityMinRadius </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        VisibilityRadius </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        VisibilityURadius </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        VisibilityUV </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        VisibilityUVTangent </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        VisibilityVRadius </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICANALYSISEXPORT  LocalRadiusAnalysisBuilder : public NXOpen::Builder
        {
            private: LocalRadiusAnalysisBuilderImpl * m_localradiusanalysisbuilder_impl;
            private: friend class  _LocalRadiusAnalysisBuilderBuilder;
            protected: LocalRadiusAnalysisBuilder();
            public: ~LocalRadiusAnalysisBuilder();
            /**Returns  the selection point 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::GeometricConstraintDataManager * SelectionPoint
            (
            );
            /**Returns  the toggle coordinates 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool VisibilityCoordinates
            (
            );
            /**Sets  the toggle coordinates 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetVisibilityCoordinates
            (
                bool visibilityCoordinates /** visibilitycoordinates */ 
            );
            /**Returns  the toggle uv 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool VisibilityUV
            (
            );
            /**Sets  the toggle uv 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetVisibilityUV
            (
                bool visibilityUV /** visibilityuv */ 
            );
            /**Returns  the toggle min radius tangent 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool VisibilityMinMaxRadiusTangent
            (
            );
            /**Sets  the toggle min radius tangent 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetVisibilityMinMaxRadiusTangent
            (
                bool visibilityMinMaxRadiusTangent /** visibilityminmaxradiustangent */ 
            );
            /**Returns  the toggle max radius tangent 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool VisibilityUVTangent
            (
            );
            /**Sets  the toggle max radius tangent 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetVisibilityUVTangent
            (
                bool visibilityUVTangent /** visibilityuvtangent */ 
            );
            /**Returns  the toggle radius show 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool VisibilityRadius
            (
            );
            /**Sets  the toggle radius show 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetVisibilityRadius
            (
                bool visibilityRadius /** visibilityradius */ 
            );
            /**Returns  the toggle min radius show 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool VisibilityMinRadius
            (
            );
            /**Sets  the toggle min radius show 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetVisibilityMinRadius
            (
                bool visibilityMinRadius /** visibilityminradius */ 
            );
            /**Returns  the toggle max radius show 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool VisibilityMaxRadius
            (
            );
            /**Sets  the toggle max radius show 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetVisibilityMaxRadius
            (
                bool visibilityMaxRadius /** visibilitymaxradius */ 
            );
            /**Returns  the toggle uradius show 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool VisibilityURadius
            (
            );
            /**Sets  the toggle uradius show 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetVisibilityURadius
            (
                bool visibilityURadius /** visibilityuradius */ 
            );
            /**Returns  the toggle vradius show 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool VisibilityVRadius
            (
            );
            /**Sets  the toggle vradius show 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetVisibilityVRadius
            (
                bool visibilityVRadius /** visibilityvradius */ 
            );
            /** TODO: fill in a description for this 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void ButtonOpenInformationWindow
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

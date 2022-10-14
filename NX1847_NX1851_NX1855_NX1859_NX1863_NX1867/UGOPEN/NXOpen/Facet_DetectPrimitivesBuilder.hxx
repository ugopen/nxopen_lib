#ifndef NXOpen_FACET_DETECTPRIMITIVESBUILDER_HXX_INCLUDED
#define NXOpen_FACET_DETECTPRIMITIVESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Facet_DetectPrimitivesBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_facet_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Facet
    {
        class DetectPrimitivesBuilder;
    }
    class Builder;
    class Expression;
    class SelectDisplayableObjectList;
    namespace Facet
    {
        class _DetectPrimitivesBuilderBuilder;
        class DetectPrimitivesBuilderImpl;
        /**
               This class manages the primitive shape detection for a facet body.
             <br> To create a new instance of this class, use @link NXOpen::Facet::FacetModelingCollection::CreateDetectPrimitivesBuilder  NXOpen::Facet::FacetModelingCollection::CreateDetectPrimitivesBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        CurvatureSensitivity </td> <td> 
         
        20 </td> </tr> 

        </table>  

         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_FACETEXPORT  DetectPrimitivesBuilder : public NXOpen::Builder
        {
            private: DetectPrimitivesBuilderImpl * m_detectprimitivesbuilder_impl;
            private: friend class  _DetectPrimitivesBuilderBuilder;
            protected: DetectPrimitivesBuilder();
            public: ~DetectPrimitivesBuilder();
            /**Returns  the facet selection. Inputs to this command can be convergent objects.
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * FacetSelection
            (
            );
            /**Returns  the curvature sensitivity 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: int CurvatureSensitivity
            (
            );
            /**Sets  the curvature sensitivity 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetCurvatureSensitivity
            (
                int curvatureSensitivity /** curvaturesensitivity */ 
            );
            /** Returns the plane color  @return  Array of 3 RGB values, each between 0 and 1 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<double> GetPlaneColor
            (
            );
            /** Sets the plane color 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPlaneColor
            (
                const std::vector<double> & planeColor /** Array of 3 RGB values, each between 0 and 1 */
            );
            /** Returns the sphere color  @return  Array of 3 RGB values, each between 0 and 1 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<double> GetSphereColor
            (
            );
            /** Sets the sphere color 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSphereColor
            (
                const std::vector<double> & sphereColor /** Array of 3 RGB values, each between 0 and 1 */
            );
            /** Returns the cylinder color  @return  Array of 3 RGB values, each between 0 and 1 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<double> GetCylinderColor
            (
            );
            /** Sets the cylinder color 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetCylinderColor
            (
                const std::vector<double> & cylinderColor /** Array of 3 RGB values, each between 0 and 1 */
            );
            /** Returns the cone color  @return  Array of 3 RGB values, each between 0 and 1 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<double> GetConeColor
            (
            );
            /** Sets the cone color 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetConeColor
            (
                const std::vector<double> & coneColor /** Array of 3 RGB values, each between 0 and 1 */
            );
            /** Returns the blend color  @return  Array of 3 RGB values, each between 0 and 1 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<double> GetBlendColor
            (
            );
            /** Sets the blend color 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetBlendColor
            (
                const std::vector<double> & blendColor /** Array of 3 RGB values, each between 0 and 1 */
            );
            /** Returns Other type of color. All non-primitive shapes are classfied as Other type  @return  Array of 3 RGB values, each between 0 and 1 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<double> GetOtherColor
            (
            );
            /** Sets the other color 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetOtherColor
            (
                const std::vector<double> & otherColor /** Array of 3 RGB values, each between 0 and 1 */
            );
            /**Returns  the blend factor 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * BlendFactor
            (
            );
            /** Adjust shape detection result with selectivity angle 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void AdjustShapeBoundary
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
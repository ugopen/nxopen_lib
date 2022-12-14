#ifndef NXOpen_FACET_SUBDIVIDEFACETBODYBUILDER_HXX_INCLUDED
#define NXOpen_FACET_SUBDIVIDEFACETBODYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Facet_SubdivideFacetBodyBuilder.ja
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
#include <NXOpen/Facet_SubdivideFacetBodyBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/ObjectList.hxx>
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
        class SubdivideFacetBodyBuilder;
    }
    class Builder;
    namespace Facet
    {
        class SelectFacetedBodyList;
    }
    namespace GeometricUtilities
    {
        class BoundaryDefinitionBuilderList;
    }
    class SelectDisplayableObjectList;
    namespace Facet
    {
        class _SubdivideFacetBodyBuilderBuilder;
        class SubdivideFacetBodyBuilderImpl;
        /** This class provides functionality to subdivide the polygons to increase the density of the facet bodies.
            Subdividing Polygons creates a smoother representation. <br> To create a new instance of this class, use @link NXOpen::Facet::FacetedBodyCollection::CreateSubdivideFacetBodyBuilder  NXOpen::Facet::FacetedBodyCollection::CreateSubdivideFacetBodyBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        AngleThreshold </td> <td> 
         
        30 </td> </tr> 

        <tr><td> 
         
        EdgeLength </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        InterpolationMethod </td> <td> 
         
        Cubic </td> </tr> 

        <tr><td> 
         
        IsEditCopy </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        IsOptimize </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        SubdivisionMethod </td> <td> 
         
        SubdivideIntoFour </td> </tr> 

        </table>  

         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_FACETEXPORT  SubdivideFacetBodyBuilder : public NXOpen::Builder
        {
            /** Subdivision methods */
            public: enum SubdivisionMethodType
            {
                SubdivisionMethodTypeSubdivideIntoFour/** Subdivides the polygons into four sub triangles. The original mesh structure remains.*/,
                SubdivisionMethodTypeSubdividebyEdgeLength/** Subdivides the polygons to a specified edge length. The original mesh structure disappears. */
            };

            /** Subdivision interpolation methods */
            public: enum InterpolationMethodType
            {
                InterpolationMethodTypeLinear/** In the linear option the sub-triangles are coplanar to the original triangle. Shape resolution remains untouched. */,
                InterpolationMethodTypeCubic/** In the cubic option the sub-triangles are fitted cubic to the surrounding triangles. Shape resolution increases. */
            };

            private: SubdivideFacetBodyBuilderImpl * m_subdividefacetbodybuilder_impl;
            private: friend class  _SubdivideFacetBodyBuilderBuilder;
            protected: SubdivideFacetBodyBuilder();
            public: ~SubdivideFacetBodyBuilder();
            /**Returns  the facet bodies to be subdivided
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Facet::SubdivideFacetBodyBuilder::Bodies NXOpen::Facet::SubdivideFacetBodyBuilder::Bodies@endlink  instead. <br>  

             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::Facet::SubdivideFacetBodyBuilder::Bodies instead.") NXOpen::Facet::SelectFacetedBodyList * FacetBodies
            (
            );
            /**Returns  the facet bodies to be subdivided. Inputs to this command can be convergent objects. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * Bodies
            (
            );
            /**Returns  an optional list of regions on the facet bodies to be subdivided. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::BoundaryDefinitionBuilderList * RegionList
            (
            );
            /**Returns  the subdivision method 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Facet::SubdivideFacetBodyBuilder::SubdivisionMethodType SubdivisionMethod
            (
            );
            /**Sets  the subdivision method 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetSubdivisionMethod
            (
                NXOpen::Facet::SubdivideFacetBodyBuilder::SubdivisionMethodType subdivisionMethod /** subdivisionmethod */ 
            );
            /**Returns  the interpolation method 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Facet::SubdivideFacetBodyBuilder::InterpolationMethodType InterpolationMethod
            (
            );
            /**Sets  the interpolation method 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetInterpolationMethod
            (
                NXOpen::Facet::SubdivideFacetBodyBuilder::InterpolationMethodType interpolationMethod /** interpolationmethod */ 
            );
            /**Returns  the angular tolerance to detect sharp edges to be kept. Cubic interpolation can not interpolate over an edge of two triangles whose normals differ more than the specified value. Same applies to re-meshing. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double AngleThreshold
            (
            );
            /**Sets  the angular tolerance to detect sharp edges to be kept. Cubic interpolation can not interpolate over an edge of two triangles whose normals differ more than the specified value. Same applies to re-meshing. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetAngleThreshold
            (
                double angleThreshold /** anglethreshold */ 
            );
            /**Returns  the value indicating length of the edge of the polygons to be subdivided.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: double EdgeLength
            (
            );
            /**Sets  the value indicating length of the edge of the polygons to be subdivided.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetEdgeLength
            (
                double edgeLength /** edgelength */ 
            );
            /**Returns  the value indicating whether to perform a decimation step after the subdivision.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool IsOptimize
            (
            );
            /**Sets  the value indicating whether to perform a decimation step after the subdivision.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetOptimize
            (
                bool isOptimize /** isoptimize */ 
            );
            /**Returns  the value indicating if a copy of the facet body to be subdivided without altering the original. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool IsEditCopy
            (
            );
            /**Sets  the value indicating if a copy of the facet body to be subdivided without altering the original. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetEditCopy
            (
                bool isEditCopy /** iseditcopy */ 
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

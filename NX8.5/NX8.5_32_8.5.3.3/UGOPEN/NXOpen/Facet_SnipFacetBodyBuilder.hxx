#ifndef NXOpen_FACET_SNIPFACETBODYBUILDER_HXX_INCLUDED
#define NXOpen_FACET_SNIPFACETBODYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Facet_SnipFacetBodyBuilder.ja
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
#include <NXOpen/Facet_SnipFacetBodyBuilder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/ugmath.hxx>
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
        class SnipFacetBodyBuilder;
    }
    class Builder;
    class Direction;
    namespace Facet
    {
        class SelectFacetedBodyList;
    }
    namespace GeometricUtilities
    {
        class BoundaryDefinitionBuilderList;
    }
    class Plane;
    class SectionList;
    class SelectPointList;
    namespace Facet
    {
        class _SnipFacetBodyBuilderBuilder;
        class SnipFacetBodyBuilderImpl;
        /** Represents a SnipFacetBody builder  <br> To create a new instance of this class, use @link Facet::FacetedBodyCollection::CreateSnipFacetBodyBuilder  Facet::FacetedBodyCollection::CreateSnipFacetBodyBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        AlongDirection </td> <td> 
         
        ViewDirection </td> </tr> 

        <tr><td> 
         
        BoundaryFacetTreatmentType </td> <td> 
         
        SnipFacets </td> </tr> 

        <tr><td> 
         
        CanDivide </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        IsEditCopy </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        IsSnipNearFacets </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_FACETEXPORT  SnipFacetBodyBuilder : public Builder
        {
            /** Snip method */
            public: enum Types
            {
                TypesSnipRegion/** Snip by region */,
                TypesSnipWithCurves/** Snip with curves */,
                TypesSnipAtPlane/** Snip at plane */
            };

            /** Snipping direction when snipping type "by profiles"  */
            public: enum DirectionType
            {
                DirectionTypeViewDirection/** Snip along view direction */,
                DirectionTypeFacetNormal/** Snip along facet normal */,
                DirectionTypeAlongVector/** Snip along specified vector */
            };

            /** Boundary facet treatment type: */
            public: enum BoundaryFacetTreatmentMethod
            {
                BoundaryFacetTreatmentMethodSnipFacets/** Snip scarred facets by the border */,
                BoundaryFacetTreatmentMethodRemoveFacets/** Remove scarred facets */
            };

            private: SnipFacetBodyBuilderImpl * m_snipfacetbodybuilder_impl;
            private: friend class  _SnipFacetBodyBuilderBuilder;
            protected: SnipFacetBodyBuilder();
            public: ~SnipFacetBodyBuilder();
            /**Returns  the facet bodies to snip 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Facet::SelectFacetedBodyList * FacetBodies
            (
            );
            /**Returns  the value indicating if only facets near to the viewer to be snipped 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool IsSnipNearFacets
            (
            );
            /**Sets  the value indicating if only facets near to the viewer to be snipped 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetSnipNearFacets
            (
                bool isSnipNearFacets /** issnipnearfacets */ 
            );
            /**Returns  the list of regions to snip 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::BoundaryDefinitionBuilderList * RegionList
            (
            );
            /**Returns  the list of snipping profiles 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SectionList * ProfileList
            (
            );
            /**Returns  the direction in which snipping profiles are projected on the facet bodies  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Facet::SnipFacetBodyBuilder::DirectionType AlongDirection
            (
            );
            /**Sets  the direction in which snipping profiles are projected on the facet bodies  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetAlongDirection
            (
                NXOpen::Facet::SnipFacetBodyBuilder::DirectionType alongDirection /** alongdirection */ 
            );
            /**Returns  the projection vector 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * ProjectionVector
            (
            );
            /**Sets  the projection vector 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetProjectionVector
            (
                NXOpen::Direction * projectionVector /** projectionvector */ 
            );
            /**Returns  the view direction 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Vector3d ViewDirection
            (
            );
            /**Sets  the view direction 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetViewDirection
            (
                const NXOpen::Vector3d & viewDirection /** viewdirection */ 
            );
            /**Returns  the snipping plane 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Plane * Plane
            (
            );
            /**Sets  the snipping plane 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetPlane
            (
                NXOpen::Plane * plane /** plane */ 
            );
            /**Returns  the point indicating the portion of the facet body with respect to specified region to be snipped. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectPointList * RegionPoint
            (
            );
            /**Returns  the value indicating if facet body is to be divided 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool CanDivide
            (
            );
            /**Sets  the value indicating if facet body is to be divided 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetCanDivide
            (
                bool canDivide /** candivide */ 
            );
            /** Switch the region to be snipped indicated by the region point. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SwitchRegion
            (
            );
            /**Returns  the value indicating if a copy of the facet body to be snipped without altering the original 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool IsEditCopy
            (
            );
            /**Sets  the value indicating if a copy of the facet body to be snipped without altering the original 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetEditCopy
            (
                bool isEditCopy /** iseditcopy */ 
            );
            /**Returns  the boundary facet treatment type 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Facet::SnipFacetBodyBuilder::BoundaryFacetTreatmentMethod BoundaryFacetTreatmentType
            (
            );
            /**Sets  the boundary facet treatment type 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetBoundaryFacetTreatmentType
            (
                NXOpen::Facet::SnipFacetBodyBuilder::BoundaryFacetTreatmentMethod boundaryFacetTreatmentType /** boundaryfacettreatmenttype */ 
            );
            /**Returns  the snipping method accessor
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Facet::SnipFacetBodyBuilder::Types Type
            (
            );
            /**Sets  the snipping method accessor
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetType
            (
                NXOpen::Facet::SnipFacetBodyBuilder::Types type /** type */ 
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

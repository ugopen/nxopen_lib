#ifndef NXOpen_FACET_MERGEFACETBODYBUILDER_HXX_INCLUDED
#define NXOpen_FACET_MERGEFACETBODYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Facet_MergeFacetBodyBuilder.ja
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
#include <NXOpen/SelectObject.hxx>
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
        class MergeFacetBodyBuilder;
    }
    class Builder;
    class Expression;
    namespace Facet
    {
        class SelectFacetedBody;
    }
    namespace Facet
    {
        class _MergeFacetBodyBuilderBuilder;
        class MergeFacetBodyBuilderImpl;
        /**
            Represents a @link NXOpen::Facet::MergeFacetBodyBuilder NXOpen::Facet::MergeFacetBodyBuilder@endlink 
            It merges two overlapping NX facet bodies. It returns a new mergered NX facet body. The two input bodies
            can be kept, deleted or hidden.
             <br> To create a new instance of this class, use @link NXOpen::Facet::FacetedBodyCollection::CreateMergeFacetBodyBuilder  NXOpen::Facet::FacetedBodyCollection::CreateMergeFacetBodyBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        ChordHeight.Value </td> <td> 
         
        0.05 (millimeters part), 0.005 (inches part) </td> </tr> 

        <tr><td> 
         
        EdgeLength.Value </td> <td> 
         
        1 (millimeters part), 0.1 (inches part) </td> </tr> 

        <tr><td> 
         
        InputStatus </td> <td> 
         
        Keep </td> </tr> 

        </table>  

         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_FACETEXPORT  MergeFacetBodyBuilder : public NXOpen::Builder
        {
            /** Represents the option for keeping, deleting or hiding input two facet bodies after builder committing */
            public: enum Input
            {
                InputKeep/** Keep the input facet body after builder committing */,
                InputDelete/** Delete the input facet body after builder committing */,
                InputHide/** Hide the input facet body after builder committing */
            };

            private: MergeFacetBodyBuilderImpl * m_mergefacetbodybuilder_impl;
            private: friend class  _MergeFacetBodyBuilderBuilder;
            protected: MergeFacetBodyBuilder();
            public: ~MergeFacetBodyBuilder();
            /**Returns  the first NX facet body to be merged 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Facet::SelectFacetedBody * FacetBodyOne
            (
            );
            /**Returns  the second NX facet body to be merged 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Facet::SelectFacetedBody * FacetBodyTwo
            (
            );
            /**Returns  the chord height to control the size of new facets 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ChordHeight
            (
            );
            /**Returns  the edge length to control the size of new facets 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * EdgeLength
            (
            );
            /**Returns  the option to specify how to deal with the input two facet bodies: keep, delete or hide 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Facet::MergeFacetBodyBuilder::Input InputStatus
            (
            );
            /**Sets  the option to specify how to deal with the input two facet bodies: keep, delete or hide 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : studio_free_form ("STUDIO FREE FORM") OR die_engineering ("DIE ENGINEERING") */
            public: void SetInputStatus
            (
                NXOpen::Facet::MergeFacetBodyBuilder::Input inputStatus /** inputstatus */ 
            );
            /**Returns  the distance tolerance used in the merge facet body feature 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: double DistanceTolerance
            (
            );
            /**Sets  the distance tolerance used in the merge facet body feature 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: void SetDistanceTolerance
            (
                double distanceTolerance /** distancetolerance */ 
            );
            /**Returns  the angle tolerance used in the merge facet body feature 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: double AngleTolerance
            (
            );
            /**Sets  the angle tolerance used in the merge facet body feature 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: void SetAngleTolerance
            (
                double angleTolerance /** angletolerance */ 
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

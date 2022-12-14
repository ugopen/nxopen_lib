#ifndef NXOpen_GEOMETRICUTILITIES_COLORCODEDREGIONBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_COLORCODEDREGIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_ColorCodedRegionBuilder.ja
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
#include <NXOpen/GeometricUtilities_ColorCodedRegionBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_geometricutilities_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace GeometricUtilities
    {
        class ColorCodedRegionBuilder;
    }
    namespace Facet
    {
        class FacetedBody;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricUtilities
    {
        class _ColorCodedRegionBuilderBuilder;
        class ColorCodedRegionBuilderImpl;
        /** Represents a @link NXOpen::GeometricUtilities::ColorCodedRegionBuilder NXOpen::GeometricUtilities::ColorCodedRegionBuilder@endlink .
                The Color Coded Region block allows the user to select color coded regions of facet bodies .
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  ColorCodedRegionBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: ColorCodedRegionBuilderImpl * m_colorcodedregionbuilder_impl;
            private: friend class  _ColorCodedRegionBuilderBuilder;
            protected: ColorCodedRegionBuilder();
            public: ~ColorCodedRegionBuilder();
            /**Returns  the option to select all regions of the same color 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool AllSameColor
            (
            );
            /**Sets  the option to select all regions of the same color 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR studio_free_form ("STUDIO FREE FORM") */
            public: void SetAllSameColor
            (
                bool allSameColor /** allsamecolor */ 
            );
            /** Build Colored Region 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void BuildColoredRegion
            (
                NXOpen::Facet::FacetedBody * facetBody /** target facet body */,
                int facetId /** picked facet ID */,
                int localVertexId /** loccal vertex id of the triangle */
            );
            /** Deselect Colored Region 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void DeselectColoredRegion
            (
                int objIndex /** colored object to be deselected */
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful 
             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: virtual bool Validate
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

#ifndef NXOpen_TOOLING_MWSEARCHREGIONBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_MWSEARCHREGIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_MWSearchRegionBuilder.ja
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
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/Tooling_MWSearchRegionBuilder.hxx>
#include <NXOpen/libnxopencpp_tooling_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Tooling
    {
        class MWSearchRegionBuilder;
    }
    class Builder;
    class NXColor;
    class SelectEdgeList;
    class SelectFaceList;
    namespace Tooling
    {
        class _MWSearchRegionBuilderBuilder;
        class MWSearchRegionBuilderImpl;
        /** The Search Region builder is for defining a region by searching the region faces given a set of seed faces and boundary edges.  <br> To create a new instance of this class, use @link NXOpen::Tooling::MWSearchRegionCollection::CreateBuilder  NXOpen::Tooling::MWSearchRegionCollection::CreateBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        HighlightConnectingFacesScale </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        MaximumNumberOfFacesSearched </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        TranslucencyAsBoundaryFacesToggle </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  MWSearchRegionBuilder : public NXOpen::Builder
        {
            private: MWSearchRegionBuilderImpl * m_mwsearchregionbuilder_impl;
            private: friend class  _MWSearchRegionBuilderBuilder;
            protected: MWSearchRegionBuilder();
            public: ~MWSearchRegionBuilder();
            /**Returns  the select seed faces 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectFaceList * SelectSeedFaces
            (
            );
            /**Returns  the select boundary edges 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectEdgeList * SelectBoundaryEdges
            (
            );
            /**Returns  the select boundary faces 
             <br>  Created in NX6.0.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectFaceList * SelectBoundaryFaces
            (
            );
            /**Returns  the highlight connecting faces scale 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: int HighlightConnectingFacesScale
            (
            );
            /**Sets  the highlight connecting faces scale 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetHighlightConnectingFacesScale
            (
                int highlightConnectingFacesScale /** highlightconnectingfacesscale */ 
            );
            /**Returns  the translucency as boundary faces toggle 
             <br>  Created in NX6.0.3.  <br>  
             <br> License requirements : None */
            public: bool TranslucencyAsBoundaryFacesToggle
            (
            );
            /**Sets  the translucency as boundary faces toggle 
             <br>  Created in NX6.0.3.  <br>  
             <br> License requirements : None */
            public: void SetTranslucencyAsBoundaryFacesToggle
            (
                bool translucencyAsBoundaryFacesToggle /** translucencyasboundaryfacestoggle */ 
            );
            /**Returns  the option to use different colors as boundary faces 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool DifferentColorsAsBoundaryFacesOption
            (
            );
            /**Sets  the option to use different colors as boundary faces 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetDifferentColorsAsBoundaryFacesOption
            (
                bool differentColorsAsBoundaryFacesOption /** differentcolorsasboundaryfacesoption */ 
            );
            /**Returns  the maximum number of faces to be searched 
             <br>  Created in NX6.0.3.  <br>  
             <br> License requirements : None */
            public: int MaximumNumberOfFacesSearched
            (
            );
            /**Sets  the maximum number of faces to be searched 
             <br>  Created in NX6.0.3.  <br>  
             <br> License requirements : None */
            public: void SetMaximumNumberOfFacesSearched
            (
                int maximumNumberOfFacesSearched /** maximumnumberoffacessearched */ 
            );
            /**Returns  the color to be applied to the selected boundary faces 
             <br>  Created in NX6.0.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * BoundaryFacesColor
            (
            );
            /**Sets  the color to be applied to the selected boundary faces 
             <br>  Created in NX6.0.3.  <br>  
             <br> License requirements : None */
            public: void SetBoundaryFacesColor
            (
                NXOpen::NXColor * boundaryFacesColor /** boundaryfacescolor */ 
            );
            /** Change the color of the selected boundary using the specified color 
             <br>  Created in NX6.0.3.  <br>  
             <br> License requirements : None */
            public: void ChangeBoundaryFacesColor
            (
            );
            /** Initialize the data for the Search Region builder 
             <br>  Created in NX6.0.3.  <br>  
             <br> License requirements : None */
            public: void InitBuilderData
            (
            );
            /** Display the product body in the part file 
             <br>  Created in NX6.0.3.  <br>  
             <br> License requirements : None */
            public: void DisplayProductBody
            (
            );
            /** Turn off all parting lines 
             <br>  Created in NX6.0.3.  <br>  
             <br> License requirements : None */
            public: void TurnOffAllPartingLines
            (
            );
            /** Update the region with the new region faces and seed faces 
             <br>  Created in NX6.0.3.  <br>  
             <br> License requirements : None */
            public: void UpdateRegion
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

#ifndef NXOpen_DRAWINGS_SHIPDRAFTINGVIEWLINESBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_SHIPDRAFTINGVIEWLINESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_ShipDraftingViewLinesBuilder.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/Preferences_ViewStylePreferencesData.hxx>
#include <NXOpen/libnxopencpp_drawings_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Drawings
    {
        class ShipDraftingViewLinesBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class NXColor;
    namespace Drawings
    {
        class _ShipDraftingViewLinesBuilderBuilder;
        class ShipDraftingViewLinesBuilderImpl;
        /** Represents a ship view lines block  <br> To create a new instance of this class, use @link NXOpen::Drawings::ViewStyleBuilder::CreateShipDraftingViewLinesBuilder  NXOpen::Drawings::ViewStyleBuilder::CreateShipDraftingViewLinesBuilder @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  ShipDraftingViewLinesBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: ShipDraftingViewLinesBuilderImpl * m_shipdraftingviewlinesbuilder_impl;
            private: friend class  _ShipDraftingViewLinesBuilderBuilder;
            protected: ShipDraftingViewLinesBuilder();
            public: ~ShipDraftingViewLinesBuilder();
            /**Returns  the single line representation toggle 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool SingleLineRepresentation
            (
            );
            /**Sets  the single line representation toggle 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetSingleLineRepresentation
            (
                bool singleLineRepresentation /** singlelinerepresentation */ 
            );
            /**Returns  the non-sectioned visible color on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * NonSectionedVisibleColor
            (
            );
            /**Sets  the non-sectioned visible color on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetNonSectionedVisibleColor
            (
                NXOpen::NXColor * nonSectionedVisibleColor /** Sets a new non-sectined visible color on the ship drafting view lines sub-builder */
            );
            /**Returns  the non-sectioned visible font on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::Font NonSectionedVisibleFont
            (
            );
            /**Sets  the non-sectioned visible font on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetNonSectionedVisibleFont
            (
                NXOpen::Preferences::Font nonSectionedVisibleFont /** Sets a new non-sectioned visible font on the ship drafting view lines sub-builder */
            );
            /**Returns  the non-sectioned visible width on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::Width NonSectionedVisibleWidth
            (
            );
            /**Sets  the non-sectioned visible width on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetNonSectionedVisibleWidth
            (
                NXOpen::Preferences::Width nonSectionedVisibleWidth /** Sets a new non-sectioned visible width on the ship drafting view lines sub-builder */
            );
            /**Returns  the non-sectioned hidden color on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * NonSectionedHiddenColor
            (
            );
            /**Sets  the non-sectioned hidden color on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetNonSectionedHiddenColor
            (
                NXOpen::NXColor * nonSectionedHiddenColor /** Sets a new non-sectined hidden color on the ship drafting view lines sub-builder */
            );
            /**Returns  the non-sectioned hidden font on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::Font NonSectionedHiddenFont
            (
            );
            /**Sets  the non-sectioned hidden font on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetNonSectionedHiddenFont
            (
                NXOpen::Preferences::Font nonSectionedHiddenFont /** Sets a new non-sectioned hidden font on the ship drafting view lines sub-builder */
            );
            /**Returns  the non-sectioned hidden width on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::Width NonSectionedHiddenWidth
            (
            );
            /**Sets  the non-sectioned hidden width on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetNonSectionedHiddenWidth
            (
                NXOpen::Preferences::Width nonSectionedHiddenWidth /** Sets a new non-sectioned hidden width on the ship drafting view lines sub-builder */
            );
            /**Returns  the sectioned visible color on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * SectionedVisibleColor
            (
            );
            /**Sets  the sectioned visible color on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetSectionedVisibleColor
            (
                NXOpen::NXColor * sectionedVisibleColor /** Sets a new sectined visible color on the ship drafting view lines sub-builder */
            );
            /**Returns  the sectioned visible font on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::Font SectionedVisibleFont
            (
            );
            /**Sets  the sectioned visible font on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetSectionedVisibleFont
            (
                NXOpen::Preferences::Font sectionedVisibleFont /** Sets a new sectioned visible font on the ship drafting view lines sub-builder */
            );
            /**Returns  the sectioned visible width on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::Width SectionedVisibleWidth
            (
            );
            /**Sets  the sectioned visible width on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetSectionedVisibleWidth
            (
                NXOpen::Preferences::Width sectionedVisibleWidth /** Sets a new sectioned visible width on the ship drafting view lines sub-builder */
            );
            /**Returns  the sectioned hidden color on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * SectionedHiddenColor
            (
            );
            /**Sets  the sectioned hidden color on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetSectionedHiddenColor
            (
                NXOpen::NXColor * sectionedHiddenColor /** Sets a new sectined hidden color on the ship drafting view lines sub-builder */
            );
            /**Returns  the sectioned hidden font on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::Font SectionedHiddenFont
            (
            );
            /**Sets  the sectioned hidden font on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetSectionedHiddenFont
            (
                NXOpen::Preferences::Font sectionedHiddenFont /** Sets a new sectioned hidden font on the ship drafting view lines sub-builder */
            );
            /**Returns  the sectioned hidden width on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::Width SectionedHiddenWidth
            (
            );
            /**Sets  the sectioned hidden width on the Ship Structure Lines 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetSectionedHiddenWidth
            (
                NXOpen::Preferences::Width sectionedHiddenWidth /** Sets a new sectioned hidden width on the ship drafting view lines sub-builder */
            );
            /**Returns  the Secondary non-sectioned visible color on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * NonSectionedSecondaryVisibleColor
            (
            );
            /**Sets  the Secondary non-sectioned visible color on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetNonSectionedSecondaryVisibleColor
            (
                NXOpen::NXColor * nonSectionedSecondaryVisibleColor /** Sets a new non-sectined visible color on the ship drafting view lines sub-builder */
            );
            /**Returns  the Secondary non-sectioned visible font on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::Font NonSectionedSecondaryVisibleFont
            (
            );
            /**Sets  the Secondary non-sectioned visible font on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetNonSectionedSecondaryVisibleFont
            (
                NXOpen::Preferences::Font nonSectionedSecondaryVisibleFont /** Sets a new non-sectioned visible font on the ship drafting view lines sub-builder */
            );
            /**Returns  the Secondary non-sectioned visible width on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::Width NonSectionedSecondaryVisibleWidth
            (
            );
            /**Sets  the Secondary non-sectioned visible width on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetNonSectionedSecondaryVisibleWidth
            (
                NXOpen::Preferences::Width nonSectionedSecondaryVisibleWidth /** Sets a new non-sectioned visible width on the ship drafting view lines sub-builder */
            );
            /**Returns  the Secondary non-sectioned hidden color on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * NonSectionedSecondaryHiddenColor
            (
            );
            /**Sets  the Secondary non-sectioned hidden color on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetNonSectionedSecondaryHiddenColor
            (
                NXOpen::NXColor * nonSectionedSecondaryHiddenColor /** Sets a new non-sectined hidden color on the ship drafting view lines sub-builder */
            );
            /**Returns  the Secondary non-sectioned hidden font on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::Font NonSectionedSecondaryHiddenFont
            (
            );
            /**Sets  the Secondary non-sectioned hidden font on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetNonSectionedSecondaryHiddenFont
            (
                NXOpen::Preferences::Font nonSectionedSecondaryHiddenFont /** Sets a new non-sectioned hidden font on the ship drafting view lines sub-builder */
            );
            /**Returns  the Secondary non-sectioned hidden width on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::Width NonSectionedSecondaryHiddenWidth
            (
            );
            /**Sets  the Secondary non-sectioned hidden width on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetNonSectionedSecondaryHiddenWidth
            (
                NXOpen::Preferences::Width nonSectionedSecondaryHiddenWidth /** Sets a new non-sectioned hidden width on the ship drafting view lines sub-builder */
            );
            /**Returns  the Secondary sectioned visible color on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * SectionedSecondaryVisibleColor
            (
            );
            /**Sets  the Secondary sectioned visible color on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetSectionedSecondaryVisibleColor
            (
                NXOpen::NXColor * sectionedSecondaryVisibleColor /** Sets a new sectined visible color on the ship drafting view lines sub-builder */
            );
            /**Returns  the Secondary sectioned visible font on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::Font SectionedSecondaryVisibleFont
            (
            );
            /**Sets  the Secondary sectioned visible font on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetSectionedSecondaryVisibleFont
            (
                NXOpen::Preferences::Font sectionedSecondaryVisibleFont /** Sets a new sectioned visible font on the ship drafting view lines sub-builder */
            );
            /**Returns  the Secondary sectioned visible width on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::Width SectionedSecondaryVisibleWidth
            (
            );
            /**Sets  the Secondary sectioned visible width on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetSectionedSecondaryVisibleWidth
            (
                NXOpen::Preferences::Width sectionedSecondaryVisibleWidth /** Sets a new sectioned visible width on the ship drafting view lines sub-builder */
            );
            /**Returns  the Secondary sectioned hidden color on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * SectionedSecondaryHiddenColor
            (
            );
            /**Sets  the Secondary sectioned hidden color on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetSectionedSecondaryHiddenColor
            (
                NXOpen::NXColor * sectionedSecondaryHiddenColor /** Sets a new sectined hidden color on the ship drafting view lines sub-builder */
            );
            /**Returns  the Secondary sectioned hidden font on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::Font SectionedSecondaryHiddenFont
            (
            );
            /**Sets  the Secondary sectioned hidden font on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetSectionedSecondaryHiddenFont
            (
                NXOpen::Preferences::Font sectionedSecondaryHiddenFont /** Sets a new sectioned hidden font on the ship drafting view lines sub-builder */
            );
            /**Returns  the Secondary sectioned hidden width on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Preferences::Width SectionedSecondaryHiddenWidth
            (
            );
            /**Sets  the Secondary sectioned hidden width on the Ship Structure Lines 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
            public: void SetSectionedSecondaryHiddenWidth
            (
                NXOpen::Preferences::Width sectionedSecondaryHiddenWidth /** Sets a new sectioned hidden width on the ship drafting view lines sub-builder */
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
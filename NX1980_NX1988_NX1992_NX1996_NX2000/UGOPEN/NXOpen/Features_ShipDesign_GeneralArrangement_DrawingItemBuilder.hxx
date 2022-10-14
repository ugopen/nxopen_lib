#ifndef NXOpen_FEATURES_SHIPDESIGN_GENERALARRANGEMENT_DRAWINGITEMBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_GENERALARRANGEMENT_DRAWINGITEMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_GeneralArrangement_DrawingItemBuilder.ja
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
        namespace ShipDesign
        {
            namespace GeneralArrangement
            {
                class DrawingItemBuilder;
            }
        }
    }
    class Builder;
    namespace Features
    {
        namespace ShipDesign
        {
            namespace GeneralArrangement
            {
                class _DrawingItemBuilderBuilder;
                class DrawingItemBuilderImpl;
                /** This builder allows you to define the general arrangement drawing item information. 
                            It represents @link NXOpen::Features::ShipDesign::GeneralArrangement::DrawingItemBuilder NXOpen::Features::ShipDesign::GeneralArrangement::DrawingItemBuilder@endlink .
                            This builder won't create General Arrangement View and just returns NULL. 
                             <br> To obtain an instance of this class use @link NXOpen::Features::ShipDesign::GeneralArrangement::DrawingAutomationBuilder::CreateDrawingViewItemBuilder NXOpen::Features::ShipDesign::GeneralArrangement::DrawingAutomationBuilder::CreateDrawingViewItemBuilder@endlink  or @link NXOpen::Features::ShipDesign::GeneralArrangement::DrawingAutomationBuilder::CreateDrawingTableItemBuilder NXOpen::Features::ShipDesign::GeneralArrangement::DrawingAutomationBuilder::CreateDrawingTableItemBuilder@endlink .  <br> 
                 <br>  Created in NX12.0.2.  <br>  
                */
                class NXOPENCPP_FEATURESEXPORT  DrawingItemBuilder : public NXOpen::Builder
                {
                    private: DrawingItemBuilderImpl * m_drawingitembuilder_impl;
                    private: friend class  _DrawingItemBuilderBuilder;
                    protected: DrawingItemBuilder();
                    public: ~DrawingItemBuilder();
                    /**Returns  the create item 
                     <br>  Created in NX12.0.2.  <br>  
                     <br> License requirements : None */
                    public: bool CreateItem
                    (
                    );
                    /**Sets  the create item 
                     <br>  Created in NX12.0.2.  <br>  
                     <br> License requirements : nx_ship_gen_arrange ("Ship General Arrangement") */
                    public: void SetCreateItem
                    (
                        bool createItem /** createitem */ 
                    );
                };
            }
        }
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
#ifndef NXOpen_FEATURES_SHIPDESIGN_GENERALARRANGEMENT_DRAWINGTABLEITEMBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_GENERALARRANGEMENT_DRAWINGTABLEITEMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_GeneralArrangement_DrawingTableItemBuilder.ja
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
#include <NXOpen/Features_ShipDesign_GeneralArrangement_DrawingItemBuilder.hxx>
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
                class DrawingTableItemBuilder;
            }
        }
    }
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
    namespace Features
    {
        namespace ShipDesign
        {
            namespace GeneralArrangement
            {
                class _DrawingTableItemBuilderBuilder;
                class DrawingTableItemBuilderImpl;
                /** This builder allows you to define the general arrangement drawing table item information. 
                            It represents @link NXOpen::Features::ShipDesign::GeneralArrangement::DrawingTableItemBuilder NXOpen::Features::ShipDesign::GeneralArrangement::DrawingTableItemBuilder@endlink .
                            This builder won't create Table and just returns NULL. 
                             <br> To create a new instance of this class, use @link NXOpen::Features::ShipDesign::GeneralArrangement::DrawingAutomationBuilder::CreateDrawingTableItemBuilder  NXOpen::Features::ShipDesign::GeneralArrangement::DrawingAutomationBuilder::CreateDrawingTableItemBuilder @endlink  <br> 
                 <br>  Created in NX12.0.2.  <br>  
                */
                class NXOPENCPP_FEATURESEXPORT  DrawingTableItemBuilder : public NXOpen::Features::ShipDesign::GeneralArrangement::DrawingItemBuilder
                {
                    private: DrawingTableItemBuilderImpl * m_drawingtableitembuilder_impl;
                    private: friend class  _DrawingTableItemBuilderBuilder;
                    protected: DrawingTableItemBuilder();
                    public: ~DrawingTableItemBuilder();
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
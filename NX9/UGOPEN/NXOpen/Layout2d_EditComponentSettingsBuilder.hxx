#ifndef NXOpen_LAYOUT2D_EDITCOMPONENTSETTINGSBUILDER_HXX_INCLUDED
#define NXOpen_LAYOUT2D_EDITCOMPONENTSETTINGSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Layout2d_EditComponentSettingsBuilder.ja
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
#include <NXOpen/Layout2d_ComponentSettingsBlockBuilder.hxx>
#include <NXOpen/Layout2d_EditComponentSettingsBuilder.hxx>
#include <NXOpen/libnxopencpp_layout2d_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Layout2d
    {
        class EditComponentSettingsBuilder;
    }
    class Builder;
    namespace Layout2d
    {
        class ComponentSettingsBlockBuilder;
    }
    class NXObject;
    namespace Layout2d
    {
        class _EditComponentSettingsBuilderBuilder;
        class EditComponentSettingsBuilderImpl;
        /** Represents a @link Layout2d::EditComponentSettingsBuilder Layout2d::EditComponentSettingsBuilder@endlink  builder.
                It provides an interface for editing layout2d component settings. 
                The committed object is the component with the new settings  <br> To create a new instance of this class, use @link Drafting::SettingsManager::CreateLayout2dEditComponentSettingsBuilder  Drafting::SettingsManager::CreateLayout2dEditComponentSettingsBuilder @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_LAYOUT2DEXPORT  EditComponentSettingsBuilder : public Builder
        {
            private: EditComponentSettingsBuilderImpl * m_editcomponentsettingsbuilder_impl;
            private: friend class  _EditComponentSettingsBuilderBuilder;
            protected: EditComponentSettingsBuilder();
            public: ~EditComponentSettingsBuilder();
            /**Returns  the 2d component settings block builder which holds the component settings builder 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Layout2d::ComponentSettingsBlockBuilder * ComponentSettings
            (
            );
            /** Inherit Settings From Selected Objects 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            public: void InheritSettingsFromSelectedObject
            (
                NXOpen::NXObject * selectedObject /** The selected 2d component object. 
                                                                                        NULL is not allowed. */
            );
            /** Inherit Settings From Customer Default 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            public: void InheritSettingsFromCustomerDefault
            (
            );
            /** Inherit Settings From Preference 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            public: void InheritSettingsFromPreferences
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

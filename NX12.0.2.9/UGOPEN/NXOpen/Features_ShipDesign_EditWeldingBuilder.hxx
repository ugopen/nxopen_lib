#ifndef NXOpen_FEATURES_SHIPDESIGN_EDITWELDINGBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_EDITWELDINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_EditWeldingBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/Weld_CharacteristicsBuilder.hxx>
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
            class EditWeldingBuilder;
        }
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class SelectNXObjectList;
    namespace Weld
    {
        class CharacteristicsBuilder;
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class _EditWeldingBuilderBuilder;
            class EditWeldingBuilderImpl;
            /**
                Used to create a @link NXOpen::Features::ShipDesign::EditWeldingBuilder NXOpen::Features::ShipDesign::EditWeldingBuilder@endlink  which
                is used to change the welding characteristics on the seams in the plate systems.
                 <br> To create a new instance of this class, use @link NXOpen::Features::ShipCollection::CreateEditWeldingBuilder  NXOpen::Features::ShipCollection::CreateEditWeldingBuilder @endlink  <br> 
             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  EditWeldingBuilder : public NXOpen::Features::FeatureBuilder
            {
                private: EditWeldingBuilderImpl * m_editweldingbuilder_impl;
                private: friend class  _EditWeldingBuilderBuilder;
                protected: EditWeldingBuilder();
                public: ~EditWeldingBuilder();
                /**Returns  the objects to change the welding characteristics 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectNXObjectList * Seams
                (
                );
                /**Returns  the weld characteristics 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Weld::CharacteristicsBuilder * WeldCharacteristics
                (
                );
            };
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

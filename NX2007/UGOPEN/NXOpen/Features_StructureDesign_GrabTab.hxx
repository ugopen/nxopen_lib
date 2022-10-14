#ifndef NXOpen_FEATURES_STRUCTUREDESIGN_GRABTAB_HXX_INCLUDED
#define NXOpen_FEATURES_STRUCTUREDESIGN_GRABTAB_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_StructureDesign_GrabTab.ja
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
#include <NXOpen/Features_BodyFeature.hxx>
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
        namespace StructureDesign
        {
            class GrabTab;
        }
    }
    namespace Features
    {
        class BodyFeature;
    }
    namespace Features
    {
        namespace StructureDesign
        {
            class _GrabTabBuilder;
            class GrabTabImpl;
            /** Represents a grab tab feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::StructureDesign::GrabTabBuilder  NXOpen::Features::StructureDesign::GrabTabBuilder @endlink  <br> 
             <br>  Created in NX1953.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  GrabTab : public NXOpen::Features::BodyFeature
            {
                private: GrabTabImpl * m_grabtab_impl;
                private: friend class  _GrabTabBuilder;
                protected: GrabTab();
                public: ~GrabTab();
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
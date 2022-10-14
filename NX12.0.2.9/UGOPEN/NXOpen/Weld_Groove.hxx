#ifndef NXOpen_WELD_GROOVE_HXX_INCLUDED
#define NXOpen_WELD_GROOVE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_Groove.ja
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
#include <NXOpen/Features_Feature.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/Weld_IFeature.hxx>
#include <NXOpen/libnxopencpp_weld_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Weld
    {
        class Groove;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    namespace Features
    {
        class Feature;
    }
    class INXObject;
    class ReferenceSet;
    namespace Weld
    {
        class IFeature;
    }
    namespace Weld
    {
        class _GrooveBuilder;
        class GrooveImpl;
        /** Represents a WeldGroove feature.  <br> To create or edit an instance of this class, use @link NXOpen::Weld::GrooveBuilder  NXOpen::Weld::GrooveBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_WELDEXPORT  Groove : public NXOpen::Features::Feature, public virtual NXOpen::Weld::IFeature
        {
            private: GrooveImpl * m_groove_impl;
            private: friend class  _GrooveBuilder;
            protected: Groove();
            public: ~Groove();
            /** Returns the feature diagnostic information, warning, or error codes. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: virtual void GetFeatureDiagnostics
            (
                std::vector<int> & diagnosticCodes /** the information, warning, or error codes for this feature. */
            );
            /** Gets the feature icon name.  @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: virtual NXString GetFeatureIconName
            (
            );
            /** Gets the feature layer.  @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: virtual int GetFeatureLayer
            (
            );
            /** Gets the feature color.  @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: virtual int GetFeatureObjectColor
            (
            );
            /** Gets all the reference sets that this feature is a member of. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: virtual void GetFeatureReferenceSets
            (
                std::vector<NXOpen::ReferenceSet *> & refSet /** refset */ 
            );
            /** Gets all the reference sets that this feature is a member of. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: virtual void GetFeatureReferenceSetStrings
            (
                std::vector<NXString> & refSet /** refset */ 
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
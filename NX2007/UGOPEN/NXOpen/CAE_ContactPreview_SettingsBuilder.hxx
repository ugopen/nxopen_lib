#ifndef NXOpen_CAE_CONTACTPREVIEW_SETTINGSBUILDER_HXX_INCLUDED
#define NXOpen_CAE_CONTACTPREVIEW_SETTINGSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ContactPreview_SettingsBuilder.ja
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
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        namespace ContactPreview
        {
            class SettingsBuilder;
        }
    }
    class Builder;
    namespace CAE
    {
        namespace ContactPreview
        {
            class _SettingsBuilderBuilder;
            class SettingsBuilderImpl;
            /** Represents a @link CAE::ContactPreview::SettingsBuilder CAE::ContactPreview::SettingsBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::CAE::CaePart::CreateContactPreviewSettingsBuilder  NXOpen::CAE::CaePart::CreateContactPreviewSettingsBuilder @endlink  <br> 
            Default values.
            <list type="table"> 
             
            <listheader><term> 
            Property</term>  <description> 
            Value</description> </listheader>
            <item><term> 
             
            ContactSide </term> <description> 
             
            Both </description> </item> 

            </list> 

             <br>  Created in NX2007.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  SettingsBuilder : public NXOpen::Builder
            {
                /** The selection types */
                public: enum ContactSideOptions
                {
                    ContactSideOptionsBoth/** both */ ,
                    ContactSideOptionsContact/** contact */ ,
                    ContactSideOptionsTarget/** target */ 
                };

                private: SettingsBuilderImpl * m_settingsbuilder_impl;
                private: friend class  _SettingsBuilderBuilder;
                protected: SettingsBuilder();
                public: ~SettingsBuilder();
                /**Returns  the selection type 
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::ContactPreview::SettingsBuilder::ContactSideOptions ContactSide
                (
                );
                /**Sets  the selection type 
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: void SetContactSide
                (
                    NXOpen::CAE::ContactPreview::SettingsBuilder::ContactSideOptions selectionType /** selectiontype */ 
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
#ifndef NXOpen_PID_PREFERENCESOFFSHEETCONNECTORBUILDER_HXX_INCLUDED
#define NXOpen_PID_PREFERENCESOFFSHEETCONNECTORBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PID_PreferencesOffSheetConnectorBuilder.ja
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
#include <NXOpen/Diagramming_TextStyleBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libpidopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PID
    {
        class PreferencesOffSheetConnectorBuilder;
    }
    namespace Diagramming
    {
        class TextStyleBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace PID
    {
        class _PreferencesOffSheetConnectorBuilderBuilder;
        class PreferencesOffSheetConnectorBuilderImpl;
        /**
            Represents a PreferencesOffSheetConnectorBuilder
            
         <br>  Created in NX11.0.1.  <br>  
        */
        class PIDOPENCPPEXPORT  PreferencesOffSheetConnectorBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /**  @brief  the style of OSC elements.  

              */
            public: enum StyleOption
            {
                StyleOptionSmallFilledArrowOut/** small filled arrow out */ ,
                StyleOptionSmallFilledArrowIn/** small filled arrow in */ ,
                StyleOptionBox/** box */ ,
                StyleOptionChevronOut/** chevron out */ ,
                StyleOptionChevronIn/** chevron in */ 
            };

            private: PreferencesOffSheetConnectorBuilderImpl * m_preferencesoffsheetconnectorbuilder_impl;
            private: friend class  _PreferencesOffSheetConnectorBuilderBuilder;
            protected: PreferencesOffSheetConnectorBuilder();
            public: ~PreferencesOffSheetConnectorBuilder();
            /**Returns  the style of OSC 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: NXOpen::PID::PreferencesOffSheetConnectorBuilder::StyleOption Style
            (
            );
            /**Sets  the style of OSC 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: void SetStyle
            (
                NXOpen::PID::PreferencesOffSheetConnectorBuilder::StyleOption style /** style */ 
            );
            /**Returns  the text style of the OSC. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: NXOpen::Diagramming::TextStyleBuilder * TextStyleBuilder
            (
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

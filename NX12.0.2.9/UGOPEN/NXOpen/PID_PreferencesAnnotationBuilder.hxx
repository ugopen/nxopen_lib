#ifndef NXOpen_PID_PREFERENCESANNOTATIONBUILDER_HXX_INCLUDED
#define NXOpen_PID_PREFERENCESANNOTATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PID_PreferencesAnnotationBuilder.ja
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
#include <NXOpen/Diagramming_DataType.hxx>
#include <NXOpen/Diagramming_Tables_CellSettingsBuilder.hxx>
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
        class PreferencesAnnotationBuilder;
    }
    namespace Diagramming
    {
        namespace Tables
        {
            class CellSettingsBuilder;
        }
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
        class _PreferencesAnnotationBuilderBuilder;
        class PreferencesAnnotationBuilderImpl;
        /**
            Represents a PreferencesAnnotationBuilder
            
         <br>  Created in NX11.0.1.  <br>  
        */
        class PIDOPENCPPEXPORT  PreferencesAnnotationBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: PreferencesAnnotationBuilderImpl * m_preferencesannotationbuilder_impl;
            private: friend class  _PreferencesAnnotationBuilderBuilder;
            protected: PreferencesAnnotationBuilder();
            public: ~PreferencesAnnotationBuilder();
            /**Returns  the horizontal position of the connection tag. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: NXOpen::Diagramming::DiagrammingConnectionlabelhorizontaloffsetposition ConnectionLabelHorizontalOffsetPosition
            (
            );
            /**Sets  the horizontal position of the connection tag. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: void SetConnectionLabelHorizontalOffsetPosition
            (
                NXOpen::Diagramming::DiagrammingConnectionlabelhorizontaloffsetposition position /** position */ 
            );
            /**Returns  the vertical position of the connection tag. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: NXOpen::Diagramming::DiagrammingConnectionlabelverticaloffsetposition ConnectionLabelVerticalOffsetPosition
            (
            );
            /**Sets  the vertical position of the connection tag. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: void SetConnectionLabelVerticalOffsetPosition
            (
                NXOpen::Diagramming::DiagrammingConnectionlabelverticaloffsetposition position /** position */ 
            );
            /**Returns  the tag is displayed at the center of the connection.
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: bool ConnectionLabelPositionCenter
            (
            );
            /**Sets  the tag is displayed at the center of the connection.
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: void SetConnectionLabelPositionCenter
            (
                bool center /** center */ 
            );
            /**Returns  the gap between the connection and the tag.
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: double ConnectionLabelOffset
            (
            );
            /**Sets  the gap between the connection and the tag.
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: void SetConnectionLabelOffset
            (
                double offset /** offset */ 
            );
            /**Returns  the connection text style of the Annotation. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: NXOpen::Diagramming::TextStyleBuilder * TextStyleConnectionBuilder
            (
            );
            /**Returns  the note text style of the Annotation. 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: NXOpen::Diagramming::TextStyleBuilder * TextStyleNoteBuilder
            (
            );
            /**Returns     the preferences tabular note settings builder 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: NXOpen::Diagramming::Tables::CellSettingsBuilder * TablesCellSettings
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

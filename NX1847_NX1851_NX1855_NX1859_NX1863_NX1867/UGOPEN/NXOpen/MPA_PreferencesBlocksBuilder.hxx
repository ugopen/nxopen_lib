#ifndef NXOpen_MPA_PREFERENCESBLOCKSBUILDER_HXX_INCLUDED
#define NXOpen_MPA_PREFERENCESBLOCKSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MPA_PreferencesBlocksBuilder.ja
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
#include <NXOpen/LineColorFontWidthBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TextColorFontWidthBuilder.hxx>
#include <NXOpen/libmpaopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace MPA
    {
        class PreferencesBlocksBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class LineColorFontWidthBuilder;
    class TextColorFontWidthBuilder;
    namespace MPA
    {
        class _PreferencesBlocksBuilderBuilder;
        class PreferencesBlocksBuilderImpl;

        /// \cond NX_NO_DOC 
        /**
            Represents a PreferencesBlocksBuilder which controls Border,linecolorfontwidth,textColorFontWidth,TextHeight
            and Label of Nodes
            
         <br>  Created in NX1847.0.0.  <br>  
        */
        class MPAOPENCPPEXPORT  PreferencesBlocksBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: PreferencesBlocksBuilderImpl * m_preferencesblocksbuilder_impl;
            private: friend class  _PreferencesBlocksBuilderBuilder;
            protected: PreferencesBlocksBuilder();
            public: ~PreferencesBlocksBuilder();

            /// \cond NX_NO_DOC 
            /**Returns  the state of  Border provided by user  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowBorder
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the state of  Border provided by user  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_sdpd_pam_a (" NX Physical Architecture Diagram Author") */
            public: void SetShowBorder
            (
                bool border /** border */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the line color font width provided by user  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::LineColorFontWidthBuilder * LineColorFontWidth
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the Text color font width provided by user  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TextColorFontWidthBuilder * TextColorFontWidth
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the value of text height provided by user  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: double TextHeight
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the value of text height provided by user  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_sdpd_pam_a (" NX Physical Architecture Diagram Author") */
            public: void SetTextHeight
            (
                double height /** height */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the state of label provided by user  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowLabel
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the state of label provided by user  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_sdpd_pam_a (" NX Physical Architecture Diagram Author") */
            public: void SetShowLabel
            (
                bool label /** label */ 
            );

            /// \endcond 
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

        /// \endcond 
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

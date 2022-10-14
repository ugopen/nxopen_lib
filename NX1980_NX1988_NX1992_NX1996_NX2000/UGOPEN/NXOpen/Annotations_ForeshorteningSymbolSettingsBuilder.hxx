#ifndef NXOpen_ANNOTATIONS_FORESHORTENINGSYMBOLSETTINGSBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_FORESHORTENINGSYMBOLSETTINGSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_ForeshorteningSymbolSettingsBuilder.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Annotations
    {
        class ForeshorteningSymbolSettingsBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Annotations
    {
        class _ForeshorteningSymbolSettingsBuilderBuilder;
        class ForeshorteningSymbolSettingsBuilderImpl;
        /** Represents a @link NXOpen::Annotations::ForeshorteningSymbolSettingsBuilder NXOpen::Annotations::ForeshorteningSymbolSettingsBuilder@endlink  builder 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  ForeshorteningSymbolSettingsBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** Represents foreshortening symbol type */
            public: enum SymbolType
            {
                SymbolTypeRegular/** regular */ ,
                SymbolTypeStretched/** stretched */ 
            };

            /** Represents foreshortening symbol method type */
            public: enum MethodType
            {
                MethodTypeWidthAndAngle/** width and angle */ ,
                MethodTypeWidthAndHeight/** width and height */ 
            };

            private: ForeshorteningSymbolSettingsBuilderImpl * m_foreshorteningsymbolsettingsbuilder_impl;
            private: friend class  _ForeshorteningSymbolSettingsBuilderBuilder;
            protected: ForeshorteningSymbolSettingsBuilder();
            public: ~ForeshorteningSymbolSettingsBuilder();
            /**Returns  the foreshortening symbol type 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::ForeshorteningSymbolSettingsBuilder::SymbolType ForeshorteningSymbolType
            (
            );
            /**Sets  the foreshortening symbol type 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetForeshorteningSymbolType
            (
                NXOpen::Annotations::ForeshorteningSymbolSettingsBuilder::SymbolType foreshorteningSymbolType /** foreshorteningsymboltype */ 
            );
            /**Returns  the foreshortening symbol method 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::ForeshorteningSymbolSettingsBuilder::MethodType ForeshorteningSymbolMethodType
            (
            );
            /**Sets  the foreshortening symbol method 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetForeshorteningSymbolMethodType
            (
                NXOpen::Annotations::ForeshorteningSymbolSettingsBuilder::MethodType foreshorteningSymbolMethod /** foreshorteningsymbolmethod */ 
            );
            /**Returns  the foreshortening symbol width 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double Width
            (
            );
            /**Sets  the foreshortening symbol width 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetWidth
            (
                double foreshorteningSymbolWidth /** foreshorteningsymbolwidth */ 
            );
            /**Returns  the foreshortening symbol height 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double Height
            (
            );
            /**Sets  the foreshortening symbol height 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetHeight
            (
                double foreshorteningSymbolHeight /** foreshorteningsymbolheight */ 
            );
            /**Returns  the foreshortening symbol angle 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double Angle
            (
            );
            /**Sets  the foreshortening symbol angle 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetAngle
            (
                double foreshorteningSymbolAngle /** foreshorteningsymbolangle */ 
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not yet implemented
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
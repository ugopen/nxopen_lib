#ifndef NXOpen_ANNOTATIONS_STYLEBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_STYLEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_StyleBuilder.ja
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
#include <NXOpen/Annotations_BreakSettingsBuilder.hxx>
#include <NXOpen/Annotations_DimensionStyleBuilder.hxx>
#include <NXOpen/Annotations_DisplayStyleBuilder.hxx>
#include <NXOpen/Annotations_ForeshorteningSymbolSettingsBuilder.hxx>
#include <NXOpen/Annotations_FrameBarStyleBuilder.hxx>
#include <NXOpen/Annotations_HatchStyleBuilder.hxx>
#include <NXOpen/Annotations_HoleCalloutSettingsBuilder.hxx>
#include <NXOpen/Annotations_LetteringStyleBuilder.hxx>
#include <NXOpen/Annotations_LineArrowStyleBuilder.hxx>
#include <NXOpen/Annotations_OrdinateStyleBuilder.hxx>
#include <NXOpen/Annotations_RadialStyleBuilder.hxx>
#include <NXOpen/Annotations_SingleSidedDisplayBuilder.hxx>
#include <NXOpen/Annotations_SymbolStyleBuilder.hxx>
#include <NXOpen/Annotations_UnitsStyleBuilder.hxx>
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
        class StyleBuilder;
    }
    namespace Annotations
    {
        class BreakSettingsBuilder;
    }
    namespace Annotations
    {
        class DimensionStyleBuilder;
    }
    namespace Annotations
    {
        class DisplayStyleBuilder;
    }
    namespace Annotations
    {
        class ForeshorteningSymbolSettingsBuilder;
    }
    namespace Annotations
    {
        class FrameBarStyleBuilder;
    }
    namespace Annotations
    {
        class HatchStyleBuilder;
    }
    namespace Annotations
    {
        class HoleCalloutSettingsBuilder;
    }
    namespace Annotations
    {
        class LetteringStyleBuilder;
    }
    namespace Annotations
    {
        class LineArrowStyleBuilder;
    }
    namespace Annotations
    {
        class OrdinateStyleBuilder;
    }
    namespace Annotations
    {
        class RadialStyleBuilder;
    }
    namespace Annotations
    {
        class SingleSidedDisplayBuilder;
    }
    namespace Annotations
    {
        class SymbolStyleBuilder;
    }
    namespace Annotations
    {
        class UnitsStyleBuilder;
    }
    class DisplayableObject;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Annotations
    {
        class _StyleBuilderBuilder;
        class StyleBuilderImpl;
        /**
            Represents a @link NXOpen::Annotations::StyleBuilder NXOpen::Annotations::StyleBuilder@endlink .
            This class is used to set Annotation preferences when creating or editing an annotation.
            
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  StyleBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: StyleBuilderImpl * m_stylebuilder_impl;
            private: friend class  _StyleBuilderBuilder;
            protected: StyleBuilder();
            public: ~StyleBuilder();
            /**Returns  the dimension style builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::DimensionStyleBuilder * DimensionStyle
            (
            );
            /**Returns  the units style builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::UnitsStyleBuilder * UnitsStyle
            (
            );
            /**Returns  the radial style builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::RadialStyleBuilder * RadialStyle
            (
            );
            /**Returns  the ordinate style builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::OrdinateStyleBuilder * OrdinateStyle
            (
            );
            /**Returns  the lettering style builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::LetteringStyleBuilder * LetteringStyle
            (
            );
            /**Returns  the line/arrow style builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::LineArrowStyleBuilder * LineArrowStyle
            (
            );
            /**Returns  the symbol style builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SymbolStyleBuilder * SymbolStyle
            (
            );
            /**Returns  the hatch style builder 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::HatchStyleBuilder * HatchStyle
            (
            );
            /**Returns  the frame bar builder 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::FrameBarStyleBuilder * FrameBarStyle
            (
            );
            /**Returns  the hole callout settings builder 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::HoleCalloutSettingsBuilder * HoleCalloutSettings
            (
            );
            /** Inherit Settings From Selected Objects 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void InheritSettingsFromSelectedObjects
            (
                NXOpen::DisplayableObject * selectedObject /** The selected annotation or table instance object. 
                                                                                        NULL is not allowed. */
            );
            /** Inherit Settings From Customer Default 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void InheritSettingsFromCustomerDefault
            (
            );
            /** Inherit Settings From Preference 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void InheritSettingsFromPreferences
            (
            );
            /**Returns  the get break builder 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::BreakSettingsBuilder * BreakSettings
            (
            );
            /**Returns  the get builder for foreshortening symbol 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::ForeshorteningSymbolSettingsBuilder * ForeshorteningSymbolSettings
            (
            );
            /**Returns  the single sided display builder 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SingleSidedDisplayBuilder * SingleSidedDisplay
            (
            );
            /**Returns  the display style builder 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::DisplayStyleBuilder * DisplayStyle
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
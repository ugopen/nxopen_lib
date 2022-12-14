#ifndef NXOpen_DRAWINGS_DRAWINGREGIONRULESBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_DRAWINGREGIONRULESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_DrawingRegionRulesBuilder.ja
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
#include <NXOpen/Drawings_DrawingRegionRulesBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_drawings_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Drawings
    {
        class DrawingRegionRulesBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Drawings
    {
        class _DrawingRegionRulesBuilderBuilder;
        class DrawingRegionRulesBuilderImpl;
        /** Represents a Drawing region rules builder 
         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  DrawingRegionRulesBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: DrawingRegionRulesBuilderImpl * m_drawingregionrulesbuilder_impl;
            private: friend class  _DrawingRegionRulesBuilderBuilder;
            protected: DrawingRegionRulesBuilder();
            public: ~DrawingRegionRulesBuilder();
            /** Get Rules  @return  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetRules
            (
            );
            /** Set Rules 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_drawing_auto ("NX Drawing Automation") */
            public: void SetRules
            (
                std::vector<NXString> & rules /** rules */ 
            );
            /** Remove Rules 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : nx_drawing_auto ("NX Drawing Automation") */
            public: void RemoveRules
            (
                std::vector<NXString> & rules /** rules */ 
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

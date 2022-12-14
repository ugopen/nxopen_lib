#ifndef NXOpen_MPA_PREFERENCESPHYSICALCONNECTIONBUILDER_HXX_INCLUDED
#define NXOpen_MPA_PREFERENCESPHYSICALCONNECTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MPA_PreferencesPhysicalConnectionBuilder.ja
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
        class PreferencesPhysicalConnectionBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class LineColorFontWidthBuilder;
    namespace MPA
    {
        class _PreferencesPhysicalConnectionBuilderBuilder;
        class PreferencesPhysicalConnectionBuilderImpl;
        /** Represents a PreferencesPhysicalConnectionBuilder which controls size, style of Physical connection in physical Diagram 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class MPAOPENCPPEXPORT  PreferencesPhysicalConnectionBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: PreferencesPhysicalConnectionBuilderImpl * m_preferencesphysicalconnectionbuilder_impl;
            private: friend class  _PreferencesPhysicalConnectionBuilderBuilder;
            protected: PreferencesPhysicalConnectionBuilder();
            public: ~PreferencesPhysicalConnectionBuilder();
            /**Returns  the line color font width for Assembly Constraint Connections provided by user 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::LineColorFontWidthBuilder * LineColorFontWidthAssemblyConstraint
            (
            );
            /**Returns  the line color font width for Inter Part Expression connections of MPA diagram  
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::LineColorFontWidthBuilder * LineColorFontWidthIPExp
            (
            );
            /**Returns  the line color font width for Inter Part Measure connections of MPA diagram  
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::LineColorFontWidthBuilder * LineColorFontWidthIPMeasure
            (
            );
            /**Returns  the line color font width for Position Dependent Wave Link connections of MPA diagram  
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::LineColorFontWidthBuilder * LineColorFontWidthPDWaveLink
            (
            );
            /**Returns  the line color font width for Position Independent Wave Link connections of MPA diagram  
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::LineColorFontWidthBuilder * LineColorFontWidthPIWaveLink
            (
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

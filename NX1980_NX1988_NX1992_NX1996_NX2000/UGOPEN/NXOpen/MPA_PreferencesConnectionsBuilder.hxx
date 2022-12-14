#ifndef NXOpen_MPA_PREFERENCESCONNECTIONSBUILDER_HXX_INCLUDED
#define NXOpen_MPA_PREFERENCESCONNECTIONSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MPA_PreferencesConnectionsBuilder.ja
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
        class PreferencesConnectionsBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class LineColorFontWidthBuilder;
    namespace MPA
    {
        class _PreferencesConnectionsBuilderBuilder;
        class PreferencesConnectionsBuilderImpl;
        /** Represents a PreferencesConnectionsBuilder which controls color, font, width of connections and size, style of arrows. 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class MPAOPENCPPEXPORT  PreferencesConnectionsBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** Enum that represents the Arrow Style of Connection on sheet */
            public: enum Styles
            {
                StylesClosed/** closed*/,
                StylesCloseddouble/** closed Double  */,
                StylesCloseddoublesolid/** closed double solid  */,
                StylesClosedsolid/** closed solid  */,
                StylesFilled/**  filled  */,
                StylesFilleddouble/**  filled double  */,
                StylesOpen/**  open  */,
                StylesOpendouble/** open double  */
            };

            private: PreferencesConnectionsBuilderImpl * m_preferencesconnectionsbuilder_impl;
            private: friend class  _PreferencesConnectionsBuilderBuilder;
            protected: PreferencesConnectionsBuilder();
            public: ~PreferencesConnectionsBuilder();
            /**Returns  the line color font width for Assembly Constraint Connections provided by user 
             <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::MPA::PreferencesPhysicalConnectionBuilder::LineColorFontWidthAssemblyConstraint NXOpen::MPA::PreferencesPhysicalConnectionBuilder::LineColorFontWidthAssemblyConstraint@endlink  instead <br>  

             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1980.0.0.  Use NXOpen::MPA::PreferencesPhysicalConnectionBuilder::LineColorFontWidthAssemblyConstraint instead") NXOpen::LineColorFontWidthBuilder * LineColorFontWidthAssemblyConstraint
            (
            );
            /**Returns  the line color font width for Inter Part Expression connections of MPA diagram  
             <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::MPA::PreferencesPhysicalConnectionBuilder::LineColorFontWidthIPExp NXOpen::MPA::PreferencesPhysicalConnectionBuilder::LineColorFontWidthIPExp@endlink  instead <br>  

             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1980.0.0.  Use NXOpen::MPA::PreferencesPhysicalConnectionBuilder::LineColorFontWidthIPExp instead") NXOpen::LineColorFontWidthBuilder * LineColorFontWidthIPExp
            (
            );
            /**Returns  the line color font width for Inter Part Measure connections of MPA diagram  
             <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::MPA::PreferencesPhysicalConnectionBuilder::LineColorFontWidthIPMeasure NXOpen::MPA::PreferencesPhysicalConnectionBuilder::LineColorFontWidthIPMeasure@endlink  instead <br>  

             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1980.0.0.  Use NXOpen::MPA::PreferencesPhysicalConnectionBuilder::LineColorFontWidthIPMeasure instead") NXOpen::LineColorFontWidthBuilder * LineColorFontWidthIPMeasure
            (
            );
            /**Returns  the line color font width for Position Dependent Wave Link connections of MPA diagram  
             <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::MPA::PreferencesPhysicalConnectionBuilder::LineColorFontWidthPDWaveLink NXOpen::MPA::PreferencesPhysicalConnectionBuilder::LineColorFontWidthPDWaveLink@endlink  instead <br>  

             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1980.0.0.  Use NXOpen::MPA::PreferencesPhysicalConnectionBuilder::LineColorFontWidthPDWaveLink instead") NXOpen::LineColorFontWidthBuilder * LineColorFontWidthPDWaveLink
            (
            );
            /**Returns  the line color font width for Position Independent Wave Link connections of MPA diagram  
             <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::MPA::PreferencesPhysicalConnectionBuilder::LineColorFontWidthPIWaveLink NXOpen::MPA::PreferencesPhysicalConnectionBuilder::LineColorFontWidthPIWaveLink@endlink  instead <br>  

             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1980.0.0.  Use NXOpen::MPA::PreferencesPhysicalConnectionBuilder::LineColorFontWidthPIWaveLink instead") NXOpen::LineColorFontWidthBuilder * LineColorFontWidthPIWaveLink
            (
            );
            /**Returns  the value of arrow size for connection of MPA diagram  
             <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::MPA::PreferencesArrowConnectionBuilder::ArrowSize NXOpen::MPA::PreferencesArrowConnectionBuilder::ArrowSize@endlink  instead <br>  

             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1980.0.0.  Use NXOpen::MPA::PreferencesArrowConnectionBuilder::ArrowSize instead") double ArrowSize
            (
            );
            /**Sets  the value of arrow size for connection of MPA diagram  
             <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::MPA::PreferencesArrowConnectionBuilder::ArrowSize NXOpen::MPA::PreferencesArrowConnectionBuilder::ArrowSize@endlink  instead <br>  

             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_sdpd_pam_a (" NX Physical Architecture Diagram Author") */
            public: NX_DEPRECATED("Deprecated in NX1980.0.0.  Use NXOpen::MPA::PreferencesArrowConnectionBuilder::ArrowSize instead") void SetArrowSize
            (
                double size /** size */ 
            );
            /**Returns  the arrow style for connection of MPA diagram 
             <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::MPA::PreferencesArrowConnectionBuilder::ArrowStyle NXOpen::MPA::PreferencesArrowConnectionBuilder::ArrowStyle@endlink  instead <br>  

             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX1980.0.0.  Use NXOpen::MPA::PreferencesArrowConnectionBuilder::ArrowStyle instead") int ArrowStyle
            (
            );
            /**Sets  the arrow style for connection of MPA diagram 
             <br>  @deprecated Deprecated in NX1980.0.0.  Use @link NXOpen::MPA::PreferencesArrowConnectionBuilder::ArrowStyle NXOpen::MPA::PreferencesArrowConnectionBuilder::ArrowStyle@endlink  instead <br>  

             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_sdpd_pam_a (" NX Physical Architecture Diagram Author") */
            public: NX_DEPRECATED("Deprecated in NX1980.0.0.  Use NXOpen::MPA::PreferencesArrowConnectionBuilder::ArrowStyle instead") void SetArrowStyle
            (
                int style /** style */ 
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

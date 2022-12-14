#ifndef NXOpen_SCHEMATIC_FLOWDIRECTIONARROWBUILDER_HXX_INCLUDED
#define NXOpen_SCHEMATIC_FLOWDIRECTIONARROWBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Schematic_FlowDirectionArrowBuilder.ja
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
#include <NXOpen/Schematic_Connection.hxx>
#include <NXOpen/libnxopencpp_schematic_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Schematic
    {
        class FlowDirectionArrowBuilder;
    }
    class Builder;
    namespace Schematic
    {
        class Connection;
    }
    namespace Schematic
    {
        class _FlowDirectionArrowBuilderBuilder;
        class FlowDirectionArrowBuilderImpl;

        /// \cond NX_NO_DOC 
        /**  @brief 
            Represents FlowDirectionArrowBuilder  

         
              <br> To create a new instance of this class, use @link NXOpen::Schematic::SchematicManager::CreateFdaBuilder  NXOpen::Schematic::SchematicManager::CreateFdaBuilder @endlink  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_SCHEMATICEXPORT  FlowDirectionArrowBuilder : public NXOpen::Builder
        {
            private: FlowDirectionArrowBuilderImpl * m_flowdirectionarrowbuilder_impl;
            private: friend class  _FlowDirectionArrowBuilderBuilder;
            protected: FlowDirectionArrowBuilder();
            public: ~FlowDirectionArrowBuilder();

            /// \cond NX_NO_DOC 
            /**Returns  the percent along the segment for this Flow Direction Arrow. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: double LocationPercent
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the percent along the segment for this Flow Direction Arrow. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLocationPercent
            (
                double locationPercent /** locationpercent */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the segment this Flow Direction Arrow is located on. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: int LocationSegment
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the segment this Flow Direction Arrow is located on. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLocationSegment
            (
                int segment /** segment */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Gets the connection for this Flow Direction Arrow. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Schematic::Connection * GetConnection
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Sets the connection for this Flow Direction Arrow. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetConnection
            (
                NXOpen::Schematic::Connection * connection /** connection */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Change the direction of FDA. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void ReverseDirection
            (
            );

            /// \endcond 
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

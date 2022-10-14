#ifndef NXOpen_DIAGRAMMINGLIBRARYAUTHOR_SYMBOLPORTBUILDER_HXX_INCLUDED
#define NXOpen_DIAGRAMMINGLIBRARYAUTHOR_SYMBOLPORTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     DiagrammingLibraryAuthor_SymbolPortBuilder.ja
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
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_diagramminglibraryauthor_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace DiagrammingLibraryAuthor
    {
        class SymbolPortBuilder;
    }
    class Builder;
    namespace DiagrammingLibraryAuthor
    {
        class AttributeHolder;
    }
    namespace DiagrammingLibraryAuthor
    {
        class _SymbolPortBuilderBuilder;
        class SymbolPortBuilderImpl;

        /// \cond NX_NO_DOC 
        /**  @brief  Represents a SymbolPortBuilder.  

          
                Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.  <br> To create a new instance of this class, use @link NXOpen::DiagrammingLibraryAuthor::SymbolDesignerManager::CreateSymbolPortBuilder  NXOpen::DiagrammingLibraryAuthor::SymbolDesignerManager::CreateSymbolPortBuilder @endlink  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_DIAGRAMMINGLIBRARYAUTHOREXPORT  SymbolPortBuilder : public NXOpen::Builder
        {
            private: SymbolPortBuilderImpl * m_symbolportbuilder_impl;
            private: friend class  _SymbolPortBuilderBuilder;
            protected: SymbolPortBuilder();
            public: ~SymbolPortBuilder();

            /// \cond NX_NO_DOC 
            /** Gets the port objects which have user attributes of the port.  @return  the port objects 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::DiagrammingLibraryAuthor::AttributeHolder * GetPortObject
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Set port location 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLocation
            (
                const NXOpen::Point2d & portLocation /** the port location */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Get port location point @return  the port location 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point2d GetLocation
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Set connection direction 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetConnectionDirection
            (
                const NXOpen::Point2d & connectionDirection /** the connection direction */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Get connection direction  @return  the connection direction 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point2d GetConnectionDirection
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Set port id 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPortID
            (
                const NXString & portID /** the port id */
            );
            /** Set port id 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            void SetPortID
            (
                const char * portID /** the port id */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Get port id @return  the port id 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetPortID
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Set port direction 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDirection
            (
                const NXString & portDirection /** the port direction */
            );
            /** Set port direction 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            void SetDirection
            (
                const char * portDirection /** the port direction */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Get port direction @return  the port direction 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetDirection
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
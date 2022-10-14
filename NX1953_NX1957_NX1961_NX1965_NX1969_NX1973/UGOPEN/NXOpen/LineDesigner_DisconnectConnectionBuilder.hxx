#ifndef NXOpen_LINEDESIGNER_DISCONNECTCONNECTIONBUILDER_HXX_INCLUDED
#define NXOpen_LINEDESIGNER_DISCONNECTCONNECTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     LineDesigner_DisconnectConnectionBuilder.ja
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
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/liblinedesigneropencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace LineDesigner
    {
        class DisconnectConnectionBuilder;
    }
    class Builder;
    class SelectPointList;
    namespace LineDesigner
    {
        class _DisconnectConnectionBuilderBuilder;
        class DisconnectConnectionBuilderImpl;
        /** 
            
            
            
            
            
             <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateDisconnectConnectionBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateDisconnectConnectionBuilder @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class LINEDESIGNEROPENCPPEXPORT  DisconnectConnectionBuilder : public NXOpen::Builder
        {
            private: DisconnectConnectionBuilderImpl * m_disconnectconnectionbuilder_impl;
            private: friend class  _DisconnectConnectionBuilderBuilder;
            protected: DisconnectConnectionBuilder();
            public: ~DisconnectConnectionBuilder();
            /**Returns  an API that gives connector 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::SelectPointList * SelConnector
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
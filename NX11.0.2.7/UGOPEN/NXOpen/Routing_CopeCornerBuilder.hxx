#ifndef NXOpen_ROUTING_COPECORNERBUILDER_HXX_INCLUDED
#define NXOpen_ROUTING_COPECORNERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_CopeCornerBuilder.ja
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
#include <NXOpen/Routing_CopeCornerBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_routing_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Routing
    {
        class CopeCornerBuilder;
    }
    class Builder;
    namespace Routing
    {
        class Stock;
    }
    class SelectNXObject;
    class SelectNXObjectList;
    namespace Routing
    {
        class _CopeCornerBuilderBuilder;
        class CopeCornerBuilderImpl;
        /** Builder class for Cope Corner object <br> To create a new instance of this class, use @link NXOpen::Routing::RouteManager::CreateCopeCornerBuilder  NXOpen::Routing::RouteManager::CreateCopeCornerBuilder @endlink  <br> 
         <br>  @deprecated Deprecated in NX8.0.0.  Use @link NXOpen::Routing::AssignCornerBuilder NXOpen::Routing::AssignCornerBuilder@endlink  instead. <br>  

         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  NX_DEPRECATED("Deprecated in NX8.0.0.  Use NXOpen::Routing::AssignCornerBuilder instead.")  CopeCornerBuilder : public NXOpen::Builder
        {
            private: CopeCornerBuilderImpl * m_copecornerbuilder_impl;
            private: friend class  _CopeCornerBuilderBuilder;
            protected: CopeCornerBuilder();
            public: ~CopeCornerBuilder();
            /**Returns  the user selected @link NXOpen::Routing::ControlPoint NXOpen::Routing::ControlPoint@endlink 
                        for cope corner creation.
                    
             <br>  @deprecated Deprecated in NX8.0.0.  Use @link NXOpen::Routing::AssignCornerBuilder NXOpen::Routing::AssignCornerBuilder@endlink  instead. <br>  

             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Use NXOpen::Routing::AssignCornerBuilder instead.") NXOpen::SelectNXObject * SelectControlPoint
            (
            );
            /**Returns  the user selected correct object where correct object is
                        @link NXOpen::Routing::Stock NXOpen::Routing::Stock@endlink  and @link NXOpen::Routing::ISegment NXOpen::Routing::ISegment@endlink .
                     
             <br>  @deprecated Deprecated in NX8.0.0.  Use @link NXOpen::Routing::AssignCornerBuilder NXOpen::Routing::AssignCornerBuilder@endlink  instead. <br>  

             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Use NXOpen::Routing::AssignCornerBuilder instead.") NXOpen::SelectNXObjectList * SelectCopeStock
            (
            );
            /** Set the @link NXOpen::Routing::Stock NXOpen::Routing::Stock@endlink  object list when list box
                        is updated. 
             <br>  @deprecated Deprecated in NX8.0.0.  Use @link NXOpen::Routing::AssignCornerBuilder NXOpen::Routing::AssignCornerBuilder@endlink  instead. <br>  

             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced") */
            public:  NX_DEPRECATED("Deprecated in NX8.0.0.  Use NXOpen::Routing::AssignCornerBuilder instead.") void SetStockList
            (
                const std::vector<NXOpen::Routing::Stock *> & objects /** Routing Stocks for cope creation*/
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
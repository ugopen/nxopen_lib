#ifndef NXOpen_ASSEMBLIES_COMPONENTORDER_HXX_INCLUDED
#define NXOpen_ASSEMBLIES_COMPONENTORDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Assemblies_ComponentOrder.ja
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
#include <NXOpen/Assemblies_Order.hxx>
#include <NXOpen/libnxopencpp_assemblies_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Assemblies
    {
        class ComponentOrder;
    }
    namespace Assemblies
    {
        class Component;
    }
    namespace Assemblies
    {
        class ComponentAssembly;
    }
    namespace Assemblies
    {
        class Order;
    }
    namespace Assemblies
    {
        class _ComponentOrderBuilder;
        class ComponentOrderImpl;
        /**  Represents an order object that stores the order of child @link Assemblies::Component Assemblies::Component@endlink s in context
               of parent @link Assemblies::ComponentAssembly Assemblies::ComponentAssembly@endlink . Typically, an @link Assemblies::ComponentAssembly Assemblies::ComponentAssembly@endlink  
               can have multiple @link Assemblies::ComponentOrder Assemblies::ComponentOrder@endlink s and user can switch between 
               @link Assemblies::ComponentOrder Assemblies::ComponentOrder@endlink s to display different order of the assembly in the tree. 
          
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_ASSEMBLIESEXPORT  ComponentOrder : public Assemblies::Order
        {
            private: ComponentOrderImpl * m_componentorder_impl;
            private: friend class  _ComponentOrderBuilder;
            protected: ComponentOrder();
            public: ~ComponentOrder();
            /** Given a parent @link Assemblies::ComponentAssembly Assemblies::ComponentAssembly@endlink  this method
                    returns immediate child @link Assemblies::Component Assemblies::Component@endlink s in the same order in
                    which they are ordered in this @link Assemblies::ComponentOrder Assemblies::ComponentOrder@endlink  @return  Children of @link Assemblies::ComponentAssembly Assemblies::ComponentAssembly@endlink   
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Assemblies::Component *> AskChildrenOrder
            (
                NXOpen::Assemblies::ComponentAssembly * parent /** @link Assemblies::ComponentAssembly Assemblies::ComponentAssembly@endlink  whose children are required */
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
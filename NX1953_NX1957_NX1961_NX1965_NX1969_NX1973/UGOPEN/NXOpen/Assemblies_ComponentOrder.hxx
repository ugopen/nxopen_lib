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
        class Order;
    }
    namespace Assemblies
    {
        class _ComponentOrderBuilder;
        class ComponentOrderImpl;
        /**  Represents an order object that stores the order of child @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink s in context
               of parent @link NXOpen::Assemblies::ComponentAssembly NXOpen::Assemblies::ComponentAssembly@endlink . Typically, an @link NXOpen::Assemblies::ComponentAssembly NXOpen::Assemblies::ComponentAssembly@endlink  
               can have multiple @link NXOpen::Assemblies::ComponentOrder NXOpen::Assemblies::ComponentOrder@endlink s and user can switch between 
               @link NXOpen::Assemblies::ComponentOrder NXOpen::Assemblies::ComponentOrder@endlink s to display different order of the assembly in the tree. 
          
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_ASSEMBLIESEXPORT  ComponentOrder : public NXOpen::Assemblies::Order
        {
            private: ComponentOrderImpl * m_componentorder_impl;
            private: friend class  _ComponentOrderBuilder;
            protected: ComponentOrder();
            public: ~ComponentOrder();
            /** Given a parent @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink  this method
                    returns immediate child @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink s in the same order in
                    which they are ordered in this @link NXOpen::Assemblies::ComponentOrder NXOpen::Assemblies::ComponentOrder@endlink  @return  Children of @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink   
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Assemblies::Component *> AskChildrenOrder
            (
                NXOpen::Assemblies::Component * parent /** @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink  whose children are required */
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

#ifndef NXOpen_ASSEMBLIES_COMPONENTGROUP_HXX_INCLUDED
#define NXOpen_ASSEMBLIES_COMPONENTGROUP_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Assemblies_ComponentGroup.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/PartLoadStatus.hxx>
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
        class ComponentGroup;
    }
    namespace Assemblies
    {
        class Component;
    }
    class NXObject;
    class PartLoadStatus;
    namespace Assemblies
    {
        class _ComponentGroupBuilder;
        class ComponentGroupImpl;
        /** 
           Represents a Component Group that is defined within an Assembly.
           
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_ASSEMBLIESEXPORT  ComponentGroup : public NXOpen::NXObject
        {
            private: ComponentGroupImpl * m_componentgroup_impl;
            private: friend class  _ComponentGroupBuilder;
            protected: ComponentGroup();
            public: ~ComponentGroup();
            /** 
                   Loads a selected component group by name during Assembly part file open.

                    <br> 
                   This operation is used in conjunction with the @link NXOpen::LoadOptions NXOpen::LoadOptions@endlink 
                   enumerator @link NXOpen::LoadOptions::LoadComponents NXOpen::LoadOptions::LoadComponents@endlink  and using the
                   specify filter option.
                   This method is not intented to be used after an Assembly has been
                   loaded but during the loading operations.
                    <br> 

                    @return  Parts
                                             that could not be loaded and their associated errors. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: NXOpen::PartLoadStatus * Open
            (
            );
            /**Returns  the number of Components within this Component Group 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: int NumberOfComponents
            (
            );
            /** Returns the Components within this Component Group  @return  the components 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Assemblies::Component *> GetComponents
            (
            );
            /** Adds a component to a component group.  If add chilren is true, the children of the added component
                       are also added.
                   
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void AddComponent
            (
                NXOpen::Assemblies::Component * component /** the component to add */,
                bool andChildren /** if true add chilren of component also */
            );
            /** Removes a component from a component group 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES") */
            public: void RemoveComponent
            (
                NXOpen::Assemblies::Component * component /** the component to remove */
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

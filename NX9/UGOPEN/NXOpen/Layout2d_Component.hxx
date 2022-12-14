#ifndef NXOpen_LAYOUT2D_COMPONENT_HXX_INCLUDED
#define NXOpen_LAYOUT2D_COMPONENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Layout2d_Component.ja
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
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/libnxopencpp_layout2d_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Layout2d
    {
        class Component;
    }
    class DisplayableObject;
    namespace Layout2d
    {
        class _ComponentBuilder;
        class ComponentImpl;
        /** Represents the Component object.  <br> To create or edit an instance of this class, use @link Layout2d::DefineComponentBuilder  Layout2d::DefineComponentBuilder @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_LAYOUT2DEXPORT  Component : public DisplayableObject
        {
            private: ComponentImpl * m_component_impl;
            private: friend class  _ComponentBuilder;
            protected: Component();
            public: ~Component();
            /** Activates the component. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            public: void Activate
            (
            );
            /** Deactivates the component. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            public: void Deactivate
            (
            );
            /**Returns  the active state of 2d component. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: bool IsActive
            (
            );
            /** Updates the component and all of its sub components. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            public: void Update
            (
            );
            /**Returns  the lock update status of 2d component.
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: bool LockUpdateStatus
            (
            );
            /**Sets  the lock update status of 2d component.
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            public: void SetLockUpdateStatus
            (
                bool lock /** lock */ 
            );
            /** Exits the component active status without committing the changes. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_drafting_plus ("DraftingPlus") */
            public: void ExitActivate
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

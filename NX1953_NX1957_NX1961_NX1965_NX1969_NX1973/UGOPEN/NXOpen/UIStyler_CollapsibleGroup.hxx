#ifndef NXOpen_UISTYLER_COLLAPSIBLEGROUP_HXX_INCLUDED
#define NXOpen_UISTYLER_COLLAPSIBLEGROUP_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     UIStyler_CollapsibleGroup.ja
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
#include <NXOpen/UIStyler_StylerItem.hxx>
#include <NXOpen/UIStyler_StylerItem.hxx>
#include <NXOpen/libnxopenuicpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace UIStyler
    {
        class CollapsibleGroup;
    }
    namespace UIStyler
    {
        class StylerItem;
    }
    namespace UIStyler
    {
        class CollapsibleGroupImpl;
        /** Represents a Collapsible Group for UI Styler 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENUICPPEXPORT  CollapsibleGroup : public NXOpen::UIStyler::StylerItem
        {
            private: CollapsibleGroupImpl * m_collapsiblegroup_impl;
            /// \cond NX_NO_DOC 
            public: explicit CollapsibleGroup(void *ptr);
            /// \endcond 
            /**Sets label of collapsible group
             <br>  Created in NX6.0.5.  <br>  
             <br> License requirements : None */
            public: void SetLabel
            (
                const NXString & strLabel /** Text to be set as label */
            );
            /**Sets label of collapsible group
             <br>  Created in NX6.0.5.  <br>  
             <br> License requirements : None */
            void SetLabel
            (
                const char * strLabel /** Text to be set as label */
            );
            /**Returns the visibility
             <br>  Created in NX6.0.5.  <br>  
             <br> License requirements : None */
            public: bool Visibility
            (
            );
            /**Sets the visibility
             <br>  Created in NX6.0.5.  <br>  
             <br> License requirements : None */
            public: void SetVisibility
            (
                bool type /** type */ 
            );
            /**Returns the collapse-state
             <br>  Created in NX6.0.5.  <br>  
             <br> License requirements : None */
            public: bool CollapseState
            (
            );
            /**Sets the collapse-state
             <br>  Created in NX6.0.5.  <br>  
             <br> License requirements : None */
            public: void SetCollapseState
            (
                bool itemVal /** item val */ 
            );
        }; //lint !e1712 default constructor not defined for class  

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

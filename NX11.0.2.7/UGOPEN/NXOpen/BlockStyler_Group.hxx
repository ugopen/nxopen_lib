#ifndef NXOpen_BLOCKSTYLER_GROUP_HXX_INCLUDED
#define NXOpen_BLOCKSTYLER_GROUP_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     BlockStyler_Group.ja
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
#include <NXOpen/BlockStyler_Group.hxx>
#include <NXOpen/BlockStyler_UIBlock.hxx>
#include <NXOpen/BlockStyler_UIBlock.hxx>
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
    namespace BlockStyler
    {
        class Group;
    }
    namespace BlockStyler
    {
        class PropertyList;
    }
    namespace BlockStyler
    {
        class UIBlock;
    }
    namespace BlockStyler
    {
        class _GroupBuilder;
        class GroupImpl;
        /** Represents a Group Block
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENUICPPEXPORT  Group : public NXOpen::BlockStyler::UIBlock
        {
            private: GroupImpl * m_group_impl;
            private: friend class  _GroupBuilder;
            protected: Group();
            public: ~Group();
            /**Returns  the Column
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: int Column
            (
            );
            /**Sets  the Column
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetColumn
            (
                int numColumn /** num column */ 
            );
            /**Returns  the Localize
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool Localize
            (
            );
            /**Sets  the Localize
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetLocalize
            (
                bool localize /** localize */ 
            );
            /**Returns  the Members
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::BlockStyler::PropertyList * Members
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
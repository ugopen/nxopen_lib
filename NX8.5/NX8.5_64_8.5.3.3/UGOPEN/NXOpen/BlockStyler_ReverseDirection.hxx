#ifndef NXOpen_BLOCKSTYLER_REVERSEDIRECTION_HXX_INCLUDED
#define NXOpen_BLOCKSTYLER_REVERSEDIRECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     BlockStyler_ReverseDirection.ja
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
#include <NXOpen/BlockStyler_UIBlock.hxx>
#include <NXOpen/BlockStyler_ReverseDirection.hxx>
#include <NXOpen/ugmath.hxx>
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
        class ReverseDirection;
    }
    namespace BlockStyler
    {
        class UIBlock;
    }
    namespace BlockStyler
    {
        class _ReverseDirectionBuilder;
        class ReverseDirectionImpl;
        /** Represents Reverse Direction block
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENUICPPEXPORT  ReverseDirection : public BlockStyler::UIBlock
        {
            private: ReverseDirectionImpl * m_reversedirection_impl;
            private: friend class  _ReverseDirectionBuilder;
            protected: ReverseDirection();
            public: ~ReverseDirection();
            /**Returns  the Direction. It specifies the orientation of direction handle.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Vector3d Direction
            (
            );
            /**Sets  the Direction. It specifies the orientation of direction handle.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetDirection
            (
                const NXOpen::Vector3d & direction /** direction */ 
            );
            /**Returns  the Flip. If true, the handle is flipped opposite of the direction.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool Flip
            (
            );
            /**Sets  the Flip. If true, the handle is flipped opposite of the direction.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetFlip
            (
                bool flip /** flip */ 
            );
            /**Returns  the Origin. It specifies the origin of direction handle.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point3d Origin
            (
            );
            /**Sets  the Origin. It specifies the origin of direction handle.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetOrigin
            (
                const NXOpen::Point3d & origin /** origin */ 
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
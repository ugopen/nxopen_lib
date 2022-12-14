#ifndef NXOpen_CAM_CONTACTMOVEBUILDER_HXX_INCLUDED
#define NXOpen_CAM_CONTACTMOVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ContactMoveBuilder.ja
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
#include <NXOpen/CAM_MoveBuilder.hxx>
#include <NXOpen/libnxopencpp_cam_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAM
    {
        class ContactMoveBuilder;
    }
    namespace CAM
    {
        class MoveBuilder;
    }
    namespace CAM
    {
        class ObjectContainer;
    }
    namespace CAM
    {
        class _ContactMoveBuilderBuilder;
        class ContactMoveBuilderImpl;

        /// \cond NX_NO_DOC 
        /** Represents the contact move  <br> To create a new instance of this class, use @link NXOpen::CAM::MoveCollection::CreateContactMoveBuilder  NXOpen::CAM::MoveCollection::CreateContactMoveBuilder @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  ContactMoveBuilder : public NXOpen::CAM::MoveBuilder
        {
            /** the tool side */

            /// \cond NX_NO_DOC 
            public: enum ToolSide
            {
                ToolSideLeft/** Left */,
                ToolSideRight/** Right */
            };


            /// \endcond 
            private: ContactMoveBuilderImpl * m_contactmovebuilder_impl;
            private: friend class  _ContactMoveBuilderBuilder;
            protected: ContactMoveBuilder();
            public: ~ContactMoveBuilder();

            /// \cond NX_NO_DOC 
            /**Returns  the tool side 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ContactMoveBuilder::ToolSide ToolSideDirection
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the tool side 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void SetToolSideDirection
            (
                NXOpen::CAM::ContactMoveBuilder::ToolSide toolSide /** toolside */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the move container 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ObjectContainer * MoveContainer
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

#ifndef NXOpen_CAM_MERGEPATHSUBTRACTIVEBUILDER_HXX_INCLUDED
#define NXOpen_CAM_MERGEPATHSUBTRACTIVEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MergePathSubtractiveBuilder.ja
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
#include <NXOpen/CAM_NCGroupBuilder.hxx>
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
        class MergePathSubtractiveBuilder;
    }
    namespace CAM
    {
        class NCGroupBuilder;
    }
    namespace CAM
    {
        class NcmScBuilder;
    }
    namespace CAM
    {
        class _MergePathSubtractiveBuilderBuilder;
        class MergePathSubtractiveBuilderImpl;

        /// \cond NX_NO_DOC 
        /** Represents a merge path subtractive builder  <br> To create a new instance of this class, use @link NXOpen::CAM::NCGroupCollection::CreateMergePathSubtractiveBuilder  NXOpen::CAM::NCGroupCollection::CreateMergePathSubtractiveBuilder @endlink  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  MergePathSubtractiveBuilder : public NXOpen::CAM::NCGroupBuilder
        {
            private: MergePathSubtractiveBuilderImpl * m_mergepathsubtractivebuilder_impl;
            private: friend class  _MergePathSubtractiveBuilderBuilder;
            protected: MergePathSubtractiveBuilder();
            public: ~MergePathSubtractiveBuilder();

            /// \cond NX_NO_DOC 
            /**Returns  the non-cutting moves builder  
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::NcmScBuilder * NonCuttingBuilder
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
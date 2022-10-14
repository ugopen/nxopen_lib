#ifndef NXOpen_CAM_MERGEPATHADDITIVE_HXX_INCLUDED
#define NXOpen_CAM_MERGEPATHADDITIVE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MergePathAdditive.ja
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
#include <NXOpen/CAM_NCGroup.hxx>
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
        class MergePathAdditive;
    }
    namespace CAM
    {
        class NCGroup;
    }
    namespace CAM
    {
        class _MergePathAdditiveBuilder;
        class MergePathAdditiveImpl;
        /** Represents a Merge Path Additive group  <br> To obtain an instance of this class use @link NXOpen::CAM::NCGroupCollection NXOpen::CAM::NCGroupCollection@endlink   <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  MergePathAdditive : public NXOpen::CAM::NCGroup
        {
            private: MergePathAdditiveImpl * m_mergepathadditive_impl;
            private: friend class  _MergePathAdditiveBuilder;
            protected: MergePathAdditive();
            public: ~MergePathAdditive();
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
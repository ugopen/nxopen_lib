#ifndef NXOpen_CAE_QUALITYAUDIT_MESHLEVELLENGTHRATIORANGECHECK_HXX_INCLUDED
#define NXOpen_CAE_QUALITYAUDIT_MESHLEVELLENGTHRATIORANGECHECK_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_QualityAudit_MeshLevelLengthRatioRangeCheck.ja
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
#include <NXOpen/CAE_QualityAudit_Action.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        namespace QualityAudit
        {
            class MeshLevelLengthRatioRangeCheck;
        }
    }
    namespace CAE
    {
        namespace QualityAudit
        {
            class Action;
        }
    }
    namespace CAE
    {
        namespace QualityAudit
        {
            class _MeshLevelLengthRatioRangeCheckBuilder;
            class MeshLevelLengthRatioRangeCheckImpl;
            /**  @brief  This action checks the ratio between two consecutive supports after meshing. 

               <br> To obtain all the actions see @link CAE::QualityAudit::ActionList CAE::QualityAudit::ActionList@endlink .  <br> 
             <br>  Created in NX1847.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  MeshLevelLengthRatioRangeCheck : public NXOpen::CAE::QualityAudit::Action
            {
                private: MeshLevelLengthRatioRangeCheckImpl * m_meshlevellengthratiorangecheck_impl;
                private: friend class  _MeshLevelLengthRatioRangeCheckBuilder;
                protected: MeshLevelLengthRatioRangeCheck();
                public: ~MeshLevelLengthRatioRangeCheck();
            };
        }
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

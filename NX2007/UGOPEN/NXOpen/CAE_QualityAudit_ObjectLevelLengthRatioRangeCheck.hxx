#ifndef NXOpen_CAE_QUALITYAUDIT_OBJECTLEVELLENGTHRATIORANGECHECK_HXX_INCLUDED
#define NXOpen_CAE_QUALITYAUDIT_OBJECTLEVELLENGTHRATIORANGECHECK_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_QualityAudit_ObjectLevelLengthRatioRangeCheck.ja
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
            class ObjectLevelLengthRatioRangeCheck;
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
            class _ObjectLevelLengthRatioRangeCheckBuilder;
            class ObjectLevelLengthRatioRangeCheckImpl;
            /**  @brief  This action checks the ratio between two consecutive supports before meshing. 

               <br> To obtain all the actions see @link CAE::QualityAudit::ActionList CAE::QualityAudit::ActionList@endlink .  <br> 
             <br>  Created in NX1847.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  ObjectLevelLengthRatioRangeCheck : public NXOpen::CAE::QualityAudit::Action
            {
                private: ObjectLevelLengthRatioRangeCheckImpl * m_objectlevellengthratiorangecheck_impl;
                private: friend class  _ObjectLevelLengthRatioRangeCheckBuilder;
                protected: ObjectLevelLengthRatioRangeCheck();
                public: ~ObjectLevelLengthRatioRangeCheck();
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
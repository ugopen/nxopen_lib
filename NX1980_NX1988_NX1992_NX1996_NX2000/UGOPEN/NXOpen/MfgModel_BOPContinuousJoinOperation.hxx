#ifndef NXOpen_MFGMODEL_BOPCONTINUOUSJOINOPERATION_HXX_INCLUDED
#define NXOpen_MFGMODEL_BOPCONTINUOUSJOINOPERATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MfgModel_BOPContinuousJoinOperation.ja
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
#include <NXOpen/MfgModel_BOPOperation.hxx>
#include <NXOpen/libmfgmodelopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace MfgModel
    {
        class BOPContinuousJoinOperation;
    }
    namespace MfgModel
    {
        class BOPOperation;
    }
    namespace MfgModel
    {
        class _BOPContinuousJoinOperationBuilder;
        class BOPContinuousJoinOperationImpl;

        /// \cond NX_NO_DOC 
        /** Represents BOPContinuousJoinOperation Instance 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class MFGMODELOPENCPPEXPORT  BOPContinuousJoinOperation : public NXOpen::MfgModel::BOPOperation
        {
            private: BOPContinuousJoinOperationImpl * m_bopcontinuousjoinoperation_impl;
            private: friend class  _BOPContinuousJoinOperationBuilder;
            protected: BOPContinuousJoinOperation();
            public: ~BOPContinuousJoinOperation();
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

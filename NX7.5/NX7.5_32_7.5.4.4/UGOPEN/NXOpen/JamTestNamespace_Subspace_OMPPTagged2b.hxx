#ifndef NXOpen_JAMTESTNAMESPACE_SUBSPACE_OMPPTAGGED2B_HXX_INCLUDED
#define NXOpen_JAMTESTNAMESPACE_SUBSPACE_OMPPTAGGED2B_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     JamTestNamespace_Subspace_OMPPTagged2b.ja
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
#include <NXOpen/JamTestNamespace_Subspace_OMPPTagged2.hxx>
#include <NXOpen/JamTestNamespace_Subspace_OMPPTagged2b.hxx>
#include <NXOpen/JamTestNamespace_Subspace_OMPPTagged2.hxx>
#include <NXOpen/libnxopenjamtestcpp_exports.hxx>
namespace NXOpen
{
    namespace JamTestNamespace
    {
        namespace Subspace
        {
            class OMPPTagged2b;
        }
    }
    namespace JamTestNamespace
    {
        namespace Subspace
        {
            class OMPPTagged2;
        }
    }
    namespace JamTestNamespace
    {
        namespace Subspace
        {
            class _OMPPTagged2bBuilder;
            class OMPPTagged2bImpl;
            /** Test class for testing a class inside a nested namespace  <br> This is a testing class. <br> */
            class NXOPENJAMTESTCPPEXPORT  OMPPTagged2b : public JamTestNamespace::Subspace::OMPPTagged2
            {
                private: OMPPTagged2bImpl * m_ompptagged2b_impl;
                private: friend class  _OMPPTagged2bBuilder;
                protected: OMPPTagged2b();
                public: ~OMPPTagged2b();
                /** Test method  @return   <br> License requirements : None */
                public: double DivideBy10
                (
                    int input /** input */ 
                );
                /** Returns a data struct  @return   <br> License requirements : None */
                public: NXOpen::JamTestNamespace::Subspace::OMPPTagged2::Struct1 GetStruct
                (
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif

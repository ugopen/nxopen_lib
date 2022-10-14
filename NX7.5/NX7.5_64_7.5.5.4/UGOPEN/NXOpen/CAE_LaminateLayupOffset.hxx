#ifndef NXOpen_CAE_LAMINATELAYUPOFFSET_HXX_INCLUDED
#define NXOpen_CAE_LAMINATELAYUPOFFSET_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_LaminateLayupOffset.ja
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
#include <NXOpen/CAE_LaminateLayupOffset.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class LaminateLayupOffset;
    }
    class NXObject;
    namespace CAE
    {
        class _LaminateLayupOffsetBuilder;
        class LaminateLayupOffsetImpl;
        /**  @brief  laminate layup offset  

          */
        class NXOPENCPPEXPORT  LaminateLayupOffset : public NXObject
        {
            private: LaminateLayupOffsetImpl * m_laminatelayupoffset_impl;
            private: friend class  _LaminateLayupOffsetBuilder;
            protected: LaminateLayupOffset();
            public: ~LaminateLayupOffset();
            /**Returns  the name of the layup offset  <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: NXString LayupOffsetName
            (
            );
            /**Sets  the name of the layup offset  <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetLayupOffsetName
            (
                const NXString & name /** the layup offset name */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
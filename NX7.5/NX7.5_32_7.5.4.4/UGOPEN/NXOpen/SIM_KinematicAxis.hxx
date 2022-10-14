#ifndef NXOpen_SIM_KINEMATICAXIS_HXX_INCLUDED
#define NXOpen_SIM_KINEMATICAXIS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SIM_KinematicAxis.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace SIM
    {
        class KinematicAxis;
    }
    class NXObject;
    namespace SIM
    {
        class _KinematicAxisBuilder;
        class KinematicAxisImpl;
        /**  @brief  Represents the SimKimAxis class object  

            <br> Use the @link KinematicAxisBuilder KinematicAxisBuilder@endlink  class to create a KinematicAxis object. <br> */
        class NXOPENCPPEXPORT  KinematicAxis : public NXObject
        {
            private: KinematicAxisImpl * m_kinematicaxis_impl;
            private: friend class  _KinematicAxisBuilder;
            protected: KinematicAxis();
            public: ~KinematicAxis();
        };
    }
}
#undef EXPORTLIBRARY
#endif
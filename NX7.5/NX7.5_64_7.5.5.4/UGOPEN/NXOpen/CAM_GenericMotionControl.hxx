#ifndef NXOpen_CAM_GENERICMOTIONCONTROL_HXX_INCLUDED
#define NXOpen_CAM_GENERICMOTIONCONTROL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_GenericMotionControl.ja
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
#include <NXOpen/CAM_Operation.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class GenericMotionControl;
    }
    namespace CAM
    {
        class Operation;
    }
    namespace CAM
    {
        class _GenericMotionControlBuilder;
        class GenericMotionControlImpl;
        /** Represents a Generic Motion Control operation */
        class NXOPENCPPEXPORT  GenericMotionControl : public CAM::Operation
        {
            private: GenericMotionControlImpl * m_genericmotioncontrol_impl;
            private: friend class  _GenericMotionControlBuilder;
            protected: GenericMotionControl();
            public: ~GenericMotionControl();
        };
    }
}
#undef EXPORTLIBRARY
#endif

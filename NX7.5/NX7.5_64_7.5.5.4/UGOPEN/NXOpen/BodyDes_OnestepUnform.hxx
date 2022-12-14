#ifndef NXOpen_BODYDES_ONESTEPUNFORM_HXX_INCLUDED
#define NXOpen_BODYDES_ONESTEPUNFORM_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     BodyDes_OnestepUnform.ja
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
#include <NXOpen/Features_Feature.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace BodyDes
    {
        class OnestepUnform;
    }
    namespace Features
    {
        class Feature;
    }
    namespace BodyDes
    {
        class _OnestepUnformBuilder;
        class OnestepUnformImpl;
        /** Represents a onestep unform feature */
        class NXOPENCPPEXPORT  OnestepUnform : public Features::Feature
        {
            private: OnestepUnformImpl * m_onestepunform_impl;
            private: friend class  _OnestepUnformBuilder;
            protected: OnestepUnform();
            public: ~OnestepUnform();
        };
    }
}
#undef EXPORTLIBRARY
#endif

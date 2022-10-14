#ifndef NXOpen_CAE_CAEBODY_HXX_INCLUDED
#define NXOpen_CAE_CAEBODY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_CAEBody.ja
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
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/IBody.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class CAEBody;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class DisplayableObject;
    class IBody;
    class INXObject;
    namespace CAE
    {
        class _CAEBodyBuilder;
        class CAEBodyImpl;
        /**  @brief  Represents a CAE body geometry  

          */
        class NXOPENCPPEXPORT  CAEBody : public DisplayableObject, public virtual IBody
        {
            private: CAEBodyImpl * m_caebody_impl;
            private: friend class  _CAEBodyBuilder;
            protected: CAEBody();
            public: ~CAEBody();
        };
    }
}
#undef EXPORTLIBRARY
#endif
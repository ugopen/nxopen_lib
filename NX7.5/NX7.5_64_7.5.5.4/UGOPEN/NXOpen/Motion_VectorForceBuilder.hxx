#ifndef NXOpen_MOTION_VECTORFORCEBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_VECTORFORCEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_VectorForceBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/Motion_VObject.hxx>
#include <NXOpen/Motion_VectorForceBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class VectorForceBuilder;
    }
    class Builder;
    namespace Motion
    {
        class VObject;
    }
    namespace Motion
    {
        class _VectorForceBuilderBuilder;
        class VectorForceBuilderImpl;
        /**
            Represents a @link Motion::VectorForceBuilder Motion::VectorForceBuilder@endlink 
             <br> To create a new instance of this class, use @link Motion::VectorForceCollection::CreateVectorForceBuilder Motion::VectorForceCollection::CreateVectorForceBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  VectorForceBuilder : public Builder
        {
            private: VectorForceBuilderImpl * m_vectorforcebuilder_impl;
            private: friend class  _VectorForceBuilderBuilder;
            protected: VectorForceBuilder();
            public: ~VectorForceBuilder();
            /**Returns  the vobject data  <br> License requirements : None */
            public: NXOpen::Motion::VObject * VObject
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
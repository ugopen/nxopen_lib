#ifndef NXOpen_CAE_RESPONSESIMULATION_BASEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_BASEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_BaseBuilder.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class BaseBuilder;
        }
    }
    class Builder;
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class ObjectLabel;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _BaseBuilderBuilder;
            class BaseBuilderImpl;
            /** Represents the abstract builder class for all objects defined in response analysis meta solution  <br> This is an abstract class, and cannot be created. <br> */
            class NXOPENCPPEXPORT  BaseBuilder : public Builder
            {
                private: BaseBuilderImpl * m_basebuilder_impl;
                private: friend class  _BaseBuilderBuilder;
                protected: BaseBuilder();
                public: ~BaseBuilder();
                /**Returns  the object label  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::ObjectLabel * ObjectLabel
                (
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
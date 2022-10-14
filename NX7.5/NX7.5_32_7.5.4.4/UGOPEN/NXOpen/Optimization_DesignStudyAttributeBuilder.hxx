#ifndef NXOpen_OPTIMIZATION_DESIGNSTUDYATTRIBUTEBUILDER_HXX_INCLUDED
#define NXOpen_OPTIMIZATION_DESIGNSTUDYATTRIBUTEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Optimization_DesignStudyAttributeBuilder.ja
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
#include <NXOpen/Optimization_DesignStudyAttributeBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Optimization
    {
        class DesignStudyAttributeBuilder;
    }
    class Builder;
    class NXObject;
    namespace Optimization
    {
        class _DesignStudyAttributeBuilderBuilder;
        class DesignStudyAttributeBuilderImpl;
        /** Represents a @link Optimization::DesignStudyAttributeBuilder Optimization::DesignStudyAttributeBuilder@endlink   <br> To create a new instance of this class, use @link Optimization::DesignStudyCollection::CreateDesignStudyAttributeBuilder Optimization::DesignStudyCollection::CreateDesignStudyAttributeBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  DesignStudyAttributeBuilder : public Builder
        {
            private: DesignStudyAttributeBuilderImpl * m_designstudyattributebuilder_impl;
            private: friend class  _DesignStudyAttributeBuilderBuilder;
            protected: DesignStudyAttributeBuilder();
            public: ~DesignStudyAttributeBuilder();
            /** Adopt object  <br> License requirements : None */
            public: void AdoptObject
            (
                NXOpen::NXObject * object /** Object to adopt */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
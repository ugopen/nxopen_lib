#ifndef NXOpen_ANNOTATIONS_BASESURFACEFINISHBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_BASESURFACEFINISHBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_BaseSurfaceFinishBuilder.ja
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
#include <NXOpen/Annotations_PmiAttributeBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class BaseSurfaceFinishBuilder;
    }
    namespace Annotations
    {
        class PmiAttributeBuilder;
    }
    namespace Annotations
    {
        class _BaseSurfaceFinishBuilderBuilder;
        class BaseSurfaceFinishBuilderImpl;
        /** Represents a @link Annotations::BaseSurfaceFinish Annotations::BaseSurfaceFinish@endlink  builder  <br> This is an abstract class, and cannot be instantiated. <br> */
        class NXOPENCPPEXPORT  BaseSurfaceFinishBuilder : public Annotations::PmiAttributeBuilder
        {
            /** the valid surface finish tolerance types */
            public: enum ToleranceOption
            {
                ToleranceOptionNone/** No tolerance */,
                ToleranceOptionEqualBilateral/** Equal bilateral */,
                ToleranceOptionBilateral/** Bilateral */,
                ToleranceOptionUnilateralPlus/** Unilateral plus */,
                ToleranceOptionUnilateralMinus/** Unilateral minus */,
                ToleranceOptionPlusLimitTwoLines/** Plus limit two lines */,
                ToleranceOptionMinusLimitTwoLines/** Minus limit two lines*/,
                ToleranceOptionPlusLimitOneLine/** Plus limit one line*/,
                ToleranceOptionMinusLimitOneLine/** Minus limit one line*/
            };

            /** the valid parantheses types */
            public: enum ParanthesesType
            {
                ParanthesesTypeNone/** None */,
                ParanthesesTypeLeft/** Left */,
                ParanthesesTypeRight/** Right */,
                ParanthesesTypeBoth/** Both */
            };

            private: BaseSurfaceFinishBuilderImpl * m_basesurfacefinishbuilder_impl;
            private: friend class  _BaseSurfaceFinishBuilderBuilder;
            protected: BaseSurfaceFinishBuilder();
            public: ~BaseSurfaceFinishBuilder();
        };
    }
}
#undef EXPORTLIBRARY
#endif

#ifndef NXOpen_GEOMETRICUTILITIES_PATTERNINCREMENTSBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_PATTERNINCREMENTSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_PatternIncrementsBuilder.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/GeometricUtilities_PatternIncrementsBuilder.hxx>
#include <NXOpen/GeometricUtilities_PatternIncrementsList.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricUtilities
    {
        class PatternIncrementsBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricUtilities
    {
        class PatternIncrementsList;
    }
    namespace GeometricUtilities
    {
        class _PatternIncrementsBuilderBuilder;
        class PatternIncrementsBuilderImpl;
        /** pattern increments builder */
        class NXOPENCPPEXPORT  PatternIncrementsBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            private: PatternIncrementsBuilderImpl * m_patternincrementsbuilder_impl;
            private: friend class  _PatternIncrementsBuilderBuilder;
            protected: PatternIncrementsBuilder();
            public: ~PatternIncrementsBuilder();
            /**Returns  the increments @link GeometricUtilities::PatternIncrementsList GeometricUtilities::PatternIncrementsList@endlink  in Direction1.  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::PatternIncrementsList * IncrementsListInDirection1
            (
            );
            /**Returns  the increments @link GeometricUtilities::PatternIncrementsList GeometricUtilities::PatternIncrementsList@endlink  in Direction2.  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::PatternIncrementsList * IncrementsListInDirection2
            (
            );
            /** Returns true if the inputs to the component are sufficient for 
                        commit to be called.  For example, if the component requires
                        you to set some property, this method will return false if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful  <br> License requirements : None */
            public: virtual bool Validate
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif

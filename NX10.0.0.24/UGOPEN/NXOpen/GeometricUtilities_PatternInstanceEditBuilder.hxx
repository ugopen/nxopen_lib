#ifndef NXOpen_GEOMETRICUTILITIES_PATTERNINSTANCEEDITBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_PATTERNINSTANCEEDITBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_PatternInstanceEditBuilder.ja
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
#include <NXOpen/GeometricUtilities_InstanceEditedExpressionsList.hxx>
#include <NXOpen/GeometricUtilities_PatternInstanceEditBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_geometricutilities_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace GeometricUtilities
    {
        class PatternInstanceEditBuilder;
    }
    class Builder;
    namespace GeometricUtilities
    {
        class InstanceEditedExpressionsList;
    }
    namespace GeometricUtilities
    {
        class _PatternInstanceEditBuilderBuilder;
        class PatternInstanceEditBuilderImpl;
        /** pattern instance edit builder  <br> To create a new instance of this class, use @link NXOpen::GeometricUtilities::PatternDefinition::CreatePatternInstanceEditBuilder  NXOpen::GeometricUtilities::PatternDefinition::CreatePatternInstanceEditBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  PatternInstanceEditBuilder : public NXOpen::Builder
        {
            private: PatternInstanceEditBuilderImpl * m_patterninstanceeditbuilder_impl;
            private: friend class  _PatternInstanceEditBuilderBuilder;
            protected: PatternInstanceEditBuilder();
            public: ~PatternInstanceEditBuilder();
            /**Returns  the edited expressions list @link GeometricUtilities::InstanceEditedExpressionsList GeometricUtilities::InstanceEditedExpressionsList@endlink . 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::InstanceEditedExpressionsList * EditedExpressionsList
            (
            );
            /** Sets the indices of the selected Pattern Instances whose expressions are to be edited with
                        the expressions provided in the @link GeometricUtilities::InstanceEditedExpressionsList GeometricUtilities::InstanceEditedExpressionsList@endlink . 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetSelectedInstances
            (
                const std::vector<int> & firstIndexOfSelectedInstances /** firstindexofselectedinstances */ ,
                const std::vector<int> & secondIndexOfSelectedInstances /** secondindexofselectedinstances */ 
            );
        };
    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif

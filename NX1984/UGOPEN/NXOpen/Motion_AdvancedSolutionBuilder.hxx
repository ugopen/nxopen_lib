#ifndef NXOpen_MOTION_ADVANCEDSOLUTIONBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_ADVANCEDSOLUTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_AdvancedSolutionBuilder.ja
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
#include <NXOpen/Motion_MotionBuilder.hxx>
#include <NXOpen/libnxopencpp_motion_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Motion
    {
        class AdvancedSolutionBuilder;
    }
    namespace Motion
    {
        class MotionBuilder;
    }
    namespace Motion
    {
        class _AdvancedSolutionBuilderBuilder;
        class AdvancedSolutionBuilderImpl;
        /** Represents a @link NXOpen::Motion::AdvancedSolution NXOpen::Motion::AdvancedSolution@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Motion::MotionSolutionCollection::CreateAdvancedSolutionBuilder  NXOpen::Motion::MotionSolutionCollection::CreateAdvancedSolutionBuilder @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  AdvancedSolutionBuilder : public NXOpen::Motion::MotionBuilder
        {
            private: AdvancedSolutionBuilderImpl * m_advancedsolutionbuilder_impl;
            private: friend class  _AdvancedSolutionBuilderBuilder;
            protected: AdvancedSolutionBuilder();
            public: ~AdvancedSolutionBuilder();
            /**Returns  the definition of text based element - MDF definition 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXString Definition
            (
            );
            /**Sets  the definition of text based element - MDF definition 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetDefinition
            (
                const NXString & definition /** definition */ 
            );
            /**Sets  the definition of text based element - MDF definition 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            void SetDefinition
            (
                const char * definition /** definition */ 
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
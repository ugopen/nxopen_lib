#ifndef NXOpen_MOTION_RESULTMEASUREBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_RESULTMEASUREBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_ResultMeasureBuilder.ja
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
#include <NXOpen/Motion_MotionSolution.hxx>
#include <NXOpen/Motion_ResultMeasure.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class ResultMeasureBuilder;
    }
    class Builder;
    namespace Motion
    {
        class MotionSolution;
    }
    class SelectNXObject;
    class TaggedObject;
    namespace Motion
    {
        class _ResultMeasureBuilderBuilder;
        class ResultMeasureBuilderImpl;
        /** Represents a @link NXOpen::Motion::ResultMeasure NXOpen::Motion::ResultMeasure@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Motion::ResultMeasureCollection::CreateResultMeasureBuilder  NXOpen::Motion::ResultMeasureCollection::CreateResultMeasureBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  ResultMeasureBuilder : public NXOpen::Builder
        {
            private: ResultMeasureBuilderImpl * m_resultmeasurebuilder_impl;
            private: friend class  _ResultMeasureBuilderBuilder;
            protected: ResultMeasureBuilder();
            public: ~ResultMeasureBuilder();
            /**Returns  the solution 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::MotionSolution * Solution
            (
            );
            /**Sets  the solution 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetSolution
            (
                NXOpen::Motion::MotionSolution * solution /** solution */ 
            );
            /**Returns  the result type 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::ResultMeasure::ResultType ResultType
            (
            );
            /**Sets  the result type 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetResultType
            (
                NXOpen::Motion::ResultMeasure::ResultType resultType /** resulttype */ 
            );
            /**Returns  the reference object 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::SelectNXObject * ReferenceObject
            (
            );
            /**Returns  the interference result type 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::ResultMeasure::InterferenceType InterferenceType
            (
            );
            /**Sets  the interference result type 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetInterferenceType
            (
                NXOpen::Motion::ResultMeasure::InterferenceType interferenceType /** interferencetype */ 
            );
            /**Returns  the expression name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXString ExpName
            (
            );
            /**Sets  the expression name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetExpName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the expression name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            void SetExpName
            (
                const char * name /** name */ 
            );
            /** Commits the Builder, and returns the created result measure object. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::TaggedObject * CommitResultMeasure
            (
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

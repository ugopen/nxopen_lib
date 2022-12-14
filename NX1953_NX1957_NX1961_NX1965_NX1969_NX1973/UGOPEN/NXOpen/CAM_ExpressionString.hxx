#ifndef NXOpen_CAM_EXPRESSIONSTRING_HXX_INCLUDED
#define NXOpen_CAM_EXPRESSIONSTRING_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ExpressionString.ja
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
#include <NXOpen/CAM_Typedefs.hxx>
#include <NXOpen/CAM_BaseBuilder.hxx>
#include <NXOpen/libnxopencpp_cam_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAM
    {
        class ExpressionString;
    }
    namespace CAM
    {
        class BaseBuilder;
    }
    namespace CAM
    {
        class _ExpressionStringBuilder;
        class ExpressionStringImpl;
        /** Represents expression string
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  ExpressionString : public NXOpen::CAM::BaseBuilder
        {
            private: ExpressionStringImpl * m_expressionstring_impl;
            private: friend class  _ExpressionStringBuilder;
            protected: ExpressionString();
            public: ~ExpressionString();

            /// \cond NX_NO_DOC 
            /**Returns  the intent 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::ParamValueIntent Intent
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the intent 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetIntent
            (
                NXOpen::CAM::ParamValueIntent newIntent /** the new source */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the string value 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Value
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the string value 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetValue
            (
                const NXString & newValue /** the new value */
            );
            /**Sets  the string value 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetValue
            (
                const char * newValue /** the new value */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the expression string 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Expression
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the expression string 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetExpression
            (
                const NXString & newValue /** the new value */
            );
            /**Sets  the expression string 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetExpression
            (
                const char * newValue /** the new value */
            );

            /// \endcond 
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

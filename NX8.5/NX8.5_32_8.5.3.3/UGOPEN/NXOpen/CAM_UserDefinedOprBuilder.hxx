#ifndef NXOpen_CAM_USERDEFINEDOPRBUILDER_HXX_INCLUDED
#define NXOpen_CAM_USERDEFINEDOPRBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_UserDefinedOprBuilder.ja
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
#include <NXOpen/CAM_OperationBuilder.hxx>
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
        class UserDefinedOprBuilder;
    }
    namespace CAM
    {
        class OperationBuilder;
    }
    namespace CAM
    {
        class _UserDefinedOprBuilderBuilder;
        class UserDefinedOprBuilderImpl;
        /** Represents a UserDefinedOpr Builder  <br> This is an abstract class, and cannot be instantiated.  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  UserDefinedOprBuilder : public CAM::OperationBuilder
        {
            private: UserDefinedOprBuilderImpl * m_userdefinedoprbuilder_impl;
            private: friend class  _UserDefinedOprBuilderBuilder;
            protected: UserDefinedOprBuilder();
            public: ~UserDefinedOprBuilder();
            /**Returns  the name  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXString EnvVarName
            (
            );
            /**Sets  the name  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetEnvVarName
            (
                const NXString & varName /**  the variable name */
            );
            /**Sets  the name  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            void SetEnvVarName
            (
                const char * varName /**  the variable name */
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

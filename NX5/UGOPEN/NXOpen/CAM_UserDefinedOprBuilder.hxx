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
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/CAM_OperationBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
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
        /** Represents a UserDefinedOpr Builder  <br> This is an abstract class, and cannot be instantiated. <br> */
        class NXOPENCPPEXPORT UserDefinedOprBuilder : public CAM::OperationBuilder
        {
            private: friend class  _UserDefinedOprBuilderBuilder;
            protected: UserDefinedOprBuilder();
            /**Returns  the name   <br> License requirements : None */
            public: NXString EnvVarName
            (
            );
            /**Sets  the name   <br> License requirements : None */
            public: void SetEnvVarName
            (
                const NXString & var_name /**  the variable name */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
#ifndef NXOpen_CAE_MODELANDLOADPREPROCESSEXPORTTOBINARYBUILDER_HXX_INCLUDED
#define NXOpen_CAE_MODELANDLOADPREPROCESSEXPORTTOBINARYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ModelAndLoadPreProcessExportToBinaryBuilder.ja
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
#include <NXOpen/CAE_ModelAndLoadPreProcessOperationBuilder.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class ModelAndLoadPreProcessExportToBinaryBuilder;
    }
    namespace CAE
    {
        class ModelAndLoadPreProcessOperationBuilder;
    }
    namespace CAE
    {
        class _ModelAndLoadPreProcessExportToBinaryBuilderBuilder;
        class ModelAndLoadPreProcessExportToBinaryBuilderImpl;
        /** Builds a @link NXOpen::CAE::ModelAndLoadPreProcessExportToBinary NXOpen::CAE::ModelAndLoadPreProcessExportToBinary@endlink 
            which represents an operation.  <br> This class has no kf creator.  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ModelAndLoadPreProcessExportToBinaryBuilder : public NXOpen::CAE::ModelAndLoadPreProcessOperationBuilder
        {
            private: ModelAndLoadPreProcessExportToBinaryBuilderImpl * m_modelandloadpreprocessexporttobinarybuilder_impl;
            private: friend class  _ModelAndLoadPreProcessExportToBinaryBuilderBuilder;
            protected: ModelAndLoadPreProcessExportToBinaryBuilder();
            public: ~ModelAndLoadPreProcessExportToBinaryBuilder();
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

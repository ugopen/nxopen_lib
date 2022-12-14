#ifndef NXOpen_TOOLING_SIZERIMPORTBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_SIZERIMPORTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_SIZERImportBuilder.ja
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
#include <NXOpen/Tooling_SIZERImportBuilder.hxx>
#include <NXOpen/libnxopencpp_tooling_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Tooling
    {
        class SIZERImportBuilder;
    }
    class BasePart;
    class Builder;
    namespace Tooling
    {
        class _SIZERImportBuilderBuilder;
        class SIZERImportBuilderImpl;
        /** Imports results for motor selection from SIZER drive design based on
                the sizing, configuration, and selection of drive components.  <br> To create a new instance of this class, use @link Tooling::SIZERCollection::CreateImportBuilder  Tooling::SIZERCollection::CreateImportBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  SIZERImportBuilder : public Builder
        {
            /** Represents the position mode. */
            public: enum PositionMode
            {
                PositionModeInferredOnly/** Inferred Only */,
                PositionModeAbsoluteOrigin/** Absolute Origin */,
                PositionModeSelectOrigin/** Select Origin */,
                PositionModeByConstraints/** By Constraints */,
                PositionModeMove/** Move */
            };

            private: SIZERImportBuilderImpl * m_sizerimportbuilder_impl;
            private: friend class  _SIZERImportBuilderBuilder;
            protected: SIZERImportBuilder();
            public: ~SIZERImportBuilder();
            /**Returns  the input *.mdex file, which is imported from SIZER. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString InputFile
            (
            );
            /**Sets  the input *.mdex file, which is imported from SIZER. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetInputFile
            (
                const NXString & filename /** filename */ 
            );
            /**Sets  the input *.mdex file, which is imported from SIZER. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            void SetInputFile
            (
                const char * filename /** filename */ 
            );
            /** Generates motor 3D model.  @return  Motor Part object 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::BasePart * GenerateMotorModel
            (
                const NXString & motorType /** Motor Type   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Generates motor 3D model.  @return  Motor Part object 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            NXOpen::BasePart * GenerateMotorModel
            (
                const char * motorType /** Motor Type   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the position method, which is used in adding to assembly. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::SIZERImportBuilder::PositionMode PositionMethod
            (
            );
            /**Sets  the position method, which is used in adding to assembly. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetPositionMethod
            (
                NXOpen::Tooling::SIZERImportBuilder::PositionMode positionMethod /** positionmethod */ 
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

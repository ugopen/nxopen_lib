#ifndef NXOpen_CAE_FUNCTIONBUILDER_HXX_INCLUDED
#define NXOpen_CAE_FUNCTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_FunctionBuilder.ja
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
#include <NXOpen/CAE_Function.hxx>
#include <NXOpen/CAE_XYFunctionDataTypes.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class FunctionBuilder;
    }
    class Builder;
    namespace CAE
    {
        class Function;
    }
    namespace CAE
    {
        class _FunctionBuilderBuilder;
        class FunctionBuilderImpl;
        /** This builder class is used to create or edit @link  CAE::Function   CAE::Function @endlink  objects.
            All:
            @link CAE::FunctionBuilder::SetName CAE::FunctionBuilder::SetName@endlink ,
            @link CAE::FunctionBuilder::SetTypes CAE::FunctionBuilder::SetTypes@endlink ,
            @link CAE::FunctionBuilder::SetUnits CAE::FunctionBuilder::SetUnits@endlink ;

            formula:
            @link CAE::FunctionBuilder::SetDefinitions CAE::FunctionBuilder::SetDefinitions@endlink ,
            @link CAE::FunctionBuilder::SetReferencedObjects CAE::FunctionBuilder::SetReferencedObjects@endlink ,
            @link CAE::FunctionBuilder::SetMathPlotData CAE::FunctionBuilder::SetMathPlotData@endlink ;

            table function:
            @link CAE::FunctionBuilder::SetTableData CAE::FunctionBuilder::SetTableData@endlink .
             <br> To create a new instance of this class, use @link CAE::FunctionCollection::CreateFunctionBuilder CAE::FunctionCollection::CreateFunctionBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  FunctionBuilder : public Builder
        {
            private: FunctionBuilderImpl * m_functionbuilder_impl;
            private: friend class  _FunctionBuilderBuilder;
            protected: FunctionBuilder();
            public: ~FunctionBuilder();
            /**Sets  the function name. For math function, the name is function name.
                        For table function, the name is the AFU file name with directory  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Returns  the function name. For math function, the name is function name.
                        For table function, the name is the AFU file name with directory  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: NXString Name
            (
            );
            /** Sets types of a function  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void SetTypes
            (
                NXOpen::CAE::Function::Type functionType /** Math function or Table function. */,
                NXOpen::CAE::XyFunctionMacroType macroType /** For Motion Simulation or Advanced Simulation or General Purpose. */,
                NXOpen::CAE::XyFunctionGeneralType generalType /** Data type of function.
                                                                                 If macro_type is @link CAE::XyFunctionMacroTypeMotion CAE::XyFunctionMacroTypeMotion@endlink ,
                                                                                 it must be @link CAE::XyFunctionGeneralTypeGeneral CAE::XyFunctionGeneralTypeGeneral@endlink  or
                                                                                            @link CAE::XyFunctionGeneralTypeTime CAE::XyFunctionGeneralTypeTime@endlink .
                                                                                 If macro_type is @link CAE::XyFunctionMacroTypeLoad CAE::XyFunctionMacroTypeLoad@endlink  or
                                                                                 it must be @link CAE::XyFunctionGeneralTypeGeneral CAE::XyFunctionGeneralTypeGeneral@endlink  or
                                                                                            @link CAE::XyFunctionGeneralTypeTime CAE::XyFunctionGeneralTypeTime@endlink  or
                                                                                            @link CAE::XyFunctionGeneralTypeSpectrum CAE::XyFunctionGeneralTypeSpectrum@endlink  or
                                                                                            @link CAE::XyFunctionGeneralTypePowerSpectralDensity CAE::XyFunctionGeneralTypePowerSpectralDensity@endlink  or
                                                                                            @link CAE::XyFunctionGeneralTypeShockResponseSpectrum CAE::XyFunctionGeneralTypeShockResponseSpectrum@endlink .
                                                                                 If macro_type is @link CAE::XyFunctionMacroTypeMaterial CAE::XyFunctionMacroTypeMaterial@endlink ,
                                                                                 it must be @link CAE::XyFunctionGeneralTypeGeneral CAE::XyFunctionGeneralTypeGeneral@endlink  or
                                                                                            @link CAE::XyFunctionGeneralTypeTime CAE::XyFunctionGeneralTypeTime@endlink  or
                                                                                            @link CAE::XyFunctionGeneralTypeTemperature CAE::XyFunctionGeneralTypeTemperature@endlink  or
                                                                                            @link CAE::XyFunctionGeneralTypeStressStrain CAE::XyFunctionGeneralTypeStressStrain@endlink  or
                                                                                            @link CAE::XyFunctionGeneralTypeLife CAE::XyFunctionGeneralTypeLife@endlink .
                                                                                 If macro_type is @link CAE::XyFunctionMacroTypeResponse CAE::XyFunctionMacroTypeResponse@endlink ,
                                                                                 it must be @link CAE::XyFunctionGeneralTypeGeneral CAE::XyFunctionGeneralTypeGeneral@endlink  or
                                                                                            @link CAE::XyFunctionGeneralTypeTime CAE::XyFunctionGeneralTypeTime@endlink  or
                                                                                            @link CAE::XyFunctionGeneralTypeSpectrum CAE::XyFunctionGeneralTypeSpectrum@endlink  or
                                                                                            @link CAE::XyFunctionGeneralTypePowerSpectralDensity CAE::XyFunctionGeneralTypePowerSpectralDensity@endlink  or
                                                                                            @link CAE::XyFunctionGeneralTypeShockResponseSpectrum CAE::XyFunctionGeneralTypeShockResponseSpectrum@endlink  or
                                                                                            @link CAE::XyFunctionGeneralTypeCrossSpectrum CAE::XyFunctionGeneralTypeCrossSpectrum@endlink  or
                                                                                            @link CAE::XyFunctionGeneralTypeTransmissibility CAE::XyFunctionGeneralTypeTransmissibility@endlink . */
            );
            /** Returns types of a function  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void GetTypes
            (
                NXOpen::CAE::Function::Type* functionType /** Math function or Table function */,
                NXOpen::CAE::XyFunctionMacroType* macroType /** For Motion Simulation or Advanced Simulation or General Purpose */,
                NXOpen::CAE::XyFunctionGeneralType* generalType /** Data type of function */
            );
            /** Sets units of a function  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void SetUnits
            (
                NXOpen::CAE::XyFunctionUnit xUnit /** x unit */ ,
                NXOpen::CAE::XyFunctionUnit yUnit /** y unit */ ,
                NXOpen::CAE::XyFunctionUnit frfUnit /** frf unit */ 
            );
            /** Returns units of a function  <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void GetUnits
            (
                NXOpen::CAE::XyFunctionUnit* xUnit /** x unit */ ,
                NXOpen::CAE::XyFunctionUnit* yUnit /** y unit */ ,
                NXOpen::CAE::XyFunctionUnit* frfUnit /** frf unit */ 
            );
            /** Sets definition strings of a math function. Only used when function type
                        is @link CAE::Function::TypeMath CAE::Function::TypeMath@endlink   <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void SetDefinitions
            (
                std::vector<NXString> & definitions /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Returns definition strings of a math function. Only used when function type
                        is @link CAE::Function::TypeMath CAE::Function::TypeMath@endlink   @return   <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: std::vector<NXString> GetDefinitions
            (
            );
            /** Sets referenced objects of a math function. Only used when function type
                        is @link CAE::Function::TypeMath CAE::Function::TypeMath@endlink   <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void SetReferencedObjects
            (
                const std::vector<NXOpen::CAE::Function *> & objects /** objects */ 
            );
            /** Returns referenced objects of a math function. Only used when function type
                        is @link CAE::Function::TypeMath CAE::Function::TypeMath@endlink   @return   <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: std::vector<NXOpen::CAE::Function *> GetReferencedObjects
            (
            );
            /** Sets plot data setting for a math function. Only used when function type
                        is @link CAE::Function::TypeMath CAE::Function::TypeMath@endlink   <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void SetMathPlotData
            (
                int dataCount /** data count */ ,
                double xMinimum /** x minimum */ ,
                double xIncrement /** x increment */ 
            );
            /** Returns plot data setting of a math function. Only used when function type
                        is @link CAE::Function::TypeMath CAE::Function::TypeMath@endlink   <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void GetMathPlotData
            (
                int* dataCount /** data count */ ,
                double* xMinimum /** x minimum */ ,
                double* xIncrement /** x increment */ 
            );
            /** Sets data for a table function. Only used when function type
                        is @link CAE::Function::TypeTable CAE::Function::TypeTable@endlink   <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void SetTableData
            (
                int recordIndex /** Begins with one */,
                const NXString & recordName /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & recordTimestamp /** A time string indicating the creating or editing time of an afu record. 
                                                                     The string could be returned by @link CAE::AfuManager::CreateRecord CAE::AfuManager::CreateRecord@endlink 
                                                                     or @link CAE::AfuManager::EditRecord CAE::AfuManager::EditRecord@endlink 
                                                                     or @link CAE::AfuManager::GetAfuData CAE::AfuManager::GetAfuData@endlink    <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::CAE::Function::InterpolationMethod interpolateMethod /** interpolate method */ 
            );
            /** Returns data of a table function. Only used when function type
                        is @link CAE::Function::TypeTable CAE::Function::TypeTable@endlink   <br> License requirements : nx_ftk ("NX Advanced Graphing") */
            public: void GetTableData
            (
                int* recordIndex /**  Begins with one */,
                NXString* recordName /** record name */ ,
                NXString* recordTimestamp /** A time string indicating the last creating or editing time of an afu record */,
                NXOpen::CAE::Function::InterpolationMethod* interpolateMethod /** interpolate method */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
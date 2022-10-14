#ifndef NXOpen_CAE_AEROSTRUCTURES_AUTHOR_CALCULATIONCONTEXT_HXX_INCLUDED
#define NXOpen_CAE_AEROSTRUCTURES_AUTHOR_CALCULATIONCONTEXT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AeroStructures_Author_CalculationContext.ja
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
#include <NXOpen/CAE_AeroStructures_Author_AbbContext.hxx>
#include <NXOpen/CAE_AeroStructures_Author_InputParameter.hxx>
#include <NXOpen/CAE_AeroStructures_Author_OutputParameter.hxx>
#include <NXOpen/CAE_AeroStructures_Author_OutputScalar.hxx>
#include <NXOpen/CAE_AeroStructures_LoadCase.hxx>
#include <NXOpen/NXObject.hxx>
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
        namespace AeroStructures
        {
            namespace Author
            {
                class CalculationContext;
            }
        }
    }
    namespace CAE
    {
        namespace AeroStructures
        {
            namespace Author
            {
                class AbbContext;
            }
        }
    }
    namespace CAE
    {
        namespace AeroStructures
        {
            namespace Author
            {
                class InputParameter;
            }
        }
    }
    namespace CAE
    {
        namespace AeroStructures
        {
            namespace Author
            {
                class OutputParameter;
            }
        }
    }
    namespace CAE
    {
        namespace AeroStructures
        {
            namespace Author
            {
                class OutputScalar;
            }
        }
    }
    namespace CAE
    {
        namespace AeroStructures
        {
            class LoadCase;
        }
    }
    class NXObject;
    class Unit;
    namespace CAE
    {
        namespace AeroStructures
        {
            namespace Author
            {
                class _CalculationContextBuilder;
                class CalculationContextImpl;
                /**  @brief  Calculation context is passed to the method implementation. 
                                  It contains methods to retrieve the load case set and input parameter values,
                                  method to set the output values and log messages   

                   <br> No support for KF  <br> 
                 <br>  Created in NX12.0.0.  <br>  
                */
                class NXOPENCPP_CAEEXPORT  CalculationContext : public NXOpen::NXObject
                {
                    /**
                                Unit systems that can be used by a calculation method.
                            */
                    public: enum UnitSystem
                    {
                        UnitSystemMetric/** Metric Unit System */,
                        UnitSystemEnglish/** SI Unit System */,
                        UnitSystemSi/** English Unit System */,
                        UnitSystemUnknown/** Unknown Unit System */
                    };

                    private: CalculationContextImpl * m_calculationcontext_impl;
                    private: friend class  _CalculationContextBuilder;
                    protected: CalculationContext();
                    public: ~CalculationContext();
                    /**Returns  the name. 
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    public: NXString Name
                    (
                    );
                    /** Get the load case array used by the calculation
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    public: void GetLoadCaseArray
                    (
                        std::vector<NXOpen::CAE::AeroStructures::LoadCase *> & lcarray /** lcarray */ 
                    );
                    /** Get an input parameter  @return  
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    public: NXOpen::CAE::AeroStructures::Author::InputParameter * GetInput
                    (
                        const NXString & inputName /** inputname */ 
                    );
                    /** Get an input parameter  @return  
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    NXOpen::CAE::AeroStructures::Author::InputParameter * GetInput
                    (
                        const char * inputName /** inputname */ 
                    );
                    /** Get MS output parameter  @return  
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    public: NXOpen::CAE::AeroStructures::Author::OutputScalar * GetOutputMs
                    (
                    );
                    /** Get an output parameter  @return  
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    public: NXOpen::CAE::AeroStructures::Author::OutputParameter * GetOutput
                    (
                        const NXString & outputName /** outputname */ 
                    );
                    /** Get an output parameter  @return  
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    NXOpen::CAE::AeroStructures::Author::OutputParameter * GetOutput
                    (
                        const char * outputName /** outputname */ 
                    );
                    /** Get unit from its name 
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    public: NXOpen::Unit * GetUnit
                    (
                        const NXString & unitName /** unitname */ 
                    );
                    /** Get unit from its name 
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    NXOpen::Unit * GetUnit
                    (
                        const char * unitName /** unitname */ 
                    );
                    /** Log an info message
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    public: void Log
                    (
                        const NXString & message /** an info message */
                    );
                    /** Log an info message
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    void Log
                    (
                        const char * message /** an info message */
                    );
                    /** Log an info message indexed by possibly empty failure mode and load case
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    public: void Log
                    (
                        const NXString & failureMode /** a failure mode name (an empty string indicates that the message is not failure mode specific)*/,
                        int lcIndex /** load case index corresponding to the load case position in the load case array of the calculation context starting from 0 (-1 means that the message is not load case specific) */,
                        const NXString & message /** an info message*/
                    );
                    /** Log an info message indexed by possibly empty failure mode and load case
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    void Log
                    (
                        const char * failureMode /** a failure mode name (an empty string indicates that the message is not failure mode specific)*/,
                        int lcIndex /** load case index corresponding to the load case position in the load case array of the calculation context starting from 0 (-1 means that the message is not load case specific) */,
                        const char * message /** an info message*/
                    );
                    /** Log an info message indexed by possibly empty failure mode and load case
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    public: void Log
                    (
                        const NXString & failureMode /** a failure mode name (an empty string indicates that the message is not failure mode specific)*/,
                        const NXString & loadCase /** a load case name (an empty string indicates that the message is not load case specific)*/,
                        const NXString & message /** an info message */
                    );
                    /** Log an info message indexed by possibly empty failure mode and load case
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    void Log
                    (
                        const char * failureMode /** a failure mode name (an empty string indicates that the message is not failure mode specific)*/,
                        const char * loadCase /** a load case name (an empty string indicates that the message is not load case specific)*/,
                        const char * message /** an info message */
                    );
                    /** Log a warning message
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    public: void Warn
                    (
                        const NXString & message /** a warning message */
                    );
                    /** Log a warning message
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    void Warn
                    (
                        const char * message /** a warning message */
                    );
                    /** Log a warning message indexed by possibly empty failure mode and load case
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    public: void Warn
                    (
                        const NXString & failureMode /** a failure mode name (an empty string indicates that the message is not failure mode specific)*/,
                        int lcIndex /** load case index corresponding to the load case position in the load case array of the calculation context starting from 0 (-1 means that the message is not load case specific) */,
                        const NXString & message /** a warning message*/
                    );
                    /** Log a warning message indexed by possibly empty failure mode and load case
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    void Warn
                    (
                        const char * failureMode /** a failure mode name (an empty string indicates that the message is not failure mode specific)*/,
                        int lcIndex /** load case index corresponding to the load case position in the load case array of the calculation context starting from 0 (-1 means that the message is not load case specific) */,
                        const char * message /** a warning message*/
                    );
                    /** Log a warning message indexed by possibly empty failure mode and load case
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    public: void Warn
                    (
                        const NXString & failureMode /** a failure mode name (an empty string indicates that the message is not failure mode specific)*/,
                        const NXString & loadCase /** a load case name (an empty string indicates that the message is not load case specific)*/,
                        const NXString & message /** a warning message */
                    );
                    /** Log a warning message indexed by possibly empty failure mode and load case
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    void Warn
                    (
                        const char * failureMode /** a failure mode name (an empty string indicates that the message is not failure mode specific)*/,
                        const char * loadCase /** a load case name (an empty string indicates that the message is not load case specific)*/,
                        const char * message /** a warning message */
                    );
                    /** Log an error message
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    public: void Error
                    (
                        const NXString & message /** an error message */
                    );
                    /** Log an error message
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    void Error
                    (
                        const char * message /** an error message */
                    );
                    /** Log an error message indexed by possibly empty failure mode and load case
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    public: void Error
                    (
                        const NXString & failureMode /** a failure mode name (an empty string indicates that the message is not failure mode specific)*/,
                        int lcIndex /** load case index corresponding to the load case position in the load case array of the calculation context starting from 0 (-1 means that the message is not load case specific) */,
                        const NXString & message /** an error message*/
                    );
                    /** Log an error message indexed by possibly empty failure mode and load case
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    void Error
                    (
                        const char * failureMode /** a failure mode name (an empty string indicates that the message is not failure mode specific)*/,
                        int lcIndex /** load case index corresponding to the load case position in the load case array of the calculation context starting from 0 (-1 means that the message is not load case specific) */,
                        const char * message /** an error message*/
                    );
                    /** Log an error message indexed by possibly empty failure mode and load case
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    public: void Error
                    (
                        const NXString & failureMode /** a failure mode name (an empty string indicates that the message is not failure mode specific)*/,
                        const NXString & loadCase /** a load case name (an empty string indicates that the message is not load case specific)*/,
                        const NXString & message /** an error message */
                    );
                    /** Log an error message indexed by possibly empty failure mode and load case
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    void Error
                    (
                        const char * failureMode /** a failure mode name (an empty string indicates that the message is not failure mode specific)*/,
                        const char * loadCase /** a load case name (an empty string indicates that the message is not load case specific)*/,
                        const char * message /** an error message */
                    );
                    /** Returns the ABB context object
                     <br>  Created in NX12.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    public: NXOpen::CAE::AeroStructures::Author::AbbContext * GetAbbContext
                    (
                    );
                    /** Creates and return a path to an empty temporary directory  @return  
                     <br>  Created in NX1872.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    public: NXString GetTempPath
                    (
                    );
                    /** Returns the unit type object for a given measure and unit name   @return  unit type of the measure 
                     <br>  Created in NX1926.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    public: NXOpen::Unit * GetUnitType
                    (
                        const NXString & measureName /** the input measure name */,
                        const NXString & unitSymbol /** the input unit name */
                    );
                    /** Returns the unit type object for a given measure and unit name   @return  unit type of the measure 
                     <br>  Created in NX1926.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    NXOpen::Unit * GetUnitType
                    (
                        const char * measureName /** the input measure name */,
                        const char * unitSymbol /** the input unit name */
                    );
                    /** Returns the unit type object for a given measure in the method unit system. The unit system
                                can be defined by an author in the definition of the method or by the user in the margin solution 
                                editor. If there is no method or solution unit system the method uses the current base unit system.
                             @return  unit type of the measure 
                     <br>  Created in NX1926.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    public: NXOpen::Unit * GetUnitForMeasure
                    (
                        const NXString & measureName /** the input measure name */
                    );
                    /** Returns the unit type object for a given measure in the method unit system. The unit system
                                can be defined by an author in the definition of the method or by the user in the margin solution 
                                editor. If there is no method or solution unit system the method uses the current base unit system.
                             @return  unit type of the measure 
                     <br>  Created in NX1926.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    NXOpen::Unit * GetUnitForMeasure
                    (
                        const char * measureName /** the input measure name */
                    );
                    /** Set Selected LC 
                     <br>  Created in NX1926.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    public: void SetSelectedLoadCase
                    (
                        int lcIndex /** load case index corresponding to the load case position in the load case array of the calculation context starting from 0 (-1 means that the message is not load case specific) */,
                        bool selected /** boolean for load case selection (or not) */
                    );
                    /** Set Selected LCs by array 
                     <br>  Created in NX1926.0.0.  <br>  
                     <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                    public: void SetSelectedLoadCases
                    (
                        const std::vector<int> & lcIndexes /** list of indexes for selected load cases */
                    );
                };
            }
        }
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
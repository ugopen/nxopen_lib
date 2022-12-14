#ifndef NXOpen_CAE_AEROSTRUCTURES_TABLEPARAMETER_HXX_INCLUDED
#define NXOpen_CAE_AEROSTRUCTURES_TABLEPARAMETER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AeroStructures_TableParameter.ja
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
#include <NXOpen/CAE_AeroStructures_Laminate.hxx>
#include <NXOpen/CAE_AeroStructures_ParameterDescriptor.hxx>
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
            class TableParameter;
        }
    }
    namespace CAE
    {
        namespace AeroStructures
        {
            class Laminate;
        }
    }
    class NXObject;
    class Unit;
    namespace CAE
    {
        namespace AeroStructures
        {
            class _TableParameterBuilder;
            class TableParameterImpl;
            /**  @brief  This is the TableParameter  

               <br> No support for KF  <br> 
             <br>  Created in NX1847.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  TableParameter : public NXOpen::NXObject
            {
                private: TableParameterImpl * m_tableparameter_impl;
                private: friend class  _TableParameterBuilder;
                protected: TableParameter();
                public: ~TableParameter();
                /**Returns  the size of the table 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                public: int Size
                (
                );
                /**Returns  the size parameter 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                public: NXString SizeParameter
                (
                );
                /**Returns  the size offset 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                public: int SizeOffset
                (
                );
                /** Returns a list of all column names 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                public: std::vector<NXString> GetColumnNames
                (
                );
                /** Returns the parameter type for a column 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                public: NXOpen::CAE::AeroStructures::ParameterDescriptor::ParameterType GetColumnType
                (
                    const NXString & columnName /** columnname */ 
                );
                /** Returns the parameter type for a column 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                NXOpen::CAE::AeroStructures::ParameterDescriptor::ParameterType GetColumnType
                (
                    const char * columnName /** columnname */ 
                );
                /** Get the values of an integer column 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                public: std::vector<int> GetIntegerValues
                (
                    const NXString & columnName /** columnname */ 
                );
                /** Get the values of an integer column 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                std::vector<int> GetIntegerValues
                (
                    const char * columnName /** columnname */ 
                );
                /** Get the values of a scalar column ("Not a number" values are returned as system NAN)
                These values are expressed in default unit type that can be retrieved by calling @link CAE::AeroStructures::TableParameter::GetUnitType CAE::AeroStructures::TableParameter::GetUnitType@endlink  
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                public: std::vector<double> GetScalarValues
                (
                    const NXString & columnName /** columnname */ 
                );
                /** Get the values of a scalar column ("Not a number" values are returned as system NAN)
                These values are expressed in default unit type that can be retrieved by calling @link CAE::AeroStructures::TableParameter::GetUnitType CAE::AeroStructures::TableParameter::GetUnitType@endlink  
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                std::vector<double> GetScalarValues
                (
                    const char * columnName /** columnname */ 
                );
                /** Get the values of a scalar column converted in a specified unit ("Not a number" values are returned as system NAN)
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                public: std::vector<double> GetScalarValues
                (
                    const NXString & columnName /** columnname */ ,
                    NXOpen::Unit * unitType /** unit type */ 
                );
                /** Get the values of a scalar column converted in a specified unit ("Not a number" values are returned as system NAN)
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                std::vector<double> GetScalarValues
                (
                    const char * columnName /** columnname */ ,
                    NXOpen::Unit * unitType /** unit type */ 
                );
                /** Get the measure name of a scalar column
                                Returns "Unitless" for unitless case
                              
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                public: NXString GetMeasure
                (
                    const NXString & columnName /** columnname */ 
                );
                /** Get the measure name of a scalar column
                                Returns "Unitless" for unitless case
                              
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                NXString GetMeasure
                (
                    const char * columnName /** columnname */ 
                );
                /** Get the unit type of a scalar column
                              * Returns null if the column is unitless
                              
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                public: NXOpen::Unit * GetUnitType
                (
                    const NXString & columnName /** columnname */ 
                );
                /** Get the unit type of a scalar column
                              * Returns null if the column is unitless
                              
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                NXOpen::Unit * GetUnitType
                (
                    const char * columnName /** columnname */ 
                );
                /** Get the value of a string column 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                public: std::vector<NXString> GetStringValues
                (
                    const NXString & columnName /** columnname */ 
                );
                /** Get the value of a string column 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                std::vector<NXString> GetStringValues
                (
                    const char * columnName /** columnname */ 
                );
                /** Get the value of a Boolean column 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                public: std::vector<bool> GetBooleanValues
                (
                    const NXString & columnName /** columnname */ 
                );
                /** Get the value of a Boolean column 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                std::vector<bool> GetBooleanValues
                (
                    const char * columnName /** columnname */ 
                );
                /** Get the values of a laminate column  @return  
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                public: std::vector<NXOpen::CAE::AeroStructures::Laminate *> GetLaminateValues
                (
                    const NXString & columnName /** columnname */ 
                );
                /** Get the values of a laminate column  @return  
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : sc_aero_environment ("Simcenter AeroStructures Environment"), sc_margin_safety ("Simcenter Margin Of Safety") */
                std::vector<NXOpen::CAE::AeroStructures::Laminate *> GetLaminateValues
                (
                    const char * columnName /** columnname */ 
                );
            };
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

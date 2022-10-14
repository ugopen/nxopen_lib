#ifndef NXOpen_PCBEXCHANGE_COMPSETTINGSBUILDER_HXX_INCLUDED
#define NXOpen_PCBEXCHANGE_COMPSETTINGSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PcbExchange_CompSettingsBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_pcbexchange_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PcbExchange
    {
        class CompSettingsBuilder;
    }
    class Builder;
    class Expression;
    class NXColor;
    namespace PcbExchange
    {
        class _CompSettingsBuilderBuilder;
        class CompSettingsBuilderImpl;
        /** Represents a builder to create or edit component settings.  <br> To create a new instance of this class, use @link NXOpen::PcbExchange::Manager::CreateCompSettingsBuilder  NXOpen::PcbExchange::Manager::CreateCompSettingsBuilder @endlink  <br> 
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_PCBEXCHANGEEXPORT  CompSettingsBuilder : public NXOpen::Builder
        {
            /** The model options. */
            public: enum ModelOption
            {
                ModelOptionZeroResistor/** zero resistor */ ,
                ModelOptionOneResistor/** one resistor */ ,
                ModelOptionTwoResistor/** two resistor */ ,
                ModelOptionNone/** none */ 
            };

            /** The element size options. */
            public: enum ElementSizeOption
            {
                ElementSizeOptionAuto/** auto */ ,
                ElementSizeOptionSpecify/** specify */ 
            };

            /** The element thickness options. */
            public: enum ElementThicknessOption
            {
                ElementThicknessOptionNull/** null */ ,
                ElementThicknessOptionSpecify/** specify */ 
            };

            /** This enum defines the material from options. */
            public: enum MaterialFromOption
            {
                MaterialFromOptionPCBMaterialLibrary/** pcbmaterial library */ ,
                MaterialFromOptionNXMaterialLibrary/** nxmaterial library */ 
            };

            private: CompSettingsBuilderImpl * m_compsettingsbuilder_impl;
            private: friend class  _CompSettingsBuilderBuilder;
            protected: CompSettingsBuilder();
            public: ~CompSettingsBuilder();
            /**Returns  the model option. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PcbExchange::CompSettingsBuilder::ModelOption Model
            (
            );
            /**Sets  the model option. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_maya_exchange ("Unigraphics NX PCB Exchange") */
            public: void SetModel
            (
                NXOpen::PcbExchange::CompSettingsBuilder::ModelOption model /** model */ 
            );
            /**Returns  the case to board resistance for one-resistor models. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ThetaCB
            (
            );
            /**Returns  the junction to case resistance for two-resistor models. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ThetaJC
            (
            );
            /**Returns  the junction to board resistance for two-resistor models. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ThetaJB
            (
            );
            /**Returns  the junction capacitance for two-resistor models. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * JunctionCapacitance
            (
            );
            /**Returns  the maximum temperature for zero-resistor and one-resistor models. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Tmax
            (
            );
            /**Returns  the maximum case temperature for two-resistor models. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * TmaxCase
            (
            );
            /**Returns  the maximum junction temperature for two-resistor models. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * TmaxJunction
            (
            );
            /**Returns  the dissipation. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Dissipation
            (
            );
            /**Returns  the element size option. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PcbExchange::CompSettingsBuilder::ElementSizeOption ElementSizeEnum
            (
            );
            /**Sets  the element size option. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_maya_exchange ("Unigraphics NX PCB Exchange") */
            public: void SetElementSizeEnum
            (
                NXOpen::PcbExchange::CompSettingsBuilder::ElementSizeOption elementSizeEnum /** elementsizeenum */ 
            );
            /**Returns  the element size. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ElementSize
            (
            );
            /**Returns  the element thickness option. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PcbExchange::CompSettingsBuilder::ElementThicknessOption ElementThicknessEnum
            (
            );
            /**Sets  the element thickness option. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_maya_exchange ("Unigraphics NX PCB Exchange") */
            public: void SetElementThicknessEnum
            (
                NXOpen::PcbExchange::CompSettingsBuilder::ElementThicknessOption elementThicknessEnum /** elementthicknessenum */ 
            );
            /**Returns  the element thickness. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ElementThickness
            (
            );
            /**Returns  the material from option. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PcbExchange::CompSettingsBuilder::MaterialFromOption MaterialFrom
            (
            );
            /**Sets  the material from option. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_maya_exchange ("Unigraphics NX PCB Exchange") */
            public: void SetMaterialFrom
            (
                NXOpen::PcbExchange::CompSettingsBuilder::MaterialFromOption materialFrom /** materialfrom */ 
            );
            /**Returns  the PCB case material. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: int CasePcbMaterial
            (
            );
            /**Sets  the PCB case material. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_maya_exchange ("Unigraphics NX PCB Exchange") */
            public: void SetCasePcbMaterial
            (
                int casePcbMaterial /** casepcbmaterial */ 
            );
            /**Returns  the NX case material 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: int CaseNxMaterial
            (
            );
            /**Sets  the NX case material 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_maya_exchange ("Unigraphics NX PCB Exchange") */
            public: void SetCaseNxMaterial
            (
                int caseNxMaterial /** casenxmaterial */ 
            );
            /**Returns  the element color. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * Elementcolor
            (
            );
            /**Sets  the element color. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_maya_exchange ("Unigraphics NX PCB Exchange") */
            public: void SetElementcolor
            (
                NXOpen::NXColor * elementcolor /** elementcolor */ 
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
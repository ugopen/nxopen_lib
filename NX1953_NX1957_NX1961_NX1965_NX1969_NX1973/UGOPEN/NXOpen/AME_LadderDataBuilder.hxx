#ifndef NXOpen_AME_LADDERDATABUILDER_HXX_INCLUDED
#define NXOpen_AME_LADDERDATABUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_LadderDataBuilder.ja
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
#include <NXOpen/Diagramming_Tables_Table.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libameopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace AME
    {
        class LadderDataBuilder;
    }
    class Builder;
    namespace Diagramming
    {
        namespace Tables
        {
            class Table;
        }
    }
    namespace AME
    {
        class _LadderDataBuilderBuilder;
        class LadderDataBuilderImpl;
        /** Represents a method used in the ladder data <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::LadderDataBuilder  NXOpen::AME::AMEManager::LadderDataBuilder @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  LadderDataBuilder : public NXOpen::Builder
        {
            /** Represents the type of ladder */
            public: enum Ladders
            {
                LaddersOne/** one */  = 1,
                LaddersTwo/** two */ 
            };

            private: LadderDataBuilderImpl * m_ladderdatabuilder_impl;
            private: friend class  _LadderDataBuilderBuilder;
            protected: LadderDataBuilder();
            public: ~LadderDataBuilder();
            /**Returns   the number of ladders 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: int NumberOfLadders
            (
            );
            /**Sets   the number of ladders 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetNumberOfLadders
            (
                int ladders /** ladders */ 
            );
            /**Returns   the number of ladders 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: int LinesPerLadder
            (
            );
            /**Sets   the number of ladders 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetLinesPerLadder
            (
                int line /** line */ 
            );
            /**Returns  the devisions start value for ladder1 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString StartValueLadder1
            (
            );
            /**Sets  the devisions start value for ladder1 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetStartValueLadder1
            (
                const NXString & value1 /** value1 */ 
            );
            /**Sets  the devisions start value for ladder1 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetStartValueLadder1
            (
                const char * value1 /** value1 */ 
            );
            /**Returns  the devisions start value for ladder2 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString StartValueLadder2
            (
            );
            /**Sets  the devisions start value for ladder2 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetStartValueLadder2
            (
                const NXString & value2 /** value2 */ 
            );
            /**Sets  the devisions start value for ladder2 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetStartValueLadder2
            (
                const char * value2 /** value2 */ 
            );
            /**Returns  the height of the divisions 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: int DisplayDigit
            (
            );
            /**Sets  the height of the divisions 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetDisplayDigit
            (
                int display /** display */ 
            );
            /** Set cursor location on the sheet 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetLadderStartLocation
            (
                const NXOpen::Point2d & point /** point */ 
            );
            /** Create ladder data table 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void MakeLadderDataTable
            (
                NXOpen::Diagramming::Tables::Table * table /** table */ 
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

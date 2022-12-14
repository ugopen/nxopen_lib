#ifndef NXOpen_DATEITEMBUILDER_HXX_INCLUDED
#define NXOpen_DATEITEMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     DateItemBuilder.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class DateItemBuilder;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class _DateItemBuilderBuilder;
    class DateItemBuilderImpl;
    /**
        This class stores a date and time.    The class does verify that the year string and time string
        are in a valid format.  The first date supported is 2-Jan-1900 00:00:00 UTC and the last date supported
        is 31st-Dec-9999 00:00:00 UTC. Though note that the time input is in local time and converted to UTC internally.
        
        NOTE: The class does NOT verify that the combination of day, month, year and time is valid.
        
         <br> To create a new instance of this class, use @link NXOpen::DateBuilder::CreateDateItemBuilder  NXOpen::DateBuilder::CreateDateItemBuilder @endlink  <br> 
     <br>  Created in NX8.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  DateItemBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
    {
        /** Days of the month */
        public: enum DayOfMonth
        {
            DayOfMonthDay01/** day01 */ ,
            DayOfMonthDay02/** day02 */ ,
            DayOfMonthDay03/** day03 */ ,
            DayOfMonthDay04/** day04 */ ,
            DayOfMonthDay05/** day05 */ ,
            DayOfMonthDay06/** day06 */ ,
            DayOfMonthDay07/** day07 */ ,
            DayOfMonthDay08/** day08 */ ,
            DayOfMonthDay09/** day09 */ ,
            DayOfMonthDay10/** day10 */ ,
            DayOfMonthDay11/** day11 */ ,
            DayOfMonthDay12/** day12 */ ,
            DayOfMonthDay13/** day13 */ ,
            DayOfMonthDay14/** day14 */ ,
            DayOfMonthDay15/** day15 */ ,
            DayOfMonthDay16/** day16 */ ,
            DayOfMonthDay17/** day17 */ ,
            DayOfMonthDay18/** day18 */ ,
            DayOfMonthDay19/** day19 */ ,
            DayOfMonthDay20/** day20 */ ,
            DayOfMonthDay21/** day21 */ ,
            DayOfMonthDay22/** day22 */ ,
            DayOfMonthDay23/** day23 */ ,
            DayOfMonthDay24/** day24 */ ,
            DayOfMonthDay25/** day25 */ ,
            DayOfMonthDay26/** day26 */ ,
            DayOfMonthDay27/** day27 */ ,
            DayOfMonthDay28/** day28 */ ,
            DayOfMonthDay29/** day29 */ ,
            DayOfMonthDay30/** day30 */ ,
            DayOfMonthDay31/** day31 */ ,
            DayOfMonthBlank/** blank */ 
        };

        /** Months of the year. */
        public: enum MonthOfYear
        {
            MonthOfYearJan/** jan */ ,
            MonthOfYearFeb/** feb */ ,
            MonthOfYearMar/** mar */ ,
            MonthOfYearApr/** apr */ ,
            MonthOfYearMay/** may */ ,
            MonthOfYearJun/** jun */ ,
            MonthOfYearJul/** jul */ ,
            MonthOfYearAug/** aug */ ,
            MonthOfYearSep/** sep */ ,
            MonthOfYearOct/** oct */ ,
            MonthOfYearNov/** nov */ ,
            MonthOfYearDec/** dec */ ,
            MonthOfYearBlank/** blank */ 
        };

        private: DateItemBuilderImpl * m_dateitembuilder_impl;
        private: friend class  _DateItemBuilderBuilder;
        protected: DateItemBuilder();
        public: ~DateItemBuilder();
        /**Returns  the day 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::DateItemBuilder::DayOfMonth Day
        (
        );
        /**Sets  the day 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void SetDay
        (
            NXOpen::DateItemBuilder::DayOfMonth day /** day */ 
        );
        /**Returns  the month 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::DateItemBuilder::MonthOfYear Month
        (
        );
        /**Sets  the month 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void SetMonth
        (
            NXOpen::DateItemBuilder::MonthOfYear month /** month */ 
        );
        /**Returns  the year.  The year string is four characters long and represents an integer within
                    the range minimum year and maximum year (inclusive). The year can also be an empty string. 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: NXString Year
        (
        );
        /**Sets  the year.  The year string is four characters long and represents an integer within
                    the range minimum year and maximum year (inclusive). The year can also be an empty string. 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void SetYear
        (
            const NXString & year /** year */ 
        );
        /**Sets  the year.  The year string is four characters long and represents an integer within
                    the range minimum year and maximum year (inclusive). The year can also be an empty string. 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        void SetYear
        (
            const char * year /** year */ 
        );
        /**Returns  the time. The time string is a 24-hour clock time in the format HH:MM:SS or HH:MM.  The
                    string can also be empty.  
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: NXString Time
        (
        );
        /**Sets  the time. The time string is a 24-hour clock time in the format HH:MM:SS or HH:MM.  The
                    string can also be empty.  
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void SetTime
        (
            const NXString & time /** time */ 
        );
        /**Sets  the time. The time string is a 24-hour clock time in the format HH:MM:SS or HH:MM.  The
                    string can also be empty.  
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        void SetTime
        (
            const char * time /** time */ 
        );
        /** Validate whether the inputs to the component are sufficient for 
                    commit to be called.  If the component is not in a state to commit
                    then an exception is thrown.  For example, if the component requires
                    you to set some property, this method will throw an exception if
                    you haven't set it.  This method throws a not-yet-implemented
                    NXException for some components.
                 @return  Was self validation successful 
         <br>  Created in NX3.0.1.  <br>  
         <br> License requirements : None */
        public: virtual bool Validate
        (
        );
    };
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

#ifndef NXOpen_COMPAREAUTOTESTPRINT_HXX_INCLUDED
#define NXOpen_COMPAREAUTOTESTPRINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CompareAutotestPrint.ja
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
#include <NXOpen/GeometricUtilities_BodyCompareBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class CompareAutotestPrint;
    class DebugSession;
    namespace GeometricUtilities
    {
        class BodyCompareBuilder;
    }
    class CompareAutotestPrintImpl;

    /// \cond NX_NO_DOC 
    /** Represents a class that is used for NX testing.  This class should not be made available to customers  <br> To obtain an instance of this class, refer to @link NXOpen::DebugSession  NXOpen::DebugSession @endlink  <br> 
     <br>  Created in NX1953.0.0.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  CompareAutotestPrint
    {
        /** Compare Options */

        /// \cond NX_NO_DOC 
        public: enum OptionLevel
        {
            OptionLevelOne/** level 1 */,
            OptionLevelTwo/** level 2 */,
            OptionLevelThree/** level 3 */
        };


        /// \endcond 
        private: CompareAutotestPrintImpl * m_compareautotestprint_impl;
        private: NXOpen::DebugSession* m_owner;
        /// \cond NX_NO_DOC 
        public: explicit CompareAutotestPrint(NXOpen::DebugSession *owner);


        /// \endcond 
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~CompareAutotestPrint();

        /// \cond NX_NO_DOC 
        /** Print compare result to xml 
         <br>  Created in NX1953.0.0.  <br>  
         <br> License requirements : None */
        public: void PrintResult
        (
            NXOpen::GeometricUtilities::BodyCompareBuilder * builder /** compare builder to validate */,
            NXOpen::CompareAutotestPrint::OptionLevel level /** print options */
        );

        /// \endcond 
    }; //lint !e1712 default constructor not defined for class  


    /// \endcond 
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
#ifndef NXOpen_DRAFTINGDEBUGTOOL_HXX_INCLUDED
#define NXOpen_DRAFTINGDEBUGTOOL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     DraftingDebugTool.ja
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
    class DraftingDebugTool;
    class DebugSession;
    namespace Annotations
    {
        class Dimension;
    }
    class BasePart;
    class DraftingDebugToolImpl;

    /// \cond NX_NO_DOC 
    /** Represents a class that is used for NX testing.  This class should not
    be made available to customers  <br> To obtain an instance of this class, refer to @link NXOpen::DebugSession  NXOpen::DebugSession @endlink  <br> 
     <br>  Created in NX10.0.0.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  DraftingDebugTool
    {
        /** This reprensents the types of tests we can perform.*/
        public: enum Testtype
        {
            TesttypeUpgrade/** upgrade */ ,
            TesttypeRecreate/** recreate */ ,
            TesttypeNone/** none */ 
        };

        /** This reprensents the types of tolerance we will use.*/
        public: enum TestTolerance
        {
            TestToleranceDefault/** default */ ,
            TestToleranceAutoRounded/** auto rounded */ 
        };

        private: DraftingDebugToolImpl * m_draftingdebugtool_impl;
        private: NXOpen::DebugSession* m_owner;
        /// \cond NX_NO_DOC 
        public: explicit DraftingDebugTool(NXOpen::DebugSession *owner);


        /// \endcond 
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~DraftingDebugTool();
        /** This function takes in a dimension and perform a test on the dimension
         <br>  Created in NX10.0.0.  <br>  
         <br> License requirements : None */
        public: void TestDimension
        (
            NXOpen::Annotations::Dimension * dimension /** Dimension to test */,
            NXOpen::DraftingDebugTool::Testtype testType /** Test to perform */,
            NXOpen::DraftingDebugTool::TestTolerance testToleranceType /** Test Tolerance type */,
            bool doUpdate /** Whether to do update or not */,
            bool* isTestPass /** Is test pass */,
            NXString* testResults /** The Test results */
        );
        /** This function takes in a part file and perform tests on every dimension in the part
         <br>  Created in NX10.0.0.  <br>  
         <br> License requirements : None */
        public: void TestDimensions
        (
            NXOpen::BasePart * basePart /** Part to perform recreate tests */,
            NXOpen::DraftingDebugTool::Testtype testType /** Test to perform */,
            NXOpen::DraftingDebugTool::TestTolerance testToleranceType /** Test Tolerance type */,
            bool doUpdate /** Whether to do update or not */,
            bool moveFailsToAnotherLayer /** Whether to move the fails to another layer ror not */,
            int layerToMoveTo /** Layer to move the fails to */,
            bool stopWhenFail /** Whether to stop testing when a dimension failed the test or not*/,
            bool outputOnlyFails /** Whether only display the failed dimensions or not */,
            bool* isTestPass /** Is test pass */,
            std::vector<NXString> & entries /** The Test results */
        );
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

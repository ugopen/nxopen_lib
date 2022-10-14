#ifndef NXOpen_CAE_MODELCHECK_ELEMENTTESTRESULT_HXX_INCLUDED
#define NXOpen_CAE_MODELCHECK_ELEMENTTESTRESULT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ModelCheck_ElementTestResult.ja
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
#include <NXOpen/CAE_ModelCheck_TestResult.hxx>
#include <NXOpen/CAE_ModelCheck_TestValueTypes.hxx>
#include <NXOpen/TransientObject.hxx>
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
        namespace ModelCheck
        {
            class ElementTestResult;
        }
    }
    namespace CAE
    {
        class FEElement;
    }
    namespace CAE
    {
        namespace ModelCheck
        {
            class TestResult;
        }
    }
    namespace CAE
    {
        namespace ModelCheck
        {
        }
    }
    namespace CAE
    {
        namespace ModelCheck
        {
            class ElementTestResultImpl;
            /** Represents quality checking result for an element.   <br> To obtain an instance of this class use CAE.ModelCheck.ElementQualityCheckResults.GetElementTestResults  <br> 
             <br>  Created in NX8.5.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  ElementTestResult : public NXOpen::TransientObject
            {
                private: ElementTestResultImpl * m_elementtestresult_impl;
                /// \cond NX_NO_DOC 
                public: explicit ElementTestResult(void *ptr);
                /// \endcond 
                /** Frees the object from memory.  After this method is called,
                        it is illegal to use the object.  In .NET, this method is automatically
                        called when the object is deleted by the garbage collector.  
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: virtual ~ElementTestResult();
                /**Returns  the overall result of this element. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::ModelCheck::TestValueTypes::Result OverallResult
                (
                );
                /** Returns the quality test results of this element 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: std::vector<NXOpen::CAE::ModelCheck::TestResult *> GetTestResults
                (
                );
                /** Returns the element associated with quality test results 
                 <br>  Created in NX1961.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::FEElement * GetTestElement
                (
                );
            }; //lint !e1712 default constructor not defined for class  

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
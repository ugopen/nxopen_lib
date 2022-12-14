#ifndef NXOpen_FEATUREPROCESSBUILDERSTATUS_HXX_INCLUDED
#define NXOpen_FEATUREPROCESSBUILDERSTATUS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     FeatureProcessBuilderStatus.ja
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
#include <NXOpen/TransientObject.hxx>
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
    class FeatureProcessBuilderStatus;
    class FeatureProcessBuilderStatusImpl;
    /** 
     <br>  Created in NX7.5.0.  <br>  
    */
    class NXOPENCPPEXPORT  FeatureProcessBuilderStatus : public NXOpen::TransientObject
    {
        /** Result status enumeration to indicate the result status of feature process creation*/
        public: enum ResultStatus
        {
            ResultStatusNoError/** All operations have been created. No errors. */,
            ResultStatusOperationNotAllocated/** Some operations have been created, but others didn't. */,
            ResultStatusNoOperationsCreated/** No operations have been created. */
        };

        private: FeatureProcessBuilderStatusImpl * m_featureprocessbuilderstatus_impl;
        /// \cond NX_NO_DOC 
        public: explicit FeatureProcessBuilderStatus(void *ptr);
        /// \endcond 
        /** Free resources associated with the instance. After this method
            is called, it is illegal to use the object.  In .NET, this method
            is automatically called when the object is deleted by the garbage
            collector. 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: virtual ~FeatureProcessBuilderStatus();
        /** Returns a result status code for a feature process builder.  @return  
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::FeatureProcessBuilderStatus::ResultStatus GetResultStatus
        (
        );
        /** Sets a result status code for a feature process builder. 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: void SetResultStatus
        (
            NXOpen::FeatureProcessBuilderStatus::ResultStatus result /** result */ 
        );
    }; //lint !e1712 default constructor not defined for class  

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

#ifndef NXOpen_CAE_RESULTPARAMETERSWITHNODALFORCEREPORT_HXX_INCLUDED
#define NXOpen_CAE_RESULTPARAMETERSWITHNODALFORCEREPORT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResultParametersWithNodalForceReport.ja
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
#include <NXOpen/CAE_Result.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class ResultParametersWithNodalForceReport;
    }
    namespace CAE
    {
        class BaseIteration;
    }
    namespace CAE
    {
        class NodalForceReport;
    }
    class Unit;
    namespace CAE
    {
        class _ResultParametersWithNodalForceReportBuilder;
        class ResultParametersWithNodalForceReportImpl;
        /** 
             <br> To obtain an instance of this class use @link Session::ResultManager Session::ResultManager@endlink .  <br> 
         <br>  Created in NX11.0.2.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ResultParametersWithNodalForceReport : public NXOpen::TaggedObject
        {
            /** Post View result type options*/
            public: enum ResultType
            {
                ResultTypeForce/** force */ ,
                ResultTypeMoment/** moment */ 
            };

            private: ResultParametersWithNodalForceReportImpl * m_resultparameterswithnodalforcereport_impl;
            private: friend class  _ResultParametersWithNodalForceReportBuilder;
            protected: ResultParametersWithNodalForceReport();
            public: ~ResultParametersWithNodalForceReport();
            /** Ask NodalForceReport   @return   
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::NodalForceReport * GetNodalForceReport
            (
            );
            /** Ask current iteration   @return   
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::BaseIteration * GetCurrentIteration
            (
            );
            /** Set current iteration  
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetCurrentIteration
            (
                NXOpen::CAE::BaseIteration * iteration /** iteration */ 
            );
            /** Ask result unit  @return   
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::Unit * GetUnit
            (
            );
            /** Set result unit 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetUnit
            (
                NXOpen::Unit * unit /** unit */ 
            );
            /** Ask result type value  @return   
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::ResultParametersWithNodalForceReport::ResultType GetCurrentResultType
            (
            );
            /** Set result type value 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetCurrentResultType
            (
                NXOpen::CAE::ResultParametersWithNodalForceReport::ResultType resultType /** resulttype */ 
            );
            /** Ask result component value  @return   
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::Result::Component GetCurrentResultComp
            (
            );
            /** Set result component value 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetCurrentResultComp
            (
                NXOpen::CAE::Result::Component resultComp /** resultcomp */ 
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

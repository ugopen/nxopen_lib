#ifndef NXOpen_CAE_RESULTMEASURERESULTALLOPTIONS_HXX_INCLUDED
#define NXOpen_CAE_RESULTMEASURERESULTALLOPTIONS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResultMeasureResultAllOptions.ja
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
#include <NXOpen/CAE_ResultMeasureResultOptions.hxx>
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
        class ResultMeasureResultAllOptions;
    }
    namespace CAE
    {
        class ResultMeasureResultOptions;
    }
    namespace CAE
    {
    }
    namespace CAE
    {
        class ResultMeasureResultAllOptionsImpl;
        /**
            Represents the combination of all result options for result measure
             <br> To obtain an instance of this class use @link NXOpen::CAE::ResultMeasureCollection NXOpen::CAE::ResultMeasureCollection@endlink .  <br> 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ResultMeasureResultAllOptions : public NXOpen::CAE::ResultMeasureResultOptions
        {
            private: ResultMeasureResultAllOptionsImpl * m_resultmeasureresultalloptions_impl;
            /// \cond NX_NO_DOC 
            public: explicit ResultMeasureResultAllOptions(void *ptr);
            /// \endcond 
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: virtual ~ResultMeasureResultAllOptions();
            /** Set the coordinate system for directional components 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetCoordinateSystem
            (
                NXOpen::CAE::Result::CoordinateSystem eCsys /** ecsys */ 
            );
            /** Set the shell section for shell stress/strain results 
             <br>  @deprecated Deprecated in NX2007.0.0.  Use @link NXOpen::CAE::ResultMeasureResultAllOptions::SetResultShellSection NXOpen::CAE::ResultMeasureResultAllOptions::SetResultShellSection@endlink  instead <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX2007.0.0.  Use NXOpen::CAE::ResultMeasureResultAllOptions::SetResultShellSection instead") void SetShellSection
            (
                NXOpen::CAE::Result::Section eShellSect /** eshellsect */ 
            );
            /** Set the beam section for beam stress/strain results 
             <br>  @deprecated Deprecated in NX2007.0.0.  Use @link NXOpen::CAE::ResultMeasureResultAllOptions::SetResultBeamSection NXOpen::CAE::ResultMeasureResultAllOptions::SetResultBeamSection@endlink  instead <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX2007.0.0.  Use NXOpen::CAE::ResultMeasureResultAllOptions::SetResultBeamSection instead") void SetBeamSection
            (
                NXOpen::CAE::Result::Section eBeamSect /** ebeamsect */ 
            );
            /** Set the shell section for shell stress/strain results 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetResultShellSection
            (
                NXOpen::CAE::Result::ShellSection eShellSect /** eshellsect */ 
            );
            /** Set the beam section for beam stress/strain results 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetResultBeamSection
            (
                NXOpen::CAE::Result::BeamSection eBeamSect /** ebeamsect */ 
            );
            /** Set the option to calculate beam stresses for beam results only 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetCalculateBeamResults
            (
                bool bCalcBeamResults /** bcalcbeamresults */ 
            );
            /** Set the option to add beam fillets for calculation of beam stresses only 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetAddBeamFillets
            (
                bool bAddBeamFillets /** baddbeamfillets */ 
            );
            /** Set the beam fillet radius if adding beam fillets for calculation of beam results only 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetBeamFilletRadius
            (
                double beamFilletRadius /** beamfilletradius */ 
            );
        }; //lint !e1712 default constructor not defined for class  

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
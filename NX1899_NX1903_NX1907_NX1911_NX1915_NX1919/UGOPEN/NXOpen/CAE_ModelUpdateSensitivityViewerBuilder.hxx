#ifndef NXOpen_CAE_MODELUPDATESENSITIVITYVIEWERBUILDER_HXX_INCLUDED
#define NXOpen_CAE_MODELUPDATESENSITIVITYVIEWERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ModelUpdateSensitivityViewerBuilder.ja
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
#include <NXOpen/Builder.hxx>
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
        class ModelUpdateSensitivityViewerBuilder;
    }
    class Builder;
    namespace CAE
    {
        class _ModelUpdateSensitivityViewerBuilderBuilder;
        class ModelUpdateSensitivityViewerBuilderImpl;
        /** Represents @link NXOpen::CAE::ModelUpdateSensitivityViewerBuilder NXOpen::CAE::ModelUpdateSensitivityViewerBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::CAE::ModelUpdateSolutionCollection::CreateSensitivityViewerBuilder  NXOpen::CAE::ModelUpdateSolutionCollection::CreateSensitivityViewerBuilder @endlink  <br> 
         <br>  @deprecated Deprecated in NX1899.0.0.  Use @link NXOpen::CAE::ModelUpdateSolution::PlotSensitivities NXOpen::CAE::ModelUpdateSolution::PlotSensitivities@endlink  instead. <br>  

         <br>  Created in NX6.0.0.  <br>  
        */
        class NX_DEPRECATED("Deprecated in NX1899.0.0.  Use NXOpen::CAE::ModelUpdateSolution::PlotSensitivities instead.") NXOPENCPP_CAEEXPORT  ModelUpdateSensitivityViewerBuilder : public NXOpen::Builder
        {
            private: ModelUpdateSensitivityViewerBuilderImpl * m_modelupdatesensitivityviewerbuilder_impl;
            private: friend class  _ModelUpdateSensitivityViewerBuilderBuilder;
            protected: ModelUpdateSensitivityViewerBuilder();
            public: ~ModelUpdateSensitivityViewerBuilder();
            /** Gets the target IDs 
             <br>  @deprecated Deprecated in NX1899.0.0.  Use @link NXOpen::CAE::ModelUpdateSolution::PlotSensitivities NXOpen::CAE::ModelUpdateSolution::PlotSensitivities@endlink  instead. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Use NXOpen::CAE::ModelUpdateSolution::PlotSensitivities instead.") void GetTargetIds
            (
                std::vector<int> & targetIds /** SM allocated array containing the targets ID */
            );
            /** Sets the terget IDs 
             <br>  @deprecated Deprecated in NX1899.0.0.  Use @link NXOpen::CAE::ModelUpdateSolution::PlotSensitivities NXOpen::CAE::ModelUpdateSolution::PlotSensitivities@endlink  instead. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Use NXOpen::CAE::ModelUpdateSolution::PlotSensitivities instead.") void SetTargetIds
            (
                const std::vector<int> & targetIds /** The target IDs */
            );
            /** Gets the design variable labels  @return  SM allocated array containing the design variable labels 
             <br>  @deprecated Deprecated in NX1899.0.0.  Use @link NXOpen::CAE::ModelUpdateSolution::PlotSensitivities NXOpen::CAE::ModelUpdateSolution::PlotSensitivities@endlink  instead. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Use NXOpen::CAE::ModelUpdateSolution::PlotSensitivities instead.") std::vector<NXString> GetDesignVariableLabels
            (
            );
            /** Sets the design variable labels 
             <br>  @deprecated Deprecated in NX1899.0.0.  Use @link NXOpen::CAE::ModelUpdateSolution::PlotSensitivities NXOpen::CAE::ModelUpdateSolution::PlotSensitivities@endlink  instead. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Use NXOpen::CAE::ModelUpdateSolution::PlotSensitivities instead.") void SetDesignVariableLabels
            (
                std::vector<NXString> & designVaraibleLabels /** The design variable labels */
            );
            /** Gets the sensitivity values  @return  SM allocated array containing the sensitivity values 
             <br>  @deprecated Deprecated in NX1899.0.0.  Use @link NXOpen::CAE::ModelUpdateSolution::PlotSensitivities NXOpen::CAE::ModelUpdateSolution::PlotSensitivities@endlink  instead. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Use NXOpen::CAE::ModelUpdateSolution::PlotSensitivities instead.") std::vector<double> GetSensitivityValues
            (
            );
            /** Sets the sensitivity values 
             <br>  @deprecated Deprecated in NX1899.0.0.  Use @link NXOpen::CAE::ModelUpdateSolution::PlotSensitivities NXOpen::CAE::ModelUpdateSolution::PlotSensitivities@endlink  instead. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : nx_correl_update ("FE Model Update") */
            public: NX_DEPRECATED("Deprecated in NX1899.0.0.  Use NXOpen::CAE::ModelUpdateSolution::PlotSensitivities instead.") void SetSensitivityValues
            (
                const std::vector<double> & sensitivityValues /** The sensitivity values */
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

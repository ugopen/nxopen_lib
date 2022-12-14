#ifndef NXOpen_CAE_MODELCHECK_MODELSETUPCHECKBUILDER_HXX_INCLUDED
#define NXOpen_CAE_MODELCHECK_MODELSETUPCHECKBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ModelCheck_ModelSetupCheckBuilder.ja
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
        namespace ModelCheck
        {
            class ModelSetupCheckBuilder;
        }
    }
    class Builder;
    namespace CAE
    {
        namespace ModelCheck
        {
            class _ModelSetupCheckBuilderBuilder;
            class ModelSetupCheckBuilderImpl;
            /**Represents a @link NXOpen::CAE::ModelCheck::ModelSetupCheckBuilder NXOpen::CAE::ModelCheck::ModelSetupCheckBuilder@endlink  which can be
                used to check if the active @link NXOpen::CAE::SimSolution NXOpen::CAE::SimSolution@endlink  contains all the necessary 
                items for the analysis, including elements, loads, constraints and materials. Also it could check 
                label conficts and component connect status.
                @link Builder::Commit Builder::Commit@endlink  performs the check. The check result is written into a report
                file or listed in a separate information window, along with an error summary for each topic   <br> To create a new instance of this class, use @link NXOpen::CAE::ModelCheckManager::CreateModelSetupCheckBuilder  NXOpen::CAE::ModelCheckManager::CreateModelSetupCheckBuilder @endlink  <br> 
             <br>  Created in NX8.5.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  ModelSetupCheckBuilder : public NXOpen::Builder
            {
                private: ModelSetupCheckBuilderImpl * m_modelsetupcheckbuilder_impl;
                private: friend class  _ModelSetupCheckBuilderBuilder;
                protected: ModelSetupCheckBuilder();
                public: ~ModelSetupCheckBuilder();
                /**Returns  the value indicating whether to check labeling conflicts for node, element and coordindate system across component FEMS
                        and reports the label range in which the conflict occurs 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: bool CheckLabelConflicts
                (
                );
                /**Sets  the value indicating whether to check labeling conflicts for node, element and coordindate system across component FEMS
                        and reports the label range in which the conflict occurs 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
                public: void SetCheckLabelConflicts
                (
                    bool checkLabelConflicts /** checklabelconflicts */ 
                );
                /**Returns  the option specifying whether to check for component FEMs that are not connected  
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: bool CheckUnconnectedComponent
                (
                );
                /**Sets  the option specifying whether to check for component FEMs that are not connected  
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
                public: void SetCheckUnconnectedComponent
                (
                    bool checkUnconnectedComponent /** checkunconnectedcomponent */ 
                );
                /**Returns  the value indicating whether to check all components associated with the assembly FEM in the 
                            model check, regardless of load status. If false, only the fully loaded components are included 
                            in the check 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: bool CheckAllComponents
                (
                );
                /**Sets  the value indicating whether to check all components associated with the assembly FEM in the 
                            model check, regardless of load status. If false, only the fully loaded components are included 
                            in the check 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
                public: void SetCheckAllComponents
                (
                    bool checkAllComponents /** checkallcomponents */ 
                );
                /**Returns  the value indicating whether to list comprehensive descriptions of any problems and suggest
                            possible remedies. If false, only the simple descriptions of problems are listed 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: bool IsDetailedMessage
                (
                );
                /**Sets  the value indicating whether to list comprehensive descriptions of any problems and suggest
                            possible remedies. If false, only the simple descriptions of problems are listed 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
                public: void SetDetailedMessage
                (
                    bool isDetailedMessage /** isdetailedmessage */ 
                );
                /**Returns  the full name of the report file. If NULL, the report is listed in a separate listing window  
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXString ReportFileName
                (
                );
                /**Sets  the full name of the report file. If NULL, the report is listed in a separate listing window  
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
                public: void SetReportFileName
                (
                    const NXString & reportFileName /** reportfilename */ 
                );
                /**Sets  the full name of the report file. If NULL, the report is listed in a separate listing window  
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
                void SetReportFileName
                (
                    const char * reportFileName /** reportfilename */ 
                );
                /** Performs model setup check @return  Model setup checking result. Zero indicates the checking is successful 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
                public: int DoCheck
                (
                );
            };
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

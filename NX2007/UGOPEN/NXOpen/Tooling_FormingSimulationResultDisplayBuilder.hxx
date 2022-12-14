#ifndef NXOpen_TOOLING_FORMINGSIMULATIONRESULTDISPLAYBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_FORMINGSIMULATIONRESULTDISPLAYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_FormingSimulationResultDisplayBuilder.ja
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
#include <NXOpen/libnxopencpp_tooling_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Tooling
    {
        class FormingSimulationResultDisplayBuilder;
    }
    class Builder;
    namespace Tooling
    {
        class _FormingSimulationResultDisplayBuilderBuilder;
        class FormingSimulationResultDisplayBuilderImpl;
        /** Represents a forming simulation analysis - Result Display builder  <br> To create a new instance of this class, use @link NXOpen::Tooling::ProgressiveDieManager::CreateFormingSimulationResultDisplayBuilder  NXOpen::Tooling::ProgressiveDieManager::CreateFormingSimulationResultDisplayBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        FormabilityStrainType </term> <description> 
         
        TopPrincipalStrain </description> </item> 

        <item><term> 
         
        State </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        StrainType </term> <description> 
         
        TopFirstPriStrain </description> </item> 

        <item><term> 
         
        StressType </term> <description> 
         
        TopFirstPriStress </description> </item> 

        </list> 

         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  FormingSimulationResultDisplayBuilder : public NXOpen::Builder
        {
            /** Options to set stress type to display for stress analysis result. */
            public: enum StressTypeName
            {
                StressTypeNameTopFirstPriStress/** Display top fist principal stress. */,
                StressTypeNameTopSecondPriStress/** Display top second principal stress. */,
                StressTypeNameTopEquivalentStress/** Display top equivalent stress. */,
                StressTypeNameMidFirstPriStress/** Display middle fist principal stress. */,
                StressTypeNameMidSecondPriStress/** Display middle second principal stress. */,
                StressTypeNameMidEquivalentStress/** Display middle equivalent stress. */,
                StressTypeNameBottomFirstPriStress/** Display bottom fist principal stress. */,
                StressTypeNameBottomSecondPriStress/** Display bottom second principal stress. */,
                StressTypeNameBottomEquivalentStress/** Display bottom equivalent stress. */
            };

            /** Options to set strain type to display for strain analysis result. */
            public: enum StrainTypeName
            {
                StrainTypeNameTopFirstPriStrain/** Display top fist principal strain. */,
                StrainTypeNameTopSecondPriStrain/** Display top second principal strain. */,
                StrainTypeNameTopEquivalentStrain/** Display top equivalent strain. */,
                StrainTypeNameMidFirstPriStrain/** Display middle fist principal strain. */,
                StrainTypeNameMidSecondPriStrain/** Display middle second principal strain. */,
                StrainTypeNameMidEquivalentStrain/** Display middle equivalent strain. */,
                StrainTypeNameBottomFirstPriStrain/** Display bottom fist principal strain. */,
                StrainTypeNameBottomSecondPriStrain/** Display bottom second principal strain. */,
                StrainTypeNameBottomEquivalentStrain/** Display bottom equivalent strain. */
            };

            /** Options to set strain type to display for formability analysis result. */
            public: enum FormabilityStrainTypeName
            {
                FormabilityStrainTypeNameTopPrincipalStrain/** Display top principal strain. */,
                FormabilityStrainTypeNameMidPrincipalStrain/** Display middle principal strain. */,
                FormabilityStrainTypeNameBottomPrincipalStrain/** Display bottom principal strain. */
            };

            private: FormingSimulationResultDisplayBuilderImpl * m_formingsimulationresultdisplaybuilder_impl;
            private: friend class  _FormingSimulationResultDisplayBuilderBuilder;
            protected: FormingSimulationResultDisplayBuilder();
            public: ~FormingSimulationResultDisplayBuilder();
            /** Set all the result files of the analysis result. If d3plot and its subsequent files is added,
                        the subsequent root files with a two letter appendage(d3plotaa, d3plotab, etc.) and their
                        subsequent files(d3plotaa01, d3plotaa02, etc.) should also be added. Otherwise, only the root
                        file with a two letter appendage and its subsequent files should be added. Only add subsequent
                        files is not allowed. 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetResultFileNames
            (
                std::vector<NXString> & resultFileNames /** resultfilenames */ 
            );
            /**Returns  the result file folder 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ResultFileFolder
            (
            );
            /**Sets  the result file folder 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetResultFileFolder
            (
                const NXString & folderName /** foldername */ 
            );
            /**Sets  the result file folder 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            void SetResultFileFolder
            (
                const char * folderName /** foldername */ 
            );
            /** Import geometries from analysis result files. 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void ImportGeometries
            (
            );
            /** Display formability analysis result. 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void DisplayFormability
            (
            );
            /** Display stress analysis result. 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void DisplayStress
            (
            );
            /** Display strain analysis result. 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void DisplayStrain
            (
            );
            /** Display thickness analysis result. It shows the thicknesses of all elements. 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void DisplayThickness
            (
            );
            /** Display thinning analysis result. It shows the thinning of all elements. 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void DisplayThinning
            (
            );
            /** Display springbcak analysis result. It shows the springbcak of all elements. 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void DisplaySpringback
            (
            );
            /**Returns  the stress type 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::FormingSimulationResultDisplayBuilder::StressTypeName StressType
            (
            );
            /**Sets  the stress type 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetStressType
            (
                NXOpen::Tooling::FormingSimulationResultDisplayBuilder::StressTypeName stressType /** stresstype */ 
            );
            /**Returns  the strain type 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::FormingSimulationResultDisplayBuilder::StrainTypeName StrainType
            (
            );
            /**Sets  the strain type 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetStrainType
            (
                NXOpen::Tooling::FormingSimulationResultDisplayBuilder::StrainTypeName strainType /** straintype */ 
            );
            /**Returns  the formability strain type 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::FormingSimulationResultDisplayBuilder::FormabilityStrainTypeName FormabilityStrainType
            (
            );
            /**Sets  the formability strain type 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetFormabilityStrainType
            (
                NXOpen::Tooling::FormingSimulationResultDisplayBuilder::FormabilityStrainTypeName formabilityStrainType /** formabilitystraintype */ 
            );
            /**Returns  the index of the state which is currently displayed in graphic window 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: int State
            (
            );
            /**Sets  the index of the state which is currently displayed in graphic window 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetState
            (
                int state /** state */ 
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

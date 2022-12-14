#ifndef NXOpen_CAE_DURSPECIALISTLOCALDEFINITIONBUILDER_HXX_INCLUDED
#define NXOpen_CAE_DURSPECIALISTLOCALDEFINITIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurSpecialistLocalDefinitionBuilder.ja
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
#include <NXOpen/CAE_DurSpecialistAnalysisType.hxx>
#include <NXOpen/CAE_DurSpecialistSimulationObjectTable.hxx>
#include <NXOpen/CAE_DurSpecialistSolutionBuilder.hxx>
#include <NXOpen/CAE_SelectElementsBuilder.hxx>
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
        class DurSpecialistLocalDefinitionBuilder;
    }
    class Builder;
    namespace CAE
    {
        class DurSpecialistAnalysisType;
    }
    namespace CAE
    {
        class DurSpecialistSimulationObjectTable;
    }
    namespace CAE
    {
        class SelectElementsBuilder;
    }
    class NXObject;
    class PhysicalMaterial;
    namespace CAE
    {
        class _DurSpecialistLocalDefinitionBuilderBuilder;
        class DurSpecialistLocalDefinitionBuilderImpl;
        /** Represents a @link NXOpen::CAE::DurSpecialistLocalDefinition NXOpen::CAE::DurSpecialistLocalDefinition@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::CAE::DurSpecialistLocalDefinitionCollection::CreateLocalDefinitionBuilder  NXOpen::CAE::DurSpecialistLocalDefinitionCollection::CreateLocalDefinitionBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        IsAnalysisTypeInherited </term> <description> 
         
        true </description> </item> 

        <item><term> 
         
        IsMaterialInherited </term> <description> 
         
        true </description> </item> 

        <item><term> 
         
        Location </term> <description> 
         
        Elements </description> </item> 

        <item><term> 
         
        MaterialSource </term> <description> 
         
        InheritFromSimulation </description> </item> 

        </list> 

         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurSpecialistLocalDefinitionBuilder : public NXOpen::Builder
        {
            /** Represents location type */
            public: enum LocationType
            {
                LocationTypeElements/** Objects (translates to elements) */,
                LocationTypeGroups/** Objects (translates to elements) */,
                LocationTypeSeamWelds/** Objects (translates to elements) */,
                LocationTypeSpotWelds/** Objects (translates to elements) */,
                LocationTypeRemainingStructure/** Use the remaining structure */,
                LocationTypeAllModel/** Use all model */,
                LocationTypeNone/** Dummy local definition (no location) */
            };

            /** Represents the material curve plot type 
             <br>  @deprecated Deprecated in NX1984.0.0.  Use @link CAE::DurSpecialistLocalDefinitionBuilder::PlotMaterialType CAE::DurSpecialistLocalDefinitionBuilder::PlotMaterialType@endlink  instead. <br>  
            */
            public: enum NX_DEPRECATED("Deprecated in NX1984.0.0.  Use CAE::DurSpecialistLocalDefinitionBuilder::PlotMaterialType instead.") PlotCurve
            {
                PlotCurveStressLife/** The material stress-life curve */,
                PlotCurveStrainLife/** The material strain-life curve */,
                PlotCurveRambergOsgood/** The material Ramberg Osgood stress and strain curve */,
                PlotCurveMansonCoffinMorrow/** The material Manson-Coffin-Morrow curve */
            };

            /** Represents the material curve plot type */
            public: enum PlotMaterialType
            {
                PlotMaterialTypeStressLifeSNCurve/** The material stress-life (S-N Curve) */,
                PlotMaterialTypeStrainLifePlots/** The material strain-life plots */,
                PlotMaterialTypeStressStrainCurve/** The material stress-strain curve */,
                PlotMaterialTypeStrainLifeENCurve/** The material strain-life (e-N Curve) */
            };

            private: DurSpecialistLocalDefinitionBuilderImpl * m_durspecialistlocaldefinitionbuilder_impl;
            private: friend class  _DurSpecialistLocalDefinitionBuilderBuilder;
            protected: DurSpecialistLocalDefinitionBuilder();
            public: ~DurSpecialistLocalDefinitionBuilder();
            /**Returns  the LocalDefinition name. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the LocalDefinition name. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetName
            (
                const NXString & title /** title */ 
            );
            /**Sets  the LocalDefinition name. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            void SetName
            (
                const char * title /** title */ 
            );
            /** Returns the description  @return  
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetDescription
            (
            );
            /** Sets the description 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetDescription
            (
                const std::vector<NXString> & description /** description */ 
            );
            /**Returns  the analysis type from solution flag 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsAnalysisTypeInherited
            (
            );
            /**Sets  the analysis type from solution flag 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetAnalysisTypeInherited
            (
                bool isInherited /** isinherited */ 
            );
            /**Returns  the analysis type. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistAnalysisType * AnalysisType
            (
            );
            /**Sets  the analysis type. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetAnalysisType
            (
                NXOpen::CAE::DurSpecialistAnalysisType * analysisType /** analysistype */ 
            );
            /**Returns  the location
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistLocalDefinitionBuilder::LocationType Location
            (
            );
            /**Sets  the location
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetLocation
            (
                NXOpen::CAE::DurSpecialistLocalDefinitionBuilder::LocationType type /** type */ 
            );
            /**Returns  the material from solution flag 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsMaterialInherited
            (
            );
            /**Sets  the material from solution flag 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetMaterialInherited
            (
                bool isInherited /** isinherited */ 
            );
            /**Returns  the material source. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistSolutionBuilder::MaterialSourceType MaterialSource
            (
            );
            /**Sets  the material source. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetMaterialSource
            (
                NXOpen::CAE::DurSpecialistSolutionBuilder::MaterialSourceType type /** type */ 
            );
            /**Returns  the selected material. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PhysicalMaterial * SelectedMaterial
            (
            );
            /**Sets  the selected material. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetSelectedMaterial
            (
                NXOpen::PhysicalMaterial * material /** @link NXOpen::PhysicalMaterial NXOpen::PhysicalMaterial@endlink  to assign  */
            );
            /**Returns  the simulation objects 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistSimulationObjectTable * SimulationObjects
            (
            );
            /**Returns  the option to get the selected element faces 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: NXOpen::CAE::SelectElementsBuilder * SelectElements
            (
            );
            /**  The option to clear the selected groups 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void ClearSelectedGroups
            (
            );
            /**  The option to set the selected groups 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetSelectedGroups
            (
                const std::vector<NXOpen::NXObject *> & selectedGroups /** selectedgroups */ 
            );
            /**  The option to set the selected seam weld sets 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetSelectedSeamWeldSets
            (
                const std::vector<NXOpen::NXObject *> & selectedSets /** selectedsets */ 
            );
            /**  The option to set the selected spot weld sets 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetSelectedSpotWeldSets
            (
                const std::vector<NXOpen::NXObject *> & selectedSets /** selectedsets */ 
            );
            /** Reset to default according to analysis type 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void Reset
            (
            );
            /**Returns  the option to get/set the group reference value 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: int SelectionType
            (
            );
            /**Sets  the option to get/set the group reference value 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetSelectionType
            (
                int selType /** seltype */ 
            );
            /** Get the associated @link NXOpen::CAE::DurSpecialistAnalysisType NXOpen::CAE::DurSpecialistAnalysisType@endlink  object.  @return  The active @link NXOpen::CAE::DurSpecialistAnalysisType NXOpen::CAE::DurSpecialistAnalysisType@endlink  object 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: NXOpen::CAE::DurSpecialistAnalysisType * GetActiveAnalysisType
            (
            );
            /** Plot material curve  @return  Error codes array 
             <br>  @deprecated Deprecated in NX1984.0.0.  Use @link CAE::DurSpecialistLocalDefinitionBuilder::PlotMaterial CAE::DurSpecialistLocalDefinitionBuilder::PlotMaterial@endlink  instead. <br>  

             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: NX_DEPRECATED("Deprecated in NX1984.0.0.  Use CAE::DurSpecialistLocalDefinitionBuilder::PlotMaterial instead.") std::vector<int> PlotMaterialCurve
            (
                NXOpen::CAE::DurSpecialistLocalDefinitionBuilder::PlotCurve type /** type */ ,
                int deviceIndex /** deviceindex */ ,
                int viewIndex /** viewindex */ 
            );
            /** Plot material curve  @return  Error codes array 
             <br>  Created in NX1984.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: std::vector<int> PlotMaterial
            (
                NXOpen::CAE::DurSpecialistLocalDefinitionBuilder::PlotMaterialType type /** type */ ,
                int deviceIndex /** deviceindex */ ,
                int viewIndex /** viewindex */ 
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

#ifndef NXOpen_CAE_DURSPECIALISTPLOTMATERIALBUILDER_HXX_INCLUDED
#define NXOpen_CAE_DURSPECIALISTPLOTMATERIALBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurSpecialistPlotMaterialBuilder.ja
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
        class DurSpecialistPlotMaterialBuilder;
    }
    class Builder;
    class PhysicalMaterial;
    namespace CAE
    {
        class _DurSpecialistPlotMaterialBuilderBuilder;
        class DurSpecialistPlotMaterialBuilderImpl;
        /** Represents a @link CAE::DurSpecialistPlotMaterialBuilder CAE::DurSpecialistPlotMaterialBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::CAE::DurSpecialistManager::CreatePlotMaterialBuilder  NXOpen::CAE::DurSpecialistManager::CreatePlotMaterialBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        MansonCoffinMorrow </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        PlotTypeEnum </term> <description> 
         
        StressLife </description> </item> 

        <item><term> 
         
        RambergOsgood </term> <description> 
         
        1 </description> </item> 

        </list> 

         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurSpecialistPlotMaterialBuilder : public NXOpen::Builder
        {
            /** Material Plot Type */
            public: enum PlotType
            {
                PlotTypeStressLife/** Plot Stress Life SN-Curve  */,
                PlotTypeStrainLife/** Plot Strain Life SN-Curve  */
            };

            private: DurSpecialistPlotMaterialBuilderImpl * m_durspecialistplotmaterialbuilder_impl;
            private: friend class  _DurSpecialistPlotMaterialBuilderBuilder;
            protected: DurSpecialistPlotMaterialBuilder();
            public: ~DurSpecialistPlotMaterialBuilder();
            /**Returns  the plot type enum 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistPlotMaterialBuilder::PlotType PlotTypeEnum
            (
            );
            /**Sets  the plot type enum 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetPlotTypeEnum
            (
                NXOpen::CAE::DurSpecialistPlotMaterialBuilder::PlotType plotTypeEnum /** plottypeenum */ 
            );
            /**Returns  the manson coffin morrow 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: bool MansonCoffinMorrow
            (
            );
            /**Sets  the manson coffin morrow 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetMansonCoffinMorrow
            (
                bool mansonCoffinMorrow /** mansoncoffinmorrow */ 
            );
            /**Returns  the ramberg osgood 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: bool RambergOsgood
            (
            );
            /**Sets  the ramberg osgood 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetRambergOsgood
            (
                bool rambergOsgood /** rambergosgood */ 
            );
            /**Returns  the selected material. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PhysicalMaterial * SelectedMaterial
            (
            );
            /**Sets  the selected material. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetSelectedMaterial
            (
                NXOpen::PhysicalMaterial * material /** @link NXOpen::PhysicalMaterial NXOpen::PhysicalMaterial@endlink  to assign  */
            );
            /** Sets temperature filter 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetTemperatureFilter
            (
                const std::vector<double> & filters /** temperature filters */
            );
            /** Plots material curve  @return  Error codes array 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: std::vector<int> PlotMaterialCurve
            (
                int deviceIndex /** deviceindex */ ,
                int viewIndex /** viewindex */ ,
                bool isOverlay /** isoverlay */ 
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
#ifndef NXOpen_CAE_LOADMAPPINGBUILDER_HXX_INCLUDED
#define NXOpen_CAE_LOADMAPPINGBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_LoadMappingBuilder.ja
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
#include <NXOpen/Fields_FieldFolder.hxx>
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
        class LoadMappingBuilder;
    }
    class Builder;
    namespace CAE
    {
        class SimLoad;
    }
    namespace Fields
    {
        class FieldFolder;
    }
    namespace CAE
    {
        class _LoadMappingBuilderBuilder;
        class LoadMappingBuilderImpl;
        /**  @brief  Represents a @link NXOpen::CAE::LoadMappingBuilder NXOpen::CAE::LoadMappingBuilder@endlink  builder 
                to map forces to area corrected spatial forces.  

         
             <br> To create a new instance of this class, use @link NXOpen::CAE::SimSimulation::CreateLoadMappingBuilder  NXOpen::CAE::SimSimulation::CreateLoadMappingBuilder @endlink  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  LoadMappingBuilder : public NXOpen::Builder
        {
            private: LoadMappingBuilderImpl * m_loadmappingbuilder_impl;
            private: friend class  _LoadMappingBuilderBuilder;
            protected: LoadMappingBuilder();
            public: ~LoadMappingBuilder();
            /** Set forces on load mapping builder 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetForces
            (
                const std::vector<NXOpen::CAE::SimLoad *> & forces /** forces */ 
            );
            /** Set destination folder for spatial pressure fields created by builder 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetFolder
            (
                NXOpen::Fields::FieldFolder * folder /** folder */ 
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

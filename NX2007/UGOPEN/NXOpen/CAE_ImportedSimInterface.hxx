#ifndef NXOpen_CAE_IMPORTEDSIMINTERFACE_HXX_INCLUDED
#define NXOpen_CAE_IMPORTEDSIMINTERFACE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ImportedSimInterface.ja
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
#include <NXOpen/CAE_ImportedSimInterfaceCollection.hxx>
#include <NXOpen/NXObject.hxx>
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
        class ImportedSimInterface;
    }
    namespace CAE
    {
        class FEModelOccurrence;
    }
    namespace CAE
    {
        class SimulationInterface;
    }
    class NXObject;
    namespace CAE
    {
        class _ImportedSimInterfaceBuilder;
        class ImportedSimInterfaceImpl;
        /** Represents a Imported Simulation Interface <br> To obtain an instance of this class use CAE::ImportedSimInterfaceCollection  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ImportedSimInterface : public NXOpen::NXObject
        {
            private: ImportedSimInterfaceImpl * m_importedsiminterface_impl;
            private: friend class  _ImportedSimInterfaceBuilder;
            protected: ImportedSimInterface();
            public: ~ImportedSimInterface();
            /** Sync  Imported SimulationInterface 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void AttachFemComponents
            (
                const std::vector<NXOpen::CAE::FEModelOccurrence *> & femOccs /** Array of FeModelOccurrences to sync with @link NXOpen::CAE::FEModelOccurrence NXOpen::CAE::FEModelOccurrence@endlink */
            );
            /** Get simulation interface  @return  Simulation Interface
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::SimulationInterface * GetSimif
            (
            );
            /** Get expression conflict option 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::ImportedSimInterfaceCollection::ExpressionConflictOption GetExpconfop
            (
            );
            /** Get fem occurence    
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: std::vector<NXOpen::CAE::FEModelOccurrence *> GetFemoccs
            (
            );
            /** Set fem occurence    
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetFemoccs
            (
                const std::vector<NXOpen::CAE::FEModelOccurrence *> & femoccs /** femoccs */ 
            );
            /** Get update pending status  
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: bool GetUpdatepending
            (
            );
            /** Update sim interface  
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void UpdateSimInterface
            (
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

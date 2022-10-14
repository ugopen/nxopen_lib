#ifndef NXOpen_CAE_RESPONSESIMULATION_MANAGER_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_MANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_Manager.ja
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
        namespace ResponseSimulation
        {
            class Manager;
        }
    }
    namespace CAE
    {
        class SimSimulation;
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class EvaluationSettingManager;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class ExcitationCollection;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class RSEventCollection;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class SensorCollection;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class SolutionCollection;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class StrainGageCollection;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class ManagerImpl;
            /** Represents the Response Simulation manager to contain all Response Simulation objects  <br> To obtain an instance of this class, refer to @link CAE::SimSimulation  CAE::SimSimulation @endlink  <br> 
             <br>  Created in NX5.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  Manager
            {
                private: ManagerImpl * m_manager_impl;
                private: NXOpen::CAE::SimSimulation* m_owner;
                /// \cond NX_NO_DOC 
                public: explicit Manager(NXOpen::CAE::SimSimulation *owner);


                /// \endcond 
                public: 
                /**Returns the tag of this object.  */
                tag_t Tag() const; 
                public: ~Manager();


                /** Returns the Response Simulation solution collection belonging to this sim part 
                 <br>  Created in NX3.0.0.  <br>  
                */
                public: NXOpen::CAE::ResponseSimulation::SolutionCollection *Solutions();
                /** Returns the Response Simulation event collection belonging to this sim part 
                 <br>  Created in NX3.0.0.  <br>  
                */
                public: NXOpen::CAE::ResponseSimulation::RSEventCollection *Events();
                /** Returns the Response Simulation excitation collection belonging to this sim part 
                 <br>  Created in NX3.0.0.  <br>  
                */
                public: NXOpen::CAE::ResponseSimulation::ExcitationCollection *Excitations();
                /** Returns the Response Simulation evaluation data manager belonging to this sim part 
                 <br>  Created in NX3.0.0.  <br>  
                */
                public: NXOpen::CAE::ResponseSimulation::EvaluationSettingManager *EvaluationSettingManager();
                /** Returns the Response Simulation sensor collection belonging to this sim part 
                 <br>  Created in NX3.0.0.  <br>  
                */
                public: NXOpen::CAE::ResponseSimulation::SensorCollection *Sensors();
                /** Returns the Response Simulation strain gage collection belonging to this sim part 
                 <br>  Created in NX3.0.0.  <br>  
                */
                public: NXOpen::CAE::ResponseSimulation::StrainGageCollection *StrainGages();
            }; //lint !e1712 default constructor not defined for class  

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
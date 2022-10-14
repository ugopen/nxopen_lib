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
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
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
            /** Represents the Response Simulation manager to contain all Response Simulation objects  <br> To obtain an instance of this class, refer to @link CAE::SimSimulation CAE::SimSimulation@endlink  <br> */
            class NXOPENCPPEXPORT Manager
            {
                private: NXOpen::CAE::SimSimulation* m_owner;
                public: explicit Manager(NXOpen::CAE::SimSimulation *owner): m_owner(owner)
                     ,solutions(NULL)
                     ,events(NULL)
                     ,excitations(NULL)
                     ,evaluationSettingManager(NULL)
                     ,sensors(NULL)
                     ,strainGages(NULL)
                {
                }
                public: 
                /**Returns the tag of this object.  */
                tag_t Tag() const; 


                private: NXOpen::CAE::ResponseSimulation::SolutionCollection *solutions;
                /** Returns the Response Simulation solution collection belonging to this sim part */
                public: NXOpen::CAE::ResponseSimulation::SolutionCollection *Solutions()
                {
                    return solutions;
                }
                private: NXOpen::CAE::ResponseSimulation::RSEventCollection *events;
                /** Returns the Response Simulation event collection belonging to this sim part */
                public: NXOpen::CAE::ResponseSimulation::RSEventCollection *Events()
                {
                    return events;
                }
                private: NXOpen::CAE::ResponseSimulation::ExcitationCollection *excitations;
                /** Returns the Response Simulation excitation collection belonging to this sim part */
                public: NXOpen::CAE::ResponseSimulation::ExcitationCollection *Excitations()
                {
                    return excitations;
                }
                private: NXOpen::CAE::ResponseSimulation::EvaluationSettingManager *evaluationSettingManager;
                /** Returns the Response Simulation evaluation data manager belonging to this sim part */
                public: NXOpen::CAE::ResponseSimulation::EvaluationSettingManager *EvaluationSettingManager()
                {
                    return evaluationSettingManager;
                }
                private: NXOpen::CAE::ResponseSimulation::SensorCollection *sensors;
                /** Returns the Response Simulation sensor collection belonging to this sim part */
                public: NXOpen::CAE::ResponseSimulation::SensorCollection *Sensors()
                {
                    return sensors;
                }
                private: NXOpen::CAE::ResponseSimulation::StrainGageCollection *strainGages;
                /** Returns the Response Simulation strain gage collection belonging to this sim part */
                public: NXOpen::CAE::ResponseSimulation::StrainGageCollection *StrainGages()
                {
                    return strainGages;
                }
                public: virtual void initialize();
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
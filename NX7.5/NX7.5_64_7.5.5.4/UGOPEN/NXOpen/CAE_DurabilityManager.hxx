#ifndef NXOpen_CAE_DURABILITYMANAGER_HXX_INCLUDED
#define NXOpen_CAE_DURABILITYMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurabilityManager.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class DurabilityManager;
    }
    namespace CAE
    {
        class SimSimulation;
    }
    namespace CAE
    {
        class DurabilityEvent;
    }
    namespace CAE
    {
        class DurabilityEventSolverBuilder;
    }
    namespace CAE
    {
        class DurabilityMetaSolution;
    }
    namespace CAE
    {
        class DurabilityMetaSolutionCollection;
    }
    namespace CAE
    {
        class DurabilitySolverBuilder;
    }
    namespace CAE
    {
        class DurabilityManagerImpl;
        /** Represents the durability manager that contains all durability objects.  <br> To obtain an instance of this class, refer to @link CAE::SimSimulation CAE::SimSimulation@endlink  <br> */
        class NXOPENCPPEXPORT  DurabilityManager
        {
            private: DurabilityManagerImpl * m_durabilitymanager_impl;
            private: NXOpen::CAE::SimSimulation* m_owner;
            /** Constructor */
            public: explicit DurabilityManager(NXOpen::CAE::SimSimulation *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~DurabilityManager();
            /** Creates a builder for the durability metasolution solver. @return   <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: NXOpen::CAE::DurabilitySolverBuilder * CreateSolverBuilder
            (
                NXOpen::CAE::DurabilityMetaSolution * durabilityTag /** The metasolution.*/
            );
            /** Creates a builder for a durability event solver. @return   <br> License requirements : nx_adv_durability ("NX Advanced Durability") */
            public: NXOpen::CAE::DurabilityEventSolverBuilder * CreateEventSolverBuilder
            (
                NXOpen::CAE::DurabilityEvent * eventTag /** The event.*/
            );


            /** Returns the durability metasolution collection belonging to this sim part. */
            public: NXOpen::CAE::DurabilityMetaSolutionCollection *MetaSolutions();
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
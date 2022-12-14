#ifndef NXOpen_MECHANICALROUTING_INSULATIONSERVICE_HXX_INCLUDED
#define NXOpen_MECHANICALROUTING_INSULATIONSERVICE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MechanicalRouting_InsulationService.ja
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
#include <NXOpen/libnxopencpp_mechanicalrouting_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace MechanicalRouting
    {
        class InsulationService;
    }
    namespace MechanicalRouting
    {
        class RoutingManager;
    }
    namespace Assemblies
    {
        class Component;
    }
    class NXObject;
    namespace MechanicalRouting
    {
        class InsulationServiceImpl;
        /** Represents a @link NXOpen::MechanicalRouting::InsulationService NXOpen::MechanicalRouting::InsulationService@endlink  object.
                Uses the @link MechanicalRouting::RoutingManager::InsulationService MechanicalRouting::RoutingManager::InsulationService@endlink  to obtain
                an instance of this class.
              <br> To obtain an instance of this class, refer to @link NXOpen::MechanicalRouting::RoutingManager  NXOpen::MechanicalRouting::RoutingManager @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_MECHANICALROUTINGEXPORT  InsulationService
        {
            private: InsulationServiceImpl * m_insulationservice_impl;
            private: NXOpen::MechanicalRouting::RoutingManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit InsulationService(NXOpen::MechanicalRouting::RoutingManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~InsulationService();
            /** Get all insulation occurences in current container  @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : routing_pipetube ("Routing Piping and Tubing") */
            public: std::vector<NXOpen::NXObject *> GetAllInsulatedObjectsInContainer
            (
                NXOpen::Assemblies::Component * container /** container */ 
            );
        }; //lint !e1712 default constructor not defined for class  

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

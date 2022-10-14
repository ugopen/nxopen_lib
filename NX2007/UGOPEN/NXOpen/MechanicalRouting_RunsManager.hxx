#ifndef NXOpen_MECHANICALROUTING_RUNSMANAGER_HXX_INCLUDED
#define NXOpen_MECHANICALROUTING_RUNSMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MechanicalRouting_RunsManager.ja
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
        class RunsManager;
    }
    namespace MechanicalRouting
    {
        class RoutingManager;
    }
    namespace Assemblies
    {
        class Component;
    }
    class CollaborativeDesign;
    class NXObject;
    class Part;
    namespace MechanicalRouting
    {
        class RunsManagerImpl;
        /** Represents the Runs Manager used to manage runs in Mechanical Routing application,
                including loading and unloading runs, associating/detaching runs to/from the part, setting/clearing
                the active run, and adding/removing components to/from the runs
             <br> To obtain an instance of this class, refer to @link NXOpen::MechanicalRouting::RoutingManager  NXOpen::MechanicalRouting::RoutingManager @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_MECHANICALROUTINGEXPORT  RunsManager
        {
            private: RunsManagerImpl * m_runsmanager_impl;
            private: NXOpen::MechanicalRouting::RoutingManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit RunsManager(NXOpen::MechanicalRouting::RoutingManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~RunsManager();
            /** Loads the runs in to the NX session
                    
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void LoadRuns
            (
                NXOpen::CollaborativeDesign * collaborativeDesign /** The collaborative design containing the runs to load */,
                std::vector<NXString> & runIdsToLoad /** The run ids of the runs to load */
            );
            /** Closes and unloads the passed in run
                    
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void UnloadRun
            (
                NXOpen::NXObject * run /** The run to unload */
            );
            /** Gets the loaded runs in the NX session
                    
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void GetLoadedRuns
            (
                std::vector<NXOpen::NXObject *> & runs /** The run objects that are loaded in the NX session */
            );
            /** Associates the run to the part
                    
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void AssociateRun
            (
                NXOpen::Part * part /** The part to associate the run to */,
                NXOpen::NXObject * run /** The run to associate with the part */
            );
            /** Detaches the run from the part
                    
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void DissociateRun
            (
                NXOpen::Part * part /** The part to detach the run from */,
                NXOpen::NXObject * run /** The run to detach from the part */
            );
            /** Sets the active run to the passed in run for the specified part
                    
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void SetActiveRun
            (
                NXOpen::Part * part /** The part to set the active run for */,
                NXOpen::NXObject * run /** The run to set active in the part */
            );
            /** Makes any active runs inactive for the specified part
                    
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void MakeRunInactive
            (
                NXOpen::Part * part /** The part for which to make the active run inactive. */
            );
            /** Makes the passed in component a member of the passed in run 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void AddToRun
            (
                NXOpen::Assemblies::Component * component /** The component to add to the run. */,
                NXOpen::NXObject * run /** The run to add the component to. */
            );
            /** Makes the passed in components members of the passed in run 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void AddComponentsToRun
            (
                const std::vector<NXOpen::Assemblies::Component *> & componentsToAdd /** The components to add to the run */,
                NXOpen::NXObject * run /** The run to add the components to */
            );
            /** Removes the passed in component from membership of any runs it belongs to 
             <br>  @deprecated Deprecated in NX2007.0.0.  Please use @link NXOpen::MechanicalRouting::RunsManager::RemoveComponentFromRun NXOpen::MechanicalRouting::RunsManager::RemoveComponentFromRun@endlink  instead. <br>  

             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NX_DEPRECATED("Deprecated in NX2007.0.0.  Please use NXOpen::MechanicalRouting::RunsManager::RemoveComponentFromRun instead.") void RemoveFromRun
            (
                NXOpen::Assemblies::Component * component /** The component to remove the run membership of. */
            );
            /** Removes the passed in component from membership of the passed in run 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void RemoveComponentFromRun
            (
                NXOpen::Assemblies::Component * component /** The component to remove from the run. */,
                NXOpen::NXObject * run /** The run to remove the component from. */
            );
            /** Moves membership of the passed in component from whatever run it belongs to the passed in run 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void MoveToRun
            (
                NXOpen::Assemblies::Component * component /** The component to move to another run. */,
                NXOpen::NXObject * run /** The run to move the component to. */
            );
            /** Moves membership of the passed in components from whatever runs they belong to the passed in run 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void MoveComponentsToRun
            (
                const std::vector<NXOpen::Assemblies::Component *> & componentsToMove /** The components to move to the run */,
                NXOpen::NXObject * run /** The run to move the components to */
            );
            /** Deletes a run object from a RSD 3D authored Run 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void Delete3dRunObject
            (
                NXOpen::Part * part /** The part containing the given run */,
                NXOpen::NXObject * runObject /** The run object to be deleted, it's limited to run and branch only. */
            );
            /** Shows the flow direction of all the branches for the run 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void ShowFlowDirectionForRun
            (
                NXOpen::Part * part /** The part containing the run or components associated to the run to show the flow direction for */,
                NXOpen::NXObject * run /** The run to show the flow direction for */
            );
            /** Shows the flow direction of the specified branch of the run 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void ShowFlowDirectionForRunBranch
            (
                NXOpen::Part * part /** The part containing the run branch or the components associated to the run branch to show the flow direction for */,
                NXOpen::NXObject * run /** The branch to show the flow direction for */
            );
            /** Reverses the flow direction of the specified branch of the run 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void ReverseFlowDirectionForRunBranch
            (
                NXOpen::NXObject * run /** The branch to reverse the flow direction for */
            );
            /** Deletes one or more 3D authored runs from the part file 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void Delete3dRunObjects
            (
                const std::vector<NXOpen::NXObject *> & runObjects /** The run objects to be deleted, the function is limited to delete multiple runs only. */
            );
            /** Loads one or more given assemblies which are associated to PID run. 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void LoadPidRunAssemblies
            (
                const std::vector<NXOpen::Part *> & assemblies /** The assemblies to be loaded. */
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
#ifndef NXOpen_TOOLING_MWPARTINGMANAGERBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_MWPARTINGMANAGERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_MWPartingManagerBuilder.ja
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
#include <NXOpen/Tooling_MWPartingManagerBuilder.hxx>
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
        class MWPartingManagerBuilder;
    }
    class Builder;
    namespace Tooling
    {
        class _MWPartingManagerBuilderBuilder;
        class MWPartingManagerBuilderImpl;
        /** Builder for the Parting Manager in the Mold Wizard application  <br> To create a new instance of this class, use @link Tooling::MWPartingManagerCollection::CreateBuilder  Tooling::MWPartingManagerCollection::CreateBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  MWPartingManagerBuilder : public Builder
        {
            /** The status of the parting manager data. */
            public: enum DataStatus
            {
                DataStatusNotFreed/** Data not freed yet.      */,
                DataStatusFreed/** Data already freed.      */,
                DataStatusForceUpdate/** Data needs force update. */
            };

            /** The type of registering UNDO identifier. */
            public: enum RegisterType
            {
                RegisterTypeInit/** Initialize registration for UNDO identifiers. */,
                RegisterTypeCurrent/** Register current UNDO mark. */,
                RegisterTypeClear/** Clear all registered UNDO identifiers. */
            };

            private: MWPartingManagerBuilderImpl * m_mwpartingmanagerbuilder_impl;
            private: friend class  _MWPartingManagerBuilderBuilder;
            protected: MWPartingManagerBuilder();
            public: ~MWPartingManagerBuilder();
            /** Perform the module initialization tasks when entering the Mold Wizard Parting environment.  @return  Return the error flag indicating the type of error 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: int InitModule
            (
            );
            /** Perform initialization of the settings for parting when entering the Mold Wizard Parting environment. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void InitPartingSettings
            (
            );
            /** Perform the syncronization tasks when entering the Parting Manager environment. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void PerformSyncTasks
            (
            );
            /** Perform the syncronization tasks when exiting the Parting Manager environment. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void PerformSyncTasksOnExit
            (
            );
            /** Set the update lock. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetUpdateLock
            (
            );
            /** Reset the update lock. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void ResetUpdateLock
            (
                int doUpdate /** indicates whether to perform update after resetting the update lock */
            );
            /** Get the status of the parting manager data.  @return  Return the status of the parting manager data  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: int GetPartingManagerDataStatus
            (
            );
            /** Set the status of the parting manager data. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetPartingManagerDataStatus
            (
                int pmDataStatus /** Set the status of the parting manager data */
            );
            /** Get if it is within a parting command.  @return  Return if it is within a parting command 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: int GetInPartingCommand
            (
            );
            /** Set if it is within a parting command. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetInPartingCommand
            (
                int inPartingCommand /** Set if it is within a parting command */
            );
            /** Update the Parting Navigator. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void UpdatePartingNavigator
            (
            );
            /** Register the UNDO identifiers. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void RegisterUndoIds
            (
                int registerType /** The register type for UNDO identifiers */
            );
            /** Register or unregister the post UNDO callback function for the Wall Thickness Checker. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void RegisterWtcPostUndoCallback
            (
                int registerPostUNDO /** Indicate if it is to register:1 or unregister:0 the post UNDO callback function. */
            );
            /** Initialize, reset or delete the transient meshes created in the Wall Thickness Checker. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void DeleteTransientMeshes
            (
                int deleteMesh /** Indicate if it is to initialize:0; reset:1; or delete:2 the transient meshes. */
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

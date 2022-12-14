#ifndef NXOpen_STAGEMODEL_OBJECTUPDATESTATEMANAGER_HXX_INCLUDED
#define NXOpen_STAGEMODEL_OBJECTUPDATESTATEMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     StageModel_ObjectUpdateStateManager.ja
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
#include <NXOpen/Session.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libstagemodelopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace StageModel
    {
        class ObjectUpdateStateManager;
    }
    namespace StageModel
    {
        class Manager;
    }
    class NXObject;
    class TaggedObject;
    namespace StageModel
    {
        class ObjectUpdateStateManagerImpl;
        /** Provides interface for objtects up to date status.  <br> To obtain an instance of this class, refer to @link NXOpen::StageModel::Manager  NXOpen::StageModel::Manager @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class STAGEMODELOPENCPPEXPORT  ObjectUpdateStateManager
        {
            /** Defines allowed Up to date status. 
             <br>  Created in NX1953.0.0.  <br>  
            */
            public: enum Status
            {
                StatusInvalidUpToDate/** invalid up to date */ ,
                StatusUpToDate/** up to date */ ,
                StatusUpToDateToOodParent/** up to date to ood parent */ ,
                StatusOutOfDateCannotUpdate/** out of date cannot update */ ,
                StatusFailed/** failed */ ,
                StatusOutOfDateCanUpdate/** out of date can update */ ,
                StatusNoState/** no state */ ,
                StatusUpdateFrozen/** update frozen */ ,
                StatusParentNotLoaded/** parent not loaded */ ,
                StatusInterPartAssoBroken/** inter part asso broken */ 
            };

            private: ObjectUpdateStateManagerImpl * m_objectupdatestatemanager_impl;
            private: NXOpen::StageModel::Manager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit ObjectUpdateStateManager(NXOpen::StageModel::Manager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~ObjectUpdateStateManager();
            /** Get up to date status of the object.
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : stage_model (" Stage Model") */
            public: NXOpen::StageModel::ObjectUpdateStateManager::Status GetStatus
            (
                NXOpen::TaggedObject * object /** object */ 
            );
            /** Updates all given out-of-date objects to make them up to date 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : stage_model (" Stage Model") */
            public: void MakeUpToDate
            (
                const std::vector<NXOpen::NXObject *> & objects /** The objects to be made up to date */,
                NXOpen::Session::UndoMarkId undoMarkId /** If any update error occurs, the system will roll back to this
                                                                      undo mark. */
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

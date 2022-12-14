#ifndef NXOpen_FEATURES_EDITWITHROLLBACKMANAGER_HXX_INCLUDED
#define NXOpen_FEATURES_EDITWITHROLLBACKMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_EditWithRollbackManager.ja
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
#include <NXOpen/Features_EditWithRollbackManager.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        class EditWithRollbackManager;
    }
    namespace Features
    {
        class _EditWithRollbackManagerBuilder;
        class EditWithRollbackManagerImpl;
        /**  @brief 
            Represents an object that stores transient data during Edit with Rollback of a feature.
             

         

            
             <br> 
            A call to @link NXOpen::Features::FeatureCollection::StartEditWithRollbackManager NXOpen::Features::FeatureCollection::StartEditWithRollbackManager@endlink  will roll the model to a suitable point 
            before feature edit can begin.
             <br> 
             <br> 
            The feature edit is expected to happen after the call to @link NXOpen::Features::FeatureCollection::StartEditWithRollbackManager NXOpen::Features::FeatureCollection::StartEditWithRollbackManager@endlink 
             <br> 
             <br> 
            The feature edit should be followed by a call to @link NXOpen::Features::EditWithRollbackManager::UpdateFeature NXOpen::Features::EditWithRollbackManager::UpdateFeature@endlink .
            A true needs to be passed into @link NXOpen::Features::EditWithRollbackManager::UpdateFeature NXOpen::Features::EditWithRollbackManager::UpdateFeature@endlink  indicating that there was an
            error while editing the feature so all the transient data is cleaned up.
            A false needs to be passed into @link NXOpen::Features::EditWithRollbackManager::UpdateFeature NXOpen::Features::EditWithRollbackManager::UpdateFeature@endlink  if there was no error
            while editing the feature.
             <br> 
             <br> 
            The call to method @link NXOpen::Features::EditWithRollbackManager::UpdateFeature NXOpen::Features::EditWithRollbackManager::UpdateFeature@endlink  should be followed by a call to
            @link NXOpen::Features::EditWithRollbackManager::Stop NXOpen::Features::EditWithRollbackManager::Stop@endlink . This method rolls forward the model to the original current
            feature after the feature is edited with rollback.
             <br> 
             <br> 
            Finally a call to @link NXOpen::Features::EditWithRollbackManager::Destroy NXOpen::Features::EditWithRollbackManager::Destroy@endlink  will destroy the transient object of class
            @link NXOpen::Features::EditWithRollbackManager NXOpen::Features::EditWithRollbackManager@endlink .
             <br> 
             <br> 
            Hence the sequence of calls -
            <ol>
            <li>@link NXOpen::Features::FeatureCollection::StartEditWithRollbackManager NXOpen::Features::FeatureCollection::StartEditWithRollbackManager@endlink </li>
            <li>Feature edit using builder</li>
            <li>@link NXOpen::Features::EditWithRollbackManager::UpdateFeature NXOpen::Features::EditWithRollbackManager::UpdateFeature@endlink </li>
            <li>@link NXOpen::Features::EditWithRollbackManager::Stop NXOpen::Features::EditWithRollbackManager::Stop@endlink </li>
            <li>@link NXOpen::Features::EditWithRollbackManager::Destroy NXOpen::Features::EditWithRollbackManager::Destroy@endlink </li>
            </ol>
             <br> 
              <br> An instance of this class can be created by a call to Features.FeatureCollection.StartEditWithRollbackManager  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  EditWithRollbackManager : public NXOpen::TaggedObject
        {
            private: EditWithRollbackManagerImpl * m_editwithrollbackmanager_impl;
            private: friend class  _EditWithRollbackManagerBuilder;
            protected: EditWithRollbackManager();
            public: ~EditWithRollbackManager();
            /** Updates the feature after the feature is edited with rollback
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void UpdateFeature
            (
                bool errorDuringFeatureEdit /** True if feature edit resulted in an error.
                                                                       False otherwise */
            );
            /** Rolls the model to the original current feature after the feature is edited with rollback
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void Stop
            (
            );
            /** Delete the Edit With Rollback Manager 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void Destroy
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

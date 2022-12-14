#ifndef NXOpen_STAGEMODEL_PMIMANAGER_HXX_INCLUDED
#define NXOpen_STAGEMODEL_PMIMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     StageModel_PmiManager.ja
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
#include <NXOpen/StageModel_ReusePmiBuilder.hxx>
#include <NXOpen/StageModel_ReuseViewBuilder.hxx>
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
        class PmiManager;
    }
    class Session;
    namespace StageModel
    {
        class ReusePmiBuilder;
    }
    namespace StageModel
    {
        class ReuseViewBuilder;
    }
    namespace StageModel
    {
        class Stage;
    }
    namespace StageModel
    {
        class PmiManagerImpl;
        /** Represents the Stage Model PMI Manager class. <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
         <br>  Created in NX1926.0.0.  <br>  
        */
        class STAGEMODELOPENCPPEXPORT  PmiManager
        {
            private: PmiManagerImpl * m_pmimanager_impl;
            private: NXOpen::Session* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit PmiManager(NXOpen::Session *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            private: static PmiManager* thePmiManager;
            /** Returns the PmiManager object for the running session which serves as the 'gateway' class for the application API.  
                References to all other objects in this API are obtained either directly or indirectly via methods and properties on this class.  
                Platform Session should be initialized using 'GetSession' method from NXOpen API prior to this call.  
            */
            public: static PmiManager* GetPmiManager(NXOpen::Session *owner);
            public: ~PmiManager();
            /** Creates a @link StageModel::ReusePmiBuilder StageModel::ReusePmiBuilder@endlink  
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : stage_model (" Stage Model") */
            public: NXOpen::StageModel::ReusePmiBuilder * CreateReusePmiBuilder
            (
                NXOpen::StageModel::Stage * stage /** stage */ 
            );
            /** Creates a @link StageModel::ReuseViewBuilder StageModel::ReuseViewBuilder@endlink  
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : stage_model (" Stage Model") */
            public: NXOpen::StageModel::ReuseViewBuilder * CreateReuseViewBuilder
            (
                NXOpen::StageModel::Stage * stage /** stage */ 
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

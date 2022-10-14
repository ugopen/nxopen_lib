#ifndef NXOpen_CAE_QUALITYAUDIT_ACTIONSETTINGS_HXX_INCLUDED
#define NXOpen_CAE_QUALITYAUDIT_ACTIONSETTINGS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_QualityAudit_ActionSettings.ja
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
#include <NXOpen/CAE_Connections_CommonTypes.hxx>
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
        namespace QualityAudit
        {
            class ActionSettings;
        }
    }
    namespace CAE
    {
        namespace QualityAudit
        {
            class Action;
        }
    }
    class NXObject;
    namespace CAE
    {
        namespace QualityAudit
        {
            class _ActionSettingsBuilder;
            class ActionSettingsImpl;
            /**  @brief  The Quality Audit ActionSettings is the base class for @link NXOpen::CAE::QualityAudit::Action NXOpen::CAE::QualityAudit::Action@endlink  settings. It provides basic functionality. 

               <br> Settings instances can be obtained via @link NXOpen::CAE::QualityAudit::Action::Settings NXOpen::CAE::QualityAudit::Action::Settings@endlink .  <br> 
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  ActionSettings : public NXOpen::NXObject
            {
                private: ActionSettingsImpl * m_actionsettings_impl;
                private: friend class  _ActionSettingsBuilder;
                protected: ActionSettings();
                public: ~ActionSettings();
                /** Reset the action settings to default values 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
                public: void ResetToDefaults
                (
                );
                /**Returns  the action using these settings 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::QualityAudit::Action * Action
                (
                );
                /** The supported connection types using the settings 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: std::vector<NXOpen::CAE::Connections::ConnectionType> GetSupportedConnectionTypes
                (
                );
                /** Sets the override flag of settings for the specified connection type.
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void AllowOverride
                (
                    NXOpen::CAE::Connections::ConnectionType connectionType /** connectiontype */ ,
                    bool allowOverride /** allowoverride */ 
                );
                /** Tells if overriding is allowed for the specified connection type.
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: bool CanOverride
                (
                    NXOpen::CAE::Connections::ConnectionType connectionType /** connectiontype */ 
                );
            };
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
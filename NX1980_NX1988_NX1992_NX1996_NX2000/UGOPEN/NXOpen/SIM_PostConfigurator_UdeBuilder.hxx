#ifndef NXOpen_SIM_POSTCONFIGURATOR_UDEBUILDER_HXX_INCLUDED
#define NXOpen_SIM_POSTCONFIGURATOR_UDEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SIM_PostConfigurator_UdeBuilder.ja
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
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/SIM_PostConfigurator_UdeParameterBuilder.hxx>
#include <NXOpen/libnxopencpp_sim_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace SIM
    {
        namespace PostConfigurator
        {
            class UdeBuilder;
        }
    }
    class Builder;
    namespace SIM
    {
        namespace PostConfigurator
        {
            class UdeParameterBuilder;
        }
    }
    namespace SIM
    {
        namespace PostConfigurator
        {
            class UdeParameterBuilderList;
        }
    }
    namespace SIM
    {
        namespace PostConfigurator
        {
            class _UdeBuilderBuilder;
            class UdeBuilderImpl;
            /** This class is used to create a new event.
                        Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
                     <br> To create a new instance of this class, use @link NXOpen::SIM::PostConfigurator::PostConfiguratorManager::CreateUdeBuilder  NXOpen::SIM::PostConfigurator::PostConfiguratorManager::CreateUdeBuilder @endlink  <br> 
             <br>  Created in NX12.0.1.  <br>  
            */
            class NXOPENCPP_SIMEXPORT  UdeBuilder : public NXOpen::Builder
            {
                /** Type of Event Description  */
                public: enum EventDescriptionType
                {
                    EventDescriptionTypeNone/** None   */,
                    EventDescriptionTypeSpecify/** Specify */
                };

                private: UdeBuilderImpl * m_udebuilder_impl;
                private: friend class  _UdeBuilderBuilder;
                protected: UdeBuilder();
                public: ~UdeBuilder();
                /**Returns  the event name 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: NXString EventName
                (
                );
                /**Sets  the event name 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void SetEventName
                (
                    const NXString & name /** name */ 
                );
                /**Sets  the event name 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                void SetEventName
                (
                    const char * name /** name */ 
                );
                /**Returns  the event ID 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: NXString EventID
                (
                );
                /**Sets  the event ID 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void SetEventID
                (
                    const NXString & stringEventID /** stringeventid */ 
                );
                /**Sets  the event ID 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                void SetEventID
                (
                    const char * stringEventID /** stringeventid */ 
                );
                /**Returns  the post event 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: NXString PostEvent
                (
                );
                /**Sets  the post event 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void SetPostEvent
                (
                    const NXString & postEventID /** posteventid */ 
                );
                /**Sets  the post event 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                void SetPostEvent
                (
                    const char * postEventID /** posteventid */ 
                );
                /**Returns  the event description type 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SIM::PostConfigurator::UdeBuilder::EventDescriptionType EventDescription
                (
                );
                /**Sets  the event description type 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void SetEventDescription
                (
                    NXOpen::SIM::PostConfigurator::UdeBuilder::EventDescriptionType eventDescription /** eventdescription */ 
                );
                /**Returns  the event description 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: NXString EventHelpDescription
                (
                );
                /**Sets  the event description 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void SetEventHelpDescription
                (
                    const NXString & helpDescription /** helpdescription */ 
                );
                /**Sets  the event description 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                void SetEventHelpDescription
                (
                    const char * helpDescription /** helpdescription */ 
                );
                /**Returns  the event url location 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: NXString EventHelpLocation
                (
                );
                /**Sets  the event url location 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void SetEventHelpLocation
                (
                    const NXString & helpLocation /** helplocation */ 
                );
                /**Sets  the event url location 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                void SetEventHelpLocation
                (
                    const char * helpLocation /** helplocation */ 
                );
                /**Returns  the event category milling 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: bool EventCategoryMilling
                (
                );
                /**Sets  the event category milling 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void SetEventCategoryMilling
                (
                    bool categoryMilling /** categorymilling */ 
                );
                /**Returns  the event category turning 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: bool EventCategoryTurning
                (
                );
                /**Sets  the event category turning 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void SetEventCategoryTurning
                (
                    bool categoryTurning /** categoryturning */ 
                );
                /**Returns  the event category drilling 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: bool EventCategoryDrilling
                (
                );
                /**Sets  the event category drilling 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void SetEventCategoryDrilling
                (
                    bool categoryDrilling /** categorydrilling */ 
                );
                /**Returns  the event category wire EDM 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: bool EventCategoryWireEDM
                (
                );
                /**Sets  the event category wire EDM 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void SetEventCategoryWireEDM
                (
                    bool categoryWireEDM /** categorywireedm */ 
                );
                /** Adds item to item used list 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void AddItem
                (
                    NXOpen::SIM::PostConfigurator::UdeParameterBuilder * itemBuilder /** itembuilder */ 
                );
                /** Deletes parameter from ude list 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void DeleteItem
                (
                    NXOpen::SIM::PostConfigurator::UdeParameterBuilder * itemBuilder /** itembuilder */ 
                );
                /** Deletes all parameters from ude list 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void DeleteItems
                (
                );
                /**Returns  the ude parameter list 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SIM::PostConfigurator::UdeParameterBuilderList * UdeParameterList
                (
                );
                /** Returns the ude parameter builder by parameter ID  @return  the ude parameter builder 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SIM::PostConfigurator::UdeParameterBuilder * GetUdeParameterBuilder
                (
                    const NXString & parameterID /** parameterid */ 
                );
                /** Returns the ude parameter builder by parameter ID  @return  the ude parameter builder 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                NXOpen::SIM::PostConfigurator::UdeParameterBuilder * GetUdeParameterBuilder
                (
                    const char * parameterID /** parameterid */ 
                );
                /** Renames the parameter ID 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void RenameParameterID
                (
                    NXOpen::SIM::PostConfigurator::UdeParameterBuilder * itemBuilder /** itembuilder */ ,
                    const NXString & oldParameterID /** oldparameterid */ ,
                    const NXString & newParameterID /** newparameterid */ 
                );
                /** Renames the parameter ID 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                void RenameParameterID
                (
                    NXOpen::SIM::PostConfigurator::UdeParameterBuilder * itemBuilder /** itembuilder */ ,
                    const char * oldParameterID /** oldparameterid */ ,
                    const char * newParameterID /** newparameterid */ 
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
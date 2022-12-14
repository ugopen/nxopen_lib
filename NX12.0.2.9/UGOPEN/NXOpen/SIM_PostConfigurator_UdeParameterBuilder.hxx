#ifndef NXOpen_SIM_POSTCONFIGURATOR_UDEPARAMETERBUILDER_HXX_INCLUDED
#define NXOpen_SIM_POSTCONFIGURATOR_UDEPARAMETERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SIM_PostConfigurator_UdeParameterBuilder.ja
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
            class UdeParameterBuilder;
        }
    }
    class Builder;
    namespace SIM
    {
        namespace PostConfigurator
        {
            class _UdeParameterBuilderBuilder;
            class UdeParameterBuilderImpl;
            /** This class is used to create a new event item.
                        Calling @link Builder::Commit Builder::Commit@endlink  on this builder will only return NULL.
                     <br> To create a new instance of this class, use @link NXOpen::SIM::PostConfigurator::PostConfiguratorManager::CreateUdeParameterBuilder  NXOpen::SIM::PostConfigurator::PostConfiguratorManager::CreateUdeParameterBuilder @endlink  <br> 
             <br>  Created in NX12.0.1.  <br>  
            */
            class NXOPENCPP_SIMEXPORT  UdeParameterBuilder : public NXOpen::Builder
            {
                /** Type of Event Item  */
                public: enum Type
                {
                    TypeGroup/** Group       */,
                    TypeDouble/** Double      */,
                    TypeInteger/** Integer     */,
                    TypeString/** String      */,
                    TypeBoolean/** Boolean     */,
                    TypeEnumeration/** Enumeration */,
                    TypeVector/** Vector      */,
                    TypePoint/** Point       */,
                    TypeBitmap/** Bitmap      */
                };

                /** Type of Group State  */
                public: enum GroupStateType
                {
                    GroupStateTypeOpen/** Open   */,
                    GroupStateTypeClosed/** Closed */,
                    GroupStateTypeEnd/** End */
                };

                /** Type of Event Parameter Status */
                public: enum ParameterStatusType
                {
                    ParameterStatusTypeNone/** None - Text Status is Invisible  */,
                    ParameterStatusTypeOn/** On   - Text Status is Activate   */,
                    ParameterStatusTypeOff/** Off  - Text Status is Deactivate */
                };

                private: UdeParameterBuilderImpl * m_udeparameterbuilder_impl;
                private: friend class  _UdeParameterBuilderBuilder;
                protected: UdeParameterBuilder();
                public: ~UdeParameterBuilder();
                /**Returns  the item type 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SIM::PostConfigurator::UdeParameterBuilder::Type ItemType
                (
                );
                /**Sets  the item type 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void SetItemType
                (
                    NXOpen::SIM::PostConfigurator::UdeParameterBuilder::Type itemType /** itemtype */ 
                );
                /**Returns  the parameter ID 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: NXString ParameterID
                (
                );
                /**Sets  the parameter ID 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void SetParameterID
                (
                    const NXString & paramID /** paramid */ 
                );
                /**Sets  the parameter ID 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                void SetParameterID
                (
                    const char * paramID /** paramid */ 
                );
                /**Returns  the User Interface Label 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: NXString UILabel
                (
                );
                /**Sets  the User Interface Label 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void SetUILabel
                (
                    const NXString & uiLabel /** uilabel */ 
                );
                /**Sets  the User Interface Label 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                void SetUILabel
                (
                    const char * uiLabel /** uilabel */ 
                );
                /**Returns  the toggle default value 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: bool ToggleDefaultValue
                (
                );
                /**Sets  the toggle default value 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void SetToggleDefaultValue
                (
                    bool toggleDefaultValue /** toggledefaultvalue */ 
                );
                /**Returns  the group state 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SIM::PostConfigurator::UdeParameterBuilder::GroupStateType GroupState
                (
                );
                /**Sets  the group state 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void SetGroupState
                (
                    NXOpen::SIM::PostConfigurator::UdeParameterBuilder::GroupStateType state /** state */ 
                );
                /**Returns  the double default value 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: double DoubleDefaultValue
                (
                );
                /**Sets  the double default value 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void SetDoubleDefaultValue
                (
                    double doubleDefaultValue /** doubledefaultvalue */ 
                );
                /**Returns  the integer default value 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: int IntegerDefaultValue
                (
                );
                /**Sets  the integer default value 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void SetIntegerDefaultValue
                (
                    int integerDefaultValue /** integerdefaultvalue */ 
                );
                /** Gets a list of enumeration items  @return  the list of enumeration items 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: std::vector<NXString> GetEnumerationItems
                (
                );
                /** Sets a list of enumeration items 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void SetEnumerationItems
                (
                    std::vector<NXString> & enumerationItems /** the list of enumeration items */
                );
                /**Returns  the enumumeration item default value 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: NXString EnumerationDefaultValue
                (
                );
                /**Sets  the enumumeration item default value 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void SetEnumerationDefaultValue
                (
                    const NXString & enumerationDefaultValue /** enumerationdefaultvalue */ 
                );
                /**Sets  the enumumeration item default value 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                void SetEnumerationDefaultValue
                (
                    const char * enumerationDefaultValue /** enumerationdefaultvalue */ 
                );
                /**Returns  the string default value 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: NXString StringDefaultValue
                (
                );
                /**Sets  the string default value 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void SetStringDefaultValue
                (
                    const NXString & stringDefaultValue /** stringdefaultvalue */ 
                );
                /**Sets  the string default value 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                void SetStringDefaultValue
                (
                    const char * stringDefaultValue /** stringdefaultvalue */ 
                );
                /**Returns  the item status 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SIM::PostConfigurator::UdeParameterBuilder::ParameterStatusType ParameterStatus
                (
                );
                /**Sets  the item status 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void SetParameterStatus
                (
                    NXOpen::SIM::PostConfigurator::UdeParameterBuilder::ParameterStatusType parameterStatus /** parameterstatus */ 
                );
                /** Sets the ude parameter builder group 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : nx_post_config_full ("NX Post Configurator") OR nx_post_config_adv ("NX Post Configurator") */
                public: void SetGroup
                (
                    NXOpen::SIM::PostConfigurator::UdeParameterBuilder * parentBuilder /** the parameter builder group */
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

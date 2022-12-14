#ifndef NXOpen_ROUTINGCOMMON_CUSTOMMANAGER_HXX_INCLUDED
#define NXOpen_ROUTINGCOMMON_CUSTOMMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     RoutingCommon_CustomManager.ja
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
#include <NXOpen/Routing_CustomManager.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_routingcommon_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace RoutingCommon
    {
        class CustomManager;
    }
    class Session;
    namespace Assemblies
    {
        class Component;
    }
    class NXObject;
    namespace Routing
    {
        class ComponentNamePluginData;
    }
    namespace Routing
    {
        class DesignRuleViolation;
    }
    namespace RoutingCommon
    {
        class CustomManagerImpl;
        /** The Routing Custom Manager allows you to customize the Routed System Designer (RSD)
                applications by adding plugins and design rules.  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGCOMMONEXPORT  CustomManager
        {
            public: /** This defines the prototype for all Routing design rules. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            typedef NXOpen::Callback2<void, NXOpen::Routing::CustomManager::DesignRuleReason, std::vector<NXOpen::NXObject *>> DesignRule;
            /** Defines the application for the enter and exit application plugins. */
            public: enum Application
            {
                ApplicationElectrical/** electrical */ ,
                ApplicationMechanical/** mechanical */ 
            };

            public: /** This defines the prototype for the plugin called when entering a
                        Routed System Designer (RSD) application. The plugin is given the
                        application being entered, either
                        @link NXOpen::RoutingCommon::CustomManager::Application::Electrical NXOpen::RoutingCommon::CustomManager::Application::Electrical@endlink  or
                        @link NXOpen::RoutingCommon::CustomManager::Application::Mechanical NXOpen::RoutingCommon::CustomManager::Application::Mechanical@endlink . 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            typedef NXOpen::Callback1<void, NXOpen::RoutingCommon::CustomManager::Application> RSDApplicationEnterPlugin;
            public: /** This defines the prototype for the plugin called when exiting a
                        Routed System Designer (RSD) application. The plugin is given the
                        application being exited, either
                        @link NXOpen::RoutingCommon::CustomManager::Application::Electrical NXOpen::RoutingCommon::CustomManager::Application::Electrical@endlink  or
                        @link NXOpen::RoutingCommon::CustomManager::Application::Mechanical NXOpen::RoutingCommon::CustomManager::Application::Mechanical@endlink . 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            typedef NXOpen::Callback1<void, NXOpen::RoutingCommon::CustomManager::Application> RSDApplicationExitPlugin;
            public: /** This defines the prototype for the Cableway XML file name plugin. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_cabling ("Routing Cabling") */
            typedef NXOpen::Callback0<NXString> CablewayXmlFileNamePlugin;
            public: /** This defines the prototype for the Cableway unique node name plugin.
                        The node may already have a unique ID set as the object name. It is this plugin's
                        responsibility to check for the existing unique ID and decide to use it or not.
                        Note: It is this plugin's responsibility to ensure uniqueness. Routing will not
                        check the returned value to make sure it is unique.
                    
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_cabling ("Routing Cabling") */
            typedef NXOpen::Callback3<NXString, NXString, NXOpen::Assemblies::Component *, NXOpen::NXObject *> CablewayUniqueNodeNamePlugin;
            public: /** This defines the prototype for the Cableway unique segment name plugin. May be given
                        a Routing segment, a curve, or a hanger component. Hanger components are represented
                        as a zero length segment and so need a unique segment ID. The segment may already have
                        a unique ID set as the object name. It is this plugin's responsibility to check for the
                        existing unique ID and decide to use it or not.
                        Note: It is this plugin's responsibility to ensure uniqueness. Routing will not
                        check the returned value to make sure it is unique.
                    
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_cabling ("Routing Cabling") */
            typedef NXOpen::Callback3<NXString, NXString, NXOpen::Assemblies::Component *, NXOpen::NXObject *> CablewayUniqueSegmentNamePlugin;
            public: /** This defines the prototype for the Cableway device identifier plugin.
                        When given a component, this plugin should return the identifier to use in the XML file
                        for the device that the component represents. Return NULL if the component should
                        not be exported to the XML file.
                    
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_cabling ("Routing Cabling") */
            typedef NXOpen::Callback1<NXString, NXOpen::Assemblies::Component *> CablewayDeviceIdentifierPlugin;
            public: /** This defines the prototype for the Cableway pre-export plugin. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_cabling ("Routing Cabling") */
            typedef NXOpen::Callback1<void, NXString> CablewayPreExportPlugin;
            public: /** This defines the prototype for the Cableway post-export plugin. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_cabling ("Routing Cabling") */
            typedef NXOpen::Callback1<void, NXString> CablewayPostExportPlugin;
            public: /** This defines the prototype for the Cableway area name plugin.
                        When given a component, this plugin should return the area name to use for that
                        component and its child components during a Cableway Export.
                    
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_cabling ("Routing Cabling") */
            typedef NXOpen::Callback1<NXString, NXOpen::Assemblies::Component *> CablewayAreaNamePlugin;
            public: /** This defines the prototype for the component name plugins used when Routing
                        needs to create a new component. You plugin should fill out the information on the
                        @link Routing::ComponentNamePluginData Routing::ComponentNamePluginData@endlink  object.
                    
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            typedef NXOpen::Callback1<void, NXOpen::Routing::ComponentNamePluginData *> ComponentNamePlugin;
            private: CustomManagerImpl * m_custommanager_impl;
            private: NXOpen::Session* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit CustomManager(NXOpen::Session *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~CustomManager();
            /** Adds the design rule with the given reason.
                        NOTE: You can register more than one design rule with the same reason.  @return  A unique identifier for your design rule. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: int AddDesignRule
            (
                NXOpen::Routing::CustomManager::DesignRuleReason reason /** The reason for which you want this design rule called. */,
                const NXString & name /** A descriptive name for this design rule. */,
                const NXString & description /** A detailed description of what this design rule checks. */,
                const NXOpen::RoutingCommon::CustomManager::DesignRule&  designRuleMethod /** The method you want to be called. */
            );
            /** Adds the design rule with the given reason.
                        NOTE: You can register more than one design rule with the same reason.  @return  A unique identifier for your design rule. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            int AddDesignRule
            (
                NXOpen::Routing::CustomManager::DesignRuleReason reason /** The reason for which you want this design rule called. */,
                const char * name /** A descriptive name for this design rule. */,
                const char * description /** A detailed description of what this design rule checks. */,
                const NXOpen::RoutingCommon::CustomManager::DesignRule&  designRuleMethod /** The method you want to be called. */
            );
            /** Removes the registered design rule. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void RemoveDesignRule
            (
                int designRuleMethodId /** The design rule identifier indicating which design rule to remove. */
            );
            /** Removes all the design rules registered for a particular reason. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void RemoveAllDesignRulesForReason
            (
                NXOpen::Routing::CustomManager::DesignRuleReason reason /** The reason for which you want to remove all the design rules. */
            );
            /** Removes all the registered design rules, except those configured in the Application View (APV) file. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void RemoveAllDesignRules
            (
            );
            /** Returns the design rules, if any, registered for the given reason. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void GetDesignRulesRegisteredForReason
            (
                NXOpen::Routing::CustomManager::DesignRuleReason reason /** The reason for which you want a list of design rules. */,
                std::vector<int> & registeredDesignRuleIds /** The design rule identifiers, if any, registered with this reason. */
            );
            /** Returns any violations recorded against a design rule reason.  @return  The violations for this reason. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: std::vector<NXOpen::Routing::DesignRuleViolation *> GetViolationsForReason
            (
                NXOpen::Routing::CustomManager::DesignRuleReason reason /** The reason for which you want a list of violations. */
            );
            /** Returns any violations recorded against a design rule.  @return  The violations for this reason. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: std::vector<NXOpen::Routing::DesignRuleViolation *> GetViolationsOfRule
            (
                const NXString & designRuleName /** The Design Rule for which you want a list of violations. */
            );
            /** Returns any violations recorded against a design rule.  @return  The violations for this reason. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            std::vector<NXOpen::Routing::DesignRuleViolation *> GetViolationsOfRule
            (
                const char * designRuleName /** The Design Rule for which you want a list of violations. */
            );
            /** Creates a new violation for a design rule reason.  @return  The newly created violation object. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXOpen::Routing::DesignRuleViolation * CreateViolationForReason
            (
                const NXString & designRuleName /** The Design Rule for which you want to create a new violation. */,
                NXOpen::Routing::CustomManager::DesignRuleReason reason /** The reason for which you want to create a new violation. */,
                const NXString & shortDescription /** A short description of the violation displayed as the message on the Design Rule Violation dialog. */,
                const NXString & longDescription /** A more detailed description of the violation displayed by the Full Violation Text button on the Design Rule Violation dialog. */,
                const std::vector<NXOpen::NXObject *> & objects /** The objects in violation. */
            );
            /** Creates a new violation for a design rule reason.  @return  The newly created violation object. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            NXOpen::Routing::DesignRuleViolation * CreateViolationForReason
            (
                const char * designRuleName /** The Design Rule for which you want to create a new violation. */,
                NXOpen::Routing::CustomManager::DesignRuleReason reason /** The reason for which you want to create a new violation. */,
                const char * shortDescription /** A short description of the violation displayed as the message on the Design Rule Violation dialog. */,
                const char * longDescription /** A more detailed description of the violation displayed by the Full Violation Text button on the Design Rule Violation dialog. */,
                const std::vector<NXOpen::NXObject *> & objects /** The objects in violation. */
            );
            /** Finds the violation of a design rule reason attached to the given object and deletes it.
                        Useful when the given object no longer violates this rule.
                        This method calls update after deleting the violations. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void DeleteViolationsOnObjectForReason
            (
                NXOpen::Routing::CustomManager::DesignRuleReason reason /** The reason for which you want to delete a violation. */,
                NXOpen::NXObject * nxObject /** The object on which to delete the violation. */
            );
            /** Finds the violation of a design rule attached to the given object and deletes it.
                        Useful when the given object no longer violates this rule.
                        This method calls update after deleting the violations. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: void DeleteViolationsOfRuleOnObject
            (
                const NXString & designRuleName /** The Design Rule for which you want to delete a violation. */,
                NXOpen::NXObject * nxObject /** The object on which to delete the violation. */
            );
            /** Finds the violation of a design rule attached to the given object and deletes it.
                        Useful when the given object no longer violates this rule.
                        This method calls update after deleting the violations. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            void DeleteViolationsOfRuleOnObject
            (
                const char * designRuleName /** The Design Rule for which you want to delete a violation. */,
                NXOpen::NXObject * nxObject /** The object on which to delete the violation. */
            );
            /** Removes all the registered plugins. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void RemoveAllPlugins
            (
            );
            /** Sets the plugin Routing will call when entering a Routed System Designer (RSD) application.
                        Will throw an error if one is already registered.
                    
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetRSDApplicationEnterPlugin
            (
                const NXOpen::RoutingCommon::CustomManager::RSDApplicationEnterPlugin&  applicationEnterPlugin /** The method you want Routing to call when entering the application. */
            );
            /** Removes any registered application enter plugin. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void RemoveRSDApplicationEnterPlugin
            (
            );
            /** Sets the plugin Routing will call when exiting a Routed System Designer (RSD) application.
                        Will throw an error if one is already registered.
                    
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetRSDApplicationExitPlugin
            (
                const NXOpen::RoutingCommon::CustomManager::RSDApplicationExitPlugin&  applicationExitPlugin /** The method you want Routing to call when exiting the application. */
            );
            /** Removes any registered application exit plugin. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void RemoveRSDApplicationExitPlugin
            (
            );
            /** Sets the plugin Routing will call before Cableway Export to get the name to use for
                        the Cableway XML file.
                        Will throw an error if one is already registered.
                    
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_cabling ("Routing Cabling") */
            public: void SetCablewayXmlFileNamePlugin
            (
                const NXOpen::RoutingCommon::CustomManager::CablewayXmlFileNamePlugin&  xmlFileNamePlugin /** The method you want Routing to call to get the XML file name. */
            );
            /** Removes any registered Cableway XML file name plugin. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_cabling ("Routing Cabling") */
            public: void RemoveCablewayXmlFileNamePlugin
            (
            );
            /** Sets the plugin Routing will call during Cableway Export to get a new, unique name for
                        the node in the XML file that represents the given @link Routing::ControlPoint Routing::ControlPoint@endlink .
                        Note: It is this plugin's responsibility to ensure uniqueness. Routing will not
                        check the returned value to make sure it is unique.
                        Will throw an error if one is already registered.
                    
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_cabling ("Routing Cabling") */
            public: void SetCablewayUniqueNodeNamePlugin
            (
                const NXOpen::RoutingCommon::CustomManager::CablewayUniqueNodeNamePlugin&  uniqueNodeNamePlugin /** The method you want Routing to call to get a new, unique name of this XML node. */
            );
            /** Removes any registered Cableway node unique name plugin. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_cabling ("Routing Cabling") */
            public: void RemoveCablewayUniqueNodeNamePlugin
            (
            );
            /** Sets the plugin Routing will call during Cableway Export to get a new, unique name for
                        the segment in the XML file that represents the given @link Routing::ISegment Routing::ISegment@endlink .
                        Note: It is this plugin's responsibility to ensure uniqueness. Routing will not
                        check the returned value to make sure it is unique.
                        Will throw an error if one is already registered.
                    
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_cabling ("Routing Cabling") */
            public: void SetCablewayUniqueSegmentNamePlugin
            (
                const NXOpen::RoutingCommon::CustomManager::CablewayUniqueSegmentNamePlugin&  uniqueSegmentNamePlugin /** The method you want Routing to call to get a new, unique name of this XML segment. */
            );
            /** Removes any registered Cableway segment unique name plugin. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_cabling ("Routing Cabling") */
            public: void RemoveCablewayUniqueSegmentNamePlugin
            (
            );
            /** Sets the plugin Routing will call to determine if a device component should be
                        included in the Cableway Export. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_cabling ("Routing Cabling") */
            public: void SetCablewayDeviceIdentifierPlugin
            (
                const NXOpen::RoutingCommon::CustomManager::CablewayDeviceIdentifierPlugin&  cablewayDeviceIdentifierPlugin /** The method you want Routing to call to determine if a device component should be
                                included in the Cableway Export. */
            );
            /** Removes any registered Cableway device identifier plugin. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_cabling ("Routing Cabling") */
            public: void RemoveCablewayDeviceIdentifierPlugin
            (
            );
            /** Sets the plugin Routing will call after Cableway pre-export. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_cabling ("Routing Cabling") */
            public: void SetCablewayPreExportPlugin
            (
                const NXOpen::RoutingCommon::CustomManager::CablewayPreExportPlugin&  cablewayPreExportPlugin /** The method you want Routing to call just before exporting a Cableway XML file. */
            );
            /** Removes any registered Cableway pre-export plugin. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_cabling ("Routing Cabling") */
            public: void RemoveCablewayPreExportPlugin
            (
            );
            /** Sets the plugin Routing will call after Cableway post-export. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_cabling ("Routing Cabling") */
            public: void SetCablewayPostExportPlugin
            (
                const NXOpen::RoutingCommon::CustomManager::CablewayPostExportPlugin&  cablewayPostExportPlugin /** The method you want Routing to call after exporting a Cableway XML file. */
            );
            /** Removes any registered Cableway post-export plugin. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_cabling ("Routing Cabling") */
            public: void RemoveCablewayPostExportPlugin
            (
            );
            /** Sets the plugin Routing will call to determine the area name. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_cabling ("Routing Cabling") */
            public: void SetCablewayAreaNamePlugin
            (
                const NXOpen::RoutingCommon::CustomManager::CablewayAreaNamePlugin&  cablewayAreaNamePlugin /** The method you want Routing to call to determine the area name. */
            );
            /** Removes any registered Cableway area name plugin. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_cabling ("Routing Cabling") */
            public: void RemoveCablewayAreaNamePlugin
            (
            );
            /** Sets the wiring component name plugin.
                        Will throw an error if one is already registered.
                    
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetWiringComponentNamePlugin
            (
                const NXOpen::RoutingCommon::CustomManager::ComponentNamePlugin&  wiringComponentNamePlugin /** The method you want Routing to call to get the wiring component name. */
            );
            /** Removes any registered wiring component name plugin, except one configured in the Application View (APV) file. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void RemoveWiringComponentNamePlugin
            (
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

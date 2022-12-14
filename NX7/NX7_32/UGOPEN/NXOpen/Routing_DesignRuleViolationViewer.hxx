#ifndef NXOpen_ROUTING_DESIGNRULEVIOLATIONVIEWER_HXX_INCLUDED
#define NXOpen_ROUTING_DESIGNRULEVIOLATIONVIEWER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_DesignRuleViolationViewer.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/Routing_DesignRuleViolationViewer.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class DesignRuleViolationViewer;
    }
    class Builder;
    namespace Routing
    {
        class _DesignRuleViolationViewerBuilder;
        /** This class can be used to set the violation id, update text for overridding the violation and 
                update the user name used to override the violation.  <br> To create a new instance of this class, use @link Routing::RouteManager::CreateDesignRuleViolationViewer Routing::RouteManager::CreateDesignRuleViolationViewer@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        DialogViolationId </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FilterOptionValue </td> <td> 
         
        AllViolations </td> </tr> 

        <tr><td> 
         
        NavigateViolationLocationOption </td> <td> 
         
        true </td> </tr> 

        <tr><td> 
         
        OverrideOptionValue </td> <td> 
         
        No </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT DesignRuleViolationViewer : public Builder
        {
            /** Enumerations to show options for filter. */
            public: enum FilterOption
            {
                FilterOptionAllViolations/** will show all violations */,
                FilterOptionSkipOverrides/** will not show overridden violations */,
                FilterOptionOverridesOnly/** will show only overridden violations */
            };

            /** Enumerations to show options for override */
            public: enum OverrideOption
            {
                OverrideOptionYes/** this shows that current violation is overridden violations */,
                OverrideOptionNo/** this shows that current violation is not overridden. */
            };

            private: friend class  _DesignRuleViolationViewerBuilder;
            protected: DesignRuleViolationViewer();
            /**Returns  the dialog design rule violation Id  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: int DialogViolationId
            (
            );
            /**Sets  the dialog design rule violation Id  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetDialogViolationId
            (
                int dialogViolationID /** dialogviolationid */ 
            );
            /**Returns  the state of Violation Location toggle option, 
                        if true: Navigate Violation Locations of current violation
                        if false: Navigate Violations.   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: bool NavigateViolationLocationOption
            (
            );
            /**Sets  the state of Violation Location toggle option, 
                        if true: Navigate Violation Locations of current violation
                        if false: Navigate Violations.   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetNavigateViolationLocationOption
            (
                bool navigateViolationLocationOption /** navigateviolationlocationoption */ 
            );
            /**Returns  the value for filter option of route Design Rule Violation   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::DesignRuleViolationViewer::FilterOption FilterOptionValue
            (
            );
            /**Sets  the value for filter option of route Design Rule Violation   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetFilterOptionValue
            (
                NXOpen::Routing::DesignRuleViolationViewer::FilterOption filterOptionValue /** filter option value */ 
            );
            /**Returns  the value for design Rule Violation override option
                        if Yes: violation is overridden
                        if No:  violation is not overridden  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::DesignRuleViolationViewer::OverrideOption OverrideOptionValue
            (
            );
            /**Sets  the value for design Rule Violation override option
                        if Yes: violation is overridden
                        if No:  violation is not overridden  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetOverrideOptionValue
            (
                NXOpen::Routing::DesignRuleViolationViewer::OverrideOption overrideOptionValue /** override option value */ 
            );
            /**Returns  the username who has overridden design Rule violation  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString Username
            (
            );
            /**Sets  the username who has overridden design Rule violation  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetUsername
            (
                const NXString & username /** username */ 
            );
            /** Returns the text written as a reason for overriding the violation  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXString> GetOverrideText
            (
            );
            /** Sets the text for reason of overriding the violation  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetOverrideText
            (
                const std::vector<NXString> & overrideText /** overridetext */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif

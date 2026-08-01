/*==================================================================================================

    This material contains trade secrets or otherwise confidential information owned by
    Siemens Industry Software Inc. or its affiliates (collectively, "SISW"), or its licensors.
    Access to and use of this information is strictly limited as set forth in the Customer's
    applicable agreements with SISW.

    Unpublished work Copyright 2024 Siemens

====================================================================================================

    NOTE:  NX Development provides programming examples for illustration only.
    NX Development assumes you are familiar with the programming language
    demonstrated in these examples, and the tools used to create and debug NX/Open
    programs. GTAC support professionals can help explain the functionality of
    a particular procedure, but neither GTAC nor NX Development will modify
    these examples to provide added functionality or construction procedures.

File description:

    Implements an example Routed System Design (RSD) Mechanical connection compatibility design rule.

    This example design rule will handle an interactive check as well as a concurrent check after
    placing a part.


==================================================================================================*/
#ifndef Routing_Example_Compatibility_DesignRules_HPP_INCLUDED
#define Routing_Example_Compatibility_DesignRules_HPP_INCLUDED

#pragma once

#include <NXOpen/Routing_CustomManager.hxx>
#include <NXOpen/Session.hxx>

namespace NXOpen::Routing
{
    using StlNXObjectVector  = std::vector<NXObject*>;
    using StlViolationVector = std::vector<DesignRuleViolation*>;

    //----------------------------------------------------------------------------------------------
    // This class contains a few example design rules to show how to register C++ design rules
    // with the Routing Custom Manager design rule registry.
    class ConnectionCompatibilityDesignRule
    {
        //------------------------------------------------------------------------------------------
        // This default constructor registers the design rule.
        public: ConnectionCompatibilityDesignRule();

        //------------------------------------------------------------------------------------------
        // This is the method registered for the design rule.
        public: void CompatibilityDesignRule
        (
            CustomManager::DesignRuleReason reason,
            StlNXObjectVector               objects
        );

        //------------------------------------------------------------------------------------------
        public: ~ConnectionCompatibilityDesignRule() noexcept                                            = delete;
        public: ConnectionCompatibilityDesignRule( const ConnectionCompatibilityDesignRule& )            = delete;
        public: ConnectionCompatibilityDesignRule& operator=( const ConnectionCompatibilityDesignRule& ) = delete;
        public: ConnectionCompatibilityDesignRule( ConnectionCompatibilityDesignRule&& )                 = delete;
        public: ConnectionCompatibilityDesignRule& operator=( ConnectionCompatibilityDesignRule&& )      = delete;
    };

    extern ConnectionCompatibilityDesignRule* theDesignRule;
}

#endif // Routing_Example_Compatibility_DesignRules_HPP_INCLUDED

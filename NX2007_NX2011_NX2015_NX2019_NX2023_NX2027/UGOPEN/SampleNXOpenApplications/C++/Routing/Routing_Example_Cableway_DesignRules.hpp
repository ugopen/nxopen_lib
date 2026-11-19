/*==================================================================================================
                                       Copyright 2021 Siemens
====================================================================================================

    NOTE:  NX Development provides programming examples for illustration only.
    NX Development assumes you are familiar with the programming language
    demonstrated in these examples, and the tools used to create and debug NX/Open
    programs. GTAC support professionals can help explain the functionality of
    a particular procedure, but neither GTAC nor NX Development will modify
    these examples to provide added functionality or construction procedures.

File description:

    The interface for a C++ class that implements example Routing Cableway Design Rules.

    See Routing_Example_Cableway_DesignRules.cpp for the implementation.


==================================================================================================*/
#ifndef CablewayDesignRules_HPP_INCLUDED
#define CablewayDesignRules_HPP_INCLUDED

#pragma once

#include <vector>

#include <NXOpen/NXObject.hxx>
#include <NXOpen/Routing_CustomManager.hxx>
#include <NXOpen/Routing_DesignRuleViolation.hxx>

namespace NXOpen
{
    namespace Routing
    {
        using StlNXObjectVector = std::vector<NXObject *>;

        //------------------------------------------------------------------------------------------
        // This class contains an example design rule to show how to register C++ design rules
        // with the Routing Custom Manager design rule registry and how to check segregation codes
        // on multi-tiered hangers, penetrations, and trays.
        class DesignRules
        {
            //--------------------------------------------------------------------------------------
            // This default constructor registers the SegregationCodeDesignRule design rule.
            public: DesignRules();

            //--------------------------------------------------------------------------------------
            // Called only during an interactive design rule check.
            // 
            // Looks through all components under the work part looking for tiered hangers, 
            // penetrations, and trays on segments. If the component or segment has a TierCount
            // attribute whose value is greater than zero, this check validates that the 
            // segregation code does not have more values than there are tiers.
            //
            // \param[in]
            //      reason
            //          The reason Routing is calling this design rule.
            //          Does nothing if not DesignRuleReasonCablewayValidation.
            //
            // \param[in]
            //      objects
            //          Ignored. The rule searches for all components under the work part.
            public: void SegregationCodeDesignRule
            (
                CustomManager::DesignRuleReason reason,
                StlNXObjectVector               objects
            );

            //--------------------------------------------------------------------------------------
            private: int m_segregationCodeRuleId = -1;
        };

        extern DesignRules* theDesignRules = nullptr;
    }
}

#endif // CablewayDesignRules_HPP_INCLUDED

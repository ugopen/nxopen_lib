/*==================================================================================================
               Copyright 2017 Siemens Product Lifecycle Management Software Inc.
====================================================================================================

    NOTE:  NX Development provides programming examples for illustration only.
    NX Development assumes you are familiar with the programming language
    demonstrated in these examples, and the tools used to create and debug NX/Open
    programs. GTAC support professionals can help explain the functionality of
    a particular procedure, but neither GTAC nor NX Development will modify
    these examples to provide added functionality or construction procedures.

File description:

    The interface for a C++ class that implements example Routing Design Rules.

    See Routing_Example_DesignRules.cpp for the implementation.


==================================================================================================*/
#ifndef DesignRules_HPP_INCLUDED
#define DesignRules_HPP_INCLUDED

#ifdef USE_PRAGMA_ONCE
#pragma once
#endif

#include <sstream>
#include <string>
#include <vector>

#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/LogFile.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Routing_CustomManager.hxx>
#include <NXOpen/Routing_DesignRuleViolation.hxx>
#include <NXOpen/Session.hxx>

namespace NXOpen
{
    namespace Routing
    {
        using StlNXObjectVector  = std::vector<NXObject *>;
        using StlViolationVector = std::vector<DesignRuleViolation *>;

        //------------------------------------------------------------------------------------------
        // This class contains a few example design rules to show how to register C++ design rules
        // with the Routing Custom Manager design rule registry.
        class DesignRules
        {
            //--------------------------------------------------------------------------------------
            // This default constructor registers every design rule listed below.
            public: DesignRules();

            //--------------------------------------------------------------------------------------
            // Called whenever a path is made.
            //
            // \param[in]
            //      reason
            //          The reason Routing is calling this design rule.
            //          Must be either DesignRuleReasonCreatePath or DesignRuleReasonInteractive.
            //
            // \param[in]
            //      objects
            //          The segments just created by the Create Path command.
            public: void CreatePathDesignRule
            (
                CustomManager::DesignRuleReason reason,
                StlNXObjectVector               objects
            );

            //--------------------------------------------------------------------------------------
            // Called whenever a segment is subdivided.
            //
            // \param[in]
            //      reason
            //          The reason Routing is calling this design rule.
            //          Must be either DesignRuleReasonSubdivideSegment or DesignRuleReasonInteractive.
            //
            // \param[in]
            //      objects
            //          The segments just created by the Create Path command.
            public: void SubdivideSegmentDesignRule
            (
                CustomManager::DesignRuleReason reason,
                StlNXObjectVector               objects
            );

            //--------------------------------------------------------------------------------------
            // Called during an interactive check to verify that modular connectors are placed on
            // the correct port on their parent connector.
            //
            // \param[in]
            //      reason
            //          The reason Routing is calling this design rule.
            //          Must be DesignRuleReasonInteractive.
            //
            // \param[in]
            //      objects
            //          This is empty for interactive checks, so it's not used.
            public: void ModularConnectorDesignRule
            (
                CustomManager::DesignRuleReason reason,
                StlNXObjectVector               /*objects*/
            );

            //--------------------------------------------------------------------------------------
            private: int m_createPathRuleId;
            private: int m_subdivideSegmentRuleId;
            private: int m_modularConnectorRuleId;
        };

        extern DesignRules* theDesignRules;
    }
}

#endif // DesignRules_HPP_INCLUDED

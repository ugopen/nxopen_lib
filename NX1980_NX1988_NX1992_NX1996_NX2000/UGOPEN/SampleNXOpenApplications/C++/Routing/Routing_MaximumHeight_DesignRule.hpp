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

The interface for a C++ class that implements example Routing Maximum Height Design Rule.

See Routing_MaximumHeight_DesignRule.cpp for the implementation.


==================================================================================================*/
#ifndef MAXIMMUMHEIGHT_DESIGNRULE_INCLUDED
#define MAXIMMUMHEIGHT_DESIGNRULE_INCLUDED

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
        using StlNXObjectVector = std::vector<NXObject *>;
        using StlViolationVector = std::vector<DesignRuleViolation *>;

        //------------------------------------------------------------------------------------------
        // This class registers the Maximum Height Design Rules with RoutingCustomManager
        class MaxHeightDesignRules
        {
            //--------------------------------------------------------------------------------------
            // This default constructor registers every design rule listed below.
            public: MaxHeightDesignRules();

            //--------------------------------------------------------------------------------------
            // Callback method for Maximum Height Desgin Rule
            //
            // \param[in]
            //      reason
            //          The reason Routing is calling this design rule.
            //
            // \param[in]
            //      objects
            //          The segments just which needs to be check for Maximum Height Design Rule
            public: void CreateMaximumHeightDesignRule
            (
                CustomManager::DesignRuleReason reason,
                StlNXObjectVector               objects
            );

            //--------------------------------------------------------------------------------------

            private: int m_maxHeightRuleForCreatePath;
            private: int m_maxHeightRuleForHealPath;
            private: int m_maxHeightRuleForAssignCorner;
            private: int m_maxHeightRuleForAssignStock;
            private: int m_maxHeightRuleForRemovePart;
            private: int m_maxHeightRuleForAutoRoutePinLevel;
            private: int m_maxHeightRuleForManualRoutePinLevel;
            private: int m_maxHeightRuleForAutoRouteComponentLevel;
            private: int m_maxHeightRuleForManualRouteComponentLevel;
            private: int m_maxHeightRuleForInteractive;
            private: int m_maxHeightRuleForTransformPath;
            private: int m_maxHeightRuleForEditCharacteristic;

        };

        extern MaxHeightDesignRules* maxHeightRule;
    }
}


#endif // MAXIMMUMHEIGHT_DESIGNRULE_INCLUDED

#ifndef NXOpen_LINEDESIGNER_DBSTAIRWAYEQUIPMENTNODE_HXX_INCLUDED
#define NXOpen_LINEDESIGNER_DBSTAIRWAYEQUIPMENTNODE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     LineDesigner_DBStairwayEquipmentNode.ja
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
#include <NXOpen/LineDesigner_DBSmartComplexEquipmentNode.hxx>
#include <NXOpen/liblinedesigneropencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace LineDesigner
    {
        class DBStairwayEquipmentNode;
    }
    namespace LineDesigner
    {
        class DBSmartComplexEquipmentNode;
    }
    namespace LineDesigner
    {
        class _DBStairwayEquipmentNodeBuilder;
        class DBStairwayEquipmentNodeImpl;
        /** Represents DB stairway equipment node  <br> To create a new instance of this class, use @link NXOpen::LineDesigner::DBNodeManager::CreateDBStairwayEquipmentNode  NXOpen::LineDesigner::DBNodeManager::CreateDBStairwayEquipmentNode @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class LINEDESIGNEROPENCPPEXPORT  DBStairwayEquipmentNode : public NXOpen::LineDesigner::DBSmartComplexEquipmentNode
        {
            private: DBStairwayEquipmentNodeImpl * m_dbstairwayequipmentnode_impl;
            private: friend class  _DBStairwayEquipmentNodeBuilder;
            protected: DBStairwayEquipmentNode();
            public: ~DBStairwayEquipmentNode();
            /** An API to add left railing to stairway 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void AddLeftRailing
            (
            );
            /** An API to add right railing to stairway 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void AddRightRailing
            (
            );
            /** An API to remove left railing to stairway 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void RemoveLeftRailing
            (
            );
            /** An API to remove right railing to stairway 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void RemoveRightRailing
            (
            );
            /** An API to remove both railings to stairway 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void RemoveBothRailing
            (
            );
        };
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
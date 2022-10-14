#ifndef NXOpen_AME_POUSELECTIONBUILDER_HXX_INCLUDED
#define NXOpen_AME_POUSELECTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_POUSelectionBuilder.ja
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
#include <NXOpen/AME_POUSelectionBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libameopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace AME
    {
        class POUSelectionBuilder;
    }
    class NXObject;
    class SelectNXObjectList;
    namespace AME
    {
        class _POUSelectionBuilderBuilder;
        class POUSelectionBuilderImpl;
        /** JA class for the insert Eng object dialog <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreatePouSelectionBuilder  NXOpen::AME::AMEManager::CreatePouSelectionBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  POUSelectionBuilder : public NXOpen::TaggedObject
        {
            private: POUSelectionBuilderImpl * m_pouselectionbuilder_impl;
            private: friend class  _POUSelectionBuilderBuilder;
            protected: POUSelectionBuilder();
            public: ~POUSelectionBuilder();
            /**Returns  the selected Groups
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::SelectNXObjectList * SelectGroup
            (
            );
            /**Returns  the selected Engineering Objects
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::SelectNXObjectList * SelectAdditionalObjs
            (
            );
            /** Add plc block
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void AddSoftwareObject
            (
                NXOpen::NXObject * swObject /** swobject */ 
            );
            /** Remove plc block
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void RemoveSoftwareObject
            (
                NXOpen::NXObject * plcBlock /** plcblock */ 
            );
            /** Add eo object
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void AddEoObject
            (
                NXOpen::NXObject * eoObject /** eoobject */ 
            );
            /** Remove eo object
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void RemoveEoObject
            (
                NXOpen::NXObject * eoObject /** eoobject */ 
            );
            /** Update plc block
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void UpdateToNewPlc
            (
                NXOpen::NXObject * station /** station */ 
            );
            /** Clear the selection
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void Clear
            (
            );
            /**Returns  the toggle whether to chech the station after the connect finished or not 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: bool CheckAfterConnect
            (
            );
            /**Sets  the toggle whether to chech the station after the connect finished or not 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetCheckAfterConnect
            (
                bool checkAfterConnect /** checkafterconnect */ 
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
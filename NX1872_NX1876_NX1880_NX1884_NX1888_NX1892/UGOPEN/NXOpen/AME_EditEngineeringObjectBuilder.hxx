#ifndef NXOpen_AME_EDITENGINEERINGOBJECTBUILDER_HXX_INCLUDED
#define NXOpen_AME_EDITENGINEERINGOBJECTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_EditEngineeringObjectBuilder.ja
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
#include <NXOpen/AME_EngineeringObjectAspectDetailBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObject.hxx>
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
        class EditEngineeringObjectBuilder;
    }
    namespace AME
    {
        class AMEEngObject;
    }
    namespace AME
    {
        class EngineeringObjectAspectDetailBuilder;
    }
    namespace AME
    {
        class SelectAMEBaseNodeList;
    }
    class Builder;
    class NXObject;
    class SelectNXObject;
    namespace AME
    {
        class _EditEngineeringObjectBuilderBuilder;
        class EditEngineeringObjectBuilderImpl;
        /** JA class for the Eng object dialog <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateEditEngineeringObjectBuilder  NXOpen::AME::AMEManager::CreateEditEngineeringObjectBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  EditEngineeringObjectBuilder : public NXOpen::Builder
        {
            /** Assign EOs or POUs */
            public: enum SourceType
            {
                SourceTypeAssignEos/** assign eos */ ,
                SourceTypeAssignPous/** assign pous */ 
            };

            private: EditEngineeringObjectBuilderImpl * m_editengineeringobjectbuilder_impl;
            private: friend class  _EditEngineeringObjectBuilderBuilder;
            protected: EditEngineeringObjectBuilder();
            public: ~EditEngineeringObjectBuilder();
            /**Returns  the string name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString EngObjName
            (
            );
            /**Sets  the string name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetEngObjName
            (
                const NXString & stringName /** stringname */ 
            );
            /**Sets  the string name 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetEngObjName
            (
                const char * stringName /** stringname */ 
            );
            /**Returns  the string description 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString EngObjDescription
            (
            );
            /**Sets  the string description 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetEngObjDescription
            (
                const NXString & stringDescription /** stringdescription */ 
            );
            /**Sets  the string description 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetEngObjDescription
            (
                const char * stringDescription /** stringdescription */ 
            );
            /**Returns  the aspect detail ui block
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::EngineeringObjectAspectDetailBuilder * ListAspectDetail
            (
            );
            /**Adds selected objects for Edit an aspect
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetEngobjectsToEdit
            (
                const std::vector<NXOpen::AME::AMEEngObject *> & engObject /** Array of Engineering Objects */
            );
            /**Pass Aspect States To Builder
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetAspectStates
            (
                const std::vector<NXOpen::NXObject *> & roots /** Array of Engineering Roots */,
                const std::vector<int> & states /** Array of States */
            );
            /**Returns  the selected plc symbols 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::SelectAMEBaseNodeList * SelectedPlcBaseSymbols
            (
            );
            /**Returns  the selection where the object will be reassigned. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::SelectNXObject * SelectionParent
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
#ifndef NXOpen_AME_REPORTTEMPLATE_HXX_INCLUDED
#define NXOpen_AME_REPORTTEMPLATE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_ReportTemplate.ja
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
#include <NXOpen/AME_ReportHeaderPlaceHolderDataNode.hxx>
#include <NXOpen/AME_ReportPlaceHolderData.hxx>
#include <NXOpen/NXObject.hxx>
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
        class ReportTemplate;
    }
    namespace AME
    {
        class ReportHeaderPlaceHolderDataNode;
    }
    namespace AME
    {
        class ReportPlaceHolderData;
    }
    class NXObject;
    namespace AME
    {
        class _ReportTemplateBuilder;
        class ReportTemplateImpl;
        /** JA class for the ReportTemplate object <br> This is an abstract class, and cannot be instantiated.  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  ReportTemplate : public NXOpen::NXObject
        {
            private: ReportTemplateImpl * m_reporttemplate_impl;
            private: friend class  _ReportTemplateBuilder;
            protected: ReportTemplate();
            public: ~ReportTemplate();
            /** Set content placeholder data 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetContentPlaceholderDataAt
            (
                NXOpen::AME::ReportPlaceHolderData * dataObject /** dataobject */ ,
                int colIndex /** colindex */ 
            );
            /** Create content placeholder data 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::ReportPlaceHolderData * CreatePlaceholderData
            (
            );
            /** Reset placeholder data 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void ResetContentPlaceholderDataAt
            (
                int colIndex /** colindex */ 
            );
            /** Deletes placeholder data corresponding to input index 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void RemoveInputPlaceholderdata
            (
                const std::vector<int> & allSelectedColumnsOfTable /** allselectedcolumnsoftable */ 
            );
            /** Create header placeholder data node
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXOpen::AME::ReportHeaderPlaceHolderDataNode * CreateHeaderPlaceholderData
            (
            );
            /** Delete header placeholder data node
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void DeleteHeaderPlaceholderData
            (
                int colIndex /** colindex */ ,
                int rowIndex /** rowindex */ 
            );
            /** Set header placeholder data 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetHeaderPlaceholderDataAt
            (
                NXOpen::AME::ReportHeaderPlaceHolderDataNode * dataObject /** dataobject */ ,
                int counter /** counter */ 
            );
            /** Set header placeholder cell ref 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetHeaderPlaceholderCellRefAt
            (
                NXOpen::AME::ReportHeaderPlaceHolderDataNode * dataObject /** dataobject */ ,
                int colIndex /** colindex */ ,
                int rowIndex /** rowindex */ 
            );
            /** Update Placeholder chain and text rotation
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void UpdatePlaceholdersAndTextRotation
            (
                const NXString & currentTxt /** currenttxt */ ,
                int colIndex /** colindex */ ,
                int rowIndex /** rowindex */ ,
                bool isInHeader /** isinheader */ ,
                int textDir /** textdir */ 
            );
            /** Update Placeholder chain and text rotation
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void UpdatePlaceholdersAndTextRotation
            (
                const char * currentTxt /** currenttxt */ ,
                int colIndex /** colindex */ ,
                int rowIndex /** rowindex */ ,
                bool isInHeader /** isinheader */ ,
                int textDir /** textdir */ 
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

#ifndef NXOpen_REPORT_REPORTMANAGER_HXX_INCLUDED
#define NXOpen_REPORT_REPORTMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Report_ReportManager.ja
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
#include <NXOpen/Report_ReportPreference.hxx>
#include <NXOpen/Report_ResultXmlFileWriter.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_report_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Report
    {
        class ReportManager;
    }
    class Session;
    namespace Report
    {
        class AutomationLogger;
    }
    namespace Report
    {
        class CommandManager;
    }
    namespace Report
    {
        class ReportPreference;
    }
    namespace Report
    {
        class ResultXmlFileWriter;
    }
    namespace Report
    {
        class ReportManagerImpl;
        /** Represents the report manager.  <br> To obtain an instance of this class use @link NXOpen::Session::ReportManager NXOpen::Session::ReportManager@endlink .  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_REPORTEXPORT  ReportManager
        {
            private: ReportManagerImpl * m_reportmanager_impl;
            private: NXOpen::Session* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit ReportManager(NXOpen::Session *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~ReportManager();
            /** Creates a new @link NXOpen::Report::ResultXmlFileWriter NXOpen::Report::ResultXmlFileWriter@endlink  object. @return   
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Report::ResultXmlFileWriter * CreateResultXmlFileWriter
            (
            );
            /**Returns  the report preference. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Report::ReportPreference * Preference
            (
            );
            /** Gets the original dimension of a given image file. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void GetOriginalImageDimension
            (
                const NXString & imageFullFileName /** the full image file name */,
                double* width /** width */ ,
                double* height /** height */ 
            );
            /** Gets the original dimension of a given image file. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            void GetOriginalImageDimension
            (
                const char * imageFullFileName /** the full image file name */,
                double* width /** width */ ,
                double* height /** height */ 
            );


            /** Returns the @link NXOpen::Report::AutomationLogger NXOpen::Report::AutomationLogger@endlink  belonging to the report manager 
             <br>  Created in NX11.0.0.  <br>  
            */
            public: NXOpen::Report::AutomationLogger *AutomationLogger();
            /** Returns the @link NXOpen::Report::CommandManager NXOpen::Report::CommandManager@endlink  belonging to the report manager 
             <br>  Created in NX11.0.0.  <br>  
            */
            public: NXOpen::Report::CommandManager *CommandManager();
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
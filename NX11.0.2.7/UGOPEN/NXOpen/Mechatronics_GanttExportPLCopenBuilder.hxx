#ifndef NXOpen_MECHATRONICS_GANTTEXPORTPLCOPENBUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_GANTTEXPORTPLCOPENBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_GanttExportPLCopenBuilder.ja
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
#include <NXOpen/Mechatronics_GanttExportPLCopenBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_mechatronics_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mechatronics
    {
        class GanttExportPLCopenBuilder;
    }
    class Builder;
    namespace Mechatronics
    {
        class _GanttExportPLCopenBuilderBuilder;
        class GanttExportPLCopenBuilderImpl;
        /** Represents a @link NXOpen::Mechatronics::GanttOperationObject NXOpen::Mechatronics::GanttOperationObject@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Mechatronics::GanttCollection::CreateGanttExportPlcopenBuilder  NXOpen::Mechatronics::GanttCollection::CreateGanttExportPlcopenBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        ToggleLongName </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  GanttExportPLCopenBuilder : public NXOpen::Builder
        {
            private: GanttExportPLCopenBuilderImpl * m_ganttexportplcopenbuilder_impl;
            private: friend class  _GanttExportPLCopenBuilderBuilder;
            protected: GanttExportPLCopenBuilder();
            public: ~GanttExportPLCopenBuilder();
            /**Returns  the native file browser 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXString NativeFileBrowser
            (
            );
            /**Sets  the native file browser 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetNativeFileBrowser
            (
                const NXString & filename /** filename */ 
            );
            /**Sets  the native file browser 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            void SetNativeFileBrowser
            (
                const char * filename /** filename */ 
            );
            /**Returns  the toggle long name 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool ToggleLongName
            (
            );
            /**Sets  the toggle long name 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetToggleLongName
            (
                bool toggleLongName /** togglelongname */ 
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

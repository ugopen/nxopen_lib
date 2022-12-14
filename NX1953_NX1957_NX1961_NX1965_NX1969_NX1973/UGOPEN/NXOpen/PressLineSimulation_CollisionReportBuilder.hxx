#ifndef NXOpen_PRESSLINESIMULATION_COLLISIONREPORTBUILDER_HXX_INCLUDED
#define NXOpen_PRESSLINESIMULATION_COLLISIONREPORTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PressLineSimulation_CollisionReportBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/libpresslinesimulopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PressLineSimulation
    {
        class CollisionReportBuilder;
    }
    class Builder;
    namespace PressLineSimulation
    {
        class ICollisionReportable;
    }
    namespace PressLineSimulation
    {
        class _CollisionReportBuilderBuilder;
        class CollisionReportBuilderImpl;
        /** This class builds a report from the collisions collected by the static collision checker. <br> To create a new instance of this class, use @link NXOpen::PressLineSimulation::ApplicationManager::CreateCollisionReportBuilder  NXOpen::PressLineSimulation::ApplicationManager::CreateCollisionReportBuilder @endlink  <br> 
         <br>  Created in NX1953.0.0.  <br>  
        */
        class PRESSLINESIMULOPENCPPEXPORT  CollisionReportBuilder : public NXOpen::Builder
        {
            private: CollisionReportBuilderImpl * m_collisionreportbuilder_impl;
            private: friend class  _CollisionReportBuilderBuilder;
            protected: CollisionReportBuilder();
            public: ~CollisionReportBuilder();
            /**Returns  the export file path for the collision report
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ExportFilePath
            (
            );
            /**Sets  the export file path for the collision report
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_pls_die_checker (" NX Press Die Checker") OR nx_pls_line_setup (" NX Press Line Setup") */
            public: void SetExportFilePath
            (
                const NXString & filename /** filename */ 
            );
            /**Sets  the export file path for the collision report
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_pls_die_checker (" NX Press Die Checker") OR nx_pls_line_setup (" NX Press Line Setup") */
            void SetExportFilePath
            (
                const char * filename /** filename */ 
            );
            /**Returns  the report source.
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PressLineSimulation::ICollisionReportable * ReportSource
            (
            );
            /**Sets  the report source.
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_pls_die_checker (" NX Press Die Checker") OR nx_pls_line_setup (" NX Press Line Setup") */
            public: void SetReportSource
            (
                NXOpen::PressLineSimulation::ICollisionReportable * reportSource /** reportsource */ 
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

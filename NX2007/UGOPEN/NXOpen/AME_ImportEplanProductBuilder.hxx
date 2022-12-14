#ifndef NXOpen_AME_IMPORTEPLANPRODUCTBUILDER_HXX_INCLUDED
#define NXOpen_AME_IMPORTEPLANPRODUCTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AME_ImportEplanProductBuilder.ja
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
        class ImportEplanProductBuilder;
    }
    class Builder;
    namespace AME
    {
        class _ImportEplanProductBuilderBuilder;
        class ImportEplanProductBuilderImpl;
        /** Imports a eplan product xml file <br> To create a new instance of this class, use @link NXOpen::AME::AMEManager::CreateImportEplanProductBuilder  NXOpen::AME::AMEManager::CreateImportEplanProductBuilder @endlink  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class AMEOPENCPPEXPORT  ImportEplanProductBuilder : public NXOpen::Builder
        {
            private: ImportEplanProductBuilderImpl * m_importeplanproductbuilder_impl;
            private: friend class  _ImportEplanProductBuilderBuilder;
            protected: ImportEplanProductBuilder();
            public: ~ImportEplanProductBuilder();
            /**Returns  the xml file which is being imported 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: NXString FileToImport
            (
            );
            /**Sets  the xml file which is being imported 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void SetFileToImport
            (
                const NXString & fileToImport /** filetoimport */ 
            );
            /**Sets  the xml file which is being imported 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            void SetFileToImport
            (
                const char * fileToImport /** filetoimport */ 
            );
            /** Validate the Eplan Product xml import data. This should be called prior to commit. 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : ad_automation_design ("FULL AUTOMATION DESIGNER") */
            public: void ValidateEplanProductXmlData
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

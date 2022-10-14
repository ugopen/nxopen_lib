#ifndef NXOpen_WELD_WELDIMPORTBUILDER_HXX_INCLUDED
#define NXOpen_WELD_WELDIMPORTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_WeldImportBuilder.ja
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
#include <NXOpen/Weld_WeldImportBuilder.hxx>
#include <NXOpen/libnxopencpp_weld_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Weld
    {
        class WeldImportBuilder;
    }
    class Builder;
    namespace Weld
    {
        class _WeldImportBuilderBuilder;
        class WeldImportBuilderImpl;
        /** Creates Weld features by reading a csv file  <br> To create a new instance of this class, use @link NXOpen::Weld::WeldManager::CreateImportBuilder  NXOpen::Weld::WeldManager::CreateImportBuilder @endlink  <br> 
         <br>  Created in NX7.5.1.  <br>  
        */
        class NXOPENCPP_WELDEXPORT  WeldImportBuilder : public NXOpen::Builder
        {
            private: WeldImportBuilderImpl * m_weldimportbuilder_impl;
            private: friend class  _WeldImportBuilderBuilder;
            protected: WeldImportBuilder();
            public: ~WeldImportBuilder();
            /**Returns  the input csv file 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXString InputFile
            (
            );
            /**Sets  the input csv file 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: void SetInputFile
            (
                const NXString & filename /** filename */ 
            );
            /**Sets  the input csv file 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            void SetInputFile
            (
                const char * filename /** filename */ 
            );
            /**Returns  the template file indicating attribute mapping. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXString TemplateFile
            (
            );
            /**Sets  the template file indicating attribute mapping. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: void SetTemplateFile
            (
                const NXString & filename /** filename */ 
            );
            /**Sets  the template file indicating attribute mapping. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            void SetTemplateFile
            (
                const char * filename /** filename */ 
            );
            /**Returns  the option to indicate if warning messages need to be confirmed. If false setting, all warnings will be accepted. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool ConfirmWarningMessages
            (
            );
            /**Sets  the option to indicate if warning messages need to be confirmed. If false setting, all warnings will be accepted. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : structure_weld ("STRUCTURE WELD") */
            public: void SetConfirmWarningMessages
            (
                bool option /** option */ 
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
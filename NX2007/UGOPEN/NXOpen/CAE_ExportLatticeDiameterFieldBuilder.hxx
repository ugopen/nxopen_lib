#ifndef NXOpen_CAE_EXPORTLATTICEDIAMETERFIELDBUILDER_HXX_INCLUDED
#define NXOpen_CAE_EXPORTLATTICEDIAMETERFIELDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ExportLatticeDiameterFieldBuilder.ja
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
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class ExportLatticeDiameterFieldBuilder;
    }
    class Builder;
    namespace CAE
    {
        class _ExportLatticeDiameterFieldBuilderBuilder;
        class ExportLatticeDiameterFieldBuilderImpl;
        /**Exports lattice diameters to a field for a given solution <br> To create a new instance of this class, use @link NXOpen::CAE::SimSolution::CreateExportLatticeDiameterFieldBuilder  NXOpen::CAE::SimSolution::CreateExportLatticeDiameterFieldBuilder @endlink  <br> 
         <br>  Created in NX2007.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ExportLatticeDiameterFieldBuilder : public NXOpen::Builder
        {
            private: ExportLatticeDiameterFieldBuilderImpl * m_exportlatticediameterfieldbuilder_impl;
            private: friend class  _ExportLatticeDiameterFieldBuilderBuilder;
            protected: ExportLatticeDiameterFieldBuilder();
            public: ~ExportLatticeDiameterFieldBuilder();
            /**Returns the output field file 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXString FieldFile
            (
            );
            /**Sets the output field file 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetFieldFile
            (
                const NXString & filename /** filename */ 
            );
            /**Sets the output field file 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            void SetFieldFile
            (
                const char * filename /** filename */ 
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

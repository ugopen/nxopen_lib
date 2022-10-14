#ifndef NXOpen_CAE_ALTERNATEFEMREPRESENTATIONDATASOURCEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_ALTERNATEFEMREPRESENTATIONDATASOURCEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AlternateFemRepresentationDataSourceBuilder.ja
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
#include <NXOpen/CAE_DataReaderDatabaseOptions.hxx>
#include <NXOpen/CAE_SimResultReference.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class AlternateFemRepresentationDataSourceBuilder;
    }
    namespace CAE
    {
        class DataReaderDatabaseOptions;
    }
    namespace CAE
    {
        class SimResultReference;
    }
    namespace CAE
    {
        class _AlternateFemRepresentationDataSourceBuilderBuilder;
        class AlternateFemRepresentationDataSourceBuilderImpl;
        /**  @brief  Represents a @link NXOpen::CAE::AlternateFemRepresentationDataSourceBuilder NXOpen::CAE::AlternateFemRepresentationDataSourceBuilder@endlink  
            which can be used to create and edit data source for FemDataSets.  

           <br> This is an abstract class, and cannot be instantiated.  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  AlternateFemRepresentationDataSourceBuilder : public NXOpen::TaggedObject
        {
            private: AlternateFemRepresentationDataSourceBuilderImpl * m_alternatefemrepresentationdatasourcebuilder_impl;
            private: friend class  _AlternateFemRepresentationDataSourceBuilderBuilder;
            protected: AlternateFemRepresentationDataSourceBuilder();
            public: ~AlternateFemRepresentationDataSourceBuilder();
            /** Sets the file path or the managed file specification of the FEM dataset source file
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetFilePath
            (
                const NXString & filepath /** File path or managed file specification of the FEM dataset source file*/
            );
            /** Sets the file path or the managed file specification of the FEM dataset source file
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetFilePath
            (
                const char * filepath /** File path or managed file specification of the FEM dataset source file*/
            );
            /** Sets the result reference 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetResultReference
            (
                NXOpen::CAE::SimResultReference * pResultRef /** Result Reference associated to the Fem Data Set Source. */
            );
            /** Gets the database options  @return  DatabaseOptions of the Fem Data Set Source. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::DataReaderDatabaseOptions * GetDatabaseOptions
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
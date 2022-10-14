#ifndef NXOpen_CAE_ALTERNATEFEMREPRESENTATIONSOURCEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_ALTERNATEFEMREPRESENTATIONSOURCEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AlternateFemRepresentationSourceBuilder.ja
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
#include <NXOpen/CAE_AlternateFemRepresentationDataSourceBuilder.hxx>
#include <NXOpen/CAE_AlternateFemRepresentationSource.hxx>
#include <NXOpen/CAE_DataReaderDatabaseOptions.hxx>
#include <NXOpen/CAE_SimResultReference.hxx>
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
        class AlternateFemRepresentationSourceBuilder;
    }
    class BasePropertyTable;
    class Builder;
    namespace CAE
    {
        class AlternateFemRepresentationDataSourceBuilder;
    }
    namespace CAE
    {
        class AlternateFemRepresentationSource;
    }
    namespace CAE
    {
        class DataReaderDatabaseOptions;
    }
    namespace CAE
    {
        class SimResultReference;
    }
    class Unit;
    namespace CAE
    {
        class _AlternateFemRepresentationSourceBuilderBuilder;
        class AlternateFemRepresentationSourceBuilderImpl;
        /**  @brief  Represents a @link NXOpen::CAE::AlternateFemRepresentationSourceBuilder NXOpen::CAE::AlternateFemRepresentationSourceBuilder@endlink  
            which can be used to create FemDataSets.  

           <br> Not support KF.  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  AlternateFemRepresentationSourceBuilder : public NXOpen::Builder
        {
            private: AlternateFemRepresentationSourceBuilderImpl * m_alternatefemrepresentationsourcebuilder_impl;
            private: friend class  _AlternateFemRepresentationSourceBuilderBuilder;
            protected: AlternateFemRepresentationSourceBuilder();
            public: ~AlternateFemRepresentationSourceBuilder();
            /** Commits the changes that have been applied to the builder and returns
                    the edited or newly created @link NXOpen::CAE::AlternateFemRepresentationSource NXOpen::CAE::AlternateFemRepresentationSource@endlink   @return  The object being edited, or the new object. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::AlternateFemRepresentationSource * CommitAlternateFemRepresentationSource
            (
            );
            /** Sets the name of the FemDataSet 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /** Sets the name of the FemDataSet 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetName
            (
                const char * name /** name */ 
            );
            /** Sets the file path 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetFilePath
            (
                const NXString & filepath /** Name of the file associated to the Fem Data Set. */
            );
            /** Sets the file path 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetFilePath
            (
                const char * filepath /** Name of the file associated to the Fem Data Set. */
            );
            /** Sets the result reference 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetResultReference
            (
                NXOpen::CAE::SimResultReference * pResultRef /** Result Reference associated to the Fem Data Set. */
            );
            /** Gets the database options 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::DataReaderDatabaseOptions * GetDatabaseOptions
            (
            );
            /** Sets the length unit 
             <br>  @deprecated Deprecated in NX1872.0.0.  Use @link NXOpen::CAE::AlternateFemRepresentationSourceBuilder::GetDatabaseOptions NXOpen::CAE::AlternateFemRepresentationSourceBuilder::GetDatabaseOptions@endlink instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX1872.0.0.  Use NXOpen::CAE::AlternateFemRepresentationSourceBuilder::GetDatabaseOptionsinstead.") void SetLengthUnit
            (
                NXOpen::Unit * lengthUnit /** Length unit used to read the data file. */
            );
            /** Sets the mass unit 
             <br>  @deprecated Deprecated in NX1872.0.0.  Use @link NXOpen::CAE::AlternateFemRepresentationSourceBuilder::GetDatabaseOptions NXOpen::CAE::AlternateFemRepresentationSourceBuilder::GetDatabaseOptions@endlink instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX1872.0.0.  Use NXOpen::CAE::AlternateFemRepresentationSourceBuilder::GetDatabaseOptionsinstead.") void SetMassUnit
            (
                NXOpen::Unit * massUnit /** Mass unit used to read the data file. */
            );
            /** Sets the mesh creation mode 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetMeshCreationMode
            (
                NXOpen::CAE::AlternateFemRepresentationSource::CreateMeshMode creationMode /** Mesh creation mode used to read the data file. */
            );
            /**Returns  the @link NXOpen::BasePropertyTable NXOpen::BasePropertyTable@endlink  of the Alternate Fem Representation Source.
                        Not all Alternate Fem Representation Sources do have property table 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::BasePropertyTable * PropertyTable
            (
            );
            /** Gets the data sources names of the Alternate Fem Representation Source  @return  The data source names. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: std::vector<NXString> GetDataSourceNames
            (
            );
            /** Adds a new @link CAE::AlternateFemRepresentationDataSourceBuilder CAE::AlternateFemRepresentationDataSourceBuilder@endlink  in this builder and returns it.  @return  The new data source . 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::AlternateFemRepresentationDataSourceBuilder * GetNewDataSourceBuilder
            (
            );
            /** Removes the given @link CAE::AlternateFemRepresentationDataSourceBuilder CAE::AlternateFemRepresentationDataSourceBuilder@endlink  from this builder. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void RemoveDataSourceBuilder
            (
                NXOpen::CAE::AlternateFemRepresentationDataSourceBuilder * sourceBuilder /** sourcebuilder */ 
            );
            /** Gets the @link CAE::AlternateFemRepresentationDataSourceBuilder CAE::AlternateFemRepresentationDataSourceBuilder@endlink  of the main data source.  @return  The main data source builder. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::AlternateFemRepresentationDataSourceBuilder * GetMainDataSourceBuilder
            (
            );
            /** Gets the @link CAE::AlternateFemRepresentationDataSourceBuilder CAE::AlternateFemRepresentationDataSourceBuilder@endlink  of the data source with the given name. 
                       The name should be one retrieved from @link CAE::AlternateFemRepresentationSourceBuilder::GetDataSourceNames CAE::AlternateFemRepresentationSourceBuilder::GetDataSourceNames@endlink .  @return  The data source builder. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::AlternateFemRepresentationDataSourceBuilder * GetDataSourceBuilder
            (
                const NXString & dataSourceName /** the data source name. */
            );
            /** Gets the @link CAE::AlternateFemRepresentationDataSourceBuilder CAE::AlternateFemRepresentationDataSourceBuilder@endlink  of the data source with the given name. 
                       The name should be one retrieved from @link CAE::AlternateFemRepresentationSourceBuilder::GetDataSourceNames CAE::AlternateFemRepresentationSourceBuilder::GetDataSourceNames@endlink .  @return  The data source builder. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            NXOpen::CAE::AlternateFemRepresentationDataSourceBuilder * GetDataSourceBuilder
            (
                const char * dataSourceName /** the data source name. */
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
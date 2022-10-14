#ifndef NXOpen_CAE_MODELANDLOADPREPROCESSINPUTFILEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_MODELANDLOADPREPROCESSINPUTFILEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ModelAndLoadPreProcessInputFileBuilder.ja
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
#include <NXOpen/CAE_ModelAndLoadPreProcessOperationBuilder.hxx>
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
        class ModelAndLoadPreProcessInputFileBuilder;
    }
    namespace CAE
    {
        class DataReaderDatabaseOptions;
    }
    namespace CAE
    {
        class ModelAndLoadPreProcessOperationBuilder;
    }
    namespace CAE
    {
        class _ModelAndLoadPreProcessInputFileBuilderBuilder;
        class ModelAndLoadPreProcessInputFileBuilderImpl;
        /**
            Builds a @link NXOpen::CAE::ModelAndLoadPreProcessInputFile NXOpen::CAE::ModelAndLoadPreProcessInputFile@endlink  object which 
            represets an operation.
             <br> There is no kf creator for this.  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ModelAndLoadPreProcessInputFileBuilder : public NXOpen::CAE::ModelAndLoadPreProcessOperationBuilder
        {
            /** The quantity for the dataset*/
            public: enum Quantity
            {
                QuantityPressure/** pressure */ ,
                QuantityDisplacement/** displacement */ ,
                QuantityVelocity/** velocity */ ,
                QuantityAcceleration/** acceleration */ ,
                QuantityMassDensity/** mass density */ ,
                QuantitySpeedOfSound/** speed of sound */ ,
                QuantityForce/** force */ ,
                QuantityTemperature/** temperature */ ,
                QuantityRotation/** rotation */ ,
                QuantityAngularVelocity/** angular velocity */ ,
                QuantityAngularAcceleration/** angular acceleration */ ,
                QuantityMoment/** moment */ ,
                QuantityMPFDisplacement/** mpfdisplacement */ ,
                QuantityMPFVelocity/** mpfvelocity */ ,
                QuantityMPFAcceleration/** mpfacceleration */ ,
                QuantityModeDisplacement/** mode displacement */ ,
                QuantityModeRotation/** mode rotation */ 
            };

            /** The location for the dataset*/
            public: enum Location
            {
                LocationNode/** node */ ,
                LocationElement/** element */ ,
                LocationMotionElement/** motion element */ ,
                LocationMode/** mode */ 
            };

            /** The sorting for the dataset*/
            public: enum Sorting
            {
                SortingVectors/** vectors */ ,
                SortingFunctions/** functions */ 
            };

            /** Mesh source type (e.g. same as Data Source, File) */
            public: enum MeshSource
            {
                MeshSourceDataSource/** data source */ ,
                MeshSourceFile/** file */ 
            };

            /** The type of offset strategy to apply when processing MPFs */
            public: enum MpfOffsetStrategy
            {
                MpfOffsetStrategyNoOffset/** no offset */ ,
                MpfOffsetStrategyAutomaticOffset/** automatic offset */ ,
                MpfOffsetStrategyManualOffset/** manual offset */ 
            };

            private: ModelAndLoadPreProcessInputFileBuilderImpl * m_modelandloadpreprocessinputfilebuilder_impl;
            private: friend class  _ModelAndLoadPreProcessInputFileBuilderBuilder;
            protected: ModelAndLoadPreProcessInputFileBuilder();
            public: ~ModelAndLoadPreProcessInputFileBuilder();
            /**Returns  the data source file 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXString FilePath
            (
            );
            /**Sets  the data source file 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetFilePath
            (
                const NXString & filePath /** filepath */ 
            );
            /**Sets  the data source file 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetFilePath
            (
                const char * filePath /** filepath */ 
            );
            /**Returns  the data source database options 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DataReaderDatabaseOptions * DatabaseOptions
            (
            );
            /**Returns  the mesh source type (Data Source or File) 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::ModelAndLoadPreProcessInputFileBuilder::MeshSource MeshSourceType
            (
            );
            /**Sets  the mesh source type (Data Source or File) 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetMeshSourceType
            (
                NXOpen::CAE::ModelAndLoadPreProcessInputFileBuilder::MeshSource type /** type */ 
            );
            /**Returns  the mesh source file 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXString MeshFilePath
            (
            );
            /**Sets  the mesh source file 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetMeshFilePath
            (
                const NXString & filePath /** filepath */ 
            );
            /**Sets  the mesh source file 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetMeshFilePath
            (
                const char * filePath /** filepath */ 
            );
            /**Returns  the mesh source database options 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DataReaderDatabaseOptions * MeshDatabaseOptions
            (
            );
            /** Refreshes the data set list. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void RefreshDataSets
            (
            );
            /** Select query. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetQuerySelected
            (
                NXOpen::CAE::ModelAndLoadPreProcessInputFileBuilder::Quantity quantity /** quantity */ ,
                NXOpen::CAE::ModelAndLoadPreProcessInputFileBuilder::Location location /** location */ ,
                NXOpen::CAE::ModelAndLoadPreProcessInputFileBuilder::Sorting sorting /** sorting */ ,
                const NXString & name /** name */ ,
                bool selected /** selected */ 
            );
            /** Select query. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetQuerySelected
            (
                NXOpen::CAE::ModelAndLoadPreProcessInputFileBuilder::Quantity quantity /** quantity */ ,
                NXOpen::CAE::ModelAndLoadPreProcessInputFileBuilder::Location location /** location */ ,
                NXOpen::CAE::ModelAndLoadPreProcessInputFileBuilder::Sorting sorting /** sorting */ ,
                const char * name /** name */ ,
                bool selected /** selected */ 
            );
            /** Sets query target storage name. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetQueryTargetStorageName
            (
                NXOpen::CAE::ModelAndLoadPreProcessInputFileBuilder::Quantity quantity /** quantity */ ,
                NXOpen::CAE::ModelAndLoadPreProcessInputFileBuilder::Location location /** location */ ,
                NXOpen::CAE::ModelAndLoadPreProcessInputFileBuilder::Sorting sorting /** sorting */ ,
                const NXString & name /** name */ ,
                const NXString & targetStorageName /** targetstoragename */ 
            );
            /** Sets query target storage name. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetQueryTargetStorageName
            (
                NXOpen::CAE::ModelAndLoadPreProcessInputFileBuilder::Quantity quantity /** quantity */ ,
                NXOpen::CAE::ModelAndLoadPreProcessInputFileBuilder::Location location /** location */ ,
                NXOpen::CAE::ModelAndLoadPreProcessInputFileBuilder::Sorting sorting /** sorting */ ,
                const char * name /** name */ ,
                const char * targetStorageName /** targetstoragename */ 
            );
            /** Select or deselect a subcase. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetSubcaseSelected
            (
                const NXString & subcaseName /** subcasename */ ,
                bool selected /** selected */ 
            );
            /** Select or deselect a subcase. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetSubcaseSelected
            (
                const char * subcaseName /** subcasename */ ,
                bool selected /** selected */ 
            );
            /** Select or deselect a component name. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetComponentNameSelected
            (
                const NXString & componentName /** componentname */ ,
                bool selected /** selected */ 
            );
            /** Select or deselect a component name. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetComponentNameSelected
            (
                const char * componentName /** componentname */ ,
                bool selected /** selected */ 
            );
            /** Select or deselect a RPM. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetRpmSelected
            (
                double rpmValue /** rpmvalue */ ,
                bool selected /** selected */ 
            );
            /** Select or deselect an Order Cut. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetOrderCutSelected
            (
                double orderCutValue /** ordercutvalue */ ,
                bool selected /** selected */ 
            );
            /**Returns  the offset auto-compute flag 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::ModelAndLoadPreProcessInputFileBuilder::MpfOffsetStrategy MpfOffsetStrategyType
            (
            );
            /**Sets  the offset auto-compute flag 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetMpfOffsetStrategyType
            (
                NXOpen::CAE::ModelAndLoadPreProcessInputFileBuilder::MpfOffsetStrategy strategy /** strategy */ 
            );
            /**Returns  the manual offset value that is applied on processed MPFs 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: int ManualMpfOffset
            (
            );
            /**Sets  the manual offset value that is applied on processed MPFs 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetManualMpfOffset
            (
                int offset /** offset */ 
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
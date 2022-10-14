#ifndef NXOpen_CAE_POSTGRAPHBUILDER_HXX_INCLUDED
#define NXOpen_CAE_POSTGRAPHBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PostGraphBuilder.ja
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
#include <NXOpen/CAE_PostGraphBuilder.hxx>
#include <NXOpen/CAE_XyplotDataTypes.hxx>
#include <NXOpen/ugmath.hxx>
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
        class PostGraphBuilder;
    }
    class Builder;
    namespace Fields
    {
        class FieldTable;
    }
    class TaggedObject;
    namespace CAE
    {
        class _PostGraphBuilderBuilder;
        class PostGraphBuilderImpl;
        /**
                Represents a @link CAE::PostGraphBuilder CAE::PostGraphBuilder@endlink 
             <br> This is an abstract class and cannot be instantiated  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  PostGraphBuilder : public Builder
        {
            /** This option is used to when the geometric entity selected has multiple 
                        result values. This option applies to how we will resolve these multiple values into one */
            public: enum GeometryValue
            {
                GeometryValueAverage/** average */ ,
                GeometryValueMinimum/** minimum */ ,
                GeometryValueMaximum/** maximum */ ,
                GeometryValueSum/** sum */ 
            };

            /** nodal combination option for determining the nodal result value for element and element-nodal result */
            public: enum NodalCombination
            {
                NodalCombinationAverage/** average */ ,
                NodalCombinationMinimum/** minimum */ ,
                NodalCombinationMaximum/** maximum */ ,
                NodalCombinationSum/** sum */ ,
                NodalCombinationNone/** none */ 
            };

            /** error handling option when incompactible results are selected */
            public: enum IncompatibleResult
            {
                IncompatibleResultSkip/** skip */ ,
                IncompatibleResultAbort/** abort */ 
            };

            /** error handling option when result values are not present for the selected entities */
            public: enum DataErrorHandling
            {
                DataErrorHandlingSkip/** skip */ ,
                DataErrorHandlingUserValue/** User given value will used for those entities which do not have result value associated with them */
            };

            /** error handling option when there are expression evaluation errors while evaluating the formula */
            public: enum EvalutionErrors
            {
                EvalutionErrorsSkip/** skip */ ,
                EvalutionErrorsUserValue/** user value */ ,
                EvalutionErrorsAbort/** abort */ 
            };

            /** types of the entity objects which are selected */
            public: enum EntityType
            {
                EntityTypeNode/** node */ ,
                EntityTypeElement/** element */ ,
                EntityTypePoint/** point */ ,
                EntityTypeEdge/** edge */ ,
                EntityTypeFace/** face */ ,
                EntityTypeBody/** body */ 
            };

            private: PostGraphBuilderImpl * m_postgraphbuilder_impl;
            private: friend class  _PostGraphBuilderBuilder;
            protected: PostGraphBuilder();
            public: ~PostGraphBuilder();
            /**Returns  the graph title 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXString GraphTitle
            (
            );
            /**Sets  the graph title 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetGraphTitle
            (
                const NXString & graphTitle /** graphtitle */ 
            );
            /**Sets  the graph title 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetGraphTitle
            (
                const char * graphTitle /** graphtitle */ 
            );
            /**Returns   the nodal combination option for determining the nodal value for element and element-nodal results 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::PostGraphBuilder::NodalCombination NodalCombinationValue
            (
            );
            /**Sets   the nodal combination option for determining the nodal value for element and element-nodal results 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetNodalCombinationValue
            (
                NXOpen::CAE::PostGraphBuilder::NodalCombination nodalValue /** nodalvalue */ 
            );
            /**Returns  the geometry value option in case of edge, face or body selection 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::PostGraphBuilder::GeometryValue GeometryCombinationValue
            (
            );
            /**Sets  the geometry value option in case of edge, face or body selection 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetGeometryCombinationValue
            (
                NXOpen::CAE::PostGraphBuilder::GeometryValue geometryValue /** geometryvalue */ 
            );
            /**Returns  the complex plot display option while plotting complex result type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::Xyplot::ComplexOption2D ComplexGraphTypes
            (
            );
            /**Sets  the complex plot display option while plotting complex result type 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetComplexGraphTypes
            (
                NXOpen::CAE::Xyplot::ComplexOption2D complexGraphTypes /** complexgraphtypes */ 
            );
            /**Returns  the error handling option when results are not compatible on selected entities or path 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::PostGraphBuilder::IncompatibleResult IncompatibleResultOption
            (
            );
            /**Sets  the error handling option when results are not compatible on selected entities or path 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetIncompatibleResultOption
            (
                NXOpen::CAE::PostGraphBuilder::IncompatibleResult incompatibleResult /** incompatibleresult */ 
            );
            /**Returns  the error handling option when there are evaluation errors on selected entities or path 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::PostGraphBuilder::EvalutionErrors EvalutionErrorsOption
            (
            );
            /**Sets  the error handling option when there are evaluation errors on selected entities or path 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetEvalutionErrorsOption
            (
                NXOpen::CAE::PostGraphBuilder::EvalutionErrors evalutionErrorsOption /** evalutionerrorsoption */ 
            );
            /**Returns  the entity type of the tags of entities which passed using SetEntityObjects function 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::PostGraphBuilder::EntityType SelectedEntityType
            (
            );
            /**Sets  the entity type of the tags of entities which passed using SetEntityObjects function 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetSelectedEntityType
            (
                NXOpen::CAE::PostGraphBuilder::EntityType geometryEntity /** geometryentity */ 
            );
            /**Returns  the error handling option when result is not present on selected entities or path 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::PostGraphBuilder::DataErrorHandling NoDataOption
            (
            );
            /**Sets  the error handling option when result is not present on selected entities or path 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetNoDataOption
            (
                NXOpen::CAE::PostGraphBuilder::DataErrorHandling noDataOption /** nodataoption */ 
            );
            /**Returns  the error handling value used when error occurs or no data present on entities 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: double UserData
            (
            );
            /**Sets  the error handling value used when error occurs or no data present on entities 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetUserData
            (
                double userDataOption /** userdataoption */ 
            );
            /** Set entity ids for extracting result data 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetEntityIds
            (
                bool isnodal /** isnodal */ ,
                const std::vector<int> & entityIds /** entityids */ 
            );
            /** Set free points for extracting data 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetFreePoints
            (
                const std::vector<NXOpen::Point3d> & freePoints /** freepoints */ 
            );
            /** Sets the entity objects for extracting result data. Objects passed to this method 
                        are of the type defined by @link CAE::PostGraphBuilder::SelectedEntityType CAE::PostGraphBuilder::SelectedEntityType@endlink .
                        The types of objects allowed to be set are is defined by the
                        @link CAE::PostGraphBuilder::EntityType CAE::PostGraphBuilder::EntityType@endlink .
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetEntityObjects
            (
                const std::vector<NXOpen::TaggedObject *> & entityObjs /** entityobjs */ 
            );
            /**Returns  the option to create field of the across iteration graph created by expression 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: bool CreateFieldOption
            (
            );
            /**Sets  the option to create field of the across iteration graph created by expression 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetCreateFieldOption
            (
                bool createField /** createfield */ 
            );
            /**Returns  the save in AFU option to save graph data as AFU records 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: bool SaveAfuOption
            (
            );
            /**Sets  the save in AFU option to save graph data as AFU records 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetSaveAfuOption
            (
                bool saveAFU /** saveafu */ 
            );
            /** Gets the field which is created when user sets the 
                        @link CAE::PostGraphBuilder::CreateFieldOption CAE::PostGraphBuilder::CreateFieldOption @endlink and @link CAE::PostGraphBuilder::SetCreateFieldOption CAE::PostGraphBuilder::SetCreateFieldOption @endlink  
                        to true for across iterations type of graphs  @return  field 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::Fields::FieldTable * GetFieldTable
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
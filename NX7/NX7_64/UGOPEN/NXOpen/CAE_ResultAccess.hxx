#ifndef NXOpen_CAE_RESULTACCESS_HXX_INCLUDED
#define NXOpen_CAE_RESULTACCESS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResultAccess.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/CAE_Result.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class ResultAccess;
    }
    namespace CAE
    {
        class Result;
    }
    namespace CAE
    {
        class ResultParameters;
    }
    namespace CAE
    {
        class _ResultAccessBuilder;
        /** Represents a specific result state for a given @link CAE::Result CAE::Result@endlink . 
                <br/>The result state is defined by @link CAE::ResultParameters CAE::ResultParameters@endlink 
                <br/>Use @link CAE::ResultManager CAE::ResultManager@endlink  to create an @link CAE::ResultAccess CAE::ResultAccess@endlink .
                
                <br/>The unit of result value can be accessed using @link CAE::ResultParameters::GetUnit CAE::ResultParameters::GetUnit@endlink 
             <br> An instance of this class can not be obtained <br> */
        class NXOPENCPPEXPORT ResultAccess : public TaggedObject
        {
            private: friend class  _ResultAccessBuilder;
            protected: ResultAccess();
            /**  Returns the @link CAE::Result CAE::Result@endlink  which defines this result Access object
                         The @link CAE::Result CAE::Result@endlink  can be queried in order to set result state in
                         @link CAE::ResultParameters CAE::ResultParameters@endlink  
                      @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::Result * GetResult
            (
            );
            /**  Returns the @link CAE::ResultParameters CAE::ResultParameters@endlink  which defines the current result state.
                          <br/>The @link CAE::ResultParameters CAE::ResultParameters@endlink  can be modified but these changes will only take 
                          affect after @link CAE::ResultAccess::SetParameters CAE::ResultAccess::SetParameters@endlink  is called.  @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::ResultParameters * GetParameters
            (
            );
            /** Sets@link CAE::ResultParameters CAE::ResultParameters@endlink . This will validate any inappropiate settings.
                    If the input is not valid it will revert back to previous settings  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetParameters
            (
                NXOpen::CAE::ResultParameters * resultParameters /** result parameters */ 
            );
            /** Ask minimum value of current result state defined by @link CAE::ResultParameters CAE::ResultParameters@endlink  @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: double AskMinimum
            (
            );
            /** Ask maximum value of current result state defined by @link CAE::ResultParameters CAE::ResultParameters@endlink  @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: double AskMaximum
            (
            );
            /** Ask for the N extreme Min and Max values and the location of current result state defined by @link CAE::ResultParameters CAE::ResultParameters@endlink .
                        @link CAE::Result::Location CAE::Result::Location@endlink  will return where the result is defined. 
                        If it is an element-nodal result subIDs will be filled with node index and IDs will contain
                        element index. For all other cases subIDs will be 0.  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void AskNMinMaxLocation
            (
                int numExtreme /** numextreme */ ,
                NXOpen::CAE::Result::Location* location /** location */ ,
                std::vector<double> & min /** min */ ,
                std::vector<double> & max /** max */ ,
                std::vector<int> & minID /** minid */ ,
                std::vector<int> & minSubID /** minsubid */ ,
                std::vector<int> & maxID /** maxid */ ,
                std::vector<int> & maxSubID /** maxsubid */ 
            );
            /** Ask Min and Max value of current result state defined by @link CAE::ResultParameters CAE::ResultParameters@endlink 
                        If the @link CAE::Result::Location CAE::Result::Location@endlink   is nodal or elemental then ID will be node and element respectively.
                        If it is an element-nodal result then subIDs will be node at which extreme value happens.  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void AskMinMaxLocation
            (
                NXOpen::CAE::Result::Location* location /** location */ ,
                double* min /** min */ ,
                double* max /** max */ ,
                int* minID /** minid */ ,
                int* maxID /** maxid */ ,
                int* minSubID /** minsubid */ ,
                int* maxSubID /** maxsubid */ 
            );
            /** Ask current component value at a specified node index @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: double AskNodalResult
            (
                int nodeIndex /** nodeindex */ 
            );
            /** Ask all component values at a specified node index
                        Use @link CAE::ResultAccess::AskResultComponents CAE::ResultAccess::AskResultComponents@endlink  to query type of components <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void AskNodalResultAllComponents
            (
                int nodeIndex /** nodeindex */ ,
                std::vector<double> & value /** value */ 
            );
            /** Ask current component value at a specified element index. @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: double AskElementResult
            (
                int elementIndex /** elementindex */ 
            );
            /** Ask all component values at a specified element index
                        Use @link CAE::ResultAccess::AskResultComponents CAE::ResultAccess::AskResultComponents@endlink  to query type of components <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void AskElementResultAllComponents
            (
                int elementIndex /** elementindex */ ,
                std::vector<double> & value /** value */ 
            );
            /** Ask element nodal result at a specified element index <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void AskElementNodalResult
            (
                int elementIndex /** elementindex */ ,
                std::vector<int> & nodeLabels /** index of nodes that forms the element */,
                std::vector<double> & value /** Values at each node */
            );
            /** Ask element nodal result at a specified element index 
                        Use @link CAE::ResultAccess::AskResultComponents CAE::ResultAccess::AskResultComponents@endlink  to query type of components
                        All values will be returned as a single dimensional array. The array can be addressed
                        as index = node_index*numComponents +  component_index
                     <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void AskElementNodalResultAllComponents
            (
                int elementIndex /** elementindex */ ,
                std::vector<int> & nodeIndex /** nodeindex */ ,
                int* numComponents /** numcomponents */ ,
                std::vector<double> & value /** the array size will be  numComponents x totalNodes */
            );
            /** Ask current component value at a specified location. Only Nodal and Element nodal
                        result will return valid value. If point lies outside model boundary, exception will be thrown.
                        The result value will be interpolated at the given location
                     @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: double AskResultAtLocation
            (
                const NXOpen::Point3d & location /** location */ 
            );
            /** Ask all component values at a specified position. Only Nodal and Element nodal
                        result will return valid value. If point lies outside model boundary, exception will be thrown
                        Use @link CAE::ResultAccess::AskResultComponents CAE::ResultAccess::AskResultComponents@endlink  to query type of components.
                        The result value will be interpolated at the given location
                     <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void AskResultAtLocationAllComponents
            (
                const NXOpen::Point3d & position /** position */ ,
                std::vector<double> & value /** value */ 
            );
            /** Returns the result type for the current result state defined by @link CAE::ResultParameters CAE::ResultParameters@endlink    @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::Result::DataType AskCurrentResultDataType
            (
            );
            /** Return all results components for the current result state defined by @link CAE::ResultParameters CAE::ResultParameters@endlink      @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: std::vector<NXString> AskResultComponents
            (
                std::vector<NXOpen::CAE::Result::Component> & components /** components */ 
            );
            /** Is result fully averaged @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: bool IsFullyAveraged
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
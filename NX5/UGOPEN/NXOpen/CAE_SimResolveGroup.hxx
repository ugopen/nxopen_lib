#ifndef NXOpen_CAE_SIMRESOLVEGROUP_HXX_INCLUDED
#define NXOpen_CAE_SIMRESOLVEGROUP_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SimResolveGroup.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class SimResolveGroup;
    }
    namespace CAE
    {
        class SimResolveObject;
    }
    namespace CAE
    {
        class SimSolution;
    }
    namespace CAE
    {
        class SimSolutionStep;
    }
    class NXObject;
    namespace CAE
    {
        class _SimResolveGroupBuilder;
        /**  @brief  Represents BC Resolve Group object  

          */
        class NXOPENCPPEXPORT SimResolveGroup : public NXObject
        {
            /** The different resolve group types
                      */
            public: enum BcType
            {
                BcTypeLoad/** Resolve group is for conflicting BC Loads */,
                BcTypeConstraint/** Resolve group is for conflicting BC Constraints */,
                BcTypeSimulationObject/** Resolve group is for conflicting BC Simulation objects */,
                BcTypeMax/** Count of bc types */
            };

            private: friend class  _SimResolveGroupBuilder;
            protected: SimResolveGroup();
            /**Returns  the type of the resolve group  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::SimResolveGroup::BcType Type
            (
            );
            /** Returns the parent solution if it is a child of a solution, else null  @return  parent solution  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::SimSolution * GetParentSolution
            (
            );
            /** Returns the parent solution step if it is a child of a solution step , else null  @return  parent solution step  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::SimSolutionStep * GetParentStep
            (
            );
            /** Returns the count of resolve objects in the resolve group  @return  count of resolve objects  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: int GetResolveObjectCount
            (
            );
            /** Returns the resolve object by index in the resolve group  @return  resolve object for the index passed  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::SimResolveObject * GetResolveObjectByIndex
            (
                int resolve_object_index /** index of the resolve object asked for */
            );
            /** Returns the resolve objects in the resolve group  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void GetResolveObjects
            (
                std::vector<NXOpen::CAE::SimResolveObject *> & resolve_objects /** array of resolve objects */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif

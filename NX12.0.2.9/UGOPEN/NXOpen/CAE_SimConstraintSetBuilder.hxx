#ifndef NXOpen_CAE_SIMCONSTRAINTSETBUILDER_HXX_INCLUDED
#define NXOpen_CAE_SIMCONSTRAINTSETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SimConstraintSetBuilder.ja
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
        class SimConstraintSetBuilder;
    }
    class Builder;
    namespace CAE
    {
        class PropertyTable;
    }
    namespace CAE
    {
        class _SimConstraintSetBuilderBuilder;
        class SimConstraintSetBuilderImpl;
        /** Represents a @link CAE::SimConstraintSetBuilder CAE::SimConstraintSetBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::CAE::SimSimulation::CreateConstraintSetBuilder  NXOpen::CAE::SimSimulation::CreateConstraintSetBuilder @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  SimConstraintSetBuilder : public NXOpen::Builder
        {
            private: SimConstraintSetBuilderImpl * m_simconstraintsetbuilder_impl;
            private: friend class  _SimConstraintSetBuilderBuilder;
            protected: SimConstraintSetBuilder();
            public: ~SimConstraintSetBuilder();
            /**Returns  the name of the constraint set descriptor 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXString DescriptorName
            (
            );
            /**Returns  the constraint set's property table 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::PropertyTable * PropertyTable
            (
            );
            /**Returns  the label of constraint set 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: int Label
            (
            );
            /**Sets  the label of constraint set 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLabel
            (
                int constraintSetLabel /** constraintsetlabel */ 
            );
            /**Returns  the name of constraint set 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name of constraint set 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void SetName
            (
                const NXString & constraintSetName /** constraintsetname */ 
            );
            /**Sets  the name of constraint set 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            void SetName
            (
                const char * constraintSetName /** constraintsetname */ 
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

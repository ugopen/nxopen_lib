#ifndef NXOpen_CAE_RESULTVARIABLE_HXX_INCLUDED
#define NXOpen_CAE_RESULTVARIABLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResultVariable.ja
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
#include <NXOpen/CAE_Result.hxx>
#include <NXOpen/CAE_ResultVariable.hxx>
#include <NXOpen/Fields_NameVariable.hxx>
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
        class ResultVariable;
    }
    class CoordinateSystem;
    namespace Fields
    {
        class NameVariable;
    }
    namespace CAE
    {
        class _ResultVariableBuilder;
        class ResultVariableImpl;
        /**  @brief  Controls Result Exp Object.  

          <br> To obtain an instance of this class use CAE::ResultManager  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ResultVariable : public NXOpen::Fields::NameVariable
        {
            /** Element Nodal Combination Options */
            public: enum NodalCombination
            {
                NodalCombinationNone/** none */ ,
                NodalCombinationNodal/** nodal */ ,
                NodalCombinationElemental/** elemental */ 
            };

            private: ResultVariableImpl * m_resultvariable_impl;
            private: friend class  _ResultVariableBuilder;
            protected: ResultVariable();
            public: ~ResultVariable();
            /**Returns  the Quantity
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::Result::Quantity Quan
            (
            );
            /**Sets  the Quantity
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetQuan
            (
                NXOpen::CAE::Result::Quantity quan /** quan */ 
            );
            /**Returns  the Location
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::Result::Location Loc
            (
            );
            /**Sets  the Location
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetLoc
            (
                NXOpen::CAE::Result::Location loc /** loc */ 
            );
            /**Returns  the Component
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::Result::Component Comp
            (
            );
            /**Sets  the Component
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetComp
            (
                NXOpen::CAE::Result::Component loc /** loc */ 
            );
            /**Sets  the shell section
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetShellSect
            (
                NXOpen::CAE::Result::Section sect /** sect */ 
            );
            /**Returns  the shell section
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::Result::Section ShellSect
            (
            );
            /**Sets  the beam section
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetBeamSect
            (
                NXOpen::CAE::Result::Section beamSect /** beam sect */ 
            );
            /**Returns  the beam section
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::Result::Section BeamSect
            (
            );
            /**Sets  the ply ID
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetPlyid
            (
                int plyid /** plyid */ 
            );
            /**Returns  the ply ID
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: int Plyid
            (
            );
            /**Sets  the layer
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetLayer
            (
                int layer /** layer */ 
            );
            /**Returns  the layer
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: int Layer
            (
            );
            /**Sets  the Derive beam results
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetDerivebeamres
            (
                bool derivebeamres /** derivebeamres */ 
            );
            /**Returns  the Derive beam results
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: bool Derivebeamres
            (
            );
            /**Sets  the Beam fillets
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetAddfillets
            (
                bool addfillets /** addfillets */ 
            );
            /**Returns  the Beam fillets
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: bool Addfillets
            (
            );
            /**Sets  the Fillet radius scale factor
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetFilletradscale
            (
                double filletradscale /** filletradscale */ 
            );
            /**Returns  the Fillet radius scale factor
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: double Filletradscale
            (
            );
            /**Sets  the Nodal Combination 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetNodalcombinetype
            (
                NXOpen::CAE::ResultVariable::NodalCombination computetype /** computetype */ 
            );
            /**Returns  the Nodal Combination 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::ResultVariable::NodalCombination Nodalcombinetype
            (
            );
            /**Sets  the MIDs
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetMids
            (
                bool mids /** mids */ 
            );
            /**Returns  the MIDs
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: bool Mids
            (
            );
            /**Sets  the PIDs
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetPids
            (
                bool mids /** mids */ 
            );
            /**Returns  the PIDs
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: bool Pids
            (
            );
            /**Sets  the Element types
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetElemtypes
            (
                bool elemtypes /** elemtypes */ 
            );
            /**Returns  the Element types
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: bool Elemtypes
            (
            );
            /**Sets  the Complex type
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetComplex
            (
                NXOpen::CAE::Result::Complex complex /** complex */ 
            );
            /**Returns  the Complex type
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::Result::Complex Complex
            (
            );
            /**Sets  the Phase angle
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetPhase
            (
                double phase /** phase */ 
            );
            /**Returns  the Phase angle
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: double Phase
            (
            );
            /**Sets  the Co-ordinate System
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetCsys
            (
                NXOpen::CAE::Result::CoordinateSystem csys /** csys */ 
            );
            /**Returns  the Co-ordinate System
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::Result::CoordinateSystem Csys
            (
            );
            /**Sets  the Selected Co-ordinate System
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetSelectedcsys
            (
                NXOpen::CoordinateSystem * selectedcsys /** selectedcsys */ 
            );
            /**Returns  the Selected Co-ordinate System
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CoordinateSystem * Selectedcsys
            (
            );
            /**Sets  the Absolute value from result
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetAbs
            (
                bool abs /** abs */ 
            );
            /**Returns  the Absolute value from result
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: bool Abs
            (
            );
            /**Returns  the Result Field Expression Name
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXString Expname
            (
            );
            /**Sets  the elemental result criteria
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetElementcriteria
            (
                NXOpen::CAE::Result::ElementValueCriterion criteria /** criteria */ 
            );
            /**Returns  the elemental result criteria
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::Result::ElementValueCriterion Elementcriteria
            (
            );
            /** Re-Name Result Variable 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void Rename
            (
                const NXString & expname /** expname */ 
            );
            /** Re-Name Result Variable 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void Rename
            (
                const char * expname /** expname */ 
            );
            /**Sets  the Result type username
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetUsertypename
            (
                const NXString & usertypename /** usertypename */ 
            );
            /**Sets  the Result type username
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetUsertypename
            (
                const char * usertypename /** usertypename */ 
            );
            /**Returns  the Result type username
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXString Usertypename
            (
            );
            /**Sets  the ply ID
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetNumberofcomponent
            (
                int numcomponent /** numcomponent */ 
            );
            /**Returns  the ply ID
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: int Numberofcomponent
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
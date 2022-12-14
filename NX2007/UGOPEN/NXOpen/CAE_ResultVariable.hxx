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
#include <NXOpen/CAE_SignalProcessingPlotData.hxx>
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

            /** Complex Options */
            public: enum ComplexType
            {
                ComplexTypeReal/** real */ ,
                ComplexTypeImaginary/** imaginary */ ,
                ComplexTypeAmplitude/** amplitude */ ,
                ComplexTypeSignedAmplitude/** signed amplitude */ ,
                ComplexTypePhaseAngle/** phase angle */ ,
                ComplexTypeRealImaginary/** real imaginary */ 
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
             <br>  @deprecated Deprecated in NX2007.0.0.  Use @link NXOpen::CAE::ResultVariable::SetShellSection NXOpen::CAE::ResultVariable::SetShellSection@endlink  instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX2007.0.0.  Use NXOpen::CAE::ResultVariable::SetShellSection instead.") void SetShellSect
            (
                NXOpen::CAE::Result::Section sect /** sect */ 
            );
            /**Returns  the shell section
             <br>  @deprecated Deprecated in NX2007.0.0.  Use NXOpen.CAE.ResultVariable.GetShellSection instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX2007.0.0.  Use NXOpen.CAE.ResultVariable.GetShellSection instead.") NXOpen::CAE::Result::Section ShellSect
            (
            );
            /**Sets  the shell section
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetShellSection
            (
                NXOpen::CAE::Result::ShellSection section /** section */ 
            );
            /**Returns  the shell section
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::Result::ShellSection ShellSection
            (
            );
            /**Sets  the beam section
             <br>  @deprecated Deprecated in NX2007.0.0.  Use <jamethod>NXOpen.CAE.ResultVariable.SetBeamSection</jamethod> instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX2007.0.0.  Use <jamethod>NXOpen.CAE.ResultVariable.SetBeamSection</jamethod> instead.") void SetBeamSect
            (
                NXOpen::CAE::Result::Section beamSect /** beam sect */ 
            );
            /**Returns  the beam section
             <br>  @deprecated Deprecated in NX2007.0.0.  Use NXOpen.CAE.ResultVariable.GetBeamSection instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX2007.0.0.  Use NXOpen.CAE.ResultVariable.GetBeamSection instead.") NXOpen::CAE::Result::Section BeamSect
            (
            );
            /**Sets  the beam section
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetBeamSection
            (
                NXOpen::CAE::Result::BeamSection section /** section */ 
            );
            /**Returns  the beam section
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::Result::BeamSection BeamSection
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
                NXOpen::CAE::ResultVariable::NodalCombination combinetype /** combinetype */ 
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
             <br>  @deprecated Deprecated in NX1872.0.0.  Use @link NXOpen::CAE::ResultVariable::SetComplexopt NXOpen::CAE::ResultVariable::SetComplexopt@endlink  instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX1872.0.0.  Use NXOpen::CAE::ResultVariable::SetComplexopt instead.") void SetComplex
            (
                NXOpen::CAE::Result::Complex complex /** complex */ 
            );
            /**Returns  the Complex type
             <br>  @deprecated Deprecated in NX1872.0.0.  Use NXOpen.CAE.ResultVariable.GetComplexopt instead. <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NX_DEPRECATED("Deprecated in NX1872.0.0.  Use NXOpen.CAE.ResultVariable.GetComplexopt instead.") NXOpen::CAE::Result::Complex Complex
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
            /**Sets  the Include Internal Elements which doing nodal averaging
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetIncludeInternalElement
            (
                bool includeinternalelem /** includeinternalelem */ 
            );
            /**Returns  the Include Internal Elements which doing nodal averaging
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: bool IncludeInternalElement
            (
            );
            /**Sets  the Nodal Combination 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetComputetype
            (
                NXOpen::CAE::Result::ComputationType computetype /** computetype */ 
            );
            /**Returns  the Nodal Combination 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::Result::ComputationType Computetype
            (
            );
            /**Sets  the Acoustic Environment Spectrum Scaling. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetSpectrumScaling
            (
                NXOpen::CAE::SignalProcessingPlotData::ScalingType specScaling /** spec scaling */ 
            );
            /**Returns  the Acoustic Environment Spectrum Scaling. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::SignalProcessingPlotData::ScalingType SpectrumScaling
            (
            );
            /**Sets  the Acoustic Environment Weighting. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetAcousticWeighting
            (
                NXOpen::CAE::SignalProcessingPlotData::AcousticalWeighting weight /** weight */ 
            );
            /**Returns  the Acoustic Environment Weighting. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::SignalProcessingPlotData::AcousticalWeighting AcousticWeighting
            (
            );
            /**Sets  the  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetProjectOnNodeNormal
            (
                bool projectOnNodeNormal /** projectonnodenormal */ 
            );
            /**Returns  the  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: bool ProjectOnNodeNormal
            (
            );
            /**Returns  the complex type for result variable
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::ResultVariable::ComplexType Complexopt
            (
            );
            /**Sets  the complex type for result variable
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetComplexopt
            (
                NXOpen::CAE::ResultVariable::ComplexType complex /** complex */ 
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

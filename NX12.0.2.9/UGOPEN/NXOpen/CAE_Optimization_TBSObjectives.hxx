#ifndef NXOpen_CAE_OPTIMIZATION_TBSOBJECTIVES_HXX_INCLUDED
#define NXOpen_CAE_OPTIMIZATION_TBSOBJECTIVES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Optimization_TBSObjectives.ja
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
#include <NXOpen/CAE_Optimization_TBSSingleObjective.hxx>
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
        namespace Optimization
        {
            class TBSObjectives;
        }
    }
    namespace CAE
    {
        namespace Optimization
        {
            class TBSSingleObjective;
        }
    }
    namespace CAE
    {
        namespace Optimization
        {
            class _TBSObjectivesBuilder;
            class TBSObjectivesImpl;
            /** Represents the objective functions of an optimization 
             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  TBSObjectives : public NXOpen::TaggedObject
            {
                /** Defines the target type of the design objective */
                public: enum ObjectiveType
                {
                    ObjectiveTypeMinimum/** Target is to minimize the list of design response */,
                    ObjectiveTypeMaximum/** Target is to maximize the list of design response */,
                    ObjectiveTypeMaxMin/** Target is the MINMAX formulation of the list of design responses */
                };

                private: TBSObjectivesImpl * m_tbsobjectives_impl;
                private: friend class  _TBSObjectivesBuilder;
                protected: TBSObjectives();
                public: ~TBSObjectives();
                /**Returns  the target objective type 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Optimization::TBSObjectives::ObjectiveType TargetObjective
                (
                );
                /**Sets  the target objective type 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization") */
                public: void SetTargetObjective
                (
                    NXOpen::CAE::Optimization::TBSObjectives::ObjectiveType target /** target */ 
                );
                /** Returns the design response  @return  
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: std::vector<NXOpen::CAE::Optimization::TBSSingleObjective *> GetObjectives
                (
                );
                /** Sets the design response 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization") */
                public: void SetObjectives
                (
                    const std::vector<NXOpen::CAE::Optimization::TBSSingleObjective *> & objectives /** objectives */ 
                );
                /** Add objectives 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization") */
                public: void AddObjectives
                (
                    const std::vector<NXOpen::CAE::Optimization::TBSSingleObjective *> & objectives /** objectives */ 
                );
                /** Remove objectives 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization") */
                public: void RemoveObjectives
                (
                    const std::vector<NXOpen::CAE::Optimization::TBSSingleObjective *> & objectives /** objectives */ ,
                    bool deleteObject /** deleteobject */ 
                );
            };
        }
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

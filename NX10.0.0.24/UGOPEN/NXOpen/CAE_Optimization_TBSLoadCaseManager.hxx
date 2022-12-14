#ifndef NXOpen_CAE_OPTIMIZATION_TBSLOADCASEMANAGER_HXX_INCLUDED
#define NXOpen_CAE_OPTIMIZATION_TBSLOADCASEMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Optimization_TBSLoadCaseManager.ja
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
#include <NXOpen/CAE_Optimization_TBSLoadCase.hxx>
#include <NXOpen/CAE_Optimization_TBSLoadCaseManager.hxx>
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
            class TBSLoadCaseManager;
        }
    }
    namespace CAE
    {
        namespace Optimization
        {
            class TBSLoadCase;
        }
    }
    namespace CAE
    {
        namespace Optimization
        {
            class _TBSLoadCaseManagerBuilder;
            class TBSLoadCaseManagerImpl;
            /** Managers load cases
             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  TBSLoadCaseManager : public NXOpen::TaggedObject
            {
                /** Defines the selection of the loadcase */
                public: enum SelectionType
                {
                    SelectionTypeMaximum/** Maximum value of the selected load cases */,
                    SelectionTypeMinimum/** Minimum value of the selected load cases */,
                    SelectionTypeSum/** Sum of the selected load cases */
                };

                private: TBSLoadCaseManagerImpl * m_tbsloadcasemanager_impl;
                private: friend class  _TBSLoadCaseManagerBuilder;
                protected: TBSLoadCaseManager();
                public: ~TBSLoadCaseManager();
                /**Returns  the selection option 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Optimization::TBSLoadCaseManager::SelectionType SelectionOption
                (
                );
                /**Sets  the selection option 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization") */
                public: void SetSelectionOption
                (
                    NXOpen::CAE::Optimization::TBSLoadCaseManager::SelectionType selectionOption /** selectionoption */ 
                );
                /** Returns the load cases  @return  
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: std::vector<NXOpen::CAE::Optimization::TBSLoadCase *> GetLoadCases
                (
                );
                /** Sets the load cases 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization") */
                public: void SetLoadCases
                (
                    const std::vector<NXOpen::CAE::Optimization::TBSLoadCase *> & loadCases /** loadcases */ 
                );
                /** Adds the load cases 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization") */
                public: void AddLoadCases
                (
                    const std::vector<NXOpen::CAE::Optimization::TBSLoadCase *> & loadCases /** loadcases */ 
                );
                /** Removes the load cases 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : cae_opt_topo ("NX Topology Optimization") OR cae_opt_topobead ("NX Bead Optimization") OR cae_opt_toposhape ("NX Shape Optimization") */
                public: void RemoveLoadCases
                (
                    const std::vector<NXOpen::CAE::Optimization::TBSLoadCase *> & loadCases /** loadcases */ ,
                    bool deleteLoadCase /** deleteloadcase */ 
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

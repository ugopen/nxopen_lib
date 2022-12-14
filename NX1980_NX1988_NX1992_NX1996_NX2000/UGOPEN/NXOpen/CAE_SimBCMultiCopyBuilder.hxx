#ifndef NXOpen_CAE_SIMBCMULTICOPYBUILDER_HXX_INCLUDED
#define NXOpen_CAE_SIMBCMULTICOPYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SimBCMultiCopyBuilder.ja
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
#include <NXOpen/CAE_SimLbcFolder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class SimBCMultiCopyBuilder;
    }
    class Builder;
    namespace CAE
    {
        class SelectSimBCList;
    }
    namespace CAE
    {
        class SimLbcFolder;
    }
    namespace CAE
    {
        class _SimBCMultiCopyBuilderBuilder;
        class SimBCMultiCopyBuilderImpl;
        /** Represents a @link CAE::SimBCMultiCopyBuilder CAE::SimBCMultiCopyBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::CAE::SimSimulation::CreateBcMultiCopyBuilder  NXOpen::CAE::SimSimulation::CreateBcMultiCopyBuilder @endlink  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  SimBCMultiCopyBuilder : public NXOpen::Builder
        {
            /** Copy destination type */
            public: enum Destination
            {
                DestinationSameAsOriginal/** copy will be placed in same folder */,
                DestinationRoot/** copy will be placed in ROOT folder */,
                DestinationSpecify/** copy will be placed in specified folder */
            };

            private: SimBCMultiCopyBuilderImpl * m_simbcmulticopybuilder_impl;
            private: friend class  _SimBCMultiCopyBuilderBuilder;
            protected: SimBCMultiCopyBuilder();
            public: ~SimBCMultiCopyBuilder();
            /**Returns  the list of BCs to be multi-copied 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::SelectSimBCList * Selection
            (
            );
            /** Add copy parameters set 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void AddCopySet
            (
                const NXString & prefix /** string to prefix to copy names */,
                const NXString & suffix /** string to postfix to copy names */,
                NXOpen::CAE::SimBCMultiCopyBuilder::Destination destination /** destination to place the created copies */,
                NXOpen::CAE::SimLbcFolder * folder /** Folder for copies when destination type is Specify */,
                bool retainAssociation /** Retain associations from source in copies */
            );
            /** Add copy parameters set 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void AddCopySet
            (
                const char * prefix /** string to prefix to copy names */,
                const char * suffix /** string to postfix to copy names */,
                NXOpen::CAE::SimBCMultiCopyBuilder::Destination destination /** destination to place the created copies */,
                NXOpen::CAE::SimLbcFolder * folder /** Folder for copies when destination type is Specify */,
                bool retainAssociation /** Retain associations from source in copies */
            );
            /** Edit Nth copy parameters set. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void EditCopySet
            (
                int index /** index of parameter set to edit */,
                const NXString & prefix /** string to prefix to copy names */,
                const NXString & suffix /** string to postfix to copy names */,
                NXOpen::CAE::SimBCMultiCopyBuilder::Destination destination /** destination to place the created copies */,
                NXOpen::CAE::SimLbcFolder * folder /** Folder for copies when destination type is Specify */,
                bool retainAssociation /** Retain associations from source in copies */
            );
            /** Edit Nth copy parameters set. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void EditCopySet
            (
                int index /** index of parameter set to edit */,
                const char * prefix /** string to prefix to copy names */,
                const char * suffix /** string to postfix to copy names */,
                NXOpen::CAE::SimBCMultiCopyBuilder::Destination destination /** destination to place the created copies */,
                NXOpen::CAE::SimLbcFolder * folder /** Folder for copies when destination type is Specify */,
                bool retainAssociation /** Retain associations from source in copies */
            );
            /** Remove copy parameters set.  If the prefix/suffix combination does not exist, will do nothing 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void RemoveCopySet
            (
                int index /** index of parameter set to remove */
            );
            /** Remove copy parameters set.  If the prefix/suffix combination does not exist, will do nothing 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void DeleteAllCopySets
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

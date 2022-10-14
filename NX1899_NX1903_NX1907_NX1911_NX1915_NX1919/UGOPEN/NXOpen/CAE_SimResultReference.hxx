#ifndef NXOpen_CAE_SIMRESULTREFERENCE_HXX_INCLUDED
#define NXOpen_CAE_SIMRESULTREFERENCE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SimResultReference.ja
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
#include <NXOpen/CAE_IPostScenarioDataSource.hxx>
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
        class SimResultReference;
    }
    namespace CAE
    {
        class CompanionResultCollection;
    }
    namespace CAE
    {
        class IPostScenarioDataSource;
    }
    class TaggedObject;
    class Unit;
    namespace CAE
    {
        class _SimResultReferenceBuilder;
        class SimResultReferenceImpl;
        /** Represents a Result Reference in the .sim files.

                For more information, refer to the Solver language documentation in the 
                <a href="../opencae/Solvers.html"> SolverLanguageDocumentation</a>. 

             <br> This class is not created directly by the user.  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  SimResultReference : public NXOpen::TaggedObject, public virtual NXOpen::CAE::IPostScenarioDataSource
        {
            /** Result Types */
            public: enum Type
            {
                TypeStructural/** structural result          */,
                TypeThermal/** thermal result             */,
                TypeFlow/** flow result                */,
                TypeMagnetics/** magnetics result           */,
                TypeAcoustic/** acoustic  result           */,
                TypeVibroAcoustic/** vibration acoustic  result */
            };

            private: SimResultReferenceImpl * m_simresultreference_impl;
            private: friend class  _SimResultReferenceBuilder;
            protected: SimResultReference();
            public: ~SimResultReference();
            /** Returns the children of the Solution of the given Identifier  @return  
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::TaggedObject * Find
            (
                const NXString & journalIdentifier /** Journal identifier of the object */
            );
            /** Returns the children of the Solution of the given Identifier  @return  
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::TaggedObject * Find
            (
                const char * journalIdentifier /** Journal identifier of the object */
            );
            /** Specify local result file 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetLocalResultFile
            (
                const NXString & dirpath /** directory name */,
                const NXString & filename /** file name */
            );
            /** Specify local result file 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetLocalResultFile
            (
                const char * dirpath /** directory name */,
                const char * filename /** file name */
            );
            /** Specify managed result file 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetManagedResultFile
            (
                const NXString & file /** file name */
            );
            /** Specify managed result file 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetManagedResultFile
            (
                const char * file /** file name */
            );
            /** Clear previously specified result file location 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetInferredResultFile
            (
            );
            /** Get the result file directory and result file name 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void GetResultFile
            (
                NXString* resultfiledir /** directly path where result file is stored */,
                NXString* resfilename /** result file name */
            );
            /** Get the result file directory and result file name 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void DeleteResultFile
            (
            );
            /** Get the managed result file name  @return  managed result file name 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXString GetManagedResultFile
            (
            );
            /** Get basic 6 units which are stored with solution used for loading the result file 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void GetResultFileUnits
            (
                std::vector<NXOpen::Unit *> & units /** 6 basic units used to define the quantities in result file in order of mass, length, time, temperature, angle, and thermal energy */
            );
            /** Set result file units 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetResultFileUnits
            (
                const std::vector<NXOpen::Unit *> & units /** 6 units for mass, length, time, temperature, angle, and thermal energy */
            );
            /** Clears previously specified result file units 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetInferredResultFileUnits
            (
            );


            /** Returns the CAE Companion Results collection belonging to this Result Reference 
             <br>  Created in NX10.0.0.  <br>  
            */
            public: NXOpen::CAE::CompanionResultCollection *CompanionResults();
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
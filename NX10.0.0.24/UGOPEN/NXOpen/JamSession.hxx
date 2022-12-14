#ifndef NXOpen_JAMSESSION_HXX_INCLUDED
#define NXOpen_JAMSESSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     JamSession.ja
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
#include <NXOpen/JamTest.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopenjamtestcpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class JamSession;
    class JamNXColorManager;
    class JamTest;
    class OMSchema;
    class _JamSessionBuilder;
    class JamSessionImpl;
    /** Represents a Jam session  <br> No creator defined as this is an internal class  <br> 
     <br>  Created in NX3.0.2.  <br>  
    */
    class NXOPENJAMTESTCPPEXPORT  JamSession : public NXOpen::TaggedObject
    {
         /** Allocation statistics */
        public:
        struct  AllocationStatistics
        {
            public: /** num jam tests allocated */ int NumJamTestsAllocated;
            public: /** num jam tests deallocated */ int NumJamTestsDeallocated;
            public: AllocationStatistics() :
                NumJamTestsAllocated(),
                NumJamTestsDeallocated()
            {
            }
            /** Constructor for the AllocationStatistics struct. */ 
            public: AllocationStatistics(int numJamTestsAllocatedInitial /** num jam tests allocated */ , 
                    int numJamTestsDeallocatedInitial /** num jam tests deallocated */ ) :
                NumJamTestsAllocated(numJamTestsAllocatedInitial),
                NumJamTestsDeallocated(numJamTestsDeallocatedInitial)
            {
            }
        };

        private: JamSessionImpl * m_jamsession_impl;
        private: static JamSession *theJamSession;
        public: static JamSession *GetJamSession();
        private: friend class  _JamSessionBuilder;
        protected: JamSession();
        public: ~JamSession();
        /** Create new JamTest  @return  
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::JamTest * NewJamTest
        (
        );
        /** Get the allocation statistics  @return  
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::JamSession::AllocationStatistics GetAllocationStatistics
        (
        );
        /** Returns the schemas  @return  
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : None */
        public: std::vector<NXOpen::OMSchema *> GetOMSchemas
        (
        );
        /** Returns a schema  @return  
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::OMSchema * GetOMSchema
        (
            const NXString & name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Returns a schema  @return  
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : None */
        NXOpen::OMSchema * GetOMSchema
        (
            const char * name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );


        /** used to manage the standard NX colors 
         <br>  Created in NX3.0.0.  <br>  
        */
        public: NXOpen::JamNXColorManager *Colors();
    };
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

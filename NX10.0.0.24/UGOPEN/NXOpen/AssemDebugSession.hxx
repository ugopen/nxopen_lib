#ifndef NXOpen_ASSEMDEBUGSESSION_HXX_INCLUDED
#define NXOpen_ASSEMDEBUGSESSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AssemDebugSession.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class AssemDebugSession;
    class DebugSession;
    class BasePart;
    class Part;
    class AssemDebugSessionImpl;

    /// \cond NX_NO_DOC 
    /** Represents a class that is used for NX ASSEM Autotest.  This class should not
    be made available to customers  <br> To obtain an instance of this class, refer to @link NXOpen::DebugSession  NXOpen::DebugSession @endlink  <br> 
     <br>  Created in NX6.0.2.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  AssemDebugSession
    {
        /** Represents the Parasolid Part Event Monitor id 
            */
        public: enum ParasolidLoadStatusEventId { ParasolidLoadStatusEventIdDummyMember }; // Used as an id
        /** Represents the CM Partition Load Event Monitor id 
            */
        public: enum CmPartitionLoadStatusEventId { CmPartitionLoadStatusEventIdDummyMember }; // Used as an id
        private: AssemDebugSessionImpl * m_assemdebugsession_impl;
        private: NXOpen::DebugSession* m_owner;
        /// \cond NX_NO_DOC 
        public: explicit AssemDebugSession(NXOpen::DebugSession *owner);


        /// \endcond 
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~AssemDebugSession();
        /** Compare the input plmxml file to a master plmxml filename  
         <br>  Created in NX6.0.2.  <br>  
         <br> License requirements : None */
        public: void ComparePlmxml
        (
            const NXString & masterXmlFilename /** Recorded PLMXML file name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            const NXString & newXmlFilename /** Playback PLMXML file name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Compare the input plmxml file to a master plmxml filename  
         <br>  Created in NX6.0.2.  <br>  
         <br> License requirements : None */
        void ComparePlmxml
        (
            const char * masterXmlFilename /** Recorded PLMXML file name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            const char * newXmlFilename /** Playback PLMXML file name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Create a new plmxml file for the input part with the given name 
         <br>  Created in NX6.0.2.  <br>  
         <br> License requirements : None */
        public: void NewPlmxml
        (
            NXOpen::Part * workPart /** Part Filename */,
            const NXString & newXml /** New PLMXML filename   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Create a new plmxml file for the input part with the given name 
         <br>  Created in NX6.0.2.  <br>  
         <br> License requirements : None */
        void NewPlmxml
        (
            NXOpen::Part * workPart /** Part Filename */,
            const char * newXml /** New PLMXML filename   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Print all in-session inter-part links 
         <br>  Created in NX6.0.2.  <br>  
         <br> License requirements : None */
        public: void PrintAllIpLinksInSession
        (
        );
        /** Print information about all constraints in session 
         <br>  Created in NX6.0.3.  <br>  
         <br> License requirements : None */
        public: void PrintConstraintInformation
        (
        );
        /** Print information about all the reference set objects in the given part 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: void PrintReferenceSetsInformationOfPart
        (
            NXOpen::BasePart * basePart /** basepart */ 
        );
        /** Print the corresponding lightweight bodies for the solid bodies 
                that are displayed in the current work view 
         <br>  Created in NX7.0.0.  <br>  
         <br> License requirements : None */
        public: void PrintLightweightOfAllDisplayedBodiesInWorkView
        (
        );
        /** Print information about all the components in the given part 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: void PrintAllComponentsInPart
        (
            NXOpen::BasePart * basePart /** basepart */ 
        );
        /** Print information about all the components representation status in the given display part 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: void PrintAllComponentsRepresentationStatusInPart
        (
            NXOpen::BasePart * basePart /** basepart */ 
        );
        /** Print all referencers to in-session product interfaces 
         <br>  Created in NX7.5.1.  <br>  
         <br> License requirements : None */
        public: void PrintAllPiReferencesInSession
        (
        );
        /** Start gathering Parasolid Part Event Monitor status in the given display part  @return  Client Id for the PEM 
         <br>  Created in NX7.5.1.  <br>  
         <br> License requirements : None */
        public: NXOpen::AssemDebugSession::ParasolidLoadStatusEventId StartPrintAllParasolidLoadStatusInPart
        (
        );
        /** Stop gathering information about the Parasolid Part Event Monitor in the given display part 
         <br>  Created in NX7.5.1.  <br>  
         <br> License requirements : None */
        public: void EndPrintAllParasolidLoadStatusInPart
        (
            NXOpen::AssemDebugSession::ParasolidLoadStatusEventId clientId /** Client id for the PEM */
        );
        /** Start gathering CM Partition Part Event Monitor status in the given display part  @return  Client Id for the PEM 
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::AssemDebugSession::CmPartitionLoadStatusEventId StartPrintAllCmPartitionLoadStatusInPart
        (
        );
        /** Stop gathering information about the CM Partition Part Event Monitor in the given display part 
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: void EndPrintAllCmPartitionLoadStatusInPart
        (
            NXOpen::AssemDebugSession::CmPartitionLoadStatusEventId clientId /** Client id for the PEM */
        );
        /** Dump the CFI structured storage hierarchy for the specified part into xml. This includes both storage
                and stream data. If includeQafData is true then all the quick access folders(QAF) data will be 
                dumped as well.
            
         <br>  Created in NX7.5.2.  <br>  
         <br> License requirements : None */
        public: void PrintStructuredStorages
        (
            NXOpen::BasePart * basePart /** basepart */ ,
            bool includeQafData /** If true then include quick access folders */
        );
        /**
                Dump the component pattern data information into xml.
            
         <br>  Created in NX8.5.0.  <br>  
         <br> License requirements : None */
        public: void PrintCompPatternInformationInPart
        (
            NXOpen::BasePart * basePart /** basepart */ 
        );
        /**
                Dumps part family data in work part into xml.
            
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: void PrintPartFamilyData
        (
            NXOpen::BasePart * workPart /** workpart */ 
        );
        /**
                Process any pending Assembly Navigator updates.
            
         <br>  Created in NX10.0.0.  <br>  
         <br> License requirements : None */
        public: void ProcessAssemblyNavigatorUpdates
        (
        );
        /**
                Expand all in the Assembly Navigator.
            
         <br>  Created in NX10.0.0.  <br>  
         <br> License requirements : None */
        public: void ExpandAssemblyNavigator
        (
        );
        /**
                Expand all in the Constraint Navigator.
            
         <br>  Created in NX10.0.0.  <br>  
         <br> License requirements : None */
        public: void ExpandConstraintNavigator
        (
        );
        /**
                Dump clearance data in display part into xml.
            
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: void PrintClearanceData
        (
            NXOpen::BasePart * displayPart /** displaypart */ 
        );
        /** 
                Dump assembly order data information into xml.
            
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: void PrintAssemblyOrdersData
        (
            NXOpen::BasePart * displayPart /** displaypart */ 
        );
        /**   
                Dumb positioning task collection information into xml.   
            
         <br>  Created in NX10.0.0.  <br>  
         <br> License requirements : None */
        public: void PrintPositioningTaskInformation
        (
            NXOpen::BasePart * displayPart /** displaypart */ 
        );
    }; //lint !e1712 default constructor not defined for class  


    /// \endcond 
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
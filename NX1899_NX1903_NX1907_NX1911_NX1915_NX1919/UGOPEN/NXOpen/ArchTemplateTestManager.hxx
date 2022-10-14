#ifndef NXOpen_ARCHTEMPLATETESTMANAGER_HXX_INCLUDED
#define NXOpen_ARCHTEMPLATETESTMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ArchTemplateTestManager.ja
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
    class ArchTemplateTestManager;
    class TemplateTestManager;
    class Axis;
    namespace Features
    {
        class Feature;
    }
    class NXObject;
    class Plane;
    class Point;
    class ArchTemplateTestManagerImpl;

    /// \cond NX_NO_DOC 
    /** Represents a class that is used for autotests.  This class should not
    be made available to customers  <br> To obtain an instance of this class, refer to @link NXOpen::TemplateTestManager  NXOpen::TemplateTestManager @endlink  <br> 
     <br>  Created in NX8.0.0.  <br>  
    */
    class NXOPENDEBUGSESSIONCPPEXPORT  ArchTemplateTestManager
    {
        /** Specifies view statistics type to be performed.
              */
        public: enum StatisticsViewType
        {
            StatisticsViewTypeWorkView/** Output statistics for work view of current displayed part */,
            StatisticsViewTypeDisplayedPartViews/** Output statistics for all displayed views of current displayed part */,
            StatisticsViewTypeAllDisplayedViews/** Output statistics for all displayed views from all displayed parts */
        };

        /** Specifies tolerance type to be performed.
              */
        public: enum ToleranceType
        {
            ToleranceTypeStandard/** standard */ ,
            ToleranceTypeCustom/** custom */ 
        };

        private: ArchTemplateTestManagerImpl * m_archtemplatetestmanager_impl;
        private: NXOpen::TemplateTestManager* m_owner;
        /// \cond NX_NO_DOC 
        public: explicit ArchTemplateTestManager(NXOpen::TemplateTestManager *owner);


        /// \endcond 
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~ArchTemplateTestManager();
        /**Sample Template Test
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void RunSampleTemplateTest
        (
            const NXString & testName /** testname */ ,
            int version /** version */ ,
            const std::vector<int> & errorCodes /** errorcodes */ ,
            bool bool0 /** bool0 */ ,
            int int0 /** int0 */ ,
            double float0 /** float0 */ ,
            const std::vector<NXOpen::Features::Feature *> & features0 /** features0 */ ,
            const std::vector<NXOpen::NXObject *> & nxobjects0 /** nxobjects0 */ ,
            const NXString & strings0 /** strings0 */ 
        );
        /**Sample Template Test
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        void RunSampleTemplateTest
        (
            const char * testName /** testname */ ,
            int version /** version */ ,
            const std::vector<int> & errorCodes /** errorcodes */ ,
            bool bool0 /** bool0 */ ,
            int int0 /** int0 */ ,
            double float0 /** float0 */ ,
            const std::vector<NXOpen::Features::Feature *> & features0 /** features0 */ ,
            const std::vector<NXOpen::NXObject *> & nxobjects0 /** nxobjects0 */ ,
            const char * strings0 /** strings0 */ 
        );
        /**Add Comment
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void RunLinetest
        (
            const NXString & testName /** testname */ ,
            int version /** version */ ,
            const std::vector<int> & errorCodes /** errorcodes */ ,
            const std::vector<NXOpen::Features::Feature *> & line0 /** line0 */ 
        );
        /**Add Comment
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        void RunLinetest
        (
            const char * testName /** testname */ ,
            int version /** version */ ,
            const std::vector<int> & errorCodes /** errorcodes */ ,
            const std::vector<NXOpen::Features::Feature *> & line0 /** line0 */ 
        );
        /**Prints the number of attributes and attribute information available on the selected object
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void RunPrintObjectAttributes
        (
            const NXString & testName /** testname */ ,
            int version /** version */ ,
            const std::vector<int> & errorCodes /** errorcodes */ ,
            const std::vector<NXOpen::NXObject *> & selectobject0 /** selectobject0 */ 
        );
        /**Prints the number of attributes and attribute information available on the selected object
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        void RunPrintObjectAttributes
        (
            const char * testName /** testname */ ,
            int version /** version */ ,
            const std::vector<int> & errorCodes /** errorcodes */ ,
            const std::vector<NXOpen::NXObject *> & selectobject0 /** selectobject0 */ 
        );
        /**Add Comment
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: void RunParameterAxis
        (
            const NXString & testName /** testname */ ,
            int version /** version */ ,
            const std::vector<int> & errorCodes /** errorcodes */ ,
            const std::vector<NXOpen::Axis *> & a00 /** a00 */ ,
            const std::vector<NXOpen::Axis *> & a11 /** a11 */ 
        );
        /**Add Comment
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        void RunParameterAxis
        (
            const char * testName /** testname */ ,
            int version /** version */ ,
            const std::vector<int> & errorCodes /** errorcodes */ ,
            const std::vector<NXOpen::Axis *> & a00 /** a00 */ ,
            const std::vector<NXOpen::Axis *> & a11 /** a11 */ 
        );
        /**Add Comment
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: void RunParameterPlane
        (
            const NXString & testName /** testname */ ,
            int version /** version */ ,
            const std::vector<int> & errorCodes /** errorcodes */ ,
            const std::vector<NXOpen::Plane *> & pl00 /** pl00 */ ,
            const std::vector<NXOpen::Plane *> & pl11 /** pl11 */ 
        );
        /**Add Comment
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        void RunParameterPlane
        (
            const char * testName /** testname */ ,
            int version /** version */ ,
            const std::vector<int> & errorCodes /** errorcodes */ ,
            const std::vector<NXOpen::Plane *> & pl00 /** pl00 */ ,
            const std::vector<NXOpen::Plane *> & pl11 /** pl11 */ 
        );
        /**Add Comment
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        public: void RunParameterPoint
        (
            const NXString & testName /** testname */ ,
            int version /** version */ ,
            const std::vector<int> & errorCodes /** errorcodes */ ,
            const std::vector<NXOpen::Point *> & p10 /** p10 */ ,
            const std::vector<NXOpen::Point *> & p21 /** p21 */ 
        );
        /**Add Comment
         <br>  Created in NX9.0.0.  <br>  
         <br> License requirements : None */
        void RunParameterPoint
        (
            const char * testName /** testname */ ,
            int version /** version */ ,
            const std::vector<int> & errorCodes /** errorcodes */ ,
            const std::vector<NXOpen::Point *> & p10 /** p10 */ ,
            const std::vector<NXOpen::Point *> & p21 /** p21 */ 
        );
        /** Tests visualization statistics 
         <br>  Created in NX12.0.2.  <br>  
         <br> License requirements : None */
        public: void RunVisualizationStatistics
        (
            const NXString & testName /** testname */ ,
            int version /** version */ ,
            const std::vector<int> & errorCodes /** errorcodes */ ,
            NXOpen::ArchTemplateTestManager::StatisticsViewType statisticsViewType /** statisticsviewtype */ ,
            NXOpen::ArchTemplateTestManager::ToleranceType toleranceType /** tolerancetype */ ,
            double tolerance /** tolerance */ 
        );
        /** Tests visualization statistics 
         <br>  Created in NX12.0.2.  <br>  
         <br> License requirements : None */
        void RunVisualizationStatistics
        (
            const char * testName /** testname */ ,
            int version /** version */ ,
            const std::vector<int> & errorCodes /** errorcodes */ ,
            NXOpen::ArchTemplateTestManager::StatisticsViewType statisticsViewType /** statisticsviewtype */ ,
            NXOpen::ArchTemplateTestManager::ToleranceType toleranceType /** tolerancetype */ ,
            double tolerance /** tolerance */ 
        );
        /** Tests visualization setup 
         <br>  Created in NX12.0.2.  <br>  
         <br> License requirements : None */
        public: void RunVisualizationSetup
        (
            const NXString & testName /** testname */ ,
            int version /** version */ ,
            const std::vector<int> & errorCodes /** errorcodes */ ,
            const NXString & paxFileSpec /** paxfilespec */ 
        );
        /** Tests visualization setup 
         <br>  Created in NX12.0.2.  <br>  
         <br> License requirements : None */
        void RunVisualizationSetup
        (
            const char * testName /** testname */ ,
            int version /** version */ ,
            const std::vector<int> & errorCodes /** errorcodes */ ,
            const char * paxFileSpec /** paxfilespec */ 
        );
        /** Tests visualization settings test 
         <br>  Created in NX12.0.2.  <br>  
         <br> License requirements : None */
        public: void RunVisualizationSettingsTest
        (
            const NXString & testName /** testname */ ,
            int version /** version */ ,
            const std::vector<int> & errorCodes /** errorcodes */ 
        );
        /** Tests visualization settings test 
         <br>  Created in NX12.0.2.  <br>  
         <br> License requirements : None */
        void RunVisualizationSettingsTest
        (
            const char * testName /** testname */ ,
            int version /** version */ ,
            const std::vector<int> & errorCodes /** errorcodes */ 
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
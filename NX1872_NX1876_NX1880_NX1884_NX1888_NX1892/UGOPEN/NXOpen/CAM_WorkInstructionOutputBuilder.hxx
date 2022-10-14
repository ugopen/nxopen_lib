#ifndef NXOpen_CAM_WORKINSTRUCTIONOUTPUTBUILDER_HXX_INCLUDED
#define NXOpen_CAM_WORKINSTRUCTIONOUTPUTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_WorkInstructionOutputBuilder.ja
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
#include <NXOpen/libnxopencpp_cam_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAM
    {
        class WorkInstructionOutputBuilder;
    }
    class Builder;
    namespace CAM
    {
        class CAMObject;
    }
    namespace CAM
    {
        class _WorkInstructionOutputBuilderBuilder;
        class WorkInstructionOutputBuilderImpl;
        /** Represents the builder for Work Instruction Output.
                This class is used to publish work instructions for the end user.  <br> To create a new instance of this class, use @link NXOpen::CAM::CAMSetup::CreateWorkInstructionOutputBuilder  NXOpen::CAM::CAMSetup::CreateWorkInstructionOutputBuilder @endlink  <br> 
         <br>  Created in NX9.0.3.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  WorkInstructionOutputBuilder : public NXOpen::Builder
        {
            /** the output format type */
            public: enum OutputFormatType
            {
                OutputFormatTypeHtml/** html */ ,
                OutputFormatTypePdf/** pdf */ ,
                OutputFormatTypeCsv/** csv */ ,
                OutputFormatTypeXml/** xml */ 
            };

            /** the page orientation type */
            public: enum PageOrientationType
            {
                PageOrientationTypeLandscape/** landscape */ ,
                PageOrientationTypePortrait/** portrait */ 
            };

            /** the page size type */
            public: enum PageSizeType
            {
                PageSizeTypeA0/** a0 */ ,
                PageSizeTypeA1/** a1 */ ,
                PageSizeTypeA2/** a2 */ ,
                PageSizeTypeA3/** a3 */ ,
                PageSizeTypeA4/** a4 */ ,
                PageSizeTypeB1/** b1 */ ,
                PageSizeTypeB2/** b2 */ ,
                PageSizeTypeB3/** b3 */ ,
                PageSizeTypeB4/** b4 */ ,
                PageSizeTypeB5/** b5 */ ,
                PageSizeTypeExecutive/** executive */ ,
                PageSizeTypeFolio/** folio */ ,
                PageSizeTypeLegal/** legal */ ,
                PageSizeTypeLetter/** letter */ ,
                PageSizeTypeTabloid/** tabloid */ 
            };

            private: WorkInstructionOutputBuilderImpl * m_workinstructionoutputbuilder_impl;
            private: friend class  _WorkInstructionOutputBuilderBuilder;
            protected: WorkInstructionOutputBuilder();
            public: ~WorkInstructionOutputBuilder();
            /**Returns  the output format 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::WorkInstructionOutputBuilder::OutputFormatType OutputFormat
            (
            );
            /**Sets  the output format 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : nx_wi_authoring (" NX Work Instruction Authoring") */
            public: void SetOutputFormat
            (
                NXOpen::CAM::WorkInstructionOutputBuilder::OutputFormatType format /** format */ 
            );
            /**Returns  the output file 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : None */
            public: NXString OutputFile
            (
            );
            /**Sets  the output file 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : nx_wi_authoring (" NX Work Instruction Authoring") */
            public: void SetOutputFile
            (
                const NXString & filename /** filename */ 
            );
            /**Sets  the output file 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : nx_wi_authoring (" NX Work Instruction Authoring") */
            void SetOutputFile
            (
                const char * filename /** filename */ 
            );
            /**Returns  the open file 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : None */
            public: bool OpenFile
            (
            );
            /**Sets  the open file 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : nx_wi_authoring (" NX Work Instruction Authoring") */
            public: void SetOpenFile
            (
                bool openFile /** openfile */ 
            );
            /**Returns  the page orientation 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::WorkInstructionOutputBuilder::PageOrientationType PageOrientation
            (
            );
            /**Sets  the page orientation 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : nx_wi_authoring (" NX Work Instruction Authoring") */
            public: void SetPageOrientation
            (
                NXOpen::CAM::WorkInstructionOutputBuilder::PageOrientationType pageOrientation /** pageorientation */ 
            );
            /**Returns  the page size 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::WorkInstructionOutputBuilder::PageSizeType PageSize
            (
            );
            /**Sets  the page size 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : nx_wi_authoring (" NX Work Instruction Authoring") */
            public: void SetPageSize
            (
                NXOpen::CAM::WorkInstructionOutputBuilder::PageSizeType pageSize /** pagesize */ 
            );
            /**Returns  the scale factor 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : None */
            public: double ScaleFactor
            (
            );
            /**Sets  the scale factor 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : nx_wi_authoring (" NX Work Instruction Authoring") */
            public: void SetScaleFactor
            (
                double scaleFactor /** scalefactor */ 
            );
            /** Publish the Work Instructions 
             <br>  Created in NX9.0.3.  <br>  
             <br> License requirements : nx_wi_authoring (" NX Work Instruction Authoring") */
            public: void Publish
            (
                const std::vector<NXOpen::CAM::CAMObject *> & objects /** array of objects */,
                NXOpen::CAM::CAMObject * firstSelObj /** firstselobj */ ,
                int currentView /** CAM_SETUP_view */
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
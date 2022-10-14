#ifndef NXOpen_CAM_DEBUG_HXX_INCLUDED
#define NXOpen_CAM_DEBUG_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_Debug.ja
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
    namespace CAM
    {
        class Debug;
    }
    class DebugSession;
    namespace CAM
    {
        class CAMObject;
    }
    namespace CAM
    {
        class Operation;
    }
    namespace CAM
    {
        class DebugImpl;

        /// \cond NX_NO_DOC 
        /** Represents a class that is used for NX testing.  This class should not
            be made available to customers  <br> To obtain an instance of this class, refer to @link NXOpen::DebugSession  NXOpen::DebugSession @endlink  <br> 
         <br>  Created in NX9.0.2.  <br>  
        */
        class NXOPENDEBUGSESSIONCPPEXPORT  Debug
        {
            private: DebugImpl * m_debug_impl;
            private: NXOpen::DebugSession* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit Debug(NXOpen::DebugSession *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~Debug();

            /// \cond NX_NO_DOC 
            /** Debug Trace user button presses. 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: void ButtonDown
            (
                bool isOn /** ison */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Debug Measure display time 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: void Timer
            (
                bool isOn /** ison */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Debug Trace display functions 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: void Trace
            (
                bool isOn /** ison */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Debug Trace get state 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: bool GetTraceOn
            (
                const NXString & traceName /** tracename */ 
            );
            /** Debug Trace get state 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            bool GetTraceOn
            (
                const char * traceName /** tracename */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Debug Trace set state 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void SetTraceOn
            (
                const NXString & traceName /** tracename */ ,
                bool isOn /** ison */ 
            );
            /** Debug Trace set state 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            void SetTraceOn
            (
                const char * traceName /** tracename */ ,
                bool isOn /** ison */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Debug Table of tool path display motions 
             <br>  Created in NX9.0.2.  <br>  
             <br> License requirements : None */
            public: void Table
            (
                bool isOn /** ison */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Debug Table of tool path findings 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: void Finding
            (
                NXOpen::CAM::CAMObject * opr /** the param object */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Display the dialog used to edit the param object
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void DisplayDialog
            (
                NXOpen::CAM::CAMObject * paramObj /** the param object */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Print XML diagnostic of dialog used to edit the param object
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: void DialogDiagnostic
            (
                NXOpen::CAM::CAMObject * paramObject /** the param object */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Execute dialog elements and print XML diagnostic of the dialog
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: void ExecuteDialogElements
            (
                NXOpen::CAM::CAMObject * paramObject /** the param object */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Return valid tool librefs based on input tool DBC Class identification and query string 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetLibraryTools
            (
                const NXString & classId /** classid */ ,
                const NXString & queryString /** querystring */ 
            );
            /** Return valid tool librefs based on input tool DBC Class identification and query string 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : None */
            std::vector<NXString> GetLibraryTools
            (
                const char * classId /** classid */ ,
                const char * queryString /** querystring */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Validate path data (level, region, pattern markers ...) in the tool path of path owner.
                        Return true if validation is ok (no errors).
                        Otherwise, return false (have errors) and fill up arrays errorCodeList and errorCodeStrings 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: bool ValidatePath
            (
                NXOpen::CAM::CAMObject * paramObj /** the param object */,
                std::vector<int> & errorCodeList /** errorcodelist */ ,
                std::vector<NXString> & errorCodeStrings /** errorcodestrings */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Get the status of the param mapping. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool GetParamMappingStatus
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Set the status of the param mapping. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void SetParamMappingStatus
            (
                bool paramMapStatus /** parammapstatus */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Master template update API 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void UpdateMasterTemplate
            (
                const NXString & fileLocation /** filelocation */ ,
                const NXString & masterTemplateName /** mastertemplatename */ 
            );
            /** Master template update API 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            void UpdateMasterTemplate
            (
                const char * fileLocation /** filelocation */ ,
                const char * masterTemplateName /** mastertemplatename */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Get runtime operation from Merge object @return  the runtime oper 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::Operation * GetRuntimeOperation
            (
                NXOpen::CAM::CAMObject * paramObject /** the param object */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**  Is the path edited  @return  true if path edited 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsPathEdited
            (
                NXOpen::CAM::CAMObject * objectTag /** the param object */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**  Set gouge check stock 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void SetGougeCheckStock
            (
                NXOpen::CAM::CAMObject * objectTag /** the param object */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Compare path event data (width/height ...) between the master and current tool paths
                        of path owner.
                        Return true if comparing path data are ok (ie., no differences).
                        Otherwise, return false (ie., have differences). 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: bool ComparePathEventData
            (
                NXOpen::CAM::CAMObject * paramObj /** the param object */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Debug Table for param validity status 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void DumpParamValidityStatus
            (
                const std::vector<NXOpen::CAM::CAMObject *> & objects /** Array of param objects*/
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Dump MasterTemplate information 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void DumpMasterTemplate
            (
                const NXString & masterTemplateFile /** mastertemplatefile */ 
            );
            /** Dump MasterTemplate information 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            void DumpMasterTemplate
            (
                const char * masterTemplateFile /** mastertemplatefile */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Clean Master Template 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void CleanMasterTemplate
            (
                const NXString & masterTemplateFile /** mastertemplatefile */ 
            );
            /** Clean Master Template 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            void CleanMasterTemplate
            (
                const char * masterTemplateFile /** mastertemplatefile */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Create type template parts from the master template 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void CreateTypeTemplateParts
            (
                const NXString & fileLocation /** filelocation */ ,
                const NXString & masterTemplateName /** mastertemplatename */ ,
                const NXString & templateFolderName /** templatefoldername */ 
            );
            /** Create type template parts from the master template 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            void CreateTypeTemplateParts
            (
                const char * fileLocation /** filelocation */ ,
                const char * masterTemplateName /** mastertemplatename */ ,
                const char * templateFolderName /** templatefoldername */ 
            );

            /// \endcond 
        }; //lint !e1712 default constructor not defined for class  


        /// \endcond 
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
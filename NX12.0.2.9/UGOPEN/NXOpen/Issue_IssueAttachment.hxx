#ifndef NXOpen_ISSUE_ISSUEATTACHMENT_HXX_INCLUDED
#define NXOpen_ISSUE_ISSUEATTACHMENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Issue_IssueAttachment.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_issue_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Issue
    {
        class IssueAttachment;
    }
    class NXObject;
    namespace Issue
    {
        class _IssueAttachmentBuilder;
        class IssueAttachmentImpl;
        /** Represents the Issue Attachment object.  <br> To create a new instance of this class, use @link NXOpen::Issue::IssueManager::CreateIssueAttachment  NXOpen::Issue::IssueManager::CreateIssueAttachment @endlink  <br> 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_ISSUEEXPORT  IssueAttachment : public NXOpen::NXObject
        {
            /** Represents the possible attachment types
                         for a @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink .
                    */
            public: enum Type
            {
                TypeGeneric/** Generic type */,
                TypeText/** Text type */,
                TypePart/** Part type */,
                TypeXml/** XML type */,
                TypeImage/** Image type */,
                TypeValidationLog/** Validation log file */,
                TypeBookmark/** Bookmark type */,
                TypeSnapshot/** Snapshot type */,
                TypeValidationResult/** ValidationResult object type */,
                TypeWorkset/** Workset type */,
                TypeShapeDesignElement/** Shape Design Element type */,
                TypeReuseDesignElement/** Reuse Design Element type */,
                TypeSubordinateDesignElement/** Subordinate Design Element type */,
                TypePromissoryDesignElement/** Promissory Design Element type */,
                TypeDesignControlElement/** Design Control Element type */,
                TypeSubset/** Subset type */,
                TypeMSWord/** Microsoft Word type */,
                TypeMSExcel/** Microsoft Excel type */,
                TypeMSPowerPoint/** Microsoft Power Point type */
            };

            private: IssueAttachmentImpl * m_issueattachment_impl;
            private: friend class  _IssueAttachmentBuilder;
            protected: IssueAttachment();
            public: ~IssueAttachment();
            /**Returns  the attachment type 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Issue::IssueAttachment::Type AttachmentType
            (
            );
            /**Sets  the attachment type 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_issue_mgmt ("NX Issue Tracking") */
            public: void SetAttachmentType
            (
                NXOpen::Issue::IssueAttachment::Type type /** type */ 
            );
            /**Returns  the refereced attachment id which specifies one attachment that is related 
                    to this @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ReferencedAttachmentId
            (
            );
            /**Sets  the refereced attachment id which specifies one attachment that is related 
                    to this @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_issue_mgmt ("NX Issue Tracking") */
            public: void SetReferencedAttachmentId
            (
                const NXString & referencedAttachmentId /** referencedattachmentid */ 
            );
            /**Sets  the refereced attachment id which specifies one attachment that is related 
                    to this @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_issue_mgmt ("NX Issue Tracking") */
            void SetReferencedAttachmentId
            (
                const char * referencedAttachmentId /** referencedattachmentid */ 
            );
            /** Recapture the snapshot 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_issue_mgmt ("NX Issue Tracking") */
            public: void RecaptureSnapshot
            (
                const NXString & bookmarkFileSpec /** bookmarkfilespec */ ,
                const NXString & imageFileSpec /** imagefilespec */ 
            );
            /** Recapture the snapshot 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_issue_mgmt ("NX Issue Tracking") */
            void RecaptureSnapshot
            (
                const char * bookmarkFileSpec /** bookmarkfilespec */ ,
                const char * imageFileSpec /** imagefilespec */ 
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

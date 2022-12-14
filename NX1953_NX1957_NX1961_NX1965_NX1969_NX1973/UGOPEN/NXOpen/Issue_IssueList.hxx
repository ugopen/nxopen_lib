#ifndef NXOpen_ISSUE_ISSUELIST_HXX_INCLUDED
#define NXOpen_ISSUE_ISSUELIST_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Issue_IssueList.ja
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
#include <NXOpen/Issue_IssueContent.hxx>
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
        class IssueList;
    }
    namespace Issue
    {
        class IssueContent;
    }
    class NXObject;
    namespace Issue
    {
        class _IssueListBuilder;
        class IssueListImpl;
        /** Represents the Issue List object. 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_ISSUEEXPORT  IssueList : public NXOpen::NXObject
        {
            private: IssueListImpl * m_issuelist_impl;
            private: friend class  _IssueListBuilder;
            protected: IssueList();
            public: ~IssueList();
            /** Reloads the @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink s 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_issue_mgmt ("NX Issue Tracking") */
            public: void ReloadIssues
            (
            );
            /** Returns all the @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink s 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_issue_mgmt ("NX Issue Tracking") */
            public: std::vector<NXOpen::Issue::IssueContent *> GetIssues
            (
            );
            /** Returns whether the list exists in database 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_issue_mgmt ("NX Issue Tracking") */
            public: bool ExistsInDatabase
            (
            );
            /** Saves the modified @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink s 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_issue_mgmt ("NX Issue Tracking") */
            public: void SaveChanges
            (
            );
            /** Discards the modified @link NXOpen::Issue::IssueContent NXOpen::Issue::IssueContent@endlink s 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_issue_mgmt ("NX Issue Tracking") */
            public: void DiscardChanges
            (
            );
            /** Saves the config of @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  to server 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_issue_mgmt ("NX Issue Tracking") */
            public: void SaveConfig
            (
            );
            /** Resets the config of @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_issue_mgmt ("NX Issue Tracking") */
            public: void ResetConfig
            (
            );
            /** Changes the config of @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_issue_mgmt ("NX Issue Tracking") */
            public: void ChangeConfig
            (
                const NXString & queryName /** The saved query name */,
                std::vector<NXString> & criteriaTitles /** The query critetia titles */,
                std::vector<NXString> & criteriaValues /** The query critetia values */
            );
            /** Changes the config of @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_issue_mgmt ("NX Issue Tracking") */
            void ChangeConfig
            (
                const char * queryName /** The saved query name */,
                std::vector<NXString> & criteriaTitles /** The query critetia titles */,
                std::vector<NXString> & criteriaValues /** The query critetia values */
            );
            /** Sets the related parts of @link NXOpen::Issue::IssueList NXOpen::Issue::IssueList@endlink  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_issue_mgmt ("NX Issue Tracking") */
            public: void SetRelatedParts
            (
                const std::vector<NXOpen::NXObject *> & parts /** parts */ 
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

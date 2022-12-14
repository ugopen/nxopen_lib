#ifndef NXOpen_ISSUE_ISSUEBRIEFCASESYNCHRONIZEBUILDER_HXX_INCLUDED
#define NXOpen_ISSUE_ISSUEBRIEFCASESYNCHRONIZEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Issue_IssueBriefcaseSynchronizeBuilder.ja
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
#include <NXOpen/Issue_IssueAttachment.hxx>
#include <NXOpen/Issue_IssueBriefcaseSynchronizeBuilder.hxx>
#include <NXOpen/Builder.hxx>
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
        class IssueBriefcaseSynchronizeBuilder;
    }
    class Builder;
    namespace Issue
    {
        class IssueAttachment;
    }
    namespace Issue
    {
        class _IssueBriefcaseSynchronizeBuilderBuilder;
        class IssueBriefcaseSynchronizeBuilderImpl;
        /** Represents a @link NXOpen::Issue::IssueBriefcase NXOpen::Issue::IssueBriefcase@endlink  synchronize builder  <br> To create a new instance of this class, use @link NXOpen::Issue::IssueBriefcase::CreateSynchronizeContentBuilder  NXOpen::Issue::IssueBriefcase::CreateSynchronizeContentBuilder @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_ISSUEEXPORT  IssueBriefcaseSynchronizeBuilder : public NXOpen::Builder
        {
            private: IssueBriefcaseSynchronizeBuilderImpl * m_issuebriefcasesynchronizebuilder_impl;
            private: friend class  _IssueBriefcaseSynchronizeBuilderBuilder;
            protected: IssueBriefcaseSynchronizeBuilder();
            public: ~IssueBriefcaseSynchronizeBuilder();
            /** Adds an part type @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink ,
                    only the added parts can be synchronized to server.
                    
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_issue_mgmt ("NX Issue Tracking") */
            public: void AddPartAttachment
            (
                NXOpen::Issue::IssueAttachment * attachment /** attachment */ 
            );
            /** Adds an part type @link NXOpen::Issue::IssueAttachment NXOpen::Issue::IssueAttachment@endlink . 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : nx_issue_mgmt ("NX Issue Tracking") */
            public: void RemovePartAttachment
            (
                NXOpen::Issue::IssueAttachment * attachment /** attachment */ 
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

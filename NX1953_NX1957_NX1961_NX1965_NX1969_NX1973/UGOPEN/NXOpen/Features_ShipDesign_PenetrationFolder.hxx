#ifndef NXOpen_FEATURES_SHIPDESIGN_PENETRATIONFOLDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_PENETRATIONFOLDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_PenetrationFolder.ja
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
#include <NXOpen/Issue_IssueFolder.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace ShipDesign
        {
            class PenetrationFolder;
        }
    }
    namespace Issue
    {
        class IssueFolder;
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class _PenetrationFolderBuilder;
            class PenetrationFolderImpl;
            /** Represents the Penetration Folder object.  <br> Not support KF.  <br> 
             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  PenetrationFolder : public NXOpen::Issue::IssueFolder
            {
                private: PenetrationFolderImpl * m_penetrationfolder_impl;
                private: friend class  _PenetrationFolderBuilder;
                protected: PenetrationFolder();
                public: ~PenetrationFolder();
            };
        }
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

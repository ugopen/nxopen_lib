#ifndef NXOpen_DRAFTING_DRAFTINGAPPLICATIONMANAGER_HXX_INCLUDED
#define NXOpen_DRAFTING_DRAFTINGAPPLICATIONMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drafting_DraftingApplicationManager.ja
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
#include <NXOpen/Drafting_CutCopyPasteBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Drafting
    {
        class DraftingApplicationManager;
    }
    class Part;
    namespace Drafting
    {
        class CutCopyPasteBuilder;
    }
    namespace Drafting
    {
        class DraftingApplicationManagerImpl;
        /** Represents an object that manages drafting objects and member views.  <br> To obtain an instance of this class, refer to @link Part Part@endlink  <br> */
        class NXOPENCPPEXPORT  DraftingApplicationManager
        {
            private: DraftingApplicationManagerImpl * m_draftingapplicationmanager_impl;
            private: NXOpen::Part* m_owner;
            /** Constructor */
            public: explicit DraftingApplicationManager(NXOpen::Part *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~DraftingApplicationManager();
            /** Creates the CutCopyPaste builder  @return   <br> License requirements : None */
            public: NXOpen::Drafting::CutCopyPasteBuilder * CreateCutCopyPasteBuilder
            (
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
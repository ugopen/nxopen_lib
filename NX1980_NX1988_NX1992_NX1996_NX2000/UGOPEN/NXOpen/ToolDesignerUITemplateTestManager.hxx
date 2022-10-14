#ifndef NXOpen_TOOLDESIGNERUITEMPLATETESTMANAGER_HXX_INCLUDED
#define NXOpen_TOOLDESIGNERUITEMPLATETESTMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ToolDesignerUITemplateTestManager.ja
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
#include <NXOpen/libnxopendebuguicpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class ToolDesignerUITemplateTestManager;
    class UITemplateTestManager;
    class ToolDesignerUITemplateTestManagerImpl;

    /// \cond NX_NO_DOC 
    /** Represents a class that is used for autotests.  This class should not
    be made available to customers  <br> To obtain an instance of this class, refer to @link NXOpen::UITemplateTestManager  NXOpen::UITemplateTestManager @endlink  <br> 
     <br>  Created in NX1847.0.0.  <br>  
    */
    class NXOPENDEBUGUICPPEXPORT  ToolDesignerUITemplateTestManager
    {
        private: ToolDesignerUITemplateTestManagerImpl * m_tooldesigneruitemplatetestmanager_impl;
        private: NXOpen::UITemplateTestManager* m_owner;
        /// \cond NX_NO_DOC 
        public: explicit ToolDesignerUITemplateTestManager(NXOpen::UITemplateTestManager *owner);


        /// \endcond 
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~ToolDesignerUITemplateTestManager();
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
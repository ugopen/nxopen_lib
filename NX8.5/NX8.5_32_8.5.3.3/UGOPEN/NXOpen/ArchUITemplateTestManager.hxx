#ifndef NXOpen_ARCHUITEMPLATETESTMANAGER_HXX_INCLUDED
#define NXOpen_ARCHUITEMPLATETESTMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ArchUITemplateTestManager.ja
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
    class ArchUITemplateTestManager;
    class UITemplateTestManager;
    namespace Features
    {
        class Feature;
    }
    class NXObject;
    class ArchUITemplateTestManagerImpl;
    /** Represents a class that is used for autotests.  This class should not
    be made available to customers  <br> To obtain an instance of this class, refer to @link UITemplateTestManager  UITemplateTestManager @endlink  <br> 
     <br>  Created in NX8.0.0.  <br>  
    */
    class NXOPENDEBUGUICPPEXPORT  ArchUITemplateTestManager
    {
        private: ArchUITemplateTestManagerImpl * m_archuitemplatetestmanager_impl;
        private: NXOpen::UITemplateTestManager* m_owner;
        /// \cond NX_NO_DOC 
        public: explicit ArchUITemplateTestManager(NXOpen::UITemplateTestManager *owner);


        /// \endcond 
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        public: ~ArchUITemplateTestManager();
        /**  
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void RunFrameworkTemplateTest1
        (
            const NXString & testName /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            int version /** version */ ,
            const std::vector<int> & errorCodes /** errorcodes */ ,
            bool boolOption /** the part that will own the feature */,
            int intValue /** intvalue */ ,
            double doubleValue /** doublevalue */ ,
            const NXString & stringValue /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            const std::vector<NXOpen::NXObject *> & objects /** objects */ ,
            const std::vector<NXOpen::Features::Feature *> & features /** features */ 
        );
        /**  
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        void RunFrameworkTemplateTest1
        (
            const char * testName /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            int version /** version */ ,
            const std::vector<int> & errorCodes /** errorcodes */ ,
            bool boolOption /** the part that will own the feature */,
            int intValue /** intvalue */ ,
            double doubleValue /** doublevalue */ ,
            const char * stringValue /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            const std::vector<NXOpen::NXObject *> & objects /** objects */ ,
            const std::vector<NXOpen::Features::Feature *> & features /** features */ 
        );
        /**  
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void UIFrameworkTest
        (
            const NXString & testName /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            int version /** version */ ,
            const std::vector<int> & errorCodes /** errorcodes */ ,
            bool boolValue /** bool value */ ,
            double doubleValue /** doublevalue */ ,
            int intValue /** intvalue */ ,
            const std::vector<NXOpen::Features::Feature *> & features /** features */ ,
            const std::vector<NXOpen::NXObject *> & objects /** objects */ ,
            const NXString & stringValue /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /**  
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        void UIFrameworkTest
        (
            const char * testName /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            int version /** version */ ,
            const std::vector<int> & errorCodes /** errorcodes */ ,
            bool boolValue /** bool value */ ,
            double doubleValue /** doublevalue */ ,
            int intValue /** intvalue */ ,
            const std::vector<NXOpen::Features::Feature *> & features /** features */ ,
            const std::vector<NXOpen::NXObject *> & objects /** objects */ ,
            const char * stringValue /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
    }; //lint !e1712 default constructor not defined for class  

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

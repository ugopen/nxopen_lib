#ifndef NXOpen_FILENEWTEMPLATE_HXX_INCLUDED
#define NXOpen_FILENEWTEMPLATE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     FileNewTemplate.ja
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
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class FileNewTemplate;
    class FileNewTemplateImpl;
    /**
        Represents a @link NXOpen::FileNewTemplate NXOpen::FileNewTemplate@endlink 
         <br> Use the @link NXOpen::FileNew NXOpen::FileNew@endlink  to query objects of this class.  <br> 
     <br>  Created in NX1847.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  FileNewTemplate : public NXOpen::TransientObject
    {
        private: FileNewTemplateImpl * m_filenewtemplate_impl;
        /// \cond NX_NO_DOC 
        public: explicit FileNewTemplate(void *ptr);
        /// \endcond 
        /** Gets if the template is a blank template that creates a new file using customer defaults instead of a seed part 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: bool IsBlank
        (
        );
        /** Gets the name of the template 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: NXString GetName
        (
        );
        /** Gets the units of the template 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::Part::Units GetUnits
        (
        );
        /** Free resources associated with the instance of this report. 
                This also free the resource associated with the status objects. 
                After this method is called, it is illegal to use the object.  
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: virtual ~FileNewTemplate();
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

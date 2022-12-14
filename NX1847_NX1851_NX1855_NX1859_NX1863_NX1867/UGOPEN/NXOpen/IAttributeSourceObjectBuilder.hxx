#ifndef NXOpen_IATTRIBUTESOURCEOBJECTBUILDER_HXX_INCLUDED
#define NXOpen_IATTRIBUTESOURCEOBJECTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     IAttributeSourceObjectBuilder.ja
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
#include <NXOpen/ErrorList.hxx>
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
    class IAttributeSourceObjectBuilder;
    class ErrorList;
    class NXObject;
    /** Represents an interface to perform various database operations on an array of @link NXOpen::NXObject NXOpen::NXObject@endlink . 

     <br>  Created in NX8.5.0.  <br>  
    */
    class NXOPENCPPEXPORT  IAttributeSourceObjectBuilder
    {
        virtual void EnsureVtableExists() {}
        public: virtual ~IAttributeSourceObjectBuilder() {}
        /**  Auto assigns the attributes for a given array of objects and returns an array of objects that failed to auto assign.
           
         <br>  Created in NX8.5.0.  <br>  
         <br> License requirements : None */
        public: virtual NXOpen::ErrorList * AutoAssignAttributes
        (
            const std::vector<NXOpen::NXObject *> & objects /** objects */ 
        ) = 0;
        /**  Auto assigns the attributes for a given object and returns an array of objects that failed to auto assign.
                properties needs to be created using @link CreateAttributeTitleToNamingPatternMap CreateAttributeTitleToNamingPatternMap@endlink 
           
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : None */
        public: virtual NXOpen::ErrorList * AutoAssignAttributesWithNamingPattern
        (
            const std::vector<NXOpen::NXObject *> & objects /** objects */ ,
            const std::vector<NXOpen::NXObject *> & properties /** properties */ 
        ) = 0;
        /** Creates a map object of attribute titles to their corresponding naming pattern 
         <br>  Created in NX12.0.0.  <br>  
         <br> License requirements : None */
        public: virtual NXOpen::NXObject * CreateAttributeTitleToNamingPatternMap
        (
            std::vector<NXString> & attributeTitles /** attributetitles */ ,
            std::vector<NXString> & titlePatterns /** titlepatterns */ 
        ) = 0;
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

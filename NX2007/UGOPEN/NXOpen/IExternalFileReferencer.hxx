#ifndef NXOpen_IEXTERNALFILEREFERENCER_HXX_INCLUDED
#define NXOpen_IEXTERNALFILEREFERENCER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     IExternalFileReferencer.ja
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
#include <NXOpen/ExternalFileReferenceAdapter.hxx>
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
    class IExternalFileReferencer;
    class ExternalFileReferenceAdapter;
    /** Represents an interface needed to be implemented by the application object
        which wants to establish an external file reference managed in Teamcenter. 
     <br>  Created in NX1847.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  IExternalFileReferencer
    {
        virtual void EnsureVtableExists() {}
        public: virtual ~IExternalFileReferencer() {}
        /**  Returns the external file reference object. In case the referencer object has multiple external references,
                 use referenceObjectId to return the correct external file adapter.  @return  external file reference object 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: virtual NXOpen::ExternalFileReferenceAdapter * GetExternalFileReferenceAdapter
        (
            int referenceObjectId /** the unique identifier of the external reference required in case where referencer has multiple external references */
        ) = 0;
        /**  Sets the external file reference object. In case the referencer object has multiple external references,
                 use referenceObjectId to set the correct reference. 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: virtual void SetExternalFileReferenceAdapter
        (
            int referenceObjectId /** the unique identifier of the external reference required in case where referencer has multiple external references */,
            NXOpen::ExternalFileReferenceAdapter * adapter /** external file reference object */
        ) = 0;
        /**  Gets the file definition to use for external file adapter. 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: virtual NXString GetExternalFileDefinitionKey
        (
            NXOpen::ExternalFileReferenceAdapter * adapter /** external file reference object */
        ) = 0;
        /** Establish the external reference to the given file specification.  @return  external file reference object 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        public: virtual NXOpen::ExternalFileReferenceAdapter * EstablishReference
        (
            int referenceObjectId /** the unique identifier to use for this reference if referencer has multiple external references */,
            NXOpen::ExternalFileReferenceAdapter::Type referenceType /** the kind of reference to establish */,
            const NXString & externalFileSpec /** the external file specification. */
        ) = 0;
        /** Establish the external reference to the given file specification.  @return  external file reference object 
         <br>  Created in NX1847.0.0.  <br>  
         <br> License requirements : None */
        virtual NXOpen::ExternalFileReferenceAdapter * EstablishReference
        (
            int referenceObjectId /** the unique identifier to use for this reference if referencer has multiple external references */,
            NXOpen::ExternalFileReferenceAdapter::Type referenceType /** the kind of reference to establish */,
            const char * externalFileSpec /** the external file specification. */
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
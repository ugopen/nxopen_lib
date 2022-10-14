#ifndef NXOpen_TOOLING_CLONEOBJECT_HXX_INCLUDED
#define NXOpen_TOOLING_CLONEOBJECT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_CloneObject.ja
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
#include <NXOpen/Tooling_CloneObject.hxx>
#include <NXOpen/Tooling_ClonePart.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Tooling
    {
        class CloneObject;
    }
    namespace Tooling
    {
        class ClonePart;
    }
    namespace Tooling
    {
        class CloneObjectImpl;
        /** Represents the clone operation in Add Reusable Component Builder. 
              <br> To create an instance of this object use @link Tooling::AddReusablePart::CreateCloneObject Tooling::AddReusablePart::CreateCloneObject@endlink  <br> */
        class NXOPENCPPEXPORT  CloneObject : public TransientObject
        {
            private: CloneObjectImpl * m_cloneobject_impl;
            public: explicit CloneObject(void *ptr);
            /** Destructs the class. 
                      <br> License requirements : None */
            public: virtual ~CloneObject();
            /** Adds the part/assembly to be cloned. 
                      <br> License requirements : None */
            public: void AddAssembly
            (
                const NXString & assemName /** Project assembly name */
            );
            /** Creates a new clone part item. 
                      @return  the new @link Tooling::ClonePart Tooling::ClonePart@endlink  instance  <br> License requirements : None */
            public: NXOpen::Tooling::ClonePart * CreateClonePartItem
            (
                const NXString & partName /** clone part name */
            );
            /** Performs the clone operation. 
                      @return   <br> License requirements : None */
            public: NXString Commit
            (
            );
            /** Find the part item to be cloned by giving part name  @return  The returned @link Tooling::ClonePart Tooling::ClonePart@endlink  instance  <br> License requirements : None */
            public: NXOpen::Tooling::ClonePart * FindClonePartItem
            (
                const NXString & partName /** clone part name */
            );
            /**Returns  the destination folder
                      <br> License requirements : None */
            public: NXString OutputFolder
            (
            );
            /**Sets  the destination folder
                      <br> License requirements : None */
            public: void SetOutputFolder
            (
                const NXString & outputFolder /** outputfolder */ 
            );
            /**Returns  the clone method
                      <br> License requirements : None */
            public: int CloneMethod
            (
            );
            /**Sets  the clone method
                      <br> License requirements : None */
            public: void SetCloneMethod
            (
                int cloneMethod /** clonemethod */ 
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
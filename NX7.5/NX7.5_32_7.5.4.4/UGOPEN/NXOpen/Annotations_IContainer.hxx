#ifndef NXOpen_ANNOTATIONS_ICONTAINER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_ICONTAINER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_IContainer.ja
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
#include <NXOpen/INXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class IContainer;
    }
    class INXObject;
    class NXObject;
    namespace Annotations
    {
        /** Represents an object that contains other objects */
        class NXOPENCPPEXPORT  IContainer : public virtual INXObject
        {
            public: virtual ~IContainer() {}
            /** Returns the objects in the container  @return  List of objects  <br> License requirements : None */
            public: virtual std::vector<NXOpen::NXObject *> GetObjects
            (
            ) = 0;
            /** Removes an object in the container. The container object is deleted when
                        the last object in it is deleted  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: virtual void RemoveObject
            (
                NXOpen::NXObject * object /** Object to remove */
            ) = 0;
        };
    }
}
#undef EXPORTLIBRARY
#endif
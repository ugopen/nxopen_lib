#ifndef NXOpen_ASSEMBLIES_PRODUCTINTERFACE_INTERFACEOBJECT_HXX_INCLUDED
#define NXOpen_ASSEMBLIES_PRODUCTINTERFACE_INTERFACEOBJECT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Assemblies_ProductInterface_InterfaceObject.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Assemblies
    {
        namespace ProductInterface
        {
            class InterfaceObject;
        }
    }
    class NXObject;
    namespace Assemblies
    {
        namespace ProductInterface
        {
            class _InterfaceObjectBuilder;
            /** Represents a Product Interface Object Builder. It creates a product interface object  <br> To create a new instance of this class, use @link Assemblies::ProductInterface::ObjectBuilder::AddProductInterfaceObject Assemblies::ProductInterface::ObjectBuilder::AddProductInterfaceObject@endlink  <br> */
            class NXOPENCPPEXPORT InterfaceObject : public NXObject
            {
                private: friend class  _InterfaceObjectBuilder;
                protected: InterfaceObject();
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
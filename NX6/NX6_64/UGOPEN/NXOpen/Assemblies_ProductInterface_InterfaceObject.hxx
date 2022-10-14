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
                /** Returns the type of the input product interface object   @return  type of the product interface object  <br> License requirements : None */
                public: NXString GetProductInterfaceObjectType
                (
                );
                /** Returns the underlying NX object referenced by the input product interface object   @return  nx item referenced by the product interface  <br> License requirements : None */
                public: NXOpen::NXObject * GetProductInterfaceDefiningEntity
                (
                );
                /** Returns the status of the input product interface object   @return  status of the product interface object  <br> License requirements : None */
                public: NXString GetProductInterfaceObjectStatus
                (
                );
                /** Sets the user comments on the input product interface object  <br> License requirements : None */
                public: void SetUserComments
                (
                    const NXString & userComments /** user comments to be set on the product interface object   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /** Returns the user comments on the input product interface object  @return  user comments on the product interface object  <br> License requirements : None */
                public: NXString GetUserComments
                (
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
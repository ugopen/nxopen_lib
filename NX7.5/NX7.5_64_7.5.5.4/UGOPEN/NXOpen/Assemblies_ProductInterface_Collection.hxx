#ifndef NXOpen_ASSEMBLIES_PRODUCTINTERFACE_COLLECTION_HXX_INCLUDED
#define NXOpen_ASSEMBLIES_PRODUCTINTERFACE_COLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Assemblies_ProductInterface_Collection.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Assemblies
    {
        namespace ProductInterface
        {
            class Collection;
        }
    }
    class Part;
    namespace Assemblies
    {
        namespace ProductInterface
        {
            class ObjectBuilder;
        }
    }
    class NXObject;
    namespace Assemblies
    {
        namespace ProductInterface
        {
            class CollectionImpl;
            /** This class represents the collection of product interface objects  <br> To obtain an instance of this class, refer to @link Part Part@endlink  <br> */
            class NXOPENCPPEXPORT  Collection
            {
                private: CollectionImpl * m_collection_impl;
                private: NXOpen::Part* m_owner;
                /** Constructor */
                public: explicit Collection(NXOpen::Part *owner);
                public: 
                /**Returns the tag of this object.  */
                tag_t Tag() const; 
                public: ~Collection();
                /** Create Product Interface Object Builder  @return   <br> License requirements : None */
                public: NXOpen::Assemblies::ProductInterface::ObjectBuilder * CreateObjectBuilder
                (
                );
                /** Find the Product Interface Object with input name  @return  Product Interface Object with this identifier  <br> License requirements : None */
                public: NXOpen::NXObject * FindObject
                (
                    const NXString & journalIdentifier /** Identifier of the product interface object you want */
                );
            }; //lint !e1712 default constructor not defined for class  

        }
    }
}
#undef EXPORTLIBRARY
#endif

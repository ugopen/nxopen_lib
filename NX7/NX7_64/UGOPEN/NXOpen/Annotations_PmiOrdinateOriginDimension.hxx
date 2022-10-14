#ifndef NXOpen_ANNOTATIONS_PMIORDINATEORIGINDIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIORDINATEORIGINDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiOrdinateOriginDimension.ja
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
#include <NXOpen/Annotations_IPmi.hxx>
#include <NXOpen/Annotations_AssociatedObject.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/Annotations_OrdinateOriginDimension.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class PmiOrdinateOriginDimension;
    }
    namespace Annotations
    {
        class AssociatedObject;
    }
    namespace Annotations
    {
        class BusinessModifier;
    }
    namespace Annotations
    {
        class IPmi;
    }
    namespace Annotations
    {
        class OrdinateOriginDimension;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class INXObject;
    namespace Annotations
    {
        class _PmiOrdinateOriginDimensionBuilder;
        /** Represents a PMI ordinate origin dimension  <br> To create a new instance of this class, use @link Annotations::DimensionCollection::CreatePmiOrdinateOriginDimension Annotations::DimensionCollection::CreatePmiOrdinateOriginDimension@endlink  <br> */
        class NXOPENCPPEXPORT PmiOrdinateOriginDimension : public Annotations::OrdinateOriginDimension, public virtual Annotations::IPmi
        {
            private: friend class  _PmiOrdinateOriginDimensionBuilder;
            protected: PmiOrdinateOriginDimension();
            /** Returns the business modifiers  @return  List of business modifiers  <br> License requirements : None */
            public: virtual std::vector<NXOpen::Annotations::BusinessModifier *> GetBusinessModifiers
            (
            );
            /** Sets the business modifiers  <br> License requirements : geometric_tol ("GDT") */
            public: virtual void SetBusinessModifiers
            (
                const std::vector<NXOpen::Annotations::BusinessModifier *> & businessModifiers /** List of new business modifiers */
            );
            /** Returns the associated object  @return  Associated object  <br> License requirements : None */
            public: virtual NXOpen::Annotations::AssociatedObject * GetAssociatedObject
            (
            );
            /** Sets the associated object  <br> License requirements : geometric_tol ("GDT") */
            public: virtual void SetAssociatedObject
            (
                NXOpen::Annotations::AssociatedObject * assocObj /** New associated object */
            );
            /**Returns  the index. It is a unique integer assigned to a PMI object.  <br> License requirements : None */
            public: virtual int Index
            (
            );
            /**Sets  the index. It is a unique integer assigned to a PMI object.  <br> License requirements : geometric_tol ("GDT") */
            public: virtual void SetIndex
            (
                int index /** New integer for PMI object */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
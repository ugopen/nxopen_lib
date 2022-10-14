#ifndef NXOpen_ANNOTATIONS_PMICUSTOMSYMBOL_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMICUSTOMSYMBOL_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiCustomSymbol.ja
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
#include <NXOpen/Annotations_CustomSymbol.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class PmiCustomSymbol;
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
        class CustomSymbol;
    }
    namespace Annotations
    {
        class IPmi;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class INXObject;
    namespace Annotations
    {
        class _PmiCustomSymbolBuilder;
        /** Represents a PMI custom symbol */
        class NXOPENCPPEXPORT PmiCustomSymbol : public Annotations::CustomSymbol, public virtual Annotations::IPmi
        {
            private: friend class  _PmiCustomSymbolBuilder;
            protected: PmiCustomSymbol();
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
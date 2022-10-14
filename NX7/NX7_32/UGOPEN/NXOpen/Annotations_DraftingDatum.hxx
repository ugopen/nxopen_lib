#ifndef NXOpen_ANNOTATIONS_DRAFTINGDATUM_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_DRAFTINGDATUM_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_DraftingDatum.ja
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
#include <NXOpen/Annotations_IDatum.hxx>
#include <NXOpen/Annotations_Gdt.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class DraftingDatum;
    }
    namespace Annotations
    {
        class Gdt;
    }
    namespace Annotations
    {
        class IDatum;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class INXObject;
    namespace Annotations
    {
        class _DraftingDatumBuilder;
        /** Represents a datum */
        class NXOPENCPPEXPORT DraftingDatum : public Annotations::Gdt, public virtual Annotations::IDatum
        {
            private: friend class  _DraftingDatumBuilder;
            protected: DraftingDatum();
            /**Returns  the label  <br> License requirements : None */
            public: virtual NXString Label
            (
            );
            /**Sets  the label  <br> License requirements : geometric_tol ("GDT") */
            public: virtual void SetLabel
            (
                const NXString & label /** New datum label */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
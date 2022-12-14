#ifndef NXOpen_ANNOTATIONS_DRAFTINGDATUMTARGET_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_DRAFTINGDATUMTARGET_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_DraftingDatumTarget.ja
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
#include <NXOpen/Annotations_IDatumTarget.hxx>
#include <NXOpen/Annotations_Gdt.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class DraftingDatumTarget;
    }
    namespace Annotations
    {
        class ArbitraryTarget;
    }
    namespace Annotations
    {
        class DraftingArbitraryTarget;
    }
    namespace Annotations
    {
        class DraftingLineTarget;
    }
    namespace Annotations
    {
        class DraftingPointTarget;
    }
    namespace Annotations
    {
        class Gdt;
    }
    namespace Annotations
    {
        class IDatumTarget;
    }
    namespace Annotations
    {
        class LineTarget;
    }
    namespace Annotations
    {
        class PointTarget;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class INXObject;
    namespace Annotations
    {
        class _DraftingDatumTargetBuilder;
        /** Represents a datum target */
        class NXOPENCPPEXPORT DraftingDatumTarget : public Annotations::Gdt, public virtual Annotations::IDatumTarget
        {
            private: friend class  _DraftingDatumTargetBuilder;
            protected: DraftingDatumTarget();
            /** Converts a datum target line or area to a datum target point.  @return  New point target  <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Annotations::PointTarget * ConvertToPointTarget
            (
            );
            /** Converts a datum target point or area to a datum target line.  @return  New line target  <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Annotations::LineTarget * ConvertToLineTarget
            (
            );
            /** Converts a datum target point, line, or non-rectangular area to a rectangular area.  @return  New rectangulartarget  <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Annotations::ArbitraryTarget * ConvertToAreaTarget
            (
            );
            /** Converts a drafting datum target line or area to a drafting datum target point.  @return  New point target  <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Annotations::DraftingPointTarget * ConvertToDraftingPointTarget
            (
            );
            /** Converts a drafting datum target point or area to a drafting datum target line.  @return  New line target  <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Annotations::DraftingLineTarget * ConvertToDraftingLineTarget
            (
            );
            /** Converts a drafting datum target point, line, or non-rectangular area to a drafting rectangular area.  @return  New rectangulartarget  <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Annotations::DraftingArbitraryTarget * ConvertToDraftingAreaTarget
            (
            );
            /**Returns  the datum target label  <br> License requirements : None */
            public: virtual NXString DatumLabel
            (
            );
            /**Sets  the datum target label  <br> License requirements : geometric_tol ("GDT") */
            public: virtual void SetDatumLabel
            (
                const NXString & datum_label /** New datum label */
            );
            /**Returns  the datum target index  <br> License requirements : None */
            public: virtual int TargetIndex
            (
            );
            /**Sets  the datum target index  <br> License requirements : geometric_tol ("GDT") */
            public: virtual void SetTargetIndex
            (
                int index /** New datum target index */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif

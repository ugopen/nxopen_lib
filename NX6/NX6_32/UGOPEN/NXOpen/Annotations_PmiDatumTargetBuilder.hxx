#ifndef NXOpen_ANNOTATIONS_PMIDATUMTARGETBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIDATUMTARGETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiDatumTargetBuilder.ja
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
#include <NXOpen/Annotations_AssociatedObjectsBuilder.hxx>
#include <NXOpen/Annotations_PmiDatumTargetBuilder.hxx>
#include <NXOpen/Annotations_DatumTargetBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class PmiDatumTargetBuilder;
    }
    namespace Annotations
    {
        class AssociatedObjectsBuilder;
    }
    namespace Annotations
    {
        class DatumTargetBuilder;
    }
    class SelectDisplayableObject;
    namespace Annotations
    {
        class _PmiDatumTargetBuilderBuilder;
        /**
            Represents a @link Annotations::PmiDatumTargetBuilder Annotations::PmiDatumTargetBuilder@endlink 
             <br> To create a new instance of this class, use @link Annotations::AnnotationManager::CreatePmiDatumTargetBuilder Annotations::AnnotationManager::CreatePmiDatumTargetBuilder@endlink  <br> 
        Default values:
        Height.RightHandSide: 10 (millimeters part), 1 (inches part)
        InnerDiameter.RightHandSide: 1 (millimeters part), .1 (inches part)
        OuterDiameter.RightHandSide: 10 (millimeters part), 1 (inches part)
        Width.RightHandSide: 10 (millimeters part), 1 (inches part)
        */
        class NXOPENCPPEXPORT PmiDatumTargetBuilder : public Annotations::DatumTargetBuilder
        {
            private: friend class  _PmiDatumTargetBuilderBuilder;
            protected: PmiDatumTargetBuilder();
            /**Returns  the region selection  <br> License requirements : None */
            public: NXOpen::SelectDisplayableObject * RegionSelection
            (
            );
            /**Returns  the associated objects  <br> License requirements : None */
            public: NXOpen::Annotations::AssociatedObjectsBuilder * AssociatedObjects
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif

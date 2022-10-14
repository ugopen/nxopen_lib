#ifndef NXOpen_FEATURES_SHEETMETAL_FLEXIBLECABLEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_FLEXIBLECABLEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_FlexibleCableBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_SheetMetal_FlexibleCableBuilder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        namespace SheetMetal
        {
            class FlexibleCableBuilder;
        }
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class TaggedObjectList;
    namespace Features
    {
        namespace SheetMetal
        {
            class _FlexibleCableBuilderBuilder;
            /** Represents a Flexible Cable feature builder.  <br> To create a new instance of this class, use @link Features::SheetMetal::SheetmetalManager::CreateFlexibleCableBuilder Features::SheetMetal::SheetmetalManager::CreateFlexibleCableBuilder@endlink  <br> 
            Default values:
            ConductorSpacing.RightHandSide: 1 (millimeters part), 0.04 (inches part)
            ConductorWidth.RightHandSide: 2 (millimeters part), 0.08 (inches part)
            CrossSectionWidth.RightHandSide: 30 (millimeters part), 1.2 (inches part)
            NoOfConductors: 5
            StrippingLength.RightHandSide: 3 (millimeters part), 0.12 (inches part)
            Thickness.RightHandSide: 1 (millimeters part), 0.04 (inches part)
            */
            class NXOPENCPPEXPORT FlexibleCableBuilder : public Features::FeatureBuilder
            {
                private: friend class  _FlexibleCableBuilderBuilder;
                protected: FlexibleCableBuilder();
                /**Returns   <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::TaggedObjectList * TypeList
                (
                );
                /**Returns  the thickness  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Expression * Thickness
                (
                );
                /**Returns  the cross section width  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Expression * CrossSectionWidth
                (
                );
                /**Returns  the conductor width  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Expression * ConductorWidth
                (
                );
                /**Returns  the conductor spacing  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Expression * ConductorSpacing
                (
                );
                /**Returns  the stripping length  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Expression * StrippingLength
                (
                );
                /**Returns  the no of conductors  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
                public: int NoOfConductors
                (
                );
                /**Sets  the no of conductors  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
                public: void SetNoOfConductors
                (
                    int noOfConductors /** noofconductors */ 
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
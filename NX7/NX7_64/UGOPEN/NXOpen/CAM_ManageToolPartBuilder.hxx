#ifndef NXOpen_CAM_MANAGETOOLPARTBUILDER_HXX_INCLUDED
#define NXOpen_CAM_MANAGETOOLPARTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ManageToolPartBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class ManageToolPartBuilder;
    }
    class Builder;
    class NXObject;
    namespace CAM
    {
        class _ManageToolPartBuilderBuilder;
        /** Represents an Export Tool Part Builder  <br> This is an abstract class, and cannot be instantiated. <br> */
        class NXOPENCPPEXPORT ManageToolPartBuilder : public Builder
        {
            private: friend class  _ManageToolPartBuilderBuilder;
            protected: ManageToolPartBuilder();
            /**Returns  the export tool part toggle state  <br> License requirements : None */
            public: bool ExportToggleState
            (
            );
            /**Sets  the export tool part toggle state  <br> License requirements : None */
            public: void SetExportToggleState
            (
                bool state /** if true export also tool part on export, otherwise don't */
            );
            /**Returns  the tool mounting junction  <br> License requirements : None */
            public: NXOpen::NXObject * ToolMountingJunction
            (
            );
            /**Sets  the tool mounting junction  <br> License requirements : None */
            public: void SetToolMountingJunction
            (
                NXOpen::NXObject * toolMountingJunction /** tool mounting junction */ 
            );
            /** The r1 tool tip junction, applies for turning tools only  <br> License requirements : None */
            public: void AskR1ToolTipJunction
            (
                NXOpen::NXObject ** r1ToolTipJunction /** The Tool Tip Junction at radius R1*/,
                int* r1ToolTipTrackingPoint /** The tracking point (1..9) where the junction origin is located */
            );
            /** Updates the r1 tool tip junction and related tracking point (1..9) <br> License requirements : None */
            public: void UpdateR1ToolTipJunction
            (
                NXOpen::NXObject * r1ToolTipJunction /** The tool tip junction at radius R1*/,
                int r1ToolTipTrackingPoint /** The tracking point (1..9) where the junction origin is located */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
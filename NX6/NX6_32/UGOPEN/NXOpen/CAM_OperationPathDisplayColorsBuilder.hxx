#ifndef NXOpen_CAM_OPERATIONPATHDISPLAYCOLORSBUILDER_HXX_INCLUDED
#define NXOpen_CAM_OPERATIONPATHDISPLAYCOLORSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_OperationPathDisplayColorsBuilder.ja
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
#include <NXOpen/CAM_OperationPathDisplayColorsBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class OperationPathDisplayColorsBuilder;
    }
    class NXColor;
    namespace CAM
    {
        class _OperationPathDisplayColorsBuilderBuilder;
        /** Represents a path display colors Builder  <br> This is an abstract class and cannot be instantiated. <br> */
        class NXOPENCPPEXPORT OperationPathDisplayColorsBuilder : public TaggedObject
        {
            private: friend class  _OperationPathDisplayColorsBuilderBuilder;
            protected: OperationPathDisplayColorsBuilder();
            /**Returns  the color rapid  <br> License requirements : None */
            public: NXOpen::NXColor * Rapid
            (
            );
            /**Sets  the color rapid  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRapid
            (
                NXOpen::NXColor * colorRapid /** colorrapid */ 
            );
            /**Returns  the color approach  <br> License requirements : None */
            public: NXOpen::NXColor * Approach
            (
            );
            /**Sets  the color approach  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetApproach
            (
                NXOpen::NXColor * colorApproach /** colorapproach */ 
            );
            /**Returns  the color engage  <br> License requirements : None */
            public: NXOpen::NXColor * Engage
            (
            );
            /**Sets  the color engage  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetEngage
            (
                NXOpen::NXColor * colorEngage /** colorengage */ 
            );
            /**Returns  the color first cut  <br> License requirements : None */
            public: NXOpen::NXColor * FirstCut
            (
            );
            /**Sets  the color first cut  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetFirstCut
            (
                NXOpen::NXColor * colorFirstCut /** colorfirstcut */ 
            );
            /**Returns  the color stepover  <br> License requirements : None */
            public: NXOpen::NXColor * Stepover
            (
            );
            /**Sets  the color stepover  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetStepover
            (
                NXOpen::NXColor * colorStepover /** colorstepover */ 
            );
            /**Returns  the color cut  <br> License requirements : None */
            public: NXOpen::NXColor * Cut
            (
            );
            /**Sets  the color cut  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCut
            (
                NXOpen::NXColor * colorCut /** colorcut */ 
            );
            /**Returns  the color traversal  <br> License requirements : None */
            public: NXOpen::NXColor * Traversal
            (
            );
            /**Sets  the color traversal  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetTraversal
            (
                NXOpen::NXColor * colorTraversal /** colortraversal */ 
            );
            /**Returns  the color retract  <br> License requirements : None */
            public: NXOpen::NXColor * Retract
            (
            );
            /**Sets  the color retract  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetRetract
            (
                NXOpen::NXColor * colorRetract /** colorretract */ 
            );
            /**Returns  the color departure  <br> License requirements : None */
            public: NXOpen::NXColor * Departure
            (
            );
            /**Sets  the color departure  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetDeparture
            (
                NXOpen::NXColor * colorDeparture /** colordeparture */ 
            );
            /**Returns  the color common  <br> License requirements : None */
            public: NXOpen::NXColor * Common
            (
            );
            /**Sets  the color common  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCommon
            (
                NXOpen::NXColor * colorCommon /** colorcommon */ 
            );
            /** Set the color to all common  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetAllCommonColor
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
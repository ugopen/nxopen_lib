#ifndef NXOpen_CAM_PMOPTOOLAXISCIBUILDER_HXX_INCLUDED
#define NXOpen_CAM_PMOPTOOLAXISCIBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_PmopToolAxisCiBuilder.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class PmopToolAxisCiBuilder;
    }
    class SmartObject;
    namespace CAM
    {
        class _PmopToolAxisCiBuilderBuilder;
        /** Represents a PmopToolAxisCiBuilder  <br> This is an abstract class, and cannot be instantiated. <br> */
        class NXOPENCPPEXPORT PmopToolAxisCiBuilder : public TaggedObject
        {
            /** Available types for pmop tool axis type */
            public: enum ToolAxisTypes
            {
                ToolAxisTypesNone/** +ZM axis */,
                ToolAxisTypesVector/** Specify Vector */,
                ToolAxisTypesNormalToPart/** Normal To Floor Face */,
                ToolAxisTypesNormalToFirstFace/** Normal To First Face */
            };

            private: friend class  _PmopToolAxisCiBuilderBuilder;
            protected: PmopToolAxisCiBuilder();
            /**Returns  the tool axis type  <br> License requirements : None */
            public: NXOpen::CAM::PmopToolAxisCiBuilder::ToolAxisTypes ToolAxis
            (
            );
            /**Sets  the tool axis type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetToolAxis
            (
                NXOpen::CAM::PmopToolAxisCiBuilder::ToolAxisTypes newValue /** the tool axis type */
            );
            /**Returns  the tool axis vector  <br> License requirements : None */
            public: NXOpen::SmartObject * FixedVector
            (
            );
            /**Sets  the tool axis vector  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetFixedVector
            (
                NXOpen::SmartObject * newValue /** new value */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif

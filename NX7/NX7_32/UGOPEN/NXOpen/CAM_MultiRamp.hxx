#ifndef NXOpen_CAM_MULTIRAMP_HXX_INCLUDED
#define NXOpen_CAM_MULTIRAMP_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MultiRamp.ja
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
#include <NXOpen/CAM_MultiRamp.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class MultiRamp;
    }
    namespace CAM
    {
        class InheritableDoubleBuilder;
    }
    namespace CAM
    {
        class _MultiRampBuilder;
        /**
            Represents a @link CAM::MultiRamp CAM::MultiRamp@endlink 
            */
        class NXOPENCPPEXPORT MultiRamp : public TaggedObject
        {
            /** the multi ramp pattern types */
            public: enum Types
            {
                TypesNone/** Multi ramp pattern: None */,
                TypesRampOutOrInOnly/** Multi ramp pattern: Ramp out/in only" */,
                TypesRampOutOrIn/** Multi ramp pattern: Ramp out/in */
            };

            private: friend class  _MultiRampBuilder;
            protected: MultiRamp();
            /**Returns  the multi ramp pattern  <br> License requirements : None */
            public: NXOpen::CAM::MultiRamp::Types Pattern
            (
            );
            /**Sets  the multi ramp pattern  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetPattern
            (
                NXOpen::CAM::MultiRamp::Types multiRampPattern /** the multi ramp pattern */
            );
            /**Returns  the maximum ramp length  <br> License requirements : None */
            public: NXOpen::CAM::InheritableDoubleBuilder * MaxRampLength
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif

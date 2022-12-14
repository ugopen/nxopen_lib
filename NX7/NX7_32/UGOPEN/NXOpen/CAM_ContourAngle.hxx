#ifndef NXOpen_CAM_CONTOURANGLE_HXX_INCLUDED
#define NXOpen_CAM_CONTOURANGLE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ContourAngle.ja
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
#include <NXOpen/CAM_ContourAngle.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class ContourAngle;
    }
    namespace CAM
    {
        class _ContourAngleBuilder;
        /**
            Represents a @link CAM::ContourAngle CAM::ContourAngle@endlink 
            */
        class NXOPENCPPEXPORT ContourAngle : public TaggedObject
        {
            private: friend class  _ContourAngleBuilder;
            protected: ContourAngle();
            /**Returns  the minimum face angle  <br> License requirements : None */
            public: double Minimum
            (
            );
            /**Sets  the minimum face angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetMinimum
            (
                double minAngle /** the minimum face angle */
            );
            /**Returns  the maximum face angle  <br> License requirements : None */
            public: double Maximum
            (
            );
            /**Sets  the maximum face angle  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetMaximum
            (
                double maxAngle /** the maximum face angle */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif

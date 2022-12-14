#ifndef NXOpen_MOTION_COUPLERBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_COUPLERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_CouplerBuilder.ja
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
#include <NXOpen/Motion_MotionBuilder.hxx>
#include <NXOpen/Motion_CouplerBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class CouplerBuilder;
    }
    namespace Motion
    {
        class MotionBuilder;
    }
    namespace Motion
    {
        class SelectJoint;
    }
    class Point;
    namespace Motion
    {
        class _CouplerBuilderBuilder;
        /** Represents a @link Motion::CouplerBuilder Motion::CouplerBuilder@endlink   <br> This is an abstract class, and cannot be created. <br> */
        class NXOPENCPPEXPORT CouplerBuilder : public Motion::MotionBuilder
        {
            private: friend class  _CouplerBuilderBuilder;
            protected: CouplerBuilder();
            /**Returns  the first joint  <br> License requirements : None */
            public: NXOpen::Motion::SelectJoint * FirstJoint
            (
            );
            /**Returns  the second joint  <br> License requirements : None */
            public: NXOpen::Motion::SelectJoint * SecondJoint
            (
            );
            /**Returns  the contact point  <br> License requirements : None */
            public: NXOpen::Point * ContactPoint
            (
            );
            /**Sets  the contact point  <br> License requirements : None */
            public: void SetContactPoint
            (
                NXOpen::Point * contactPt /** contact pt */ 
            );
            /**Returns  the ratio  <br> License requirements : None */
            public: double Ratio
            (
            );
            /**Sets  the ratio  <br> License requirements : None */
            public: void SetRatio
            (
                double ratio /** ratio */ 
            );
            /**Returns  the name  <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name  <br> License requirements : None */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif

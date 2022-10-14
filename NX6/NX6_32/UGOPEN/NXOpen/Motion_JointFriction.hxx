#ifndef NXOpen_MOTION_JOINTFRICTION_HXX_INCLUDED
#define NXOpen_MOTION_JOINTFRICTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_JointFriction.ja
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
    namespace Motion
    {
        class JointFriction;
    }
    namespace Motion
    {
        class JointFrictionAdams;
    }
    namespace Motion
    {
        class JointFrictionRecurDyn;
    }
    namespace Motion
    {
        class _JointFrictionBuilder;
        /** Represents a joint friction object */
        class NXOPENCPPEXPORT JointFriction : public TaggedObject
        {
            private: friend class  _JointFrictionBuilder;
            protected: JointFriction();
            /**Returns  the option of included  <br> License requirements : mechanisms ("MECHANISMS") */
            public: bool Enable
            (
            );
            /**Sets  the option of included  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetEnable
            (
                bool enable /** enable */ 
            );
            /**Returns  the joint adams friction  <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::JointFrictionAdams * AdamsFriction
            (
            );
            /**Returns  the joint recurdyn friction  <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::JointFrictionRecurDyn * RecurDynFriction
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
#ifndef NXOpen_DIE_CONNECTPROFILEPARENTBUILDER_HXX_INCLUDED
#define NXOpen_DIE_CONNECTPROFILEPARENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_ConnectProfileParentBuilder.ja
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
#include <NXOpen/Die.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Die
    {
        class ConnectProfileParentBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class IProfile;
    namespace Die
    {
        class _ConnectProfileParentBuilderBuilder;
        /** Represents a Die Connecting Profile sub feature.  <br> This sub feature is created via the main feature builder. <br> */
        class NXOPENCPPEXPORT ConnectProfileParentBuilder : public Features::FeatureBuilder
        {
            private: friend class  _ConnectProfileParentBuilderBuilder;
            protected: ConnectProfileParentBuilder();
            /** Sets the connecting profiles of the steel insert  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetProfile
            (
                NXOpen::Die::DirectionOption direction /** profile direction */,
                const std::vector<NXOpen::IProfile *> & profileEntries /** profile entries */
            );
            /** Gets the connecting profiles of the steel insert  @return  profile entries  <br> License requirements : ug_die_design ("Die Design") */
            public: std::vector<NXOpen::IProfile *> GetProfile
            (
                NXOpen::Die::DirectionOption* direction /** profile direction */
            );
            /**Sets  the design status of  die connecting profiles  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDesignStatus
            (
                bool designStatus /** design status */ 
            );
            /**Returns  the design status of  die connecting profiles  <br> License requirements : ug_die_design ("Die Design") */
            public: bool DesignStatus
            (
            );
            /**Returns  the build status of die connecting profiles  <br> License requirements : ug_die_design ("Die Design") */
            public: NXOpen::Die::DieBuildStatusOption BuildStatus
            (
            );
            /**Sets  the display status of die pierce holes  <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDisplayStatus
            (
                bool displayStatus /** display status */ 
            );
            /**Returns  the display status of die pierce holes  <br> License requirements : ug_die_design ("Die Design") */
            public: bool DisplayStatus
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
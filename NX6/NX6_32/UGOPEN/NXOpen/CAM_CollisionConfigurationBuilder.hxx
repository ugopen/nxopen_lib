#ifndef NXOpen_CAM_COLLISIONCONFIGURATIONBUILDER_HXX_INCLUDED
#define NXOpen_CAM_COLLISIONCONFIGURATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_CollisionConfigurationBuilder.ja
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
#include <NXOpen/CAM_CollisionConfigurationBuilder.hxx>
#include <NXOpen/CAM_CollisionPairBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class CollisionConfigurationBuilder;
    }
    class Builder;
    namespace CAM
    {
        class CollisionPairBuilder;
    }
    namespace CAM
    {
        class _CollisionConfigurationBuilderBuilder;
        /**
            Represents a @link CAM::CollisionConfigurationBuilder CAM::CollisionConfigurationBuilder@endlink 
             <br> This is an abstract class, and cannot be instantiated. <br> */
        class NXOPENCPPEXPORT CollisionConfigurationBuilder : public Builder
        {
            private: friend class  _CollisionConfigurationBuilderBuilder;
            protected: CollisionConfigurationBuilder();
            /** Creates a list item  @return  collision pair builder <br> License requirements : None */
            public: NXOpen::CAM::CollisionPairBuilder * CreateCollisionPairBuilder
            (
                int position /** position */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif

#ifndef NXOpen_CAM_PROFILESTRATEGY_HXX_INCLUDED
#define NXOpen_CAM_PROFILESTRATEGY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_ProfileStrategy.ja
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
#include <NXOpen/CAM_ProfileStrategy.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class ProfileStrategy;
    }
    namespace CAM
    {
        class _ProfileStrategyBuilder;
        /** Represents profile strategy */
        class NXOPENCPPEXPORT ProfileStrategy : public TaggedObject
        {
            /** the profile strategy options */
            public: enum Types
            {
                TypesDiametersOnly/** Profile strategy: Diameters Only */,
                TypesFacesOnly/** Profile strategy: Faces Only */,
                TypesDiametersThenFaces/** Profile strategy: Diameters First, Then Faces */,
                TypesFacesThenDiameters/** Profile strategy: Faces First, Then Diameters */,
                TypesTowardsCorner/** Profile strategy: Towards Corner */,
                TypesAwayFromCorner/** Profile strategy: Away from Corner */,
                TypesDownOnly/** Profile strategy: Down Only */,
                TypesFinishAll/** Profile strategy: Finish All */
            };

            private: friend class  _ProfileStrategyBuilder;
            protected: ProfileStrategy();
            /**Returns  the profile strategy  <br> License requirements : None */
            public: NXOpen::CAM::ProfileStrategy::Types Type
            (
            );
            /**Sets  the profile strategy  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetType
            (
                NXOpen::CAM::ProfileStrategy::Types type /** the profile strategy */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
#ifndef NXOpen_FEATURES_HUMAN_HXX_INCLUDED
#define NXOpen_FEATURES_HUMAN_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_Human.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Features_Feature.hxx>
#include <NXOpen/HumanReachZone.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class Human;
    }
    namespace Features
    {
        class Feature;
    }
    class HumanReachZone;
    class NXObject;
    namespace Features
    {
        class _HumanBuilder;
        /** Represents a human feature. */
        class NXOPENCPPEXPORT Human : public Features::Feature
        {
            private: friend class  _HumanBuilder;
            protected: Human();
            /** Create a new ReachZone object for human feature  <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
            public: void CreateReachZone
            (
                int* index /** index of the reach zone */,
                NXOpen::HumanReachZone ** reach_zone /** reach zone */
            );
            /** Find the selected ReachZone object for human feature  @return  reach zone  <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
            public: NXOpen::HumanReachZone * FindSelectedReachZone
            (
                NXOpen::NXObject * reach_zone_geom /** reach zone geom tag */
            );
            /** Delete a ReachZone object from human feature  <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
            public: void DeleteNthReachZone
            (
                int index /** index of the reach zone */
            );
            /** Get a ReachZone object from human feature  @return  reach zone  <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
            public: NXOpen::HumanReachZone * GetNthReachZone
            (
                int index /** index of the reach zone */
            );
            /** Get a reach zone numbers of a human feature  @return  numbers of reach zones  <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
            public: int GetNumReachZones
            (
            );
            /** Find ReachZone object in a human feature by reach zone name  @return  reach zone  <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
            public: NXOpen::HumanReachZone * FindNamedReachZone
            (
                const NXString & reach_zone_name /** reach zone name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Check whether human is correct compared with user defined base human  <br> License requirements : solid_modeling ("SOLIDS MODELING"), ug_human ("Human Modelling") */
            public: void CheckHuman
            (
                NXOpen::Features::Human * base_human /** User defined base human used for check */,
                bool check_human_data /** Flag of check human data */,
                bool check_segment /** Flag of check human segment position */,
                bool check_expression /** Flag of check human expression */,
                bool check_reach_zone /** Flag of check human reach zone */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif

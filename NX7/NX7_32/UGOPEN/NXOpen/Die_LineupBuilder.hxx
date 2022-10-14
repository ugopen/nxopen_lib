#ifndef NXOpen_DIE_LINEUPBUILDER_HXX_INCLUDED
#define NXOpen_DIE_LINEUPBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_LineupBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Die
    {
        class LineupBuilder;
    }
    class Body;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace Die
    {
        class _LineupBuilderBuilder;
        /** Represents a Lineup feature builder  <br> To create a new instance of this class, use @link Die::DieCollection::Lineup Die::DieCollection::Lineup@endlink  <br> */
        class NXOPENCPPEXPORT LineupBuilder : public Features::FeatureBuilder
        {
            private: friend class  _LineupBuilderBuilder;
            protected: LineupBuilder();
            /** Sets the product sheet bodies of the lineup  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetProductBodies
            (
                const std::vector<NXOpen::Body *> & objects /** objects */ 
            );
            /** Gets the product sheet bodies of the lineup  @return   <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: std::vector<NXOpen::Body *> GetProductBodies
            (
            );
            /** Sets the detailed description of the lineup  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetDetails
            (
                std::vector<NXString> & strings /** detail strings   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Gets the detailed description of the lineup  @return  detail strings  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: std::vector<NXString> GetDetails
            (
            );
            /**Returns  the origin of the lineup  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: NXOpen::Point3d Origin
            (
            );
            /**Sets  the origin of the lineup  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetOrigin
            (
                const NXOpen::Point3d & origin /** origin */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
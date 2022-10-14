#ifndef NXOpen_FEATURES_TRIMBODYBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_TRIMBODYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_TrimBodyBuilder.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class TrimBodyBuilder;
    }
    class Body;
    namespace Features
    {
        class FeatureBuilder;
    }
    class NXObject;
    namespace Features
    {
        class _TrimBodyBuilderBuilder;
        /** Represents the trim body feature builder.  <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateTrimBodyBuilder Features::FeatureCollection::CreateTrimBodyBuilder@endlink  <br> */
        class NXOPENCPPEXPORT TrimBodyBuilder : public Features::FeatureBuilder
        {
            /** Represents the trim direction */
            public: enum DirectionType
            {
                DirectionTypePositiveNormal = 1/** positive normal */ ,
                DirectionTypeNegativeNormal = -1/** negative normal */ ,
                DirectionTypeInvalid/** invalid */ 
            };

            private: friend class  _TrimBodyBuilderBuilder;
            protected: TrimBodyBuilder();
            /** Returns the target bodies of the trim body operation.  @return  Target bodies  <br> License requirements : None */
            public: std::vector<NXOpen::Body *> GetTargets
            (
            );
            /**Returns  the tool of the trim body feature
                 <br> License requirements : None */
            public: NXOpen::NXObject * Tool
            (
            );
            /**Returns  the trim direction of the trim body feature  <br> License requirements : None */
            public: NXOpen::Features::TrimBodyBuilder::DirectionType TrimDirection
            (
            );
            /** Sets the targets for a trim body opearation. Any existing targets will
                  * be erased.  For create multiple target bodies can be set. 
                  * This method will throw an exception during edit operation as the bodies
                  * can not be changed at that point.
                   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetTargets
            (
                const std::vector<NXOpen::Body *> & target /** target bodies */
            );
            /** Adds a target body during create. A new target will be added to the 
                 *  trim body operation. During edit, an exception will be thrown as 
                 *  the target can not be modified during edit.
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void AddTarget
            (
                NXOpen::Body * target /** Body to add */
            );
            /** Removes a target body is removed from trim body in create.
                 *  During edit, an exception will be thrown as 
                 *  target body can not be changed during edit.
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void RemoveTarget
            (
                NXOpen::Body * target /** Body to remove */
            );
            /**Sets  the tool of the trim body feature
                 <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetTool
            (
                NXOpen::NXObject * tool /** Set trim body tool */
            );
            /**Sets  the trim direction of the trim body feature  <br> License requirements : None */
            public: void SetTrimDirection
            (
                NXOpen::Features::TrimBodyBuilder::DirectionType direction /** Set trim direction */
            );
            /** Reverse the trim direction of trim body feature
                  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void Reverse
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
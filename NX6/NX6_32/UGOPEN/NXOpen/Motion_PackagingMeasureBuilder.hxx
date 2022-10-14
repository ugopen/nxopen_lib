#ifndef NXOpen_MOTION_PACKAGINGMEASUREBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_PACKAGINGMEASUREBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_PackagingMeasureBuilder.ja
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
#include <NXOpen/Motion_PackagingBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class PackagingMeasureBuilder;
    }
    class DisplayableObject;
    namespace Motion
    {
        class PackagingBuilder;
    }
    namespace Motion
    {
        class _PackagingMeasureBuilderBuilder;
        /** This is the builder class to create or edit a Measure object. <br> To create a new instance of this class, use @link Motion::PackagingCollection::CreateMeasureBuilder Motion::PackagingCollection::CreateMeasureBuilder@endlink  <br> */
        class NXOPENCPPEXPORT PackagingMeasureBuilder : public Motion::PackagingBuilder
        {
            /** Measure type */
            public: enum MeasureType
            {
                MeasureTypeMinimumDistance/** Measure minimum distance between objects. */,
                MeasureTypeAngle/** Measure angle between lines or linear edges. */
            };

            /** Measure condition */
            public: enum MeasureCondition
            {
                MeasureConditionLessThan/** Stop event defined by minimum measurement
                                                                                          less than threshold value. */,
                MeasureConditionGreaterThan/** Stop event defined by minimum measurement
                                                                                          greater than threshold value. */,
                MeasureConditionEqualTo/** Stop event defined by minimum measurement
                                                                                          equal to threshold (target) value. */
            };

            private: friend class  _PackagingMeasureBuilderBuilder;
            protected: PackagingMeasureBuilder();
            /** Returns the geometry list 2 of @link  Motion::PackagingMeasure   Motion::PackagingMeasure @endlink  object.
                    Measure can have one or two lists defined.  If the user
                    defines two lists, then measurements will be done between
                    each object in list 1 against each object in list 2.  @return   <br> License requirements : mechanisms ("MECHANISMS") */
            public: std::vector<NXOpen::DisplayableObject *> GetList2
            (
            );
            /** Sets the geometry list 2.  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetList2
            (
                const std::vector<NXOpen::DisplayableObject *> & list2 /** list2 */ 
            );
            /**Returns  the Measure type defined at @link  Motion::PackagingMeasureBuilder::MeasureType   Motion::PackagingMeasureBuilder::MeasureType @endlink   <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::PackagingMeasureBuilder::MeasureType MsType
            (
            );
            /**Sets  the Measure type defined at @link  Motion::PackagingMeasureBuilder::MeasureType   Motion::PackagingMeasureBuilder::MeasureType @endlink   <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetMsType
            (
                NXOpen::Motion::PackagingMeasureBuilder::MeasureType mType /** m type */ 
            );
            /**Returns  theMmeasure condition defined at @link  Motion::PackagingMeasureBuilder::MeasureCondition   Motion::PackagingMeasureBuilder::MeasureCondition @endlink   <br> License requirements : mechanisms ("MECHANISMS") */
            public: NXOpen::Motion::PackagingMeasureBuilder::MeasureCondition Condition
            (
            );
            /**Sets  theMmeasure condition defined at @link  Motion::PackagingMeasureBuilder::MeasureCondition   Motion::PackagingMeasureBuilder::MeasureCondition @endlink   <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetCondition
            (
                NXOpen::Motion::PackagingMeasureBuilder::MeasureCondition condition /** condition */ 
            );
            /**Returns  the Measure threshold value  <br> License requirements : mechanisms ("MECHANISMS") */
            public: double Threshold
            (
            );
            /**Sets  the Measure threshold value  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetThreshold
            (
                double threshold /** threshold */ 
            );
            /**Returns  the Measure tolerance value  <br> License requirements : mechanisms ("MECHANISMS") */
            public: double Tolerance
            (
            );
            /**Sets  the Measure tolerance value  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetTolerance
            (
                double tolerance /** tolerance */ 
            );
            /**Returns  the Stop_On_Event flag of @link  Motion::PackagingMeasure   Motion::PackagingMeasure @endlink  object  <br> License requirements : mechanisms ("MECHANISMS") */
            public: bool StopOnEvent
            (
            );
            /**Sets  the Stop_On_Event flag of @link  Motion::PackagingMeasure   Motion::PackagingMeasure @endlink  object  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetStopOnEvent
            (
                bool stopOnEvent /** stop on event */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
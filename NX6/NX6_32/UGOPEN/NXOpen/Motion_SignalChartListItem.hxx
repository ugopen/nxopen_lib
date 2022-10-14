#ifndef NXOpen_MOTION_SIGNALCHARTLISTITEM_HXX_INCLUDED
#define NXOpen_MOTION_SIGNALCHARTLISTITEM_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_SignalChartListItem.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/Motion_SignalChartListItem.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class SignalChartListItem;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Motion
    {
        class MotionSensor;
    }
    namespace Motion
    {
        class _SignalChartListItemBuilder;
        /** 
            Represents a SignalChartListItem,
            List Item inside a SignalChartBuilder 
             <br> To create a new instance of this class, use @link Motion::SignalChartCollection::CreateSignalChartListItem Motion::SignalChartCollection::CreateSignalChartListItem@endlink  <br> */
        class NXOPENCPPEXPORT SignalChartListItem : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            /** time sensor  */
            public: enum Timer
            {
                TimerTimer/** Timer */,
                TimerAbsoluteTime/** Absolute time */
            };

            /** signal chart list item condition  */
            public: enum Condition
            {
                ConditionLessThan/** Less than */,
                ConditionGreaterThan/** Greater than */
            };

            private: friend class  _SignalChartListItemBuilder;
            protected: SignalChartListItem();
            /**Returns  the sensor  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: NXOpen::Motion::MotionSensor * Sensor
            (
            );
            /**Sets  the sensor  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: void SetSensor
            (
                NXOpen::Motion::MotionSensor * sensor /** sensor */ 
            );
            /**Returns  the time sensor  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: NXOpen::Motion::SignalChartListItem::Timer TimeSensor
            (
            );
            /**Sets  the time sensor  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: void SetTimeSensor
            (
                NXOpen::Motion::SignalChartListItem::Timer timeSensor /** timesensor */ 
            );
            /**Returns  the event condition  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: NXOpen::Motion::SignalChartListItem::Condition EventCondition
            (
            );
            /**Sets  the event condition  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: void SetEventCondition
            (
                NXOpen::Motion::SignalChartListItem::Condition condition /** condition */ 
            );
            /**Returns  the threshold  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: double Threshold
            (
            );
            /**Sets  the threshold  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: void SetThreshold
            (
                double threshold /** threshold */ 
            );
            /**Returns  the delay time  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: double DelayTime
            (
            );
            /**Sets  the delay time  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: void SetDelayTime
            (
                double delayTime /** delaytime */ 
            );
            /**Returns  the siganl  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: double Signal
            (
            );
            /**Sets  the siganl  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: void SetSignal
            (
                double signal /** signal */ 
            );
            /**Returns  the always evaluated  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: bool AlwaysEvaluated
            (
            );
            /**Sets  the always evaluated  <br> License requirements : nx_motion_motor ("NX Motion Motor") */
            public: void SetAlwaysEvaluated
            (
                bool alwaysEvaluated /** alwaysevaluated */ 
            );
            /** Returns true if the inputs to the component are sufficient for 
                        commit to be called.  For example, if the component requires
                        you to set some property, this method will return false if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: virtual bool Validate
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
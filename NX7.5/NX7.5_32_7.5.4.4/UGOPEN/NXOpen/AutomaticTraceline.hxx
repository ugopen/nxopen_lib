#ifndef NXOpen_AUTOMATICTRACELINE_HXX_INCLUDED
#define NXOpen_AUTOMATICTRACELINE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     AutomaticTraceline.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Traceline.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class AutomaticTraceline;
    class Direction;
    class Point;
    class Traceline;
    class _AutomaticTracelineBuilder;
    class AutomaticTracelineImpl;
    /** Represents an automatic traceline. This type of traceline has its shape
        automatically derived from its defining properties. 
     <br> No creator defined due to apiwrap problems <br> */
    class NXOPENCPPEXPORT  AutomaticTraceline : public Traceline
    {
        /** Controls the mode used when evaluating an automatic traceline */
        public: enum ModeOption
        {
            ModeOptionEvaluate/** Evaluate which mode to use */,
            ModeOptionOrientation/** Align with orientation */,
            ModeOptionInfer/** Infer orientation from start and end directions */
        };

        private: AutomaticTracelineImpl * m_automatictraceline_impl;
        private: friend class  _AutomaticTracelineBuilder;
        protected: AutomaticTraceline();
        public: ~AutomaticTraceline();
        /**Returns  the start point of the traceline  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
        public: NXOpen::Point * StartPoint
        (
        );
        /**Sets  the start point of the traceline  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
        public: void SetStartPoint
        (
            NXOpen::Point * point /** New start point */
        );
        /**Returns  the start direction of the traceline  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
        public: NXOpen::Direction * StartDirection
        (
        );
        /**Sets  the start direction of the traceline  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
        public: void SetStartDirection
        (
            NXOpen::Direction * direction /** New start direction */
        );
        /**Returns  the end point of the traceline  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
        public: NXOpen::Point * EndPoint
        (
        );
        /**Sets  the end point of the traceline  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
        public: void SetEndPoint
        (
            NXOpen::Point * point /** New end point */
        );
        /**Returns  the end direction of the traceline  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
        public: NXOpen::Direction * EndDirection
        (
        );
        /**Sets  the end direction of the traceline  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
        public: void SetEndDirection
        (
            NXOpen::Direction * direction /** New end direction */
        );
        /**Returns  the orientation of the traceline  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
        public: NXOpen::Matrix3x3 Orientation
        (
        );
        /**Sets  the orientation of the traceline  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
        public: void SetOrientation
        (
            const NXOpen::Matrix3x3 & orientation /** New orientation */
        );
        /**Returns  the mode of the traceline  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
        public: NXOpen::AutomaticTraceline::ModeOption Mode
        (
        );
        /**Sets  the mode of the traceline  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
        public: void SetMode
        (
            NXOpen::AutomaticTraceline::ModeOption mode /** New mode */
        );
        /**Returns  the solution used in the traceline  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
        public: int Solution
        (
        );
        /**Sets  the solution used in the traceline  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
        public: void SetSolution
        (
            int solution /** New solution to use */
        );
        /**Returns  the start offset of the traceline  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
        public: double StartOffset
        (
        );
        /**Sets  the start offset of the traceline  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
        public: void SetStartOffset
        (
            double startOffset /** New start offset */
        );
        /**Returns  the end offset of the traceline  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
        public: double EndOffset
        (
        );
        /**Sets  the end offset of the traceline  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
        public: void SetEndOffset
        (
            double endOffset /** New end offset */
        );
        /** Gets the segment constraints of the traceline  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
        public: void GetSegmentConstraints
        (
            std::vector<int> & segmentIndices /** Segment indices */,
            std::vector<double> & segmentLengths /** Segment lengths */
        );
        /** Sets the segment constraints of the traceline  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
        public: void SetSegmentConstraints
        (
            const std::vector<int> & segmentIndices /** Segment indices */,
            const std::vector<double> & segmentLengths /** Segment lengths */
        );
        /** Removes the segment constraint from the traceline  <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
        public: void RemoveSegmentConstraint
        (
            int segmentIndex /** Segment index */
        );
    };
}
#undef EXPORTLIBRARY
#endif

#ifndef NXOpen_SKETCHEVALUATOR_HXX_INCLUDED
#define NXOpen_SKETCHEVALUATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchEvaluator.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class SketchEvaluator;
    class Curve;
    class Section;
    class _SketchEvaluatorBuilder;
    class SketchEvaluatorImpl;
    /** Represents a sketch-on-path evaluator. It allows an application to evaluate
     *  a section and a sketch-on-path at specific path locations.
      <br> To create a new instance of this class, use @link SketchEvaluatorCollection::Create SketchEvaluatorCollection::Create@endlink  <br> */
    class NXOPENCPPEXPORT  SketchEvaluator : public TaggedObject
    {
        private: SketchEvaluatorImpl * m_sketchevaluator_impl;
        private: friend class  _SketchEvaluatorBuilder;
        protected: SketchEvaluator();
        public: ~SketchEvaluator();
        /**Sets  the master section. Variational sweep accepts 
                sections created ONLY on in the context of a Sketch on Path. 
                Make sure this section is coming from sketch curves created using
                the sketch on path feature. The application should not mutate the
                section if evaluator object is created with vsweep feature. 
                Return code : 0 : no error,
                VARSWEEP_SKETCH_NOT_ON_PATH : on an error condition
               <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetSection
        (
            NXOpen::Section * section /** master section */
        );
        /**Sets  the distance tolerance <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetDistanceTolerance
        (
            double distanceTolerance /** distance tolerance */ 
        );
        /**Sets  the angle tolerance [degrees] <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetAngularTolerance
        (
            double angleTolerance /** angle tolerance */ 
        );
        /**Sets  the option which allows automatic create of non-associative UG curves
              *  for the sketch evaluation.
              *
              * Note: [1] This property is only used for a call to method "EvaluateOneSketch".
              *       [2] this property is defaulted to false.
               <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetCreateCurveOption
        (
            bool createCurveOption /** create curve option */ 
        );
        /**Returns  the option which allows automatic create of non-associative UG curves
              *  for the sketch evaluation.
              *
              * Note: [1] This property is only used for a call to method "EvaluateOneSketch".
              *       [2] this property is defaulted to false.
               <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: bool CreateCurveOption
        (
        );
        /**Sets  the option which allows the automatic conversion of curves
              *  into an approximation of sorted sequence of arcs and lines.
              *  This option only convert curves that are not arcs and lines. 
              *  
              * Note: [1] This property is only used for a call to method "EvaluateOneSketch".
              *       [2] This property is defaulted to false.
               <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetSimplifyCurveOption
        (
            bool simplifySplineOption /** the simplify spline option */
        );
        /**Returns  the option which allows the automatic conversion of curves
              *  into an approximation of sorted sequence of arcs and lines.
              *  This option only convert curves that are not arcs and lines. 
              *  
              * Note: [1] This property is only used for a call to method "EvaluateOneSketch".
              *       [2] This property is defaulted to false.
               <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: bool SimplifyCurveOption
        (
        );
        /** Work-horse method that evaluates the master section and its sketch on path
              * at a specific path location.
              *
              *  Pre-conditions :
              *     [1]  A master section must have been registered with call to mutator set_section()
              *          or the sketch evaluator must be constructed with an existing feature.
              *
              *     [2] The application should edit the properties "CreateCurveOption", "SimplifyCurveOption"
              *         as needed before calling this method.
              *
              *  Post-conditions:
              *     [3] If the "create curve" option is set to false, the output curves should be 
              *         accessed right away.
              *         The lifetime of these curves is as long as the next call to method "EvaluateOneSketch".
              *
              *     [4] If the application wants to evaluate the same sketch at multiple path location,
              *         it should make several consecutive calls to method "EvaluateOneSketch".
              *         At the end of the operation, the application must call method "Destroy".
              *
              *     [5] If the "simplify curve" option is false, the number of curves will always be the same.
              *
              *     [6] The design of this functionality has not been tailored for master section
              *         with multiple loops. If the master section has multiple loops, all the curves
              *         will be returned in the order of the loops in the section. 
              *      
              *     [7] Method "EvaluateOneSketch" changes the state of the sketch on path. Therefore,
              *         the part is temporarily in out of date state. The application should leverage
              *         the NX undo mechanism to reset the state to its original. An alternative solution
              *         is to suppress and unsuppress the sketch on path and variational sweep features
              *         involved.
               @return   <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: std::vector<NXOpen::Curve *> EvaluateOneSketch
        (
            double pathLocation /** input path arc length percent to evaluate at. */
        );
        /**Returns  the distance tolerance <br> License requirements : None */
        public: double DistanceTolerance
        (
        );
        /**Returns  the angle tolerance [degrees] <br> License requirements : None */
        public: double AngularTolerance
        (
        );
        /**Returns  the master section. Variational sweep accepts 
                sections created ONLY on in the context of a Sketch on Path. 
                Make sure this section is coming from sketch curves created using
                the sketch on path feature. The application should not mutate the
                section if evaluator object is created with vsweep feature. 
                Return code : 0 : no error,
                VARSWEEP_SKETCH_NOT_ON_PATH : on an error condition
               <br> License requirements : None */
        public: NXOpen::Section * Section
        (
        );
        /** Deletes the sketch evaluator, and cleans up any objects created by the it <br> License requirements : None */
        public: void Destroy
        (
        );
    };
}
#undef EXPORTLIBRARY
#endif

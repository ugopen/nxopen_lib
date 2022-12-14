#ifndef NXOpen_DIE_COMPENSATEROUGHDATABUILDER_HXX_INCLUDED
#define NXOpen_DIE_COMPENSATEROUGHDATABUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_CompensateRoughDataBuilder.ja
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
#include <NXOpen/Die_CompensateRoughDataBuilder.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_die_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Die
    {
        class CompensateRoughDataBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    class ScCollector;
    class Section;
    class SelectBodyList;
    namespace Die
    {
        class _CompensateRoughDataBuilderBuilder;
        class CompensateRoughDataBuilderImpl;
        /**
            Represents a @link NXOpen::Die::CompensateRoughDataBuilder NXOpen::Die::CompensateRoughDataBuilder@endlink . This class is used to edit
            and create a Compensate Rough Curve or Compensate Rough Sheet feature.
             <br> To create a new instance of this class, use @link NXOpen::Die::DieCollection::CompensateRoughData  NXOpen::Die::DieCollection::CompensateRoughData @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        AngleTolerance </td> <td> 
         
        0.5 </td> </tr> 

        <tr><td> 
         
        Approximation </td> <td> 
         
        Coarse </td> </tr> 

        <tr><td> 
         
        DistanceTolerance </td> <td> 
         
        0.0254 (millimeters part), 0.001 (inches part) </td> </tr> 

        <tr><td> 
         
        JoinOutputCurves </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        MaximumGap </td> <td> 
         
        5.0 (millimeters part), 0.2 (inches part) </td> </tr> 

        <tr><td> 
         
        ModifyInputSheet </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_DIEEXPORT  CompensateRoughDataBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** Settings for the type of data being compensated. */
            public: enum Types
            {
                TypesSheetBody/** Sheet bodies being compensated. */,
                TypesCurve/** Curves being compensated. */
            };

            /** Settings for the amount of approximation to perform. */
            public: enum ApproximationType
            {
                ApproximationTypeCoarse/** Perform a coarse approximation. */,
                ApproximationTypeRough/** Perform a rough approximation. */,
                ApproximationTypeFine/** Perform a fine approximation. */,
                ApproximationTypeExact/** Perform no approximation. */
            };

            private: CompensateRoughDataBuilderImpl * m_compensateroughdatabuilder_impl;
            private: friend class  _CompensateRoughDataBuilderBuilder;
            protected: CompensateRoughDataBuilder();
            public: ~CompensateRoughDataBuilder();
            /**Returns  the curve collector containing the curves that will be approximated. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * CurveCollector
            (
            );
            /**Returns  the sheet bodies that will be approximated. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBodyList * SheetBodies
            (
            );
            /**Returns  the faces to project the output curves onto. If faces are selected then the output curves will be 
                        projected normal to these faces. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * ProjectToFaces
            (
            );
            /**Returns  the join output curves setting, true indicates that the output curves will be joined
                        into a single curve. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool JoinOutputCurves
            (
            );
            /**Sets  the join output curves setting, true indicates that the output curves will be joined
                        into a single curve. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetJoinOutputCurves
            (
                bool joinOutputCurves /** joinoutputcurves */ 
            );
            /**Returns  the modify input sheet setting. If true the input sheet will be modified, otherwise
                        a new sheet will be created. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool ModifyInputSheet
            (
            );
            /**Sets  the modify input sheet setting. If true the input sheet will be modified, otherwise
                        a new sheet will be created. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetModifyInputSheet
            (
                bool modifyInputSheet /** modifyinputsheet */ 
            );
            /**Returns  the approximation desired. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Die::CompensateRoughDataBuilder::ApproximationType Approximation
            (
            );
            /**Sets  the approximation desired. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetApproximation
            (
                NXOpen::Die::CompensateRoughDataBuilder::ApproximationType approximation /** approximation */ 
            );
            /**Returns  the distance tolerance. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double DistanceTolerance
            (
            );
            /**Sets  the distance tolerance. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDistanceTolerance
            (
                double distanceTolerance /** distancetolerance */ 
            );
            /**Returns  the angle tolerance. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double AngleTolerance
            (
            );
            /**Sets  the angle tolerance. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetAngleTolerance
            (
                double angleTolerance /** angletolerance */ 
            );
            /**Returns  the maximum gap. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double MaximumGap
            (
            );
            /**Sets  the maximum gap. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetMaximumGap
            (
                double maximumGap /** maximumgap */ 
            );
            /**Returns  the type of input data being supplied. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Die::CompensateRoughDataBuilder::Types Type
            (
            );
            /**Sets  the type of input data being supplied. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetType
            (
                NXOpen::Die::CompensateRoughDataBuilder::Types type /** type */ 
            );
        };
    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif

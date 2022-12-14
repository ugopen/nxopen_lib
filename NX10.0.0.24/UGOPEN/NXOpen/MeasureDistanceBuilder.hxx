#ifndef NXOpen_MEASUREDISTANCEBUILDER_HXX_INCLUDED
#define NXOpen_MEASUREDISTANCEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MeasureDistanceBuilder.ja
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
#include <NXOpen/MeasureDistanceBuilder.hxx>
#include <NXOpen/MeasureBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class MeasureDistanceBuilder;
    class Direction;
    class MeasureBuilder;
    class ScCollector;
    class SelectDisplayableObject;
    class SelectDisplayableObjectList;
    class _MeasureDistanceBuilderBuilder;
    class MeasureDistanceBuilderImpl;
    /**
    Represents a @link MeasureDistanceBuilder MeasureDistanceBuilder@endlink 
     <br> To create a new instance of this class, use @link NXOpen::MeasureManager::CreateMeasureDistanceBuilder  NXOpen::MeasureManager::CreateMeasureDistanceBuilder @endlink  <br> 
     <br>  Created in NX5.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  MeasureDistanceBuilder : public NXOpen::MeasureBuilder
    {
        /** the type of distance measurement */
        public: enum DistanceType
        {
            DistanceTypeDistance/** distance */ ,
            DistanceTypeSmartDistance/** smart distance */ ,
            DistanceTypeProjectedDistance/** projected distance */ ,
            DistanceTypeSmartProjectedDistance/** smart projected distance */ ,
            DistanceTypeScreenDistance/** screen distance */ ,
            DistanceTypeLength/** length */ ,
            DistanceTypeRadius/** radius */ ,
            DistanceTypeDiameter/** diameter */ ,
            DistanceTypePointsOnCurves/** points on curves */ ,
            DistanceTypeRoutingPathLength/** routing path length */ ,
            DistanceTypeBetweenSets/** between sets */ 
        };

        /** the subtype of distance measurement */
        public: enum MeasureType
        {
            MeasureTypeToAPoint/** to apoint */ ,
            MeasureTypeMinimum/** minimum */ ,
            MeasureTypeLocalMinimum/** local minimum */ ,
            MeasureTypeMaximum/** maximum */ ,
            MeasureTypeMinClearance/** min clearance */ ,
            MeasureTypeMaxClearance/** max clearance */ 
        };

        private: MeasureDistanceBuilderImpl * m_measuredistancebuilder_impl;
        private: friend class  _MeasureDistanceBuilderBuilder;
        protected: MeasureDistanceBuilder();
        public: ~MeasureDistanceBuilder();
        /**Returns  the projection vector 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::Direction * ProjectionVector
        (
        );
        /**Sets  the projection vector 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetProjectionVector
        (
            NXOpen::Direction * projectionVector /** projectionvector */ 
        );
        /**Returns  the object1 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SelectDisplayableObject * Object1
        (
        );
        /**Returns  the object2 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SelectDisplayableObject * Object2
        (
        );
        /**Returns  the length objects 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SelectDisplayableObjectList * LengthObjects
        (
        );
        /**Returns  the length collector of objects 
         <br>  Created in NX8.5.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::ScCollector * LengthCollector
        (
        );
        /**Returns  the radius objects 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SelectDisplayableObject * RadiusObjects
        (
        );
        /**Returns  the diameter objects 
         <br>  Created in NX8.5.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SelectDisplayableObject * DiameterObjects
        (
        );
        /**Returns  the set1 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SelectDisplayableObjectList * Set1
        (
        );
        /**Returns  the set2 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SelectDisplayableObjectList * Set2
        (
        );
        /**Returns  the mtype 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::MeasureDistanceBuilder::MeasureType Mtype
        (
        );
        /**Sets  the mtype 
         <br>  Created in NX5.0.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetMtype
        (
            NXOpen::MeasureDistanceBuilder::MeasureType mtype /** mtype */ 
        );
        /**Returns  the exact flag 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : None */
        public: bool IsExact
        (
        );
        /**Sets  the exact flag 
         <br>  Created in NX7.5.0.  <br>  
         <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetExact
        (
            bool isExact /** isexact */ 
        );
        /**Returns  the first collector of objects for distance between two collectors 
         <br>  Created in NX8.5.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::ScCollector * DistanceCollector1
        (
        );
        /**Returns  the second collector of objects for distance between two collectors 
         <br>  Created in NX8.5.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::ScCollector * DistanceCollector2
        (
        );
    };
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

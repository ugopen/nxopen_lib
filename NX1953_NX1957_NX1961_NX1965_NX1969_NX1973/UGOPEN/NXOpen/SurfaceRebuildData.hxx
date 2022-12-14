#ifndef NXOpen_SURFACEREBUILDDATA_HXX_INCLUDED
#define NXOpen_SURFACEREBUILDDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SurfaceRebuildData.ja
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
#include <NXOpen/TransientObject.hxx>
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
    class SurfaceRebuildData;
    class SurfaceRebuildDataImpl;
    /** Represents surface rebuild data structure.  <br> To create a new instance of this class, use @link NXOpen::Features::MeshSurfaceBuilder::NewRebuildData  NXOpen::Features::MeshSurfaceBuilder::NewRebuildData @endlink  <br> 
     <br>  Created in NX4.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  SurfaceRebuildData : public NXOpen::TransientObject
    {
        /** Surface rebuild types. */
        public: enum Type
        {
            TypeNone/** None   */,
            TypeManual/** Manual */,
            TypeAuto/** Auto   */
        };

        private: SurfaceRebuildDataImpl * m_surfacerebuilddata_impl;
        /// \cond NX_NO_DOC 
        public: explicit SurfaceRebuildData(void *ptr);
        /// \endcond 
        /** Dispose transient object. 
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : None */
        public: virtual ~SurfaceRebuildData();
        /**Sets  
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
        public: void SetPrimaryRebuildType
        (
            NXOpen::SurfaceRebuildData::Type primaryRebuildType /** primary rebuild type */ 
        );
        /**Returns  
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
        public: NXOpen::SurfaceRebuildData::Type PrimaryRebuildType
        (
        );
        /**Sets  
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
        public: void SetPrimaryDegree
        (
            int degree /** degree. */
        );
        /**Returns  
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
        public: int PrimaryDegree
        (
        );
        /**Sets  
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
        public: void SetPrimaryMaxDegree
        (
            int maxDegree /** max degree. */
        );
        /**Returns  
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
        public: int PrimaryMaxDegree
        (
        );
        /**Sets  
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
        public: void SetPrimaryMaxSegments
        (
            int maxSegments /** max_segments. */
        );
        /**Returns  
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
        public: int PrimaryMaxSegments
        (
        );
        /**Sets  
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
        public: void SetCrossRebuildType
        (
            NXOpen::SurfaceRebuildData::Type crossRebuildType /** cross rebuild type. */
        );
        /**Returns  
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
        public: NXOpen::SurfaceRebuildData::Type CrossRebuildType
        (
        );
        /**Sets  
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
        public: void SetCrossDegree
        (
            int degree /** degree. */
        );
        /**Returns  
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
        public: int CrossDegree
        (
        );
        /**Sets  
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
        public: void SetCrossMaxDegree
        (
            int maxDegree /** max degree */
        );
        /**Returns  
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
        public: int CrossMaxDegree
        (
        );
        /**Sets  
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
        public: void SetCrossMaxSegments
        (
            int maxSegments /** max_segments. */
        );
        /**Returns  
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
        public: int CrossMaxSegments
        (
        );
        /** Set surface rebubild tolerances. The tolerance array length is 4.
                tolerances[0] -\> G0 tolerance
                tolerances[1] -\> G1 tolerance
                tolerances[2] -\> G2 tolerance
                tolerances[3] -\> Intersection tolerance
            
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
        public: void SetTolerances
        (
            const std::vector<double> & tolerances /** tolerances array. */
        );
        /** Get surface rebubild tolerances. The tolerance array length is 4.
                tolerances[0] -\> G0 tolerance
                tolerances[1] -\> G1 tolerance
                tolerances[2] -\> G2 tolerance
                tolerances[3] -\> Intersection tolerance
             @return  tolerances array. 
         <br>  Created in NX4.0.0.  <br>  
         <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
        public: std::vector<double> GetTolerances
        (
            int numTolerances /** num tolerances */ 
        );
    }; //lint !e1712 default constructor not defined for class  

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

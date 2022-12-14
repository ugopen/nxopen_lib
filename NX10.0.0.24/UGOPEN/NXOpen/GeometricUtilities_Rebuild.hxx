#ifndef NXOpen_GEOMETRICUTILITIES_REBUILD_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_REBUILD_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_Rebuild.ja
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
#include <NXOpen/GeometricUtilities_Rebuild.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_geometricutilities_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace GeometricUtilities
    {
        class Rebuild;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace GeometricUtilities
    {
        class _RebuildBuilder;
        class RebuildImpl;
        /** Represents a @link NXOpen::GeometricUtilities::Rebuild NXOpen::GeometricUtilities::Rebuild@endlink .
            The Rebuild block provides control over the method in which a surface is rebuilt (None, Manual,
            Advanced). Rebuild can be used for both uni-directional and bi-directional rebuild functions. 
            Uni-directional functions require one instance of the rebuild block while bi-directional functions 
            require two instances of the Rebuild block.
            
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  Rebuild : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /**  
                    This enum represents the Rebuild type. 
                    */
            public: enum RebuildTypes
            {
                RebuildTypesNone/** No degree entry or simple integer/enumerable value used to specify the rebuild degree.*/,
                RebuildTypesManual/** Specify the rebuild degree manually. */,
                RebuildTypesAdvanced/** Specify the maximum degree and maximum segments to rebuild.*/,
                RebuildTypesKeepParameterization/** Keep the parameterization */
            };

            /** 
                    This enum represents the degree type when the Rebuild option menu is set to None.
                    */
            public: enum DegreeTypes
            {
                DegreeTypesCubic/** The rebuild degree is cubic. */,
                DegreeTypesQuintic/** The rebuild degree is quintic */
            };

            private: RebuildImpl * m_rebuild_impl;
            private: friend class  _RebuildBuilder;
            protected: Rebuild();
            public: ~Rebuild();
            /**Returns  the rebuild type.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: NXOpen::GeometricUtilities::Rebuild::RebuildTypes RebuildType
            (
            );
            /**Sets  the rebuild type.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: void SetRebuildType
            (
                NXOpen::GeometricUtilities::Rebuild::RebuildTypes rebuildType /** Rebuild Type */
            );
            /**Returns  the degree when rebuild type is none.
                        In general, the degree is limited from 1 to 24. However,degree = 1 will only be used for 
                        Through Curve case to replace the current V-degree option, which can start from 1. 
                        Otherwise the minimum degree should be 2.
                      
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: int Degree
            (
            );
            /**Sets  the degree when rebuild type is none.
                        In general, the degree is limited from 1 to 24. However,degree = 1 will only be used for 
                        Through Curve case to replace the current V-degree option, which can start from 1. 
                        Otherwise the minimum degree should be 2.
                      
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: void SetDegree
            (
                int degree /** Integer Degree */
            );
            /**Returns  the degree type when rebuild type is none. 
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: NXOpen::GeometricUtilities::Rebuild::DegreeTypes DegreeType
            (
            );
            /**Sets  the degree type when rebuild type is none. 
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: void SetDegreeType
            (
                NXOpen::GeometricUtilities::Rebuild::DegreeTypes degreeType /** Degree Type */
            );
            /**Returns  the maximum degree when rebuild type is advanced. 
                        The maximum degree value is limited from 2 to 24.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: int MaximumDegree
            (
            );
            /**Sets  the maximum degree when rebuild type is advanced. 
                        The maximum degree value is limited from 2 to 24.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: void SetMaximumDegree
            (
                int maximumDegree /** Maximum Degree */
            );
            /**Returns  the maximum segments when rebuild type is advanced. 
                        The maximum segments value is limited from 1 to 1000.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: int MaximumSegments
            (
            );
            /**Sets  the maximum segments when rebuild type is advanced. 
                        The maximum segments value is limited from 1 to 1000.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: void SetMaximumSegments
            (
                int maximumSegments /** Maximum Segments */
            );
            /**Returns  the degree when rebuild type is manual.
                        The degree value is limited from 2 to 24.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: int ManualDegree
            (
            );
            /**Sets  the degree when rebuild type is manual.
                        The degree value is limited from 2 to 24.
                    
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : features_modeling ("FEATURES MODELING"), nx_freeform_1 ("basic freeform modeling") */
            public: void SetManualDegree
            (
                int manualDegree /** Manual Degree */
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful 
             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: virtual bool Validate
            (
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

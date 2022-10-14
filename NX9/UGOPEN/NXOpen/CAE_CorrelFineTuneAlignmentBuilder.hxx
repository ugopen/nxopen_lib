#ifndef NXOpen_CAE_CORRELFINETUNEALIGNMENTBUILDER_HXX_INCLUDED
#define NXOpen_CAE_CORRELFINETUNEALIGNMENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_CorrelFineTuneAlignmentBuilder.ja
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
#include <NXOpen/CAE_CorrelBaseBuilder.hxx>
#include <NXOpen/CAE_CorrelFineTuneAlignmentBuilder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class CorrelFineTuneAlignmentBuilder;
    }
    namespace CAE
    {
        class CorrelBaseBuilder;
    }
    class Expression;
    namespace CAE
    {
        class _CorrelFineTuneAlignmentBuilderBuilder;
        class CorrelFineTuneAlignmentBuilderImpl;
        /** This builder is used to nudge the alignment by a fine adjustment  <br> To create a new instance of this class, use @link CAE::CorrelManager::CreateCorrelFineTuneAlignmentBuilder  CAE::CorrelManager::CreateCorrelFineTuneAlignmentBuilder @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  CorrelFineTuneAlignmentBuilder : public CAE::CorrelBaseBuilder
        {
            /** the distance vector enumeration for the alignment nudge*/
            public: enum DistanceVector
            {
                DistanceVectorXc/** xc */ ,
                DistanceVectorYc/** yc */ ,
                DistanceVectorZc/** zc */ ,
                DistanceVectorNegXc/** neg xc */ ,
                DistanceVectorNegYc/** neg yc */ ,
                DistanceVectorNegZc/** neg zc */ 
            };

            /** the angle vector enumeration for the alignment nudge*/
            public: enum AngleVector
            {
                AngleVectorXc/** xc */ ,
                AngleVectorYc/** yc */ ,
                AngleVectorZc/** zc */ ,
                AngleVectorNegXc/** neg xc */ ,
                AngleVectorNegYc/** neg yc */ ,
                AngleVectorNegZc/** neg zc */ 
            };

            private: CorrelFineTuneAlignmentBuilderImpl * m_correlfinetunealignmentbuilder_impl;
            private: friend class  _CorrelFineTuneAlignmentBuilderBuilder;
            protected: CorrelFineTuneAlignmentBuilder();
            public: ~CorrelFineTuneAlignmentBuilder();
            /**Returns  the distance expression 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * DistanceExp
            (
            );
            /**Returns  the distance vector enumeration 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::CorrelFineTuneAlignmentBuilder::DistanceVector DistanceEnum
            (
            );
            /**Sets  the distance vector enumeration 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetDistanceEnum
            (
                NXOpen::CAE::CorrelFineTuneAlignmentBuilder::DistanceVector distanceEnum /** distanceenum */ 
            );
            /** The move button to nudge alignment by the defined distance along the selected distance vector
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void MoveButton
            (
            );
            /**Returns  the angular expression 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * AngularExp
            (
            );
            /**Returns  the angle vector enumeration 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::CorrelFineTuneAlignmentBuilder::AngleVector AngleEnum
            (
            );
            /**Sets  the angle vector enumeration 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void SetAngleEnum
            (
                NXOpen::CAE::CorrelFineTuneAlignmentBuilder::AngleVector angleEnum /** angleenum */ 
            );
            /** The rotate button to nudge alignment by the defined angle via the selected angle vector
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_correl_base ("FE Correlation") */
            public: void RotateButton
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
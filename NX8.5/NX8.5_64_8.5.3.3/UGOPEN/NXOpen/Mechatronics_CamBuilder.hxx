#ifndef NXOpen_MECHATRONICS_CAMBUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_CAMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_CamBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Mechatronics_CouplingBuilder.hxx>
#include <NXOpen/Mechatronics_CamBuilder.hxx>
#include <NXOpen/libnxopencpp_mechatronics_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mechatronics
    {
        class CamBuilder;
    }
    class Expression;
    namespace Mechatronics
    {
        class CouplingBuilder;
    }
    namespace Mechatronics
    {
        class MotionProfile;
    }
    namespace Mechatronics
    {
        class _CamBuilderBuilder;
        class CamBuilderImpl;
        /** Represents a @link Mechatronics::Cam Mechatronics::Cam@endlink  builder.  <br> To create a new instance of this class, use @link Mechatronics::CamCollection::CreateCamBuilder  Mechatronics::CamCollection::CreateCamBuilder @endlink  <br> 
         <br>  Created in NX7.5.1.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  CamBuilder : public Mechatronics::CouplingBuilder
        {
            /** Represents the axis joint type. */
            public: enum AxisJointType
            {
                AxisJointTypeLinear/** Linear */,
                AxisJointTypeAngular/** Angular */
            };

            private: CamBuilderImpl * m_cambuilder_impl;
            private: friend class  _CamBuilderBuilder;
            protected: CamBuilder();
            public: ~CamBuilder();
            /**Returns  the master axis type. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Mechatronics::CamBuilder::AxisJointType MasterAxisType
            (
            );
            /**Sets  the master axis type. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetMasterAxisType
            (
                NXOpen::Mechatronics::CamBuilder::AxisJointType masterAxisType /** masteraxistype */ 
            );
            /**Returns  the slave axis type. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Mechatronics::CamBuilder::AxisJointType SlaveAxisType
            (
            );
            /**Sets  the slave axis type. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetSlaveAxisType
            (
                NXOpen::Mechatronics::CamBuilder::AxisJointType slaveAxisType /** slaveaxistype */ 
            );
            /**Returns  the motion profile. This can be @link MotionProfile MotionProfile@endlink . 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Mechatronics::MotionProfile * MotionProfile
            (
            );
            /**Sets  the motion profile. This can be @link MotionProfile MotionProfile@endlink . 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SetMotionProfile
            (
                NXOpen::Mechatronics::MotionProfile * profile /** profile */ 
            );
            /**Returns  the master offset. 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: NXOpen::Expression * MasterOffset
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
#ifndef NXOpen_CAE_POSTSCENARIOCOORDINATESYSTEM_HXX_INCLUDED
#define NXOpen_CAE_POSTSCENARIOCOORDINATESYSTEM_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PostScenarioCoordinateSystem.ja
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
#include <NXOpen/ugmath.hxx>
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
        class PostScenarioCoordinateSystem;
    }
    namespace CAE
    {
        /** Coordinate System Types */
        enum PostScenarioCoordinateSystemType
        {
            PostScenarioCoordinateSystemTypeRectangular/** cartesian coordinate system */,
            PostScenarioCoordinateSystemTypeCylindrical/** cylindrical coordinate system */,
            PostScenarioCoordinateSystemTypeSpherical/** spherical coordinate system */
        };

    }
    namespace CAE
    {
        class PostScenarioCoordinateSystemImpl;
        /**  @brief  Represents a local coordinate system.  

         
             <br> Not support KF.  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  PostScenarioCoordinateSystem : public NXOpen::TransientObject
        {
            private: PostScenarioCoordinateSystemImpl * m_postscenariocoordinatesystem_impl;
            /// \cond NX_NO_DOC 
            public: explicit PostScenarioCoordinateSystem(void *ptr);
            /// \endcond 
            /** Get the type of the coordinate system. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::PostScenarioCoordinateSystemType GetCsysType
            (
            );
            /** Set the type of the coordinate system. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetCsysType
            (
                NXOpen::CAE::PostScenarioCoordinateSystemType type /** type */ 
            );
            /** Get the origin of the coordinate system. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::Vector3d GetOrigin
            (
            );
            /** Set the origin of the coordinate system. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetOrigin
            (
                const NXOpen::Vector3d & origin /** origin */ 
            );
            /** Get the transformation matrix of the coordinate system. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::Matrix3x3 GetMatrix
            (
            );
            /** Set the transformation matrix of the coordinate system. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetMatrix
            (
                const NXOpen::Matrix3x3 & matrix /** matrix */ 
            );
            /** Destroys the object. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~PostScenarioCoordinateSystem();
        }; //lint !e1712 default constructor not defined for class  

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
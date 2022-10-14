#ifndef NXOpen_CAE_BUSHINGEADBUILDER_HXX_INCLUDED
#define NXOpen_CAE_BUSHINGEADBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_BushingEADBuilder.ja
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
#include <NXOpen/CAE_SelectElementsBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class BushingEADBuilder;
    }
    class Builder;
    namespace CAE
    {
        class PhysicalPropertyTable;
    }
    namespace CAE
    {
        class SelectElementsBuilder;
    }
    namespace CAE
    {
        class SelectFENodeList;
    }
    class CoordinateSystem;
    class Direction;
    class Point;
    namespace CAE
    {
        class _BushingEADBuilderBuilder;
        class BushingEADBuilderImpl;
        /** This class provides Bushing Associated Data Support  <br> To create a new instance of this class, use @link NXOpen::CAE::NodeElementManager::CreateBushingEadBuilder  NXOpen::CAE::NodeElementManager::CreateBushingEadBuilder @endlink  <br> 
         <br>  Created in NX7.5.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  BushingEADBuilder : public NXOpen::Builder
        {
            /** indicates to ignore, apply or clear the state property upon commit */
            public: enum State
            {
                StateApply/** apply the property */,
                StateClear/** clear the property */,
                StateIgnore/** ignore the property */
            };

            /** indicates which orientation method to use */
            public: enum OrientationMethod
            {
                OrientationMethodVector/** use a vector to orient the element */,
                OrientationMethodCsystem/** use a csystem to orient the element */,
                OrientationMethodNode/** use a node to orient the element */,
                OrientationMethodCsystemData/** use a csys data to orient the element */
            };

            /** indicates which type of coordinate system data to use */
            public: enum CoordinateSystemDataType
            {
                CoordinateSystemDataTypeCartesian/** use cartesian coordinate system data to orient the element */,
                CoordinateSystemDataTypeCylindrical/** use cylindrical coordinate system data to orient the element */,
                CoordinateSystemDataTypeSpherical/** use spherical coordinate system data to orient the element */
            };

            private: BushingEADBuilderImpl * m_bushingeadbuilder_impl;
            private: friend class  _BushingEADBuilderBuilder;
            protected: BushingEADBuilder();
            public: ~BushingEADBuilder();
            /**Returns  the select element operator selects elements 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::SelectElementsBuilder * Elements
            (
            );
            /**Returns  the get oriDirr operator gets  orientaion vector value 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::Direction * OriDirr
            (
            );
            /**Sets  the get oriDirr operator gets  orientaion vector value 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetOriDirr
            (
                NXOpen::Direction * oriDirr /** oridirr */ 
            );
            /**Returns  the state drives the commit action 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::BushingEADBuilder::State OrientationState
            (
            );
            /**Sets  the state drives the commit action 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetOrientationState
            (
                NXOpen::CAE::BushingEADBuilder::State orientationState /** orientation state */ 
            );
            /**Returns  the method to get the element orientation method 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::BushingEADBuilder::OrientationMethod OriMethod
            (
            );
            /**Sets  the method to get the element orientation method 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetOriMethod
            (
                NXOpen::CAE::BushingEADBuilder::OrientationMethod oriMethod /** orimethod */ 
            );
            /**Returns  the get ori_node operator selects an orientation node 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::SelectFENodeList * OriNode
            (
            );
            /**Returns  the get coordinate system method gets the coordinate system for orienting by coordinate system 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CoordinateSystem * OriCsystem
            (
            );
            /**Sets  the get coordinate system method gets the coordinate system for orienting by coordinate system 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetOriCsystem
            (
                NXOpen::CoordinateSystem * oriCsystem /** oricsystem */ 
            );
            /**Returns  the physical property table state state drives the action upon commit 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::BushingEADBuilder::State PhysicalPropertyTableState
            (
            );
            /**Sets  the physical property table state state drives the action upon commit 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetPhysicalPropertyTableState
            (
                NXOpen::CAE::BushingEADBuilder::State physicalPropertyTableState /** physicalpropertytablestate */ 
            );
            /**Returns  the physical property table of the bushing element 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::PhysicalPropertyTable * PhysicalPropertyTable
            (
            );
            /**Sets  the physical property table of the bushing element 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetPhysicalPropertyTable
            (
                NXOpen::CAE::PhysicalPropertyTable * physicalPropertyTable /** physicalpropertytable */ 
            );
            /**Returns  the get selection csys data type gets coordinate system data type 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::BushingEADBuilder::CoordinateSystemDataType CsysDataType
            (
            );
            /**Sets  the get selection csys data type gets coordinate system data type 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetCsysDataType
            (
                NXOpen::CAE::BushingEADBuilder::CoordinateSystemDataType csysDataType /** csysdatatype */ 
            );
            /**Returns  the get coordinate system data point origin gets the coordinates of origin point for orientation 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::Point * PointOrigin
            (
            );
            /**Sets  the get coordinate system data point origin gets the coordinates of origin point for orientation 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetPointOrigin
            (
                NXOpen::Point * originPoint /** orientation csys data origin point */
            );
            /**Returns  the get coordinate system data point on z axis gets the coordinates of point on z-axis for orientation 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::Point * PointOnZaxis
            (
            );
            /**Sets  the get coordinate system data point on z axis gets the coordinates of point on z-axis for orientation 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetPointOnZaxis
            (
                NXOpen::Point * zAxisPoint /** orientation csys data point on z-axis */
            );
            /**Returns  the get coordinate system data point in plane gets the coordinates of point in x-z plane if cartesian csys or point in azimuthal origin plane if cylindrical/spherical csys for orientation 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::Point * PointInPlane
            (
            );
            /**Sets  the get coordinate system data point in plane gets the coordinates of point in x-z plane if cartesian csys or point in azimuthal origin plane if cylindrical/spherical csys for orientation 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetPointInPlane
            (
                NXOpen::Point * planePoint /** orientation csys data point in the x-z plane if cartesian csys or azimuthal origin plane if cylindrical/spherical csys*/
            );
            /**Returns  the get preferred csys label gets the label assigned to the csys data 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: int PreferredLabel
            (
            );
            /**Sets  the get preferred csys label gets the label assigned to the csys data 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetPreferredLabel
            (
                int preferredLabel /** preferredlabel */ 
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
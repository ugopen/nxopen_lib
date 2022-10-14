#ifndef NXOpen_TOOLING_UNDERSIZEBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_UNDERSIZEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_UndersizeBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/Tooling_UndersizeBuilder.hxx>
#include <NXOpen/libnxopencpp_tooling_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Tooling
    {
        class UndersizeBuilder;
    }
    class Builder;
    class Expression;
    class Point;
    class SelectBodyList;
    class SelectPointList;
    namespace Tooling
    {
        class _UndersizeBuilderBuilder;
        class UndersizeBuilderImpl;
        /**  Represents a @link NXOpen::Tooling::UndersizeBuilder NXOpen::Tooling::UndersizeBuilder@endlink      <br> To create a new instance of this class, use @link NXOpen::Tooling::UndersizeCollection::CreateUndersizeBuilder  NXOpen::Tooling::UndersizeCollection::CreateUndersizeBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Angle.Value </td> <td> 
         
        90 (millimeters part), 90 (inches part) </td> </tr> 

        <tr><td> 
         
        OrbitSize.Value </td> <td> 
         
        0.05 (millimeters part), 0.002 (inches part) </td> </tr> 

        <tr><td> 
         
        OrbitType </td> <td> 
         
        Circular </td> </tr> 

        <tr><td> 
         
        SparkGap.Value </td> <td> 
         
        0.05 (millimeters part), 0.002 (inches part) </td> </tr> 

        </table>  

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  UndersizeBuilder : public NXOpen::Builder
        {
            /** Represents the orbit type */
            public: enum Orbit
            {
                OrbitCircular/** circular */,
                OrbitSquare/** square */,
                OrbitTriangle/** triangle */,
                OrbitSpherical/** spherical */,
                OrbitPoints/** specify points */
            };

            private: UndersizeBuilderImpl * m_undersizebuilder_impl;
            private: friend class  _UndersizeBuilderBuilder;
            protected: UndersizeBuilder();
            public: ~UndersizeBuilder();
            /**Returns  the orbit type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::UndersizeBuilder::Orbit OrbitType
            (
            );
            /**Sets  the orbit type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetOrbitType
            (
                NXOpen::Tooling::UndersizeBuilder::Orbit orbitType /** orbittype */ 
            );
            /**Returns  the reference point which is the center of the distribution circle
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * PointSpecify
            (
            );
            /**Sets  the reference point which is the center of the distribution circle
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPointSpecify
            (
                NXOpen::Point * pointSpecify /** pointspecify */ 
            );
            /**Returns  the body will be used as electrode body to do undersize 
             <br>  @deprecated Deprecated in NX10.0.0.  Use @link Tooling::UndersizeBuilder::ElectrodeBodies Tooling::UndersizeBuilder::ElectrodeBodies@endlink  instead. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Use Tooling::UndersizeBuilder::ElectrodeBodies instead.") NXOpen::SelectBodyList * SelectElectrodeBlock
            (
            );
            /**Returns  the electrode body to do undersize 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBodyList * ElectrodeBodies
            (
            );
            /**Returns  the points will be used as copy positions to undersize electrode 
             <br>  @deprecated Deprecated in NX10.0.0.  Use @link Tooling::UndersizeBuilder::OrbitPointList Tooling::UndersizeBuilder::OrbitPointList@endlink  instead. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX10.0.0.  Use Tooling::UndersizeBuilder::OrbitPointList instead.") NXOpen::SelectPointList * SelectPoints
            (
            );
            /**Returns  the points to be used as copy positions to undersize electrode 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectPointList * OrbitPointList
            (
            );
            /**Returns  the angle which is between two distribution electrodes 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Angle
            (
            );
            /**Returns  the orbit size which determines the radius of the distribution circle 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OrbitSize
            (
            );
            /**Returns  the spark gap which is the gap between the electrode head and the work piece 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * SparkGap
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
#ifndef NXOpen_MECHATRONICS_CURVEONCURVEJOINTBUILDER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_CURVEONCURVEJOINTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_CurveOnCurveJointBuilder.ja
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
#include <NXOpen/Mechatronics_PhysicsJointBuilder.hxx>
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
        class CurveOnCurveJointBuilder;
    }
    class Direction;
    class Expression;
    namespace Mechatronics
    {
        class PhysicsJointBuilder;
    }
    class NXObject;
    class Point;
    namespace Mechatronics
    {
        class _CurveOnCurveJointBuilderBuilder;
        class CurveOnCurveJointBuilderImpl;
        /** Represents a @link NXOpen::Mechatronics::CurveOnCurveJoint NXOpen::Mechatronics::CurveOnCurveJoint@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Mechatronics::CurveOnCurveJointCollection::CreateCurveOnCurveJointBuilder  NXOpen::Mechatronics::CurveOnCurveJointCollection::CreateCurveOnCurveJointBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Offset.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        Sliding </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  CurveOnCurveJointBuilder : public NXOpen::Mechatronics::PhysicsJointBuilder
        {
            private: CurveOnCurveJointBuilderImpl * m_curveoncurvejointbuilder_impl;
            private: friend class  _CurveOnCurveJointBuilderBuilder;
            protected: CurveOnCurveJointBuilder();
            public: ~CurveOnCurveJointBuilder();
            /** Get the section curve which belong to the attachment @return  curve or edge
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: std::vector<NXOpen::NXObject *> GetSectionCurve
            (
            );
            /** Set the section curve which belong to the attachment
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetSectionCurve
            (
                const std::vector<NXOpen::NXObject *> & curves /** curve or edge*/
            );
            /** Get the connected curve which the attachment will move along  @return  curve or edge
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: std::vector<NXOpen::NXObject *> GetConnectedCurve
            (
            );
            /** Set the connected curve which the attachment will move along 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetConnectedCurve
            (
                const std::vector<NXOpen::NXObject *> & curves /** curve or edge*/
            );
            /**Returns  the selected point on curve 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Point * PointOnCurve
            (
            );
            /**Sets  the selected point on curve 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetPointOnCurve
            (
                NXOpen::Point * pointOnCurve /** pointoncurve */ 
            );
            /**Returns  the axis vector which is tangent to the connected curve at the selected point 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Direction * AxisVector
            (
            );
            /**Sets  the axis vector which is tangent to the connected curve at the selected point 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetAxisVector
            (
                NXOpen::Direction * axisVector /** axisvector */ 
            );
            /**Returns  the offset specifies the "Zero Point" on the curve whose distance to the point along the curve is the offset value.
                        Zero Point is on the opposite direction of the axis with respect to the point on the curve. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Expression * Offset
            (
            );
            /**Returns  the sliding 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: bool Sliding
            (
            );
            /**Sets  the sliding 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SetSliding
            (
                bool sliding /** sliding */ 
            );
            /** Evaluate the path. If there is no path, create it, otherwise evaluate it.
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void EvaluatePath
            (
                const std::vector<NXOpen::NXObject *> & curves /** curve or edge*/
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

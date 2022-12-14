#ifndef NXOpen_MOTION_CURVECONTACTBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_CURVECONTACTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_CurveContactBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/Motion_CurveContactBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_motion_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Motion
    {
        class CurveContactBuilder;
    }
    class Builder;
    namespace Motion
    {
        class CurveContactAdams;
    }
    namespace Motion
    {
        class CurveContactRecurdyn;
    }
    class SelectNXObjectList;
    namespace Motion
    {
        class _CurveContactBuilderBuilder;
        class CurveContactBuilderImpl;
        /** Represents a @link Motion::CurveContactBuilder Motion::CurveContactBuilder@endlink   <br> To create a new instance of this class, use @link Motion::CurveContactCollection::CreateCurveContactBuilder  Motion::CurveContactCollection::CreateCurveContactBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        AdamsParameters.DynamicCoefficientExpression.Value </td> <td> 
         
        0.05 </td> </tr> 

        <tr><td> 
         
        AdamsParameters.ForceExponentExpression.Value </td> <td> 
         
        1.2 </td> </tr> 

        <tr><td> 
         
        AdamsParameters.MaterialDampingExpression.Value </td> <td> 
         
        100000.0 (millimeters part), 570.993 (inches part) </td> </tr> 

        <tr><td> 
         
        AdamsParameters.PenetrationDepthExpression.Value </td> <td> 
         
        0.001 (millimeters part), 0.00003937 (inches part) </td> </tr> 

        <tr><td> 
         
        AdamsParameters.SlipVelocityExpression.Value </td> <td> 
         
        0.1 (millimeters part), 0.003937 (inches part) </td> </tr> 

        <tr><td> 
         
        AdamsParameters.StaticCoefficientExpression.Value </td> <td> 
         
        0.08 </td> </tr> 

        <tr><td> 
         
        AdamsParameters.StiffnessExpression.Value </td> <td> 
         
        100000000000.0 (millimeters part), 570993141.98628 (inches part) </td> </tr> 

        <tr><td> 
         
        AdamsParameters.TransitionVelocityExpression.Value </td> <td> 
         
        1.0 (millimeters part), 0.03937 (inches part) </td> </tr> 

        <tr><td> 
         
        DisplayScale </td> <td> 
         
        1.0 </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.BufferRadiusFactorExpression.Value </td> <td> 
         
        1.2 </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.CurveToleranceFactorExpression.Value </td> <td> 
         
        10.0 </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.DynamicCoefficientExpression.Value </td> <td> 
         
        0.05 </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.FirstCurveMaximumPenetrationExpression.Value </td> <td> 
         
        10.0 (millimeters part), 0.3937 (inches part) </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.ForceExponentExpression.Value </td> <td> 
         
        1.2 </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.MaterialDampingExpression.Value </td> <td> 
         
        100000.0 (millimeters part), 570.993 (inches part) </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.MaximumStepSizeFactorExpression.Value </td> <td> 
         
        2.0 </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.PenetrationDepthExpression.Value </td> <td> 
         
        0.001 (millimeters part), 0.00003937 (inches part) </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.SecondCurveMaximumPenetrationExpression.Value </td> <td> 
         
        10.0 (millimeters part), 0.3937 (inches part) </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.SlipVelocityExpression.Value </td> <td> 
         
        0.1 (millimeters part), 0.003937 (inches part) </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.StaticCoefficientExpression.Value </td> <td> 
         
        0.08 </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.StiffnessExpression.Value </td> <td> 
         
        100000000000.0 (millimeters part), 570993141.98628 (inches part) </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.TransitionVelocityExpression.Value </td> <td> 
         
        1.0 (millimeters part), 0.03937 (inches part) </td> </tr> 

        </table>  

         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  CurveContactBuilder : public Builder
        {
            /** the enum for the materia side direction of the selected geometry*/
            public: enum GeometryMaterialSide
            {
                GeometryMaterialSideDirection/** direction */ ,
                GeometryMaterialSideDirectionReverse/** direction reverse */ 
            };

            private: CurveContactBuilderImpl * m_curvecontactbuilder_impl;
            private: friend class  _CurveContactBuilderBuilder;
            protected: CurveContactBuilder();
            public: ~CurveContactBuilder();
            /**Returns  the selection of the first contact curve 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * FirstContactCurve
            (
            );
            /**Returns  the selection of the second contact curve 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * SecondContactCurve
            (
            );
            /**Returns  the contact name 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ContactName
            (
            );
            /**Sets  the contact name 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetContactName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the contact name 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            void SetContactName
            (
                const char * name /** name */ 
            );
            /**Returns  the display scale 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: double DisplayScale
            (
            );
            /**Sets  the display scale 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetDisplayScale
            (
                double displayScale /** display scale */ 
            );
            /**Returns  the first geometry materia side direction 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Motion::CurveContactBuilder::GeometryMaterialSide FirstGeometryMaterialDirection
            (
            );
            /**Sets  the first geometry materia side direction 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetFirstGeometryMaterialDirection
            (
                NXOpen::Motion::CurveContactBuilder::GeometryMaterialSide sideDirection /** side direction */ 
            );
            /**Returns  the second geometry materia side direction 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Motion::CurveContactBuilder::GeometryMaterialSide SecondGeometryMaterialDirection
            (
            );
            /**Sets  the second geometry materia side direction 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetSecondGeometryMaterialDirection
            (
                NXOpen::Motion::CurveContactBuilder::GeometryMaterialSide sideDirection /** side direction */ 
            );
            /**Returns  the 2D CurveContact's subobject (the adams parameters) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Motion::CurveContactAdams * AdamsParameters
            (
            );
            /**Returns  the 2D CurveContact's subobject (the recurdyn parameters) 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Motion::CurveContactRecurdyn * RecurdynParameters
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

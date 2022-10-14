#ifndef NXOpen_TOOLING_DEFINECAMBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_DEFINECAMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_DefineCamBuilder.ja
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
#include <NXOpen/Tooling_DefineCamBuilder.hxx>
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
        class DefineCamBuilder;
    }
    class Axis;
    class Builder;
    class Direction;
    class Expression;
    class SelectDisplayableObjectList;
    namespace Tooling
    {
        class _DefineCamBuilderBuilder;
        class DefineCamBuilderImpl;
        /** Represents a @link NXOpen::Tooling::DefineCamBuilder NXOpen::Tooling::DefineCamBuilder@endlink  to create different types of cam objects, which
            are used for kinematic motion  <br> To create a new instance of this class, use @link NXOpen::Tooling::ProgressiveDieManager::CreateDefineCamBuilder  NXOpen::Tooling::ProgressiveDieManager::CreateDefineCamBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        LinearBackstopOffset.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        MotionDistance </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        PressStartAngle </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        PressStopAngle </td> <td> 
         
        90 </td> </tr> 

        <tr><td> 
         
        ReturnStartAngle </td> <td> 
         
        180 </td> </tr> 

        <tr><td> 
         
        ReturnStopAngle </td> <td> 
         
        270 </td> </tr> 

        <tr><td> 
         
        RockerAxisBackstopOffset.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        RotaryBackstopOffset.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        </table>  

         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  DefineCamBuilder : public NXOpen::Builder
        {
            /** Specifies the cam types */
            public: enum Types
            {
                TypesLinearCam/** Linear cam type */,
                TypesRotaryCam/** Rotary cam types */,
                TypesRockerCam/** Rocker cam types */,
                TypesCushionProgram/** Cushion Program cam type */
            };

            private: DefineCamBuilderImpl * m_definecambuilder_impl;
            private: friend class  _DefineCamBuilderBuilder;
            protected: DefineCamBuilder();
            public: ~DefineCamBuilder();
            /**Returns  the define cam type 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::DefineCamBuilder::Types Type
            (
            );
            /**Sets  the define cam type 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetType
            (
                NXOpen::Tooling::DefineCamBuilder::Types type /** type */ 
            );
            /**Returns  the linear cam body 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * LinearCamBodies
            (
            );
            /**Returns  the rotary cam body 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * RotaryCamBodies
            (
            );
            /**Returns  the rocker cam body 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * RockerCamBodies
            (
            );
            /**Returns  the rocker body of rocker cam 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * RockerCamRockerBodies
            (
            );
            /**Returns  the linear drive body which drives the linear body 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * LinearDriveBodies
            (
            );
            /**Returns  the rotary drive body which drives the rotary body 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * RotaryDriveBodies
            (
            );
            /**Returns  the rocker drive body which drives the rotary body of rocker cam 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * RockerDriveBodies
            (
            );
            /**Returns  the linear direction is the direction linear cam body move offset along 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * LinearDirection
            (
            );
            /**Sets  the linear direction is the direction linear cam body move offset along 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetLinearDirection
            (
                NXOpen::Direction * linearDirection /** lineardirection */ 
            );
            /**Returns  the linear backstop offset value, which affects the initial position of linear cam body
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * LinearBackstopOffset
            (
            );
            /**Returns  the rocker cam direction that the cam body moves along
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * RockerCamDirection
            (
            );
            /**Sets  the rocker cam direction that the cam body moves along
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetRockerCamDirection
            (
                NXOpen::Direction * rockerCamDirection /** rockercamdirection */ 
            );
            /**Returns  the rotary direction that the rotary body rotates around
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Axis * RotaryDirection
            (
            );
            /**Sets  the rotary direction that the rotary body rotates around
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetRotaryDirection
            (
                NXOpen::Axis * rotaryDirection /** rotarydirection */ 
            );
            /**Returns  the rotary backstop offset, which affects the initial position of rotary cam body 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RotaryBackstopOffset
            (
            );
            /**Returns  the rocker axis direction that the rocker body rotates around
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Axis * RockerAxisDirection
            (
            );
            /**Sets  the rocker axis direction that the rocker body rotates around
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetRockerAxisDirection
            (
                NXOpen::Axis * rockerAxisDirection /** rockeraxisdirection */ 
            );
            /**Returns  the rocker axis backstop offset, which affects the initial position of rocker body 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RockerAxisBackstopOffset
            (
            );
            /**Returns  the cam name 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXString CamName
            (
            );
            /**Sets  the cam name 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetCamName
            (
                const NXString & camName /** camname */ 
            );
            /**Sets  the cam name 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            void SetCamName
            (
                const char * camName /** camname */ 
            );
            /**Returns  the cushion body, actually, it often is the bolster body to do the kinematic motion
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * CushionBody
            (
            );
            /**Returns  the cushion direction that the cushion body moves along
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * CushionDirection
            (
            );
            /**Sets  the cushion direction that the cushion body moves along
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetCushionDirection
            (
                NXOpen::Direction * cushionDirection /** cushiondirection */ 
            );
            /**Returns  the motion distance 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double MotionDistance
            (
            );
            /**Sets  the motion distance 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetMotionDistance
            (
                double motionDistance /** motiondistance */ 
            );
            /**Returns  the press start angle 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double PressStartAngle
            (
            );
            /**Sets  the press start angle 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetPressStartAngle
            (
                double pressStartAngle /** pressstartangle */ 
            );
            /**Returns  the press stop angle 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double PressStopAngle
            (
            );
            /**Sets  the press stop angle 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetPressStopAngle
            (
                double pressStopAngle /** pressstopangle */ 
            );
            /**Returns  the return start angle 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double ReturnStartAngle
            (
            );
            /**Sets  the return start angle 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetReturnStartAngle
            (
                double returnStartAngle /** returnstartangle */ 
            );
            /**Returns  the return stop angle 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double ReturnStopAngle
            (
            );
            /**Sets  the return stop angle 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetReturnStopAngle
            (
                double returnStopAngle /** returnstopangle */ 
            );
            /**Returns  the cushion name 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXString CushionName
            (
            );
            /**Sets  the cushion name 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetCushionName
            (
                const NXString & cushionName /** cushionname */ 
            );
            /**Sets  the cushion name 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            void SetCushionName
            (
                const char * cushionName /** cushionname */ 
            );
            /** Delete the linear cam 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void DeleteLinearCam
            (
                const NXString & camName /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Delete the linear cam 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            void DeleteLinearCam
            (
                const char * camName /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Delete the rotary cam 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void DeleteRotaryCam
            (
                const NXString & camName /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Delete the rotary cam 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            void DeleteRotaryCam
            (
                const char * camName /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Delete the rocker cam 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void DeleteRockerCam
            (
                const NXString & camName /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Delete the rocker cam 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            void DeleteRockerCam
            (
                const char * camName /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Delete the cushion 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void DeleteCushion
            (
                const NXString & cushionName /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Delete the cushion 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            void DeleteCushion
            (
                const char * cushionName /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
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
#ifndef NXOpen_TOOLING_LSDYNAGEOMETRYPREPARATIONBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_LSDYNAGEOMETRYPREPARATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_LsdynaGeometryPreparationBuilder.ja
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
#include <NXOpen/Section.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
        class LsdynaGeometryPreparationBuilder;
    }
    class Builder;
    class Curve;
    class Expression;
    class Section;
    class SelectBody;
    class SelectCurveList;
    namespace Tooling
    {
        class _LsdynaGeometryPreparationBuilderBuilder;
        class LsdynaGeometryPreparationBuilderImpl;
        /** Stamping Die LS-Dyna integration draw geometry preprare builder. <br> To create a new instance of this class, use @link NXOpen::Tooling::AutoDieCollection::CreateLsdynaGeometryPreparationBuilder  NXOpen::Tooling::AutoDieCollection::CreateLsdynaGeometryPreparationBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        AutoPositionOption </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        BinderPosition </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        BlankOptionType </td> <td> 
         
        Sheet </td> </tr> 

        <tr><td> 
         
        BlankPositionType </td> <td> 
         
        AboveBinder </td> </tr> 

        <tr><td> 
         
        BlankPositionValue </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        BlankThickness </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ContactOffset </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ContactTypeOption </td> <td> 
         
        FormingOneWaySurfaceToSurface </td> </tr> 

        <tr><td> 
         
        DiePosition </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        DrawBeadTypeOption </td> <td> 
         
        Round </td> </tr> 

        <tr><td> 
         
        DrawTypeOption </td> <td> 
         
        SingleDraw </td> </tr> 

        <tr><td> 
         
        Friction </td> <td> 
         
        0.15 </td> </tr> 

        <tr><td> 
         
        NormalForce </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        PercentageForce </td> <td> 
         
        50 </td> </tr> 

        <tr><td> 
         
        ProcessBinder </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ProcessBinderOption </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ProcessBinderType </td> <td> 
         
        Stationary </td> </tr> 

        <tr><td> 
         
        ProcessDie </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ProcessDieOption </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ProcessDieType </td> <td> 
         
        Stationary </td> </tr> 

        <tr><td> 
         
        ProcessPunch </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ProcessPunchOption </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ProcessPunchType </td> <td> 
         
        Stationary </td> </tr> 

        <tr><td> 
         
        ProcessTypeOption </td> <td> 
         
        Closing </td> </tr> 

        <tr><td> 
         
        PunchPosition </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        RestrainForce.Value </td> <td> 
         
        356.5 (millimeters part), 356.5 (inches part) </td> </tr> 

        <tr><td> 
         
        TargetBinderType </td> <td> 
         
        Punch </td> </tr> 

        <tr><td> 
         
        TargetDieType </td> <td> 
         
        Punch </td> </tr> 

        <tr><td> 
         
        TargetPunchType </td> <td> 
         
        Punch </td> </tr> 

        <tr><td> 
         
        TensileStrength </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  LsdynaGeometryPreparationBuilder : public NXOpen::Builder
        {
            /** the enum of draw type. */
            public: enum DrawType
            {
                DrawTypeSingleDraw/** For draw die, punch and binder are lower than die. */,
                DrawTypeDoubleDraw/** For draw die, punch and binder are higher than die. */
            };

            /** the enum of material type. */
            public: enum MaterialType
            {
                MaterialTypeNXMaterial/** Use NX material for LS-Dyna solver.  */,
                MaterialTypeLSDynaMaterial/** Use LS-Dyna material for LS-Dyna solver. */
            };

            /** the enum of blank option. */
            public: enum BlankOption
            {
                BlankOptionSheet/** Select a sheet body as blank. */,
                BlankOptionCurve/** Select several curves to create a blank. */
            };

            /** the enum of blank position. */
            public: enum BlankPosition
            {
                BlankPositionAboveBinder/** Blank sheet body is above binder. */,
                BlankPositionAboveBinderandPunch/** Blank sheet body is above binder and punch. */
            };

            /** the enum of draw bead type. */
            public: enum DrawBeadType
            {
                DrawBeadTypeRound/** Draw bead section has round shape. */,
                DrawBeadTypeRectangle/** Draw bead section has rectangle shape. */
            };

            /** the enum of contact type. */
            public: enum ContactType
            {
                ContactTypeFormingOneWaySurfaceToSurface/** The draw components contact type is forming one way surface to surface. */,
                ContactTypeFormingOneWaySurfaceToSurfaceSmooth/** The draw components contact type is forming one way surface to surface smooth. */,
                ContactTypeFormingSurfaceToSurface/** The draw components contact type is forming surface to surface. */,
                ContactTypeFormingSurfaceToSurfaceSmooth/** The draw components contact type is forming surface to surface smooth. */,
                ContactTypeSurfaceToSurface/** The draw components contact type is surface to surface. */,
                ContactTypeAutomaticSurfaceToSurface/** The draw components contact type is automatic surface to surface. */
            };

            /** the enum of process type. */
            public: enum ProcessType
            {
                ProcessTypeGravity/** Blank has elastic deformation in flexible status. */,
                ProcessTypeClosing/** The process of die travels from initial position to binder. */,
                ProcessTypeDrawing/** The process of die travels from binder to punch. */
            };

            /** the enum of process action binder type. */
            public: enum ProcessActionBinder
            {
                ProcessActionBinderStationary/** The process action for binder is stationary. */,
                ProcessActionBinderClosureWith/** The process action for binder is closure with other draw components. */,
                ProcessActionBinderFollowWith/** The process action for binder is follow with other draw components. */,
                ProcessActionBinderTravel/** The process action for binder is travel to other draw components. */,
                ProcessActionBinderUntilHome/** The process action for binder is until home. */,
                ProcessActionBinderForce/** The process action for binder is by force. */
            };

            /** the enum of process action die type. */
            public: enum ProcessActionDie
            {
                ProcessActionDieStationary/** The process action for die is stationary. */,
                ProcessActionDieClosureWith/** The process action for die is closure with other draw components.  */,
                ProcessActionDieFollowWith/** The process action for die is follow with other draw components. */,
                ProcessActionDieTravel/** The process action for die is travel to other draw components. */,
                ProcessActionDieUntilHome/** The process action for die is until home. */,
                ProcessActionDieForce/** The process action for die is by force. */
            };

            /** the enum of process action punch type. */
            public: enum ProcessActionPunch
            {
                ProcessActionPunchStationary/** The process action for punch is stationary. */,
                ProcessActionPunchClosureWith/** The process action for punch is closure with other draw components. */,
                ProcessActionPunchFollowWith/** The process action for punch is follow with other draw components. */,
                ProcessActionPunchTravel/** The process action for punch is travel to other draw components. */,
                ProcessActionPunchUntilHome/** The process action for punch is until home. */,
                ProcessActionPunchForce/** The process action for punch is by force. */
            };

            /** the enum of target punch type. */
            public: enum TargetPunch
            {
                TargetPunchPunch/** For the process, the target of punch is punch. */,
                TargetPunchBinder/** For the process, the target of punch is binder. */,
                TargetPunchDie/** For the process, the target of punch is die.  */
            };

            /** the enum of target binder type.*/
            public: enum TargetBinder
            {
                TargetBinderPunch/** For the process, the target of binder is punch. */,
                TargetBinderBinder/** For the process, the target of binder is binder. */,
                TargetBinderDie/** For the process, the target of binder is die. */
            };

            /** the enum of target die type. */
            public: enum TargetDie
            {
                TargetDiePunch/** For the process, the target of die is punch. */,
                TargetDieBinder/** For the process, the target of die is binder. */,
                TargetDieDie/** For the process, the target of die is die. */
            };

            private: LsdynaGeometryPreparationBuilderImpl * m_lsdynageometrypreparationbuilder_impl;
            private: friend class  _LsdynaGeometryPreparationBuilderBuilder;
            protected: LsdynaGeometryPreparationBuilder();
            public: ~LsdynaGeometryPreparationBuilder();
            /**Returns  the draw type. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::LsdynaGeometryPreparationBuilder::DrawType DrawTypeOption
            (
            );
            /**Sets  the draw type. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetDrawTypeOption
            (
                NXOpen::Tooling::LsdynaGeometryPreparationBuilder::DrawType enumDrawType /** enumdrawtype */ 
            );
            /**Returns  the material type. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::LsdynaGeometryPreparationBuilder::MaterialType MaterialTypeOption
            (
            );
            /**Sets  the material type. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetMaterialTypeOption
            (
                NXOpen::Tooling::LsdynaGeometryPreparationBuilder::MaterialType enumMaterialType /** enummaterialtype */ 
            );
            /**Returns  the punch sheet. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBody * PunchSheet
            (
            );
            /**Returns  the binder sheet. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBody * BinderSheet
            (
            );
            /**Returns  the die sheet. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBody * DieSheet
            (
            );
            /**Returns  the blank option. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::LsdynaGeometryPreparationBuilder::BlankOption BlankOptionType
            (
            );
            /**Sets  the blank option. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetBlankOptionType
            (
                NXOpen::Tooling::LsdynaGeometryPreparationBuilder::BlankOption enumBlankOption /** enumblankoption */ 
            );
            /**Returns  the blank sheet. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBody * BlankSheet
            (
            );
            /**Returns  the blank curve. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * BlankCurve
            (
            );
            /**Returns  the blank thickness. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double BlankThickness
            (
            );
            /**Sets  the blank thickness. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetBlankThickness
            (
                double doubleBlankThickness /** doubleblankthickness */ 
            );
            /** Restore the position of die, punch and binder. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void ExecuteRestorePosition
            (
            );
            /** Move the position of die, punch and binder, according to 
                        @link Tooling::LsdynaGeometryPreparationBuilder::DiePosition Tooling::LsdynaGeometryPreparationBuilder::DiePosition@endlink ,
                        @link Tooling::LsdynaGeometryPreparationBuilder::PunchPosition Tooling::LsdynaGeometryPreparationBuilder::PunchPosition@endlink  ,
                        @link Tooling::LsdynaGeometryPreparationBuilder::BinderPosition Tooling::LsdynaGeometryPreparationBuilder::BinderPosition@endlink  settings. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void ExecuteMovePosition
            (
            );
            /**Returns  the blank position type. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::LsdynaGeometryPreparationBuilder::BlankPosition BlankPositionType
            (
            );
            /**Sets  the blank position type. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetBlankPositionType
            (
                NXOpen::Tooling::LsdynaGeometryPreparationBuilder::BlankPosition enumBlankPosition /** enumblankposition */ 
            );
            /**Returns  the draw bead type. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::LsdynaGeometryPreparationBuilder::DrawBeadType DrawBeadTypeOption
            (
            );
            /**Sets  the draw bead type. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetDrawBeadTypeOption
            (
                NXOpen::Tooling::LsdynaGeometryPreparationBuilder::DrawBeadType enumDrawBeadType /** enumdrawbeadtype */ 
            );
            /**Returns  the restraining force. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double TensileStrength
            (
            );
            /**Sets  the restraining force. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetTensileStrength
            (
                double doubleTensileStrength /** doubletensilestrength */ 
            );
            /**Returns  the expression of restraining force. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RestrainForce
            (
            );
            /**Returns  the normal force. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double NormalForce
            (
            );
            /**Sets  the normal force. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetNormalForce
            (
                double normalForce /** normalforce */ 
            );
            /**Returns  the percentage of force. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double PercentageForce
            (
            );
            /**Sets  the percentage of force. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetPercentageForce
            (
                double doublePercentageForce /** doublepercentageforce */ 
            );
            /**Returns  the automatic position for punch, die and binder. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool AutoPositionOption
            (
            );
            /**Sets  the automatic position for punch, die and binder. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetAutoPositionOption
            (
                bool toggleAutoPosition /** toggleautoposition */ 
            );
            /**Returns  the distance value to move binder. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double BinderPosition
            (
            );
            /**Sets  the distance value to move binder. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetBinderPosition
            (
                double doubleBinderPosition /** doublebinderposition */ 
            );
            /**Returns  the distance value to move die. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double DiePosition
            (
            );
            /**Sets  the distance value to move die. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetDiePosition
            (
                double doubleDiePosition /** doubledieposition */ 
            );
            /**Returns  the distance value to move punch. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double PunchPosition
            (
            );
            /**Sets  the distance value to move punch. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetPunchPosition
            (
                double doublePunchPosition /** doublepunchposition */ 
            );
            /**Returns  the distance value to move blank. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double BlankPositionValue
            (
            );
            /**Sets  the distance value to move blank. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetBlankPositionValue
            (
                double doubleBlankPosition /** doubleblankposition */ 
            );
            /**Returns  the friction. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double Friction
            (
            );
            /**Sets  the friction. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetFriction
            (
                double doubleFriction /** doublefriction */ 
            );
            /**Returns  the contact offset. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double ContactOffset
            (
            );
            /**Sets  the contact offset. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetContactOffset
            (
                double doubleContactOffset /** doublecontactoffset */ 
            );
            /**Returns  the contact type. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::LsdynaGeometryPreparationBuilder::ContactType ContactTypeOption
            (
            );
            /**Sets  the contact type. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetContactTypeOption
            (
                NXOpen::Tooling::LsdynaGeometryPreparationBuilder::ContactType enumContactType /** enumcontacttype */ 
            );
            /**Returns  the process type. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::LsdynaGeometryPreparationBuilder::ProcessType ProcessTypeOption
            (
            );
            /**Sets  the process type. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetProcessTypeOption
            (
                NXOpen::Tooling::LsdynaGeometryPreparationBuilder::ProcessType enumProcessType /** enumprocesstype */ 
            );
            /**Returns  the option of punch process. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool ProcessPunchOption
            (
            );
            /**Sets  the option of punch process. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetProcessPunchOption
            (
                bool toggleProcessPunch /** toggleprocesspunch */ 
            );
            /**Returns  the option of binder process. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool ProcessBinderOption
            (
            );
            /**Sets  the option of binder process. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetProcessBinderOption
            (
                bool toggleProcessBinder /** toggleprocessbinder */ 
            );
            /**Returns  the value of die process. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double ProcessDie
            (
            );
            /**Sets  the value of die process. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetProcessDie
            (
                double doubleProcessDie /** doubleprocessdie */ 
            );
            /**Returns  the type of binder process. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::LsdynaGeometryPreparationBuilder::ProcessActionBinder ProcessBinderType
            (
            );
            /**Sets  the type of binder process. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetProcessBinderType
            (
                NXOpen::Tooling::LsdynaGeometryPreparationBuilder::ProcessActionBinder enumProcessBinder /** enumprocessbinder */ 
            );
            /**Returns  the type of die process.  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::LsdynaGeometryPreparationBuilder::ProcessActionDie ProcessDieType
            (
            );
            /**Sets  the type of die process.  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetProcessDieType
            (
                NXOpen::Tooling::LsdynaGeometryPreparationBuilder::ProcessActionDie enumProcessDie /** enumprocessdie */ 
            );
            /**Returns  the type of punch process. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::LsdynaGeometryPreparationBuilder::ProcessActionPunch ProcessPunchType
            (
            );
            /**Sets  the type of punch process. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetProcessPunchType
            (
                NXOpen::Tooling::LsdynaGeometryPreparationBuilder::ProcessActionPunch enumProcessPunch /** enumprocesspunch */ 
            );
            /**Returns  the option of die process. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool ProcessDieOption
            (
            );
            /**Sets  the option of die process. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetProcessDieOption
            (
                bool toggleProcessDie /** toggleprocessdie */ 
            );
            /**Returns  the value of punch process. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double ProcessPunch
            (
            );
            /**Sets  the value of punch process. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetProcessPunch
            (
                double doubleProcessPunch /** doubleprocesspunch */ 
            );
            /**Returns  the value of binder process.  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double ProcessBinder
            (
            );
            /**Sets  the value of binder process.  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetProcessBinder
            (
                double doubleProcessBinder /** doubleprocessbinder */ 
            );
            /**Returns  the type of punch target.  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::LsdynaGeometryPreparationBuilder::TargetPunch TargetPunchType
            (
            );
            /**Sets  the type of punch target.  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetTargetPunchType
            (
                NXOpen::Tooling::LsdynaGeometryPreparationBuilder::TargetPunch enumTargetPunch /** enumtargetpunch */ 
            );
            /**Returns  the type of binder target.  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::LsdynaGeometryPreparationBuilder::TargetBinder TargetBinderType
            (
            );
            /**Sets  the type of binder target.  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetTargetBinderType
            (
                NXOpen::Tooling::LsdynaGeometryPreparationBuilder::TargetBinder enumTargetBinder /** enumtargetbinder */ 
            );
            /**Returns  the type of die target.  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::LsdynaGeometryPreparationBuilder::TargetDie TargetDieType
            (
            );
            /**Sets  the type of die target.  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetTargetDieType
            (
                NXOpen::Tooling::LsdynaGeometryPreparationBuilder::TargetDie enumTargetDie /** enumtargetdie */ 
            );
            /**Returns  the material name. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString MaterialName
            (
            );
            /**Sets  the material name. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetMaterialName
            (
                const NXString & materialName /** materialname */ 
            );
            /**Sets  the material name. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            void SetMaterialName
            (
                const char * materialName /** materialname */ 
            );
            /**Returns  the draw bead profiles.  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectCurveList * DrawBeadCurves
            (
            );
            /** Gets the percentage of force. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void GetPercentageForceArray
            (
                std::vector<double> & doublePercentageForceArray /** doublepercentageforcearray */ 
            );
            /** Sets the percentage of force. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetPercentageForceArray
            (
                const std::vector<double> & doublePercentageForceArray /** doublepercentageforcearray */ 
            );
            /** Sets the draw bead curves. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetDrawBeadCurves
            (
                const std::vector<NXOpen::Curve *> & drawBeadCurves /** drawbeadcurves */ 
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
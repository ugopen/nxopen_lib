#ifndef NXOpen_TOOLING_TRIMSOLIDBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_TRIMSOLIDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_TrimSolidBuilder.ja
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
#include <NXOpen/ScCollector.hxx>
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
        class TrimSolidBuilder;
    }
    namespace Assemblies
    {
        class SelectComponent;
    }
    class Body;
    class Builder;
    class Expression;
    class ScCollector;
    class SelectBody;
    class SelectBodyList;
    class SelectFaceList;
    namespace Tooling
    {
        class _TrimSolidBuilderBuilder;
        class TrimSolidBuilderImpl;
        /** Mold Wizard trim solid management builder, trims bounding box body with region, subtract 
                bounding box with workpiece or keep region and box.  <br> To create a new instance of this class, use @link NXOpen::Tooling::TrimSolidCollection::CreateTrimSolidBuilder  NXOpen::Tooling::TrimSolidCollection::CreateTrimSolidBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        ActionType </td> <td> 
         
        Trim </td> </tr> 

        <tr><td> 
         
        ChangeBoxSize </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        Clearance.Value </td> <td> 
         
        0.1 (millimeters part), 0.004 (inches part) </td> </tr> 

        <tr><td> 
         
        RemoveParameter </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  TrimSolidBuilder : public NXOpen::Builder
        {
            /** represents the option to select face or sheet body or manufacturing faces to trim the bounding box. */
            public: enum Types
            {
                TypesFace/** Region with body faces. */,
                TypesSheetBody/** Region with sheet bodies. */,
                TypesManufacturingRegion/** Region with attribute faces. */
            };

            /** represents the action to create trim solid. */
            public: enum TrimSolidAction
            {
                TrimSolidActionTrim/** Action to do trim. */,
                TrimSolidActionSubtract/** Action to do subtract. */,
                TrimSolidActionKeepBoxandRegion/** Action to keep box and region. */
            };

            private: TrimSolidBuilderImpl * m_trimsolidbuilder_impl;
            private: friend class  _TrimSolidBuilderBuilder;
            protected: TrimSolidBuilder();
            public: ~TrimSolidBuilder();
            /**Returns  the region faces to create trim solid. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::ScCollector * RegionFaces
            (
            );
            /**Returns  the sheet body to create trim solid. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::SelectBodyList * SheetBody
            (
            );
            /**Returns  the faces with the defined attribute to create trim solid.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::SelectFaceList * TaggedFaces
            (
            );
            /** The faces inside the bounding box. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void InsideBoundBox
            (
            );
            /** The faces inside/cross the bounding box. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void InsideCrossBoundBox
            (
            );
            /**Returns  the selected bounding box. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::SelectBody * SelectBoundBox
            (
            );
            /**Returns  the single side clearance value of the bounding box. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::Expression * Clearance
            (
            );
            /**Returns  the action type of trim, subtract or just keep the region and the bounding box. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::Tooling::TrimSolidBuilder::TrimSolidAction ActionType
            (
            );
            /**Sets  the action type of trim, subtract or just keep the region and the bounding box. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetActionType
            (
                NXOpen::Tooling::TrimSolidBuilder::TrimSolidAction actionType /** actiontype */ 
            );
            /**Returns  the trim body side. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: bool TrimDirection
            (
            );
            /**Sets  the trim body side. 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetTrimDirection
            (
                bool trimDirection /** trimdirection */ 
            );
            /**Returns  the option to change the created boundbox size
             <br>  Created in NX8.0.18.  <br>  
             <br> License requirements : None */
            public: bool ChangeBoxSize
            (
            );
            /**Sets  the option to change the created boundbox size
             <br>  Created in NX8.0.18.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetChangeBoxSize
            (
                bool changeBoxSize /** changeboxsize */ 
            );
            /**Returns  the component that the trimmed body is linked to. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::Assemblies::SelectComponent * SelectLinkTarget
            (
            );
            /**Returns  the type to select face, sheet body or manufacturing faces to trim the bounding box. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::Tooling::TrimSolidBuilder::Types Type
            (
            );
            /**Sets  the type to select face, sheet body or manufacturing faces to trim the bounding box. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetType
            (
                NXOpen::Tooling::TrimSolidBuilder::Types type /** type */ 
            );
            /**Returns  the option to remove parameter of the trim solid body
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: bool RemoveParameter
            (
            );
            /**Sets  the option to remove parameter of the trim solid body
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetRemoveParameter
            (
                bool removeParameter /** removeparameter */ 
            );
            /** Sets the bounding box tag. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetBoundBox
            (
                NXOpen::Body * block /** the bounding box block body*/
            );
            /** Sets the manually selected target body. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetManualBody
            (
                NXOpen::Body * block /**the manually selected target body*/
            );
            /** Creates the bounding box. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void CreateBoundBox
            (
            );
            /** Creates the tooling box.  @return  the bounded box body
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::Body * CreateToolingBox
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

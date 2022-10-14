#ifndef NXOpen_TOOLDESIGNER_MULTISECTIONBUILDER_HXX_INCLUDED
#define NXOpen_TOOLDESIGNER_MULTISECTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ToolDesigner_MultiSectionBuilder.ja
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
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libtooldesigneropencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace ToolDesigner
    {
        class MultiSectionBuilder;
    }
    class Builder;
    class SelectTaggedObject;
    class SelectTaggedObjectList;
    class TaggedObject;
    namespace ToolDesigner
    {
        class ReusePieChartCollisionBuilder;
    }
    namespace ToolDesigner
    {
        class _MultiSectionBuilderBuilder;
        class MultiSectionBuilderImpl;

        /// \cond NX_NO_DOC 
        /** A class that used for creating multi section  <br> To create a new instance of this class, use @link NXOpen::ToolDesigner::ToolDesignerManager::CreateMultiSectionBuilder  NXOpen::ToolDesigner::ToolDesignerManager::CreateMultiSectionBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        StepSizeDouble </td> <td> 
         
        5 </td> </tr> 

        </table>  

         <br>  Created in NX11.0.1.  <br>  
        */
        class TOOLDESIGNEROPENCPPEXPORT  MultiSectionBuilder : public NXOpen::Builder
        {
            private: MultiSectionBuilderImpl * m_multisectionbuilder_impl;
            private: friend class  _MultiSectionBuilderBuilder;
            protected: MultiSectionBuilder();
            public: ~MultiSectionBuilder();
            /**Returns  the gun selection getter
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") */
            public: NXOpen::SelectTaggedObject * GunSelection
            (
            );
            /** Set the gun selection 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") */
            public: void SetGunSelection
            (
                NXOpen::TaggedObject * gunSelection /** gunselection */ 
            );
            /** TODO: fill in a description for this 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") */
            public: void Setgun
            (
            );
            /** Set collision pie chart builder 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") */
            public: void SetReusePieChartCollisionBuilder
            (
                NXOpen::ToolDesigner::ReusePieChartCollisionBuilder * pieChartBuilder /** piechartbuilder */ 
            );
            /** TODO: fill in a description for this 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") */
            public: void ButtonApproach
            (
            );
            /** Set the selectable tableEditors selected items  
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") */
            public: void SetInvisibleSelection
            (
                NXOpen::TaggedObject * invisibleSelection /** invisibleselection */ 
            );
            /**Returns  the selectable tableEditors selected items (for all tables) 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") */
            public: NXOpen::SelectTaggedObjectList * InvisibleSelection
            (
            );
            /** The rotationMatixAccordingToDegreesForSelectedWeld update
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") */
            public: void UpdateRotationMatrixAccordingToDegreesForSelectedWeld
            (
                const NXOpen::Matrix3x3 & rotationMatrix /** rotationmatrix */ ,
                const NXOpen::Point3d & point /** point */ 
            );
            /**Returns  the weld selection 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") */
            public: NXOpen::SelectTaggedObject * WeldSelection
            (
            );
            /** Set the weld selection 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") */
            public: void SetWeldSelection
            (
                NXOpen::TaggedObject * weldSelection /** weldselection */ 
            );
            /**Returns  the get updateGunAssignmentToggle
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") */
            public: bool UpdateGunAssignmentToggle
            (
            );
            /** Set the gun assignment toggle 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") */
            public: void SetUpdateGunAssignmentToggle
            (
                bool update /** update */ 
            );
            /**Returns  the get updateGunAssignmentToggle
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") */
            public: bool SetApproachToggle
            (
            );
            /** Set the set approach toggle 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") */
            public: void SetSetApproachToggle
            (
                bool update /** update */ 
            );
            /**Button Calculate collision for selected weld 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") */
            public: void ButtonCalculateCollision
            (
            );
            /**Returns  the StepSizeDouble getter 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") */
            public: double StepSizeDouble
            (
            );
            /**Sets  the StepSizeDouble getter 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : fp_fixture_planner ("FULL FIXTURE PLANNER") */
            public: void SetStepSizeDouble
            (
                double stepSizeDouble /** stepsizedouble */ 
            );
        };

        /// \endcond 
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
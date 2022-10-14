#ifndef NXOpen_TOOLING_REFERENCECOPYBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_REFERENCECOPYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_ReferenceCopyBuilder.ja
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
#include <NXOpen/Tooling_CloneObject.hxx>
#include <NXOpen/ugmath.hxx>
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
        class ReferenceCopyBuilder;
    }
    namespace Assemblies
    {
        class SelectComponent;
    }
    class Axis;
    class Builder;
    class CoordinateSystem;
    class SelectBody;
    class SelectFace;
    namespace Tooling
    {
        class CloneObject;
    }
    namespace Tooling
    {
        class _ReferenceCopyBuilderBuilder;
        class ReferenceCopyBuilderImpl;
        /** 
            Represents a @link NXOpen::Tooling::ReferenceCopyBuilder NXOpen::Tooling::ReferenceCopyBuilder@endlink  builder.
             <br> To create a new instance of this class, use @link NXOpen::Tooling::MoldwizardManager::CreateReferenceCopyBuilder  NXOpen::Tooling::MoldwizardManager::CreateReferenceCopyBuilder @endlink  <br> 
         <br>  Created in NX12.0.2.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  ReferenceCopyBuilder : public NXOpen::Builder
        {
            /** This enum defines the operation types */
            public: enum Types
            {
                TypesComponent/** Copy a component */,
                TypesBody/** Copy a body */
            };

            /** This enum defines the component motion types */
            public: enum ComponentMotionTypes
            {
                ComponentMotionTypesDynamic/** Dynamic */,
                ComponentMotionTypesCSYSToCSYS/** CSYS to CSYS */,
                ComponentMotionTypesAngle/** Angle */,
                ComponentMotionTypesFaceToFace/** Face to Face */
            };

            /** This enum defines the body motion types */
            public: enum BodyMotionTypes
            {
                BodyMotionTypesDynamic/** Dynamic */,
                BodyMotionTypesCSYSToCSYS/** CSYS to CSYS */,
                BodyMotionTypesAngle/** Angle */,
                BodyMotionTypesFaceToFace/** Face to Face */
            };

            private: ReferenceCopyBuilderImpl * m_referencecopybuilder_impl;
            private: friend class  _ReferenceCopyBuilderBuilder;
            protected: ReferenceCopyBuilder();
            public: ~ReferenceCopyBuilder();
            /**Returns  the reference copy operation type 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::ReferenceCopyBuilder::Types Type
            (
            );
            /**Sets  the reference copy operation type 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetType
            (
                NXOpen::Tooling::ReferenceCopyBuilder::Types type /** type */ 
            );
            /**Returns  the component to copy.
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Assemblies::SelectComponent * CopyComponentSelection
            (
            );
            /**Returns  the body to copy.
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBody * CopyBodySelection
            (
            );
            /**Returns  the reference component motion type 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::ReferenceCopyBuilder::ComponentMotionTypes ComponentMotionType
            (
            );
            /**Sets  the reference component motion type 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetComponentMotionType
            (
                NXOpen::Tooling::ReferenceCopyBuilder::ComponentMotionTypes type /** type */ 
            );
            /**Returns  the reference body motion type 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::ReferenceCopyBuilder::BodyMotionTypes BodyMotionType
            (
            );
            /**Sets  the reference body motion type 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetBodyMotionType
            (
                NXOpen::Tooling::ReferenceCopyBuilder::BodyMotionTypes type /** type */ 
            );
            /**Returns  the move handles only 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: bool MoveHandlesOnly
            (
            );
            /**Sets  the move handles only 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetMoveHandlesOnly
            (
                bool moveHandlesOnly /** movehandlesonly */ 
            );
            /**Returns  the number of components 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: int NumberOfComponents
            (
            );
            /**Sets  the number of components 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetNumberOfComponents
            (
                int numberOfComponents /** numberofcomponents */ 
            );
            /**Returns  the number of bodies 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: int NumberOfBodies
            (
            );
            /**Sets  the number of bodies 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetNumberOfBodies
            (
                int numberOfBodies /** numberofbodies */ 
            );
            /**Returns  the new component 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: bool NewComponent
            (
            );
            /**Sets  the new component 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetNewComponent
            (
                bool newComponent /** newcomponent */ 
            );
            /**Returns  the location of the destination component. 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point3d ManipulatorOrigin
            (
            );
            /**Sets  the location of the destination component. 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetManipulatorOrigin
            (
                const NXOpen::Point3d & manipulatorOrigin /** manipulatororigin */ 
            );
            /**Returns  the orientation of the destination component. 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Matrix3x3 ManipulatorMatrix
            (
            );
            /**Sets  the orientation of the destination component. 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetManipulatorMatrix
            (
                const NXOpen::Matrix3x3 & manipulatorMatrix /** manipulatormatrix */ 
            );
            /**Returns  the from coordinate system 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CoordinateSystem * FromCsys
            (
            );
            /**Sets  the from coordinate system 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetFromCsys
            (
                NXOpen::CoordinateSystem * coordinateSystem /** coordinatesystem */ 
            );
            /**Returns  the destination coordinate system 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::CoordinateSystem * DestinationCsys
            (
            );
            /**Sets  the destination coordinate system 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetDestinationCsys
            (
                NXOpen::CoordinateSystem * coordinateSystem /** coordinatesystem */ 
            );
            /**Returns  the from face 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectFace * FromFace
            (
            );
            /**Returns  the destination face 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectFace * DestinationFace
            (
            );
            /**Returns  the rotate axis 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Axis * RotateVector
            (
            );
            /**Sets  the rotate axis 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetRotateVector
            (
                NXOpen::Axis * rotateVector /** rotatevector */ 
            );
            /**Returns  the rotate angle 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: double RotateAngle
            (
            );
            /**Sets  the rotate angle 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void SetRotateAngle
            (
                double rotateAngle /** rotateangle */ 
            );
            /**Returns  the clone client data. 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: NXOpen::Tooling::CloneObject * CloneObject
            (
            );
            /** Start to copy components. 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void BeginDrag
            (
            );
            /** Drag the copied components. 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void Drag
            (
            );
            /** End to copy components. 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR prog_die_wizard ("UG/Progressive Die Wizard") */
            public: void EndDrag
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
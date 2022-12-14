#ifndef NXOpen_FEATURES_TOOLINGBOXBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_TOOLINGBOXBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ToolingBoxBuilder.ja
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
#include <NXOpen/Features_ToolingBoxBuilder.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        class ToolingBoxBuilder;
    }
    class Direction;
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class NXColor;
    class NXObject;
    class ScCollector;
    class SelectCoordinateSystem;
    class SelectNXObjectList;
    namespace Features
    {
        class _ToolingBoxBuilderBuilder;
        class ToolingBoxBuilderImpl;
        /**
            Represents a @link NXOpen::Features::ToolingBox NXOpen::Features::ToolingBox@endlink  builder
             <br> To create a new instance of this class, use @link NXOpen::Features::ToolingFeatureCollection::CreateToolingBoxBuilder  NXOpen::Features::ToolingFeatureCollection::CreateToolingBoxBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Clearance.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        OffsetNegativeX.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        OffsetNegativeY.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        OffsetNegativeZ.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        OffsetPositiveX.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        OffsetPositiveY.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        OffsetPositiveZ.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        RadialOffset.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        ReferenceCsysType </td> <td> 
         
        Wcs </td> </tr> 

        <tr><td> 
         
        SingleOffset </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        XValue.Value </td> <td> 
         
        10 (millimeters part), 0.5 (inches part) </td> </tr> 

        <tr><td> 
         
        YValue.Value </td> <td> 
         
        10 (millimeters part), 0.5 (inches part) </td> </tr> 

        <tr><td> 
         
        ZValue.Value </td> <td> 
         
        10 (millimeters part), 0.5 (inches part) </td> </tr> 

        </table>  

         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  ToolingBoxBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** the type for box feature*/
            public: enum Types
            {
                TypesCenterAndLengths/** block with center point and lengths*/,
                TypesBoundedBlock/** bounded block*/,
                TypesBoundedCylinder/** bounded cylinder*/
            };

            /** the type of reference csys for box feature*/
            public: enum RefCsysType
            {
                RefCsysTypeWcs/** reference WCS*/,
                RefCsysTypeAbsoluteinDisplayedPart/** reference ABS in displayed part*/,
                RefCsysTypeSelectedCsys/** reference the selected csys*/
            };

            private: ToolingBoxBuilderImpl * m_toolingboxbuilder_impl;
            private: friend class  _ToolingBoxBuilderBuilder;
            protected: ToolingBoxBuilder();
            public: ~ToolingBoxBuilder();
            /**Returns  the objects used for bounded box creation. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * BoundedObject
            (
            );
            /**Returns  the reference csys type 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::ToolingBoxBuilder::RefCsysType ReferenceCsysType
            (
            );
            /**Sets  the reference csys type 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") OR studio_free_form ("STUDIO FREE FORM") OR features_modeling ("FEATURES MODELING") OR solid_modeling ("SOLIDS MODELING") */
            public: void SetReferenceCsysType
            (
                NXOpen::Features::ToolingBoxBuilder::RefCsysType referenceType /** referencetype */ 
            );
            /**Returns  the selected reference csys 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectCoordinateSystem * CsysSelection
            (
            );
            /**Returns  the cylinder axis vector to create the bounded cylinder 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * AxisVector
            (
            );
            /**Sets  the cylinder axis vector to create the bounded cylinder 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") OR studio_free_form ("STUDIO FREE FORM") OR features_modeling ("FEATURES MODELING") OR solid_modeling ("SOLIDS MODELING") */
            public: void SetAxisVector
            (
                NXOpen::Direction * cylinderVector /** cylindervector */ 
            );
            /**Returns  the edge length in X direction for general box.  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * XValue
            (
            );
            /**Returns  the edge length in Y direction for general box.  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * YValue
            (
            );
            /**Returns  the edge length in Z direction for general box.  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ZValue
            (
            );
            /**Returns  the clearance value for box in six directions. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Clearance
            (
            );
            /**Returns  the offset value for box in +X direction. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OffsetPositiveX
            (
            );
            /**Returns  the offset value for box in -X direction. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OffsetNegativeX
            (
            );
            /**Returns  the offset value for box in +Y direction. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OffsetPositiveY
            (
            );
            /**Returns  the offset value for box in -Y direction. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OffsetNegativeY
            (
            );
            /**Returns  the offset value for box in +Z direction. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OffsetPositiveZ
            (
            );
            /**Returns  the offset value for box in -Z direction. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * OffsetNegativeZ
            (
            );
            /**Returns  the radial offset value for cylinder box
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * RadialOffset
            (
            );
            /**Returns  the box type. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::ToolingBoxBuilder::Types Type
            (
            );
            /**Sets  the box type. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") OR studio_free_form ("STUDIO FREE FORM") OR features_modeling ("FEATURES MODELING") OR solid_modeling ("SOLIDS MODELING") */
            public: void SetType
            (
                NXOpen::Features::ToolingBoxBuilder::Types type /** type */ 
            );
            /**Returns  the csys associative 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool CsysAssociative
            (
            );
            /**Sets  the csys associative 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") OR studio_free_form ("STUDIO FREE FORM") OR features_modeling ("FEATURES MODELING") OR solid_modeling ("SOLIDS MODELING") */
            public: void SetCsysAssociative
            (
                bool csysAssociative /** csysassociative */ 
            );
            /**Returns  the precision value for the size of bounded box
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double PrecisionValue
            (
            );
            /**Sets  the precision value for the size of bounded box
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") OR studio_free_form ("STUDIO FREE FORM") OR features_modeling ("FEATURES MODELING") OR solid_modeling ("SOLIDS MODELING") */
            public: void SetPrecisionValue
            (
                double precisionValue /** precisionvalue */ 
            );
            /**Returns  the precision value for the center point of bounded box
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: double PositionPrecisionValue
            (
            );
            /**Sets  the precision value for the center point of bounded box
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") OR studio_free_form ("STUDIO FREE FORM") OR features_modeling ("FEATURES MODELING") OR solid_modeling ("SOLIDS MODELING") */
            public: void SetPositionPrecisionValue
            (
                double precisionValue /** precisionvalue */ 
            );
            /** Sets box csys matrix. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") OR studio_free_form ("STUDIO FREE FORM") OR features_modeling ("FEATURES MODELING") OR solid_modeling ("SOLIDS MODELING") */
            public: void SetBoxMatrixAndPosition
            (
                const NXOpen::Matrix3x3 & matrix /** matrix */ ,
                const NXOpen::Point3d & position /** position */ 
            );
            /**Returns  the box color. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * BoxColor
            (
            );
            /**Sets  the box color. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") OR studio_free_form ("STUDIO FREE FORM") OR features_modeling ("FEATURES MODELING") OR solid_modeling ("SOLIDS MODELING") */
            public: void SetBoxColor
            (
                NXOpen::NXColor * colorValue /** colorvalue */ 
            );
            /**Returns  the position of csys for box. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point3d BoxPosition
            (
            );
            /**Sets  the position of csys for box. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") OR studio_free_form ("STUDIO FREE FORM") OR features_modeling ("FEATURES MODELING") OR solid_modeling ("SOLIDS MODELING") */
            public: void SetBoxPosition
            (
                const NXOpen::Point3d & csysOrigin /** csysorigin */ 
            );
            /** Sets selected object occurrences. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") OR studio_free_form ("STUDIO FREE FORM") OR features_modeling ("FEATURES MODELING") OR solid_modeling ("SOLIDS MODELING") */
            public: void SetSelectedOccurrences
            (
                const std::vector<NXOpen::NXObject *> & selections /** Last selected objects. */,
                const std::vector<NXOpen::NXObject *> & deselections /** Last deselected objects. */
            );
            /**Returns  the selected facet bodies. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * FacetBodies
            (
            );
            /** Calculate box size and set directions, edge length, lower point position. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") OR studio_free_form ("STUDIO FREE FORM") OR features_modeling ("FEATURES MODELING") OR solid_modeling ("SOLIDS MODELING") */
            public: void CalculateBoxSize
            (
            );
            /**Returns  the value indicate whether to show bounded box dimension or not during preview. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShowDimension
            (
            );
            /**Sets  the value indicate whether to show bounded box dimension or not during preview. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") OR studio_free_form ("STUDIO FREE FORM") OR features_modeling ("FEATURES MODELING") OR solid_modeling ("SOLIDS MODELING") */
            public: void SetShowDimension
            (
                bool csysAssociative /** csysassociative */ 
            );
            /**Returns  the option to control whether the handles operate individually or not. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool SingleOffset
            (
            );
            /**Sets  the option to control whether the handles operate individually or not. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") OR nx_electrode_wizard ("NX Electrode Wizard") OR prog_die_wizard ("UG/Progressive Die Wizard") OR studio_free_form ("STUDIO FREE FORM") OR features_modeling ("FEATURES MODELING") OR solid_modeling ("SOLIDS MODELING") */
            public: void SetSingleOffset
            (
                bool csysAssociative /** csysassociative */ 
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

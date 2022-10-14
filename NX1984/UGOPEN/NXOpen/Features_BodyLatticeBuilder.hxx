#ifndef NXOpen_FEATURES_BODYLATTICEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_BODYLATTICEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_BodyLatticeBuilder.ja
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
#include <NXOpen/GeometricUtilities_CurveAlignedListBuilder.hxx>
#include <NXOpen/GeometricUtilities_UnitCellBuilder.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/Section.hxx>
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
        class BodyLatticeBuilder;
    }
    class CoordinateSystem;
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class CurveAlignedListBuilder;
    }
    namespace GeometricUtilities
    {
        class UnitCellBuilder;
    }
    class Point;
    class ScCollector;
    class Section;
    namespace Features
    {
        class _BodyLatticeBuilderBuilder;
        class BodyLatticeBuilderImpl;
        /**Represents a Features.BodyLattice builder <br> To create a new instance of this class, use @link NXOpen::Features::LatticeFeatureCollection::CreateBodyLatticeBuilder  NXOpen::Features::LatticeFeatureCollection::CreateBodyLatticeBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        AlignAtSplitCurve </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        Layers </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        OptimizationIterations </term> <description> 
         
        100 </description> </item> 

        <item><term> 
         
        Parameterization </term> <description> 
         
        Automatic </description> </item> 

        <item><term> 
         
        Type </term> <description> 
         
        UnitFill </description> </item> 

        <item><term> 
         
        UnitCell.ApproximateSourceHexMeshSize.Value </term> <description> 
         
        10 (millimeters part), 0.5 (inches part) </description> </item> 

        <item><term> 
         
        UnitCell.CellType </term> <description> 
         
        BiTriangle </description> </item> 

        <item><term> 
         
        UnitCell.CellTypeName </term> <description> 
         
        BiTriangle </description> </item> 

        <item><term> 
         
        UnitCell.EdgeLength.Value </term> <description> 
         
        10 (millimeters part), 0.5 (inches part) </description> </item> 

        <item><term> 
         
        UnitCell.IsUniformCube </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        UnitCell.SizeX.Value </term> <description> 
         
        10 (millimeters part), 0.5 (inches part) </description> </item> 

        <item><term> 
         
        UnitCell.SizeY.Value </term> <description> 
         
        10 (millimeters part), 0.5 (inches part) </description> </item> 

        <item><term> 
         
        UnitCell.SizeZ.Value </term> <description> 
         
        10 (millimeters part), 0.5 (inches part) </description> </item> 

        </list> 

         <br>  Created in NX1926.0.0.  <br>  
        */
        class NXOPENCPP_FEATURESEXPORT  BodyLatticeBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** @brief This enum represents the lattice types that are supported in NX. 

             */
            public: enum Types
            {
                TypesUnitFill/** unit fill */ ,
                TypesUnitConformal/** unit conformal */ 
            };

            /** @brief This enum represents the parameterization types that are supported in conformal body lattice. 

             */
            public: enum ParameterizationType
            {
                ParameterizationTypeAutomatic/** automatic */ ,
                ParameterizationTypePlanar/** planar */ ,
                ParameterizationTypeContour/** contour */ ,
                ParameterizationTypeCylindrical/** cylindrical */ ,
                ParameterizationTypeCurveAligned/** curve aligned */ 
            };

            private: BodyLatticeBuilderImpl * m_bodylatticebuilder_impl;
            private: friend class  _BodyLatticeBuilderBuilder;
            protected: BodyLatticeBuilder();
            public: ~BodyLatticeBuilder();
            /**Returns  @brief the type of lattice that is going to be created. 

              
                       
                       Supported lattice types are: @link NXOpen::Features::BodyLatticeBuilder::TypesUnitFill NXOpen::Features::BodyLatticeBuilder::TypesUnitFill@endlink ,
                        and @link NXOpen::Features::BodyLatticeBuilder::TypesUnitConformal NXOpen::Features::BodyLatticeBuilder::TypesUnitConformal@endlink ,
                       
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::BodyLatticeBuilder::Types Type
            (
            );
            /**Sets  @brief the type of lattice that is going to be created. 

              
                       
                       Supported lattice types are: @link NXOpen::Features::BodyLatticeBuilder::TypesUnitFill NXOpen::Features::BodyLatticeBuilder::TypesUnitFill@endlink ,
                        and @link NXOpen::Features::BodyLatticeBuilder::TypesUnitConformal NXOpen::Features::BodyLatticeBuilder::TypesUnitConformal@endlink ,
                       
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_lattice_base (" NX Lattice Base") */
            public: void SetType
            (
                NXOpen::Features::BodyLatticeBuilder::Types type /** type */ 
            );
            /**Returns the solid bodies that define the boundary for unit lattice type.
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * BoundaryBody
            (
            );
            /**Returns  the coordinate system which determines the orientation with respect to the lattice creation 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CoordinateSystem * Csys
            (
            );
            /**Sets  the coordinate system which determines the orientation with respect to the lattice creation 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: void SetCsys
            (
                NXOpen::CoordinateSystem * csys /** csys */ 
            );
            /**Returns the base face that defines the bottom plane to build conformal lattices
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * BaseFace
            (
            );
            /**Returns whether the conformal lattice will be generated on the other side of the face
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: bool ReverseFaceDirection
            (
            );
            /**Sets whether the conformal lattice will be generated on the other side of the face
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_lattice_base (" NX Lattice Base") */
            public: void SetReverseFaceDirection
            (
                bool reverseFaceDir /** reversefacedir */ 
            );
            /**Returns  the Unit Cell Builder 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::GeometricUtilities::UnitCellBuilder * UnitCell
            (
            );
            /**Returns  the optimization iterations 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: int OptimizationIterations
            (
            );
            /**Sets  the optimization iterations 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_lattice_base (" NX Lattice Base") */
            public: void SetOptimizationIterations
            (
                int optimizationIterations /** optimizationiterations */ 
            );
            /**Returns   @brief the UV mapping parameterization. 
                        
                        The UV parameters for each parameterization type are defined as the following:
                        <ul>
                        <li>For @link NXOpen::Features::BodyLatticeBuilder::ParameterizationTypeAutomatic NXOpen::Features::BodyLatticeBuilder::ParameterizationTypeAutomatic@endlink ,
                             the centre of the first face will be the origin and the face UV direction is used for parametrization.</li>
                        <li>For @link NXOpen::Features::BodyLatticeBuilder::ParameterizationTypePlanar NXOpen::Features::BodyLatticeBuilder::ParameterizationTypePlanar@endlink ,
                            @link Features::BodyLatticeBuilder::OrientationPoint1 Features::BodyLatticeBuilder::OrientationPoint1@endlink  is the origin and 
                            @link Features::BodyLatticeBuilder::OrientationPoint2 Features::BodyLatticeBuilder::OrientationPoint2@endlink   is the direction point for U direction.
                            V direction of UV mapping is perpendicular to U direction.
                            User needs to specify both these points on the input face.</li>
                         <li>For @link NXOpen::Features::BodyLatticeBuilder::ParameterizationTypeContour NXOpen::Features::BodyLatticeBuilder::ParameterizationTypeContour@endlink ,
                             User needs to specify all four contour points to define the lattice.</li>
                         <li>For @link NXOpen::Features::BodyLatticeBuilder::ParameterizationTypeCylindrical NXOpen::Features::BodyLatticeBuilder::ParameterizationTypeCylindrical@endlink ,
                             user needs to specify the split line used.</li>
                        </ul>
                         

             
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Features::BodyLatticeBuilder::ParameterizationType Parameterization
            (
            );
            /**Sets   @brief the UV mapping parameterization. 
                        
                        The UV parameters for each parameterization type are defined as the following:
                        <ul>
                        <li>For @link NXOpen::Features::BodyLatticeBuilder::ParameterizationTypeAutomatic NXOpen::Features::BodyLatticeBuilder::ParameterizationTypeAutomatic@endlink ,
                             the centre of the first face will be the origin and the face UV direction is used for parametrization.</li>
                        <li>For @link NXOpen::Features::BodyLatticeBuilder::ParameterizationTypePlanar NXOpen::Features::BodyLatticeBuilder::ParameterizationTypePlanar@endlink ,
                            @link Features::BodyLatticeBuilder::OrientationPoint1 Features::BodyLatticeBuilder::OrientationPoint1@endlink  is the origin and 
                            @link Features::BodyLatticeBuilder::OrientationPoint2 Features::BodyLatticeBuilder::OrientationPoint2@endlink   is the direction point for U direction.
                            V direction of UV mapping is perpendicular to U direction.
                            User needs to specify both these points on the input face.</li>
                         <li>For @link NXOpen::Features::BodyLatticeBuilder::ParameterizationTypeContour NXOpen::Features::BodyLatticeBuilder::ParameterizationTypeContour@endlink ,
                             User needs to specify all four contour points to define the lattice.</li>
                         <li>For @link NXOpen::Features::BodyLatticeBuilder::ParameterizationTypeCylindrical NXOpen::Features::BodyLatticeBuilder::ParameterizationTypeCylindrical@endlink ,
                             user needs to specify the split line used.</li>
                        </ul>
                         

             
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_lattice_base (" NX Lattice Base") */
            public: void SetParameterization
            (
                NXOpen::Features::BodyLatticeBuilder::ParameterizationType parameterization /** parameterization */ 
            );
            /**Returns  the orientation point1 of planar UV mapping
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * OrientationPoint1
            (
            );
            /**Sets  the orientation point1 of planar UV mapping
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_lattice_base (" NX Lattice Base") */
            public: void SetOrientationPoint1
            (
                NXOpen::Point * orientationPoint1 /** orientationpoint1 */ 
            );
            /**Returns  the orientation point2 of planar UV mapping
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * OrientationPoint2
            (
            );
            /**Sets  the orientation point2 of planar UV mapping
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_lattice_base (" NX Lattice Base") */
            public: void SetOrientationPoint2
            (
                NXOpen::Point * orientationPoint2 /** orientationpoint2 */ 
            );
            /**Returns  the contour point1 of contour UV mapping
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * ContourPoint1
            (
            );
            /**Sets  the contour point1 of contour UV mapping
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_lattice_base (" NX Lattice Base") */
            public: void SetContourPoint1
            (
                NXOpen::Point * contourPt1 /** contourpt1 */ 
            );
            /**Returns  the contour point2 of contour UV mapping
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * ContourPoint2
            (
            );
            /**Sets  the contour point2 of contour UV mapping
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_lattice_base (" NX Lattice Base") */
            public: void SetContourPoint2
            (
                NXOpen::Point * contourPt2 /** contourpt2 */ 
            );
            /**Returns  the contour point3 of contour UV mapping
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * ContourPoint3
            (
            );
            /**Sets  the contour point3 of contour UV mapping
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_lattice_base (" NX Lattice Base") */
            public: void SetContourPoint3
            (
                NXOpen::Point * contourPt3 /** contourpt3 */ 
            );
            /**Returns  the contour point4 of contour UV mapping
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * ContourPoint4
            (
            );
            /**Sets  the contour point4 of contour UV mapping
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_lattice_base (" NX Lattice Base") */
            public: void SetContourPoint4
            (
                NXOpen::Point * contourPt4 /** contourpt4 */ 
            );
            /**Returns  the split curve of cylindrical UV mapping
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Section * SplitCurve
            (
            );
            /**Returns  the align at split curve option for cylindrical UV mapping
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: bool AlignAtSplitCurve
            (
            );
            /**Sets  the align at split curve option for cylindrical UV mapping
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_lattice_base (" NX Lattice Base") */
            public: void SetAlignAtSplitCurve
            (
                bool alignAtSplitCurve /** alignatsplitcurve */ 
            );
            /**Returns  the curve aligned list 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_lattice_base (" NX Lattice Base") */
            public: NXOpen::GeometricUtilities::CurveAlignedListBuilder * CurveAlignedList
            (
            );
            /**Returns   @brief the number of unit cell layers stacked over each other. 

             
                         
                        The default is one layer only.  
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: int Layers
            (
            );
            /**Sets   @brief the number of unit cell layers stacked over each other. 

             
                         
                        The default is one layer only.  
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_lattice_base (" NX Lattice Base") */
            public: void SetLayers
            (
                int layers /** layers */ 
            );
            /**Returns   @brief the offset of the conformal lattice from the base face. 

             
                          
                         A negative offset will let the conformal lattice intersect with the base face ("into material").
                         A positive offset will move the conformal lattice away from the base face( "away from material"). 
                         Using a negative offset can ensure that the final lattice body will intersect with the base face, 
                         if that is required. The default offset is zero. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Offset
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
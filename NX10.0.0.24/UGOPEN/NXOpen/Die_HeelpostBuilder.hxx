#ifndef NXOpen_DIE_HEELPOSTBUILDER_HXX_INCLUDED
#define NXOpen_DIE_HEELPOSTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_HeelpostBuilder.ja
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
#include <NXOpen/Die_DieAttributesBuilder.hxx>
#include <NXOpen/Die_DieDirectionBuilder.hxx>
#include <NXOpen/Die_DieLocationBuilder.hxx>
#include <NXOpen/Die_DiePlaneBuilder.hxx>
#include <NXOpen/Die_HeelpostBuilder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_die_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Die
    {
        class HeelpostBuilder;
    }
    namespace Die
    {
        class DieAttributesBuilder;
    }
    namespace Die
    {
        class DieDirectionBuilder;
    }
    namespace Die
    {
        class DieLocationBuilder;
    }
    namespace Die
    {
        class DiePlaneBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class SelectCoordinateSystem;
    class SelectNXObject;
    namespace Die
    {
        class _HeelpostBuilderBuilder;
        class HeelpostBuilderImpl;
        /**
            Represents a @link Die::HeelpostBuilder Die::HeelpostBuilder@endlink  builder
             <br> To create a new instance of this class, use @link NXOpen::Die::DieCollection::Heelpost  NXOpen::Die::DieCollection::Heelpost @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        AngleTolerance </td> <td> 
         
        0.5 </td> </tr> 

        <tr><td> 
         
        BaseOffset.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        Center.InputType </td> <td> 
         
        SelectLocation </td> </tr> 

        <tr><td> 
         
        CreateFloor </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        Diameter.Value </td> <td> 
         
        50 (millimeters part), 2 (inches part) </td> </tr> 

        <tr><td> 
         
        DistanceTolerance </td> <td> 
         
        0.0254 </td> </tr> 

        <tr><td> 
         
        FloorThickness.Value </td> <td> 
         
        60 (millimeters part), 1.4 (inches part) </td> </tr> 

        <tr><td> 
         
        Height.Value </td> <td> 
         
        300 (millimeters part), 12 (inches part) </td> </tr> 

        <tr><td> 
         
        Length.Value </td> <td> 
         
        150 (millimeters part), 6 (inches part) </td> </tr> 

        <tr><td> 
         
        LocationOffset.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        PadOffset.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        PadThickness.Value </td> <td> 
         
        60 (millimeters part), 10.4 (inches part) </td> </tr> 

        <tr><td> 
         
        ReliefDepth.Value </td> <td> 
         
        5 (millimeters part), 0.2 (inches part) </td> </tr> 

        <tr><td> 
         
        ReliefWidth.Value </td> <td> 
         
        5 (millimeters part), 0.2 (inches part) </td> </tr> 

        <tr><td> 
         
        UsePercent </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        WallACreate </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        WallAOffset.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        WallARelief </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        WallAThickness.Value </td> <td> 
         
        30 (millimeters part), 1.2 (inches part) </td> </tr> 

        <tr><td> 
         
        WallBCreate </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        WallBOffset.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        WallBRelief </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        WallBThickness.Value </td> <td> 
         
        30 (millimeters part), 1.2 (inches part) </td> </tr> 

        <tr><td> 
         
        WallCCreate </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        WallCOffset.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        WallCRelief </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        WallCThickness.Value </td> <td> 
         
        30 (millimeters part), 1.2 (inches part) </td> </tr> 

        <tr><td> 
         
        WallDCreate </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        WallDOffset.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        WallDRelief </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        WallDThickness.Value </td> <td> 
         
        30 (millimeters part), 1.2 (inches part) </td> </tr> 

        <tr><td> 
         
        WallPercentage.Value </td> <td> 
         
        40 </td> </tr> 

        <tr><td> 
         
        Width.Value </td> <td> 
         
        150 (millimeters part), 6 (inches part) </td> </tr> 

        <tr><td> 
         
        XOffset.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        <tr><td> 
         
        YOffset.Value </td> <td> 
         
        0 (millimeters part), 0 (inches part) </td> </tr> 

        </table>  

         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_DIEEXPORT  HeelpostBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** Heelpost types */
            public: enum Types
            {
                TypesGuidepostWearplate/** allows a guide pin hole to be created */,
                TypesStorageBlock/** no hole allowed */,
                TypesSafetyBlock/** no hole allowed */
            };

            private: HeelpostBuilderImpl * m_heelpostbuilder_impl;
            private: friend class  _HeelpostBuilderBuilder;
            protected: HeelpostBuilder();
            public: ~HeelpostBuilder();
            /**Returns  the target solid the heelpost will be united with 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObject * Target
            (
            );
            /**Returns  the location (center) for the heelpost 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Die::DieLocationBuilder * Center
            (
            );
            /**Returns  the direction to apply to the location to determine the center of the heelpost 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Die::DieDirectionBuilder * OffsetDirection
            (
            );
            /**Returns  the offset value to apply in the offset direction to find the heelpost center 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * LocationOffset
            (
            );
            /**Returns  the base of the heelpost 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Die::DiePlaneBuilder * BaseOrientation
            (
            );
            /**Returns  the offset to apply to the given base before building the heelpost 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * BaseOffset
            (
            );
            /**Returns  the orientation at the top of the heelpost 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Die::DiePlaneBuilder * PadOrientation
            (
            );
            /**Returns  the offset value to apply to the pad orientation before building the heelpost 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * PadOffset
            (
            );
            /**Returns  the die centerline coordinate system for orienting the heelpost 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectCoordinateSystem * DieCenterlineCoordinateSystem
            (
            );
            /**Returns  the length with respect to the coordinate system 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Length
            (
            );
            /**Returns  the width with respect to the coordinate system 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Width
            (
            );
            /**Returns  the height from the selected base orientation to the origin of the pad orientation, if the pad orientation is not specified. This is before application of any specified base and pad offsets.  
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Height
            (
            );
            /**Returns  the pad thickness at the top of the post 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * PadThickness
            (
            );
            /**Returns  the value (true or false) to decide if the floor of the post should be created 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool CreateFloor
            (
            );
            /**Sets  the value (true or false) to decide if the floor of the post should be created 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetCreateFloor
            (
                bool createFloor /** createfloor */ 
            );
            /**Returns  the floor thickness 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * FloorThickness
            (
            );
            /**Returns  the diameter of the guide pin hole 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Diameter
            (
            );
            /**Returns  the offset applied in the X direction to determine the hole center 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * XOffset
            (
            );
            /**Returns  the offset applied in the Y direction to determine the hole center 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * YOffset
            (
            );
            /**Returns  the relief width 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ReliefWidth
            (
            );
            /**Returns  the relief depth 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ReliefDepth
            (
            );
            /**Returns  the value (true or false) to decide how to determine the wall thickness. True will evaluate each wall based on the total area of the post 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool UsePercent
            (
            );
            /**Sets  the value (true or false) to decide how to determine the wall thickness. True will evaluate each wall based on the total area of the post 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetUsePercent
            (
                bool usePercent /** usepercent */ 
            );
            /**Returns  the percentage of the post area to be applied to determine the wall thicknesses 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * WallPercentage
            (
            );
            /**Returns  the value (true or false) to decide if the "A" wall should be created 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool WallACreate
            (
            );
            /**Sets  the value (true or false) to decide if the "A" wall should be created 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetWallACreate
            (
                bool wallACreate /** wallacreate */ 
            );
            /**Returns  the "A" wall thickness 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * WallAThickness
            (
            );
            /**Returns  the offset from the outside to be applied to the "A" wall 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * WallAOffset
            (
            );
            /**Returns  the value (true or false) to decide if relief should be created at the top of the "A" wall 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool WallARelief
            (
            );
            /**Sets  the value (true or false) to decide if relief should be created at the top of the "A" wall 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetWallARelief
            (
                bool wallARelief /** wallarelief */ 
            );
            /**Returns  the value (true or false) to decide if the "B" wall should be created 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool WallBCreate
            (
            );
            /**Sets  the value (true or false) to decide if the "B" wall should be created 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetWallBCreate
            (
                bool wallBCreate /** wallbcreate */ 
            );
            /**Returns  the "B" wall thickness 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * WallBThickness
            (
            );
            /**Returns  the offset from the outside to be applied to the "B wall 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * WallBOffset
            (
            );
            /**Returns  the value (true or false) to decide if relief should be created at the top of the "B" wall 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool WallBRelief
            (
            );
            /**Sets  the value (true or false) to decide if relief should be created at the top of the "B" wall 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetWallBRelief
            (
                bool wallBRelief /** wallbrelief */ 
            );
            /**Returns  the value (true or false) to decide if the "C" wall should be created 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool WallCCreate
            (
            );
            /**Sets  the value (true or false) to decide if the "C" wall should be created 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetWallCCreate
            (
                bool wallCCreate /** wallccreate */ 
            );
            /**Returns  the "C" wall thickness 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * WallCThickness
            (
            );
            /**Returns  the offset from the outside to be applied to the "C" wall 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * WallCOffset
            (
            );
            /**Returns  the value (true or false) to decide if relief should be created at the top of the "C" wall 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool WallCRelief
            (
            );
            /**Sets  the value (true or false) to decide if relief should be created at the top of the "C" wall 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetWallCRelief
            (
                bool wallCRelief /** wallcrelief */ 
            );
            /**Returns  the value (true or false) to decide if the "D" wall should be created 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool WallDCreate
            (
            );
            /**Sets  the value (true or false) to decide if the "D" wall should be created 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetWallDCreate
            (
                bool wallDCreate /** walldcreate */ 
            );
            /**Returns  the "D" wall thickness 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * WallDThickness
            (
            );
            /**Returns  the offset from the outside to be applied to the "D" wall 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * WallDOffset
            (
            );
            /**Returns  the value (true or false) to decide if relief should be created at the top of the "D" wall 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: bool WallDRelief
            (
            );
            /**Sets  the value (true or false) to decide if relief should be created at the top of the "D" wall 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetWallDRelief
            (
                bool wallDRelief /** walldrelief */ 
            );
            /**Returns  the pad attributes 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Die::DieAttributesBuilder * PadAttributes
            (
            );
            /**Returns  the relief attributes 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Die::DieAttributesBuilder * ReliefAttributes
            (
            );
            /**Returns  the hole attributes 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Die::DieAttributesBuilder * HoleAttributes
            (
            );
            /**Returns  the hole diameter attributes (only the title is used) 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Die::DieAttributesBuilder * HoleDiameterAttributes
            (
            );
            /**Returns  the distance tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double DistanceTolerance
            (
            );
            /**Sets  the distance tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDistanceTolerance
            (
                double distanceTolerance /** distancetolerance */ 
            );
            /**Returns  the angle tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double AngleTolerance
            (
            );
            /**Sets  the angle tolerance 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetAngleTolerance
            (
                double angleTolerance /** angletolerance */ 
            );
            /**Returns  the post type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Die::HeelpostBuilder::Types Type
            (
            );
            /**Sets  the post type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetType
            (
                NXOpen::Die::HeelpostBuilder::Types type /** type */ 
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

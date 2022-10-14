#ifndef NXOpen_FEATURES_SHIPDESIGN_PLATESYSTEMBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_PLATESYSTEMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_PlateSystemBuilder.ja
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
#include <NXOpen/Features_ShipDesign_FeatureParmsBuilder.hxx>
#include <NXOpen/Features_ShipDesign_PlateStockBuilder.hxx>
#include <NXOpen/Features_ShipDesign_PlateSystemBuilder.hxx>
#include <NXOpen/Features_ShipDesign_ThicknessDirectionBuilder.hxx>
#include <NXOpen/GeometricUtilities_ProjectionOptions.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/Weld_CharacteristicsBuilder.hxx>
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
        namespace ShipDesign
        {
            class PlateSystemBuilder;
        }
    }
    class Body;
    class Expression;
    namespace Features
    {
        namespace ShipDesign
        {
            class FeatureParmsBuilder;
        }
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class PlateStockBuilder;
        }
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class ThicknessDirectionBuilder;
        }
    }
    namespace GeometricUtilities
    {
        class ProjectionOptions;
    }
    class Plane;
    class RegionPointList;
    class Section;
    class SelectNXObjectList;
    class TaggedObject;
    namespace Weld
    {
        class CharacteristicsBuilder;
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class _PlateSystemBuilderBuilder;
            class PlateSystemBuilderImpl;
            /**
                This class is used to create or edit the information shared between all the Basic Design plate system
                features in the Ship Design application. Currently this includes the following features:
                @link Features::ShipDesign::Deck Features::ShipDesign::Deck@endlink ,
                @link Features::ShipDesign::Hull Features::ShipDesign::Hull@endlink ,
                @link Features::ShipDesign::GenericPlateSystem Features::ShipDesign::GenericPlateSystem@endlink ,
                @link Features::ShipDesign::LongitudinalBulkhead Features::ShipDesign::LongitudinalBulkhead@endlink , and
                @link Features::ShipDesign::TransverseBulkhead Features::ShipDesign::TransverseBulkhead@endlink .
                 <br> To create a new instance of this class, use @link Features::ShipCollection::CreatePlateSystemBuilder  Features::ShipCollection::CreatePlateSystemBuilder @endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            Offset.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            Primary </td> <td> 
             
            FwdPortToInUp </td> </tr> 

            <tr><td> 
             
            PrimaryOnReference </td> <td> 
             
            FwdPortToInUp </td> </tr> 

            <tr><td> 
             
            Secondary1 </td> <td> 
             
            FwdPortToInUp </td> </tr> 

            <tr><td> 
             
            Secondary1OnReference </td> <td> 
             
            FwdPortToInUp </td> </tr> 

            <tr><td> 
             
            Secondary2 </td> <td> 
             
            FwdPortToInUp </td> </tr> 

            <tr><td> 
             
            Secondary2OnReference </td> <td> 
             
            FwdPortToInUp </td> </tr> 

            <tr><td> 
             
            Stock.KnuckleRatio </td> <td> 
             
            3.0 </td> </tr> 

            <tr><td> 
             
            Stock.KnuckleSmoothAngle </td> <td> 
             
            3.0 </td> </tr> 

            <tr><td> 
             
            Stock.MaterialOption </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            Stock.OppositeThickness.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            Stock.RestrictThicknessToMaterial </td> <td> 
             
            true </td> </tr> 

            <tr><td> 
             
            Stock.ThickenOption </td> <td> 
             
            SingleSided </td> </tr> 

            <tr><td> 
             
            Stock.Thickness.Value </td> <td> 
             
            10 (millimeters part), 0.5 (inches part) </td> </tr> 

            <tr><td> 
             
            Stock.ThicknessSourceOption </td> <td> 
             
            List </td> </tr> 

            <tr><td> 
             
            ThicknessDirection.ThicknessDirection </td> <td> 
             
            FwdPortInUp </td> </tr> 

            <tr><td> 
             
            ThicknessDirection.ThicknessDirectionOnReference </td> <td> 
             
            FwdPortInUp </td> </tr> 

            </table>  

             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  PlateSystemBuilder : public Features::ShipDesign::FeatureParmsBuilder
            {
                /** Settings used to indicate the default primary and secondary stiffener direction. The primary
                            direction is used to determine which side of the plate system the stiffener is placed upon. The
                            secondary direction is used to determine which direction the flange is pointing. The actual direction
                            depends on the plate system and the general stiffener direction. */
                public: enum StiffenerDirectionType
                {
                    StiffenerDirectionTypeFwdPortToInUp/** Direction is Forward, Port, To Reference, Inside or Up. */,
                    StiffenerDirectionTypeAftStbdFrOutDn/** Direction is Aft, Starboard, From Reference, Outside or Down. */,
                    StiffenerDirectionTypeFwdPortToInCtr/** Direction is Forward, Port, To Reference, Inside or Centered. */,
                    StiffenerDirectionTypeAftStbdFrOutCtr/** Direction is Aft, Starboard, From Reference, Outside or Centered. */
                };

                private: PlateSystemBuilderImpl * m_platesystembuilder_impl;
                private: friend class  _PlateSystemBuilderBuilder;
                protected: PlateSystemBuilder();
                public: ~PlateSystemBuilder();
                /**Returns  the sheet bodies or datum planes selected, or a face collector used to define the boundary of the plate system. The
                            selected objects are intersected with the specified mold face to define regions. The regions desired to form the
                            plate system can then be selected. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectNXObjectList * BoundarySheets
                (
                );
                /**Returns  the section containing curves that define the boundary of the plate system. The curves will 
                            be projected onto the mold face to define regions. The regions desired to form the
                            plate system can then be selected. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Section * BoundarySection
                (
                );
                /**Returns  the plane defined to indicate the boundary of the plate system. The
                            defined plane is intersected with the specified mold face to define regions. The regions desired to form the
                            plate system can then be selected. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Plane * BoundaryPlane
                (
                );
                /**Sets  the plane defined to indicate the boundary of the plate system. The
                            defined plane is intersected with the specified mold face to define regions. The regions desired to form the
                            plate system can then be selected. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetBoundaryPlane
                (
                    NXOpen::Plane * boundaryPlane /** boundaryplane */ 
                );
                /**Returns  the direction used to project
                            the boundary section curves onto the mold face.  
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::GeometricUtilities::ProjectionOptions * ProjectionDirection
                (
                );
                /**Returns  the thickness direction builder, used to specify the thickness direction from the mold face. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::ThicknessDirectionBuilder * ThicknessDirection
                (
                );
                /**Returns  the regions selected from the sheet, that has the inscribed boundaries, to keep for the final 
                            plate system shape. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::RegionPointList * Regions
                (
                );
                /**Returns  the offset to apply to the selected mold face to produce the desired mold face. The offset is applied 
                            in the thickness direction specified. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Offset
                (
                );
                /**Returns  the plate stock builder, used to define the plate material, grade, 
                            thickness, mass density, and thicken option. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::PlateStockBuilder * Stock
                (
                );
                /**Returns  the welding characteristics builder, used to assign welding characteristics to the outermost edges of a plate system. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Weld::CharacteristicsBuilder * Weld
                (
                );
                /**Returns  the tightness desired for the plate system. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: int Tightness
                (
                );
                /**Sets  the tightness desired for the plate system. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetTightness
                (
                    int tightness /** tightness */ 
                );
                /** Set the points derived from the regions of the sheet, that has the inscribed boundaries, to keep for the final 
                            plate system shape. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetRegionPoints
                (
                    const std::vector<NXOpen::Point3d> & regionPoints /** Points representing the kept regions. */
                );
                /** Create the region body that has the inscribed boundaries. The region body is used to select the regions that are kept for the final
                            plate system shape.
                            Any region body created should be deleted by using the method @link Features::ShipDesign::PlateSystemBuilder::DeleteRegionBody Features::ShipDesign::PlateSystemBuilder::DeleteRegionBody@endlink .
                            If a region body is created when there is already a current region body, that current region body will be deleted.
                            When the builder is committed, the region point coordinates from method
                            @link Features::ShipDesign::PlateSystemBuilder::SetRegionPoints Features::ShipDesign::PlateSystemBuilder::SetRegionPoints@endlink  will be used to identify the regions desired.  @return  Body associated with the select region point. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: NXOpen::Body * CreateRegionBody
                (
                );
                /** Delete the current region body. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void DeleteRegionBody
                (
                );
                /**Returns  the primary stiffener direction. This indicates which side of the plate system the 
                            stiffener should be placed upon. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::PlateSystemBuilder::StiffenerDirectionType Primary
                (
                );
                /**Sets  the primary stiffener direction. This indicates which side of the plate system the 
                            stiffener should be placed upon. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetPrimary
                (
                    NXOpen::Features::ShipDesign::PlateSystemBuilder::StiffenerDirectionType primary /** primary */ 
                );
                /**Returns  the primary stiffener direction when the plate system is located on a midship reference. 
                            This indicates which side of the plate system the 
                            stiffener should be placed upon. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::PlateSystemBuilder::StiffenerDirectionType PrimaryOnReference
                (
                );
                /**Sets  the primary stiffener direction when the plate system is located on a midship reference. 
                            This indicates which side of the plate system the 
                            stiffener should be placed upon. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetPrimaryOnReference
                (
                    NXOpen::Features::ShipDesign::PlateSystemBuilder::StiffenerDirectionType primaryOnReference /** primaryonreference */ 
                );
                /**Returns  the direction of the stiffener flange. The usage and settings depends on the type of 
                            plate system the stiffener is being placed upon, and the general direction of the 
                            stiffener itself. When the stiffener has the possibility of two general directions, 
                            then the value of Secondary2 may also be utilized. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::PlateSystemBuilder::StiffenerDirectionType Secondary1
                (
                );
                /**Sets  the direction of the stiffener flange. The usage and settings depends on the type of 
                            plate system the stiffener is being placed upon, and the general direction of the 
                            stiffener itself. When the stiffener has the possibility of two general directions, 
                            then the value of Secondary2 may also be utilized. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetSecondary1
                (
                    NXOpen::Features::ShipDesign::PlateSystemBuilder::StiffenerDirectionType secondary1 /** secondary1 */ 
                );
                /**Returns  the direction of the stiffener flange when the stiffener is located on a midship reference. 
                            The usage and settings depends on the type of 
                            plate system the stiffener is being placed upon, and the general direction of the 
                            stiffener itself. When the stiffener has the possibility of two general directions, 
                            then the value of Secondary2 may also be utilized. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::PlateSystemBuilder::StiffenerDirectionType Secondary1OnReference
                (
                );
                /**Sets  the direction of the stiffener flange when the stiffener is located on a midship reference. 
                            The usage and settings depends on the type of 
                            plate system the stiffener is being placed upon, and the general direction of the 
                            stiffener itself. When the stiffener has the possibility of two general directions, 
                            then the value of Secondary2 may also be utilized. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetSecondary1OnReference
                (
                    NXOpen::Features::ShipDesign::PlateSystemBuilder::StiffenerDirectionType secondary1OnReference /** secondary1onreference */ 
                );
                /**Returns  the direction of the stiffener flange. The usage and settings depends on the type of 
                            plate system the stiffener is being placed upon, and the general direction of the 
                            stiffener itself. When the stiffener has the possibility of two general directions, 
                            then the value of Secondary1 may also be utilized. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::PlateSystemBuilder::StiffenerDirectionType Secondary2
                (
                );
                /**Sets  the direction of the stiffener flange. The usage and settings depends on the type of 
                            plate system the stiffener is being placed upon, and the general direction of the 
                            stiffener itself. When the stiffener has the possibility of two general directions, 
                            then the value of Secondary1 may also be utilized. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetSecondary2
                (
                    NXOpen::Features::ShipDesign::PlateSystemBuilder::StiffenerDirectionType secondary2 /** secondary2 */ 
                );
                /**Returns  the direction of the stiffener flange when the stiffener is located on a midship reference. 
                            The usage and settings depends on the type of 
                            plate system the stiffener is being placed upon, and the general direction of the 
                            stiffener itself. When the stiffener has the possibility of two general directions, 
                            then the value of Secondary1 may also be utilized. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::PlateSystemBuilder::StiffenerDirectionType Secondary2OnReference
                (
                );
                /**Sets  the direction of the stiffener flange when the stiffener is located on a midship reference. 
                            The usage and settings depends on the type of 
                            plate system the stiffener is being placed upon, and the general direction of the 
                            stiffener itself. When the stiffener has the possibility of two general directions, 
                            then the value of Secondary1 may also be utilized. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetSecondary2OnReference
                (
                    NXOpen::Features::ShipDesign::PlateSystemBuilder::StiffenerDirectionType secondary2OnReference /** secondary2onreference */ 
                );
                /** Sets the knuckle edges, which includes edges for both bend and split types. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetKnuckleEdges
                (
                    const std::vector<NXOpen::TaggedObject *> & knuckleEdges /** G0 edges or camber curves with special attribute*/
                );
                /**Returns  the split knuckle edges, which are used to create seam feature to split a plate system into plate subsystem. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: NXOpen::SelectNXObjectList * SplitKnuckleEdges
                (
                );
                /** Sets the flag to indicate that split knuckle edges are out of date and need to update. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetSplitEdgeUpdateFlag
                (
                    bool isSplitEdgeUpdate /** issplitedgeupdate */ 
                );
                /** Cleans up the temp curves. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void CleanUpTemporaryCurves
                (
                );
                /** Sets the region index. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetRegionIndex
                (
                    const std::vector<int> & indexArray /** indexarray */ 
                );
                /** Deletes the preview body. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void DeletePreviewBody
                (
                    bool bDelete /** bdelete */ 
                );
                /** Sets the preview option. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetPreviewOption
                (
                    bool bPreview /** bpreview */ 
                );
            };
        }
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
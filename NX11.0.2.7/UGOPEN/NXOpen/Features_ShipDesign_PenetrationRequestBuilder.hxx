#ifndef NXOpen_FEATURES_SHIPDESIGN_PENETRATIONREQUESTBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_PENETRATIONREQUESTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_PenetrationRequestBuilder.ja
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
#include <NXOpen/Features_ShipDesign_PenetrationRequest.hxx>
#include <NXOpen/Features_ShipDesign_PenetrationRequestBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
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
            class PenetrationRequestBuilder;
        }
    }
    class Body;
    class Builder;
    class Direction;
    class Expression;
    class NXObject;
    class Point;
    class Section;
    class SelectNXObject;
    class SelectNXObjectList;
    class Sketch;
    namespace Features
    {
        namespace ShipDesign
        {
            class _PenetrationRequestBuilderBuilder;
            class PenetrationRequestBuilderImpl;
            /** Represents a @link NXOpen::Features::ShipDesign::PenetrationRequest NXOpen::Features::ShipDesign::PenetrationRequest@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Features::ShipDesign::PenetrationRequestCollection::CreatePenetrationRequestBuilder  NXOpen::Features::ShipDesign::PenetrationRequestCollection::CreatePenetrationRequestBuilder @endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            CompensationType </td> <td> 
             
            NotRequired </td> </tr> 

            <tr><td> 
             
            CornerRadius.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            CoutoutType </td> <td> 
             
            Circular </td> </tr> 

            <tr><td> 
             
            Cut </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            Diameter.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            DirectionType </td> <td> 
             
            PerpendiculartoStructure </td> </tr> 

            <tr><td> 
             
            Hanger </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            Height.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            Offset.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            PenetrationType </td> <td> 
             
            PenetratingObject </td> </tr> 

            <tr><td> 
             
            Radius.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            RequestType </td> <td> 
             
            Single </td> </tr> 

            <tr><td> 
             
            Spill </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            Width.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            </table>  

             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  PenetrationRequestBuilder : public NXOpen::Builder
            {
                /** Represents the dialog type */
                public: enum RequestDialogType
                {
                    RequestDialogTypeUnknown/** unknown */ ,
                    RequestDialogTypeCreate/** create */ ,
                    RequestDialogTypeModify/** modify */ ,
                    RequestDialogTypeRevise/** revise */ ,
                    RequestDialogTypeAssociate/** associate */ ,
                    RequestDialogTypeEditAssociate/** edit associate */ 
                };

                private: PenetrationRequestBuilderImpl * m_penetrationrequestbuilder_impl;
                private: friend class  _PenetrationRequestBuilderBuilder;
                protected: PenetrationRequestBuilder();
                public: ~PenetrationRequestBuilder();
                /**Returns  the request type 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::PenetrationRequest::RequestType RequestType
                (
                );
                /**Sets  the request type 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void SetRequestType
                (
                    NXOpen::Features::ShipDesign::PenetrationRequest::RequestType enumRequestType /** enumrequesttype */ 
                );
                /**Returns  the request name 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString RequestName
                (
                );
                /**Sets  the request name 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void SetRequestName
                (
                    const NXString & stringName /** stringname */ 
                );
                /**Sets  the request name 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                void SetRequestName
                (
                    const char * stringName /** stringname */ 
                );
                /** Returns the description  @return  
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: std::vector<NXString> GetRequestDescription
                (
                );
                /** Sets the description 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void SetRequestDescription
                (
                    const std::vector<NXString> & stringDesc /** stringdesc */ 
                );
                /**Returns  the penetration type 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::PenetrationRequest::PenetrationType PenetrationType
                (
                );
                /**Sets  the penetration type 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void SetPenetrationType
                (
                    NXOpen::Features::ShipDesign::PenetrationRequest::PenetrationType enumPenetrationType /** enumpenetrationtype */ 
                );
                /**Returns  the route penetrating 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectNXObjectList * RoutePenetrating
                (
                );
                /**Returns  the selected segment 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::NXObject * SelectedSegment
                (
                );
                /**Sets  the selected segment 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void SetSelectedSegment
                (
                    NXOpen::NXObject * selectedSegment /** selectedsegment */ 
                );
                /**Returns  the route object collector 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectNXObjectList * RouteObjectCollector
                (
                );
                /**Returns  the penetrating point 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * Point
                (
                );
                /**Sets  the penetrating point 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void SetPoint
                (
                    NXOpen::Point * pointPenetrating /** pointpenetrating */ 
                );
                /**Returns  the selection structure 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectNXObject * SelectionStructure
                (
                );
                /**Adds adjacent structures 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void AddAdjacentStructure
                (
                    NXOpen::Body * adjacentStructure /** adjacentstructure */ 
                );
                /**Returns  the coutout type 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::PenetrationRequest::CoutoutType CoutoutType
                (
                );
                /**Sets  the coutout type 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void SetCoutoutType
                (
                    NXOpen::Features::ShipDesign::PenetrationRequest::CoutoutType enumCoutoutType /** enumcoutouttype */ 
                );
                /**Returns  the diameter expression 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Diameter
                (
                );
                /**Returns  the offset expression 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Offset
                (
                );
                /**Returns  the height expression 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Height
                (
                );
                /**Returns  the width expression 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Width
                (
                );
                /**Returns  the radius expression 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Radius
                (
                );
                /**Returns  the corner radius expression 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * CornerRadius
                (
                );
                /**Returns  the hole type 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXString HoleType
                (
                );
                /**Sets  the hole type 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void SetHoleType
                (
                    const NXString & stringHoleType /** stringholetype */ 
                );
                /**Sets  the hole type 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                void SetHoleType
                (
                    const char * stringHoleType /** stringholetype */ 
                );
                /**Returns  the hole sub-type 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXString HoleSubType
                (
                );
                /**Sets  the hole sub-type 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void SetHoleSubType
                (
                    const NXString & stringHoleType /** stringholetype */ 
                );
                /**Sets  the hole sub-type 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                void SetHoleSubType
                (
                    const char * stringHoleType /** stringholetype */ 
                );
                /**Returns  the sketch 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Section * Sketch
                (
                );
                /**Returns  the modified sketch 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Sketch * ModifiedSketch
                (
                );
                /**Sets  the modified sketch 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void SetModifiedSketch
                (
                    NXOpen::Sketch * modifiedSketch /** modifiedsketch */ 
                );
                /**Returns  the direction 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::PenetrationRequest::DirectionType DirectionType
                (
                );
                /**Sets  the direction 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void SetDirectionType
                (
                    NXOpen::Features::ShipDesign::PenetrationRequest::DirectionType enumDirection /** enumdirection */ 
                );
                /**Returns  the orientation 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Direction * Orientation
                (
                );
                /**Sets  the orientation 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void SetOrientation
                (
                    NXOpen::Direction * vectorOrientation /** vectororientation */ 
                );
                /**Returns  the horizontal direction 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Direction * HorizontalDirection
                (
                );
                /**Sets  the horizontal direction 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void SetHorizontalDirection
                (
                    NXOpen::Direction * vectorHorizontalDirection /** vectorhorizontaldirection */ 
                );
                /**Returns  the compensation type 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::PenetrationRequest::CompensationType CompensationType
                (
                );
                /**Sets  the compensation type 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void SetCompensationType
                (
                    NXOpen::Features::ShipDesign::PenetrationRequest::CompensationType enumCompensationType /** enumcompensationtype */ 
                );
                /**Returns  the selection compensation 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectNXObject * SelectionCompensation
                (
                );
                /**Returns  the compensation number 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString CompensationNumber
                (
                );
                /**Sets  the compensation number 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") */
                public: void SetCompensationNumber
                (
                    const NXString & stringCompensationNumber /** stringcompensationnumber */ 
                );
                /**Sets  the compensation number 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") */
                void SetCompensationNumber
                (
                    const char * stringCompensationNumber /** stringcompensationnumber */ 
                );
                /**Returns  the hanger 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: bool Hanger
                (
                );
                /**Sets  the hanger 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") */
                public: void SetHanger
                (
                    bool toggleHanger /** togglehanger */ 
                );
                /**Returns  the selection hanger 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectNXObject * SelectionHanger
                (
                );
                /**Returns  the hanger number 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString HangerNumber
                (
                );
                /**Sets  the hanger number 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") */
                public: void SetHangerNumber
                (
                    const NXString & stringHangerNumber /** stringhangernumber */ 
                );
                /**Sets  the hanger number 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") */
                void SetHangerNumber
                (
                    const char * stringHangerNumber /** stringhangernumber */ 
                );
                /**Returns  the due date 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString DueDate
                (
                );
                /**Sets  the due date 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") */
                public: void SetDueDate
                (
                    const NXString & stringDueDate /** stringduedate */ 
                );
                /**Sets  the due date 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") */
                void SetDueDate
                (
                    const char * stringDueDate /** stringduedate */ 
                );
                /**Returns  the cut 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: bool Cut
                (
                );
                /**Sets  the cut 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") */
                public: void SetCut
                (
                    bool toggleCut /** togglecut */ 
                );
                /**Returns  the spill 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: bool Spill
                (
                );
                /**Sets  the spill 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") */
                public: void SetSpill
                (
                    bool toggleSpill /** togglespill */ 
                );
                /**Returns  the dialog type 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::PenetrationRequestBuilder::RequestDialogType DialogType
                (
                );
                /**Sets  the dialog type 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") */
                public: void SetDialogType
                (
                    NXOpen::Features::ShipDesign::PenetrationRequestBuilder::RequestDialogType dialogType /** dialogtype */ 
                );
                /** Adds nonintersected structures 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void AddNonIntersectedStructure
                (
                    NXOpen::Body * structure /** structure */ 
                );
                /** Removes all nonintersected structures 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void RemoveNonIntersectedStructures
                (
                );
                /** Removes all adjacent structures 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void RemoveAllAdjacentStructures
                (
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

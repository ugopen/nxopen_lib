#ifndef NXOpen_FEATURES_SHIPDESIGN_PENETRATIONASSOCIATIONBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_PENETRATIONASSOCIATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_PenetrationAssociationBuilder.ja
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
#include <NXOpen/Features_ShipDesign_PenetrationAssociationBuilder.hxx>
#include <NXOpen/Features_ShipDesign_PenetrationRequest.hxx>
#include <NXOpen/Builder.hxx>
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
        namespace ShipDesign
        {
            class PenetrationAssociationBuilder;
        }
    }
    class Body;
    class Builder;
    class Expression;
    namespace Features
    {
        namespace ShipDesign
        {
            class PenetrationRequest;
        }
    }
    class Part;
    class Point;
    class Section;
    class Sketch;
    namespace Features
    {
        namespace ShipDesign
        {
            class _PenetrationAssociationBuilderBuilder;
            class PenetrationAssociationBuilderImpl;
            /** Represents a @link NXOpen::Features::ShipDesign::PenetrationAssociationBuilder NXOpen::Features::ShipDesign::PenetrationAssociationBuilder@endlink  builder   <br> To create a new instance of this class, use @link NXOpen::Features::ShipDesign::PenetrationRequestCollection::CreatePenetrationAssociationBuilder  NXOpen::Features::ShipDesign::PenetrationRequestCollection::CreatePenetrationAssociationBuilder @endlink  <br> 
             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  PenetrationAssociationBuilder : public NXOpen::Builder
            {
                private: PenetrationAssociationBuilderImpl * m_penetrationassociationbuilder_impl;
                private: friend class  _PenetrationAssociationBuilderBuilder;
                protected: PenetrationAssociationBuilder();
                public: ~PenetrationAssociationBuilder();
                /**Returns  the penetration point 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * Point
                (
                );
                /**Sets  the penetration point 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void SetPoint
                (
                    NXOpen::Point * point /** point */ 
                );
                /** Used to open the cutout dialog 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void ButtonCutout
                (
                );
                /**Returns  the coutout type 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::PenetrationRequest::CoutoutType CoutoutType
                (
                );
                /**Sets  the coutout type 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void SetCoutoutType
                (
                    NXOpen::Features::ShipDesign::PenetrationRequest::CoutoutType enumCoutoutType /** enumcoutouttype */ 
                );
                /**Returns  the diameter expression 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Diameter
                (
                );
                /**Returns  the offset expression 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Offset
                (
                );
                /**Returns  the height expression 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Height
                (
                );
                /**Returns  the width expression 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Width
                (
                );
                /**Returns  the radius expression 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Radius
                (
                );
                /**Returns  the corner radius expression 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * CornerRadius
                (
                );
                /**Returns  the sketch 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Section * SketchSection
                (
                );
                /**Sets  the sketch 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void SetSketchSection
                (
                    NXOpen::Section * sectionSketch /** sectionsketch */ 
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
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::PenetrationRequest::DirectionType DirectionType
                (
                );
                /**Sets  the direction 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void SetDirectionType
                (
                    NXOpen::Features::ShipDesign::PenetrationRequest::DirectionType enumDirection /** enumdirection */ 
                );
                /**Returns  the flag to decide whether to keep association 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: bool IsKeepAssociation
                (
                );
                /**Sets  the flag to decide whether to keep association 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void SetKeepAssociation
                (
                    bool isKeepAssociation /** iskeepassociation */ 
                );
                /**Returns  the flag to decide if it's requests association or associated requests editing 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: bool IsEditMode
                (
                );
                /**Sets  the flag to decide if it's requests association or associated requests editing 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void SetEditMode
                (
                    bool isEditMode /** iseditmode */ 
                );
                /**Returns  the cutout part
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Part * CutoutPart
                (
                );
                /**Sets  the cutout part
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void SetCutoutPart
                (
                    NXOpen::Part * cutoutPart /** cutoutpart */ 
                );
                /** Adds request object
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void AddRequest
                (
                    NXOpen::Features::ShipDesign::PenetrationRequest * request /** request */ 
                );
                /** Adds adjacent structures 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void AddAdjacentStructure
                (
                    NXOpen::Body * adjacentStructure /** adjacentstructure */ 
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
                /** Adds selected curves 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void AddSelectedCurve
                (
                    NXOpen::Body * curve /** curve */ 
                );
                /** Removes all selected curves 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void RemoveSelectedCurves
                (
                );
                /** The selection compensation 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                public: void SetCompensationPartNumber
                (
                    const NXString & selectionCompensationNumber /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
                );
                /** The selection compensation 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_penetration_mgmt ("Penetration Management") */
                void SetCompensationPartNumber
                (
                    const char * selectionCompensationNumber /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
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

#ifndef NXOpen_LINEDESIGNER_FLOOREQUIPMENTBUILDER_HXX_INCLUDED
#define NXOpen_LINEDESIGNER_FLOOREQUIPMENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     LineDesigner_FloorEquipmentBuilder.ja
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
#include <NXOpen/KFObject.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/liblinedesigneropencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace LineDesigner
    {
        class FloorEquipmentBuilder;
    }
    class Builder;
    class Expression;
    class KFObject;
    class Section;
    namespace LineDesigner
    {
        class _FloorEquipmentBuilderBuilder;
        class FloorEquipmentBuilderImpl;
        /**    <br> To create a new instance of this class, use @link NXOpen::LineDesigner::LineDesignerManager::CreateFloorequipmentBuilder  NXOpen::LineDesigner::LineDesignerManager::CreateFloorequipmentBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        FloorThickness.Value </term> <description> 
         
        254 (millimeters part), 10 (inches part) </description> </item> 

        </list> 

         <br>  Created in NX9.0.0.  <br>  
        */
        class LINEDESIGNEROPENCPPEXPORT  FloorEquipmentBuilder : public NXOpen::Builder
        {
            private: FloorEquipmentBuilderImpl * m_floorequipmentbuilder_impl;
            private: friend class  _FloorEquipmentBuilderBuilder;
            protected: FloorEquipmentBuilder();
            public: ~FloorEquipmentBuilder();
            /**Returns  the outline used for creation of floor is return 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::Section * SelectOutline
            (
            );
            /**Returns  the floor thickness 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::Expression * FloorThickness
            (
            );
            /**Returns  the kf object 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: NXOpen::KFObject * KfObject
            (
            );
            /**Returns  the make sketchiInternal  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: bool MakeSketchInternal
            (
            );
            /**Sets  the make sketchiInternal  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ld_line_designer ("FULL LINE DESIGNER") */
            public: void SetMakeSketchInternal
            (
                bool makeSketchInternal /** makesketchinternal */ 
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
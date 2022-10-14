#ifndef NXOpen_FEATURES_SHIPDESIGN_PILLARSYSTEMBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_PILLARSYSTEMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_PillarSystemBuilder.ja
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
#include <NXOpen/Features_ShipDesign_ProfileSystemBuilder.hxx>
#include <NXOpen/Features_ShipDesign_PillarSystemBuilder.hxx>
#include <NXOpen/Features_ShipDesign_PointPairBuilder.hxx>
#include <NXOpen/Features_ShipDesign_SteelFeatureSpreadsheetBuilder.hxx>
#include <NXOpen/ObjectList.hxx>
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
            class PillarSystemBuilder;
        }
    }
    class Direction;
    class Expression;
    namespace Features
    {
        namespace ShipDesign
        {
            class PointPairBuilder;
        }
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class ProfileSystemBuilder;
        }
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class SteelFeatureSpreadsheetBuilder;
        }
    }
    class NXObjectList;
    class SelectNXObjectList;
    class SelectTaggedObject;
    namespace Features
    {
        namespace ShipDesign
        {
            class _PillarSystemBuilderBuilder;
            class PillarSystemBuilderImpl;
            /**
                Represents a @link Features::ShipDesign::PillarSystem Features::ShipDesign::PillarSystem@endlink  builder which is used to create or edit a pillar system feature.
                 <br> To create a new instance of this class, use @link Features::ShipCollection::CreatePillarSystemBuilder  Features::ShipCollection::CreatePillarSystemBuilder @endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            OrientationAngle.Value </td> <td> 
             
            0 </td> </tr> 

            </table>  

             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  PillarSystemBuilder : public Features::ShipDesign::ProfileSystemBuilder
            {
                /** Used to specify how the pillar system is defined. */
                public: enum Types
                {
                    TypesShipStructure/** ship structure */ ,
                    TypesPoints/** points */ 
                };

                private: PillarSystemBuilderImpl * m_pillarsystembuilder_impl;
                private: friend class  _PillarSystemBuilderBuilder;
                protected: PillarSystemBuilder();
                public: ~PillarSystemBuilder();
                /**Returns  the stock data used to define the stock information of the stiffener.
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::SteelFeatureSpreadsheetBuilder * StockData
                (
                );
                /**Returns  the ship structure to intersect with each other that defines the start of a pillar. Only used when Type is Features.ShipDesign.PillarSystemBuilder.Types.ShipStructure. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectNXObjectList * IntersectingShipStructure
                (
                );
                /**Returns  the ship sructure that defines the end of the pillar. Only used when Type is Features.ShipDesign.PillarSystemBuilder.Types.ShipStructure. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectNXObjectList * LimitingShipStructure
                (
                );
                /**Returns  the direction of the pillar. Only used when Type is Features.ShipDesign.PillarSystemBuilder.Types.ShipStructure. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Direction * Direction
                (
                );
                /**Sets  the direction of the pillar. Only used when Type is Features.ShipDesign.PillarSystemBuilder.Types.ShipStructure. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetDirection
                (
                    NXOpen::Direction * direction /** direction */ 
                );
                /**Returns  the list of pairs of points that define the ends of the pillars. Only used when Type is Features.ShipDesign.PillarSystemBuilder.Types.Points. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::NXObjectList * PointPairList
                (
                );
                /**Returns  the angle at which to orient the stock shape. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * OrientationAngle
                (
                );
                /**Returns  the type of input used to define the pillar location. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::PillarSystemBuilder::Types Type
                (
                );
                /**Sets  the type of input used to define the pillar location. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetType
                (
                    NXOpen::Features::ShipDesign::PillarSystemBuilder::Types type /** type */ 
                );
                /** Creates a @link Features::ShipDesign::PointPairBuilder Features::ShipDesign::PointPairBuilder@endlink .  @return  
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: NXOpen::Features::ShipDesign::PointPairBuilder * CreatePointPairBuilder
                (
                );
                /**Returns  the orientation line, used only if the creation method is "Specify Line". 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectTaggedObject * OrientationLine
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
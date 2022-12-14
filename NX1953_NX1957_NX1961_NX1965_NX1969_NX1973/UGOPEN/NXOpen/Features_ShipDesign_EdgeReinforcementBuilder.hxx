#ifndef NXOpen_FEATURES_SHIPDESIGN_EDGEREINFORCEMENTBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_EDGEREINFORCEMENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_EdgeReinforcementBuilder.ja
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
#include <NXOpen/Features_ShipDesign_EndCutBuilder.hxx>
#include <NXOpen/Features_ShipDesign_OrientationDefinitionBuilder.hxx>
#include <NXOpen/Features_ShipDesign_ShipNamesBuilder.hxx>
#include <NXOpen/Features_ShipDesign_StiffenerStockBuilder.hxx>
#include <NXOpen/Features_ShipDesign_ProfileSystemBuilder.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/Weld_CharacteristicsBuilder.hxx>
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
            class EdgeReinforcementBuilder;
        }
    }
    class Direction;
    class Expression;
    namespace Features
    {
        namespace ShipDesign
        {
            class EndCutBuilder;
        }
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class OrientationDefinitionBuilder;
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
            class ShipNamesBuilder;
        }
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class StiffenerStockBuilder;
        }
    }
    class Section;
    namespace Weld
    {
        class CharacteristicsBuilder;
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class _EdgeReinforcementBuilderBuilder;
            class EdgeReinforcementBuilderImpl;
            /**
                      Represents a @link NXOpen::Features::ShipDesign::EdgeReinforcement NXOpen::Features::ShipDesign::EdgeReinforcement@endlink  builder which is used to create or edit a edge reinforcement system feature.
                      <br> To create a new instance of this class, use @link NXOpen::Features::ShipCollection::CreateEdgeReinforcementBuilder  NXOpen::Features::ShipCollection::CreateEdgeReinforcementBuilder @endlink  <br> 
            Default values.
            <list type="table"> 
             
            <listheader><term> 
            Property</term>  <description> 
            Value</description> </listheader>
            <item><term> 
             
            EndCutEnd </term> <description> 
             
            Connected </description> </item> 

            <item><term> 
             
            EndCutStart </term> <description> 
             
            Connected </description> </item> 

            <item><term> 
             
            EndEndCut.ConnectionType </term> <description> 
             
            Connected </description> </item> 

            <item><term> 
             
            EndEndCut.DraftAngle.Value </term> <description> 
             
            0 </description> </item> 

            <item><term> 
             
            EndEndCut.DraftOffset.Value </term> <description> 
             
            0 (millimeters part), 0 (inches part) </description> </item> 

            <item><term> 
             
            EndEndCut.DraftType </term> <description> 
             
            Trim </description> </item> 

            <item><term> 
             
            EndEndCut.EndFaceType </term> <description> 
             
            NeatTrim </description> </item> 

            <item><term> 
             
            EndEndCut.LimitType </term> <description> 
             
            Value </description> </item> 

            <item><term> 
             
            EndEndCut.Offset.Value </term> <description> 
             
            0 (millimeters part), 0 (inches part) </description> </item> 

            <item><term> 
             
            EndEndCut.SelectionType </term> <description> 
             
            FacesWithAttributes </description> </item> 

            <item><term> 
             
            EndEndCut.ShearAngle.Value </term> <description> 
             
            0 </description> </item> 

            <item><term> 
             
            EndEndCut.TiltAngle.Value </term> <description> 
             
            0 </description> </item> 

            <item><term> 
             
            OrientationAngle.Value </term> <description> 
             
            0 </description> </item> 

            <item><term> 
             
            OrientationDefinitionBuilder.MeasureAngles </term> <description> 
             
            NormaltoCurve </description> </item> 

            <item><term> 
             
            OrientationDefinitionBuilder.ShowSurfaceAngles </term> <description> 
             
            0 </description> </item> 

            <item><term> 
             
            OrientationDefinitionBuilder.ShowTwistRate </term> <description> 
             
            0 </description> </item> 

            <item><term> 
             
            OrientationDefinitionBuilder.ShowWebAngles </term> <description> 
             
            0 </description> </item> 

            <item><term> 
             
            OrientationMethod </term> <description> 
             
            FaceNormal </description> </item> 

            <item><term> 
             
            StockData.AnchorPoint </term> <description> 
             
            0 </description> </item> 

            <item><term> 
             
            StockData.PlateHeight.Value </term> <description> 
             
            50 (millimeters part), 2 (inches part) </description> </item> 

            <item><term> 
             
            StockData.PlateStockData.KnuckleRatio </term> <description> 
             
            3.0 </description> </item> 

            <item><term> 
             
            StockData.PlateStockData.KnuckleSmoothAngle </term> <description> 
             
            3.0 </description> </item> 

            <item><term> 
             
            StockData.PlateStockData.MaterialOption </term> <description> 
             
            0 </description> </item> 

            <item><term> 
             
            StockData.PlateStockData.OppositeThickness.Value </term> <description> 
             
            0 (millimeters part), 0 (inches part) </description> </item> 

            <item><term> 
             
            StockData.PlateStockData.RestrictThicknessToMaterial </term> <description> 
             
            true </description> </item> 

            <item><term> 
             
            StockData.PlateStockData.ThickenOption </term> <description> 
             
            SingleSided </description> </item> 

            <item><term> 
             
            StockData.PlateStockData.Thickness.Value </term> <description> 
             
            10 (millimeters part), 0.5 (inches part) </description> </item> 

            <item><term> 
             
            StockData.PlateStockData.ThicknessSourceOption </term> <description> 
             
            List </description> </item> 

            <item><term> 
             
            StockData.SectionType </term> <description> 
             
            Profile </description> </item> 

            </list> 

             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  EdgeReinforcementBuilder : public NXOpen::Features::ShipDesign::ProfileSystemBuilder
            {
                /** Used to specify how the edge reinforcement system is defined. */
                public: enum Types
                {
                    TypesOnEdge/** on edge */ ,
                    TypesOnFace/** on face */ 
                };

                /** Used to specify the type of reference to use for specifying the orientation of the edge reinforcement system. */
                public: enum OrientationMethods
                {
                    OrientationMethodsFaceNormal/** face normal */ ,
                    OrientationMethodsVector/** vector */ 
                };

                /** Used to specify the type of end cut to be used at the extreme ends of the edge reinforcement system. */
                public: enum EndCutTypes
                {
                    EndCutTypesConnected/** connected */ ,
                    EndCutTypesFlangeFree/** flange free */ ,
                    EndCutTypesSniped/** sniped */ ,
                    EndCutTypesSnipedSquare/** sniped square */ ,
                    EndCutTypesNone/** none */ 
                };

                private: EdgeReinforcementBuilderImpl * m_edgereinforcementbuilder_impl;
                private: friend class  _EdgeReinforcementBuilderBuilder;
                protected: EdgeReinforcementBuilder();
                public: ~EdgeReinforcementBuilder();
                /**Returns  the stock data used to define the stock information of the edge reinforcement.
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::StiffenerStockBuilder * StockData
                (
                );
                /**Returns  the offset used for the offset distance from anchor point. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Offset
                (
                );
                /**Returns  the indication if the default direction of the flange is reverse or not. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: bool Reverse
                (
                );
                /**Sets  the indication if the default direction of the flange is reverse or not. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetReverse
                (
                    bool reverse /** reverse */ 
                );
                /**Returns  the flag that indicates if the attachment direction is reversed. 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : None */
                public: bool ReverseAttachmentDirection
                (
                );
                /**Sets  the flag that indicates if the attachment direction is reversed. 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetReverseAttachmentDirection
                (
                    bool reverse /** reverse */ 
                );
                /**Returns  the edges to reinforce. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Section * Edges
                (
                );
                /**Returns  the method used to orient the edge reinforcement. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::EdgeReinforcementBuilder::OrientationMethods OrientationMethod
                (
                );
                /**Sets  the method used to orient the edge reinforcement. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetOrientationMethod
                (
                    NXOpen::Features::ShipDesign::EdgeReinforcementBuilder::OrientationMethods orientationMethod /** orientationmethod */ 
                );
                /**Returns  the angle to use for the edge reinforcement orientation. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * OrientationAngle
                (
                );
                /**Returns  the builder used to specify the welding characteristics for the edge reinforcement. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Weld::CharacteristicsBuilder * Weld
                (
                );
                /**Returns  the type of placement being used in the edge reinforcement definition. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::EdgeReinforcementBuilder::Types Type
                (
                );
                /**Sets  the type of placement being used in the edge reinforcement definition. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetType
                (
                    NXOpen::Features::ShipDesign::EdgeReinforcementBuilder::Types type /** type */ 
                );
                /**Returns  the orientation vector when the orientation method is 
                              @link NXOpen::Features::ShipDesign::EdgeReinforcementBuilder::OrientationMethodsVector NXOpen::Features::ShipDesign::EdgeReinforcementBuilder::OrientationMethodsVector@endlink . 
                             
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Direction * OrientationVector
                (
                );
                /**Sets  the orientation vector when the orientation method is 
                              @link NXOpen::Features::ShipDesign::EdgeReinforcementBuilder::OrientationMethodsVector NXOpen::Features::ShipDesign::EdgeReinforcementBuilder::OrientationMethodsVector@endlink . 
                             
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetOrientationVector
                (
                    NXOpen::Direction * orientationVector /** orientationvector */ 
                );
                /**Returns  the builder used to define the orientation for the edge reinforcement system. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::OrientationDefinitionBuilder * OrientationDefinitionBuilder
                (
                );
                /**Returns  the end cut to use at the start of the edge reinforcement system. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::EdgeReinforcementBuilder::EndCutTypes EndCutStart
                (
                );
                /**Sets  the end cut to use at the start of the edge reinforcement system. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetEndCutStart
                (
                    NXOpen::Features::ShipDesign::EdgeReinforcementBuilder::EndCutTypes endCutStart /** endcutstart */ 
                );
                /**Returns  the end cut to use at the end of the edge reinforcement system. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::EdgeReinforcementBuilder::EndCutTypes EndCutEnd
                (
                );
                /**Sets  the end cut to use at the end of the edge reinforcement system. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetEndCutEnd
                (
                    NXOpen::Features::ShipDesign::EdgeReinforcementBuilder::EndCutTypes endCutEnd /** endcutend */ 
                );
                /**Returns  the Ship Names builder, used to assign names to the Edge Reinforcement Systems created. 
                 <br>  Created in NX9.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::ShipNamesBuilder * ShipNames
                (
                );
                /**Returns  the indication of whether to build a solid for the edge reinforcement or just the curve. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: bool BuildSolid
                (
                );
                /**Sets  the indication of whether to build a solid for the edge reinforcement or just the curve. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetBuildSolid
                (
                    bool buildSolid /** buildsolid */ 
                );
                /**Returns  the tolerance used to determine when knuckle locations are considered to be the same. 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: double KnuckleLocationTolerance
                (
                );
                /**Sets  the tolerance used to determine when knuckle locations are considered to be the same. 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetKnuckleLocationTolerance
                (
                    double knuckleLocationTolerance /** knucklelocationtolerance */ 
                );
                /**Returns  the flag that indicates if seams are to be created or updated at knuckle locations. 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: bool CreateSeamsAtKnuckles
                (
                );
                /**Sets  the flag that indicates if seams are to be created or updated at knuckle locations. 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetCreateSeamsAtKnuckles
                (
                    bool createSeams /** createseams */ 
                );
                /**Returns  the detailed start end cut. 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::EndCutBuilder * StartEndCut
                (
                );
                /**Returns  the detailed end end cut. 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::EndCutBuilder * EndEndCut
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

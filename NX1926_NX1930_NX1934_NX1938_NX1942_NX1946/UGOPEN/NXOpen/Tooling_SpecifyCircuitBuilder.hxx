#ifndef NXOpen_TOOLING_SPECIFYCIRCUITBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_SPECIFYCIRCUITBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_SpecifyCircuitBuilder.ja
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
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/Tooling_CoolingFittingData.hxx>
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
        class SpecifyCircuitBuilder;
    }
    class Body;
    class Builder;
    class NXColor;
    class NXObject;
    class Point;
    class SelectBody;
    class SelectBodyList;
    namespace Tooling
    {
        class CoolingFittingData;
    }
    namespace Tooling
    {
        class _SpecifyCircuitBuilderBuilder;
        class SpecifyCircuitBuilderImpl;
        /** Represents a builder to be used to create specify circuit.  <br> To create a new instance of this class, use @link NXOpen::Tooling::SpecifyCircuitCollection::CreateBuilder  NXOpen::Tooling::SpecifyCircuitCollection::CreateBuilder @endlink  <br> 
        Default values.
        <list type="table"> 
         
        <listheader><term> 
        Property</term>  <description> 
        Value</description> </listheader>
        <item><term> 
         
        CreateFittings </term> <description> 
         
        1 </description> </item> 

        <item><term> 
         
        KeepCircuit </term> <description> 
         
        0 </description> </item> 

        <item><term> 
         
        Layer </term> <description> 
         
        251 </description> </item> 

        <item><term> 
         
        UseSymbol </term> <description> 
         
        1 </description> </item> 

        </list> 

         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  SpecifyCircuitBuilder : public NXOpen::Builder
        {
            private: SpecifyCircuitBuilderImpl * m_specifycircuitbuilder_impl;
            private: friend class  _SpecifyCircuitBuilderBuilder;
            protected: SpecifyCircuitBuilder();
            public: ~SpecifyCircuitBuilder();
            /**Returns  the inlet channel. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBodyList * InletChannel
            (
            );
            /**Returns  the outlet channel. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBody * OutletChannel
            (
            );
            /** Check whether cooling circuit is finished or not. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void CheckStatus
            (
            );
            /**Returns  the option whether to keep the circuit displayed body.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool KeepCircuit
            (
            );
            /**Sets  the option whether to keep the circuit displayed body.
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetKeepCircuit
            (
                bool keepCircuit /** keepcircuit */ 
            );
            /**Returns  the value which specifies whether to add fittings or not. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool CreateFittings
            (
            );
            /**Sets  the value which specifies whether to add fittings or not. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetCreateFittings
            (
                bool createFittings /** createfittings */ 
            );
            /**Returns  the value which specifies whether to add real component or not. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseSymbol
            (
            );
            /**Sets  the value which specifies whether to add real component or not. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetUseSymbol
            (
                bool useSymbol /** usesymbol */ 
            );
            /**Returns  the circuit channel temperary body color. 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * CircuitColor
            (
            );
            /**Sets  the circuit channel temperary body color. 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetCircuitColor
            (
                NXOpen::NXColor * circuitColor /** circuitcolor */ 
            );
            /**Returns  the circuit channel body color. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * ChannelColor
            (
            );
            /**Sets  the circuit channel body color. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetChannelColor
            (
                NXOpen::NXColor * channelColor /** channelcolor */ 
            );
            /**Returns  the layer value for the selected channels. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: int Layer
            (
            );
            /**Sets  the layer value for the selected channels. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetLayer
            (
                int layer /** layer */ 
            );
            /** Returns the circuit channel body color.  @return  Array of 3 RGB values, each between 0 and 1 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<double> GetCircuitColor
            (
            );
            /** Sets the circuit color. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetCircuitColor
            (
                const std::vector<double> & circuitColor /** Array of 3 RGB values, each between 0 and 1 */
            );
            /** Gets intersect cooling list value. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void GetOneCircuit
            (
                const std::vector<NXOpen::Body *> & channels /** the cooling body*/
            );
            /** Initializes the circuit set data. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void InitializeCircuitSetData
            (
            );
            /** Creates the cooling fitting data object.  @return  the new @link NXOpen::Tooling::CoolingFittingData NXOpen::Tooling::CoolingFittingData@endlink  instance 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: NXOpen::Tooling::CoolingFittingData * CreateCoolingFittingData
            (
            );
            /** Gets the Cooling Fitting Data object. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: NXOpen::Tooling::CoolingFittingData * GetCoolingFittingData
            (
            );
            /** Adds a fitting point  to the deselect channel fitting points collector. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void AddADeselectedFittingPoint
            (
                NXOpen::Point * aFittingPoint /** afittingpoint */ 
            );
            /** Removes a fitting point from the deselect channel fitting points collector. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void RemoveADeselectedFittingPoint
            (
                NXOpen::Point * aFittingPoint /** afittingpoint */ 
            );
            /**Gets and records cooling fitting node information from standard part register file, including fitting type name, fitting type value, 
                    fitting bitmap, reuse part full path name, the flag to use reuse part or not, the relative location of the part family template,
                    the name of the library containing the part family template, the clone action type.
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetCoolingNodeInfo
            (
            );
            /**Creates manual link list for each circuit node, link list stores the information of each channel in one circuit
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void CreateManualLinkList
            (
                int arrowList /** arrowlist */ 
            );
            /**Sets the intersection information and inlet channel information. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetIntersectionAndInletInfo
            (
                NXOpen::Body * selectedChannel /** selectedchannel */ ,
                const NXOpen::Point3d & arrowList /** arrowlist */ 
            );
            /**Creates and displays the start channel arrow to indicate the inlet direction 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void CreateStartArrow
            (
                int nodeId /** nodeid */ ,
                double radius /** radius */ ,
                const NXOpen::Point3d & closestPoint /** closest point */ ,
                const NXOpen::Vector3d & faceVec /** face vec */ 
            );
            /**Sets circuit tree node update or not 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetCircuitTreeNodeUpdate
            (
                int nodeIndex /** nodeindex */ ,
                bool isUpdate /** isupdate */ 
            );
            /**Sets specified circuit color 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetSpecifiedCircuitColor
            (
                int nodeIndex /** nodeindex */ ,
                int nodeColor /** nodecolor */ 
            );
            /** Sets the channel type 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetChannelType
            (
                const NXString & channelType /** channeltype */ 
            );
            /** Sets the channel type 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            void SetChannelType
            (
                const char * channelType /** channeltype */ 
            );
            /**Removes one fitting point from specified circuit tree node
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void RemoveOneFittingPoint
            (
                int nodeIndex /** nodeindex */ ,
                NXOpen::Point * aPoint /** apoint */ 
            );
            /**Sets existing fitting point data details. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetExistingFittingPointDataDetails
            (
                const std::vector<NXOpen::Point *> & fittingPts /** fittingpts */ ,
                std::vector<NXString> & channelDiameters /** channeldiameters */ ,
                std::vector<NXString> & currentNames /** currentnames */ ,
                std::vector<NXString> & currentTypes /** currenttypes */ ,
                std::vector<NXString> & currentFitTypes /** currentfittypes */ ,
                std::vector<NXString> & baffleLengths /** bafflelengths */ ,
                const std::vector<bool> & fittingPointModified /** fittingpointmodified */ ,
                std::vector<NXString> & partNumbersTc /** partnumberstc */ 
            );
            /** Sets the selected circuit node  
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetCircuitSelNode
            (
                int circuitSelNode /** circuitselnode */ 
            );
            /** Removes parameters in link list that stores the information of each channel in one circuit and destroys this link list 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void RemoveParametersInLinkList
            (
                bool removeArrowAtIntersect /** removearrowatintersect */ ,
                bool removeStartArrow /** removestartarrow */ ,
                bool removeCreateBody /** removecreatebody */ ,
                bool removeFittingPoint /** removefittingpoint */ ,
                bool emptyStartStructure /** emptystartstructure */ ,
                bool doUpdate /** doupdate */ 
            );
            /**Empties new fitting point from specified circuit tree node
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void EmptyNewFittingPoint
            (
                int nodeIndex /** nodeindex */ 
            );
            /**Sets circuit tree node name
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetCircuitTreeNodeName
            (
                int nodeIndex /** nodeindex */ ,
                const NXString & nodeName /** nodename */ 
            );
            /**Sets circuit tree node name
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            void SetCircuitTreeNodeName
            (
                int nodeIndex /** nodeindex */ ,
                const char * nodeName /** nodename */ 
            );
            /**Removes inlet or outlet Label from specified circuit
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void RemoveLabel
            (
                int nodeIndex /** nodeindex */ ,
                NXOpen::NXObject * labelTag /** labeltag */ 
            );
            /**Removes one cooling arrow from specified circuit
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void RemoveOneCoolingArrow
            (
                int nodeIndex /** nodeindex */ ,
                NXOpen::NXObject * arrowTag /** arrowtag */ 
            );
            /**Blanks all the new created arrows in each intersect point of one circuit tree node, not include the inlet arrow.
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void BlankArrowsAtEachIntersection
            (
                int nodeIndex /** nodeindex */ 
            );
            /**Blanks or unblanks arrows at the intersect point.
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void BlankArrows
            (
                int nodeIndex /** nodeindex */ ,
                bool isBlank /** isblank */ 
            );
            /**Creates arrows at intersection
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void CreateArrowAtIntersection
            (
                int nodeIndex /** nodeindex */ 
            );
            /**Removes all temporary solids and lines and removes the attribute on the channels
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void RemoveAttributesAndTemporaryData
            (
                const std::vector<NXOpen::NXObject *> & nodeTag /** nodetag */ 
            );
            /**Clears the start collector data
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void ClearStartCollectorData
            (
            );
            /**Adds a channel attached by deleted point to channel list
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void AddAttachedChannelToChannelList
            (
                NXOpen::Body * attachedChannel /** attachedchannel */ 
            );
            /**Adds a deleted fitting point to deleted point list
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void AddDeletePointToDelPointList
            (
                NXOpen::Point * deleteFitPoint /** deletefitpoint */ 
            );
            /**Redisplays the arrow to get the new circuit
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void RedisplayArrow
            (
                int circuitNode /** circuitnode */ 
            );
            /** Records the blind end encountered or not. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : ug_mold_design ("UG MOLD") */
            public: void SetBlindEnd
            (
                bool isBlind /** isblind */ 
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

#ifndef NXOpen_ROUTING_CORNERTYPEBUILDER_HXX_INCLUDED
#define NXOpen_ROUTING_CORNERTYPEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_CornerTypeBuilder.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/Routing_CharacteristicList.hxx>
#include <NXOpen/Routing_CornerTypeBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Routing
    {
        class CornerTypeBuilder;
    }
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Routing
    {
        class CharacteristicList;
    }
    namespace Routing
    {
        class _CornerTypeBuilderBuilder;
        class CornerTypeBuilderImpl;
        /** Contains setting for corner creation. Type of bend to be created and the method to
                create the corner. 
            
            */
        class NXOPENCPPEXPORT  CornerTypeBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            /** Defines the type of bend available for bend creation.Type of bend available are None,Miter
                        ,Bend , S-bend and S-Elbow.
                      */
            public: enum Type
            {
                TypeNone/** none */ ,
                TypeMiter/** miter */ ,
                TypeBend/** bend */ ,
                TypeSBend/** sbend */ ,
                TypeSElbow/** selbow */ 
            };

            /** Methods available for bend creation.Three methods are available*/
            public: enum BendOptions
            {
                BendOptionsRadius/** Radius method allows corner creation with the specified radius value  */,
                BendOptionsRatioToDiameter/** Ratio to diameter method */,
                BendOptionsBendRadiusTable/** Bend table method creates bend from specified bend table*/
            };

            private: CornerTypeBuilderImpl * m_cornertypebuilder_impl;
            private: friend class  _CornerTypeBuilderBuilder;
            protected: CornerTypeBuilder();
            public: ~CornerTypeBuilder();
            /**Returns  the route corner type options  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::CornerTypeBuilder::Type RouteCornerTypeOptions
            (
            );
            /**Sets  the route corner type options  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetRouteCornerTypeOptions
            (
                NXOpen::Routing::CornerTypeBuilder::Type routeCornerTypeOptions /** routecornertypeoptions */ 
            );
            /**Returns  the route corner bend options  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::CornerTypeBuilder::BendOptions RouteCornerBendOptions
            (
            );
            /**Sets  the route corner bend options  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetRouteCornerBendOptions
            (
                NXOpen::Routing::CornerTypeBuilder::BendOptions routeCornerBendOptions /** routecornerbendoptions */ 
            );
            /**Returns  the route corner radius  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Expression * RouteCornerRadius
            (
            );
            /**Returns  the route corner ratio to diameter  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Expression * RouteCornerRatioToDiameter
            (
            );
            /** Route specify elbow  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void RouteCornerSpecifyElbow
            (
            );
            /**Returns  the route corner require linear solution  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: bool RouteCornerRequireLinearSolution
            (
            );
            /**Sets  the route corner require linear solution  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetRouteCornerRequireLinearSolution
            (
                bool routeCornerRequireLinearSolution /** routecornerrequirelinearsolution */ 
            );
            /** Route alternate solution <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void RouteCornerAlternateSolution
            (
            );
            /** Import bend radius table  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void RouteCornerImportBendRadiusTable
            (
            );
            /** Bend corner info  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void RouteCornerBendRadiusInfo
            (
            );
            /**Returns  the name of bend radius table <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString RouteCornerBendTable
            (
            );
            /**Sets  the name of bend radius table <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetRouteCornerBendTable
            (
                const NXString & bendTableName /** bendtablename */ 
            );
            /** Returns the created elbow part @return  Characteristic list used to find the appropriate  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::CharacteristicList * GetElbowPart
            (
            );
            /** Sets the elbow part to be used for elbow creation <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetElbowPart
            (
                NXOpen::Routing::CharacteristicList * elbowPart /** Characteristic list used to find the appropriate */
            );
            /** Returns the  applied charx of elbow part @return  Characteristic list used to find the appropriate  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Routing::CharacteristicList * GetElbowAppliedCharx
            (
            );
            /** Sets the applied charx for elbow creation <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetElbowAppliedCharx
            (
                NXOpen::Routing::CharacteristicList * elbowPart /** Characteristic list used to find the appropriate */
            );
            /** Returns true if the inputs to the component are sufficient for 
                        commit to be called.  For example, if the component requires
                        you to set some property, this method will return false if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful  <br> License requirements : None */
            public: virtual bool Validate
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif

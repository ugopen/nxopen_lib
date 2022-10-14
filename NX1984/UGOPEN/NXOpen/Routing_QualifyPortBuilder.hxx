#ifndef NXOpen_ROUTING_QUALIFYPORTBUILDER_HXX_INCLUDED
#define NXOpen_ROUTING_QUALIFYPORTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_QualifyPortBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/Routing_Port.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_routing_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Routing
    {
        class QualifyPortBuilder;
    }
    class Builder;
    class Direction;
    class Expression;
    class Point;
    class SelectFace;
    class SelectICurve;
    namespace Routing
    {
        class _QualifyPortBuilderBuilder;
        class QualifyPortBuilderImpl;
        /** Builder for creating/editing ports.  <br> To create a new instance of this class, use @link NXOpen::Routing::RouteManager::CreateQualifyPortBuilder  NXOpen::Routing::RouteManager::CreateQualifyPortBuilder @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  QualifyPortBuilder : public NXOpen::Builder
        {
            /** Determines the port type to create */
            public: enum CreatePortType
            {
                CreatePortTypeFitting/** Fitting Port. */,
                CreatePortTypeFixture/** Fixture Port. */,
                CreatePortTypeMulti/** Multi Port. */
            };

            /** Determines the positioning method used to create port */
            public: enum PositioningMethodType
            {
                PositioningMethodTypePointAndVector/** Point and Vector. */,
                PositioningMethodTypeMidpointOnFace/** Midpoint on Face. */,
                PositioningMethodTypeBetweenTwoLines/** Between Two Lines. */
            };

            private: QualifyPortBuilderImpl * m_qualifyportbuilder_impl;
            private: friend class  _QualifyPortBuilderBuilder;
            protected: QualifyPortBuilder();
            public: ~QualifyPortBuilder();
            /**Returns  the port type 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::QualifyPortBuilder::CreatePortType PortType
            (
            );
            /**Sets  the port type 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetPortType
            (
                NXOpen::Routing::QualifyPortBuilder::CreatePortType portType /** porttype */ 
            );
            /**Returns  the port name string 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXString PortNameString
            (
            );
            /**Sets  the port name string 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetPortNameString
            (
                const NXString & portNameString /** portnamestring */ 
            );
            /**Sets  the port name string 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetPortNameString
            (
                const char * portNameString /** portnamestring */ 
            );
            /**Returns  the positioning method type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::QualifyPortBuilder::PositioningMethodType PositioningMethod
            (
            );
            /**Sets  the positioning method type 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetPositioningMethod
            (
                NXOpen::Routing::QualifyPortBuilder::PositioningMethodType positioningMethod /** positioningmethod */ 
            );
            /**Returns  the face for positioning method Midpoint on Face 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::SelectFace * Face
            (
            );
            /**Returns  the reverse vector 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool ReverseVector
            (
            );
            /**Sets  the reverse vector 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetReverseVector
            (
                bool reverseVector /** reversevector */ 
            );
            /**Returns  the first line for positioning method Between Two Lines 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::SelectICurve * Line1
            (
            );
            /**Returns  the second line for positioning method Between Two Lines 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::SelectICurve * Line2
            (
            );
            /**Returns  the stock offset 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool StockOffset
            (
            );
            /**Sets  the stock offset 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetStockOffset
            (
                bool stockOffset /** stockoffset */ 
            );
            /**Returns  the origin point 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Point * OriginPoint
            (
            );
            /**Sets  the origin point 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetOriginPoint
            (
                NXOpen::Point * originPoint /** originpoint */ 
            );
            /**Returns  the offset vector 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Direction * OffsetVector
            (
            );
            /**Sets  the offset vector 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetOffsetVector
            (
                NXOpen::Direction * offsetVector /** offsetvector */ 
            );
            /**Returns  the offset expression 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXString OffsetExpression
            (
            );
            /**Sets  the offset expression 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetOffsetExpression
            (
                const NXString & offsetExpression /** offsetexpression */ 
            );
            /**Sets  the offset expression 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            void SetOffsetExpression
            (
                const char * offsetExpression /** offsetexpression */ 
            );
            /**Returns  the align vector 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Direction * AlignVector
            (
            );
            /**Sets  the align vector 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetAlignVector
            (
                NXOpen::Direction * alignVector /** alignvector */ 
            );
            /**Returns  the allow port engagement 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool AllowPortEngagement
            (
            );
            /**Sets  the allow port engagement 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetAllowPortEngagement
            (
                bool allowPortEngagement /** allowportengagement */ 
            );
            /**Returns  the port engagement 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Expression * PortEngagement
            (
            );
            /**Sets  the port engagement 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetPortEngagement
            (
                NXOpen::Expression * portEngagement /** portengagement */ 
            );
            /**Returns  the port extension 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Expression * PortExtension
            (
            );
            /**Sets  the port extension 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetPortExtension
            (
                NXOpen::Expression * portExtension /** portextension */ 
            );
            /**Returns  the spool delimiter 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool SpoolDelimiter
            (
            );
            /**Sets  the spool delimiter 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetSpoolDelimiter
            (
                bool spoolDelimiter /** spooldelimiter */ 
            );
            /**Returns  the allow multiple connections 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool AllowMultiConnections
            (
            );
            /**Sets  the allow multiple connections 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetAllowMultiConnections
            (
                bool multiConnections /** multiconnections */ 
            );
            /**Returns  the flow direction 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::Port::FlowDirectionType FlowDirection
            (
            );
            /**Sets  the flow direction 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetFlowDirection
            (
                NXOpen::Routing::Port::FlowDirectionType flowDirection /** flowdirection */ 
            );
            /**Returns  the cutback length 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Expression * CutbackLength
            (
            );
            /**Sets  the cutback length 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetCutbackLength
            (
                NXOpen::Expression * cutbackLength /** cutbacklength */ 
            );
            /**Returns  the back extension 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Expression * BackExtension
            (
            );
            /**Sets  the back extension 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetBackExtension
            (
                NXOpen::Expression * backExtension /** backextension */ 
            );
            /**Returns  the length addition 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Expression * LengthAddition
            (
            );
            /**Sets  the length addition 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetLengthAddition
            (
                NXOpen::Expression * lengthAddition /** lengthaddition */ 
            );
            /**Returns  the rotation vector 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Direction * RotationVector
            (
            );
            /**Sets  the rotation vector 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetRotationVector
            (
                NXOpen::Direction * rotationVector /** rotationvector */ 
            );
            /**Returns  the clocking angle 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Expression * ClockingAngle
            (
            );
            /**Returns  the align vector user defined 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool AlignVectorUserDefined
            (
            );
            /**Sets  the align vector user defined 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetAlignVectorUserDefined
            (
                bool alignVectorUserDefined /** alignvectoruserdefined */ 
            );
            /**Returns  the offset vector user defined 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool OffsetVectorUserDefined
            (
            );
            /**Sets  the offset vector user defined 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetOffsetVectorUserDefined
            (
                bool offsetVectorUserDefined /** offsetvectoruserdefined */ 
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
#ifndef NXOpen_ANNOTATIONS_LEADERDATA_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_LEADERDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_LeaderData.ja
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
#include <NXOpen/Annotations.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Annotations
    {
        class LeaderData;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class SelectDisplayableObject;
    class SelectDisplayableObjectList;
    namespace Annotations
    {
        class _LeaderDataBuilder;
        class LeaderDataImpl;
        /**
            Represents a @link NXOpen::Annotations::LeaderData NXOpen::Annotations::LeaderData@endlink .  This class is
            used to construct the definition for a single leader object.
             <br> To create a new instance of this class, use @link NXOpen::Annotations::AnnotationManager::CreateLeaderData  NXOpen::Annotations::AnnotationManager::CreateLeaderData @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  LeaderData : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** the set of datatypes used to define the types of leaders that can
                        be applied to an annotation */
            public: enum LeaderType
            {
                LeaderTypePlain/** Plain leader style */,
                LeaderTypeAllAround/** Plain leader style with all around symbol */,
                LeaderTypePlainWithoutStub/** Plain leader style with no stub */,
                LeaderTypeFlag/** Flag style */,
                LeaderTypeDatum/** Datum feature symbol style */,
                LeaderTypeDotTerminated/** Datum feature on stub of dot terminated style */,
                LeaderTypeExtension/** Id symbol extension style leader */,
                LeaderTypeAllOver/** all over */ 
            };

            /** the set of arrowhead types used to define a leader arrowhead */
            public: enum ArrowheadType
            {
                ArrowheadTypeClosedArrow/** Closed arrowhead type */,
                ArrowheadTypeClosedSolidArrow/** Closed solid arrowhead type */,
                ArrowheadTypeOpenArrow/** Open arrowhead type */,
                ArrowheadTypeFilledArrow/** Filled arrowhead type */,
                ArrowheadTypeClosedDoubleArrow/** Closed double arrowhead type */,
                ArrowheadTypeClosedDoubleSolidArrow/** Closed double solid arrowhead type */,
                ArrowheadTypeOpenDoubleArrow/** Open double arrowhead type */,
                ArrowheadTypeFilledDoubleArrow/** Filled double arrowhead type */,
                ArrowheadTypeNone/** No terminating symbol */,
                ArrowheadTypeOrigin/** Origin symbol */,
                ArrowheadTypeCross/** Cross symbol */,
                ArrowheadTypeIntegral/** Integral symbol */,
                ArrowheadTypeDot/** Dot symbol */,
                ArrowheadTypeFilledDot/** Filled dot symbol */,
                ArrowheadTypeSquare/** Square symbol */,
                ArrowheadTypeFilledSquare/** Filled square symbol */,
                ArrowheadTypeDatum/** Datum symbol */,
                ArrowheadTypeFilledDatum/** Filled datum symbol */,
                ArrowheadTypeTopOpenArrow/** Top open arrowhead */,
                ArrowheadTypeBottomOpenArrow/** bottom open arrowhead */,
                ArrowheadTypeTopFilledArrow/** top filled arrowhead */,
                ArrowheadTypeBottomFilledArrow/** bottom filled arrowhead */
            };

            private: LeaderDataImpl * m_leaderdata_impl;
            private: friend class  _LeaderDataBuilder;
            protected: LeaderData();
            public: ~LeaderData();
            /**Returns  the terminator type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::LeaderData::LeaderType TerminatorType
            (
            );
            /**Sets  the terminator type 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetTerminatorType
            (
                NXOpen::Annotations::LeaderData::LeaderType terminatorType /** terminatortype */ 
            );
            /**Returns  the leader 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObject * Leader
            (
            );
            /**Returns  the jogs 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * Jogs
            (
            );
            /**Returns  the arrowhead 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::LeaderData::ArrowheadType Arrowhead
            (
            );
            /**Sets  the arrowhead 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetArrowhead
            (
                NXOpen::Annotations::LeaderData::ArrowheadType arrowhead /** arrowhead */ 
            );
            /**Returns  the stub side 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::LeaderSide StubSide
            (
            );
            /**Sets  the stub side 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetStubSide
            (
                NXOpen::Annotations::LeaderSide stubSide /** stub side */ 
            );
            /**Returns  the stub size 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double StubSize
            (
            );
            /**Sets  the stub size 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetStubSize
            (
                double stubSize /** stubsize */ 
            );
            /**Returns  the perpendicular relationship between the first segment and stub 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: bool Perpendicular
            (
            );
            /**Sets  the perpendicular relationship between the first segment and stub 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetPerpendicular
            (
                bool isPerpendicular /** isperpendicular */ 
            );
            /**Returns  the datum arrowhead type for the datum portion of a datum on dot terminated leader 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::LeaderData::ArrowheadType DatumOnDotTerminatedArrowhead
            (
            );
            /**Sets  the datum arrowhead type for the datum portion of a datum on dot terminated leader 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetDatumOnDotTerminatedArrowhead
            (
                NXOpen::Annotations::LeaderData::ArrowheadType arrowhead /** arrowhead */ 
            );
            /**Returns  the datum start point for the leader segment of the datum portion of a datum on dot terminated leader 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point3d DatumOnDotTerminatedStartPoint
            (
            );
            /**Sets  the datum start point for the leader segment of the datum portion of a datum on dot terminated leader 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetDatumOnDotTerminatedStartPoint
            (
                const NXOpen::Point3d & startpoint /** startpoint */ 
            );
            /**Returns  the datum end point for the leader segment of the datum portion of a datum on dot terminated leadet 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point3d DatumOnDotTerminatedEndPoint
            (
            );
            /**Sets  the datum end point for the leader segment of the datum portion of a datum on dot terminated leadet 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetDatumOnDotTerminatedEndPoint
            (
                const NXOpen::Point3d & endpoint /** endpoint */ 
            );
            /**Returns  the vertical attachment 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::LeaderVerticalAttachment VerticalAttachment
            (
            );
            /**Sets  the vertical attachment 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetVerticalAttachment
            (
                NXOpen::Annotations::LeaderVerticalAttachment verticalAttachment /** vertical attachment */ 
            );
            /**Returns  the perpendicular relationship between the first segment and attachement object 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool LeaderPerpendicular
            (
            );
            /**Sets  the perpendicular relationship between the first segment and attachement object 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLeaderPerpendicular
            (
                bool isLeaderPerpendicular /** isleaderperpendicular */ 
            );
            /** Returns the stub status of the defined leader.  @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: bool HasStub
            (
            );
            /** Returns the start point of the leader.  @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point3d GetStubStartPoint
            (
            );
            /** Returns the end point of the leader.  @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point3d GetStubEndPoint
            (
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful 
             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: virtual bool Validate
            (
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

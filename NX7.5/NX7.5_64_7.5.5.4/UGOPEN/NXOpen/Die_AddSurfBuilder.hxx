#ifndef NXOpen_DIE_ADDSURFBUILDER_HXX_INCLUDED
#define NXOpen_DIE_ADDSURFBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_AddSurfBuilder.ja
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
#include <NXOpen/Die_AddSurfBuilder.hxx>
#include <NXOpen/Die_DieLimitsBuilder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Die
    {
        class AddSurfBuilder;
    }
    namespace Die
    {
        class DieLimitsBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class Point;
    class ScCollector;
    class SelectNXObjectList;
    namespace Die
    {
        class _AddSurfBuilderBuilder;
        class AddSurfBuilderImpl;
        /**
            Represents a @link Die::AddSurfBuilder Die::AddSurfBuilder@endlink  builder
             <br> To create a new instance of this class, use @link Die::DieCollection::CreateAddSurfBuilder Die::DieCollection::CreateAddSurfBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  AddSurfBuilder : public Features::FeatureBuilder
        {
            /** Settings for the type of addendum surface being created. */
            public: enum Methods
            {
                MethodsSectional/** Sweep section around tangency curve. */,
                MethodsCurveMesh/** Modeling curve mesh. */,
                MethodsChannelTunnelCap/** To close an end cap. */,
                MethodsMultiFaceBlend/** Face blend between sets of walls. */,
                MethodsWallsOnly/** Produces just the walls, no blend. */,
                MethodsDiskFaceBlend/** Disk type face blend. */,
                MethodsSphereFaceBlend/** Spherical type face blend. */
            };

            private: AddSurfBuilderImpl * m_addsurfbuilder_impl;
            private: friend class  _AddSurfBuilderBuilder;
            protected: AddSurfBuilder();
            public: ~AddSurfBuilder();
            /**Returns  the addendum section feature to define the shape of the addendum surface.  <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * SelectSection
            (
            );
            /**Returns  the trimming boundary for the addendum surface.  <br> License requirements : None */
            public: NXOpen::ScCollector * TrimBound
            (
            );
            /**Returns  the keep point for trimming.  <br> License requirements : None */
            public: NXOpen::Point * RefPoint
            (
            );
            /**Sets  the keep point for trimming.  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetRefPoint
            (
                NXOpen::Point * point0 /** point0 */ 
            );
            /**Returns  the first end point to limit the extent of the surface along the tangency curve. 
                        <br> This method has been deprecated. Use @link Die::AddSurfBuilder::Limits Die::AddSurfBuilder::Limits@endlink   
                        to access limit points.
                        <br> 
                    
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") NXOpen::Point * LimitPoint1
            (
            );
            /**Sets  the first end point to limit the extent of the surface along the tangency curve. 
                        <br> This method has been deprecated. Use @link Die::AddSurfBuilder::Limits Die::AddSurfBuilder::Limits@endlink   
                        to access limit points.
                        <br> 
                    
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") void SetLimitPoint1
            (
                NXOpen::Point * point /** point */ 
            );
            /**Returns  the second end point to limit the extent of the surface along the tangency curve. 
                        <br> This method has been deprecated. Use @link Die::AddSurfBuilder::Limits Die::AddSurfBuilder::Limits@endlink   
                        to access limit points.
                        <br> 
                    
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") NXOpen::Point * LimitPoint2
            (
            );
            /**Sets  the second end point to limit the extent of the surface along the tangency curve. 
                        <br> This method has been deprecated. Use @link Die::AddSurfBuilder::Limits Die::AddSurfBuilder::Limits@endlink   
                        to access limit points.
                        <br> 
                    
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") void SetLimitPoint2
            (
                NXOpen::Point * point /** point */ 
            );
            /**Returns  the flag that indicates during creation if a feature is to be created or just the sheet body,
                        true indicates a feature will be created.  <br> License requirements : None */
            public: bool Associative
            (
            );
            /**Sets  the flag that indicates during creation if a feature is to be created or just the sheet body,
                        true indicates a feature will be created.  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetAssociative
            (
                bool associative /** associative */ 
            );
            /**Returns  the flag that indicates whether the faces of the addendum sheet body will be sewn into one sheet body
                        or individual sheet bodies for each face will be output.  True indicates one sewn sheet body will be output.  <br> License requirements : None */
            public: bool Sewn
            (
            );
            /**Sets  the flag that indicates whether the faces of the addendum sheet body will be sewn into one sheet body
                        or individual sheet bodies for each face will be output.  True indicates one sewn sheet body will be output.  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetSewn
            (
                bool sewn /** sewn */ 
            );
            /**Returns  the addendum surface output method.  <br> License requirements : None */
            public: NXOpen::Die::AddSurfBuilder::Methods Method
            (
            );
            /**Sets  the addendum surface output method.  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetMethod
            (
                NXOpen::Die::AddSurfBuilder::Methods type /** type */ 
            );
            /**Returns  the distance tolerance.  <br> License requirements : None */
            public: double DistanceTolerance
            (
            );
            /**Sets  the distance tolerance.  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetDistanceTolerance
            (
                double distanceTolerance /** distancetolerance */ 
            );
            /**Returns  the concave corner radius value  <br> License requirements : None */
            public: NXOpen::Expression * ConcaveCornerRadius
            (
            );
            /**Returns  the spine string, which determines the orientation of the sample planes  <br> License requirements : None */
            public: NXOpen::ScCollector * Spine
            (
            );
            /** Creates a smoothed spine curve from the forming boundary using the spine radius value  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void CreateDefaultSpine
            (
            );
            /**Returns  the spine radius, used by JA_ADD_SURF_BUILDER_CreateDefaultSpine  <br> License requirements : None */
            public: double SpineRadius
            (
            );
            /**Sets  the spine radius, used by JA_ADD_SURF_BUILDER_CreateDefaultSpine  <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetSpineRadius
            (
                double spineRadius /** spineradius */ 
            );
            /**Returns  the limits to control the span of the addendum  <br> License requirements : None */
            public: NXOpen::Die::DieLimitsBuilder * Limits
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
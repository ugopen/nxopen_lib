#ifndef NXOpen_ROUTING_SPLINEDATA_HXX_INCLUDED
#define NXOpen_ROUTING_SPLINEDATA_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_SplineData.ja
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
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/Routing_DefiningPoint.hxx>
#include <NXOpen/ugmath.hxx>
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
        class SplineData;
    }
    namespace Routing
    {
        class DefiningPoint;
    }
    namespace Routing
    {
        class ISegment;
    }
    namespace Routing
    {
        class SplineDataImpl;
        /**  @brief  Represents a transient @link NXOpen::Routing::SplineData NXOpen::Routing::SplineData@endlink  object.  

         
                 <br>  This class provides the ability to create or edit Routing Spline Segments.  <br> 
                 <br>  To create an instance of this class, call @link NXOpen::Routing::SegmentManager::CreateSplineData NXOpen::Routing::SegmentManager::CreateSplineData@endlink 
                       or @link NXOpen::Routing::SplineSegment::SplineData NXOpen::Routing::SplineSegment::SplineData@endlink .  <br> 
                 <br>  For example, to change an existing spline, first get the spline's data by calling
                       @link NXOpen::Routing::SegmentManager::CreateSplineData NXOpen::Routing::SegmentManager::CreateSplineData@endlink  with the spline
                       you want to update. Then call @link NXOpen::Routing::SplineData::GetDefiningPoints NXOpen::Routing::SplineData::GetDefiningPoints@endlink 
                       to get the defining points. You can change the point's position, extension direction,
                       or extension values using the @link NXOpen::Routing::DefiningPoint NXOpen::Routing::DefiningPoint@endlink  methods.  <br> 
                 <br>  To create a new spline, create a new @link NXOpen::Routing::SplineData NXOpen::Routing::SplineData@endlink 
                       object by calling @link NXOpen::Routing::SplineSegment::SplineData NXOpen::Routing::SplineSegment::SplineData@endlink . Then
                       add points and extensions using the @link NXOpen::Routing::DefiningPoint NXOpen::Routing::DefiningPoint@endlink  methods.  <br>  
         <br>  Created in NX1953.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  SplineData : public NXOpen::TransientObject
        {
            private: SplineDataImpl * m_splinedata_impl;
            /// \cond NX_NO_DOC 
            public: explicit SplineData(void *ptr);
            /// \endcond 
            /**Returns  the number of @link NXOpen::Routing::DefiningPoint NXOpen::Routing::DefiningPoint@endlink  objects. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: int NumDefiningPoints
            (
            );
            /** Get the @link NXOpen::Routing::DefiningPoint NXOpen::Routing::DefiningPoint@endlink  objects.  @return   
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: std::vector<NXOpen::Routing::DefiningPoint *> GetDefiningPoints
            (
            );
            /** Set the @link NXOpen::Routing::DefiningPoint NXOpen::Routing::DefiningPoint@endlink  objects. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetDefiningPoints
            (
                const std::vector<NXOpen::Routing::DefiningPoint *> & definingPoints /** definingpoints */ 
            );
            /** Get the @link NXOpen::Routing::DefiningPoint NXOpen::Routing::DefiningPoint@endlink  object at the index.
                        The index should be a positive integer less than the number of defining points returned
                        by @link NXOpen::Routing::SplineData::NumDefiningPoints NXOpen::Routing::SplineData::NumDefiningPoints@endlink .  @return   
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::DefiningPoint * GetDefiningPoint
            (
                int index /** Index of the defining point. */
            );
            /** Set the @link NXOpen::Routing::DefiningPoint NXOpen::Routing::DefiningPoint@endlink  object at the index.
                        The index should be a positive integer less than the number of defining points returned
                        by @link NXOpen::Routing::SplineData::NumDefiningPoints NXOpen::Routing::SplineData::NumDefiningPoints@endlink . 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetDefiningPoint
            (
                int index /** Index of the defining point. */,
                NXOpen::Routing::DefiningPoint * definingPoint /** definingpoint */ 
            );
            /** Get the position of the @link NXOpen::Routing::DefiningPoint NXOpen::Routing::DefiningPoint@endlink  object at the index.
                        The index should be a positive integer less than the number of defining points returned
                        by @link NXOpen::Routing::SplineData::NumDefiningPoints NXOpen::Routing::SplineData::NumDefiningPoints@endlink .  @return  The position at the index. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Point3d GetPosition
            (
                int index /** Index of the defining point. */
            );
            /** Set the position of the @link NXOpen::Routing::DefiningPoint NXOpen::Routing::DefiningPoint@endlink  object at the index.
                        The index should be a positive integer less than the number of defining points returned
                        by @link NXOpen::Routing::SplineData::NumDefiningPoints NXOpen::Routing::SplineData::NumDefiningPoints@endlink . 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetPosition
            (
                int index /** Index of the defining point. */,
                const NXOpen::Point3d & position /** The position at the index. */
            );
            /** Remove a position of the @link NXOpen::Routing::DefiningPoint NXOpen::Routing::DefiningPoint@endlink  object at the index.
                         <br>  The index should be a positive integer less than the number of defining points returned
                               by @link NXOpen::Routing::SplineData::NumDefiningPoints NXOpen::Routing::SplineData::NumDefiningPoints@endlink .  <br> 
                         <br>  If the removal of the position is successful, the number of defining points will
                               be decremented and decrements the index of all the positions greater than the
                               index of the point removed.  <br>   @return  The resultant number of defining points. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: int RemovePosition
            (
                int index /** Index of the defining point. */
            );
            /** Insert a position before the @link NXOpen::Routing::DefiningPoint NXOpen::Routing::DefiningPoint@endlink  object at the index.
                         <br>  The index should be a positive integer less than the number of defining points returned
                               by @link NXOpen::Routing::SplineData::NumDefiningPoints NXOpen::Routing::SplineData::NumDefiningPoints@endlink .  <br> 
                         <br>  If the insertion of the position is successful, the number of defining points will
                               be incremented and increments the index of all of the positions greater than the
                               index of the inserted position.  <br>   @return  The resultant number of defining points. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: int InsertPositionBefore
            (
                int index /** Index of the defining point. */,
                const NXOpen::Point3d & position /** The position at the index. */
            );
            /** Insert a position after the @link NXOpen::Routing::DefiningPoint NXOpen::Routing::DefiningPoint@endlink  object at the index.
                         <br>  The index should be a positive integer less than the number of defining points returned
                               by @link NXOpen::Routing::SplineData::NumDefiningPoints NXOpen::Routing::SplineData::NumDefiningPoints@endlink .  <br> 
                         <br>  If the insertion of the position is successful, the number of defining points will
                               be incremented and increments the index of all of the positions greater than the
                               index of the inserted position.  <br>   @return  The resultant number of defining points. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: int InsertPositionAfter
            (
                int index /** Index of the defining point. */,
                const NXOpen::Point3d & position /** The position at the index. */
            );
            /** Get the extension direction of the @link NXOpen::Routing::DefiningPoint NXOpen::Routing::DefiningPoint@endlink  object at the index.
                        The index should be a positive integer less than the number of defining points returned
                        by @link NXOpen::Routing::SplineData::NumDefiningPoints NXOpen::Routing::SplineData::NumDefiningPoints@endlink .  @return  The direction at the index. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Vector3d GetDirection
            (
                int index /** Index of the defining point. */
            );
            /** Set the extension direction of the @link NXOpen::Routing::DefiningPoint NXOpen::Routing::DefiningPoint@endlink  object at the index.
                        The index should be a positive integer less than the number of defining points returned
                        by @link NXOpen::Routing::SplineData::NumDefiningPoints NXOpen::Routing::SplineData::NumDefiningPoints@endlink . 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetDirection
            (
                int index /** Index of the defining point. */,
                const NXOpen::Vector3d & direction /** The direction at the index. */
            );
            /** Get the backward extension of the @link NXOpen::Routing::DefiningPoint NXOpen::Routing::DefiningPoint@endlink  at the index.
                        The index should be a positive integer less than the number of defining points returned
                        by @link NXOpen::Routing::SplineData::NumDefiningPoints NXOpen::Routing::SplineData::NumDefiningPoints@endlink .  @return  The backward extension at the index. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: double GetBackwardExtension
            (
                int index /** Index of the defining point. */
            );
            /** Set the backward extension of the @link NXOpen::Routing::DefiningPoint NXOpen::Routing::DefiningPoint@endlink  at the index.
                        The index should be a positive integer less than the number of defining points returned
                        by @link NXOpen::Routing::SplineData::NumDefiningPoints NXOpen::Routing::SplineData::NumDefiningPoints@endlink . 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetBackwardExtension
            (
                int index /** Index of the defining point. */,
                double backwardExtension /** the backward extension at the index. */
            );
            /** Get the forward extension of the @link NXOpen::Routing::DefiningPoint NXOpen::Routing::DefiningPoint@endlink  at the index.
                        The index should be a positive integer less than the number of defining points returned
                        by @link NXOpen::Routing::SplineData::NumDefiningPoints NXOpen::Routing::SplineData::NumDefiningPoints@endlink .  @return  the forward extension at the index. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: double GetForwardExtension
            (
                int index /** Index of the defining point. */
            );
            /** Set the forward extension of the @link NXOpen::Routing::DefiningPoint NXOpen::Routing::DefiningPoint@endlink  at the index.
                        The index should be a positive integer less than the number of defining points returned
                        by @link NXOpen::Routing::SplineData::NumDefiningPoints NXOpen::Routing::SplineData::NumDefiningPoints@endlink . 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void SetForwardExtension
            (
                int index /** Index of the defining point. */,
                double forwardExtension /** the forward extension at the index. */
            );
            /** Remove an extension on the @link NXOpen::Routing::DefiningPoint NXOpen::Routing::DefiningPoint@endlink  at the index.
                        The index should be a positive integer less than the number of defining points returned
                        by @link NXOpen::Routing::SplineData::NumDefiningPoints NXOpen::Routing::SplineData::NumDefiningPoints@endlink . 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: void RemoveExtension
            (
                int index /** Index of the @link NXOpen::Routing::DefiningPoint NXOpen::Routing::DefiningPoint@endlink . */
            );
            /** Does the @link NXOpen::Routing::DefiningPoint NXOpen::Routing::DefiningPoint@endlink  have any
                        @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  that determines its location?
                        If so, you cannot change the position of this point. 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: bool IsConstrained
            (
                int index /** Index of the @link NXOpen::Routing::DefiningPoint NXOpen::Routing::DefiningPoint@endlink . */
            );
            /** Commit the @link NXOpen::Routing::SplineData NXOpen::Routing::SplineData@endlink  changes.  @return  the resultant spline segment. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : routing_base ("Routing Basic") */
            public: NXOpen::Routing::ISegment * CommitChanges
            (
            );
            /** Destroys the @link NXOpen::Routing::SplineData NXOpen::Routing::SplineData@endlink  object. 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~SplineData();
        }; //lint !e1712 default constructor not defined for class  

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

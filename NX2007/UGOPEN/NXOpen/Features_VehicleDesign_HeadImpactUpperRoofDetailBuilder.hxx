#ifndef NXOpen_FEATURES_VEHICLEDESIGN_HEADIMPACTUPPERROOFDETAILBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_VEHICLEDESIGN_HEADIMPACTUPPERROOFDETAILBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_VehicleDesign_HeadImpactUpperRoofDetailBuilder.ja
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
#include <NXOpen/TaggedObject.hxx>
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
        namespace VehicleDesign
        {
            class HeadImpactUpperRoofDetailBuilder;
        }
    }
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class Point;
    namespace Features
    {
        namespace VehicleDesign
        {
            class _HeadImpactUpperRoofDetailBuilderBuilder;
            class HeadImpactUpperRoofDetailBuilderImpl;
            /** Represents a @link NXOpen::Features::VehicleDesign::HeadImpactUpperRoofDetailBuilder NXOpen::Features::VehicleDesign::HeadImpactUpperRoofDetailBuilder@endlink .  <br> This is an abstract class and cannot be instantiated.  <br> 
             <br>  Created in NX9.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  HeadImpactUpperRoofDetailBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
            {
                private: HeadImpactUpperRoofDetailBuilderImpl * m_headimpactupperroofdetailbuilder_impl;
                private: friend class  _HeadImpactUpperRoofDetailBuilderBuilder;
                protected: HeadImpactUpperRoofDetailBuilder();
                public: ~HeadImpactUpperRoofDetailBuilder();
                /**Returns  the offset used to position point C and point D. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * RoofOffset
                (
                );
                /**Returns  the calculated horizontal distance between plane A and plane B. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * D1
                (
                );
                /**Returns  the calculated horizontal distance between plane C and plane D. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * D2
                (
                );
                /**Returns  the ratio used to locate planes E, F, G, and H. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * RoofRatio
                (
                );
                /**Returns  the vertical minimum required approach angle. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * ReqVerticalMin
                (
                );
                /**Returns  the vertical maximum required approach angle. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * ReqVerticalMax
                (
                );
                /**Returns  the point M alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool PointMFlag
                (
                );
                /**Sets  the point M alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPointMFlag
                (
                    bool pointMFlag /** pointmflag */ 
                );
                /**Returns  the point M alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * PointM
                (
                );
                /**Sets  the point M alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPointM
                (
                    NXOpen::Point * pointM /** pointm */ 
                );
                /**Returns  the point A additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool PointAFlag
                (
                );
                /**Sets  the point A additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPointAFlag
                (
                    bool pointAFlag /** pointaflag */ 
                );
                /**Returns  the point A additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * PointA
                (
                );
                /**Sets  the point A additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPointA
                (
                    NXOpen::Point * pointA /** pointa */ 
                );
                /**Returns  the point B additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool PointBFlag
                (
                );
                /**Sets  the point B additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPointBFlag
                (
                    bool pointBFlag /** pointbflag */ 
                );
                /**Returns  the point B additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * PointB
                (
                );
                /**Sets  the point B additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPointB
                (
                    NXOpen::Point * pointB /** pointb */ 
                );
                /**Returns  the point C additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool PointCFlag
                (
                );
                /**Sets  the point C additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPointCFlag
                (
                    bool pointCFlag /** pointcflag */ 
                );
                /**Returns  the point C additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * PointC
                (
                );
                /**Sets  the point C additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPointC
                (
                    NXOpen::Point * pointC /** pointc */ 
                );
                /**Returns  the point D additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool PointDFlag
                (
                );
                /**Sets  the point D additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPointDFlag
                (
                    bool pointDFlag /** pointdflag */ 
                );
                /**Returns  the point D additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * PointD
                (
                );
                /**Sets  the point D additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPointD
                (
                    NXOpen::Point * pointD /** pointd */ 
                );
                /**Returns  the create construction geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool CreateGeometry
                (
                );
                /**Sets  the create construction geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetCreateGeometry
                (
                    bool createGeometry /** creategeometry */ 
                );
                /** Validate whether the inputs to the component are sufficient for 
                            commit to be called.  If the component is not in a state to commit
                            then an exception is thrown.  For example, if the component requires
                            you to set some property, this method will throw an exception if
                            you haven't set it.  This method throws a not yet implemented
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
#ifndef NXOpen_FEATURES_VEHICLEDESIGN_HEADIMPACTAPILLARDETAILBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_VEHICLEDESIGN_HEADIMPACTAPILLARDETAILBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_VehicleDesign_HeadImpactAPillarDetailBuilder.ja
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
            class HeadImpactAPillarDetailBuilder;
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
            class _HeadImpactAPillarDetailBuilderBuilder;
            class HeadImpactAPillarDetailBuilderImpl;
            /** Represents a @link NXOpen::Features::VehicleDesign::HeadImpactAPillarDetailBuilder NXOpen::Features::VehicleDesign::HeadImpactAPillarDetailBuilder@endlink .  <br> This is an abstract class and cannot be instantiated.  <br> 
             <br>  Created in NX9.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  HeadImpactAPillarDetailBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
            {
                /** Represents the measurement methods used to position point 1. */
                public: enum MeasurementMethodType
                {
                    MeasurementMethodTypeWrapAround/** wrap around */ ,
                    MeasurementMethodTypeOnSurface/** on surface */ ,
                    MeasurementMethodTypeNotSpecified/** not specified */ 
                };

                private: HeadImpactAPillarDetailBuilderImpl * m_headimpactapillardetailbuilder_impl;
                private: friend class  _HeadImpactAPillarDetailBuilderBuilder;
                protected: HeadImpactAPillarDetailBuilder();
                public: ~HeadImpactAPillarDetailBuilder();
                /**Returns  the measurement method used to position point 1. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::VehicleDesign::HeadImpactAPillarDetailBuilder::MeasurementMethodType MeasurementMethod
                (
                );
                /**Sets  the measurement method used to position point 1. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetMeasurementMethod
                (
                    NXOpen::Features::VehicleDesign::HeadImpactAPillarDetailBuilder::MeasurementMethodType measurementMethod /** measurementmethod */ 
                );
                /**Returns  the offset used to position point 1. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Point1Offset
                (
                );
                /**Returns  the offset used to position point 2. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Point2Offset
                (
                );
                /**Returns  the offset used to position AP2. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * AP2Offset
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
                /**Returns  the left horizontal minimum required approach angle. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * ReqHorizontalLeftMin
                (
                );
                /**Returns  the left horizontal minimum required approach angle calculated value. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * HorizontalLeftMin
                (
                );
                /**Returns  the left horizontal maximum required approach angle. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * ReqHorizontalLeftMax
                (
                );
                /**Returns  the left horizontal maximum required approach angle calculated value. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * HorizontalLeftMax
                (
                );
                /**Returns  the right horizontal minimum required approach angle. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * ReqHorizontalRightMin
                (
                );
                /**Returns  the right horizontal minimum required approach angle calculated value. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * HorizontalRightMin
                (
                );
                /**Returns  the right horizontal maximum required approach angle. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * ReqHorizontalRightMax
                (
                );
                /**Returns  the right horizontal maximum required approach angle calculated value. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * HorizontalRightMax
                (
                );
                /**Returns  the left AP1 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool AP1LeftFlag
                (
                );
                /**Sets  the left AP1 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetAP1LeftFlag
                (
                    bool ap1LeftFlag /** ap1leftflag */ 
                );
                /**Returns  the left AP1 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * AP1Left
                (
                );
                /**Sets  the left AP1 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetAP1Left
                (
                    NXOpen::Point * ap1Left /** ap1left */ 
                );
                /**Returns  the right AP1 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool AP1RightFlag
                (
                );
                /**Sets  the right AP1 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetAP1RightFlag
                (
                    bool ap1RightFlag /** ap1rightflag */ 
                );
                /**Returns  the right AP1 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * AP1Right
                (
                );
                /**Sets  the right AP1 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetAP1Right
                (
                    NXOpen::Point * ap1Right /** ap1right */ 
                );
                /**Returns  the left AP2 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool AP2LeftFlag
                (
                );
                /**Sets  the left AP2 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetAP2LeftFlag
                (
                    bool ap2LeftFlag /** ap2leftflag */ 
                );
                /**Returns  the left AP2 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * AP2Left
                (
                );
                /**Sets  the left AP2 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetAP2Left
                (
                    NXOpen::Point * ap2Left /** ap2left */ 
                );
                /**Returns  the right AP2 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool AP2RightFlag
                (
                );
                /**Sets  the right AP2 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetAP2RightFlag
                (
                    bool ap2RightFlag /** ap2rightflag */ 
                );
                /**Returns  the right AP2 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * AP2Right
                (
                );
                /**Sets  the right AP2 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetAP2Right
                (
                    NXOpen::Point * ap2Right /** ap2right */ 
                );
                /**Returns  the left AP3 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool AP3LeftFlag
                (
                );
                /**Sets  the left AP3 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetAP3LeftFlag
                (
                    bool ap3LeftFlag /** ap3leftflag */ 
                );
                /**Returns  the left AP3 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * AP3Left
                (
                );
                /**Sets  the left AP3 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetAP3Left
                (
                    NXOpen::Point * ap3Left /** ap3left */ 
                );
                /**Returns  the right AP3 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool AP3RightFlag
                (
                );
                /**Sets  the right AP3 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetAP3RightFlag
                (
                    bool ap3RightFlag /** ap3rightflag */ 
                );
                /**Returns  the right AP3 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * AP3Right
                (
                );
                /**Sets  the right AP3 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetAP3Right
                (
                    NXOpen::Point * ap3Right /** ap3right */ 
                );
                /**Returns  the left Line 1 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool Line1LeftFlag
                (
                );
                /**Sets  the left Line 1 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetLine1LeftFlag
                (
                    bool line1LeftFlag /** line1leftflag */ 
                );
                /**Returns  the left Line 1 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * Line1Left
                (
                );
                /**Sets  the left Line 1 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetLine1Left
                (
                    NXOpen::Point * line1Left /** line1left */ 
                );
                /**Returns  the right Line 1 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool Line1RightFlag
                (
                );
                /**Sets  the right Line 1 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetLine1RightFlag
                (
                    bool line1RightFlag /** line1rightflag */ 
                );
                /**Returns  the right Line 1 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * Line1Right
                (
                );
                /**Sets  the right Line 1 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetLine1Right
                (
                    NXOpen::Point * line1Right /** line1right */ 
                );
                /**Returns  the left Plane 5 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool Plane5LeftFlag
                (
                );
                /**Sets  the left Plane 5 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPlane5LeftFlag
                (
                    bool plane5LeftFlag /** plane5leftflag */ 
                );
                /**Returns  the left Plane 5 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * Plane5Left
                (
                );
                /**Sets  the left Plane 5 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPlane5Left
                (
                    NXOpen::Point * plane5Left /** plane5left */ 
                );
                /**Returns  the right Plane 5 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool Plane5RightFlag
                (
                );
                /**Sets  the right Plane 5 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPlane5RightFlag
                (
                    bool plane5RightFlag /** plane5rightflag */ 
                );
                /**Returns  the right Plane 5 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * Plane5Right
                (
                );
                /**Sets  the right Plane 5 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPlane5Right
                (
                    NXOpen::Point * plane5Right /** plane5right */ 
                );
                /**Returns  the left Plane 1 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool Plane1LeftFlag
                (
                );
                /**Sets  the left Plane 1 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPlane1LeftFlag
                (
                    bool plane1LeftFlag /** plane1leftflag */ 
                );
                /**Returns  the left Plane 1 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * Plane1Left
                (
                );
                /**Sets  the left Plane 1 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPlane1Left
                (
                    NXOpen::Point * plane1Left /** plane1left */ 
                );
                /**Returns  the right Plane 1 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool Plane1RightFlag
                (
                );
                /**Sets  the right Plane 1 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPlane1RightFlag
                (
                    bool plane1RightFlag /** plane1rightflag */ 
                );
                /**Returns  the right Plane 1 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * Plane1Right
                (
                );
                /**Sets  the right Plane 1 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPlane1Right
                (
                    NXOpen::Point * plane1Right /** plane1right */ 
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
#ifndef NXOpen_FEATURES_VEHICLEDESIGN_HEADIMPACTOPILLARDETAILBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_VEHICLEDESIGN_HEADIMPACTOPILLARDETAILBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_VehicleDesign_HeadImpactOPillarDetailBuilder.ja
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
#include <NXOpen/Features_VehicleDesign_HeadImpactOPillarDetailBuilder.hxx>
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
            class HeadImpactOPillarDetailBuilder;
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
            class _HeadImpactOPillarDetailBuilderBuilder;
            class HeadImpactOPillarDetailBuilderImpl;
            /** Represents a @link Features::VehicleDesign::HeadImpactOPillarDetailBuilder Features::VehicleDesign::HeadImpactOPillarDetailBuilder@endlink .  <br> This is an abstract class and cannot be instantiated.  <br> 
             <br>  Created in NX9.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  HeadImpactOPillarDetailBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
            {
                private: HeadImpactOPillarDetailBuilderImpl * m_headimpactopillardetailbuilder_impl;
                private: friend class  _HeadImpactOPillarDetailBuilderBuilder;
                protected: HeadImpactOPillarDetailBuilder();
                public: ~HeadImpactOPillarDetailBuilder();
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
                /**Returns  the left horizontal required approach angle. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * ReqHorizontalLeftExact
                (
                );
                /**Returns  the right horizontal required approach angle. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * ReqHorizontalRightExact
                (
                );
                /**Returns  the left OP1 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool OP1LeftFlag
                (
                );
                /**Sets  the left OP1 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetOP1LeftFlag
                (
                    bool op1LeftFlag /** op1leftflag */ 
                );
                /**Returns  the left OP1 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * OP1Left
                (
                );
                /**Sets  the left OP1 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetOP1Left
                (
                    NXOpen::Point * op1Left /** op1left */ 
                );
                /**Returns  the right OP1 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool OP1RightFlag
                (
                );
                /**Sets  the right OP1 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetOP1RightFlag
                (
                    bool op1RightFlag /** op1rightflag */ 
                );
                /**Returns  the right OP1 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * OP1Right
                (
                );
                /**Sets  the right OP1 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetOP1Right
                (
                    NXOpen::Point * op1Right /** op1right */ 
                );
                /**Returns  the left OP2 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool OP2LeftFlag
                (
                );
                /**Sets  the left OP2 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetOP2LeftFlag
                (
                    bool op2LeftFlag /** op2leftflag */ 
                );
                /**Returns  the left OP2 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * OP2Left
                (
                );
                /**Sets  the left OP2 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetOP2Left
                (
                    NXOpen::Point * op2Left /** op2left */ 
                );
                /**Returns  the right OP2 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool OP2RightFlag
                (
                );
                /**Sets  the right OP2 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetOP2RightFlag
                (
                    bool op2RightFlag /** op2rightflag */ 
                );
                /**Returns  the right OP2 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * OP2Right
                (
                );
                /**Sets  the right OP2 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetOP2Right
                (
                    NXOpen::Point * op2Right /** op2right */ 
                );
                /**Returns  the left Door Top additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool DoorTopLeftFlag
                (
                );
                /**Sets  the left Door Top additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetDoorTopLeftFlag
                (
                    bool doorTopLeftFlag /** doortopleftflag */ 
                );
                /**Returns  the left Door Top additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * DoorTopLeft
                (
                );
                /**Sets  the left Door Top additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetDoorTopLeft
                (
                    NXOpen::Point * doorTopLeft /** doortopleft */ 
                );
                /**Returns  the right Door Top additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool DoorTopRightFlag
                (
                );
                /**Sets  the right Door Top additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetDoorTopRightFlag
                (
                    bool doorTopRightFlag /** doortoprightflag */ 
                );
                /**Returns  the right Door Top additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * DoorTopRight
                (
                );
                /**Sets  the right Door Top additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetDoorTopRight
                (
                    NXOpen::Point * doorTopRight /** doortopright */ 
                );
                /**Returns  the left Daylight Bottom additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool DaylightBottomLeftFlag
                (
                );
                /**Sets  the left Daylight Bottom additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetDaylightBottomLeftFlag
                (
                    bool daylightBottomLeftFlag /** daylightbottomleftflag */ 
                );
                /**Returns  the left Daylight Bottom additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * DaylightBottomLeft
                (
                );
                /**Sets  the left Daylight Bottom additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetDaylightBottomLeft
                (
                    NXOpen::Point * daylightBottomLeft /** daylightbottomleft */ 
                );
                /**Returns  the right Daylight Bottom additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool DaylightBottomRightFlag
                (
                );
                /**Sets  the right Daylight Bottom additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetDaylightBottomRightFlag
                (
                    bool daylightBottomRightFlag /** daylightbottomrightflag */ 
                );
                /**Returns  the right Daylight Bottom additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * DaylightBottomRight
                (
                );
                /**Sets  the right Daylight Bottom additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetDaylightBottomRight
                (
                    NXOpen::Point * daylightBottomRight /** daylightbottomright */ 
                );
                /**Returns  the left PT6 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool PT6LeftFlag
                (
                );
                /**Sets  the left PT6 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPT6LeftFlag
                (
                    bool pt6LeftFlag /** pt6leftflag */ 
                );
                /**Returns  the left PT6 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * PT6Left
                (
                );
                /**Sets  the left PT6 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPT6Left
                (
                    NXOpen::Point * pt6Left /** pt6left */ 
                );
                /**Returns  the right PT6 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool PT6RightFlag
                (
                );
                /**Sets  the right PT6 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPT6RightFlag
                (
                    bool pt6RightFlag /** pt6rightflag */ 
                );
                /**Returns  the right PT6 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * PT6Right
                (
                );
                /**Sets  the right PT6 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPT6Right
                (
                    NXOpen::Point * pt6Right /** pt6right */ 
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
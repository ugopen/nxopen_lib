#ifndef NXOpen_FEATURES_VEHICLEDESIGN_CLOSERANGECAMERALISTITEMBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_VEHICLEDESIGN_CLOSERANGECAMERALISTITEMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_VehicleDesign_CloseRangeCameraListItemBuilder.ja
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
#include <NXOpen/Features_VehicleDesign_CloseRangeCameraListItemBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/ScCollector.hxx>
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
            class CloseRangeCameraListItemBuilder;
        }
    }
    class Axis;
    class CoordinateSystem;
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class ScCollector;
    namespace Features
    {
        namespace VehicleDesign
        {
            class _CloseRangeCameraListItemBuilderBuilder;
            class CloseRangeCameraListItemBuilderImpl;
            /**
                Represents the builder to create camera list item used for close range visibility.
                 <br> To create a new instance of this class, use @link NXOpen::Features::VehicleDesign::CloseRangeVisibilityBuilder::CreateCameraListItemBuilder  NXOpen::Features::VehicleDesign::CloseRangeVisibilityBuilder::CreateCameraListItemBuilder @endlink  <br> 
             <br>  Created in NX8.5.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  CloseRangeCameraListItemBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
            {
                /** This enum represents the camera definition options to define the close range visibility. */
                public: enum Types
                {
                    TypesRound/** Round type */,
                    TypesRectangle/** Rectangle type */,
                    TypesFace/** Face type */
                };

                private: CloseRangeCameraListItemBuilderImpl * m_closerangecameralistitembuilder_impl;
                private: friend class  _CloseRangeCameraListItemBuilderBuilder;
                protected: CloseRangeCameraListItemBuilder();
                public: ~CloseRangeCameraListItemBuilder();
                /**Returns  the indication if the defined camera will be used for visibility compute. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: bool UseCamera
                (
                );
                /**Sets  the indication if the defined camera will be used for visibility compute. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetUseCamera
                (
                    bool useCamera /** usecamera */ 
                );
                /**Returns  the camera definition type used by the close range visibility. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::VehicleDesign::CloseRangeCameraListItemBuilder::Types CameraType
                (
                );
                /**Sets  the camera definition type used by the close range visibility. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetCameraType
                (
                    NXOpen::Features::VehicleDesign::CloseRangeCameraListItemBuilder::Types cameraType /** cameratype */ 
                );
                /**Returns  the face selections used to identify the camera surface. Only valid when the camera type is face. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::ScCollector * CameraFace
                (
                );
                /**Returns  the indication if the selected camera face surface should be reversed. Only valid when the camera type is face. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: bool FaceReverse
                (
                );
                /**Sets  the indication if the selected camera face surface should be reversed. Only valid when the camera type is face. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetFaceReverse
                (
                    bool faceReverse /** facereverse */ 
                );
                /**Returns  the selected axis defining the camera direction. Only valid when the camera type is round. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Axis * CameraAxis
                (
                );
                /**Sets  the selected axis defining the camera direction. Only valid when the camera type is round. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetCameraAxis
                (
                    NXOpen::Axis * cameraAxis /** cameraaxis */ 
                );
                /**Returns  the coordinate system specifying the camera position. Only valid when the camera type is rectangle. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CoordinateSystem * CameraCsys
                (
                );
                /**Sets  the coordinate system specifying the camera position. Only valid when the camera type is rectangle. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetCameraCsys
                (
                    NXOpen::CoordinateSystem * cameraCsys /** cameracsys */ 
                );
                /**Returns  the expression containing the value for the initial radius. Only valid when the camera type is round. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * InitialRadius
                (
                );
                /**Returns  the expression containing the value for the horizontal legth. Only valid when the camera type is rectangle. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * HorizontalLength
                (
                );
                /**Returns  the expression containing the value for the vertical legth. Only valid when the camera type is rectangle. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * VerticalLength
                (
                );
                /**Returns  the expression containing the value for the view angle. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * ViewAngle
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

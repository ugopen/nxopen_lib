#ifndef NXOpen_FEATURES_CUTFACEBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_CUTFACEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_CutFaceBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/Features_CutFaceBuilder.hxx>
#include <NXOpen/Features_FaceRecognitionBuilder.hxx>
#include <NXOpen/GeometricUtilities_ModlMotion.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Features
    {
        class CutFaceBuilder;
    }
    namespace Features
    {
        class FaceRecognitionBuilder;
    }
    namespace Features
    {
        class FeatureBuilder;
    }
    namespace GeometricUtilities
    {
        class ModlMotion;
    }
    class SelectBody;
    namespace Features
    {
        class _CutFaceBuilderBuilder;
        /**
            Represents a builder for a cut face feature.
             <br> To create a new instance of this class, use @link Features::FeatureCollection::CreateCutFaceBuilder Features::FeatureCollection::CreateCutFaceBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        FaceToCut.CoaxialEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToCut.CoplanarAxesEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToCut.CoplanarEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToCut.EqualDiameterEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToCut.OffsetEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToCut.ParallelEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToCut.PerpendicularEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToCut.SymmetricEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToCut.TangentEnabled </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        FaceToCut.UseFaceBrowse </td> <td> 
         
        1 </td> </tr> 

        <tr><td> 
         
        Motion.DeltaEnum </td> <td> 
         
        ReferenceWcsWorkPart </td> </tr> 

        <tr><td> 
         
        Motion.DeltaXc.Value </td> <td> 
         
        0.0 </td> </tr> 

        <tr><td> 
         
        Motion.DeltaYc.Value </td> <td> 
         
        0.0 </td> </tr> 

        <tr><td> 
         
        Motion.DeltaZc.Value </td> <td> 
         
        0.0 </td> </tr> 

        <tr><td> 
         
        Motion.Option </td> <td> 
         
        DistanceAngle </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT CutFaceBuilder : public Features::FeatureBuilder
        {
            private: friend class  _CutFaceBuilderBuilder;
            protected: CutFaceBuilder();
            /**Returns  the face recognition builder holding the faces to cut.  <br> License requirements : None */
            public: NXOpen::Features::FaceRecognitionBuilder * FaceToCut
            (
            );
            /**Returns  the motion about which the cut faces move  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::ModlMotion * Motion
            (
            );
            /**Returns  the do paste option defines whether paste the cut faces to a target body.  <br> License requirements : None */
            public: bool DoPaste
            (
            );
            /**Sets  the do paste option defines whether paste the cut faces to a target body.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetDoPaste
            (
                bool doPaste /** do paste */ 
            );
            /**Returns  the target body.
                        The target body can be a solid or sheet.  <br> License requirements : None */
            public: NXOpen::SelectBody * TargetBody
            (
            );
            /**Returns  the reverse direction.
                        A flag to indicate whether the target body direction is reversed, disabled if target body is solid.  <br> License requirements : None */
            public: bool ReverseDirection
            (
            );
            /**Sets  the reverse direction.
                        A flag to indicate whether the target body direction is reversed, disabled if target body is solid.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetReverseDirection
            (
                bool reverseDirection /** reverse direction */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif

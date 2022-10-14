#ifndef NXOpen_MFG_AM_SUPPORTBUILDER_HXX_INCLUDED
#define NXOpen_MFG_AM_SUPPORTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mfg_AM_SupportBuilder.ja
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
#include <NXOpen/Mfg_AM_Sketcher.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libmfgamopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mfg
    {
        namespace AM
        {
            class SupportBuilder;
        }
    }
    class Builder;
    class Face;
    namespace Mfg
    {
        namespace AM
        {
            class Sketcher;
        }
    }
    class ScCollector;
    class SelectNXObjectList;
    namespace Mfg
    {
        namespace AM
        {
            class _SupportBuilderBuilder;
            class SupportBuilderImpl;
            /** Represents a @link Mfg::AM::Support Mfg::AM::Support@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Mfg::AM::ApplicationManager::GetSupportBuilder  NXOpen::Mfg::AM::ApplicationManager::GetSupportBuilder @endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            Sketcher.CurveOnSurfaceBuilder.CurveFitData.CurveJoinMethod </td> <td> 
             
            No </td> </tr> 

            <tr><td> 
             
            Sketcher.CurveOnSurfaceBuilder.CurveFitData.Degree </td> <td> 
             
            7 </td> </tr> 

            <tr><td> 
             
            Sketcher.CurveOnSurfaceBuilder.CurveFitData.FitMethod </td> <td> 
             
            DegreeAndSegments </td> </tr> 

            <tr><td> 
             
            Sketcher.CurveOnSurfaceBuilder.CurveFitData.IsAdvancedFit </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            Sketcher.CurveOnSurfaceBuilder.CurveFitData.IsAlignShape </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            Sketcher.CurveOnSurfaceBuilder.CurveFitData.MaximumDegree </td> <td> 
             
            7 </td> </tr> 

            <tr><td> 
             
            Sketcher.CurveOnSurfaceBuilder.CurveFitData.MaximumSegments </td> <td> 
             
            1 </td> </tr> 

            <tr><td> 
             
            Sketcher.CurveOnSurfaceBuilder.CurveFitData.MinimumDegree </td> <td> 
             
            5 </td> </tr> 

            <tr><td> 
             
            Sketcher.CurveOnSurfaceBuilder.CurveFitData.Segments </td> <td> 
             
            1 </td> </tr> 

            <tr><td> 
             
            Sketcher.CurveOnSurfaceBuilder.CurveFitProperties.FitOption </td> <td> 
             
            Cubic </td> </tr> 

            <tr><td> 
             
            Sketcher.CurveOnSurfaceBuilder.CurveFitProperties.MaximumDegree </td> <td> 
             
            7 </td> </tr> 

            <tr><td> 
             
            Sketcher.CurveOnSurfaceBuilder.CurveFitProperties.MaximumSegments </td> <td> 
             
            1 </td> </tr> 

            </table>  

             <br>  Created in NX11.0.2.  <br>  
            */
            class MFGAMOPENCPPEXPORT  SupportBuilder : public NXOpen::Builder
            {
                /** the AM support types */
                public: enum Types
                {
                    TypesBlock/** block */ ,
                    TypesLine/** line */ ,
                    TypesPoint/** point */ ,
                    TypesNosupport/** nosupport */ ,
                    TypesUserDefined/** user defined */ ,
                    TypesVolume/** volume */ ,
                    TypesWeb/** web */ ,
                    TypesContour/** contour */ ,
                    TypesGusset/** gusset */ ,
                    TypesCone/** cone */ 
                };

                private: SupportBuilderImpl * m_supportbuilder_impl;
                private: friend class  _SupportBuilderBuilder;
                protected: SupportBuilder();
                public: ~SupportBuilder();
                /**Returns  the sketcher 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry") */
                public: NXOpen::Mfg::AM::Sketcher * Sketcher
                (
                );
                /**Returns  the body selection 
                 <br>  Created in NX12.0.1.  <br>  
                 <br> License requirements : None */
                public: NXOpen::ScCollector * BodySelection
                (
                );
                /**Returns  the face selection 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::ScCollector * FaceSelection
                (
                );
                /**Returns  the curve selection 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::ScCollector * CurveSelection
                (
                );
                /**Returns  the point selection 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectNXObjectList * PointSelection
                (
                );
                /**Returns  the type 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Mfg::AM::SupportBuilder::Types Type
                (
                );
                /**Sets  the type 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry") */
                public: void SetType
                (
                    NXOpen::Mfg::AM::SupportBuilder::Types type /** type */ 
                );
                /** Set the surface region faces for the support to create 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry") */
                public: void SetSurfaceRegion
                (
                    const std::vector<NXOpen::Face *> & faces /** surface region faces */
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
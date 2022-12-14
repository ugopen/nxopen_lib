#ifndef NXOpen_MFG_AM_SKETCHER_HXX_INCLUDED
#define NXOpen_MFG_AM_SKETCHER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mfg_AM_Sketcher.ja
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
#include <NXOpen/Features_CurveOnSurfaceBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/ScCollector.hxx>
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
            class Sketcher;
        }
    }
    class Builder;
    class Face;
    namespace Features
    {
        class CurveOnSurfaceBuilder;
    }
    class Point;
    class ScCollector;
    class Sketch;
    namespace Mfg
    {
        namespace AM
        {
            class _SketcherBuilder;
            class SketcherImpl;
            /** Represents a @link Mfg::AM::Sketcher Mfg::AM::Sketcher@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Mfg::AM::SupportBuilder::Sketcher  NXOpen::Mfg::AM::SupportBuilder::Sketcher @endlink  <br> 
            Default values.
            <list type="table"> 
             
            <listheader><term> 
            Property</term>  <description> 
            Value</description> </listheader>
            <item><term> 
             
            CurveOnSurfaceBuilder.CurveFitData.CurveJoinMethod </term> <description> 
             
            No </description> </item> 

            <item><term> 
             
            CurveOnSurfaceBuilder.CurveFitData.Degree </term> <description> 
             
            7 </description> </item> 

            <item><term> 
             
            CurveOnSurfaceBuilder.CurveFitData.FitMethod </term> <description> 
             
            DegreeAndSegments </description> </item> 

            <item><term> 
             
            CurveOnSurfaceBuilder.CurveFitData.IsAdvancedFit </term> <description> 
             
            0 </description> </item> 

            <item><term> 
             
            CurveOnSurfaceBuilder.CurveFitData.IsAlignShape </term> <description> 
             
            0 </description> </item> 

            <item><term> 
             
            CurveOnSurfaceBuilder.CurveFitData.MaximumDegree </term> <description> 
             
            7 </description> </item> 

            <item><term> 
             
            CurveOnSurfaceBuilder.CurveFitData.MaximumSegments </term> <description> 
             
            1 </description> </item> 

            <item><term> 
             
            CurveOnSurfaceBuilder.CurveFitData.MinimumDegree </term> <description> 
             
            5 </description> </item> 

            <item><term> 
             
            CurveOnSurfaceBuilder.CurveFitData.Segments </term> <description> 
             
            1 </description> </item> 

            <item><term> 
             
            CurveOnSurfaceBuilder.CurveFitProperties.FitOption </term> <description> 
             
            Cubic </description> </item> 

            <item><term> 
             
            CurveOnSurfaceBuilder.CurveFitProperties.MaximumDegree </term> <description> 
             
            7 </description> </item> 

            <item><term> 
             
            CurveOnSurfaceBuilder.CurveFitProperties.MaximumSegments </term> <description> 
             
            1 </description> </item> 

            </list> 

             <br>  Created in NX11.0.2.  <br>  
            */
            class MFGAMOPENCPPEXPORT  Sketcher : public NXOpen::Builder
            {
                /** the sketcher mode */
                public: enum Mode
                {
                    ModeSurfaceFace/** surface face */ ,
                    ModeSurfaceLine/** surface line */ ,
                    ModeSketchFace/** sketch face */ ,
                    ModeSketchLine/** sketch line */ 
                };

                private: SketcherImpl * m_sketcher_impl;
                private: friend class  _SketcherBuilder;
                protected: Sketcher();
                public: ~Sketcher();
                /**Returns  the sketch mode 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Mfg::AM::Sketcher::Mode SketchMode
                (
                );
                /**Sets  the sketch mode 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry") */
                public: void SetSketchMode
                (
                    NXOpen::Mfg::AM::Sketcher::Mode sketchMode /** sketchmode */ 
                );
                /**Returns  the sketch geometry collector 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::ScCollector * SketchCollector
                (
                );
                /**Returns  the Curve On Surface feature builder 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::CurveOnSurfaceBuilder * CurveOnSurfaceBuilder
                (
                );
                /** Set the faces to sketch the curve upon 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry") */
                public: void SetSketchCanvas
                (
                    const std::vector<NXOpen::Face *> & faces /** sketch faces */
                );
                /**Sets  the flag indicating if curve should be closed 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry") */
                public: void SetCloseCurve
                (
                    bool bCloseCurve /** bclosecurve */ 
                );
                /**Returns  the flag indicating if curve should be closed 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : None */
                public: bool CloseCurve
                (
                );
                /** Creates or extends the curve with points 
                 <br>  Created in NX11.0.2.  <br>  
                 <br> License requirements : am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry") */
                public: void AddCurvePoints
                (
                    const std::vector<NXOpen::Point *> & points /** sketch points */
                );
                /**Returns  the sketch which holds the section curves 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Sketch * Sketch
                (
                );
                /**Sets  the sketch which holds the section curves 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry") */
                public: void SetSketch
                (
                    NXOpen::Sketch * sectionSketch /** sectionsketch */ 
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

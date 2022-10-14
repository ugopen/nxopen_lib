#ifndef NXOpen_COMPOSITES_ROSETTEBUILDER_HXX_INCLUDED
#define NXOpen_COMPOSITES_ROSETTEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Composites_RosetteBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/libcompositesopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Composites
    {
        class RosetteBuilder;
    }
    class Builder;
    class CartesianCoordinateSystem;
    class Direction;
    namespace Features
    {
        class Feature;
    }
    class Point;
    namespace Composites
    {
        class _RosetteBuilderBuilder;
        class RosetteBuilderImpl;

        /// \cond NX_NO_DOC 
        /**
            Creates or edits a @link Composites::Rosette Composites::Rosette@endlink  object
             <br> To create a new instance of this class, use @link NXOpen::Composites::Manager::CreateRosetteBuilder  NXOpen::Composites::Manager::CreateRosetteBuilder @endlink  <br> 
         <br>  Usable only on Windows <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class COMPOSITESOPENCPPEXPORT  RosetteBuilder : public NXOpen::Builder
        {

            /// \cond NX_NO_DOC 
             /** the information required for creating a standard-mapping rosette. */
            public:
            struct StandardRosetteInfo
            {
                public: /** the @link Point Point@endlink  defining the point at which the standard-mapping rosette's zero direction is defined. */NXOpen::Point * OriginPoint;
                public: /** the @link Direction Direction@endlink  defining the zero direction of a standard-mapping rosette. */NXOpen::Direction * ZeroDirection;
                public: /** the @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink  defining the surface the standard-mapping rosette's origin must lie on. */NXOpen::Features::Feature * LayupSurface;
                public: StandardRosetteInfo() :
                    OriginPoint(),
                    ZeroDirection(),
                    LayupSurface()
                {
                }
                /** Constructor for the StandardRosetteInfo struct. */ 
                public: StandardRosetteInfo(NXOpen::Point * originPointInitial /** the @link Point Point@endlink  defining the point at which the standard-mapping rosette's zero direction is defined. */, 
                        NXOpen::Direction * zeroDirectionInitial /** the @link Direction Direction@endlink  defining the zero direction of a standard-mapping rosette. */, 
                        NXOpen::Features::Feature * layupSurfaceInitial /** the @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink  defining the surface the standard-mapping rosette's origin must lie on. */) :
                    OriginPoint(originPointInitial),
                    ZeroDirection(zeroDirectionInitial),
                    LayupSurface(layupSurfaceInitial)
                {
                }
            };


            /// \endcond 

            /// \cond NX_NO_DOC 
             /** the information required for creating a translational-mapping rosette. */
            public:
            struct TranslationalRosetteInfo
            {
                public: /** the @link CartesianCoordinateSystem CartesianCoordinateSystem@endlink  defining the orientations at a single location for translational-mapping rosette. */NXOpen::CartesianCoordinateSystem * ReferenceCsys;
                public: TranslationalRosetteInfo() :
                    ReferenceCsys()
                {
                }
                /** Constructor for the TranslationalRosetteInfo struct. */ 
                public: TranslationalRosetteInfo(NXOpen::CartesianCoordinateSystem * referenceCsysInitial /** the @link CartesianCoordinateSystem CartesianCoordinateSystem@endlink  defining the orientations at a single location for translational-mapping rosette. */) :
                    ReferenceCsys(referenceCsysInitial)
                {
                }
            };


            /// \endcond 
            private: RosetteBuilderImpl * m_rosettebuilder_impl;
            private: friend class  _RosetteBuilderBuilder;
            protected: RosetteBuilder();
            public: ~RosetteBuilder();

            /// \cond NX_NO_DOC 
            /**Returns  the @link CartesianCoordinateSystem CartesianCoordinateSystem@endlink  defining the orientations at a single location 
             <br>  Usable only on Windows <br> 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Composites::RosetteBuilder::TranslationalRosetteInfo TranslationalRosetteData
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the @link CartesianCoordinateSystem CartesianCoordinateSystem@endlink  defining the orientations at a single location 
             <br>  Usable only on Windows <br> 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void SetTranslationalRosetteData
            (
                const NXOpen::Composites::RosetteBuilder::TranslationalRosetteInfo & translationalRosetteData /** translationalrosettedata */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Returns  the @link Composites::RosetteBuilder::StandardRosetteInfo Composites::RosetteBuilder::StandardRosetteInfo@endlink  defining the data required for the standard-mapping rosette. 
             <br>  Usable only on Windows <br> 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Composites::RosetteBuilder::StandardRosetteInfo StandardRosetteData
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /**Sets  the @link Composites::RosetteBuilder::StandardRosetteInfo Composites::RosetteBuilder::StandardRosetteInfo@endlink  defining the data required for the standard-mapping rosette. 
             <br>  Usable only on Windows <br> 
             <br>  Created in NX2007.0.0.  <br>  
             <br> License requirements : None */
            public: void SetStandardRosetteData
            (
                const NXOpen::Composites::RosetteBuilder::StandardRosetteInfo & standardRosetteData /** standardrosettedata */ 
            );

            /// \endcond 
        };

        /// \endcond 
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
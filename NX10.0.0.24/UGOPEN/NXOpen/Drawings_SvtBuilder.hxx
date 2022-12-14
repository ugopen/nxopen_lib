#ifndef NXOpen_DRAWINGS_SVTBUILDER_HXX_INCLUDED
#define NXOpen_DRAWINGS_SVTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_SvtBuilder.ja
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
#include <NXOpen/Drawings_SvtBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_drawings_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Drawings
    {
        class SvtBuilder;
    }
    class Direction;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class SelectFaceList;
    namespace Drawings
    {
        class _SvtBuilderBuilder;
        class SvtBuilderImpl;
        /**
            Represents a @link NXOpen::Drawings::SvtBuilder NXOpen::Drawings::SvtBuilder@endlink 
            
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  SvtBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: SvtBuilderImpl * m_svtbuilder_impl;
            private: friend class  _SvtBuilderBuilder;
            protected: SvtBuilder();
            public: ~SvtBuilder();
            /**Returns  the orientation flag that indicates whether or not the Section View Tool view should be used to orient the section view when it is placed 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: bool Orientation
            (
            );
            /**Sets  the orientation flag that indicates whether or not the Section View Tool view should be used to orient the section view when it is placed 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetOrientation
            (
                bool orientation /** orientation */ 
            );
            /**Returns  the background faces that are to be shown in the section view.  When none are selected, all faces will be shown 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::SelectFaceList * BackgroundFaces
            (
            );
            /**Returns  the vector that represents the normal direction for the view to be created or edited.
                        The vector is used only if the Orientation flag is on.  The purpose of the direction
                        vectors is make a simple, simulated pictorial view.  Consequently it is expected that
                        a desireable orientation will need to be found interactive using the tool, and that
                        specification by vectors will be of marginal use.  The ability to specifiy the orientation
                        is being included only for completeness. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Direction * NormalDirection
            (
            );
            /**Sets  the vector that represents the normal direction for the view to be created or edited.
                        The vector is used only if the Orientation flag is on.  The purpose of the direction
                        vectors is make a simple, simulated pictorial view.  Consequently it is expected that
                        a desireable orientation will need to be found interactive using the tool, and that
                        specification by vectors will be of marginal use.  The ability to specifiy the orientation
                        is being included only for completeness. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetNormalDirection
            (
                NXOpen::Direction * normalDirection /** normaldirection */ 
            );
            /**Returns  the x direction vector for the view to be created or edited.
                        The vector is used only if the Orientation flag is on.  The purpose of the direction
                        vectors is make a simple, simulated pictorial view.  Consequently it is expected that
                        a desireable orientation will need to be found interactive using the tool, and that
                        specification by vectors will be of marginal use.  The ability to specifiy the orientation
                        is being included only for completeness. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: NXOpen::Direction * XDirection
            (
            );
            /**Sets  the x direction vector for the view to be created or edited.
                        The vector is used only if the Orientation flag is on.  The purpose of the direction
                        vectors is make a simple, simulated pictorial view.  Consequently it is expected that
                        a desireable orientation will need to be found interactive using the tool, and that
                        specification by vectors will be of marginal use.  The ability to specifiy the orientation
                        is being included only for completeness. 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : drafting ("DRAFTING") */
            public: void SetXDirection
            (
                NXOpen::Direction * xDirection /** xdirection */ 
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

#ifndef NXOpen_GEOMETRICUTILITIES_ONPATHDIMENSIONBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_ONPATHDIMENSIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_OnPathDimensionBuilder.ja
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
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_geometricutilities_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace GeometricUtilities
    {
        class OnPathDimensionBuilder;
    }
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class Point;
    class SelectObject;
    namespace GeometricUtilities
    {
        class _OnPathDimensionBuilderBuilder;
        class OnPathDimensionBuilderImpl;
        /** Builds an on-path dimension 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_GEOMETRICUTILITIESEXPORT  OnPathDimensionBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** The type of update to perform */
            public: enum UpdateReason
            {
                UpdateReasonPath/** Update because of the path may have changed */ = 1,
                UpdateReasonThroughPoint/** Update because the through point location may have changed */,
                UpdateReasonAll/** Update because either path or through point location may have changed */
            };

            private: OnPathDimensionBuilderImpl * m_onpathdimensionbuilder_impl;
            private: friend class  _OnPathDimensionBuilderBuilder;
            protected: OnPathDimensionBuilder();
            public: ~OnPathDimensionBuilder();
            /**Returns  the expression for the value of the dimension 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * Expression
            (
            );
            /**Returns  a flag indicating whether the length along the path is evaluated
                        starting from the end point of path instead of the start point of the path 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsFlipped
            (
            );
            /**Sets  a flag indicating whether the length along the path is evaluated
                        starting from the end point of path instead of the start point of the path 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetFlipped
            (
                bool flipped /** flipped */ 
            );
            /**Returns  a flag indicating whether the expression represents the percentage along
                        the path.  If false, the expression represents the length along the path 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsPercentUsed
            (
            );
            /**Sets  a flag indicating whether the expression represents the percentage along
                        the path.  If false, the expression represents the length along the path 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPercentUsed
            (
                bool usePercent /** use percent */ 
            );
            /**Returns  a flag indicating whether the expression is in terms of the mathematical
                        parameter of the path (is_parameter_used = true) or in terms of its 
                        arclength (is_parameter_used = false).  When value is true, the value
                        will always be expressed in terms of percentage (between 0 and 100) regardless
                        of is_percent_used's setting.  This property must be used with care.  Most 
                        referencing classes will only accept arclength values, and setting this property 
                        to true for those classes will result in a run time error.  Consult the referencing
                        class documentation to see if this value can be true for that particular operation. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsParameterUsed
            (
            );
            /**Sets  a flag indicating whether the expression is in terms of the mathematical
                        parameter of the path (is_parameter_used = true) or in terms of its 
                        arclength (is_parameter_used = false).  When value is true, the value
                        will always be expressed in terms of percentage (between 0 and 100) regardless
                        of is_percent_used's setting.  This property must be used with care.  Most 
                        referencing classes will only accept arclength values, and setting this property 
                        to true for those classes will result in a run time error.  Consult the referencing
                        class documentation to see if this value can be true for that particular operation. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetParameterUsed
            (
                bool useParameter /** use parameter */ 
            );
            /**Returns  the path that the dimension is evaluated on.  Note: in some cases, the
                        builder will not permit you to change the path 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectObject * Path
            (
            );
            /**Returns  the through point 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * ThroughPoint
            (
            );
            /**Sets  the through point 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetThroughPoint
            (
                NXOpen::Point * throughPoint /** throughpoint */ 
            );
            /** Updates this object if the path or through point location has changed.  
                    Call this function if the path is a section
                    and you have added or removed curves from the section, or if there
                    is a through point and the coordinates of the through point have changed. 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void Update
            (
                NXOpen::GeometricUtilities::OnPathDimensionBuilder::UpdateReason updateReason /** updatereason */ 
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

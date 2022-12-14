#ifndef NXOpen_CAE_ELEMENTSPLITBUILDER_HXX_INCLUDED
#define NXOpen_CAE_ELEMENTSPLITBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ElementSplitBuilder.ja
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
#include <NXOpen/CAE_ElementSplitBuilder.hxx>
#include <NXOpen/CAE_SelectElementsBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class ElementSplitBuilder;
    }
    class Builder;
    namespace CAE
    {
        class SelectElementsBuilder;
    }
    class Point;
    namespace CAE
    {
        class _ElementSplitBuilderBuilder;
        class ElementSplitBuilderImpl;
        /**
            Represents a @link NXOpen::CAE::ElementSplitBuilder NXOpen::CAE::ElementSplitBuilder@endlink 
             <br> To create a new instance of this class, use @link NXOpen::CAE::NodeElementManager::CreateElementSplitBuilder  NXOpen::CAE::NodeElementManager::CreateElementSplitBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ElementSplitBuilder : public NXOpen::Builder
        {
            /** the element split types */
            public: enum Types
            {
                TypesQuadTo2Tria/**Quad to 2 Tria */,
                TypesQuadTo2Quad/**Quad to 2 Quad */,
                TypesQuadTo4Quad/**Quad to 4 Quad */,
                TypesQuadTo3Quad/**Quad to 3 Quad */,
                TypesQuadTo3Tria/**Quad to 3 Tria */,
                TypesTriaTo4Tria/**Tria to 4 Tria */,
                TypesSplitByLine/**Split by line */,
                TypesTriaTo2Tria/**Tria to 2 Tria */
            };

            /** the split method types */
            public: enum SplitMethodType
            {
                SplitMethodTypeSeedElement/**by vector comparison */,
                SplitMethodTypeExistingConnectivity/**use existing element connectivity*/,
                SplitMethodTypeInteractiveMouseLocation/**Interactive Element Split*/,
                SplitMethodTypeElementShape/**Based on element shape*/
            };

            private: ElementSplitBuilderImpl * m_elementsplitbuilder_impl;
            private: friend class  _ElementSplitBuilderBuilder;
            protected: ElementSplitBuilder();
            public: ~ElementSplitBuilder();
            /**Returns  the split type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ElementSplitBuilder::Types Type
            (
            );
            /**Sets  the split type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetType
            (
                NXOpen::CAE::ElementSplitBuilder::Types type /** type */ 
            );
            /**Returns  the selected elements 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::SelectElementsBuilder * Elementsss
            (
            );
            /** Flip will not be journaled now
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void Flip
            (
            );
            /**Returns  the flip_type for first element in the selection list
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: int FirstElementSplitType
            (
            );
            /**Sets  the flip_type for first element in the selection list
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetFirstElementSplitType
            (
                int data /** data */ 
            );
            /**Returns  the use existing connectivity option
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ElementSplitBuilder::SplitMethodType SplitMethod
            (
            );
            /**Sets  the use existing connectivity option
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetSplitMethod
            (
                NXOpen::CAE::ElementSplitBuilder::SplitMethodType option /** option */ 
            );
            /**Returns  the point1, one end of line when split by line
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * Point1
            (
            );
            /**Sets  the point1, one end of line when split by line
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetPoint1
            (
                NXOpen::Point * point1 /** point1 */ 
            );
            /**Returns  the point2, the other end of line when split by line 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * Point2
            (
            );
            /**Sets  the point2, the other end of line when split by line 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetPoint2
            (
                NXOpen::Point * point2 /** point2 */ 
            );
            /**Returns  a value indicating whether elements are to be split based on Warp.  If True, elements with warp values that exceeds the value of @link NXOpen::CAE::ElementSplitBuilder::WarpValue NXOpen::CAE::ElementSplitBuilder::WarpValue @endlink and @link NXOpen::CAE::ElementSplitBuilder::SetWarpValue NXOpen::CAE::ElementSplitBuilder::SetWarpValue @endlink  are split.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: bool WarpToggle
            (
            );
            /**Sets  a value indicating whether elements are to be split based on Warp.  If True, elements with warp values that exceeds the value of @link NXOpen::CAE::ElementSplitBuilder::WarpValue NXOpen::CAE::ElementSplitBuilder::WarpValue @endlink and @link NXOpen::CAE::ElementSplitBuilder::SetWarpValue NXOpen::CAE::ElementSplitBuilder::SetWarpValue @endlink  are split.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetWarpToggle
            (
                bool warpToggle /** warptoggle */ 
            );
            /**Returns  a threshold warp value.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: double WarpValue
            (
            );
            /**Sets  a threshold warp value.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetWarpValue
            (
                double warpValue /** warpvalue */ 
            );
            /**Returns  a value indicating whether elements are to be split based on Minimum Angle.  If True, elements having minimum angle values less than the value of @link NXOpen::CAE::ElementSplitBuilder::MinAngleValue NXOpen::CAE::ElementSplitBuilder::MinAngleValue @endlink and @link NXOpen::CAE::ElementSplitBuilder::SetMinAngleValue NXOpen::CAE::ElementSplitBuilder::SetMinAngleValue @endlink  are split.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: bool MinAngleToggle
            (
            );
            /**Sets  a value indicating whether elements are to be split based on Minimum Angle.  If True, elements having minimum angle values less than the value of @link NXOpen::CAE::ElementSplitBuilder::MinAngleValue NXOpen::CAE::ElementSplitBuilder::MinAngleValue @endlink and @link NXOpen::CAE::ElementSplitBuilder::SetMinAngleValue NXOpen::CAE::ElementSplitBuilder::SetMinAngleValue @endlink  are split.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetMinAngleToggle
            (
                bool minAngleToggle /** minangletoggle */ 
            );
            /**Returns  a threshold minimum angle value.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: double MinAngleValue
            (
            );
            /**Sets  a threshold minimum angle value.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetMinAngleValue
            (
                double minAngleValue /** minanglevalue */ 
            );
            /**Returns  a value indicating whether elements are to be split based on Maximum Angle.  If True, elements with maximum angle values that exceeds the value of @link NXOpen::CAE::ElementSplitBuilder::MaxAngleValue NXOpen::CAE::ElementSplitBuilder::MaxAngleValue @endlink and @link NXOpen::CAE::ElementSplitBuilder::SetMaxAngleValue NXOpen::CAE::ElementSplitBuilder::SetMaxAngleValue @endlink  are split.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: bool MaxAngleToggle
            (
            );
            /**Sets  a value indicating whether elements are to be split based on Maximum Angle.  If True, elements with maximum angle values that exceeds the value of @link NXOpen::CAE::ElementSplitBuilder::MaxAngleValue NXOpen::CAE::ElementSplitBuilder::MaxAngleValue @endlink and @link NXOpen::CAE::ElementSplitBuilder::SetMaxAngleValue NXOpen::CAE::ElementSplitBuilder::SetMaxAngleValue @endlink  are split.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetMaxAngleToggle
            (
                bool maxAngleToggle /** maxangletoggle */ 
            );
            /**Returns  a threshold Maximum Angle Value
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: double MaxAngleValue
            (
            );
            /**Sets  a threshold Maximum Angle Value
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetMaxAngleValue
            (
                double maxAngleValue /** maxanglevalue */ 
            );
            /**Returns  a value indicating whether elements are to be split based on Jacobian.  If True, elements with jacobian values that exceeds the value of @link NXOpen::CAE::ElementSplitBuilder::JacobianValue NXOpen::CAE::ElementSplitBuilder::JacobianValue @endlink and @link NXOpen::CAE::ElementSplitBuilder::SetJacobianValue NXOpen::CAE::ElementSplitBuilder::SetJacobianValue @endlink  are split.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: bool JacobianToggle
            (
            );
            /**Sets  a value indicating whether elements are to be split based on Jacobian.  If True, elements with jacobian values that exceeds the value of @link NXOpen::CAE::ElementSplitBuilder::JacobianValue NXOpen::CAE::ElementSplitBuilder::JacobianValue @endlink and @link NXOpen::CAE::ElementSplitBuilder::SetJacobianValue NXOpen::CAE::ElementSplitBuilder::SetJacobianValue @endlink  are split.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetJacobianToggle
            (
                bool jacobianToggle /** jacobiantoggle */ 
            );
            /**Returns a threshold jacobian value.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: double JacobianValue
            (
            );
            /**Sets a threshold jacobian value.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetJacobianValue
            (
                double jacobianValue /** jacobianvalue */ 
            );
            /**Returns  a value indicating whether duplicate nodes created during split are to be merged. If false, this is user's responsibilty to merge duplicate nodes.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: bool MergeDupNode
            (
            );
            /**Sets  a value indicating whether duplicate nodes created during split are to be merged. If false, this is user's responsibilty to merge duplicate nodes.
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetMergeDupNode
            (
                bool mergeDupNode /** mergedupnode */ 
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

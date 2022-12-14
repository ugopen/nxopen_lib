#ifndef NXOpen_DIE_QUICKBINDERWRAPBUILDER_HXX_INCLUDED
#define NXOpen_DIE_QUICKBINDERWRAPBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Die_QuickBinderWrapBuilder.ja
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
#include <NXOpen/Die_QuickBinderWrapBuilder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_die_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Die
    {
        class QuickBinderWrapBuilder;
    }
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class SelectBodyList;
    namespace Die
    {
        class _QuickBinderWrapBuilderBuilder;
        class QuickBinderWrapBuilderImpl;
        /**
            Represents a @link NXOpen::Die::QuickBinderWrapBuilder NXOpen::Die::QuickBinderWrapBuilder@endlink  builder
             <br> This is an abstract class, and cannot be created.  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_DIEEXPORT  QuickBinderWrapBuilder : public NXOpen::Features::FeatureBuilder
        {
            /** Settings for the binder wrap sheet body type. */
            public: enum Types
            {
                TypesPlanar/** Planar */,
                TypesCylindrical/** Cylidrical */,
                TypesConical/** Conical */
            };

            /** Settings for the edit size type. */
            public: enum EditSizeType
            {
                EditSizeTypeRadius/** radius */ ,
                EditSizeTypeScale/** scale */ 
            };

            private: QuickBinderWrapBuilderImpl * m_quickbinderwrapbuilder_impl;
            private: friend class  _QuickBinderWrapBuilderBuilder;
            protected: QuickBinderWrapBuilder();
            public: ~QuickBinderWrapBuilder();
            /**Returns  the button 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectBodyList * Button
            (
            );
            /**Returns  the method 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Die::QuickBinderWrapBuilder::Types Type
            (
            );
            /**Sets  the method 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetType
            (
                NXOpen::Die::QuickBinderWrapBuilder::Types type /** type */ 
            );
            /**Returns  the origin 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point3d Origin
            (
            );
            /**Sets  the origin 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetOrigin
            (
                const NXOpen::Point3d & origin /** origin */ 
            );
            /**Returns  the rotation matrix 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Matrix3x3 Matrix
            (
            );
            /**Sets  the rotation matrix 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetMatrix
            (
                const NXOpen::Matrix3x3 & matrix /** matrix */ 
            );
            /**Returns  the change radius value 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ChangeRadius
            (
            );
            /**Returns  the minumum U value 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * UMinimum
            (
            );
            /**Returns  the maximum U value 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * UMaximum
            (
            );
            /**Returns  the minumum V value 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * VMinimum
            (
            );
            /**Returns  the maximum V value 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * VMaximum
            (
            );
            /**Returns  the edit size choice 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Die::QuickBinderWrapBuilder::EditSizeType EditSizeChoice
            (
            );
            /**Sets  the edit size choice 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : die_engineering ("DIE ENGINEERING") */
            public: void SetEditSizeChoice
            (
                NXOpen::Die::QuickBinderWrapBuilder::EditSizeType sizeChoice /** sizechoice */ 
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

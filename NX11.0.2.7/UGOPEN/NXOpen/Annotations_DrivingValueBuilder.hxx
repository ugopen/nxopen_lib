#ifndef NXOpen_ANNOTATIONS_DRIVINGVALUEBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_DRIVINGVALUEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_DrivingValueBuilder.ja
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
#include <NXOpen/Annotations_DrivingValueBuilder.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Annotations
    {
        class DrivingValueBuilder;
    }
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Annotations
    {
        class _DrivingValueBuilderBuilder;
        class DrivingValueBuilderImpl;
        /** 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  DrivingValueBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** the driving value method */
            public: enum DrivingValueMethod
            {
                DrivingValueMethodInferred/** inferred */ ,
                DrivingValueMethodDriving/** driving */ ,
                DrivingValueMethodReference/** reference */ 
            };

            /** the driving expression mode */
            public: enum DrivingExpressionMode
            {
                DrivingExpressionModeMeasureGeometry/** measure geometry */ ,
                DrivingExpressionModeKeepExpression/** keep expression */ 
            };

            private: DrivingValueBuilderImpl * m_drivingvaluebuilder_impl;
            private: friend class  _DrivingValueBuilderBuilder;
            protected: DrivingValueBuilder();
            public: ~DrivingValueBuilder();
            /**Returns  the driving method 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::DrivingValueBuilder::DrivingValueMethod DrivingMethod
            (
            );
            /**Sets  the driving method 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetDrivingMethod
            (
                NXOpen::Annotations::DrivingValueBuilder::DrivingValueMethod drivingMethod /** drivingmethod */ 
            );
            /**Returns  the reference dimension toggle used to create the dimension as reference instead of driving. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: bool Reference
            (
            );
            /**Sets  the reference dimension toggle used to create the dimension as reference instead of driving. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetReference
            (
                bool reference /** reference */ 
            );
            /**Returns  the expression name 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXString ExpressionName
            (
            );
            /**Sets  the expression name 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetExpressionName
            (
                const NXString & expressionName /** expressionname */ 
            );
            /**Sets  the expression name 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") OR geometric_tol ("GDT") */
            void SetExpressionName
            (
                const char * expressionName /** expressionname */ 
            );
            /**Returns  the expression value 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ExpressionValue
            (
            );
            /**Sets  the expression mode 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") OR geometric_tol ("GDT") */
            public: void SetExpressionMode
            (
                NXOpen::Annotations::DrivingValueBuilder::DrivingExpressionMode expressionMode /** expressionmode */ 
            );
            /**Returns  the expression mode 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::DrivingValueBuilder::DrivingExpressionMode ExpressionMode
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

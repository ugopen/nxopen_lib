#ifndef NXOpen_GEOMETRICUTILITIES_POINTSETALIGNMENTBUILDER_HXX_INCLUDED
#define NXOpen_GEOMETRICUTILITIES_POINTSETALIGNMENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     GeometricUtilities_PointSetAlignmentBuilder.ja
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
#include <NXOpen/GeometricUtilities_PointSetAlignmentBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace GeometricUtilities
    {
        class PointSetAlignmentBuilder;
    }
    class Builder;
    class SelectDisplayableObjectList;
    class SelectPointList;
    namespace GeometricUtilities
    {
        class _PointSetAlignmentBuilderBuilder;
        class PointSetAlignmentBuilderImpl;
        /** This class performs a point set to point set alignment  <br> To create a new instance of this class, use @link Part::CreatePointSetAlignmentBuilder Part::CreatePointSetAlignmentBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Constraint </td> <td> 
         
        None </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT  PointSetAlignmentBuilder : public Builder
        {
            /** Constraint Options */
            public: enum ConstraintOptions
            {
                ConstraintOptionsNone/** No constraint */,
                ConstraintOptionsX/** X axis */,
                ConstraintOptionsY/** Y axis */,
                ConstraintOptionsZ/** Z axis */
            };

            private: PointSetAlignmentBuilderImpl * m_pointsetalignmentbuilder_impl;
            private: friend class  _PointSetAlignmentBuilderBuilder;
            protected: PointSetAlignmentBuilder();
            public: ~PointSetAlignmentBuilder();
            /**Returns  the objects to move  <br> License requirements : None */
            public: NXOpen::SelectDisplayableObjectList * ObjectsToMove
            (
            );
            /**Returns  the "from" point set  <br> License requirements : None */
            public: NXOpen::SelectPointList * FromPointSet
            (
            );
            /**Returns  the "to" point set  <br> License requirements : None */
            public: NXOpen::SelectPointList * ToPointSet
            (
            );
            /**Returns  the constraint  <br> License requirements : None */
            public: NXOpen::GeometricUtilities::PointSetAlignmentBuilder::ConstraintOptions Constraint
            (
            );
            /**Sets  the constraint  <br> License requirements : studio_free_form ("STUDIO FREE FORM") */
            public: void SetConstraint
            (
                NXOpen::GeometricUtilities::PointSetAlignmentBuilder::ConstraintOptions constraint /** constraint */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif

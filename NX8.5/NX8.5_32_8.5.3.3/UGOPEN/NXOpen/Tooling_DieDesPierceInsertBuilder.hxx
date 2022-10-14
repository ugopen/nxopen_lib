#ifndef NXOpen_TOOLING_DIEDESPIERCEINSERTBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_DIEDESPIERCEINSERTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_DieDesPierceInsertBuilder.ja
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
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/Tooling_DieDesPierceInsertBuilder.hxx>
#include <NXOpen/libnxopencpp_tooling_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Tooling
    {
        class DieDesPierceInsertBuilder;
    }
    class Builder;
    class ScCollector;
    namespace Tooling
    {
        class _DieDesPierceInsertBuilderBuilder;
        class DieDesPierceInsertBuilderImpl;
        /** Represents Die Design Pierce Insert builder.  <br> To create a new instance of this class, use @link Tooling::AutoDieCollection::CreateDieDesPierceInsertBuilder  Tooling::AutoDieCollection::CreateDieDesPierceInsertBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        ThicknessDirectionOption </td> <td> 
         
        Upper </td> </tr> 

        <tr><td> 
         
        ThicknessValue </td> <td> 
         
        0.8 </td> </tr> 

        </table>  

         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_TOOLINGEXPORT  DieDesPierceInsertBuilder : public Builder
        {
            /** Represents the thickness direction. */
            public: enum Direction
            {
                DirectionUpper/** upper */ ,
                DirectionLower/** lower */ 
            };

            /** Represents the hole shape type. */
            public: enum HoleShapeTypes
            {
                HoleShapeTypesCircular/** circular */ ,
                HoleShapeTypesOblong/** oblong */ ,
                HoleShapeTypesSquare/** square */ ,
                HoleShapeTypesRectangular/** rectangular */ ,
                HoleShapeTypesRoundedRectangular/** rounded rectangular */ ,
                HoleShapeTypesChordRectangular/** chord rectangular */ ,
                HoleShapeTypesHexagonal/** hexagonal */ ,
                HoleShapeTypesOther/** other */ 
            };

            private: DieDesPierceInsertBuilderImpl * m_diedespierceinsertbuilder_impl;
            private: friend class  _DieDesPierceInsertBuilderBuilder;
            protected: DieDesPierceInsertBuilder();
            public: ~DieDesPierceInsertBuilder();
            /**Returns  the boundary curve selection. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::ScCollector * BoudaryCurveSelection
            (
            );
            /**Returns  the up tolerance value for length. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double UpToleranceForLength
            (
            );
            /**Sets  the up tolerance value for length. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetUpToleranceForLength
            (
                double upToleranceForLength /** uptoleranceforlength */ 
            );
            /**Returns  the down tolerance value for length. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double DownToleranceForLength
            (
            );
            /**Sets  the down tolerance value for length. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDownToleranceForLength
            (
                double downToleranceForLength /** downtoleranceforlength */ 
            );
            /**Returns  the up tolerance value for width. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double UpToleranceForWidth
            (
            );
            /**Sets  the up tolerance value for width. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetUpToleranceForWidth
            (
                double upToleranceForWidth /** uptoleranceforwidth */ 
            );
            /**Returns  the down tolerance value for width. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double DownToleranceForWidth
            (
            );
            /**Sets  the down tolerance value for width. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDownToleranceForWidth
            (
                double downToleranceForWidth /** downtoleranceforwidth */ 
            );
            /**Returns  the thickness direction option. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Tooling::DieDesPierceInsertBuilder::Direction ThicknessDirectionOption
            (
            );
            /**Sets  the thickness direction option. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetThicknessDirectionOption
            (
                NXOpen::Tooling::DieDesPierceInsertBuilder::Direction thicknessDirectionOption /** thicknessdirectionoption */ 
            );
            /**Returns  the thickness value. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double ThicknessValue
            (
            );
            /**Sets  the thickness value. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetThicknessValue
            (
                double thicknessValue /** thicknessvalue */ 
            );
            /**Returns  the punch penetration value.  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double PunchPenetration
            (
            );
            /**Sets  the punch penetration value.  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetPunchPenetration
            (
                double punchPenetration /** punchpenetration */ 
            );
            /**Returns  the clearance coefficient value. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double ClearanceCoefficient
            (
            );
            /**Sets  the clearance coefficient value. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetClearanceCoefficient
            (
                double clearanceCoefficient /** clearancecoefficient */ 
            );
            /**Returns  the die penetration value. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double DiePenetration
            (
            );
            /**Sets  the die penetration value. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetDiePenetration
            (
                double diePenetration /** diepenetration */ 
            );
            /**Returns  the tolerance coefficient value. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: double ToleranceCoefficient
            (
            );
            /**Sets  the tolerance coefficient value. 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ug_die_design ("Die Design") */
            public: void SetToleranceCoefficient
            (
                double toleranceCoefficient /** tolerancecoefficient */ 
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
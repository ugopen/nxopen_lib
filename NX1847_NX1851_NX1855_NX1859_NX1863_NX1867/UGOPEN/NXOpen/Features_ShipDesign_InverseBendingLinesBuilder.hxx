#ifndef NXOpen_FEATURES_SHIPDESIGN_INVERSEBENDINGLINESBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_INVERSEBENDINGLINESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_InverseBendingLinesBuilder.ja
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
#include <NXOpen/Features_FeatureBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace ShipDesign
        {
            class InverseBendingLinesBuilder;
        }
    }
    class Body;
    class CoordinateSystem;
    class Expression;
    namespace Features
    {
        class FeatureBuilder;
    }
    class Point;
    class SelectBodyList;
    namespace Features
    {
        namespace ShipDesign
        {
            class _InverseBendingLinesBuilderBuilder;
            class InverseBendingLinesBuilderImpl;
            /**
                Used to create or edit a @link NXOpen::Features::ShipDesign::InverseBendingLines NXOpen::Features::ShipDesign::InverseBendingLines@endlink  feature.
                This builder can create or edit multiple features, depending on the number of profile bodies input.
                 <br> To create a new instance of this class, use @link NXOpen::Features::ShipCollection::CreateInverseBendingLinesBuilder  NXOpen::Features::ShipCollection::CreateInverseBendingLinesBuilder @endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            DrawVentHoles </td> <td> 
             
            1 </td> </tr> 

            <tr><td> 
             
            Extension.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            FillingCoefficient </td> <td> 
             
            0.75 </td> </tr> 

            <tr><td> 
             
            GridSpacing.Value </td> <td> 
             
            200 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            LowerMargin.Value </td> <td> 
             
            2.5 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            MaxNumberOfCurves </td> <td> 
             
            5 </td> </tr> 

            <tr><td> 
             
            Measure </td> <td> 
             
            LeftToRight </td> </tr> 

            <tr><td> 
             
            Method </td> <td> 
             
            Automatic </td> </tr> 

            <tr><td> 
             
            NeutralAxisPercent </td> <td> 
             
            60 </td> </tr> 

            <tr><td> 
             
            NeutralMethod </td> <td> 
             
            BaseLine </td> </tr> 

            <tr><td> 
             
            NonlinearityCoefficient </td> <td> 
             
            0.3 </td> </tr> 

            <tr><td> 
             
            NumberOfCurves </td> <td> 
             
            2 </td> </tr> 

            <tr><td> 
             
            NumberOfRows </td> <td> 
             
            10 </td> </tr> 

            <tr><td> 
             
            OffsetBetweenDiagrams </td> <td> 
             
            500 </td> </tr> 

            <tr><td> 
             
            Overlap.Value </td> <td> 
             
            200 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            ReferencePlane </td> <td> 
             
            XCYCPlane </td> </tr> 

            <tr><td> 
             
            SideMargin.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            UpperMargin.Value </td> <td> 
             
            5 (millimeters part), 4 (inches part) </td> </tr> 

            <tr><td> 
             
            VarMarginIncrement.Value </td> <td> 
             
            20 (millimeters part), 0.75 (inches part) </td> </tr> 

            <tr><td> 
             
            VarMarginMax.Value </td> <td> 
             
            75 (millimeters part), 3 (inches part) </td> </tr> 

            <tr><td> 
             
            VarMarginMin.Value </td> <td> 
             
            15 (millimeters part), 0.75 (inches part) </td> </tr> 

            <tr><td> 
             
            VarOverlapMax </td> <td> 
             
            2 </td> </tr> 

            <tr><td> 
             
            VarOverlapMin </td> <td> 
             
            1 </td> </tr> 

            </table>  

             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  InverseBendingLinesBuilder : public NXOpen::Features::FeatureBuilder
            {
                /** The method used to generate the bending curves. */
                public: enum MethodType
                {
                    MethodTypeAutomatic/** Automatic. */,
                    MethodTypeNumberOfCurves/** Number of curves. */,
                    MethodTypeFillingCoefficient/** Filling Coefficient (unsupported). */,
                    MethodTypeEvenFit/** Even Fit. */
                };

                /** The method used to calculate the neutral line. */
                public: enum NeutralMethodType
                {
                    NeutralMethodTypeBaseLine/** Base line. */,
                    NeutralMethodTypeCenterLine/** Center line. */,
                    NeutralMethodTypeNeutralAxis/** Neutral axis. */
                };

                /** The reference plane to draw the diagram on. */
                public: enum ReferencePlaneType
                {
                    ReferencePlaneTypeXCYCPlane/** XC-YC plane. */,
                    ReferencePlaneTypeYCZCPlane/** YC-ZC plane. */,
                    ReferencePlaneTypeZCXCPlane/** ZC-XC plane. */,
                    ReferencePlaneTypeNegativeXCYCPlane/** -XC-YC plane. */,
                    ReferencePlaneTypeNegativeYCZCPlane/** -YC-ZC plane. */,
                    ReferencePlaneTypeNegativeZCXCPlane/** -ZC-XC plane. */,
                    ReferencePlaneTypeDefineCSYS/** User defined plane. */
                };

                /** The direction to measure from. */
                public: enum MeasureType
                {
                    MeasureTypeLeftToRight/** Left to right. */,
                    MeasureTypeRightToLeft/** Right to left. */
                };

                private: InverseBendingLinesBuilderImpl * m_inversebendinglinesbuilder_impl;
                private: friend class  _InverseBendingLinesBuilderBuilder;
                protected: InverseBendingLinesBuilder();
                public: ~InverseBendingLinesBuilder();
                /**Returns  the profile bodies to create Inverse Bending Lines on.
                             <br> The list can be populated in any one of the following ways:
                            <ul>
                            <li>If the list of profile bodies is empty, the function will search the current workset for any bent profiles. For each
                                profile that does not have an Inverse Bending Lines feature, a new one is created. A profile that
                                already has an Inverse Bending Lines feature associated to it, is edited with the new parameters.</li>
                            <li>If the list contains one or more profiles and no feature is given, an Inverse Bending Lines features will
                                be created or edited for each profile in the list.</li>
                            <li>If a feature is supplied to be edited, the list must contain a single bent profile that resides in the
                                same design element as the feature.</li>
                            </ul>
                             <br> 
                         
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectBodyList * ProfileBodies
                (
                );
                /**Returns  the method used to calculate the number and spacing of the curves on the profile. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MethodType Method
                (
                );
                /**Sets  the method used to calculate the number and spacing of the curves on the profile. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void SetMethod
                (
                    NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MethodType method /** method */ 
                );
                /**Returns  the number of curves to generate on the profile. 
                            Only when method is @link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MethodTypeNumberOfCurves NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MethodTypeNumberOfCurves@endlink .  
                        
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: int NumberOfCurves
                (
                );
                /**Sets  the number of curves to generate on the profile. 
                            Only when method is @link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MethodTypeNumberOfCurves NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MethodTypeNumberOfCurves@endlink .  
                        
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void SetNumberOfCurves
                (
                    int numberOfCurves /** numberofcurves */ 
                );
                /**Returns  the maximum number of curves to generate on the profile. 
                            Only when method is @link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MethodTypeNumberOfCurves NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MethodTypeNumberOfCurves@endlink 
                            or @link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MethodTypeEvenFit NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MethodTypeEvenFit@endlink .  
                        
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: int MaxNumberOfCurves
                (
                );
                /**Sets  the maximum number of curves to generate on the profile. 
                            Only when method is @link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MethodTypeNumberOfCurves NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MethodTypeNumberOfCurves@endlink 
                            or @link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MethodTypeEvenFit NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MethodTypeEvenFit@endlink .  
                        
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void SetMaxNumberOfCurves
                (
                    int maxNumberOfCurves /** maxnumberofcurves */ 
                );
                /**Returns  the nonlinearity coefficient used to determine the bending curve spacing. 
                            Only when method is @link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MethodTypeNumberOfCurves NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MethodTypeNumberOfCurves@endlink .
                        
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: double NonlinearityCoefficient
                (
                );
                /**Sets  the nonlinearity coefficient used to determine the bending curve spacing. 
                            Only when method is @link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MethodTypeNumberOfCurves NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MethodTypeNumberOfCurves@endlink .
                        
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void SetNonlinearityCoefficient
                (
                    double nonlinearityCoefficient /** nonlinearitycoefficient */ 
                );
                /**Returns  the filling coefficient that represents the amplitude of the bending line relative to the profile height.
                            Only when method is @link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MethodTypeFillingCoefficient NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MethodTypeFillingCoefficient@endlink .
                        
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: double FillingCoefficient
                (
                );
                /**Sets  the filling coefficient that represents the amplitude of the bending line relative to the profile height.
                            Only when method is @link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MethodTypeFillingCoefficient NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MethodTypeFillingCoefficient@endlink .
                        
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void SetFillingCoefficient
                (
                    double fillingCoefficient /** fillingcoefficient */ 
                );
                /**Returns  the neutral method determines the curve that is used for measurements and calculations when un-bending the profile. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::NeutralMethodType NeutralMethod
                (
                );
                /**Sets  the neutral method determines the curve that is used for measurements and calculations when un-bending the profile. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void SetNeutralMethod
                (
                    NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::NeutralMethodType neutralMethod /** neutralmethod */ 
                );
                /**Returns  the height of a line through the profile that maintains a constant length when the profile is bent.
                            Measured as a percentage of the profile height relative to the base line.
                        
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: double NeutralAxisPercent
                (
                );
                /**Sets  the height of a line through the profile that maintains a constant length when the profile is bent.
                            Measured as a percentage of the profile height relative to the base line.
                        
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void SetNeutralAxisPercent
                (
                    double neutralAxisPercent /** neutralaxispercent */ 
                );
                /**Returns  the reference plane type determines how you will define the plane of the diagram and table 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneType ReferencePlane
                (
                );
                /**Sets  the reference plane type determines how you will define the plane of the diagram and table 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void SetReferencePlane
                (
                    NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneType referencePlane /** referenceplane */ 
                );
                /**Returns  the reference plane origin when one of the standard planes is chosen. 
                            Only when reference plane type is one of:
                            <ul>
                            <li>@link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeXCYCPlane NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeXCYCPlane@endlink </li>.
                            <li>@link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeYCZCPlane NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeYCZCPlane@endlink </li>.
                            <li>@link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeZCXCPlane NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeZCXCPlane@endlink </li>.
                            <li>@link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeNegativeXCYCPlane NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeNegativeXCYCPlane@endlink </li>.
                            <li>@link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeNegativeYCZCPlane NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeNegativeYCZCPlane@endlink </li>.
                            <li>@link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeNegativeZCXCPlane NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeNegativeZCXCPlane@endlink </li>.
                            </ul>
                        
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * ReferencePlanePoint
                (
                );
                /**Sets  the reference plane origin when one of the standard planes is chosen. 
                            Only when reference plane type is one of:
                            <ul>
                            <li>@link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeXCYCPlane NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeXCYCPlane@endlink </li>.
                            <li>@link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeYCZCPlane NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeYCZCPlane@endlink </li>.
                            <li>@link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeZCXCPlane NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeZCXCPlane@endlink </li>.
                            <li>@link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeNegativeXCYCPlane NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeNegativeXCYCPlane@endlink </li>.
                            <li>@link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeNegativeYCZCPlane NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeNegativeYCZCPlane@endlink </li>.
                            <li>@link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeNegativeZCXCPlane NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeNegativeZCXCPlane@endlink </li>.
                            </ul>
                        
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void SetReferencePlanePoint
                (
                    NXOpen::Point * referencePlanePoint /** referenceplanepoint */ 
                );
                /**Returns  the user defined CSYS used to locate and orient the tables and diagrams.
                            Only when reference plane type is @link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeDefineCSYS NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeDefineCSYS@endlink .
                        
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CoordinateSystem * UserCsys
                (
                );
                /**Sets  the user defined CSYS used to locate and orient the tables and diagrams.
                            Only when reference plane type is @link NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeDefineCSYS NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::ReferencePlaneTypeDefineCSYS@endlink .
                        
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void SetUserCsys
                (
                    NXOpen::CoordinateSystem * userCsys /** usercsys */ 
                );
                /**Returns  the measurement direction used in the table, left to right, or right to left. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MeasureType Measure
                (
                );
                /**Sets  the measurement direction used in the table, left to right, or right to left. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void SetMeasure
                (
                    NXOpen::Features::ShipDesign::InverseBendingLinesBuilder::MeasureType measure /** measure */ 
                );
                /**Returns  the number of rows in the table. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: int NumberOfRows
                (
                );
                /**Sets  the number of rows in the table. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void SetNumberOfRows
                (
                    int numberOfRows /** numberofrows */ 
                );
                /**Returns  the overlap distance of the bending curves. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Overlap
                (
                );
                /**Returns  the grid spacing in the diagram. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * GridSpacing
                (
                );
                /**Returns  the side margin on each end of the profile. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * SideMargin
                (
                );
                /**Returns  the lower margin on the profile. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * LowerMargin
                (
                );
                /**Returns  the upper margin on the profile. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * UpperMargin
                (
                );
                /**Returns  the extension added on each end of the profile. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Extension
                (
                );
                /**Returns  the variable aligned overlap minimum number of grids. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: int VarOverlapMin
                (
                );
                /**Sets  the variable aligned overlap minimum number of grids. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") */
                public: void SetVarOverlapMin
                (
                    int varOverlapMin /** varoverlapmin */ 
                );
                /**Returns  the variable aligned overlap maximum number of grids.  
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: int VarOverlapMax
                (
                );
                /**Sets  the variable aligned overlap maximum number of grids.  
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") */
                public: void SetVarOverlapMax
                (
                    int varOverlapMax /** varoverlapmax */ 
                );
                /**Returns  the maximum horizontal margin used for profiles. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * VarMarginMax
                (
                );
                /**Returns  the minimum horizontal margin used for profiles. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * VarMarginMin
                (
                );
                /**Returns  the Increment used to vary horizontal margins for profiles. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: NXOpen::Expression * VarMarginIncrement
                (
                );
                /**Returns  the distance between the bottom of one table and the top of the next diagram. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: double OffsetBetweenDiagrams
                (
                );
                /**Sets  the distance between the bottom of one table and the top of the next diagram. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void SetOffsetBetweenDiagrams
                (
                    double offsetBetweenDiagrams /** offsetbetweendiagrams */ 
                );
                /**Returns  the switch that determines if vent holes are drawn in the diagram. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: bool DrawVentHoles
                (
                );
                /**Sets  the switch that determines if vent holes are drawn in the diagram. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void SetDrawVentHoles
                (
                    bool drawVentHoles /** drawventholes */ 
                );
                /** The profiles that failed and error code for each failed profile.  @return  The profiles that failed. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: std::vector<NXOpen::Body *> GetFailedProfiles
                (
                    std::vector<int> & failedReasons /** The error code for each failure. */
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
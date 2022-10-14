#ifndef NXOpen_FEATURES_SHIPDESIGN_SUBSYSTEMBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_SUBSYSTEMBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_SubSystemBuilder.ja
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
#include <NXOpen/Features_ShipDesign_EndCutBuilder.hxx>
#include <NXOpen/Features_ShipDesign_PillarTreatmentBlockBuilder.hxx>
#include <NXOpen/Features_ShipDesign_PlateStockBuilder.hxx>
#include <NXOpen/Features_ShipDesign_SteelFeatureSpreadsheetBuilder.hxx>
#include <NXOpen/Features_ShipDesign_StiffenerStockBuilder.hxx>
#include <NXOpen/Features_ShipDesign_StiffenerSystemBuilder.hxx>
#include <NXOpen/Features_ShipDesign_FeatureParmsBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
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
            class SubSystemBuilder;
        }
    }
    class Direction;
    class Expression;
    namespace Features
    {
        namespace ShipDesign
        {
            class EndCutBuilder;
        }
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class FeatureParmsBuilder;
        }
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class PillarTreatmentBlockBuilder;
        }
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class PlateStockBuilder;
        }
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class SteelFeatureSpreadsheetBuilder;
        }
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class StiffenerStockBuilder;
        }
    }
    class SelectCurve;
    class SelectNXObjectList;
    namespace Features
    {
        namespace ShipDesign
        {
            class _SubSystemBuilderBuilder;
            class SubSystemBuilderImpl;
            /**
                This class is used to 
                edit the Sub System Definition of a @link NXOpen::Features::ShipDesign::SubSystems NXOpen::Features::ShipDesign::SubSystems@endlink  feature.
                 <br> No creator since only created along with Features.ShipDesign.SubSystemsBuilder  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            EndEndCut.ConnectionType </td> <td> 
             
            Connected </td> </tr> 

            <tr><td> 
             
            EndEndCut.DraftAngle.Value </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            EndEndCut.DraftOffset.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            EndEndCut.DraftType </td> <td> 
             
            Trim </td> </tr> 

            <tr><td> 
             
            EndEndCut.EndFaceType </td> <td> 
             
            NeatTrim </td> </tr> 

            <tr><td> 
             
            EndEndCut.LimitType </td> <td> 
             
            Value </td> </tr> 

            <tr><td> 
             
            EndEndCut.Offset.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            EndEndCut.SelectionType </td> <td> 
             
            FacesWithAttributes </td> </tr> 

            <tr><td> 
             
            EndEndCut.ShearAngle.Value </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            EndEndCut.TiltAngle.Value </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            EndPillarTreatment.CapPlateStock.KnuckleRatio </td> <td> 
             
            3.0 </td> </tr> 

            <tr><td> 
             
            EndPillarTreatment.CapPlateStock.KnuckleSmoothAngle </td> <td> 
             
            3.0 </td> </tr> 

            <tr><td> 
             
            EndPillarTreatment.CapPlateStock.MaterialOption </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            EndPillarTreatment.CapPlateStock.OppositeThickness.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            EndPillarTreatment.CapPlateStock.RestrictThicknessToMaterial </td> <td> 
             
            true </td> </tr> 

            <tr><td> 
             
            EndPillarTreatment.CapPlateStock.ThickenOption </td> <td> 
             
            SingleSided </td> </tr> 

            <tr><td> 
             
            EndPillarTreatment.CapPlateStock.Thickness.Value </td> <td> 
             
            10 (millimeters part), 0.5 (inches part) </td> </tr> 

            <tr><td> 
             
            EndPillarTreatment.CapPlateStock.ThicknessSourceOption </td> <td> 
             
            List </td> </tr> 

            <tr><td> 
             
            ProfileStockData.AnchorPoint </td> <td> 
             
            0 </td> </tr> 

            <tr><td> 
             
            ProfileStockData.PlateHeight.Value </td> <td> 
             
            50 (millimeters part), 2 (inches part) </td> </tr> 

            <tr><td> 
             
            ProfileStockData.SectionType </td> <td> 
             
            Profile </td> </tr> 

            </table>  

             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  SubSystemBuilder : public NXOpen::Features::ShipDesign::FeatureParmsBuilder
            {
                private: SubSystemBuilderImpl * m_subsystembuilder_impl;
                private: friend class  _SubSystemBuilderBuilder;
                protected: SubSystemBuilder();
                public: ~SubSystemBuilder();
                /**Returns  the faces or curves that make up the sub system. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectNXObjectList * SubSystem
                (
                );
                /**Returns  the profile sub system stock data. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::StiffenerStockBuilder * ProfileStockData
                (
                );
                /**Returns  the plate sub system stock data. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::PlateStockBuilder * PlateStockData
                (
                );
                /**Returns  the pillar sub system stock data. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::SteelFeatureSpreadsheetBuilder * PillarStockData
                (
                );
                /**Returns  the offset to apply to the plate sub system  mold face to produce the desired mold face. The offset is applied 
                            in the thickness direction specified. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * Offset
                (
                );
                /**Returns  the method used to define the reference for the orientation angle of stiffener system.
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OrientationMethods OrientationMethod
                (
                );
                /**Sets  the method used to define the reference for the orientation angle of stiffener system.
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") */
                public: void SetOrientationMethod
                (
                    NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OrientationMethods orientationMethod /** orientationmethod */ 
                );
                /**Returns  the vector specified for the orientation angle reference. 
                            Only used when when Method is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OrientationMethodsVector NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OrientationMethodsVector@endlink .. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Direction * OrientationVector
                (
                );
                /**Sets  the vector specified for the orientation angle reference. 
                            Only used when when Method is @link NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OrientationMethodsVector NXOpen::Features::ShipDesign::StiffenerSystemBuilder::OrientationMethodsVector@endlink .. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_concept ("Ship Concept") */
                public: void SetOrientationVector
                (
                    NXOpen::Direction * orientationVector /** orientationvector */ 
                );
                /**Returns  the angle at which the stiffener system is placed relative to the reference.
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * OrientationAngle
                (
                );
                /**Returns  the end cut to use at the start of the stiffener sub system. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::StiffenerSystemBuilder::EndCutTypes EndCutStart
                (
                );
                /**Sets  the end cut to use at the start of the stiffener sub system. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetEndCutStart
                (
                    NXOpen::Features::ShipDesign::StiffenerSystemBuilder::EndCutTypes endCutStart /** endcutstart */ 
                );
                /**Returns  the tightness to apply to plate and subplate systems. 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : None */
                public: int Tightness
                (
                );
                /**Sets  the tightness to apply to plate and subplate systems. 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetTightness
                (
                    int tightness /** tightness */ 
                );
                /**Returns  the end cut to use at the end of the stiffener sub system. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::StiffenerSystemBuilder::EndCutTypes EndCutEnd
                (
                );
                /**Sets  the end cut to use at the end of the stiffener sub system. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetEndCutEnd
                (
                    NXOpen::Features::ShipDesign::StiffenerSystemBuilder::EndCutTypes endCutEnd /** endcutend */ 
                );
                /**Returns  the indication whether the direction of the flange should be reversed on this stiffener sub system. The default
                            direction is based on the ship structure that the stiffener is being built upon. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: bool Reverse
                (
                );
                /**Sets  the indication whether the direction of the flange should be reversed on this stiffener sub system. The default
                            direction is based on the ship structure that the stiffener is being built upon. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetReverse
                (
                    bool reverse /** reverse */ 
                );
                /**Returns  the line specified for the pillar system angle reference. 
                 <br>  Created in NX8.5.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectCurve * OrientationLinePillar
                (
                );
                /**Returns 
                            the name of the Subsystem and the name of the part created for the SubSystem by Transition
                        
                 <br>  Created in NX9.0.2.  <br>  
                 <br> License requirements : None */
                public: NXString Name
                (
                );
                /**Sets 
                            the name of the Subsystem and the name of the part created for the SubSystem by Transition
                        
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void SetName
                (
                    const NXString & name /** name */ 
                );
                /**Sets 
                            the name of the Subsystem and the name of the part created for the SubSystem by Transition
                        
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                void SetName
                (
                    const char * name /** name */ 
                );
                /**Returns  the mounting method 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::StiffenerSystemBuilder::MountingMethods MountingMethod
                (
                );
                /**Sets  the mounting method 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetMountingMethod
                (
                    NXOpen::Features::ShipDesign::StiffenerSystemBuilder::MountingMethods mountingMethod /** mountingmethod */ 
                );
                /**Returns  the detailed start end cut builder. 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::EndCutBuilder * StartEndCut
                (
                );
                /**Returns  the detailed end end cut builder. 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::EndCutBuilder * EndEndCut
                (
                );
                /**Returns  the detailed start pillar treatment builder. 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::PillarTreatmentBlockBuilder * StartPillarTreatment
                (
                );
                /**Returns  the detailed end pillar treatment builder. 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::PillarTreatmentBlockBuilder * EndPillarTreatment
                (
                );
                /**Returns  the indication whether the start end cut has been changed by user. 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : None */
                public: bool StartEndCutChanged
                (
                );
                /**Sets  the indication whether the start end cut has been changed by user. 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetStartEndCutChanged
                (
                    bool changed /** changed */ 
                );
                /**Returns  the indication whether the end end cut has been changed by user. 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : None */
                public: bool EndEndCutChanged
                (
                );
                /**Sets  the indication whether the end end cut has been changed by user. 
                 <br>  Created in NX12.0.2.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetEndEndCutChanged
                (
                    bool changed /** changed */ 
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
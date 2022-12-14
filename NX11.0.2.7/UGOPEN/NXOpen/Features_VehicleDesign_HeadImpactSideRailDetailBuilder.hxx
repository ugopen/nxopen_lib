#ifndef NXOpen_FEATURES_VEHICLEDESIGN_HEADIMPACTSIDERAILDETAILBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_VEHICLEDESIGN_HEADIMPACTSIDERAILDETAILBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_VehicleDesign_HeadImpactSideRailDetailBuilder.ja
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
#include <NXOpen/Features_VehicleDesign_HeadImpactSideRailDetailBuilder.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        namespace VehicleDesign
        {
            class HeadImpactSideRailDetailBuilder;
        }
    }
    class Expression;
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class Point;
    namespace Features
    {
        namespace VehicleDesign
        {
            class _HeadImpactSideRailDetailBuilderBuilder;
            class HeadImpactSideRailDetailBuilderImpl;
            /** Represents a @link NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder@endlink .  <br> This is an abstract class and cannot be instantiated.  <br> 
             <br>  Created in NX9.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  HeadImpactSideRailDetailBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
            {
                private: HeadImpactSideRailDetailBuilderImpl * m_headimpactsideraildetailbuilder_impl;
                private: friend class  _HeadImpactSideRailDetailBuilderBuilder;
                protected: HeadImpactSideRailDetailBuilder();
                public: ~HeadImpactSideRailDetailBuilder();
                /**Returns  the offset used to position SR1. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * SR1Offset
                (
                );
                /**Returns  the offset used to position SR2. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * SR2Offset
                (
                );
                /**Returns  the vertical minimum required approach angle. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * ReqVerticalMin
                (
                );
                /**Returns  the vertical maximum required approach angle. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * ReqVerticalMax
                (
                );
                /**Returns  the left horizontal required approach angle. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * ReqHorizontalLeftExact
                (
                );
                /**Returns  the right horizontal required approach angle. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Expression * ReqHorizontalRightExact
                (
                );
                /**Returns  the left SR1 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool SR1LeftFlag
                (
                );
                /**Sets  the left SR1 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetSR1LeftFlag
                (
                    bool sr1LeftFlag /** sr1leftflag */ 
                );
                /**Returns  the left SR1 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * SR1Left
                (
                );
                /**Sets  the left SR1 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetSR1Left
                (
                    NXOpen::Point * sr1Left /** sr1left */ 
                );
                /**Returns  the right SR1 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool SR1RightFlag
                (
                );
                /**Sets  the right SR1 alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetSR1RightFlag
                (
                    bool sr1RightFlag /** sr1rightflag */ 
                );
                /**Returns  the right SR1 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * SR1Right
                (
                );
                /**Sets  the right SR1 alternative point. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetSR1Right
                (
                    NXOpen::Point * sr1Right /** sr1right */ 
                );
                /**Returns  the left SR2 alternative point flag. 
                 <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SR2ALeftFlag NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SR2ALeftFlag@endlink  instead. <br>  

                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public:  NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SR2ALeftFlag instead.") bool SR2LeftFlag
                (
                );
                /**Sets  the left SR2 alternative point flag. 
                 <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SetSR2ALeftFlag NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SetSR2ALeftFlag@endlink  instead. <br>  

                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public:  NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SetSR2ALeftFlag instead.") void SetSR2LeftFlag
                (
                    bool sr2LeftFlag /** sr2leftflag */ 
                );
                /**Returns  the left SR2 alternative point. 
                 <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SR2ALeft NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SR2ALeft@endlink  instead. <br>  

                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public:  NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SR2ALeft instead.") NXOpen::Point * SR2Left
                (
                );
                /**Sets  the left SR2 alternative point. 
                 <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SetSR2ALeft NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SetSR2ALeft@endlink  instead. <br>  

                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public:  NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SetSR2ALeft instead.") void SetSR2Left
                (
                    NXOpen::Point * sr2Left /** sr2left */ 
                );
                /**Returns  the right SR2 alternative point flag. 
                 <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SR2ARightFlag NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SR2ARightFlag@endlink  instead. <br>  

                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public:  NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SR2ARightFlag instead.") bool SR2RightFlag
                (
                );
                /**Sets  the right SR2 alternative point flag. 
                 <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SetSR2ARightFlag NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SetSR2ARightFlag@endlink  instead. <br>  

                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public:  NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SetSR2ARightFlag instead.") void SetSR2RightFlag
                (
                    bool sr2RightFlag /** sr2rightflag */ 
                );
                /**Returns  the right SR2 alternative point. 
                 <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SR2ARight NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SR2ARight@endlink  instead. <br>  

                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public:  NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SR2ARight instead.") NXOpen::Point * SR2Right
                (
                );
                /**Sets  the right SR2 alternative point. 
                 <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SetSR2ARight NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SetSR2ARight@endlink  instead. <br>  

                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public:  NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::Features::VehicleDesign::HeadImpactSideRailDetailBuilder::SetSR2ARight instead.") void SetSR2Right
                (
                    NXOpen::Point * sr2Right /** sr2right */ 
                );
                /**Returns  the left SR2A alternative point flag. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: bool SR2ALeftFlag
                (
                );
                /**Sets  the left SR2A alternative point flag. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetSR2ALeftFlag
                (
                    bool sr2aLeftFlag /** sr2aleftflag */ 
                );
                /**Returns  the left SR2A alternative point. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * SR2ALeft
                (
                );
                /**Sets  the left SR2A alternative point. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetSR2ALeft
                (
                    NXOpen::Point * sr2aLeft /** sr2aleft */ 
                );
                /**Returns  the right SR2A alternative point flag. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: bool SR2ARightFlag
                (
                );
                /**Sets  the right SR2A alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetSR2ARightFlag
                (
                    bool sr2aRightFlag /** sr2arightflag */ 
                );
                /**Returns  the right SR2A alternative point. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * SR2ARight
                (
                );
                /**Sets  the right SR2A alternative point. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetSR2ARight
                (
                    NXOpen::Point * sr2aRight /** sr2aright */ 
                );
                /**Returns  the left SR2B alternative point flag. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: bool SR2BLeftFlag
                (
                );
                /**Sets  the left SR2B alternative point flag. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetSR2BLeftFlag
                (
                    bool sr2bLeftFlag /** sr2bleftflag */ 
                );
                /**Returns  the left SR2B alternative point. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * SR2BLeft
                (
                );
                /**Sets  the left SR2B alternative point. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetSR2BLeft
                (
                    NXOpen::Point * sr2bLeft /** sr2bleft */ 
                );
                /**Returns  the right SR2B alternative point flag. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: bool SR2BRightFlag
                (
                );
                /**Sets  the right SR2B alternative point flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetSR2BRightFlag
                (
                    bool sr2bRightFlag /** sr2brightflag */ 
                );
                /**Returns  the right SR2B alternative point. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * SR2BRight
                (
                );
                /**Sets  the right SR2B alternative point. 
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetSR2BRight
                (
                    NXOpen::Point * sr2bRight /** sr2bright */ 
                );
                /**Returns  the left PT11 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool PT11LeftFlag
                (
                );
                /**Sets  the left PT11 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPT11LeftFlag
                (
                    bool pt11LeftFlag /** pt11leftflag */ 
                );
                /**Returns  the left PT11 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * PT11Left
                (
                );
                /**Sets  the left PT11 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPT11Left
                (
                    NXOpen::Point * pt11Left /** pt11left */ 
                );
                /**Returns  the right PT11 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool PT11RightFlag
                (
                );
                /**Sets  the right PT11 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPT11RightFlag
                (
                    bool pt11RightFlag /** pt11rightflag */ 
                );
                /**Returns  the right PT11 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * PT11Right
                (
                );
                /**Sets  the right PT11 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPT11Right
                (
                    NXOpen::Point * pt11Right /** pt11right */ 
                );
                /**Returns  the left PT12 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool PT12LeftFlag
                (
                );
                /**Sets  the left PT12 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPT12LeftFlag
                (
                    bool pt12LeftFlag /** pt12leftflag */ 
                );
                /**Returns  the left PT12 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * PT12Left
                (
                );
                /**Sets  the left PT12 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPT12Left
                (
                    NXOpen::Point * pt12Left /** pt12left */ 
                );
                /**Returns  the right PT12 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool PT12RightFlag
                (
                );
                /**Sets  the right PT12 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPT12RightFlag
                (
                    bool pt12RightFlag /** pt12rightflag */ 
                );
                /**Returns  the right PT12 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * PT12Right
                (
                );
                /**Sets  the right PT12 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPT12Right
                (
                    NXOpen::Point * pt12Right /** pt12right */ 
                );
                /**Returns  the left PT14 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool PT14LeftFlag
                (
                );
                /**Sets  the left PT14 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPT14LeftFlag
                (
                    bool pt14LeftFlag /** pt14leftflag */ 
                );
                /**Returns  the left PT14 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * PT14Left
                (
                );
                /**Sets  the left PT14 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPT14Left
                (
                    NXOpen::Point * pt14Left /** pt14left */ 
                );
                /**Returns  the right PT14 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool PT14RightFlag
                (
                );
                /**Sets  the right PT14 additional geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPT14RightFlag
                (
                    bool pt14RightFlag /** pt14rightflag */ 
                );
                /**Returns  the right PT14 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point * PT14Right
                (
                );
                /**Sets  the right PT14 additional geometry. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetPT14Right
                (
                    NXOpen::Point * pt14Right /** pt14right */ 
                );
                /**Returns  the create construction geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : None */
                public: bool CreateGeometry
                (
                );
                /**Sets  the create construction geometry flag. 
                 <br>  Created in NX9.0.0.  <br>  
                 <br> License requirements : nx_general_packaging ("NX General Packaging") */
                public: void SetCreateGeometry
                (
                    bool createGeometry /** creategeometry */ 
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

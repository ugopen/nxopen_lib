#ifndef NXOpen_WELD_WELDADVISORBUILDER_HXX_INCLUDED
#define NXOpen_WELD_WELDADVISORBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_WeldAdvisorBuilder.ja
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
#include <NXOpen/WeldAssistant.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Weld
    {
        class WeldAdvisorBuilder;
    }
    class Builder;
    class TaggedObject;
    namespace Weld
    {
         /** Represents entity and its log message */

        struct  LogInfo
        {
            public: /**weld object*/NXOpen::TaggedObject * Entity;
            public: /** log message*/NXString LogMessage;
            public: LogInfo() :
                Entity(),
                LogMessage()
            {
            }
            /** Constructor for the LogInfo struct. */ 
            public: LogInfo(NXOpen::TaggedObject * entityInitial /**weld object*/, 
                    const NXString &logMessageInitial /** log message*/) :
                Entity(entityInitial),
                LogMessage(logMessageInitial)
            {
            }
        };

    }
    namespace Weld
    {
        class _WeldAdvisorBuilderBuilder;
        class WeldAdvisorBuilderImpl;
        /** Represents a weld advisor test  <br> To create a new instance of this class, use @link Weld::WeldManager::CreateWeldAdvisorBuilder Weld::WeldManager::CreateWeldAdvisorBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  WeldAdvisorBuilder : public Builder
        {
            private: WeldAdvisorBuilderImpl * m_weldadvisorbuilder_impl;
            private: friend class  _WeldAdvisorBuilderBuilder;
            protected: WeldAdvisorBuilder();
            public: ~WeldAdvisorBuilder();
            /** Sets the objects to be checked  <br> License requirements : ugweld ("UG WELD") */
            public: void SetObjects
            (
                const std::vector<NXOpen::TaggedObject *> & objects /** Objects to be checked*/
            );
            /** Gets the objects to be checked  <br> License requirements : ugweld ("UG WELD") */
            public: void GetObjects
            (
                std::vector<NXOpen::TaggedObject *> & objects /** Objects to be checked*/
            );
            /** Sets the checkers be executed   <br> License requirements : ugweld ("UG WELD") */
            public: void SetCheckers
            (
                const std::vector<NXOpen::Weld::WeldAdvisorCheckerType> & checkers /** Checkers to be executed*/
            );
            /** Gets the checkers be executed   <br> License requirements : ugweld ("UG WELD") */
            public: void GetCheckers
            (
                std::vector<NXOpen::Weld::WeldAdvisorCheckerType> & checkers /** Checkers to be executed*/
            );
            /** The report results to xml file   <br> License requirements : ugweld ("UG WELD") */
            public: void ReportResult
            (
                const NXString & filePath /** the file to save result   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** The save all to part   <br> License requirements : ugweld ("UG WELD") */
            public: void SaveResult
            (
            );
            /** The failed results  <br> License requirements : ugweld ("UG WELD") */
            public: void GetFailedObjects
            (
                NXOpen::Weld::WeldAdvisorCheckerType checker /** checker type*/,
                std::vector<NXString> & weldId /** weld id*/,
                std::vector<NXOpen::Weld::LogInfo> & weldObjects /** failed objects*/
            );
            /** The objects that failed weld objects referenced  <br> License requirements : ugweld ("UG WELD") */
            public: void GetReferenceObjects
            (
                NXOpen::TaggedObject * weldObject /** the weld object*/,
                NXOpen::Weld::WeldAdvisorCheckerType checker /** checker type*/,
                std::vector<NXOpen::Weld::LogInfo> & weldObjects /**reference objects*/
            );
            /** The weld advisor parameter Minimum Edge Distance  <br> License requirements : ugweld ("UG WELD") */
            public: void SetMinimumEdgeDistance
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */,
                double minEdgeDist /** The weld advisor parameter Minimum Edge Distance */
            );
            /** The weld advisor parameter Minimum Edge Distance  @return  The weld advisor parameter Minimum Edge Distance  <br> License requirements : ugweld ("UG WELD") */
            public: double GetMinimumEdgeDistance
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */
            );
            /** The weld advisor parameter Minimum Edge Distance With Sealer  <br> License requirements : ugweld ("UG WELD") */
            public: void SetMinimumEdgeDistanceWithSealer
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */,
                double minEdgeDistWithSealer /** The weld advisor parameter Minimum Edge Distance With Sealer */
            );
            /** The weld advisor parameter Minimum Edge Distance With Sealer  @return  The weld advisor parameter Minimum Edge Distance With Sealer  <br> License requirements : ugweld ("UG WELD") */
            public: double GetMinimumEdgeDistanceWithSealer
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */
            );
            /** The weld advisor parameter Minimum Spacing  <br> License requirements : ugweld ("UG WELD") */
            public: void SetMinimumPointDistance
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */,
                double minPointDist /** The weld advisor parameter Minimum Spacing */
            );
            /** The weld advisor parameter Minimum Spacing  @return  The weld advisor parameter Minimum Spacing  <br> License requirements : ugweld ("UG WELD") */
            public: double GetMinimumPointDistance
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */
            );
            /** The weld advisor parameter Maximum Stack Up Gap  <br> License requirements : ugweld ("UG WELD") */
            public: void SetMaximumStackUpGap
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */,
                double maxFaceDist /** The weld advisor parameter Maximum Stack Up Gap */
            );
            /** The weld advisor parameter Maximum Stack Up Gap  @return  The weld advisor parameter Maximum Stack Up Gap  <br> License requirements : ugweld ("UG WELD") */
            public: double GetMaximumStackUpGap
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */
            );
            /** The weld advisor parameter Maximum Point Face Distance  <br> License requirements : ugweld ("UG WELD") */
            public: void SetMaximumPointFaceDistance
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */,
                double pointFaceDist /** The weld advisor parameter Maximum Point Face Distance */
            );
            /** The weld advisor parameter Maximum Point Face Distance  @return  The weld advisor parameter Maximum Point Face Distance  <br> License requirements : ugweld ("UG WELD") */
            public: double GetMaximumPointFaceDistance
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */
            );
            /** The weld advisor parameter Maximum CSYS Face Normal Angle  <br> License requirements : ugweld ("UG WELD") */
            public: void SetMaximumCsysFaceNormalAngle
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */,
                double csysFaceNmlAngle /** The weld advisor parameter Maximum CSYS Face Normal Angle */
            );
            /** The weld advisor parameter Maximum CSYS Face Normal Angle  @return  The weld advisor parameter Maximum CSYS Face Normal Angle  <br> License requirements : ugweld ("UG WELD") */
            public: double GetMaximumCsysFaceNormalAngle
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */
            );
            /** The weld advisor parameter Check Zone Radius  <br> License requirements : ugweld ("UG WELD") */
            public: void SetCheckZoneRadius
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */,
                double faceRadius /** The weld advisor parameter Check Zone Radius */
            );
            /** The weld advisor parameter Check Zone Radius  @return  The weld advisor parameter Check Zone Radius  <br> License requirements : ugweld ("UG WELD") */
            public: double GetCheckZoneRadius
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */
            );
            /** The weld advisor parameter Sealer Check Zone Radius  <br> License requirements : ugweld ("UG WELD") */
            public: void SetSealerCheckZoneRadius
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */,
                double faceRadiusWithSealer /** The weld advisor parameter Sealer Check Zone Radius */
            );
            /** The weld advisor parameter Sealer Check Zone Radius  @return  The weld advisor parameter Sealer Check Zone Radius  <br> License requirements : ugweld ("UG WELD") */
            public: double GetSealerCheckZoneRadius
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */
            );
            /** The weld advisor parameter Planarity Tolerance  <br> License requirements : ugweld ("UG WELD") */
            public: void SetPlanarityTolerance
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */,
                double facePlanarityTolerance /** The weld advisor parameter Planarity Tolerance */
            );
            /** The weld advisor parameter Planarity Tolerance  @return  The weld advisor parameter Planarity Tolerance  <br> License requirements : ugweld ("UG WELD") */
            public: double GetPlanarityTolerance
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */
            );
            /** The weld advisor parameter Parallelism Tolerance  <br> License requirements : ugweld ("UG WELD") */
            public: void SetParallelismTolerance
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */,
                double faceParallelismTolerance /** The weld advisor parameter Parallelism Tolerance */
            );
            /** The weld advisor parameter Parallelism Tolerance  @return  The weld advisor parameter Parallelism Tolerance  <br> License requirements : ugweld ("UG WELD") */
            public: double GetParallelismTolerance
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */
            );
            /** The weld advisor parameter Flange Check Radius  <br> License requirements : ugweld ("UG WELD") */
            public: void SetFlangeCheckRadius
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */,
                double flangeRadius /** The weld advisor parameter Flange Check Radius */
            );
            /** The weld advisor parameter Flange Check Radius  @return  The weld advisor parameter Flange Check Radius  <br> License requirements : ugweld ("UG WELD") */
            public: double GetFlangeCheckRadius
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */
            );
            /** The weld advisor parameter Flange Check Height  <br> License requirements : ugweld ("UG WELD") */
            public: void SetFlangeCheckHeight
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */,
                double flangeHeight /** The weld advisor parameter Flange Check Height */
            );
            /** The weld advisor parameter Flange Check Height  @return  The weld advisor parameter Flange Check Height  <br> License requirements : ugweld ("UG WELD") */
            public: double GetFlangeCheckHeight
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */
            );
            /** The weld advisor parameter Minimum Closed Angle  <br> License requirements : ugweld ("UG WELD") */
            public: void SetMinimumClosedAngle
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */,
                double minClosedAngle /** The weld advisor parameter Minimum Closed Angle */
            );
            /** The weld advisor parameter Minimum Closed Angle  @return  The weld advisor parameter Minimum Closed Angle  <br> License requirements : ugweld ("UG WELD") */
            public: double GetMinimumClosedAngle
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */
            );
            /** The weld advisor parameter Maximum Total Metal Thickness  <br> License requirements : ugweld ("UG WELD") */
            public: void SetMaximumTotalMetalThickness
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */,
                double totalMetalThickness /** The weld advisor parameter Maximum Total Metal Thickness */
            );
            /** The weld advisor parameter Maximum Total Metal Thickness  @return  The weld advisor parameter Maximum Total Metal Thickness  <br> License requirements : ugweld ("UG WELD") */
            public: double GetMaximumTotalMetalThickness
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */
            );
            /** The weld advisor parameter Thickness Ratio  <br> License requirements : ugweld ("UG WELD") */
            public: void SetThicknessRatio
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */,
                double thicknessRatio /** The weld advisor parameter Thickness Ratio */
            );
            /** The weld advisor parameter Thickness Ratio  @return  The weld advisor parameter Thickness Ratio  <br> License requirements : ugweld ("UG WELD") */
            public: double GetThicknessRatio
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */
            );
            /** The weld advisor parameter Thickness Outer Ratio  <br> License requirements : ugweld ("UG WELD") */
            public: void SetThicknessOuterRatio
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */,
                double thicknessOuterRatio /** The weld advisor parameter Thickness Outer Ratio */
            );
            /** The weld advisor parameter Thickness Outer Ratio  @return  The weld advisor parameter Thickness Outer Ratio  <br> License requirements : ugweld ("UG WELD") */
            public: double GetThicknessOuterRatio
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */
            );
            /** The weld advisor parameter Maximum Number of Loose Panels  <br> License requirements : ugweld ("UG WELD") */
            public: void SetMaximumNumberLoosePanels
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */,
                int maxNumOfLoosePanels /** The weld advisor parameter Maximum Number of Loose Panels */
            );
            /** The weld advisor parameter Maximum Number of Loose Panels  @return  The weld advisor parameter Maximum Number of Loose Panels  <br> License requirements : ugweld ("UG WELD") */
            public: int GetMaximumNumberLoosePanels
            (
                NXOpen::Weld::WeldAdvisorCustomerDefault type /** weld type */
            );
            /** The initialization for settings  <br> License requirements : ugweld ("UG WELD") */
            public: void InitializeSettings
            (
            );
            /** The sealer included or not  <br> License requirements : ugweld ("UG WELD") */
            public: void SetIncludeSealer
            (
                bool includeSealer /** include sealer or not*/
            );
            /** The sealer included or not  @return  include sealer  <br> License requirements : ugweld ("UG WELD") */
            public: bool GetIncludeSealer
            (
            );
            /** Delete the features from the check result  <br> License requirements : ugweld ("UG WELD") */
            public: void DeleteFeaturesFromResult
            (
                const std::vector<NXOpen::TaggedObject *> & objects /** features to be deleted*/
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif

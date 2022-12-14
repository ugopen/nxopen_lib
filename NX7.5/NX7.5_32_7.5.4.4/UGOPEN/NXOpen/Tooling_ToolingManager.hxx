#ifndef NXOpen_TOOLING_TOOLINGMANAGER_HXX_INCLUDED
#define NXOpen_TOOLING_TOOLINGMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_ToolingManager.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/Tooling_ReusableObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Tooling
    {
        class ToolingManager;
    }
    class Part;
    namespace Tooling
    {
        class AddReusableFeatureCollection;
    }
    namespace Tooling
    {
        class AssignPatchCollection;
    }
    namespace Tooling
    {
        class BlankGeneratorCollection;
    }
    namespace Tooling
    {
        class BlankLayoutCollection;
    }
    namespace Tooling
    {
        class BomCollection;
    }
    namespace Tooling
    {
        class CalculateAreaCollection;
    }
    namespace Tooling
    {
        class ChannelAdjustCollection;
    }
    namespace Tooling
    {
        class ChannelFittingCollection;
    }
    namespace Tooling
    {
        class ConceptPositionCollection;
    }
    namespace Tooling
    {
        class CoolingConnectCollection;
    }
    namespace Tooling
    {
        class CoolingDefineChannelCollection;
    }
    namespace Tooling
    {
        class CoolingExtendCollection;
    }
    namespace Tooling
    {
        class CoolingPatternCollection;
    }
    namespace Tooling
    {
        class DesignTrimToolCollection;
    }
    namespace Tooling
    {
        class DieDesignSettingCollection;
    }
    namespace Tooling
    {
        class DirectUnfoldCollection;
    }
    namespace Tooling
    {
        class EWMultiPositionCollection;
    }
    namespace Tooling
    {
        class EdgePatchCollection;
    }
    namespace Tooling
    {
        class EjectorPostProcessingCollection;
    }
    namespace Tooling
    {
        class ElectrodeCopyCollection;
    }
    namespace Tooling
    {
        class EnlargeSurfaceCollection;
    }
    namespace Tooling
    {
        class FaceSplitCollection;
    }
    namespace Tooling
    {
        class FamilyMoldCollection;
    }
    namespace Tooling
    {
        class FastenerAssemConfigCollection;
    }
    namespace Tooling
    {
        class FastenerAssyCollection;
    }
    namespace Tooling
    {
        class ForceCalculationCollection;
    }
    namespace Tooling
    {
        class FormingInsertCollection;
    }
    namespace Tooling
    {
        class HoleReportCollection;
    }
    namespace Tooling
    {
        class InitProjCollection;
    }
    namespace Tooling
    {
        class InitProjectCollection;
    }
    namespace Tooling
    {
        class InsertAuxiliaryCollection;
    }
    namespace Tooling
    {
        class MWCopySheetsCollection;
    }
    namespace Tooling
    {
        class MWDefineRegionsCollection;
    }
    namespace Tooling
    {
        class MWDefineSheetsCollection;
    }
    namespace Tooling
    {
        class MWDesignGuideLinesCollection;
    }
    namespace Tooling
    {
        class MWDesignPartingSurfaceCollection;
    }
    namespace Tooling
    {
        class MWLayoutCollection;
    }
    namespace Tooling
    {
        class MWPartingManagerCollection;
    }
    namespace Tooling
    {
        class MWSearchRegionCollection;
    }
    namespace Tooling
    {
        class MWTraversePartingLinesCollection;
    }
    namespace Tooling
    {
        class MoldCsysCollection;
    }
    namespace Tooling
    {
        class MoldInsertCollection;
    }
    namespace Tooling
    {
        class MoldProcessCollection;
    }
    namespace Tooling
    {
        class MotionSimulationCollection;
    }
    namespace Tooling
    {
        class PiercingInsertCollection;
    }
    namespace Tooling
    {
        class PocketCollection;
    }
    namespace Tooling
    {
        class ProfileSplitCollection;
    }
    namespace Tooling
    {
        class ReferenceBlendCollection;
    }
    namespace Tooling
    {
        class ReliefDesignCollection;
    }
    namespace Tooling
    {
        class ReusableObject;
    }
    namespace Tooling
    {
        class ReusablePocketCollection;
    }
    namespace Tooling
    {
        class RunnerCollection;
    }
    namespace Tooling
    {
        class SIZERCollection;
    }
    namespace Tooling
    {
        class ScrapDesignCollection;
    }
    namespace Tooling
    {
        class SolidPatchCollection;
    }
    namespace Tooling
    {
        class SplitSolidCollection;
    }
    namespace Tooling
    {
        class StockSizeCollection;
    }
    namespace Tooling
    {
        class StripLayoutCollection;
    }
    namespace Tooling
    {
        class SubInsertCollection;
    }
    namespace Tooling
    {
        class TraverseLoopCollection;
    }
    namespace Tooling
    {
        class TrimMoldComponentsCollection;
    }
    namespace Tooling
    {
        class TrimRegionCollection;
    }
    namespace Tooling
    {
        class UndersizeCollection;
    }
    namespace Tooling
    {
        class ValidCheckCollection;
    }
    namespace Tooling
    {
        class WireHoleCollection;
    }
    namespace Tooling
    {
        class WorkpieceCollection;
    }
    namespace Tooling
    {
        /** Wizard type, some of them should be same as in mpdwshare_uf_mold.h */
        enum ToolingApplication
        {
            ToolingApplicationReuseLibrary/** Reuse Library */,
            ToolingApplicationMoldWizard/** MoldWizard    */,
            ToolingApplicationPdieWizard/** Progressive Die Wizard */,
            ToolingApplicationStampingDie/** Stamping Die */,
            ToolingApplicationElectrodeWizard/** Electrode Wizard */
        };

    }
    namespace Tooling
    {
        class ToolingManagerImpl;
        /** Contains the collection objects for creating and iterating over Reuse Library objects.  <br> To obtain an instance of this class, refer to @link Part Part@endlink  <br> */
        class NXOPENCPPEXPORT  ToolingManager
        {
            private: ToolingManagerImpl * m_toolingmanager_impl;
            private: NXOpen::Part* m_owner;
            /** Constructor */
            public: explicit ToolingManager(NXOpen::Part *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~ToolingManager();
            /** Creates a @link  Tooling::ReusableObject   Tooling::ReusableObject @endlink   @return @link  Tooling::ReusableObject   Tooling::ReusableObject @endlink   <br> License requirements : None */
            public: NXOpen::Tooling::ReusableObject * CreateReusableObject
            (
            );


            /** Returns the MWSearchRegionCollection instance belonging to this part */
            public: NXOpen::Tooling::MWSearchRegionCollection *MWSearchRegions();
            /** Returns the MWDefineRegionsCollection instance belonging to this part */
            public: NXOpen::Tooling::MWDefineRegionsCollection *MWDefineRegions();
            /** Returns the MWDefineSheetsCollection instance belonging to this part */
            public: NXOpen::Tooling::MWDefineSheetsCollection *MWDefineSheets();
            /** Returns the MWCopySheetsCollection instance belonging to this part */
            public: NXOpen::Tooling::MWCopySheetsCollection *MWCopySheets();
            /** Returns the MWPartingManagerCollection instance belonging to this part */
            public: NXOpen::Tooling::MWPartingManagerCollection *MWPartingManager();
            /** Returns the MWDesignPartingSurfaceCollection instance belonging to this part */
            public: NXOpen::Tooling::MWDesignPartingSurfaceCollection *MWDesignPartingSurface();
            /** Returns the MWTraversePartingLinesCollection instance belonging to this part */
            public: NXOpen::Tooling::MWTraversePartingLinesCollection *MWTraversePartingLines();
            /** Returns the MWDesignGuideLinesCollection instance belonging to this part */
            public: NXOpen::Tooling::MWDesignGuideLinesCollection *MWDesignGuideLines();
            /** Returns the ValidCheckCollection instance belonging to this part */
            public: NXOpen::Tooling::ValidCheckCollection *ValidCheck();
            /** Returns the DirectUnfold instance belonging to this part */
            public: NXOpen::Tooling::DirectUnfoldCollection *DirectUnfold();
            /** Returns the BomCollection instance belonging to this part */
            public: NXOpen::Tooling::BomCollection *Boms();
            /** Returns the StockSizeCollection instance belonging to this part */
            public: NXOpen::Tooling::StockSizeCollection *StockSizes();
            /** Returns the MoldCsysCollection instance belonging to this part */
            public: NXOpen::Tooling::MoldCsysCollection *MoldCsys();
            /** Returns the FamilyMoldCollection instance belonging to this part */
            public: NXOpen::Tooling::FamilyMoldCollection *FamilyMolds();
            /** Returns the PocketCollection instance belonging to this part */
            public: NXOpen::Tooling::PocketCollection *Pockets();
            /** Returns the ProfileSplitCollection instance belonging to this part */
            public: NXOpen::Tooling::ProfileSplitCollection *ProfileSplits();
            /** Returns the InitProjectCollection instance belonging to this part */
            public: NXOpen::Tooling::InitProjectCollection *InitializeProjects();
            /** Returns the PiercingInsert instance belonging to this part */
            public: NXOpen::Tooling::PiercingInsertCollection *PiercingInsert();
            /** Returns the StripLayout instance belonging to this part */
            public: NXOpen::Tooling::StripLayoutCollection *StripLayout();
            /** Returns the MWLayoutCollection instance belonging to this part */
            public: NXOpen::Tooling::MWLayoutCollection *Layouts();
            /** Returns the SubInsertCollection instance belonging to this part */
            public: NXOpen::Tooling::SubInsertCollection *SubInserts();
            /** Returns the ScrapDesignCollection instance belonging to this part */
            public: NXOpen::Tooling::ScrapDesignCollection *ScrapDesign();
            /** Returns the UndersizeCollection instance belonging to this part */
            public: NXOpen::Tooling::UndersizeCollection *Undersizes();
            /** Returns the WorkpieceCollection instance belonging to this part */
            public: NXOpen::Tooling::WorkpieceCollection *Workpieces();
            /** Returns the ElectrodeCopyCollection instance belonging to this part */
            public: NXOpen::Tooling::ElectrodeCopyCollection *ElectrodeCopys();
            /** Returns the InitProjCollection instance belonging to this part */
            public: NXOpen::Tooling::InitProjCollection *InitProj();
            /** Returns the ConceptPositionCollection instance belonging to this part */
            public: NXOpen::Tooling::ConceptPositionCollection *ConceptPositions();
            /** Returns the WireHole instance belonging to this part */
            public: NXOpen::Tooling::WireHoleCollection *WireHole();
            /** Returns the HoleReport instance belonging to this part */
            public: NXOpen::Tooling::HoleReportCollection *HoleReport();
            /** Returns the ReliefDesign instance belonging to this part */
            public: NXOpen::Tooling::ReliefDesignCollection *ReliefDesign();
            /** Returns the ForceCalculation instance belonging to this part */
            public: NXOpen::Tooling::ForceCalculationCollection *ForceCalculation();
            /** Returns the MoldInsertCollection instance belonging to this part */
            public: NXOpen::Tooling::MoldInsertCollection *MoldInserts();
            /** Returns the MoldProcessCollection instance belonging to this part */
            public: NXOpen::Tooling::MoldProcessCollection *MoldProcesses();
            /** Returns the FastenerAssyCollection instance belonging to this part */
            public: NXOpen::Tooling::FastenerAssyCollection *FastenerAssembly();
            /** Returns the FastenerAssemConfigCollection instance belonging to this part */
            public: NXOpen::Tooling::FastenerAssemConfigCollection *FastenerAssemConfig();
            /** Returns the AddReusableFeatureCollection instance belonging to this part */
            public: NXOpen::Tooling::AddReusableFeatureCollection *AddReusableFeature();
            /** Returns the ReferenceBlendCollection instance belonging to this part */
            public: NXOpen::Tooling::ReferenceBlendCollection *ReferenceBlends();
            /** Returns the CalculateAreaCollection instance belonging to this part */
            public: NXOpen::Tooling::CalculateAreaCollection *CalculateAreas();
            /** Returns the FaceSplitCollection instance belonging to this part */
            public: NXOpen::Tooling::FaceSplitCollection *FaceSplits();
            /** Returns the TraverseLoopCollection instance belonging to this part */
            public: NXOpen::Tooling::TraverseLoopCollection *TraverseLoops();
            /** Returns the EnlargeSurfaceCollection instance belonging to this part */
            public: NXOpen::Tooling::EnlargeSurfaceCollection *EnlargeSurfaces();
            /** Returns the SolidPatchCollection instance belonging to this part */
            public: NXOpen::Tooling::SolidPatchCollection *SolidPatchs();
            /** Returns the SplitSolidCollection instance belonging to this part */
            public: NXOpen::Tooling::SplitSolidCollection *SplitSolids();
            /** Returns the EdgePatchCollection instance belonging to this part */
            public: NXOpen::Tooling::EdgePatchCollection *EdgePatchs();
            /** Returns the AssignPatchCollection instance belonging to this part */
            public: NXOpen::Tooling::AssignPatchCollection *AssignPatchs();
            /** Returns the TrimRegionCollection instance belonging to this part */
            public: NXOpen::Tooling::TrimRegionCollection *TrimRegions();
            /** Returns the CoolingPatternCollection instance belonging to this part */
            public: NXOpen::Tooling::CoolingPatternCollection *CoolingPattern();
            /** Returns the CoolingDefineChannelCollection instance belonging to this part */
            public: NXOpen::Tooling::CoolingDefineChannelCollection *CoolingDefineChannel();
            /** Returns the ChannelAdjustCollection instance belonging to this part*/
            public: NXOpen::Tooling::ChannelAdjustCollection *ChannelAdjust();
            /** Returns the CoolingConnectCollection instance belonging to this part */
            public: NXOpen::Tooling::CoolingConnectCollection *CoolingConnect();
            /** Returns the BlankGeneratorCollection instance belonging to this part*/
            public: NXOpen::Tooling::BlankGeneratorCollection *BlankGenerator();
            /** Returns the BlankLayoutCollection instance belonging to this part */
            public: NXOpen::Tooling::BlankLayoutCollection *BlankLayout();
            /** Returns the DieDesignSettingCollection instance belonging to this part */
            public: NXOpen::Tooling::DieDesignSettingCollection *DieDesignSetting();
            /** Returns the EWMultiPositionCollection instance belonging to this part */
            public: NXOpen::Tooling::EWMultiPositionCollection *EWMultiPositions();
            /** Returns the FormingInsertCollection instance belonging to this part */
            public: NXOpen::Tooling::FormingInsertCollection *FormingInsert();
            /** Returns the InsertAuxiliaryCollection instance belonging to this part */
            public: NXOpen::Tooling::InsertAuxiliaryCollection *InsertAuxiliary();
            /** Returns the EjectorPostProcessingCollection instance belonging to this part */
            public: NXOpen::Tooling::EjectorPostProcessingCollection *EjectorPostProcessings();
            /** Returns the TrimMoldComponentsCollection instance belonging to this part */
            public: NXOpen::Tooling::TrimMoldComponentsCollection *TrimMoldComponents();
            /** Returns the DesignTrimToolCollection instance belonging to this part */
            public: NXOpen::Tooling::DesignTrimToolCollection *DesignTrimTools();
            /** Returns the CoolingExtendCollection instance belonging to this part */
            public: NXOpen::Tooling::CoolingExtendCollection *CoolingExtend();
            /** Returns the SIZERCollection instance belonging to this part */
            public: NXOpen::Tooling::SIZERCollection *SIZER();
            /** Returns the RunnerCollection instance belonging to this part */
            public: NXOpen::Tooling::RunnerCollection *Runner();
            /** Returns the MotionSimulationCollection instance belonging to this part */
            public: NXOpen::Tooling::MotionSimulationCollection *MotionSimulation();
            /** Returns the ReusablePocketCollection instance belonging to this part */
            public: NXOpen::Tooling::ReusablePocketCollection *ReusablePocket();
            /** Returns the ChannelFittingCollection instance belonging to this part */
            public: NXOpen::Tooling::ChannelFittingCollection *ChannelFitting();
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif

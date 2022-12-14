#ifndef NXOpen_FEATURES_SHEETMETAL_SHEETMETALMANAGER_HXX_INCLUDED
#define NXOpen_FEATURES_SHEETMETAL_SHEETMETALMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_SheetMetal_SheetmetalManager.ja
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
#include <NXOpen/Annotations_SheetMetalPMIBuilder.hxx>
#include <NXOpen/Features_SheetMetal_BendListBuilder.hxx>
#include <NXOpen/Features_SheetMetal_BendListItemBuilder.hxx>
#include <NXOpen/Features_SheetMetal_ExportFlatPatternBuilder.hxx>
#include <NXOpen/Features_SheetMetal_NestingBuilder.hxx>
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
        namespace SheetMetal
        {
            class SheetmetalManager;
        }
    }
    namespace Features
    {
        class FeatureCollection;
    }
    namespace Annotations
    {
        class SheetMetalPMIBuilder;
    }
    namespace Annotations
    {
        class SimpleDraftingAid;
    }
    class Body;
    class Edge;
    class Face;
    namespace Features
    {
        class Feature;
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class AdvancedFlangeBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class AssociateObjectBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class BeadBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class BendBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class BendListBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class BendListItemBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class BendTaperBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class BreakCornerBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class BridgeTransitionBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class CleanUpUtilityBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class ClosedCornerBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class ContourFlangeBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class ConvertToSheetmetalBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class DimpleBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class DrawnCutoutBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class EdgeRipBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class EditBendBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class EditCornerBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class ExportFlatPatternBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class FlangeBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class FlatPatternBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class FlatSolidBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class FlexibleCableBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class GussetBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class HemFlangeBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class JogBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class JoggleBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class LighteningCutout;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class LighteningCutoutBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class LoftedFlangeBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class LouverBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class MetaformBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class MigratedPanelBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class MultiFlange;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class MultiFlangeBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class NestingBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class NormalCutoutBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class RebendBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class ResizeBendAngleBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class ResizeBendRadiusBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class ResizeNeutralFactorBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class SheetMetalFromSolidBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class SolidPunchBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class TabBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class ThreeBendCornerBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class UnbendBuilder;
        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            /** Face Type */
            enum SheetmetalFaceType
            {
                SheetmetalFaceTypeUnknown/** unknown */ ,
                SheetmetalFaceTypeWeb/** web */ ,
                SheetmetalFaceTypeBend/** bend */ ,
                SheetmetalFaceTypeDeform/** deform */ ,
                SheetmetalFaceTypeThickness/** thickness */ 
            };

            /** Face Layer */
            enum SheetmetalFaceLayer
            {
                SheetmetalFaceLayerUnknown/** unknown */ ,
                SheetmetalFaceLayerTop/** top */ ,
                SheetmetalFaceLayerBottom/** bottom */ 
            };

            /** Bend State */
            enum SheetmetalBendState
            {
                SheetmetalBendStateUnknown/** unknown */ ,
                SheetmetalBendStateBent/** bent */ ,
                SheetmetalBendStateFlat/** flat */ 
            };

             /** This structure contains the bend parameters for a Sheet Metal bend area. */

            struct SheetmetalBendParameters
            {
                public: /**Inner Bend Radius. This works only for cylidrical bend faces. Other faces return 0.0 */double InnerRadius;
                public: /**Neutral factor value. If the flange is controlled by bend tables, then this is table value converted to neutral factor.*/double NeutralFactor;
                public: /**Bend Angle*/double BendAngle;
                public: /**Bend Face is flat or bent*/NXOpen::Features::SheetMetal::SheetmetalBendState BendState;
                public: SheetmetalBendParameters() :
                    InnerRadius(),
                    NeutralFactor(),
                    BendAngle(),
                    BendState((NXOpen::Features::SheetMetal::SheetmetalBendState)0)
                {
                }
                /** Constructor for the SheetmetalBendParameters struct. */ 
                public: SheetmetalBendParameters(double innerRadiusInitial /**Inner Bend Radius. This works only for cylidrical bend faces. Other faces return 0.0 */, 
                        double neutralFactorInitial /**Neutral factor value. If the flange is controlled by bend tables, then this is table value converted to neutral factor.*/, 
                        double bendAngleInitial /**Bend Angle*/, 
                        NXOpen::Features::SheetMetal::SheetmetalBendState bendStateInitial /**Bend Face is flat or bent*/) :
                    InnerRadius(innerRadiusInitial),
                    NeutralFactor(neutralFactorInitial),
                    BendAngle(bendAngleInitial),
                    BendState(bendStateInitial)
                {
                }
            };

        }
    }
    namespace Features
    {
        namespace SheetMetal
        {
            class SheetmetalManagerImpl;
            /** Represents an object that manages sheetmetal features  <br> To obtain an instance of this class, refer to @link NXOpen::Features::FeatureCollection  NXOpen::Features::FeatureCollection @endlink  <br> 
             <br>  Created in NX4.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  SheetmetalManager
            {
                private: SheetmetalManagerImpl * m_sheetmetalmanager_impl;
                private: NXOpen::Features::FeatureCollection* m_owner;
                /// \cond NX_NO_DOC 
                public: explicit SheetmetalManager(NXOpen::Features::FeatureCollection *owner);


                /// \endcond 
                public: 
                /**Returns the tag of this object.  */
                tag_t Tag() const; 
                public: ~SheetmetalManager();
                /** Create a NXSM Dimple feature Builder @return  DimpleBuilder object 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::DimpleBuilder * CreateDimpleFeatureBuilder
                (
                    NXOpen::Features::Feature * dimple /** The Dimple for which builder needs to be constructed. NULL for creating a new dimple */
                );
                /** Create a NXSM Drawn Cutout feature Builder @return  DrawnCutoutBuilder object 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::DrawnCutoutBuilder * CreateDrawnCutoutFeatureBuilder
                (
                    NXOpen::Features::Feature * dCutout /** The Drawn Cutout for which builder needs to be constructed. NULL for creating a new Drawn Cutout */
                );
                /** Creates a @link Features::SheetMetal::LighteningCutoutBuilder Features::SheetMetal::LighteningCutoutBuilder@endlink   @return  
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN") */
                public: NXOpen::Features::SheetMetal::LighteningCutoutBuilder * CreateLighteningCutoutBuilder
                (
                    NXOpen::Features::SheetMetal::LighteningCutout * lighteningCutout /** @link Features::SheetMetal::LighteningCutout Features::SheetMetal::LighteningCutout@endlink  to be edited */
                );
                /** Create a NXSM Louver feature Builder @return  LouverBuilder object 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::LouverBuilder * CreateLouverFeatureBuilder
                (
                    NXOpen::Features::Feature * louver /** The Louver for which builder needs to be constructed. NULL for creating a new Louver */
                );
                /** Create a NXSM Bead feature Builder @return  BeadBuilder object 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::BeadBuilder * CreateBeadFeatureBuilder
                (
                    NXOpen::Features::Feature * bead /** The Bead for which builder needs to be constructed. NULL for creating a new Bead */
                );
                /** Create a NXSM Flange feature Builder @return  FlangeBuilder object 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::FlangeBuilder * CreateFlangeFeatureBuilder
                (
                    NXOpen::Features::Feature * dCutout /** The Flange for which builder needs to be constructed. NULL for creating a new Flange */
                );
                /** Create a NXSM Break Corner feature Builder @return  BrcornerBuilder object 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::BreakCornerBuilder * CreateBreakCornerFeatureBuilder
                (
                    NXOpen::Features::Feature * brcorner /** The Break Corner for which builder needs to be constructed. NULL for creating a new Break Corner */
                );
                /** Create a NXSM Edge Rip feature Builder @return  Edge Rip Builder object 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::EdgeRipBuilder * CreateEdgeRipFeatureBuilder
                (
                    NXOpen::Features::Feature * edgeRip /** The Edge Rip for which builder needs to be constructed. NULL for creating a new Edge Rip */
                );
                /** Create a NXSM Convert To Sheetmetal feature Builder @return  Convert To Sheetmetal Builder object 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::ConvertToSheetmetalBuilder * CreateConvertToSheetmetalFeatureBuilder
                (
                    NXOpen::Features::Feature * convertToSheetMetal /** The Convert To Sheetmetal feature for which builder needs to be constructed. NULL for converting a part for the first time*/
                );
                /** Create a NXSM Normal Cutout feature Builder @return  NormalCutoutBuilder object 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::NormalCutoutBuilder * CreateNormalCutoutFeatureBuilder
                (
                    NXOpen::Features::Feature * ncutout /** The Normal Cutout for which builder needs to be constructed. NULL for creating a new Normal Cutout */
                );
                /** Create a NXSM Tab feature Builder @return  TabBuilder object 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::TabBuilder * CreateTabFeatureBuilder
                (
                    NXOpen::Features::Feature * tab /** The Tab for which builder needs to be constructed. NULL for creating a new Tab */
                );
                /** Create a NXSM Lofted Flange feature Builder @return  LoftedFlangeBuilder object 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::LoftedFlangeBuilder * CreateLoftedFlangeFeatureBuilder
                (
                    NXOpen::Features::Feature * lflange /** The Lofted Flange for which builder needs to be constructed. NULL for creating a new LoftedFlange */
                );
                /** Create a NXSM Three Bend Corner feature Builder @return  ThreeBendCornerBuilder object 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::ThreeBendCornerBuilder * CreateThreeBendCornerFeatureBuilder
                (
                    NXOpen::Features::Feature * threeBendCorner /** The Three Bend Corner for which builder needs to be constructed. NULL for creating a new Three Bend Corner */
                );
                /** Create a NXSM Contour Flange feature Builder @return  ContourFlangeBuilder object 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::ContourFlangeBuilder * CreateContourFlangeFeatureBuilder
                (
                    NXOpen::Features::Feature * contourFlange /**The Contour Flange for which builder needs to be constructed. NULL for creating a new Contour Flange */
                );
                /** Create a NXSM Flat Solid feature Builder @return  Flat Solid object 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::FlatSolidBuilder * CreateFlatSolidFeatureBuilder
                (
                    NXOpen::Features::Feature * flatSolid /**The Contour Flange for which builder needs to be constructed. NULL for creating a new Flat Solid */
                );
                /** Create a NXSM Flat Pattern feature Builder @return  Flat Pattern object 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::FlatPatternBuilder * CreateFlatPatternBuilder
                (
                    NXOpen::Features::Feature * flatPattern /**The Flat Pattern for which builder needs to be constructed. NULL for creating a new Flat Pattern */
                );
                /** Create a NXSM Bend taper feature Builder @return  Bend Taper object 
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::BendTaperBuilder * CreateBendTaperBuilder
                (
                    NXOpen::Features::Feature * bendTaper /**The Bend Taper for which builder needs to be constructed. NULL for creating a new Bend Taper */
                );
                /** Create a NXSM Bend feature Builder @return  Bend object 
                 <br>  Created in NX4.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::BendBuilder * CreateBendFeatureBuilder
                (
                    NXOpen::Features::Feature * bend /**The Bend for which builder needs to be constructed. NULL for creating a new Bend */
                );
                /** Create a NXSM Closed Corner feature Builder @return  Closed Corner object 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::ClosedCornerBuilder * CreateClosedCornerFeatureBuilder
                (
                    NXOpen::Features::Feature * closedCorner /**The Closed Corner for which builder needs to be constructed. NULL for creating a new Closed Corner */
                );
                /** Create a NXSM Jog feature Builder @return  JogBuilder object 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::JogBuilder * CreateJogFeatureBuilder
                (
                    NXOpen::Features::Feature * jog /** The Jog for which builder needs to be constructed. NULL for creating a new Jog */
                );
                /** Create a NXSM Unbend feature builder @return  Unbend object
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::UnbendBuilder * CreateUnbendFeatureBuilder
                (
                    NXOpen::Features::Feature * unbend /**The Unbend for which builder needs to be constructed. NULL for creating a new Unbend */
                );
                /** Create a NXSM Rebend feature builder @return  Rebend object
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::RebendBuilder * CreateRebendFeatureBuilder
                (
                    NXOpen::Features::Feature * rebend /**The Rebend for which builder needs to be constructed. NULL for creating a new Rebend */
                );
                /** Create a NXSM Migrated Panel feature Builder @return  Migrated Panel Builder object 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::MigratedPanelBuilder * CreateMigratedPanelFeatureBuilder
                (
                    NXOpen::Features::Feature * migratedPanel /** The Migrated Panel feature for which builder needs to be constructed. NULL for converting a part for the first time*/
                );
                /** Create a Resize Bend Radius Builder @return  ResizeBendRadius Builder object
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::ResizeBendRadiusBuilder * CreateResizeBendRadiusFeatureBuilder
                (
                    NXOpen::Features::Feature * resizeBendRadius /** The ResizeBendRadius feature for which builder needs to be constructed. NULL for creating a new ResizeBendRadius */
                );
                /** Creates Resize Bend Angle Builder  @return Resize Bend Angle Builder object
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::ResizeBendAngleBuilder * CreateResizeBendAngleBuilder
                (
                    NXOpen::Features::Feature * resizeBendAngle /**The Resize Bend Angle feature for which builder needs to be constructed. NULL for creating a new Resize Bend Angle*/
                );
                /** Create hem flange feature builder  @return  Hem Flange Builder object
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::HemFlangeBuilder * CreateHemFlangeFeatureBuilder
                (
                    NXOpen::Features::Feature * hemFalnge /** The Hem Flange feature for which builder needs to be constructed. NULL for creating a new Hem Flange */
                );
                /** Creates Resize Neutral Factor Builder  @return  
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::ResizeNeutralFactorBuilder * CreateResizeNeutralFactorBuilder
                (
                    NXOpen::Features::Feature * resizeNeutralFactor /** The Resize Neutral Factor feature for which builder needs to be constructed. NULL for creating a new Resize Neutral Factor feature */
                );
                /** Creates a @link NXOpen::Features::SheetMetal::SolidPunchBuilder NXOpen::Features::SheetMetal::SolidPunchBuilder@endlink   @return  
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::SolidPunchBuilder * CreateSolidPunchBuilder
                (
                    NXOpen::Features::Feature * solidPunch /** @link NXOpen::Features::Feature NXOpen::Features::Feature@endlink  to be edited */
                );
                /** Creates a @link NXOpen::Features::SheetMetal::BridgeTransitionBuilder NXOpen::Features::SheetMetal::BridgeTransitionBuilder@endlink   @return Bridge Transition Builder
                 <br>  Created in NX5.0.2.  <br>  
                 <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") OR nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::BridgeTransitionBuilder * CreateBridgeTransitionBuilder
                (
                    NXOpen::Features::Feature * transition /**The Bridge Transition feature for which builder needs to be constructed. NULL for creating a new Bridge Transition*/
                );
                /** Is a sheet metal body. This function will return True if the body has at least one NX Sheet Metal feature or
                                a Flexible Printed Circuit Design feature.  @return True = Body has NX Sheet Metal features or Flexible Printed Circuit Design features
                 <br>  Created in NX5.0.2.  <br>  
                 <br> License requirements : None */
                public: bool IsSheetmetalBody
                (
                    NXOpen::Body * inputBody /**The body to check*/
                );
                /** Thickness of sheet metal body. Value is returned in part units.  @return Thickness Value
                 <br>  Created in NX5.0.2.  <br>  
                 <br> License requirements : None */
                public: double GetBodyThickness
                (
                    NXOpen::Body * sheetmetalBody /**The face to check*/
                );
                /** Get inner bend faces. For every bend the inner face is the face with smaller radius.
                 <br>  Created in NX5.0.2.  <br>  
                 <br> License requirements : None */
                public: void GetInnerBendFaces
                (
                    NXOpen::Body * sheetmetalBody /**The body to check*/,
                    std::vector<NXOpen::Face *> & innerBendFaces /**Inner bend faces*/,
                    std::vector<NXOpen::Features::SheetMetal::SheetmetalBendState> & bendStates /**Bend Face is flat or bent*/
                );
                /** Sheet metal face type  @return Sheet Metal Face Type
                 <br>  Created in NX5.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::SheetMetal::SheetmetalFaceType GetFaceType
                (
                    NXOpen::Face * inputFace /**The face to check*/
                );
                /** Sheet metal face layer  @return Sheet Metal Face Layer
                 <br>  Created in NX5.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::SheetMetal::SheetmetalFaceLayer GetFaceLayer
                (
                    NXOpen::Face * inputFace /**The face to check*/
                );
                /** Opposite face to bend, web or deform face. Will raise an exception if the input face is not a valid face. @return Opposite Layer Face
                 <br>  Created in NX5.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Face * GetOppositeFace
                (
                    NXOpen::Face * inputFace /**The face to check*/
                );
                /** Bend region parameters. The values are calculated from the inner face of bend region. The radius and angle values are returned in part units. This function will raise an exception of the face is not a valid bend face.
                 <br>  Created in NX5.0.2.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::SheetMetal::SheetmetalBendParameters GetBendParameters
                (
                    NXOpen::Face * bendFace /**The face to query. This can be outer or inner bend face*/
                );
                /** Check if this edge is a thickness edge  @return True = Thickness Edge
                 <br>  Created in NX5.0.2.  <br>  
                 <br> License requirements : None */
                public: bool IsThicknessEdge
                (
                    NXOpen::Edge * inputEdge /**The edge to check*/
                );
                /** Creates a @link NXOpen::Features::SheetMetal::SheetMetalFromSolidBuilder NXOpen::Features::SheetMetal::SheetMetalFromSolidBuilder@endlink   @return  Sheet Metal from Solid Builder object
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::SheetMetalFromSolidBuilder * CreateSheetMetalFromSolidBuilder
                (
                    NXOpen::Features::Feature * sheetMetalFromSolid /** @link NXOpen::Features::SheetMetalFromSolid NXOpen::Features::SheetMetalFromSolid@endlink  to be edited */
                );
                /** Creates a @link NXOpen::Features::SheetMetal::FlexibleCableBuilder NXOpen::Features::SheetMetal::FlexibleCableBuilder@endlink   @return Flexible Cable Builder object
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Features::SheetMetal::FlexibleCableBuilder * CreateFlexibleCableBuilder
                (
                    NXOpen::Features::Feature * flexibleCable /**The Flexible Cable feature for which builder needs to be constructed. NULL for creating a new Flexible Cable. */
                );
                /** Creates a @link NXOpen::Features::SheetMetal::GussetBuilder NXOpen::Features::SheetMetal::GussetBuilder@endlink   @return  Gusset Builder object
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::GussetBuilder * CreateGussetBuilder
                (
                    NXOpen::Features::Feature * gusset /** @link NXOpen::Features::Gusset NXOpen::Features::Gusset@endlink  to be edited */
                );
                /** Creates a @link NXOpen::Features::SheetMetal::EditBendBuilder NXOpen::Features::SheetMetal::EditBendBuilder@endlink   @return  
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::EditBendBuilder * CreateEditBendBuilder
                (
                    NXOpen::Features::Feature * editBend /** @link NXOpen::Features::EditBend NXOpen::Features::EditBend@endlink  to be edited */
                );
                /** Creates a @link NXOpen::Features::SheetMetal::CleanUpUtilityBuilder NXOpen::Features::SheetMetal::CleanUpUtilityBuilder@endlink   @return  Clean-Up Utility Builder object
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::CleanUpUtilityBuilder * CreateCleanUpUtilityBuilder
                (
                );
                /** Creates a @link NXOpen::Features::SheetMetal::MetaformBuilder NXOpen::Features::SheetMetal::MetaformBuilder@endlink   @return  
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN") */
                public: NXOpen::Features::SheetMetal::MetaformBuilder * CreateMetaformBuilder
                (
                    NXOpen::Features::Feature * metaform /** @link NXOpen::Features::Metaform NXOpen::Features::Metaform@endlink  to be edited */
                );
                /** Creates a @link NXOpen::Features::SheetMetal::EditCornerBuilder NXOpen::Features::SheetMetal::EditCornerBuilder@endlink   @return  
                 <br>  Created in NX7.5.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Features::SheetMetal::EditCornerBuilder * CreateEditCornerBuilder
                (
                );
                /** Creates a @link NXOpen::Features::SheetMetal::ExportFlatPatternBuilder NXOpen::Features::SheetMetal::ExportFlatPatternBuilder@endlink  
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Features::SheetMetal::ExportFlatPatternBuilder * CreateExportFlatPatternBuilder
                (
                );
                /** Creates a @link NXOpen::Features::SheetMetal::JoggleBuilder NXOpen::Features::SheetMetal::JoggleBuilder@endlink  
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN") */
                public: NXOpen::Features::SheetMetal::JoggleBuilder * CreateJoggleBuilder
                (
                    NXOpen::Features::Feature * joggle /** joggle */ 
                );
                /** Creates a @link NXOpen::Features::SheetMetal::AdvancedFlangeBuilder NXOpen::Features::SheetMetal::AdvancedFlangeBuilder@endlink  
                 <br>  Created in NX11.0.0.  <br>  
                 <br> License requirements : adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN") */
                public: NXOpen::Features::SheetMetal::AdvancedFlangeBuilder * CreateAdvancedFlangeBuilder
                (
                    NXOpen::Features::Feature * joggle /** joggle */ 
                );
                /** Creates a @link NXOpen::Features::SheetMetal::BendListBuilder NXOpen::Features::SheetMetal::BendListBuilder@endlink  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Features::SheetMetal::BendListBuilder * CreateBendListBuilder
                (
                );
                /** Creates a @link NXOpen::Features::SheetMetal::BendListItemBuilder NXOpen::Features::SheetMetal::BendListItemBuilder@endlink  
                            BendListItemBuilder objects will be created and populated in the BendListBuilder when bend information of a flat pattern view is populated.
                            User should never need to create or delete BendListItemBuilder object on its own.
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Features::SheetMetal::BendListItemBuilder * CreateBendListItemBuilder
                (
                );
                /** Creates a @link Features::SheetMetal::MultiFlangeBuilder Features::SheetMetal::MultiFlangeBuilder@endlink   @return  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") OR nx_flexible_pcb ("NX Flexible PCB") OR nx_ship_detail ("Ship Detail Design") */
                public: NXOpen::Features::SheetMetal::MultiFlangeBuilder * CreateMultiFlangeBuilder
                (
                    NXOpen::Features::SheetMetal::MultiFlange * multiFlange /** @link Features::SheetMetal::MultiFlange Features::SheetMetal::MultiFlange@endlink  to be edited */
                );
                /** Creates a @link Features::SheetMetal::AssociateObjectBuilder Features::SheetMetal::AssociateObjectBuilder@endlink   @return  
                 <br>  Created in NX1872.0.0.  <br>  
                 <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
                public: NXOpen::Features::SheetMetal::AssociateObjectBuilder * CreateAssociateObjectBuilder
                (
                    NXOpen::Features::Feature * associateObject /** @link Features::SheetMetal::AssociateObject Features::SheetMetal::AssociateObject@endlink  to be edited */
                );

                /// \cond NX_NO_DOC 
                /** Creates a @link NXOpen::Features::SheetMetal::NestingBuilder NXOpen::Features::SheetMetal::NestingBuilder@endlink  
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : nx_2d_nesting (" NX 2D Nesting") */
                public: NXOpen::Features::SheetMetal::NestingBuilder * CreateNestingBuilder
                (
                );

                /// \endcond 
                /** Creates a @link Annotations::SheetMetalPMIBuilder Annotations::SheetMetalPMIBuilder@endlink  
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : nx_sheet_metal ("NX Sheet Metal") */
                public: NXOpen::Annotations::SheetMetalPMIBuilder * CreateSheetMetalPmiBuilder
                (
                    NXOpen::Annotations::SimpleDraftingAid * annotation /** annotation */ 
                );
            }; //lint !e1712 default constructor not defined for class  

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

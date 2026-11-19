from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
##  Represents the selection filter members for NXOpen development 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## NotSet</term><description> 
##  No filter. Should not be used. </description> </item><item><term> 
## Group</term><description> 
##  Group </description> </item><item><term> 
## Pattern</term><description> 
##  Pattern </description> </item><item><term> 
## PatternPoint</term><description> 
##  Pattern Point </description> </item><item><term> 
## ProductDefinition</term><description> 
##  Product Definition </description> </item><item><term> 
## ViewSet</term><description> 
##  View Set </description> </item><item><term> 
## Field</term><description> 
##  Field tables, formulas, etc. </description> </item><item><term> 
## AllAnalyses</term><description> 
##  All Analyses </description> </item><item><term> 
## DeviationGauge</term><description> 
##  Deviation Gauge </description> </item><item><term> 
## GridSectionAnalysis</term><description> 
##  Grid Section Analysis </description> </item><item><term> 
## HighlightLinesAnalysis</term><description> 
##  Highlight Lines Analysis </description> </item><item><term> 
## SurfaceContinuityAnalysis</term><description> 
##  Surface Continuity Analysis </description> </item><item><term> 
## GapAndFlushnessAnalysis</term><description> 
##  Gap and Flushness Analysis </description> </item><item><term> 
## CurveContinuityAnalysis</term><description> 
##  Curve Continuity Analysis </description> </item><item><term> 
## SectionAnalysis</term><description> 
##  Section Analysis </description> </item><item><term> 
## CurveAnalysis</term><description> 
##  Curve Analysis </description> </item><item><term> 
## SurfaceIntersectionAnalysis</term><description> 
##  Surface Intersection Analysis </description> </item><item><term> 
## DraftAnalysis</term><description> 
##  Draft Analysis </description> </item><item><term> 
## TrimAngleCheck</term><description> 
##  Trim Angle Check </description> </item><item><term> 
## LocalRadiusAnalysis</term><description> 
##  Local Radius Analysis </description> </item><item><term> 
## MoldFlowMoldx3dAnalysis</term><description> 
##  Mold Flow moldx3d Analysis </description> </item><item><term> 
## WallThicknessAnalysis</term><description> 
##  Wall Thickness Analysis </description> </item><item><term> 
## FaceCurvatureAnalysis</term><description> 
##  Face Curvature </description> </item><item><term> 
## FaceAnalysis</term><description> 
##  Face Analysis </description> </item><item><term> 
## SheetBoundaryAnalysis</term><description> 
##  Sheet Boundary Analysis </description> </item><item><term> 
## DistanceAnalysis</term><description> 
##  Distance Analysis </description> </item><item><term> 
## RadiusAnalysis</term><description> 
##  Radius Analysis </description> </item><item><term> 
## ReflectionAnalysis</term><description> 
##  Reflection Analysis </description> </item><item><term> 
## SlopeAnalysis</term><description> 
##  Slope Analysis </description> </item><item><term> 
## AnimationDesignerAll</term><description> 
##  All objects in Animation Designer </description> </item><item><term> 
## AnimationDesignerRigidGroup</term><description> 
##  The rigid group of objects or components for an animation </description> </item><item><term> 
## AnimationDesignerContact</term><description> 
##  The contact on objects to prevent interference between them during the animation </description> </item><item><term> 
## AnimationDesignerJoint</term><description> 
##  The joint relationship between rigid groups </description> </item><item><term> 
## AnimationDesignerMotor</term><description> 
##  The driver on joint </description> </item><item><term> 
## AnimationDesignerCoupler</term><description> 
##  The coupler relationship between joints </description> </item><item><term> 
## AnimationDesignerMonitor</term><description> 
##  The monitor of motor parameters, distance or angle between geometries during the animation </description> </item><item><term> 
## AnimationDesignerAnimatedEffects</term><description> 
##  The animated effects such as visibility, explode, camera, color during the animation </description> </item><item><term> 
## AnimationDesignerJointJogger</term><description> 
##  The jog of joints during the animation </description> </item><item><term> 
## AnimationDesignerContainer</term><description> 
##  The container of objects in navigator </description> </item><item><term> 
## AnimationDesignerFlexibleObject</term><description> 
##  The flexible objects for an animation </description> </item><item><term> 
## Component</term><description> 
##  Component </description> </item><item><term> 
## ComponentPattern</term><description> 
##  Component Pattern </description> </item><item><term> 
## AssemblyConstraint</term><description> 
##  Assembly Constraint </description> </item><item><term> 
## AssemblyConstraintGroup</term><description> 
##  Assembly Constraint Group </description> </item><item><term> 
## AutomationDesignerTerminalNode</term><description> 
##  Terminal node in Product Aspect Navigator </description> </item><item><term> 
## AutomationDesignerEPLANMacro</term><description> 
##  EPLAN Macro </description> </item><item><term> 
## AutomationDesignerAspect</term><description> 
##  Aspect node </description> </item><item><term> 
## AutomationDesignerProgramBlock</term><description> 
##  Software Element </description> </item><item><term> 
## AutomationDesignerPageObject</term><description> 
##  Page node Object </description> </item><item><term> 
## AutomationDesignerEngineeringObject</term><description> 
##  Engineering Object </description> </item><item><term> 
## AutomationDesignerVariable</term><description> 
##  Interface Variable </description> </item><item><term> 
## AutomationDesignerPlugNode</term><description> 
##  Plug and Plug-Chamber Nodes in Product Aspect Navigator </description> </item><item><term> 
## AutomationDesignerNode</term><description> 
##  Base Node </description> </item><item><term> 
## AutomationDesignerTag</term><description> 
##  Tag </description> </item><item><term> 
## AutomationDesignerCPU</term><description> 
##  CPU </description> </item><item><term> 
## AutomationDesignerUserConstant</term><description> 
##  Plc Constant </description> </item><item><term> 
## AutomationDesignerStation</term><description> 
##  Plc Station </description> </item><item><term> 
## AutomationDesignerPLCStation</term><description> 
##  Station </description> </item><item><term> 
## AutomationDesignerHardwareDevice</term><description> 
##  Module </description> </item><item><term> 
## AutomationDesignerHardwareItem</term><description> 
##  Hardware Item </description> </item><item><term> 
## AutomationDesignerLocalModuleFolder</term><description> 
##  Local Module Folder </description> </item><item><term> 
## AutomationDesignerDistributedIOFolder</term><description> 
##  Distributed I/O Folder </description> </item><item><term> 
## AutomationDesignerUpstreamDataObject</term><description> 
##  Excel Import Object </description> </item><item><term> 
## AutomationDesignerSymbol</term><description> 
##  Diagramming node </description> </item><item><term> 
## AutomationDesignerConnection</term><description> 
##  Connection object </description> </item><item><term> 
## AutomationDesignerConnectionPoint</term><description> 
##  Connection Point </description> </item><item><term> 
## AutomationDesignerAnnotation</term><description> 
##  Annotation </description> </item><item><term> 
## AutomationDesignerTable</term><description> 
##  Diagramming Table </description> </item><item><term> 
## AutomationDesignerAutomationUnassigned</term><description> 
##  Unassigned Node in Automation Navigator </description> </item><item><term> 
## AutomationDesignerDocumentRoot</term><description> 
##  Root node in Document Navigator </description> </item><item><term> 
## AutomationDesignerDocumentStructureNode</term><description> 
##  Document Structure Node </description> </item><item><term> 
## AutomationDesignerFragmentNode</term><description> 
##  Fragment Object Node </description> </item><item><term> 
## AutomationDesignerProduct</term><description> 
##  Product </description> </item><item><term> 
## AutomationDesignerProductComponent</term><description> 
##  Product Component created from Type </description> </item><item><term> 
## AutomationDesignerGroup</term><description> 
##  Group node </description> </item><item><term> 
## AutomationDesignerQuery</term><description> 
##  Query node </description> </item><item><term> 
## AutomationDesignerReportDefinition</term><description> 
##  Report definition node </description> </item><item><term> 
## AutomationDesignerPLCTagsFolder</term><description> 
##  Obsolete: Do Not Use </description> </item><item><term> 
## AutomationDesignerEClass</term><description> 
##  EClass Node </description> </item><item><term> 
## AutomationDesignerConnector</term><description> 
##  Physical Port </description> </item><item><term> 
## AutomationDesignerUserPort</term><description> 
##  User Port </description> </item><item><term> 
## AutomationDesignerPLCSubnet</term><description> 
##  PLC Subnet node </description> </item><item><term> 
## AutomationDesignerUdt</term><description> 
##  User defined data type </description> </item><item><term> 
## AutomationDesignerBaseDefinitionNode</term><description> 
##  Aspect and Product Definition node  </description> </item><item><term> 
## AutomationDesignerSymbolStructureNode</term><description> 
##  Symbol Structure Node </description> </item><item><term> 
## AutomationDesignerInterruptionPoint</term><description> 
##  Interruption Point </description> </item><item><term> 
## AutomationDesignerTagInterruptionPointNode</term><description> 
##  Interruption Point Node </description> </item><item><term> 
## AutomationDesignerRoot</term><description> 
##  Root node of Aspect Navigator </description> </item><item><term> 
## AutomationDesignerUnassigned</term><description> 
##  Unassigned folder in FLP aspect navigators </description> </item><item><term> 
## AutomationDesignerProductTemplateLinkNode</term><description> 
##  Product Template Link node </description> </item><item><term> 
## AutomationDesignerMemoryArea</term><description> 
##  Memory Area </description> </item><item><term> 
## AutomationDesigner2DSymbols3DModels</term><description> 
##  2D symbols and 3D Models assigned to a Product </description> </item><item><term> 
## AutomationDesignerCableCore</term><description> 
##  Cable Core </description> </item><item><term> 
## AutomationDesignerTagTable</term><description> 
##  Obsolete: Do Not Use </description> </item><item><term> 
## AutomationDesignerStationFolder</term><description> 
##  Folder node in Automation navigator </description> </item><item><term> 
## AutomationDesignerRack</term><description> 
##  PLC Rack </description> </item><item><term> 
## AutomationDesignerConnectedDevice</term><description> 
##  Shadow Object that represent hardware item connected to subnet via communication interface </description> </item><item><term> 
## AutomationDesignerSymbolVariant</term><description> 
##  Symbol Variant </description> </item><item><term> 
## AutomationDesignerViewPageNode</term><description> 
##  View page node in document navigator </description> </item><item><term> 
## AutomationDesignerBMECatVersionNode</term><description> 
##  BMECat version node in EClass structure navigator </description> </item><item><term> 
## AutomationDesignerEClassVersionNode</term><description> 
##  EClass Version Node </description> </item><item><term> 
## AutomationDesignerTemplateContent</term><description> 
##  Template Instance </description> </item><item><term> 
## AllCAE</term><description> 
##  The subset of CAE entities that can be shown and hidden </description> </item><item><term> 
## CAEPolygonEdge</term><description> 
##  CAE Polygon Edges </description> </item><item><term> 
## CAEPolygonFace</term><description> 
##  CAE Polygon Faces </description> </item><item><term> 
## CAEPolygonBody</term><description> 
##  CAE Polygon Bodies </description> </item><item><term> 
## CAEPolygonVertex</term><description> 
##  CAE Polygon Vertices </description> </item><item><term> 
## CAELoad</term><description> 
##  CAE Loads </description> </item><item><term> 
## CAEConstraint</term><description> 
##  CAE Constraints </description> </item><item><term> 
## CAESimulationObject</term><description> 
##  CAE Simulation Objects </description> </item><item><term> 
## CAEConnection</term><description> 
##  CAE Connections </description> </item><item><term> 
## CAEMeshPoint</term><description> 
##  CAE Mesh Points </description> </item><item><term> 
## CAEEdgeDensity</term><description> 
##  CAE Edge Density Mesh Control </description> </item><item><term> 
## CAEFaceDensity</term><description> 
##  CAE Edge Density Mesh Control </description> </item><item><term> 
## CAEWeldRowDensity</term><description> 
##  CAE Weld Row Density Mesh Control </description> </item><item><term> 
## CAEMappedHoleDensity</term><description> 
##  CAE Mapped Hole Density Mesh Control </description> </item><item><term> 
## CAEFilletDensity</term><description> 
##  CAE Fillet Density Mesh Control </description> </item><item><term> 
## CAECylinderDensity</term><description> 
##   CAE Cylinder Density Mesh Control </description> </item><item><term> 
## CAEPointDensity</term><description> 
##  CAE Point Density Mesh Control </description> </item><item><term> 
## CAEBoundingVolumeDensity</term><description> 
##  CAE Bounding Volume Density Mesh Control </description> </item><item><term> 
## CAEMeshMating</term><description> 
##  CAE Mesh Mating Condition Mesh Control </description> </item><item><term> 
## CAEEdgeSeparationCondition</term><description> 
##  CAE Edge Separation Condition Mesh Control </description> </item><item><term> 
## CAEBoundaryLayer</term><description> 
##  CAE Boundary Layer Mesh Control </description> </item><item><term> 
## CAESelectionRecipe</term><description> 
##  CAE Selection Recipe </description> </item><item><term> 
## CAECrackFaceCondition</term><description> 
##  CAE Crack Face Condition </description> </item><item><term> 
## CAEFaceMatchControl</term><description> 
##  CAE Face Match Mesh Control </description> </item><item><term> 
## CAEEdgeMatchControl</term><description> 
##  CAE Edge Match Mesh Control </description> </item><item><term> 
## CAEDOFSet</term><description> 
##  CAE DOF Set </description> </item><item><term> 
## CAEMesh</term><description> 
##  CAE Mesh </description> </item><item><term> 
## CAETransientMesh</term><description> 
##  CAE Transient Mesh </description> </item><item><term> 
## CAESensor</term><description> 
##  CAE Response Analysis Sensor </description> </item><item><term> 
## CAEResponseAnalysisStrainGauge</term><description> 
##  CAE Response Analysis Strain Gauge </description> </item><item><term> 
## CAEElement</term><description> 
##  CAE Element </description> </item><item><term> 
## CAEElementEdge</term><description> 
##  CAE Element Edge </description> </item><item><term> 
## CAEElementFace</term><description> 
##  CAE Element Face </description> </item><item><term> 
## CAENode</term><description> 
##  CAE Node </description> </item><item><term> 
## CAEMarginCalculation</term><description> 
##  CAE Aero Structures Margin Calculation </description> </item><item><term> 
## CAELoadCaseSet</term><description> 
##  CAE Aero Structures Load Case Set </description> </item><item><term> 
## CAEMarginSolution</term><description> 
##  CAE Aero Structures Margin Solution </description> </item><item><term> 
## CAEFilteringSolution</term><description> 
##  CAE Aero Structures Filtering Solution </description> </item><item><term> 
## CAEFilteringCalculation</term><description> 
##  CAE Aero Structures Filtering Calculation </description> </item><item><term> 
## CAEDurabilitySpecialistEvent</term><description> 
##  CAE Durability Specialist Event </description> </item><item><term> 
## CAELocalDefinition</term><description> 
##  CAE Durability Specialist Local Definition </description> </item><item><term> 
## CAESpecialistSolution</term><description> 
##  CAE Durability Specialist Specialist Solution </description> </item><item><term> 
## CAEFunctionDefinition</term><description> 
##  CAE Durability Specialist Function Definition </description> </item><item><term> 
## CAECorrelationInput</term><description> 
##  CAE Durability Specialist Correlation Input </description> </item><item><term> 
## CAEVibrationInput</term><description> 
##  CAE Durability Specialist Vibration Input </description> </item><item><term> 
## CAERandomDataSource</term><description> 
##  CAE Durability Specialist Random Data Source </description> </item><item><term> 
## CAEDurabilitySpecialistStrainGauge</term><description> 
##  CAE Durability Specialist Strain Gauge </description> </item><item><term> 
## CAEResultReference</term><description> 
##  CAE Result Reference </description> </item><item><term> 
## CAELayoutState</term><description> 
##  CAE Layout State </description> </item><item><term> 
## CAEFemDataSet</term><description> 
##  CAE Fem Data Set </description> </item><item><term> 
## CAELoadRecipe</term><description> 
##  CAE Load Recipe </description> </item><item><term> 
## CAEDataSource</term><description> 
##  CAE Data Source </description> </item><item><term> 
## CAEDataProcessing</term><description> 
##  CAE Data Processing MetaSolution </description> </item><item><term> 
## CAEModelAndLoadPreprocessing</term><description> 
##  CAE Model and Load Pre-processing MetaSolution </description> </item><item><term> 
## CAEAcousticsAndVibrationSolution</term><description> 
##  CAE Acoustics And Vibration Solution </description> </item><item><term> 
## CAETransientMeshGroup</term><description> 
##   CAE Transient Mesh Group </description> </item><item><term> 
## CAEUniversalConnectionFolder</term><description> 
##  CAE Universal Connection Folder </description> </item><item><term> 
## CAEUniversalConnection</term><description> 
##  CAE Universal Connection </description> </item><item><term> 
## CAESpotWeldConnection</term><description> 
##  CAE Spot Weld Connection </description> </item><item><term> 
## CAEAdhesiveConnection</term><description> 
##  CAE Adhesive Connection </description> </item><item><term> 
## CAEBoltConnection</term><description> 
##  CAE Bolt Connection </description> </item><item><term> 
## CAESeamWeldConnection</term><description> 
##  CAE Seam Weld Connection </description> </item><item><term> 
## CAESealingConnection</term><description> 
##  CAE Sealing Connection </description> </item><item><term> 
## CAESpringConnection</term><description> 
##  CAE Spring Connection </description> </item><item><term> 
## CAEDamperConnection</term><description> 
##  CAE Damper Connection </description> </item><item><term> 
## CAERigidConnection</term><description> 
##  CAE Rigid Connection </description> </item><item><term> 
## CAEBushingConnection</term><description> 
##  CAE Bushing Connection </description> </item><item><term> 
## CAEKinematicConnection</term><description> 
##  CAE Kinematic Connection </description> </item><item><term> 
## CAELumpedMass</term><description> 
##  CAE Lumped Mass </description> </item><item><term> 
## CAERivet</term><description> 
##  CAE Rivet </description> </item><item><term> 
## CAEClinch</term><description> 
##  CAE Clinch </description> </item><item><term> 
## CAECrimpConnection</term><description> 
##  CAE Crimp Connection </description> </item><item><term> 
## CAEBarConnection</term><description> 
##  CAE Bar Connection </description> </item><item><term> 
## CAEBearingConnection</term><description> 
##  CAE Bearing Connection </description> </item><item><term> 
## CAELoadCaseFilteringSolution</term><description> 
##  CAE Load Case Filtering Solution </description> </item><item><term> 
## CAEStressLinearization</term><description> 
##  CAE Stress Linearization </description> </item><item><term> 
## CAEStressLinearizationManager</term><description> 
##  CAE Stress Linearization Manager </description> </item><item><term> 
## CAEPostTransNode</term><description> 
##  Post Node </description> </item><item><term> 
## CAEPostTransElement</term><description> 
##  Post Element </description> </item><item><term> 
## CAEPostTransMesh</term><description> 
##  Post Mesh </description> </item><item><term> 
## CAEPostTransPolygonEdge</term><description> 
##  Post Polygon Edge</description> </item><item><term> 
## CAEPostTransPolygonFace</term><description> 
##  Post Polygon Face</description> </item><item><term> 
## CAEPostTransComponent</term><description> 
##  Post Component</description> </item><item><term> 
## CAEFreeBody</term><description> 
##  Nodal Force Report </description> </item><item><term> 
## CAEResultProbe</term><description> 
##  Result Probe </description> </item><item><term> 
## CAEPostTransElementFace</term><description> 
##  Post Element Face</description> </item><item><term> 
## CAEPostTransElementEdge</term><description> 
##  Post Element Edge</description> </item><item><term> 
## CAEFreeBodyFolder</term><description> 
##  CAE Nodal Force Report Folder</description> </item><item><term> 
## CAEStressLinearizationFolder</term><description> 
##  CAE Stress Linearization Folder</description> </item><item><term> 
## CAENoteConnection</term><description> 
##  CAE Note Connection </description> </item><item><term> 
## CoatingLayer</term><description> 
##  Coating Layer </description> </item><item><term> 
## CoatingStack</term><description> 
##  Coating Stack </description> </item><item><term> 
## LinearMaterial</term><description> 
##  Linear Material </description> </item><item><term> 
## DatumAxis</term><description> 
##  Datum Axis </description> </item><item><term> 
## DatumPlane</term><description> 
##  Datum Plane </description> </item><item><term> 
## SectionSegment</term><description> 
##  Section Segment </description> </item><item><term> 
## SectionLine</term><description> 
##  Section Line </description> </item><item><term> 
## CoordinateSystem</term><description> 
##  Coordinate System </description> </item><item><term> 
## Plane</term><description> 
##  Plane </description> </item><item><term> 
## DatumPlaneGrid</term><description> 
##  Datum Plane Grid </description> </item><item><term> 
## PlanarShipGrid</term><description> 
##  Planar Ship Grid </description> </item><item><term> 
## Traceline</term><description> 
##  Traceline </description> </item><item><term> 
## Image</term><description> 
##  Image </description> </item><item><term> 
## ControlCage</term><description> 
##  Control cage used by NX Realize Shape application </description> </item><item><term> 
## CageFace</term><description> 
##  Face of control cage used by NX Realize Shape application </description> </item><item><term> 
## CageEdge</term><description> 
##  Edge of control cage used by NX Realize Shape application </description> </item><item><term> 
## CageVertex</term><description> 
##  Vertex of control cage used by NX Realize Shape application </description> </item><item><term> 
## DesignMeshBody</term><description> 
##  Represents selection filter for a body of a design mesh. Design mesh is a faceted representation used by modeling applications </description> </item><item><term> 
## DesignMeshFace</term><description> 
##  Represents selection filter for a facet face, typically a triangle, of a design mesh. Design mesh is a faceted representation used by modeling applications </description> </item><item><term> 
## DesignMeshEdge</term><description> 
##  Represents selection filter for a facet edge of a design mesh. Design mesh is a faceted representation used by modeling applications </description> </item><item><term> 
## DesignMeshVertex</term><description> 
##  Represents selection filter for a facet vertex of a design mesh. Design mesh is a faceted representation used by modeling applications </description> </item><item><term> 
## AllDimensions</term><description> 
##  All Dimensions </description> </item><item><term> 
## LinearDimension</term><description> 
##  Linear Dimension </description> </item><item><term> 
## AngularDimension</term><description> 
##  Angular Dimension </description> </item><item><term> 
## RadialDimension</term><description> 
##  Radial Dimension </description> </item><item><term> 
## OrdinateDimension</term><description> 
##  Ordinate Dimension </description> </item><item><term> 
## ChamferDimension</term><description> 
##  Chamfer Dimension </description> </item><item><term> 
## ThicknessDimension</term><description> 
##  Thickness Dimension </description> </item><item><term> 
## ArcLengthDimension</term><description> 
##  Arc Length Dimension </description> </item><item><term> 
## DimensionSet</term><description> 
##  Dimension Set </description> </item><item><term> 
## AllDrafting</term><description> 
##  All Drafting </description> </item><item><term> 
## AllCenterlines</term><description> 
##  All Centerlines </description> </item><item><term> 
## AreaFill</term><description> 
##  Area Fill </description> </item><item><term> 
## AllSymbols</term><description> 
##  All Drafting Symbols </description> </item><item><term> 
## Note</term><description> 
##  Note </description> </item><item><term> 
## Label</term><description> 
##  Label </description> </item><item><term> 
## Balloon</term><description> 
##  Balloon </description> </item><item><term> 
## GDTSymbol</term><description> 
##  GDT Symbol </description> </item><item><term> 
## Centerline</term><description> 
##  Centerline </description> </item><item><term> 
## FullCircularCenterline</term><description> 
##  Full Circular Centerline </description> </item><item><term> 
## PartialCircularCenterline</term><description> 
##  Partial Circular Centerline </description> </item><item><term> 
## FullBoltCircle</term><description> 
##  Full Bolt Circle Centerline </description> </item><item><term> 
## PartialBoltCircle</term><description> 
##  Partial Bolt Circle Centerline </description> </item><item><term> 
## CenterMark</term><description> 
##  Center Mark </description> </item><item><term> 
## CylindricalCenterline</term><description> 
##  Cylindrical Centerline </description> </item><item><term> 
## SymmetricalCenterline</term><description> 
##  Symmetrical Centerline </description> </item><item><term> 
## Centerline2D</term><description> 
##  2D Centerline </description> </item><item><term> 
## Crosshatch</term><description> 
##  Crosshatch </description> </item><item><term> 
## Intersection</term><description> 
##  Intersection </description> </item><item><term> 
## TargetPoint</term><description> 
##  Target Point </description> </item><item><term> 
## UserDefinedSymbol</term><description> 
##  User Defined Symbol </description> </item><item><term> 
## OffsetCenterPoint</term><description> 
##  Offset Center Point </description> </item><item><term> 
## LabelOnParent</term><description> 
##  Label on Parent </description> </item><item><term> 
## TitleBlock</term><description> 
##  Title Block </description> </item><item><term> 
## FrameBar</term><description> 
##  Frame Bar </description> </item><item><term> 
## Arrow</term><description> 
##  Arrow </description> </item><item><term> 
## CuttingPlaneSymbol</term><description> 
##  Cutting Plane Symbol </description> </item><item><term> 
## ShipTic</term><description> 
##  Ship Tic </description> </item><item><term> 
## SupplementalGeometry</term><description> 
##  Supplemental Geometry </description> </item><item><term> 
## ViewBreak</term><description> 
##  View Break </description> </item><item><term> 
## DrawingTemplateRegion</term><description> 
##  Drawing Template Region </description> </item><item><term> 
## SurfaceFinish</term><description> 
##  Surface Finish </description> </item><item><term> 
## TabularNote</term><description> 
##  Tabular Note/Parts List </description> </item><item><term> 
## DrawingImage</term><description> 
##  Drawing Image </description> </item><item><term> 
## Component2D</term><description> 
##  2D Component </description> </item><item><term> 
## ProductGrid</term><description> 
##  Product Grid </description> </item><item><term> 
## EdgeConditionSymbol</term><description> 
##  Edge Condition Symbol </description> </item><item><term> 
## AllFacetBodies</term><description> 
##  Normal and Cloud Facet Bodies </description> </item><item><term> 
## NormalFacetBody</term><description> 
##  Normal Facet Body </description> </item><item><term> 
## CloudFacetBody</term><description> 
##  Cloud Facet Body </description> </item><item><term> 
## NXFacet</term><description> 
##  NX Facet </description> </item><item><term> 
## AllBasicAndWeldFeatures</term><description> 
##  All Basic and Weld Features </description> </item><item><term> 
## AllBasicFeatures</term><description> 
##  All Basic Features </description> </item><item><term> 
## SolidFeature</term><description> 
##  Solid Feature </description> </item><item><term> 
## CurveFeature</term><description> 
##  Curve Feature </description> </item><item><term> 
## DatumPlaneFeature</term><description> 
##  Datum Plane Feature </description> </item><item><term> 
## DatumAxisFeature</term><description> 
##  Datum Axis Feature </description> </item><item><term> 
## DatumCoordinateSystemFeature</term><description> 
##  Datum Coordinate System Feature </description> </item><item><term> 
## SketchFeature</term><description> 
##  Sketch Feature </description> </item><item><term> 
## HD3DMarkup</term><description> 
##  Markup </description> </item><item><term> 
## HD3DMarkupElement</term><description> 
##  Markup Element </description> </item><item><term> 
## AllJoinObjects</term><description> 
##  All Join objects </description> </item><item><term> 
## JoinPoint</term><description> 
##  Point Join Feature </description> </item><item><term> 
## JoinCurve</term><description> 
##  Curve Join Feature </description> </item><item><term> 
## JoinFace</term><description> 
##  Face Join Feature </description> </item><item><term> 
## JoinHole</term><description> 
##  Join Hole Feature </description> </item><item><term> 
## LineDesignerConnector</term><description> 
##  Line Designer Connector </description> </item><item><term> 
## MachiningFeature</term><description> 
##  Machining Feature in Manufacturing </description> </item><item><term> 
## MachiningToolPath</term><description> 
##  Tool Path in Manufacturing </description> </item><item><term> 
## MachiningInProcessWorkpiece</term><description> 
##  In-Process-Workpiece in Manufacturing </description> </item><item><term> 
## AdditiveManufacturingSerialNumber</term><description> 
##  Serial Number in Additive Manufacturing </description> </item><item><term> 
## AdditiveManufacturingPartGroup</term><description> 
##  Part Group in Additive Manufacturing </description> </item><item><term> 
## AdditiveManufacturingBuildTray</term><description> 
##  BuildTray in Additive Manufacturing </description> </item><item><term> 
## AdditiveManufacturingPart</term><description> 
##  Part in Additive Manufacturing </description> </item><item><term> 
## AdditiveManufacturingPartOccurrence</term><description> 
##  PartOccurrence in Additive Manufacturing </description> </item><item><term> 
## AdditiveManufacturingSupport</term><description> 
##  Support in Additive Manufacturing </description> </item><item><term> 
## AdditiveManufacturingSupportOccurrence</term><description> 
##  Support Occurrence in Additive Manufacturing </description> </item><item><term> 
## AdditiveManufacturingPartRegion</term><description> 
##  Part Region in Additive Manufacturing </description> </item><item><term> 
## AdditiveManufacturingPartRegionOccurrence</term><description> 
##  Part Region Occurrence in Additive Manufacturing </description> </item><item><term> 
## ManufacturingPlanningRigidGroup</term><description> 
##  The rigid group of objects or components for Manufacturing Planning applications </description> </item><item><term> 
## ManufacturingPlanningJoint</term><description> 
##  The joint relationship between rigid groups for Manufacturing Planning applications </description> </item><item><term> 
## MDCLogicalElement</term><description> 
##  Logical Element for Multi-Discipline Connectivity </description> </item><item><term> 
## MDCConnectionElement</term><description> 
##  Logical Connection for Multi-Discipline Connectivity </description> </item><item><term> 
## MDCPortArtifact</term><description> 
##  Logical Port for Multi-Discipline Connectivity </description> </item><item><term> 
## AllMechatronics</term><description> 
##  All Mechatronics objects </description> </item><item><term> 
## MechatronicsJoint</term><description> 
##  All kinds of mechatronics joints for defining a relationship between rigid bodies </description> </item><item><term> 
## MechatronicsCollisionBody</term><description> 
##  A Collision Body defines objects to be able to collide with one another </description> </item><item><term> 
## MechatronicsCollisionSensor</term><description> 
##  A Collision Sensor is able to detect the presence of objects that intersect with its volume </description> </item><item><term> 
## MechatronicsRuntimeButton</term><description> 
##  A Runtime Button defines the user interaction during runtime </description> </item><item><term> 
## MechatronicsDistanceSensor</term><description> 
##  A distance sensor detects the shortest distance between the sensor and collision body </description> </item><item><term> 
## Mechatronics2DLaserScanner</term><description> 
##  A laser scanner is a set of beams which detects the distances, color or other properties for target objects </description> </item><item><term> 
## MechatronicsLightCurtain</term><description> 
##  A light curtain is a set of beams which detects the collision of target objects </description> </item><item><term> 
## MechatronicsPositionSensor</term><description> 
##  A Position Control causes objects attached to an axis to move along that axis to a given position </description> </item><item><term> 
## MechatronicsVelocitySensor</term><description> 
##  A velocity sensor returns the angular or linear velocity of the selected joint </description> </item><item><term> 
## MechatronicsGenericSensor</term><description> 
##  A generic sensor returns the parameter value of the selected object </description> </item><item><term> 
## MechatronicsLimitSwitch</term><description> 
##  A limit switch references any runtime parameter from the selected object and has a boolean output </description> </item><item><term> 
## MechatronicsRelay</term><description> 
##  A relay references any runtime parameter from the selected object and has a boolean output </description> </item><item><term> 
## MechatronicsInclinometer</term><description> 
##  An inclinometer returns the angle value of the selected rigid body </description> </item><item><term> 
## MechatronicsAccelerometer</term><description> 
##  An accelerometer returns the accelerometer value of the selected rigid body </description> </item><item><term> 
## MechatronicsPneumaticCylinder</term><description> 
##  A pneumatic cylinder causes forces according to the characteristic of a compressible fluid to move simulation objects </description> </item><item><term> 
## MechatronicsPneumaticValve</term><description> 
##  A pneumatic valve controls a pneumatic cylinder </description> </item><item><term> 
## MechatronicsHydraulicCylinder</term><description> 
##  A hydraulic cylinder causes forces according to the characteristic of an incompressible fluid to move simulation objects </description> </item><item><term> 
## MechatronicsHydraulicValve</term><description> 
##  A hydraulic valve controls a hydraulic cylinder </description> </item><item><term> 
## MechatronicsRigidBody</term><description> 
##  A Rigid Body defines objects to be able to move about the world </description> </item><item><term> 
## MechatronicsConstraint</term><description> 
##  All kinds of mechatronics constraint </description> </item><item><term> 
## MechatronicsTransportSurface</term><description> 
##  Transport Surface causes a face on a geometric object to behave like it is moving even if the object is attached </description> </item><item><term> 
## MechatronicsObjectSource</term><description> 
##  Object Source is used to define some objects that can be copied during simulation </description> </item><item><term> 
## MechatronicsObjectSink</term><description> 
##  Object Sink is used to define some objects that delete copies of physics objects during simulation </description> </item><item><term> 
## MechatronicsObjectTransformer</term><description> 
##  An Object Transformer defines objects to be able to transform copies of rigid objects to another during simulation </description> </item><item><term> 
## MechatronicsObjectBehavior</term><description> 
##  Objects that are used to define kinds of behavior during simulation </description> </item><item><term> 
## MechatronicsObjectData</term><description> 
##  Objects that encapsulate data for simulation, for instance, collision material, motion profile, etc </description> </item><item><term> 
## MechatronicsProxyObject</term><description> 
##  A Proxy Object defines the object that has certain parameter attributes, encapsulates certain physics objects, and has some geometric representation </description> </item><item><term> 
## MechatronicsSignal</term><description> 
##  Signals used to define connections with adapters or external tools </description> </item><item><term> 
## MechatronicsSnapPoint</term><description> 
##  A SnapPoint defines one body positioning or two bodies that exactly lie upon each other </description> </item><item><term> 
## MechatronicsDynamicMaterial</term><description> 
##  A Dynamic Material to support variable size simulation </description> </item><item><term> 
## AllMotionSim</term><description> 
##  All MotionSim objects </description> </item><item><term> 
## AllMotionSimForceObjects</term><description> 
##  Force objects including Bushing, Contact, Damper, Force, Spring </description> </item><item><term> 
## AllMotionSimJoints</term><description> 
##  All MotionSim Joints </description> </item><item><term> 
## MotionSimRoad</term><description> 
##  Road </description> </item><item><term> 
## MotionSimBearing</term><description> 
##  Bearing </description> </item><item><term> 
## MotionSimBearingProperty</term><description> 
##  Bearing Property </description> </item><item><term> 
## MotionSimControlPort</term><description> 
##  Control Port </description> </item><item><term> 
## MotionSimControlInput</term><description> 
##  Control Input </description> </item><item><term> 
## MotionSimPathFollower</term><description> 
##  Path Follower </description> </item><item><term> 
## MotionSimControlOperation</term><description> 
##  Control Operation </description> </item><item><term> 
## MotionSimControlOutput</term><description> 
##  Control Output </description> </item><item><term> 
## MotionSimGear</term><description> 
##  Gear </description> </item><item><term> 
## MotionSimGearContact</term><description> 
##  Gear Contact </description> </item><item><term> 
## MotionSimAnimation</term><description> 
##  Animation </description> </item><item><term> 
## MotionSimGraph</term><description> 
##  Graph </description> </item><item><term> 
## MotionSimMlpp</term><description> 
##  Model and Load Pre-processing in Motion </description> </item><item><term> 
## MotionSimCurveOperationRecord</term><description> 
##  Curve Operation Record in Motion </description> </item><item><term> 
## MotionSimMotionBodyDriver</term><description> 
##  Motion Body Driver </description> </item><item><term> 
## MotionSimLoadTransfer</term><description> 
##  Load Transfer </description> </item><item><term> 
## MotionSimJointDriver</term><description> 
##  Joint Driver </description> </item><item><term> 
## MotionSimStandaloneDriver</term><description> 
##  Standalone Driver </description> </item><item><term> 
## MotionSimMechatronics</term><description> 
##  Mechatronics </description> </item><item><term> 
## MotionSimProfile</term><description> 
##  Profile in Motion </description> </item><item><term> 
## MotionSimDiscreteDrivetrain</term><description> 
##  Discrete Drivetrain </description> </item><item><term> 
## MotionSimAnimationCamera</term><description> 
##  Animation Camera in Motion </description> </item><item><term> 
## MotionSimAutoflexProperty</term><description> 
##  Autoflex Property </description> </item><item><term> 
## MotionSimBasicTireProperty</term><description> 
##  Basic Tire Property </description> </item><item><term> 
## MotionSimMotorcycleTireProperty</term><description> 
##  Motorcycle Tire Property </description> </item><item><term> 
## MotionSimNonInertialTireProperty</term><description> 
##  Non-inertial Tire Property </description> </item><item><term> 
## MotionSimFTireProperty</term><description> 
##  FTire Property </description> </item><item><term> 
## MotionSimCDTireProperty</term><description> 
##  CDTire Property </description> </item><item><term> 
## MotionSimMFTyreAndMFSwiftTireProperty</term><description> 
##  MF-Tyre and MF-Swift Tire Property </description> </item><item><term> 
## MotionSimTire</term><description> 
##  Tire </description> </item><item><term> 
## MotionSimVehicleReporting</term><description> 
##  Vehicle Reporting </description> </item><item><term> 
## MotionSimSuspensionReporting</term><description> 
##  Suspension Reporting </description> </item><item><term> 
## MotionSimInitialCondition</term><description> 
##  Initial Condition </description> </item><item><term> 
## MotionSimAnalyticalContact</term><description> 
##  Analytical Contact </description> </item><item><term> 
## MotionSimAnalyticalContactProperty</term><description> 
##  Analytical Contact Property </description> </item><item><term> 
## MotionSimSpring</term><description> 
##  Spring </description> </item><item><term> 
## MotionSimRotationalSpring</term><description> 
##  Rotational Spring </description> </item><item><term> 
## MotionSimTranslationalSpring</term><description> 
##  Translational Spring </description> </item><item><term> 
## MotionSimDamper</term><description> 
##  Damper </description> </item><item><term> 
## MotionSimRotationalDamper</term><description> 
##  Rotational Damper </description> </item><item><term> 
## MotionSimTranslationalDamper</term><description> 
##  Translational Damper </description> </item><item><term> 
## MotionSimSpringDamper</term><description> 
##  Spring Damper </description> </item><item><term> 
## MotionSimRotationalSpringDamper</term><description> 
##  Rotational Spring Damper </description> </item><item><term> 
## MotionSimTranslationalSpringDamper</term><description> 
##  Translational Spring Damper </description> </item><item><term> 
## MotionSimSplineBeam</term><description> 
##  Spline Beam </description> </item><item><term> 
## MotionSimSplineBeamProperty</term><description> 
##  SplineBeam Property </description> </item><item><term> 
## MotionSimBeamSection</term><description> 
##  Beam Section </description> </item><item><term> 
## MotionSimBeamForce</term><description> 
##  Beam Force </description> </item><item><term> 
## MotionSimUserDefinedForce</term><description> 
##  User-defined Force </description> </item><item><term> 
## MotionSimFriction</term><description> 
##  Friction </description> </item><item><term> 
## MotionSimThreePointForce</term><description> 
##  Three-point Force </description> </item><item><term> 
## MotionSimThreePointTorque</term><description> 
##  Three-point Torque </description> </item><item><term> 
## MotionSimSubmechanism</term><description> 
##  Submechanism </description> </item><item><term> 
## MotionSimSubmechanismPositioner</term><description> 
##  Submechanism Positioner </description> </item><item><term> 
## MotionSimMotionConstraint</term><description> 
##  Motion Constraint </description> </item><item><term> 
## MotionSimMotionBody</term><description> 
##  Motion Body </description> </item><item><term> 
## MotionSimScalarForce</term><description> 
##  Scalar Force </description> </item><item><term> 
## MotionSimFlexibleBody</term><description> 
##  Flexible Body </description> </item><item><term> 
## MotionSimMarker</term><description> 
##  Marker </description> </item><item><term> 
## MotionSimScalarTorque</term><description> 
##  Scalar Torque </description> </item><item><term> 
## MotionSimCurveCurveContact</term><description> 
##  Curve/Curve Contact </description> </item><item><term> 
## MotionSimContact</term><description> 
##  Contact </description> </item><item><term> 
## MotionSimBushing</term><description> 
##  Bushing </description> </item><item><term> 
## MotionSimBushingProperty</term><description> 
##  Bushing Property</description> </item><item><term> 
## MotionSimVectorForce</term><description> 
##  Vector Force </description> </item><item><term> 
## MotionSimVectorTorque</term><description> 
##  Vector Torque </description> </item><item><term> 
## MotionSimSensor</term><description> 
##  Sensor </description> </item><item><term> 
## MotionSimMotor</term><description> 
##  Motor </description> </item><item><term> 
## MotionSimMotionVector</term><description> 
##  Motion Vector </description> </item><item><term> 
## MotionSimMeasure</term><description> 
##  Measure in Motion </description> </item><item><term> 
## MotionSimTrace</term><description> 
##  Trace in Motion </description> </item><item><term> 
## MotionSimInterference</term><description> 
##  Interference in Motion </description> </item><item><term> 
## MotionSimFixedJoint</term><description> 
##  Fixed Joint </description> </item><item><term> 
## MotionSimScrewJoint</term><description> 
##  Screw Joint </description> </item><item><term> 
## MotionSimRevoluteJoint</term><description> 
##  Revolute Joint </description> </item><item><term> 
## MotionSimSliderJoint</term><description> 
##  Slider Joint </description> </item><item><term> 
## MotionSimCylinderJoint</term><description> 
##  Cylinder Joint </description> </item><item><term> 
## MotionSimUniversalJoint</term><description> 
##  Universal Joint </description> </item><item><term> 
## MotionSimSphericalJoint</term><description> 
##  Spherical Joint </description> </item><item><term> 
## MotionSimPlanarJoint</term><description> 
##  Planar Joint </description> </item><item><term> 
## MotionSimGearJoint</term><description> 
##  Gear Joint </description> </item><item><term> 
## MotionSimRackAndPinion</term><description> 
##  Rack and Pinion </description> </item><item><term> 
## MotionSimPointOnCurve</term><description> 
##  Point on Curve </description> </item><item><term> 
## MotionSimCurveOnCurve</term><description> 
##  Curve on Curve </description> </item><item><term> 
## MotionSimCable</term><description> 
##  Cable </description> </item><item><term> 
## MotionSimConstantVelocity</term><description> 
##  Constant Velocity </description> </item><item><term> 
## MotionSimAtpointJoint</term><description> 
##  Atpoint Joint </description> </item><item><term> 
## MotionSimInlineJoint</term><description> 
##  Inline Joint </description> </item><item><term> 
## MotionSimInplaneJoint</term><description> 
##  Inplane Joint </description> </item><item><term> 
## MotionSimOrientationJoint</term><description> 
##  Orientation Joint </description> </item><item><term> 
## MotionSimParallelJoint</term><description> 
##  Parallel Joint </description> </item><item><term> 
## MotionSimPerpendicularJoint</term><description> 
##  Perpendicular Joint </description> </item><item><term> 
## MotionSimGeneralCoupler</term><description> 
##  General Coupler </description> </item><item><term> 
## MotionSimMotionBodyCoupler</term><description> 
##  Motion Body Coupler </description> </item><item><term> 
## MotionSimPlantInput</term><description> 
##  Plant Input </description> </item><item><term> 
## MotionSimPlantOutput</term><description> 
##  Plant Output </description> </item><item><term> 
## MotionSimSolutionStop</term><description> 
##  Solution Stop </description> </item><item><term> 
## MotionSimSignalChart</term><description> 
##  Signal Chart </description> </item><item><term> 
## MotionSimSolution</term><description> 
##  Solution </description> </item><item><term> 
## MotionSimGearSpur</term><description> 
##  Spur Gear </description> </item><item><term> 
## MotionSimGearHelical</term><description> 
##  Helical Gear </description> </item><item><term> 
## MotionSimGearStraightBevel</term><description> 
##  Straight Bevel Gear </description> </item><item><term> 
## MotionSimGearSpiralBevel</term><description> 
##  Spiral Bevel Gear </description> </item><item><term> 
## MotionSimGearHypoid</term><description> 
##  Hypoid Gear </description> </item><item><term> 
## MotionSimBumpStop</term><description> 
##  BumpStop </description> </item><item><term> 
## MotionSimCompoundJoint</term><description> 
##  CompoundJoint </description> </item><item><term> 
## MotionSimAnimationVector</term><description> 
##  AnimationVector </description> </item><item><term> 
## MotionSimHydrodynamicBearing</term><description> 
##  Hydrodynamic Bearing </description> </item><item><term> 
## MotionSimSprungMass</term><description> 
##  Sprung Mass</description> </item><item><term> 
## MotionSimDiscreteDrivetrainReport</term><description> 
##  Discrete Drivetrain Report</description> </item><item><term> 
## MotionSimElectromagneticForce</term><description> 
##  ElectromagneticForce</description> </item><item><term> 
## MotionSimGeneralSensor</term><description> 
##  General Sensor</description> </item><item><term> 
## MotionSimContactPattern</term><description> 
##  ContactPattern </description> </item><item><term> 
## MotionSimFlexModalContent</term><description> 
##  Flex Modal Content </description> </item><item><term> 
## MotionSimFixedJointDriver</term><description> 
##  Fixed Joint Driver </description> </item><item><term> 
## MotionSimFrfInput</term><description> 
##  Frf Input </description> </item><item><term> 
## MotionSimFrfOutput</term><description> 
##  Frf Output </description> </item><item><term> 
## PhysicalDiagrammingAnnotation</term><description> 
##  Annotation for physical and boundary diagramming </description> </item><item><term> 
## PhysicalDiagrammingConnection</term><description> 
##  Connection for physical and boundary diagramming </description> </item><item><term> 
## PhysicalDiagrammingNode</term><description> 
##  Node for physical and boundary diagramming </description> </item><item><term> 
## BoundaryNode</term><description> 
##  Boundary node </description> </item><item><term> 
## PIDAnnotation</term><description> 
##  PID Annotation </description> </item><item><term> 
## PIDConnection</term><description> 
##  PID Connection </description> </item><item><term> 
## PIDSymbol</term><description> 
##  PID Symbol </description> </item><item><term> 
## PIDRun</term><description> 
##  PID Run </description> </item><item><term> 
## PIDBranch</term><description> 
##  PID Branch </description> </item><item><term> 
## PIDSheet</term><description> 
##  PID Sheet </description> </item><item><term> 
## PIDSystem</term><description> 
##  PID System </description> </item><item><term> 
## PressLineSimulationLineComponent</term><description> 
##  Selection filter for line component objects of a press line simulation job.
##                                                                   The selected object can for instance be used to define the scope for subsequent
##                                                                   collision checking. E.g. selecting a line component for the collision scope
##                                                                   means that only the selected station is taken into account for collision checking. </description> </item><item><term> 
## PressLineSimulationPressModelRoot</term><description> 
##  Selection filter for the root object of a press line simulation job.
##                                                                    The selected object can for instance be used to define the scope for
##                                                                    subsequent collision checking. E.g. selecting the root object for the collision
##                                                                    scope means that the entire press line is taken into account for collision checking. </description> </item><item><term> 
## AllRoutingObjects</term><description> 
##  All Routing Objects </description> </item><item><term> 
## RoutingControlPoint</term><description> 
##  Routing Control Point </description> </item><item><term> 
## RoutingPort</term><description> 
##  Routing Port </description> </item><item><term> 
## RoutingPartAnchor</term><description> 
##  Routing Part Anchor </description> </item><item><term> 
## RoutingSegment</term><description> 
##  Routing Segment </description> </item><item><term> 
## RoutingStock</term><description> 
##  Routing Stock </description> </item><item><term> 
## AllShip</term><description> 
##  All ship basic design structure objects </description> </item><item><term> 
## AllShipPlateSystem</term><description> 
##  All ship basic design plate systems </description> </item><item><term> 
## AllShipProfileSystem</term><description> 
##  All ship basic design profile systems </description> </item><item><term> 
## ShipHull</term><description> 
##  Ship basic design hull </description> </item><item><term> 
## ShipDeck</term><description> 
##  Ship basic design deck </description> </item><item><term> 
## ShipTransverseBulkhead</term><description> 
##  Ship basic design transverse bulkhead </description> </item><item><term> 
## ShipLongitudinalBulkhead</term><description> 
##  Ship basic design longitudinal bulkhead </description> </item><item><term> 
## ShipGenericPlateSystem</term><description> 
##  Ship basic design generic plate system </description> </item><item><term> 
## ShipStiffenerSystem</term><description> 
##  Ship basic design stiffener system </description> </item><item><term> 
## ShipPillarSystem</term><description> 
##  Ship basic design pillar system </description> </item><item><term> 
## ShipEdgeReinforcement</term><description> 
##  Ship basic design edge reinforcement system </description> </item><item><term> 
## ShipSeam</term><description> 
##  Ship basic design seam object, including scantling seam, erection seam, straking seam </description> </item><item><term> 
## SketchRelation</term><description> 
## Persistent Relation objects, formerly known as Sketch Constraints  </description> </item><item><term> 
## Sketch</term><description> 
##  Sketch is a collection of planar curves with dimensions and relations.  It may or may not be related to a feature. </description> </item><item><term> 
## SketchFoundRelation</term><description> 
##  Found Relations exist during a solver operation and can be relaxed by selecting them. </description> </item><item><term> 
## SketchCoincidentRelation</term><description> 
##  Persistent or Found Coincident Relation in a Sketch </description> </item><item><term> 
## SketchConcentricRelation</term><description> 
##  Persistent or Found Concentric Relation in a Sketch </description> </item><item><term> 
## SketchPointOnCurveRelation</term><description> 
##  Persistent or Found Point On Curve Relation in a Sketch </description> </item><item><term> 
## SketchCollinearRelation</term><description> 
##  Persistent or Found Collinear Relation in a Sketch </description> </item><item><term> 
## SketchHorizontalRelation</term><description> 
##  Persistent or Found Horizontal Relation in a Sketch </description> </item><item><term> 
## SketchHorizontalAlignmentRelation</term><description> 
##  Persistent or Found Horizontal Alignment Relation in a Sketch </description> </item><item><term> 
## SketchVerticalRelation</term><description> 
##  Persistent or Found Vertical Relation in a Sketch </description> </item><item><term> 
## SketchVerticalAlignmentRelation</term><description> 
##  Persistent or Found Vertical Alignment Relation in a Sketch </description> </item><item><term> 
## SketchTangentRelation</term><description> 
##  Persistent or Found Tangent Relation in a Sketch </description> </item><item><term> 
## SketchParallelRelation</term><description> 
##  Persistent or Found Parallel Relation in a Sketch </description> </item><item><term> 
## SketchPerpendicularRelation</term><description> 
##  Persistent or Found Perpendicular Relation in a Sketch </description> </item><item><term> 
## SketchEqualLengthRelation</term><description> 
##  Persistent or Found Equal Length Relation in a Sketch </description> </item><item><term> 
## SketchEqualRadiusRelation</term><description> 
##  Persistent or Found Equal Radius Relation in a Sketch </description> </item><item><term> 
## SketchSymmetricRelation</term><description> 
##  Persistent or Found Symmetric Relation in a Sketch </description> </item><item><term> 
## SketchMidpointRelation</term><description> 
##  Persistent Midpoint Relation in a Sketch </description> </item><item><term> 
## SketchPointOnStringRelation</term><description> 
##  Persistent Point On String Relation in a Sketch, used for a connected string of recipe curves </description> </item><item><term> 
## SketchTangentToStringRelation</term><description> 
##  Persistent Tangent To String Relation in a Sketch, used for a connected string of recipe curves </description> </item><item><term> 
## SketchPerpendicularToStringRelation</term><description> 
##  Persistent Perpendicular To String Relation in a Sketch, used for a connected string of recipe curves </description> </item><item><term> 
## SketchUniformScaleRelation</term><description> 
##  Persistent Uniform Scale Relation in a Sketch, used for splines </description> </item><item><term> 
## SketchG1SplineRelation</term><description> 
##  Persistent G1 Spline Relation in a Sketch </description> </item><item><term> 
## SketchG2SplineRelation</term><description> 
##  Persistent G2 Spline Relation in a Sketch </description> </item><item><term> 
## SketchTrimRelation</term><description> 
##  Persistent Trim Relation in a Sketch, used for trimming recipe curves </description> </item><item><term> 
## SketchOffsetRelation</term><description> 
##  Persistent or Found Offset Relation in a Sketch </description> </item><item><term> 
## SketchLinearPatternRelation</term><description> 
##  Persistent Linear Pattern Relation in a Sketch </description> </item><item><term> 
## SketchRectangularPatternRelation</term><description> 
##  Persistent Rectangular Pattern Relation in a Sketch </description> </item><item><term> 
## SketchCircularPatternRelation</term><description> 
##  Persistent Circular Pattern Relation in a Sketch </description> </item><item><term> 
## SketchGeneralPatternRelation</term><description> 
##  Persistent General Pattern Relation in a Sketch </description> </item><item><term> 
## SketchMirrorRelation</term><description> 
##  Persistent Mirror Relation in a Sketch </description> </item><item><term> 
## SketchPolygonRelation</term><description> 
##  Persistent Polygon Relation in a Sketch </description> </item><item><term> 
## SketchRigidGroupRelation</term><description> 
##  Persistent Rigid Group Relation in a Sketch </description> </item><item><term> 
## SketchScalableGroupRelation</term><description> 
##  Persistent Scalable Group Relation in a Sketch </description> </item><item><term> 
## SketchIgnoredRelation</term><description> 
##  Ignored Relation in a Sketch, prevents finding of this relation by the solver </description> </item><item><term> 
## AllEdges</term><description> 
##  All Edges </description> </item><item><term> 
## AllFaces</term><description> 
##  All Faces </description> </item><item><term> 
## AllSolidBodies</term><description> 
##  All Solid Bodies </description> </item><item><term> 
## AllSheetBodies</term><description> 
##  All Sheet Bodies </description> </item><item><term> 
## ConvergentSolidBody</term><description> 
##  Convergent Solid Body </description> </item><item><term> 
## ConvergentSheetBody</term><description> 
##  Convergent Sheet Body </description> </item><item><term> 
## PlanarFace</term><description> 
##  Planar Face </description> </item><item><term> 
## CylindricalFace</term><description> 
##  Cylindrical Face </description> </item><item><term> 
## ConicalFace</term><description> 
##  Conical Face </description> </item><item><term> 
## SphericalFace</term><description> 
##  Spherical Face </description> </item><item><term> 
## ToroidalFace</term><description> 
##  Toroidal Face </description> </item><item><term> 
## ParametricFace</term><description> 
##  Parametric Face </description> </item><item><term> 
## BlendedFace</term><description> 
##  Blended Face </description> </item><item><term> 
## OffsetFace</term><description> 
##  Offset Face </description> </item><item><term> 
## ExtrudedFace</term><description> 
##  Extruded Face </description> </item><item><term> 
## RevolvedFace</term><description> 
##  Revolved Face </description> </item><item><term> 
## ForeignFace</term><description> 
##  Foreign Face </description> </item><item><term> 
## ConvergentFace</term><description> 
##  Convergent Face </description> </item><item><term> 
## LinearEdge</term><description> 
##  Linear Edge </description> </item><item><term> 
## CircularEdge</term><description> 
##  Circular Edge </description> </item><item><term> 
## EllipticalEdge</term><description> 
##  Elliptical Edge </description> </item><item><term> 
## IntersectionEdge</term><description> 
##  Intersection Edge </description> </item><item><term> 
## SplineEdge</term><description> 
##  Spline Edge </description> </item><item><term> 
## SPCurveEdge</term><description> 
##  SP-Curve Edge </description> </item><item><term> 
## ForeignEdge</term><description> 
##  Foreign Edge </description> </item><item><term> 
## ConstantParameterEdge</term><description> 
##  Constant Parameter Edge </description> </item><item><term> 
## ConvergentEdge</term><description> 
##  Convergent Edge </description> </item><item><term> 
## ConvergentFacet</term><description> 
##  Convergent Facet </description> </item><item><term> 
## StagedModelStage</term><description> 
##  Staged Model Stage </description> </item><item><term> 
## StagedModelStageSet</term><description> 
##  Staged Model Stage Set </description> </item><item><term> 
## StructureDesignMemberCorner</term><description> 
##  The corner object between members in Structure Designer </description> </item><item><term> 
## TechnicalDataPackagePage</term><description> 
##  Technical Data Package Template Page </description> </item><item><term> 
## TechnicalDataPackageViewport</term><description> 
##  Technical Data Package Viewport </description> </item><item><term> 
## TechnicalDataPackageViewCarousel</term><description> 
##  Technical Data Package View Carousel </description> </item><item><term> 
## TechnicalDataPackageRectangle</term><description> 
##  Technical Data Package Template Rectangle </description> </item><item><term> 
## TechnicalDataPackagePDFFormField</term><description> 
##  Technical Data Package Template PDF Form Field </description> </item><item><term> 
## TechnicalDataPackageAutomaticTable</term><description> 
##  Technical Data Package Template Automatic Table </description> </item><item><term> 
## TechnicalDataPackageViewList</term><description> 
##  Technical Data Package Template View List </description> </item><item><term> 
## TechnicalDataPackagePrintView</term><description> 
##  Technical Data Package Template Print View </description> </item><item><term> 
## TechnicalDataPackageDiagramArea</term><description> 
##  Technical Data Package Template Diagram Area </description> </item><item><term> 
## AllViews</term><description> 
##  All views </description> </item><item><term> 
## SectionView</term><description> 
##  Drawing Section View </description> </item><item><term> 
## ImportedView</term><description> 
##  Drawing Imported View </description> </item><item><term> 
## OrthographicView</term><description> 
##  Drawing Orthographic View </description> </item><item><term> 
## AuxiliaryView</term><description> 
##  Drawing Auxiliary View </description> </item><item><term> 
## DetailView</term><description> 
##  Drawing Detail View </description> </item><item><term> 
## DrawingSheetView</term><description> 
##  Drawing Sheet View </description> </item><item><term> 
## ImportedPMILightweightSectionView</term><description> 
##  Drawing Imported PMI Lightweight Section View </description> </item><item><term> 
## AllBodyInWhiteDatums</term><description> 
##  Body in White Datum </description> </item><item><term> 
## AllWeldingObjects</term><description> 
##   Welding Objects </description> </item><item><term> 
## AllWeldingMeasurementObjects</term><description> 
##  Measurement Objects </description> </item><item><term> 
## GrooveWeld</term><description> 
##  Weld Groove feature </description> </item><item><term> 
## FilletWeld</term><description> 
##  Fillet Weld feature </description> </item><item><term> 
## ResistanceSpotWeld</term><description> 
##  Weld Point object of Resistance Spot type </description> </item><item><term> 
## ArcSpotWeld</term><description> 
##  Weld Point object of Arc Spot type </description> </item><item><term> 
## NutWeld</term><description> 
##  Weld Point object of Nut type </description> </item><item><term> 
## StudWeld</term><description> 
##  Weld Point object of Stud type </description> </item><item><term> 
## MechanicalClinchWeld</term><description> 
##  Weld Point object of Mechanical Clinch type </description> </item><item><term> 
## DollopWeld</term><description> 
##  Weld Point object of Dollop type </description> </item><item><term> 
## Custom1Weld</term><description> 
##  Weld Point object with no pre-defined type </description> </item><item><term> 
## Custom2Weld</term><description> 
##  Weld Point object with no pre-defined type </description> </item><item><term> 
## Custom3Weld</term><description> 
##  Weld Point object with no pre-defined type </description> </item><item><term> 
## Custom4Weld</term><description> 
##  Weld Point object with no pre-defined type </description> </item><item><term> 
## Custom5Weld</term><description> 
##  Weld Point object with no pre-defined type </description> </item><item><term> 
## UserDefinedWeld</term><description> 
##  User Defined Weld feature </description> </item><item><term> 
## FillWeld</term><description> 
##  Fill feature </description> </item><item><term> 
## WeldingJoint</term><description> 
##  Structure Welding Joint feature </description> </item><item><term> 
## WeldBead</term><description> 
##  Weld Bead feature </description> </item><item><term> 
## WeldPlugSlot</term><description> 
##  Weld Plug Slot feature </description> </item><item><term> 
## SurfaceWeld</term><description> 
##  Structure Welding Surface Weld feature </description> </item><item><term> 
## TranslateWeld</term><description> 
##  Weld Transform feature </description> </item><item><term> 
## JointMarkWeld</term><description> 
##  Joint Mark object </description> </item><item><term> 
## CompoundWeld</term><description> 
## Compound Weld  </description> </item><item><term> 
## DatumSurface</term><description> 
##  Datum Surface object </description> </item><item><term> 
## DatumPin</term><description> 
##  Datum Pin object </description> </item><item><term> 
## DatumCustom1</term><description> 
##  Weld Datum object with no pre-defined type </description> </item><item><term> 
## DatumCustom2</term><description> 
##  Weld Datum object with no pre-defined type </description> </item><item><term> 
## DatumCustom3</term><description> 
##  Weld Datum object with no pre-defined type </description> </item><item><term> 
## MeasurementSurface</term><description> 
##  Measurement Surface object </description> </item><item><term> 
## MeasurementHole</term><description> 
##  Measurement Hole object </description> </item><item><term> 
## MeasurementStud</term><description> 
##  Measurement Stud object </description> </item><item><term> 
## MeasurementSlot</term><description> 
##  Measurement Slot object </description> </item><item><term> 
## MeasurementTrim</term><description> 
##  Measurement Trim object </description> </item><item><term> 
## MeasurementHemmedEdge</term><description> 
##  Measurement Hemmed Edge object </description> </item><item><term> 
## MeasurementCustom1</term><description> 
##  Measurement object with no pre-defined type </description> </item><item><term> 
## MeasurementCustom2</term><description> 
##  Measurement object with no pre-defined type </description> </item><item><term> 
## MeasurementCustom3</term><description> 
##  Measurement object with no pre-defined type </description> </item><item><term> 
## AllConicCurves</term><description> 
##  Ellipse, Parabola, or Hyperbola </description> </item><item><term> 
## AllCurves</term><description> 
##  All types of Curves </description> </item><item><term> 
## Point</term><description> 
##  Point </description> </item><item><term> 
## PointCloud</term><description> 
##  Point Cloud </description> </item><item><term> 
## Line</term><description> 
## Line  </description> </item><item><term> 
## Arc</term><description> 
##  Arc or Circle </description> </item><item><term> 
## Ellipse</term><description> 
##  Ellipse </description> </item><item><term> 
## Parabola</term><description> 
##  Parabola </description> </item><item><term> 
## Hyperbola</term><description> 
##  Hyperbola </description> </item><item><term> 
## Spline</term><description> 
##  Spline </description> </item><item><term> 
## Polyline</term><description> 
##  Polyline </description> </item><item><term> 
## Stroke</term><description> 
##  A stroke represents a trail of points with speed information defined typically by a touch gesture </description> </item><item><term> 
## CompositesLaminate</term><description> 
##  Composites Laminate </description> </item><item><term> 
## CompositesPly</term><description> 
##  Composites Ply </description> </item><item><term> 
## AllCompositesObjects</term><description> 
##  All Composites Objects </description> </item><item><term> 
## AECGridLine</term><description> 
##  AEC grid line </description> </item><item><term> 
## AECLevelLine</term><description> 
## </description> </item><item><term> 
## AECSymbol</term><description> 
## </description> </item><item><term> 
## AECLineFormat</term><description> 
## </description> </item></list>
class FilterMember(Enum):
    """
    Members Include: <NotSet> <Group> <Pattern> <PatternPoint> <ProductDefinition> <ViewSet> <Field> <AllAnalyses> <DeviationGauge> <GridSectionAnalysis> <HighlightLinesAnalysis> <SurfaceContinuityAnalysis> <GapAndFlushnessAnalysis> <CurveContinuityAnalysis> <SectionAnalysis> <CurveAnalysis> <SurfaceIntersectionAnalysis> <DraftAnalysis> <TrimAngleCheck> <LocalRadiusAnalysis> <MoldFlowMoldx3dAnalysis> <WallThicknessAnalysis> <FaceCurvatureAnalysis> <FaceAnalysis> <SheetBoundaryAnalysis> <DistanceAnalysis> <RadiusAnalysis> <ReflectionAnalysis> <SlopeAnalysis> <AnimationDesignerAll> <AnimationDesignerRigidGroup> <AnimationDesignerContact> <AnimationDesignerJoint> <AnimationDesignerMotor> <AnimationDesignerCoupler> <AnimationDesignerMonitor> <AnimationDesignerAnimatedEffects> <AnimationDesignerJointJogger> <AnimationDesignerContainer> <AnimationDesignerFlexibleObject> <Component> <ComponentPattern> <AssemblyConstraint> <AssemblyConstraintGroup> <AutomationDesignerTerminalNode> <AutomationDesignerEPLANMacro> <AutomationDesignerAspect> <AutomationDesignerProgramBlock> <AutomationDesignerPageObject> <AutomationDesignerEngineeringObject> <AutomationDesignerVariable> <AutomationDesignerPlugNode> <AutomationDesignerNode> <AutomationDesignerTag> <AutomationDesignerCPU> <AutomationDesignerUserConstant> <AutomationDesignerStation> <AutomationDesignerPLCStation> <AutomationDesignerHardwareDevice> <AutomationDesignerHardwareItem> <AutomationDesignerLocalModuleFolder> <AutomationDesignerDistributedIOFolder> <AutomationDesignerUpstreamDataObject> <AutomationDesignerSymbol> <AutomationDesignerConnection> <AutomationDesignerConnectionPoint> <AutomationDesignerAnnotation> <AutomationDesignerTable> <AutomationDesignerAutomationUnassigned> <AutomationDesignerDocumentRoot> <AutomationDesignerDocumentStructureNode> <AutomationDesignerFragmentNode> <AutomationDesignerProduct> <AutomationDesignerProductComponent> <AutomationDesignerGroup> <AutomationDesignerQuery> <AutomationDesignerReportDefinition> <AutomationDesignerPLCTagsFolder> <AutomationDesignerEClass> <AutomationDesignerConnector> <AutomationDesignerUserPort> <AutomationDesignerPLCSubnet> <AutomationDesignerUdt> <AutomationDesignerBaseDefinitionNode> <AutomationDesignerSymbolStructureNode> <AutomationDesignerInterruptionPoint> <AutomationDesignerTagInterruptionPointNode> <AutomationDesignerRoot> <AutomationDesignerUnassigned> <AutomationDesignerProductTemplateLinkNode> <AutomationDesignerMemoryArea> <AutomationDesigner2DSymbols3DModels> <AutomationDesignerCableCore> <AutomationDesignerTagTable> <AutomationDesignerStationFolder> <AutomationDesignerRack> <AutomationDesignerConnectedDevice> <AutomationDesignerSymbolVariant> <AutomationDesignerViewPageNode> <AutomationDesignerBMECatVersionNode> <AutomationDesignerEClassVersionNode> <AutomationDesignerTemplateContent> <AllCAE> <CAEPolygonEdge> <CAEPolygonFace> <CAEPolygonBody> <CAEPolygonVertex> <CAELoad> <CAEConstraint> <CAESimulationObject> <CAEConnection> <CAEMeshPoint> <CAEEdgeDensity> <CAEFaceDensity> <CAEWeldRowDensity> <CAEMappedHoleDensity> <CAEFilletDensity> <CAECylinderDensity> <CAEPointDensity> <CAEBoundingVolumeDensity> <CAEMeshMating> <CAEEdgeSeparationCondition> <CAEBoundaryLayer> <CAESelectionRecipe> <CAECrackFaceCondition> <CAEFaceMatchControl> <CAEEdgeMatchControl> <CAEDOFSet> <CAEMesh> <CAETransientMesh> <CAESensor> <CAEResponseAnalysisStrainGauge> <CAEElement> <CAEElementEdge> <CAEElementFace> <CAENode> <CAEMarginCalculation> <CAELoadCaseSet> <CAEMarginSolution> <CAEFilteringSolution> <CAEFilteringCalculation> <CAEDurabilitySpecialistEvent> <CAELocalDefinition> <CAESpecialistSolution> <CAEFunctionDefinition> <CAECorrelationInput> <CAEVibrationInput> <CAERandomDataSource> <CAEDurabilitySpecialistStrainGauge> <CAEResultReference> <CAELayoutState> <CAEFemDataSet> <CAELoadRecipe> <CAEDataSource> <CAEDataProcessing> <CAEModelAndLoadPreprocessing> <CAEAcousticsAndVibrationSolution> <CAETransientMeshGroup> <CAEUniversalConnectionFolder> <CAEUniversalConnection> <CAESpotWeldConnection> <CAEAdhesiveConnection> <CAEBoltConnection> <CAESeamWeldConnection> <CAESealingConnection> <CAESpringConnection> <CAEDamperConnection> <CAERigidConnection> <CAEBushingConnection> <CAEKinematicConnection> <CAELumpedMass> <CAERivet> <CAEClinch> <CAECrimpConnection> <CAEBarConnection> <CAEBearingConnection> <CAELoadCaseFilteringSolution> <CAEStressLinearization> <CAEStressLinearizationManager> <CAEPostTransNode> <CAEPostTransElement> <CAEPostTransMesh> <CAEPostTransPolygonEdge> <CAEPostTransPolygonFace> <CAEPostTransComponent> <CAEFreeBody> <CAEResultProbe> <CAEPostTransElementFace> <CAEPostTransElementEdge> <CAEFreeBodyFolder> <CAEStressLinearizationFolder> <CAENoteConnection> <CoatingLayer> <CoatingStack> <LinearMaterial> <DatumAxis> <DatumPlane> <SectionSegment> <SectionLine> <CoordinateSystem> <Plane> <DatumPlaneGrid> <PlanarShipGrid> <Traceline> <Image> <ControlCage> <CageFace> <CageEdge> <CageVertex> <DesignMeshBody> <DesignMeshFace> <DesignMeshEdge> <DesignMeshVertex> <AllDimensions> <LinearDimension> <AngularDimension> <RadialDimension> <OrdinateDimension> <ChamferDimension> <ThicknessDimension> <ArcLengthDimension> <DimensionSet> <AllDrafting> <AllCenterlines> <AreaFill> <AllSymbols> <Note> <Label> <Balloon> <GDTSymbol> <Centerline> <FullCircularCenterline> <PartialCircularCenterline> <FullBoltCircle> <PartialBoltCircle> <CenterMark> <CylindricalCenterline> <SymmetricalCenterline> <Centerline2D> <Crosshatch> <Intersection> <TargetPoint> <UserDefinedSymbol> <OffsetCenterPoint> <LabelOnParent> <TitleBlock> <FrameBar> <Arrow> <CuttingPlaneSymbol> <ShipTic> <SupplementalGeometry> <ViewBreak> <DrawingTemplateRegion> <SurfaceFinish> <TabularNote> <DrawingImage> <Component2D> <ProductGrid> <EdgeConditionSymbol> <AllFacetBodies> <NormalFacetBody> <CloudFacetBody> <NXFacet> <AllBasicAndWeldFeatures> <AllBasicFeatures> <SolidFeature> <CurveFeature> <DatumPlaneFeature> <DatumAxisFeature> <DatumCoordinateSystemFeature> <SketchFeature> <HD3DMarkup> <HD3DMarkupElement> <AllJoinObjects> <JoinPoint> <JoinCurve> <JoinFace> <JoinHole> <LineDesignerConnector> <MachiningFeature> <MachiningToolPath> <MachiningInProcessWorkpiece> <AdditiveManufacturingSerialNumber> <AdditiveManufacturingPartGroup> <AdditiveManufacturingBuildTray> <AdditiveManufacturingPart> <AdditiveManufacturingPartOccurrence> <AdditiveManufacturingSupport> <AdditiveManufacturingSupportOccurrence> <AdditiveManufacturingPartRegion> <AdditiveManufacturingPartRegionOccurrence> <ManufacturingPlanningRigidGroup> <ManufacturingPlanningJoint> <MDCLogicalElement> <MDCConnectionElement> <MDCPortArtifact> <AllMechatronics> <MechatronicsJoint> <MechatronicsCollisionBody> <MechatronicsCollisionSensor> <MechatronicsRuntimeButton> <MechatronicsDistanceSensor> <Mechatronics2DLaserScanner> <MechatronicsLightCurtain> <MechatronicsPositionSensor> <MechatronicsVelocitySensor> <MechatronicsGenericSensor> <MechatronicsLimitSwitch> <MechatronicsRelay> <MechatronicsInclinometer> <MechatronicsAccelerometer> <MechatronicsPneumaticCylinder> <MechatronicsPneumaticValve> <MechatronicsHydraulicCylinder> <MechatronicsHydraulicValve> <MechatronicsRigidBody> <MechatronicsConstraint> <MechatronicsTransportSurface> <MechatronicsObjectSource> <MechatronicsObjectSink> <MechatronicsObjectTransformer> <MechatronicsObjectBehavior> <MechatronicsObjectData> <MechatronicsProxyObject> <MechatronicsSignal> <MechatronicsSnapPoint> <MechatronicsDynamicMaterial> <AllMotionSim> <AllMotionSimForceObjects> <AllMotionSimJoints> <MotionSimRoad> <MotionSimBearing> <MotionSimBearingProperty> <MotionSimControlPort> <MotionSimControlInput> <MotionSimPathFollower> <MotionSimControlOperation> <MotionSimControlOutput> <MotionSimGear> <MotionSimGearContact> <MotionSimAnimation> <MotionSimGraph> <MotionSimMlpp> <MotionSimCurveOperationRecord> <MotionSimMotionBodyDriver> <MotionSimLoadTransfer> <MotionSimJointDriver> <MotionSimStandaloneDriver> <MotionSimMechatronics> <MotionSimProfile> <MotionSimDiscreteDrivetrain> <MotionSimAnimationCamera> <MotionSimAutoflexProperty> <MotionSimBasicTireProperty> <MotionSimMotorcycleTireProperty> <MotionSimNonInertialTireProperty> <MotionSimFTireProperty> <MotionSimCDTireProperty> <MotionSimMFTyreAndMFSwiftTireProperty> <MotionSimTire> <MotionSimVehicleReporting> <MotionSimSuspensionReporting> <MotionSimInitialCondition> <MotionSimAnalyticalContact> <MotionSimAnalyticalContactProperty> <MotionSimSpring> <MotionSimRotationalSpring> <MotionSimTranslationalSpring> <MotionSimDamper> <MotionSimRotationalDamper> <MotionSimTranslationalDamper> <MotionSimSpringDamper> <MotionSimRotationalSpringDamper> <MotionSimTranslationalSpringDamper> <MotionSimSplineBeam> <MotionSimSplineBeamProperty> <MotionSimBeamSection> <MotionSimBeamForce> <MotionSimUserDefinedForce> <MotionSimFriction> <MotionSimThreePointForce> <MotionSimThreePointTorque> <MotionSimSubmechanism> <MotionSimSubmechanismPositioner> <MotionSimMotionConstraint> <MotionSimMotionBody> <MotionSimScalarForce> <MotionSimFlexibleBody> <MotionSimMarker> <MotionSimScalarTorque> <MotionSimCurveCurveContact> <MotionSimContact> <MotionSimBushing> <MotionSimBushingProperty> <MotionSimVectorForce> <MotionSimVectorTorque> <MotionSimSensor> <MotionSimMotor> <MotionSimMotionVector> <MotionSimMeasure> <MotionSimTrace> <MotionSimInterference> <MotionSimFixedJoint> <MotionSimScrewJoint> <MotionSimRevoluteJoint> <MotionSimSliderJoint> <MotionSimCylinderJoint> <MotionSimUniversalJoint> <MotionSimSphericalJoint> <MotionSimPlanarJoint> <MotionSimGearJoint> <MotionSimRackAndPinion> <MotionSimPointOnCurve> <MotionSimCurveOnCurve> <MotionSimCable> <MotionSimConstantVelocity> <MotionSimAtpointJoint> <MotionSimInlineJoint> <MotionSimInplaneJoint> <MotionSimOrientationJoint> <MotionSimParallelJoint> <MotionSimPerpendicularJoint> <MotionSimGeneralCoupler> <MotionSimMotionBodyCoupler> <MotionSimPlantInput> <MotionSimPlantOutput> <MotionSimSolutionStop> <MotionSimSignalChart> <MotionSimSolution> <MotionSimGearSpur> <MotionSimGearHelical> <MotionSimGearStraightBevel> <MotionSimGearSpiralBevel> <MotionSimGearHypoid> <MotionSimBumpStop> <MotionSimCompoundJoint> <MotionSimAnimationVector> <MotionSimHydrodynamicBearing> <MotionSimSprungMass> <MotionSimDiscreteDrivetrainReport> <MotionSimElectromagneticForce> <MotionSimGeneralSensor> <MotionSimContactPattern> <MotionSimFlexModalContent> <MotionSimFixedJointDriver> <MotionSimFrfInput> <MotionSimFrfOutput> <PhysicalDiagrammingAnnotation> <PhysicalDiagrammingConnection> <PhysicalDiagrammingNode> <BoundaryNode> <PIDAnnotation> <PIDConnection> <PIDSymbol> <PIDRun> <PIDBranch> <PIDSheet> <PIDSystem> <PressLineSimulationLineComponent> <PressLineSimulationPressModelRoot> <AllRoutingObjects> <RoutingControlPoint> <RoutingPort> <RoutingPartAnchor> <RoutingSegment> <RoutingStock> <AllShip> <AllShipPlateSystem> <AllShipProfileSystem> <ShipHull> <ShipDeck> <ShipTransverseBulkhead> <ShipLongitudinalBulkhead> <ShipGenericPlateSystem> <ShipStiffenerSystem> <ShipPillarSystem> <ShipEdgeReinforcement> <ShipSeam> <SketchRelation> <Sketch> <SketchFoundRelation> <SketchCoincidentRelation> <SketchConcentricRelation> <SketchPointOnCurveRelation> <SketchCollinearRelation> <SketchHorizontalRelation> <SketchHorizontalAlignmentRelation> <SketchVerticalRelation> <SketchVerticalAlignmentRelation> <SketchTangentRelation> <SketchParallelRelation> <SketchPerpendicularRelation> <SketchEqualLengthRelation> <SketchEqualRadiusRelation> <SketchSymmetricRelation> <SketchMidpointRelation> <SketchPointOnStringRelation> <SketchTangentToStringRelation> <SketchPerpendicularToStringRelation> <SketchUniformScaleRelation> <SketchG1SplineRelation> <SketchG2SplineRelation> <SketchTrimRelation> <SketchOffsetRelation> <SketchLinearPatternRelation> <SketchRectangularPatternRelation> <SketchCircularPatternRelation> <SketchGeneralPatternRelation> <SketchMirrorRelation> <SketchPolygonRelation> <SketchRigidGroupRelation> <SketchScalableGroupRelation> <SketchIgnoredRelation> <AllEdges> <AllFaces> <AllSolidBodies> <AllSheetBodies> <ConvergentSolidBody> <ConvergentSheetBody> <PlanarFace> <CylindricalFace> <ConicalFace> <SphericalFace> <ToroidalFace> <ParametricFace> <BlendedFace> <OffsetFace> <ExtrudedFace> <RevolvedFace> <ForeignFace> <ConvergentFace> <LinearEdge> <CircularEdge> <EllipticalEdge> <IntersectionEdge> <SplineEdge> <SPCurveEdge> <ForeignEdge> <ConstantParameterEdge> <ConvergentEdge> <ConvergentFacet> <StagedModelStage> <StagedModelStageSet> <StructureDesignMemberCorner> <TechnicalDataPackagePage> <TechnicalDataPackageViewport> <TechnicalDataPackageViewCarousel> <TechnicalDataPackageRectangle> <TechnicalDataPackagePDFFormField> <TechnicalDataPackageAutomaticTable> <TechnicalDataPackageViewList> <TechnicalDataPackagePrintView> <TechnicalDataPackageDiagramArea> <AllViews> <SectionView> <ImportedView> <OrthographicView> <AuxiliaryView> <DetailView> <DrawingSheetView> <ImportedPMILightweightSectionView> <AllBodyInWhiteDatums> <AllWeldingObjects> <AllWeldingMeasurementObjects> <GrooveWeld> <FilletWeld> <ResistanceSpotWeld> <ArcSpotWeld> <NutWeld> <StudWeld> <MechanicalClinchWeld> <DollopWeld> <Custom1Weld> <Custom2Weld> <Custom3Weld> <Custom4Weld> <Custom5Weld> <UserDefinedWeld> <FillWeld> <WeldingJoint> <WeldBead> <WeldPlugSlot> <SurfaceWeld> <TranslateWeld> <JointMarkWeld> <CompoundWeld> <DatumSurface> <DatumPin> <DatumCustom1> <DatumCustom2> <DatumCustom3> <MeasurementSurface> <MeasurementHole> <MeasurementStud> <MeasurementSlot> <MeasurementTrim> <MeasurementHemmedEdge> <MeasurementCustom1> <MeasurementCustom2> <MeasurementCustom3> <AllConicCurves> <AllCurves> <Point> <PointCloud> <Line> <Arc> <Ellipse> <Parabola> <Hyperbola> <Spline> <Polyline> <Stroke> <CompositesLaminate> <CompositesPly> <AllCompositesObjects> <AECGridLine> <AECLevelLine> <AECSymbol> <AECLineFormat>
    """
    NotSet: int
    Group: int
    Pattern: int
    PatternPoint: int
    ProductDefinition: int
    ViewSet: int
    Field: int
    AllAnalyses: int
    DeviationGauge: int
    GridSectionAnalysis: int
    HighlightLinesAnalysis: int
    SurfaceContinuityAnalysis: int
    GapAndFlushnessAnalysis: int
    CurveContinuityAnalysis: int
    SectionAnalysis: int
    CurveAnalysis: int
    SurfaceIntersectionAnalysis: int
    DraftAnalysis: int
    TrimAngleCheck: int
    LocalRadiusAnalysis: int
    MoldFlowMoldx3dAnalysis: int
    WallThicknessAnalysis: int
    FaceCurvatureAnalysis: int
    FaceAnalysis: int
    SheetBoundaryAnalysis: int
    DistanceAnalysis: int
    RadiusAnalysis: int
    ReflectionAnalysis: int
    SlopeAnalysis: int
    AnimationDesignerAll: int
    AnimationDesignerRigidGroup: int
    AnimationDesignerContact: int
    AnimationDesignerJoint: int
    AnimationDesignerMotor: int
    AnimationDesignerCoupler: int
    AnimationDesignerMonitor: int
    AnimationDesignerAnimatedEffects: int
    AnimationDesignerJointJogger: int
    AnimationDesignerContainer: int
    AnimationDesignerFlexibleObject: int
    Component: int
    ComponentPattern: int
    AssemblyConstraint: int
    AssemblyConstraintGroup: int
    AutomationDesignerTerminalNode: int
    AutomationDesignerEPLANMacro: int
    AutomationDesignerAspect: int
    AutomationDesignerProgramBlock: int
    AutomationDesignerPageObject: int
    AutomationDesignerEngineeringObject: int
    AutomationDesignerVariable: int
    AutomationDesignerPlugNode: int
    AutomationDesignerNode: int
    AutomationDesignerTag: int
    AutomationDesignerCPU: int
    AutomationDesignerUserConstant: int
    AutomationDesignerStation: int
    AutomationDesignerPLCStation: int
    AutomationDesignerHardwareDevice: int
    AutomationDesignerHardwareItem: int
    AutomationDesignerLocalModuleFolder: int
    AutomationDesignerDistributedIOFolder: int
    AutomationDesignerUpstreamDataObject: int
    AutomationDesignerSymbol: int
    AutomationDesignerConnection: int
    AutomationDesignerConnectionPoint: int
    AutomationDesignerAnnotation: int
    AutomationDesignerTable: int
    AutomationDesignerAutomationUnassigned: int
    AutomationDesignerDocumentRoot: int
    AutomationDesignerDocumentStructureNode: int
    AutomationDesignerFragmentNode: int
    AutomationDesignerProduct: int
    AutomationDesignerProductComponent: int
    AutomationDesignerGroup: int
    AutomationDesignerQuery: int
    AutomationDesignerReportDefinition: int
    AutomationDesignerPLCTagsFolder: int
    AutomationDesignerEClass: int
    AutomationDesignerConnector: int
    AutomationDesignerUserPort: int
    AutomationDesignerPLCSubnet: int
    AutomationDesignerUdt: int
    AutomationDesignerBaseDefinitionNode: int
    AutomationDesignerSymbolStructureNode: int
    AutomationDesignerInterruptionPoint: int
    AutomationDesignerTagInterruptionPointNode: int
    AutomationDesignerRoot: int
    AutomationDesignerUnassigned: int
    AutomationDesignerProductTemplateLinkNode: int
    AutomationDesignerMemoryArea: int
    AutomationDesigner2DSymbols3DModels: int
    AutomationDesignerCableCore: int
    AutomationDesignerTagTable: int
    AutomationDesignerStationFolder: int
    AutomationDesignerRack: int
    AutomationDesignerConnectedDevice: int
    AutomationDesignerSymbolVariant: int
    AutomationDesignerViewPageNode: int
    AutomationDesignerBMECatVersionNode: int
    AutomationDesignerEClassVersionNode: int
    AutomationDesignerTemplateContent: int
    AllCAE: int
    CAEPolygonEdge: int
    CAEPolygonFace: int
    CAEPolygonBody: int
    CAEPolygonVertex: int
    CAELoad: int
    CAEConstraint: int
    CAESimulationObject: int
    CAEConnection: int
    CAEMeshPoint: int
    CAEEdgeDensity: int
    CAEFaceDensity: int
    CAEWeldRowDensity: int
    CAEMappedHoleDensity: int
    CAEFilletDensity: int
    CAECylinderDensity: int
    CAEPointDensity: int
    CAEBoundingVolumeDensity: int
    CAEMeshMating: int
    CAEEdgeSeparationCondition: int
    CAEBoundaryLayer: int
    CAESelectionRecipe: int
    CAECrackFaceCondition: int
    CAEFaceMatchControl: int
    CAEEdgeMatchControl: int
    CAEDOFSet: int
    CAEMesh: int
    CAETransientMesh: int
    CAESensor: int
    CAEResponseAnalysisStrainGauge: int
    CAEElement: int
    CAEElementEdge: int
    CAEElementFace: int
    CAENode: int
    CAEMarginCalculation: int
    CAELoadCaseSet: int
    CAEMarginSolution: int
    CAEFilteringSolution: int
    CAEFilteringCalculation: int
    CAEDurabilitySpecialistEvent: int
    CAELocalDefinition: int
    CAESpecialistSolution: int
    CAEFunctionDefinition: int
    CAECorrelationInput: int
    CAEVibrationInput: int
    CAERandomDataSource: int
    CAEDurabilitySpecialistStrainGauge: int
    CAEResultReference: int
    CAELayoutState: int
    CAEFemDataSet: int
    CAELoadRecipe: int
    CAEDataSource: int
    CAEDataProcessing: int
    CAEModelAndLoadPreprocessing: int
    CAEAcousticsAndVibrationSolution: int
    CAETransientMeshGroup: int
    CAEUniversalConnectionFolder: int
    CAEUniversalConnection: int
    CAESpotWeldConnection: int
    CAEAdhesiveConnection: int
    CAEBoltConnection: int
    CAESeamWeldConnection: int
    CAESealingConnection: int
    CAESpringConnection: int
    CAEDamperConnection: int
    CAERigidConnection: int
    CAEBushingConnection: int
    CAEKinematicConnection: int
    CAELumpedMass: int
    CAERivet: int
    CAEClinch: int
    CAECrimpConnection: int
    CAEBarConnection: int
    CAEBearingConnection: int
    CAELoadCaseFilteringSolution: int
    CAEStressLinearization: int
    CAEStressLinearizationManager: int
    CAEPostTransNode: int
    CAEPostTransElement: int
    CAEPostTransMesh: int
    CAEPostTransPolygonEdge: int
    CAEPostTransPolygonFace: int
    CAEPostTransComponent: int
    CAEFreeBody: int
    CAEResultProbe: int
    CAEPostTransElementFace: int
    CAEPostTransElementEdge: int
    CAEFreeBodyFolder: int
    CAEStressLinearizationFolder: int
    CAENoteConnection: int
    CoatingLayer: int
    CoatingStack: int
    LinearMaterial: int
    DatumAxis: int
    DatumPlane: int
    SectionSegment: int
    SectionLine: int
    CoordinateSystem: int
    Plane: int
    DatumPlaneGrid: int
    PlanarShipGrid: int
    Traceline: int
    Image: int
    ControlCage: int
    CageFace: int
    CageEdge: int
    CageVertex: int
    DesignMeshBody: int
    DesignMeshFace: int
    DesignMeshEdge: int
    DesignMeshVertex: int
    AllDimensions: int
    LinearDimension: int
    AngularDimension: int
    RadialDimension: int
    OrdinateDimension: int
    ChamferDimension: int
    ThicknessDimension: int
    ArcLengthDimension: int
    DimensionSet: int
    AllDrafting: int
    AllCenterlines: int
    AreaFill: int
    AllSymbols: int
    Note: int
    Label: int
    Balloon: int
    GDTSymbol: int
    Centerline: int
    FullCircularCenterline: int
    PartialCircularCenterline: int
    FullBoltCircle: int
    PartialBoltCircle: int
    CenterMark: int
    CylindricalCenterline: int
    SymmetricalCenterline: int
    Centerline2D: int
    Crosshatch: int
    Intersection: int
    TargetPoint: int
    UserDefinedSymbol: int
    OffsetCenterPoint: int
    LabelOnParent: int
    TitleBlock: int
    FrameBar: int
    Arrow: int
    CuttingPlaneSymbol: int
    ShipTic: int
    SupplementalGeometry: int
    ViewBreak: int
    DrawingTemplateRegion: int
    SurfaceFinish: int
    TabularNote: int
    DrawingImage: int
    Component2D: int
    ProductGrid: int
    EdgeConditionSymbol: int
    AllFacetBodies: int
    NormalFacetBody: int
    CloudFacetBody: int
    NXFacet: int
    AllBasicAndWeldFeatures: int
    AllBasicFeatures: int
    SolidFeature: int
    CurveFeature: int
    DatumPlaneFeature: int
    DatumAxisFeature: int
    DatumCoordinateSystemFeature: int
    SketchFeature: int
    HD3DMarkup: int
    HD3DMarkupElement: int
    AllJoinObjects: int
    JoinPoint: int
    JoinCurve: int
    JoinFace: int
    JoinHole: int
    LineDesignerConnector: int
    MachiningFeature: int
    MachiningToolPath: int
    MachiningInProcessWorkpiece: int
    AdditiveManufacturingSerialNumber: int
    AdditiveManufacturingPartGroup: int
    AdditiveManufacturingBuildTray: int
    AdditiveManufacturingPart: int
    AdditiveManufacturingPartOccurrence: int
    AdditiveManufacturingSupport: int
    AdditiveManufacturingSupportOccurrence: int
    AdditiveManufacturingPartRegion: int
    AdditiveManufacturingPartRegionOccurrence: int
    ManufacturingPlanningRigidGroup: int
    ManufacturingPlanningJoint: int
    MDCLogicalElement: int
    MDCConnectionElement: int
    MDCPortArtifact: int
    AllMechatronics: int
    MechatronicsJoint: int
    MechatronicsCollisionBody: int
    MechatronicsCollisionSensor: int
    MechatronicsRuntimeButton: int
    MechatronicsDistanceSensor: int
    Mechatronics2DLaserScanner: int
    MechatronicsLightCurtain: int
    MechatronicsPositionSensor: int
    MechatronicsVelocitySensor: int
    MechatronicsGenericSensor: int
    MechatronicsLimitSwitch: int
    MechatronicsRelay: int
    MechatronicsInclinometer: int
    MechatronicsAccelerometer: int
    MechatronicsPneumaticCylinder: int
    MechatronicsPneumaticValve: int
    MechatronicsHydraulicCylinder: int
    MechatronicsHydraulicValve: int
    MechatronicsRigidBody: int
    MechatronicsConstraint: int
    MechatronicsTransportSurface: int
    MechatronicsObjectSource: int
    MechatronicsObjectSink: int
    MechatronicsObjectTransformer: int
    MechatronicsObjectBehavior: int
    MechatronicsObjectData: int
    MechatronicsProxyObject: int
    MechatronicsSignal: int
    MechatronicsSnapPoint: int
    MechatronicsDynamicMaterial: int
    AllMotionSim: int
    AllMotionSimForceObjects: int
    AllMotionSimJoints: int
    MotionSimRoad: int
    MotionSimBearing: int
    MotionSimBearingProperty: int
    MotionSimControlPort: int
    MotionSimControlInput: int
    MotionSimPathFollower: int
    MotionSimControlOperation: int
    MotionSimControlOutput: int
    MotionSimGear: int
    MotionSimGearContact: int
    MotionSimAnimation: int
    MotionSimGraph: int
    MotionSimMlpp: int
    MotionSimCurveOperationRecord: int
    MotionSimMotionBodyDriver: int
    MotionSimLoadTransfer: int
    MotionSimJointDriver: int
    MotionSimStandaloneDriver: int
    MotionSimMechatronics: int
    MotionSimProfile: int
    MotionSimDiscreteDrivetrain: int
    MotionSimAnimationCamera: int
    MotionSimAutoflexProperty: int
    MotionSimBasicTireProperty: int
    MotionSimMotorcycleTireProperty: int
    MotionSimNonInertialTireProperty: int
    MotionSimFTireProperty: int
    MotionSimCDTireProperty: int
    MotionSimMFTyreAndMFSwiftTireProperty: int
    MotionSimTire: int
    MotionSimVehicleReporting: int
    MotionSimSuspensionReporting: int
    MotionSimInitialCondition: int
    MotionSimAnalyticalContact: int
    MotionSimAnalyticalContactProperty: int
    MotionSimSpring: int
    MotionSimRotationalSpring: int
    MotionSimTranslationalSpring: int
    MotionSimDamper: int
    MotionSimRotationalDamper: int
    MotionSimTranslationalDamper: int
    MotionSimSpringDamper: int
    MotionSimRotationalSpringDamper: int
    MotionSimTranslationalSpringDamper: int
    MotionSimSplineBeam: int
    MotionSimSplineBeamProperty: int
    MotionSimBeamSection: int
    MotionSimBeamForce: int
    MotionSimUserDefinedForce: int
    MotionSimFriction: int
    MotionSimThreePointForce: int
    MotionSimThreePointTorque: int
    MotionSimSubmechanism: int
    MotionSimSubmechanismPositioner: int
    MotionSimMotionConstraint: int
    MotionSimMotionBody: int
    MotionSimScalarForce: int
    MotionSimFlexibleBody: int
    MotionSimMarker: int
    MotionSimScalarTorque: int
    MotionSimCurveCurveContact: int
    MotionSimContact: int
    MotionSimBushing: int
    MotionSimBushingProperty: int
    MotionSimVectorForce: int
    MotionSimVectorTorque: int
    MotionSimSensor: int
    MotionSimMotor: int
    MotionSimMotionVector: int
    MotionSimMeasure: int
    MotionSimTrace: int
    MotionSimInterference: int
    MotionSimFixedJoint: int
    MotionSimScrewJoint: int
    MotionSimRevoluteJoint: int
    MotionSimSliderJoint: int
    MotionSimCylinderJoint: int
    MotionSimUniversalJoint: int
    MotionSimSphericalJoint: int
    MotionSimPlanarJoint: int
    MotionSimGearJoint: int
    MotionSimRackAndPinion: int
    MotionSimPointOnCurve: int
    MotionSimCurveOnCurve: int
    MotionSimCable: int
    MotionSimConstantVelocity: int
    MotionSimAtpointJoint: int
    MotionSimInlineJoint: int
    MotionSimInplaneJoint: int
    MotionSimOrientationJoint: int
    MotionSimParallelJoint: int
    MotionSimPerpendicularJoint: int
    MotionSimGeneralCoupler: int
    MotionSimMotionBodyCoupler: int
    MotionSimPlantInput: int
    MotionSimPlantOutput: int
    MotionSimSolutionStop: int
    MotionSimSignalChart: int
    MotionSimSolution: int
    MotionSimGearSpur: int
    MotionSimGearHelical: int
    MotionSimGearStraightBevel: int
    MotionSimGearSpiralBevel: int
    MotionSimGearHypoid: int
    MotionSimBumpStop: int
    MotionSimCompoundJoint: int
    MotionSimAnimationVector: int
    MotionSimHydrodynamicBearing: int
    MotionSimSprungMass: int
    MotionSimDiscreteDrivetrainReport: int
    MotionSimElectromagneticForce: int
    MotionSimGeneralSensor: int
    MotionSimContactPattern: int
    MotionSimFlexModalContent: int
    MotionSimFixedJointDriver: int
    MotionSimFrfInput: int
    MotionSimFrfOutput: int
    PhysicalDiagrammingAnnotation: int
    PhysicalDiagrammingConnection: int
    PhysicalDiagrammingNode: int
    BoundaryNode: int
    PIDAnnotation: int
    PIDConnection: int
    PIDSymbol: int
    PIDRun: int
    PIDBranch: int
    PIDSheet: int
    PIDSystem: int
    PressLineSimulationLineComponent: int
    PressLineSimulationPressModelRoot: int
    AllRoutingObjects: int
    RoutingControlPoint: int
    RoutingPort: int
    RoutingPartAnchor: int
    RoutingSegment: int
    RoutingStock: int
    AllShip: int
    AllShipPlateSystem: int
    AllShipProfileSystem: int
    ShipHull: int
    ShipDeck: int
    ShipTransverseBulkhead: int
    ShipLongitudinalBulkhead: int
    ShipGenericPlateSystem: int
    ShipStiffenerSystem: int
    ShipPillarSystem: int
    ShipEdgeReinforcement: int
    ShipSeam: int
    SketchRelation: int
    Sketch: int
    SketchFoundRelation: int
    SketchCoincidentRelation: int
    SketchConcentricRelation: int
    SketchPointOnCurveRelation: int
    SketchCollinearRelation: int
    SketchHorizontalRelation: int
    SketchHorizontalAlignmentRelation: int
    SketchVerticalRelation: int
    SketchVerticalAlignmentRelation: int
    SketchTangentRelation: int
    SketchParallelRelation: int
    SketchPerpendicularRelation: int
    SketchEqualLengthRelation: int
    SketchEqualRadiusRelation: int
    SketchSymmetricRelation: int
    SketchMidpointRelation: int
    SketchPointOnStringRelation: int
    SketchTangentToStringRelation: int
    SketchPerpendicularToStringRelation: int
    SketchUniformScaleRelation: int
    SketchG1SplineRelation: int
    SketchG2SplineRelation: int
    SketchTrimRelation: int
    SketchOffsetRelation: int
    SketchLinearPatternRelation: int
    SketchRectangularPatternRelation: int
    SketchCircularPatternRelation: int
    SketchGeneralPatternRelation: int
    SketchMirrorRelation: int
    SketchPolygonRelation: int
    SketchRigidGroupRelation: int
    SketchScalableGroupRelation: int
    SketchIgnoredRelation: int
    AllEdges: int
    AllFaces: int
    AllSolidBodies: int
    AllSheetBodies: int
    ConvergentSolidBody: int
    ConvergentSheetBody: int
    PlanarFace: int
    CylindricalFace: int
    ConicalFace: int
    SphericalFace: int
    ToroidalFace: int
    ParametricFace: int
    BlendedFace: int
    OffsetFace: int
    ExtrudedFace: int
    RevolvedFace: int
    ForeignFace: int
    ConvergentFace: int
    LinearEdge: int
    CircularEdge: int
    EllipticalEdge: int
    IntersectionEdge: int
    SplineEdge: int
    SPCurveEdge: int
    ForeignEdge: int
    ConstantParameterEdge: int
    ConvergentEdge: int
    ConvergentFacet: int
    StagedModelStage: int
    StagedModelStageSet: int
    StructureDesignMemberCorner: int
    TechnicalDataPackagePage: int
    TechnicalDataPackageViewport: int
    TechnicalDataPackageViewCarousel: int
    TechnicalDataPackageRectangle: int
    TechnicalDataPackagePDFFormField: int
    TechnicalDataPackageAutomaticTable: int
    TechnicalDataPackageViewList: int
    TechnicalDataPackagePrintView: int
    TechnicalDataPackageDiagramArea: int
    AllViews: int
    SectionView: int
    ImportedView: int
    OrthographicView: int
    AuxiliaryView: int
    DetailView: int
    DrawingSheetView: int
    ImportedPMILightweightSectionView: int
    AllBodyInWhiteDatums: int
    AllWeldingObjects: int
    AllWeldingMeasurementObjects: int
    GrooveWeld: int
    FilletWeld: int
    ResistanceSpotWeld: int
    ArcSpotWeld: int
    NutWeld: int
    StudWeld: int
    MechanicalClinchWeld: int
    DollopWeld: int
    Custom1Weld: int
    Custom2Weld: int
    Custom3Weld: int
    Custom4Weld: int
    Custom5Weld: int
    UserDefinedWeld: int
    FillWeld: int
    WeldingJoint: int
    WeldBead: int
    WeldPlugSlot: int
    SurfaceWeld: int
    TranslateWeld: int
    JointMarkWeld: int
    CompoundWeld: int
    DatumSurface: int
    DatumPin: int
    DatumCustom1: int
    DatumCustom2: int
    DatumCustom3: int
    MeasurementSurface: int
    MeasurementHole: int
    MeasurementStud: int
    MeasurementSlot: int
    MeasurementTrim: int
    MeasurementHemmedEdge: int
    MeasurementCustom1: int
    MeasurementCustom2: int
    MeasurementCustom3: int
    AllConicCurves: int
    AllCurves: int
    Point: int
    PointCloud: int
    Line: int
    Arc: int
    Ellipse: int
    Parabola: int
    Hyperbola: int
    Spline: int
    Polyline: int
    Stroke: int
    CompositesLaminate: int
    CompositesPly: int
    AllCompositesObjects: int
    AECGridLine: int
    AECLevelLine: int
    AECSymbol: int
    AECLineFormat: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> FilterMember:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


## @package NXOpen.Select
## Classes, Enums and Structs under NXOpen.Select namespace


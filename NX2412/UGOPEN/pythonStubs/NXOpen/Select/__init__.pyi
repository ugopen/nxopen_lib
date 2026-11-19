from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
class FilterMember(Enum):
    """
    Members Include: 
     |NotSet|  No filter. Should not be used. 
     |Group|  Group 
     |Pattern|  Pattern 
     |PatternPoint|  Pattern Point 
     |ProductDefinition|  Product Definition 
     |ViewSet|  View Set 
     |Field|  Field tables, formulas, etc. 
     |AllAnalyses|  All Analyses 
     |DeviationGauge|  Deviation Gauge 
     |GridSectionAnalysis|  Grid Section Analysis 
     |HighlightLinesAnalysis|  Highlight Lines Analysis 
     |SurfaceContinuityAnalysis|  Surface Continuity Analysis 
     |GapAndFlushnessAnalysis|  Gap and Flushness Analysis 
     |CurveContinuityAnalysis|  Curve Continuity Analysis 
     |SectionAnalysis|  Section Analysis 
     |CurveAnalysis|  Curve Analysis 
     |SurfaceIntersectionAnalysis|  Surface Intersection Analysis 
     |DraftAnalysis|  Draft Analysis 
     |TrimAngleCheck|  Trim Angle Check 
     |LocalRadiusAnalysis|  Local Radius Analysis 
     |MoldFlowMoldx3dAnalysis|  Mold Flow moldx3d Analysis 
     |WallThicknessAnalysis|  Wall Thickness Analysis 
     |FaceCurvatureAnalysis|  Face Curvature 
     |FaceAnalysis|  Face Analysis 
     |SheetBoundaryAnalysis|  Sheet Boundary Analysis 
     |DistanceAnalysis|  Distance Analysis 
     |RadiusAnalysis|  Radius Analysis 
     |ReflectionAnalysis|  Reflection Analysis 
     |SlopeAnalysis|  Slope Analysis 
     |AnimationDesignerAll|  All objects in Animation Designer 
     |AnimationDesignerRigidGroup|  The rigid group of objects or components for an animation 
     |AnimationDesignerContact|  The contact on objects to prevent interference between them during the animation 
     |AnimationDesignerJoint|  The joint relationship between rigid groups 
     |AnimationDesignerMotor|  The driver on joint 
     |AnimationDesignerCoupler|  The coupler relationship between joints 
     |AnimationDesignerMonitor|  The monitor of motor parameters, distance or angle between geometries during the animation 
     |AnimationDesignerAnimatedEffects|  The animated effects such as visibility, explode, camera, color during the animation 
     |AnimationDesignerJointJogger|  The jog of joints during the animation 
     |AnimationDesignerContainer|  The container of objects in navigator 
     |AnimationDesignerFlexibleObject|  The flexible objects for an animation 
     |Component|  Component 
     |ComponentPattern|  Component Pattern 
     |AssemblyConstraint|  Assembly Constraint 
     |AssemblyConstraintGroup|  Assembly Constraint Group 
     |AutomationDesignerTerminalNode|  Terminal node in Product Aspect Navigator 
     |AutomationDesignerEPLANMacro|  EPLAN Macro 
     |AutomationDesignerAspect|  Aspect node 
     |AutomationDesignerProgramBlock|  Software Element 
     |AutomationDesignerPageObject|  Page node Object 
     |AutomationDesignerEngineeringObject|  Engineering Object 
     |AutomationDesignerVariable|  Interface Variable 
     |AutomationDesignerPlugNode|  Plug and Plug-Chamber Nodes in Product Aspect Navigator 
     |AutomationDesignerNode|  Base Node 
     |AutomationDesignerTag|  Tag 
     |AutomationDesignerCPU|  CPU 
     |AutomationDesignerUserConstant|  Plc Constant 
     |AutomationDesignerStation|  Plc Station 
     |AutomationDesignerPLCStation|  Station 
     |AutomationDesignerHardwareDevice|  Module 
     |AutomationDesignerHardwareItem|  Hardware Item 
     |AutomationDesignerLocalModuleFolder|  Local Module Folder 
     |AutomationDesignerDistributedIOFolder|  Distributed IO Folder 
     |AutomationDesignerUpstreamDataObject|  Excel Import Object 
     |AutomationDesignerSymbol|  Diagramming node 
     |AutomationDesignerConnection|  Connection object 
     |AutomationDesignerConnectionPoint|  Connection Point 
     |AutomationDesignerAnnotation|  Annotation 
     |AutomationDesignerTable|  Diagramming Table 
     |AutomationDesignerAutomationUnassigned|  Unassigned Node in Automation Navigator 
     |AutomationDesignerDocumentRoot|  Root node in Document Navigator 
     |AutomationDesignerDocumentStructureNode|  Document Structure Node 
     |AutomationDesignerFragmentNode|  Fragment Object Node 
     |AutomationDesignerProduct|  Product 
     |AutomationDesignerProductComponent|  Product Component created from Type 
     |AutomationDesignerGroup|  Group node 
     |AutomationDesignerQuery|  Query node 
     |AutomationDesignerReportDefinition|  Report definition node 
     |AutomationDesignerPLCTagsFolder|  Obsolete: Do Not Use 
     |AutomationDesignerEClass|  EClass Node 
     |AutomationDesignerConnector|  Physical Port 
     |AutomationDesignerUserPort|  User Port 
     |AutomationDesignerPLCSubnet|  PLC Subnet node 
     |AutomationDesignerUdt|  User defined data type 
     |AutomationDesignerBaseDefinitionNode|  Aspect and Product Definition node  
     |AutomationDesignerSymbolStructureNode|  Symbol Structure Node 
     |AutomationDesignerInterruptionPoint|  Interruption Point 
     |AutomationDesignerTagInterruptionPointNode|  Interruption Point Node 
     |AutomationDesignerRoot|  Root node of Aspect Navigator 
     |AutomationDesignerUnassigned|  Unassigned folder in FLP aspect navigators 
     |AutomationDesignerProductTemplateLinkNode|  Product Template Link node 
     |AutomationDesignerMemoryArea|  Memory Area 
     |AutomationDesigner2DSymbols3DModels|  2D symbols and 3D Models assigned to a Product 
     |AutomationDesignerCableCore|  Cable Core 
     |AutomationDesignerTagTable|  Obsolete: Do Not Use 
     |AutomationDesignerStationFolder|  Folder node in Automation navigator 
     |AutomationDesignerRack|  PLC Rack 
     |AutomationDesignerConnectedDevice|  Shadow Object that represent hardware item connected to subnet via communication interface 
     |AutomationDesignerSymbolVariant|  Symbol Variant 
     |AutomationDesignerViewPageNode|  View page node in document navigator 
     |AutomationDesignerBMECatVersionNode|  BMECat version node in EClass structure navigator 
     |AutomationDesignerEClassVersionNode|  EClass Version Node 
     |AutomationDesignerTemplateContent|  Template Instance 
     |AllCAE|  The subset of CAE entities that can be shown and hidden 
     |CAEPolygonEdge|  CAE Polygon Edges 
     |CAEPolygonFace|  CAE Polygon Faces 
     |CAEPolygonBody|  CAE Polygon Bodies 
     |CAEPolygonVertex|  CAE Polygon Vertices 
     |CAELoad|  CAE Loads 
     |CAEConstraint|  CAE Constraints 
     |CAESimulationObject|  CAE Simulation Objects 
     |CAEConnection|  CAE Connections 
     |CAEMeshPoint|  CAE Mesh Points 
     |CAEEdgeDensity|  CAE Edge Density Mesh Control 
     |CAEFaceDensity|  CAE Edge Density Mesh Control 
     |CAEWeldRowDensity|  CAE Weld Row Density Mesh Control 
     |CAEMappedHoleDensity|  CAE Mapped Hole Density Mesh Control 
     |CAEFilletDensity|  CAE Fillet Density Mesh Control 
     |CAECylinderDensity|   CAE Cylinder Density Mesh Control 
     |CAEPointDensity|  CAE Point Density Mesh Control 
     |CAEBoundingVolumeDensity|  CAE Bounding Volume Density Mesh Control 
     |CAEMeshMating|  CAE Mesh Mating Condition Mesh Control 
     |CAEEdgeSeparationCondition|  CAE Edge Separation Condition Mesh Control 
     |CAEBoundaryLayer|  CAE Boundary Layer Mesh Control 
     |CAESelectionRecipe|  CAE Selection Recipe 
     |CAECrackFaceCondition|  CAE Crack Face Condition 
     |CAEFaceMatchControl|  CAE Face Match Mesh Control 
     |CAEEdgeMatchControl|  CAE Edge Match Mesh Control 
     |CAEDOFSet|  CAE DOF Set 
     |CAEMesh|  CAE Mesh 
     |CAETransientMesh|  CAE Transient Mesh 
     |CAESensor|  CAE Response Analysis Sensor 
     |CAEResponseAnalysisStrainGauge|  CAE Response Analysis Strain Gauge 
     |CAEElement|  CAE Element 
     |CAEElementEdge|  CAE Element Edge 
     |CAEElementFace|  CAE Element Face 
     |CAENode|  CAE Node 
     |CAEMarginCalculation|  CAE Aero Structures Margin Calculation 
     |CAELoadCaseSet|  CAE Aero Structures Load Case Set 
     |CAEMarginSolution|  CAE Aero Structures Margin Solution 
     |CAEFilteringSolution|  CAE Aero Structures Filtering Solution 
     |CAEFilteringCalculation|  CAE Aero Structures Filtering Calculation 
     |CAEDurabilitySpecialistEvent|  CAE Durability Specialist Event 
     |CAELocalDefinition|  CAE Durability Specialist Local Definition 
     |CAESpecialistSolution|  CAE Durability Specialist Specialist Solution 
     |CAEFunctionDefinition|  CAE Durability Specialist Function Definition 
     |CAECorrelationInput|  CAE Durability Specialist Correlation Input 
     |CAEVibrationInput|  CAE Durability Specialist Vibration Input 
     |CAERandomDataSource|  CAE Durability Specialist Random Data Source 
     |CAEDurabilitySpecialistStrainGauge|  CAE Durability Specialist Strain Gauge 
     |CAEResultReference|  CAE Result Reference 
     |CAELayoutState|  CAE Layout State 
     |CAEFemDataSet|  CAE Fem Data Set 
     |CAELoadRecipe|  CAE Load Recipe 
     |CAEDataSource|  CAE Data Source 
     |CAEDataProcessing|  CAE Data Processing MetaSolution 
     |CAEModelAndLoadPreprocessing|  CAE Model and Load Pre-processing MetaSolution 
     |CAEAcousticsAndVibrationSolution|  CAE Acoustics And Vibration Solution 
     |CAETransientMeshGroup|   CAE Transient Mesh Group 
     |CAEUniversalConnectionFolder|  CAE Universal Connection Folder 
     |CAEUniversalConnection|  CAE Universal Connection 
     |CAESpotWeldConnection|  CAE Spot Weld Connection 
     |CAEAdhesiveConnection|  CAE Adhesive Connection 
     |CAEBoltConnection|  CAE Bolt Connection 
     |CAESeamWeldConnection|  CAE Seam Weld Connection 
     |CAESealingConnection|  CAE Sealing Connection 
     |CAESpringConnection|  CAE Spring Connection 
     |CAEDamperConnection|  CAE Damper Connection 
     |CAERigidConnection|  CAE Rigid Connection 
     |CAEBushingConnection|  CAE Bushing Connection 
     |CAEKinematicConnection|  CAE Kinematic Connection 
     |CAELumpedMass|  CAE Lumped Mass 
     |CAERivet|  CAE Rivet 
     |CAEClinch|  CAE Clinch 
     |CAECrimpConnection|  CAE Crimp Connection 
     |CAEBarConnection|  CAE Bar Connection 
     |CAEBearingConnection|  CAE Bearing Connection 
     |CAELoadCaseFilteringSolution|  CAE Load Case Filtering Solution 
     |CAEStressLinearization|  CAE Stress Linearization 
     |CAEStressLinearizationManager|  CAE Stress Linearization Manager 
     |CAEPostTransNode|  Post Node 
     |CAEPostTransElement|  Post Element 
     |CAEPostTransMesh|  Post Mesh 
     |CAEPostTransPolygonEdge|  Post Polygon Edge
     |CAEPostTransPolygonFace|  Post Polygon Face
     |CAEPostTransComponent|  Post Component
     |CAEFreeBody|  Nodal Force Report 
     |CAEResultProbe|  Result Probe 
     |CAEPostTransElementFace|  Post Element Face
     |CAEPostTransElementEdge|  Post Element Edge
     |CAEFreeBodyFolder|  CAE Nodal Force Report Folder
     |CAEStressLinearizationFolder|  CAE Stress Linearization Folder
     |CAENoteConnection|  CAE Note Connection 
     |CoatingLayer|  Coating Layer 
     |CoatingStack|  Coating Stack 
     |LinearMaterial|  Linear Material 
     |DatumAxis|  Datum Axis 
     |DatumPlane|  Datum Plane 
     |SectionSegment|  Section Segment 
     |SectionLine|  Section Line 
     |CoordinateSystem|  Coordinate System 
     |Plane|  Plane 
     |DatumPlaneGrid|  Datum Plane Grid 
     |PlanarShipGrid|  Planar Ship Grid 
     |Traceline|  Traceline 
     |Image|  Image 
     |ControlCage|  Control cage used by NX Realize Shape application 
     |CageFace|  Face of control cage used by NX Realize Shape application 
     |CageEdge|  Edge of control cage used by NX Realize Shape application 
     |CageVertex|  Vertex of control cage used by NX Realize Shape application 
     |DesignMeshBody|  Represents selection filter for a body of a design mesh. Design mesh is a faceted representation used by modeling applications 
     |DesignMeshFace|  Represents selection filter for a facet face, typically a triangle, of a design mesh. Design mesh is a faceted representation used by modeling applications 
     |DesignMeshEdge|  Represents selection filter for a facet edge of a design mesh. Design mesh is a faceted representation used by modeling applications 
     |DesignMeshVertex|  Represents selection filter for a facet vertex of a design mesh. Design mesh is a faceted representation used by modeling applications 
     |AllDimensions|  All Dimensions 
     |LinearDimension|  Linear Dimension 
     |AngularDimension|  Angular Dimension 
     |RadialDimension|  Radial Dimension 
     |OrdinateDimension|  Ordinate Dimension 
     |ChamferDimension|  Chamfer Dimension 
     |ThicknessDimension|  Thickness Dimension 
     |ArcLengthDimension|  Arc Length Dimension 
     |DimensionSet|  Dimension Set 
     |AllDrafting|  All Drafting 
     |AllCenterlines|  All Centerlines 
     |AreaFill|  Area Fill 
     |AllSymbols|  All Drafting Symbols 
     |Note|  Note 
     |Label|  Label 
     |Balloon|  Balloon 
     |GDTSymbol|  GDT Symbol 
     |Centerline|  Centerline 
     |FullCircularCenterline|  Full Circular Centerline 
     |PartialCircularCenterline|  Partial Circular Centerline 
     |FullBoltCircle|  Full Bolt Circle Centerline 
     |PartialBoltCircle|  Partial Bolt Circle Centerline 
     |CenterMark|  Center Mark 
     |CylindricalCenterline|  Cylindrical Centerline 
     |SymmetricalCenterline|  Symmetrical Centerline 
     |Centerline2D|  2D Centerline 
     |Crosshatch|  Crosshatch 
     |Intersection|  Intersection 
     |TargetPoint|  Target Point 
     |UserDefinedSymbol|  User Defined Symbol 
     |OffsetCenterPoint|  Offset Center Point 
     |LabelOnParent|  Label on Parent 
     |TitleBlock|  Title Block 
     |FrameBar|  Frame Bar 
     |Arrow|  Arrow 
     |CuttingPlaneSymbol|  Cutting Plane Symbol 
     |ShipTic|  Ship Tic 
     |SupplementalGeometry|  Supplemental Geometry 
     |ViewBreak|  View Break 
     |DrawingTemplateRegion|  Drawing Template Region 
     |SurfaceFinish|  Surface Finish 
     |TabularNote|  Tabular NoteParts List 
     |DrawingImage|  Drawing Image 
     |Component2D|  2D Component 
     |ProductGrid|  Product Grid 
     |EdgeConditionSymbol|  Edge Condition Symbol 
     |AllFacetBodies|  Normal and Cloud Facet Bodies 
     |NormalFacetBody|  Normal Facet Body 
     |CloudFacetBody|  Cloud Facet Body 
     |NXFacet|  NX Facet 
     |AllBasicAndWeldFeatures|  All Basic and Weld Features 
     |AllBasicFeatures|  All Basic Features 
     |SolidFeature|  Solid Feature 
     |CurveFeature|  Curve Feature 
     |DatumPlaneFeature|  Datum Plane Feature 
     |DatumAxisFeature|  Datum Axis Feature 
     |DatumCoordinateSystemFeature|  Datum Coordinate System Feature 
     |SketchFeature|  Sketch Feature 
     |HD3DMarkup|  Markup 
     |HD3DMarkupElement|  Markup Element 
     |AllJoinObjects|  All Join objects 
     |JoinPoint|  Point Join Feature 
     |JoinCurve|  Curve Join Feature 
     |JoinFace|  Face Join Feature 
     |JoinHole|  Join Hole Feature 
     |LineDesignerConnector|  Line Designer Connector 
     |MachiningFeature|  Machining Feature in Manufacturing 
     |MachiningToolPath|  Tool Path in Manufacturing 
     |MachiningInProcessWorkpiece|  In-Process-Workpiece in Manufacturing 
     |AdditiveManufacturingSerialNumber|  Serial Number in Additive Manufacturing 
     |AdditiveManufacturingPartGroup|  Part Group in Additive Manufacturing 
     |AdditiveManufacturingBuildTray|  BuildTray in Additive Manufacturing 
     |AdditiveManufacturingPart|  Part in Additive Manufacturing 
     |AdditiveManufacturingPartOccurrence|  PartOccurrence in Additive Manufacturing 
     |AdditiveManufacturingSupport|  Support in Additive Manufacturing 
     |AdditiveManufacturingSupportOccurrence|  Support Occurrence in Additive Manufacturing 
     |AdditiveManufacturingPartRegion|  Part Region in Additive Manufacturing 
     |AdditiveManufacturingPartRegionOccurrence|  Part Region Occurrence in Additive Manufacturing 
     |ManufacturingPlanningRigidGroup|  The rigid group of objects or components for Manufacturing Planning applications 
     |ManufacturingPlanningJoint|  The joint relationship between rigid groups for Manufacturing Planning applications 
     |MDCLogicalElement|  Logical Element for Multi-Discipline Connectivity 
     |MDCConnectionElement|  Logical Connection for Multi-Discipline Connectivity 
     |MDCPortArtifact|  Logical Port for Multi-Discipline Connectivity 
     |AllMechatronics|  All Mechatronics objects 
     |MechatronicsJoint|  All kinds of mechatronics joints for defining a relationship between rigid bodies 
     |MechatronicsCollisionBody|  A Collision Body defines objects to be able to collide with one another 
     |MechatronicsCollisionSensor|  A Collision Sensor is able to detect the presence of objects that intersect with its volume 
     |MechatronicsRuntimeButton|  A Runtime Button defines the user interaction during runtime 
     |MechatronicsDistanceSensor|  A distance sensor detects the shortest distance between the sensor and collision body 
     |Mechatronics2DLaserScanner|  A laser scanner is a set of beams which detects the distances, color or other properties for target objects 
     |MechatronicsLightCurtain|  A light curtain is a set of beams which detects the collision of target objects 
     |MechatronicsPositionSensor|  A Position Control causes objects attached to an axis to move along that axis to a given position 
     |MechatronicsVelocitySensor|  A velocity sensor returns the angular or linear velocity of the selected joint 
     |MechatronicsGenericSensor|  A generic sensor returns the parameter value of the selected object 
     |MechatronicsLimitSwitch|  A limit switch references any runtime parameter from the selected object and has a boolean output 
     |MechatronicsRelay|  A relay references any runtime parameter from the selected object and has a boolean output 
     |MechatronicsInclinometer|  An inclinometer returns the angle value of the selected rigid body 
     |MechatronicsAccelerometer|  An accelerometer returns the accelerometer value of the selected rigid body 
     |MechatronicsPneumaticCylinder|  A pneumatic cylinder causes forces according to the characteristic of a compressible fluid to move simulation objects 
     |MechatronicsPneumaticValve|  A pneumatic valve controls a pneumatic cylinder 
     |MechatronicsHydraulicCylinder|  A hydraulic cylinder causes forces according to the characteristic of an incompressible fluid to move simulation objects 
     |MechatronicsHydraulicValve|  A hydraulic valve controls a hydraulic cylinder 
     |MechatronicsRigidBody|  A Rigid Body defines objects to be able to move about the world 
     |MechatronicsConstraint|  All kinds of mechatronics constraint 
     |MechatronicsTransportSurface|  Transport Surface causes a face on a geometric object to behave like it is moving even if the object is attached 
     |MechatronicsObjectSource|  Object Source is used to define some objects that can be copied during simulation 
     |MechatronicsObjectSink|  Object Sink is used to define some objects that delete copies of physics objects during simulation 
     |MechatronicsObjectTransformer|  An Object Transformer defines objects to be able to transform copies of rigid objects to another during simulation 
     |MechatronicsObjectBehavior|  Objects that are used to define kinds of behavior during simulation 
     |MechatronicsObjectData|  Objects that encapsulate data for simulation, for instance, collision material, motion profile, etc 
     |MechatronicsProxyObject|  A Proxy Object defines the object that has certain parameter attributes, encapsulates certain physics objects, and has some geometric representation 
     |MechatronicsSignal|  Signals used to define connections with adapters or external tools 
     |MechatronicsSnapPoint|  A SnapPoint defines one body positioning or two bodies that exactly lie upon each other 
     |MechatronicsDynamicMaterial|  A Dynamic Material to support variable size simulation 
     |AllMotionSim|  All MotionSim objects 
     |AllMotionSimForceObjects|  Force objects including Bushing, Contact, Damper, Force, Spring 
     |AllMotionSimJoints|  All MotionSim Joints 
     |MotionSimRoad|  Road 
     |MotionSimBearing|  Bearing 
     |MotionSimBearingProperty|  Bearing Property 
     |MotionSimControlPort|  Control Port 
     |MotionSimControlInput|  Control Input 
     |MotionSimPathFollower|  Path Follower 
     |MotionSimControlOperation|  Control Operation 
     |MotionSimControlOutput|  Control Output 
     |MotionSimGear|  Gear 
     |MotionSimGearContact|  Gear Contact 
     |MotionSimAnimation|  Animation 
     |MotionSimGraph|  Graph 
     |MotionSimMlpp|  Model and Load Pre-processing in Motion 
     |MotionSimCurveOperationRecord|  Curve Operation Record in Motion 
     |MotionSimMotionBodyDriver|  Motion Body Driver 
     |MotionSimLoadTransfer|  Load Transfer 
     |MotionSimJointDriver|  Joint Driver 
     |MotionSimStandaloneDriver|  Standalone Driver 
     |MotionSimMechatronics|  Mechatronics 
     |MotionSimProfile|  Profile in Motion 
     |MotionSimDiscreteDrivetrain|  Discrete Drivetrain 
     |MotionSimAnimationCamera|  Animation Camera in Motion 
     |MotionSimAutoflexProperty|  Autoflex Property 
     |MotionSimBasicTireProperty|  Basic Tire Property 
     |MotionSimMotorcycleTireProperty|  Motorcycle Tire Property 
     |MotionSimNonInertialTireProperty|  Non-inertial Tire Property 
     |MotionSimFTireProperty|  FTire Property 
     |MotionSimCDTireProperty|  CDTire Property 
     |MotionSimMFTyreAndMFSwiftTireProperty|  MF-Tyre and MF-Swift Tire Property 
     |MotionSimTire|  Tire 
     |MotionSimVehicleReporting|  Vehicle Reporting 
     |MotionSimSuspensionReporting|  Suspension Reporting 
     |MotionSimInitialCondition|  Initial Condition 
     |MotionSimAnalyticalContact|  Analytical Contact 
     |MotionSimAnalyticalContactProperty|  Analytical Contact Property 
     |MotionSimSpring|  Spring 
     |MotionSimRotationalSpring|  Rotational Spring 
     |MotionSimTranslationalSpring|  Translational Spring 
     |MotionSimDamper|  Damper 
     |MotionSimRotationalDamper|  Rotational Damper 
     |MotionSimTranslationalDamper|  Translational Damper 
     |MotionSimSpringDamper|  Spring Damper 
     |MotionSimRotationalSpringDamper|  Rotational Spring Damper 
     |MotionSimTranslationalSpringDamper|  Translational Spring Damper 
     |MotionSimSplineBeam|  Spline Beam 
     |MotionSimSplineBeamProperty|  SplineBeam Property 
     |MotionSimBeamSection|  Beam Section 
     |MotionSimBeamForce|  Beam Force 
     |MotionSimUserDefinedForce|  User-defined Force 
     |MotionSimFriction|  Friction 
     |MotionSimThreePointForce|  Three-point Force 
     |MotionSimThreePointTorque|  Three-point Torque 
     |MotionSimSubmechanism|  Submechanism 
     |MotionSimSubmechanismPositioner|  Submechanism Positioner 
     |MotionSimMotionConstraint|  Motion Constraint 
     |MotionSimMotionBody|  Motion Body 
     |MotionSimScalarForce|  Scalar Force 
     |MotionSimFlexibleBody|  Flexible Body 
     |MotionSimMarker|  Marker 
     |MotionSimScalarTorque|  Scalar Torque 
     |MotionSimCurveCurveContact|  CurveCurve Contact 
     |MotionSimContact|  Contact 
     |MotionSimBushing|  Bushing 
     |MotionSimBushingProperty|  Bushing Property
     |MotionSimVectorForce|  Vector Force 
     |MotionSimVectorTorque|  Vector Torque 
     |MotionSimSensor|  Sensor 
     |MotionSimMotor|  Motor 
     |MotionSimMotionVector|  Motion Vector 
     |MotionSimMeasure|  Measure in Motion 
     |MotionSimTrace|  Trace in Motion 
     |MotionSimInterference|  Interference in Motion 
     |MotionSimFixedJoint|  Fixed Joint 
     |MotionSimScrewJoint|  Screw Joint 
     |MotionSimRevoluteJoint|  Revolute Joint 
     |MotionSimSliderJoint|  Slider Joint 
     |MotionSimCylinderJoint|  Cylinder Joint 
     |MotionSimUniversalJoint|  Universal Joint 
     |MotionSimSphericalJoint|  Spherical Joint 
     |MotionSimPlanarJoint|  Planar Joint 
     |MotionSimGearJoint|  Gear Joint 
     |MotionSimRackAndPinion|  Rack and Pinion 
     |MotionSimPointOnCurve|  Point on Curve 
     |MotionSimCurveOnCurve|  Curve on Curve 
     |MotionSimCable|  Cable 
     |MotionSimConstantVelocity|  Constant Velocity 
     |MotionSimAtpointJoint|  Atpoint Joint 
     |MotionSimInlineJoint|  Inline Joint 
     |MotionSimInplaneJoint|  Inplane Joint 
     |MotionSimOrientationJoint|  Orientation Joint 
     |MotionSimParallelJoint|  Parallel Joint 
     |MotionSimPerpendicularJoint|  Perpendicular Joint 
     |MotionSimGeneralCoupler|  General Coupler 
     |MotionSimMotionBodyCoupler|  Motion Body Coupler 
     |MotionSimPlantInput|  Plant Input 
     |MotionSimPlantOutput|  Plant Output 
     |MotionSimSolutionStop|  Solution Stop 
     |MotionSimSignalChart|  Signal Chart 
     |MotionSimSolution|  Solution 
     |MotionSimGearSpur|  Spur Gear 
     |MotionSimGearHelical|  Helical Gear 
     |MotionSimGearStraightBevel|  Straight Bevel Gear 
     |MotionSimGearSpiralBevel|  Spiral Bevel Gear 
     |MotionSimGearHypoid|  Hypoid Gear 
     |MotionSimBumpStop|  BumpStop 
     |MotionSimCompoundJoint|  CompoundJoint 
     |MotionSimAnimationVector|  AnimationVector 
     |MotionSimHydrodynamicBearing|  Hydrodynamic Bearing 
     |MotionSimSprungMass|  Sprung Mass
     |MotionSimDiscreteDrivetrainReport|  Discrete Drivetrain Report
     |MotionSimElectromagneticForce|  ElectromagneticForce
     |MotionSimGeneralSensor|  General Sensor
     |MotionSimContactPattern|  ContactPattern 
     |MotionSimFlexModalContent|  Flex Modal Content 
     |MotionSimFixedJointDriver|  Fixed Joint Driver 
     |MotionSimFrfInput|  Frf Input 
     |MotionSimFrfOutput|  Frf Output 
     |PhysicalDiagrammingAnnotation|  Annotation for physical and boundary diagramming 
     |PhysicalDiagrammingConnection|  Connection for physical and boundary diagramming 
     |PhysicalDiagrammingNode|  Node for physical and boundary diagramming 
     |BoundaryNode|  Boundary node 
     |PIDAnnotation|  PID Annotation 
     |PIDConnection|  PID Connection 
     |PIDSymbol|  PID Symbol 
     |PIDRun|  PID Run 
     |PIDBranch|  PID Branch 
     |PIDSheet|  PID Sheet 
     |PIDSystem|  PID System 
     |PressLineSimulationLineComponent|  Selection filter for line component objects of a press line simulation job.
                                                                      The selected object can for instance be used to define the scope for subsequent
                                                                      collision checking. E.g. selecting a line component for the collision scope
                                                                      means that only the selected station is taken into account for collision checking. 
     |PressLineSimulationPressModelRoot|  Selection filter for the root object of a press line simulation job.
                                                                       The selected object can for instance be used to define the scope for
                                                                       subsequent collision checking. E.g. selecting the root object for the collision
                                                                       scope means that the entire press line is taken into account for collision checking. 
     |AllRoutingObjects|  All Routing Objects 
     |RoutingControlPoint|  Routing Control Point 
     |RoutingPort|  Routing Port 
     |RoutingPartAnchor|  Routing Part Anchor 
     |RoutingSegment|  Routing Segment 
     |RoutingStock|  Routing Stock 
     |AllShip|  All ship basic design structure objects 
     |AllShipPlateSystem|  All ship basic design plate systems 
     |AllShipProfileSystem|  All ship basic design profile systems 
     |ShipHull|  Ship basic design hull 
     |ShipDeck|  Ship basic design deck 
     |ShipTransverseBulkhead|  Ship basic design transverse bulkhead 
     |ShipLongitudinalBulkhead|  Ship basic design longitudinal bulkhead 
     |ShipGenericPlateSystem|  Ship basic design generic plate system 
     |ShipStiffenerSystem|  Ship basic design stiffener system 
     |ShipPillarSystem|  Ship basic design pillar system 
     |ShipEdgeReinforcement|  Ship basic design edge reinforcement system 
     |ShipSeam|  Ship basic design seam object, including scantling seam, erection seam, straking seam 
     |SketchRelation| Persistent Relation objects, formerly known as Sketch Constraints  
     |Sketch|  Sketch is a collection of planar curves with dimensions and relations.  It may or may not be related to a feature. 
     |SketchFoundRelation|  Found Relations exist during a solver operation and can be relaxed by selecting them. 
     |SketchCoincidentRelation|  Persistent or Found Coincident Relation in a Sketch 
     |SketchConcentricRelation|  Persistent or Found Concentric Relation in a Sketch 
     |SketchPointOnCurveRelation|  Persistent or Found Point On Curve Relation in a Sketch 
     |SketchCollinearRelation|  Persistent or Found Collinear Relation in a Sketch 
     |SketchHorizontalRelation|  Persistent or Found Horizontal Relation in a Sketch 
     |SketchHorizontalAlignmentRelation|  Persistent or Found Horizontal Alignment Relation in a Sketch 
     |SketchVerticalRelation|  Persistent or Found Vertical Relation in a Sketch 
     |SketchVerticalAlignmentRelation|  Persistent or Found Vertical Alignment Relation in a Sketch 
     |SketchTangentRelation|  Persistent or Found Tangent Relation in a Sketch 
     |SketchParallelRelation|  Persistent or Found Parallel Relation in a Sketch 
     |SketchPerpendicularRelation|  Persistent or Found Perpendicular Relation in a Sketch 
     |SketchEqualLengthRelation|  Persistent or Found Equal Length Relation in a Sketch 
     |SketchEqualRadiusRelation|  Persistent or Found Equal Radius Relation in a Sketch 
     |SketchSymmetricRelation|  Persistent or Found Symmetric Relation in a Sketch 
     |SketchMidpointRelation|  Persistent Midpoint Relation in a Sketch 
     |SketchPointOnStringRelation|  Persistent Point On String Relation in a Sketch, used for a connected string of recipe curves 
     |SketchTangentToStringRelation|  Persistent Tangent To String Relation in a Sketch, used for a connected string of recipe curves 
     |SketchPerpendicularToStringRelation|  Persistent Perpendicular To String Relation in a Sketch, used for a connected string of recipe curves 
     |SketchUniformScaleRelation|  Persistent Uniform Scale Relation in a Sketch, used for splines 
     |SketchG1SplineRelation|  Persistent G1 Spline Relation in a Sketch 
     |SketchG2SplineRelation|  Persistent G2 Spline Relation in a Sketch 
     |SketchTrimRelation|  Persistent Trim Relation in a Sketch, used for trimming recipe curves 
     |SketchOffsetRelation|  Persistent or Found Offset Relation in a Sketch 
     |SketchLinearPatternRelation|  Persistent Linear Pattern Relation in a Sketch 
     |SketchRectangularPatternRelation|  Persistent Rectangular Pattern Relation in a Sketch 
     |SketchCircularPatternRelation|  Persistent Circular Pattern Relation in a Sketch 
     |SketchGeneralPatternRelation|  Persistent General Pattern Relation in a Sketch 
     |SketchMirrorRelation|  Persistent Mirror Relation in a Sketch 
     |SketchPolygonRelation|  Persistent Polygon Relation in a Sketch 
     |SketchRigidGroupRelation|  Persistent Rigid Group Relation in a Sketch 
     |SketchScalableGroupRelation|  Persistent Scalable Group Relation in a Sketch 
     |SketchIgnoredRelation|  Ignored Relation in a Sketch, prevents finding of this relation by the solver 
     |AllEdges|  All Edges 
     |AllFaces|  All Faces 
     |AllSolidBodies|  All Solid Bodies 
     |AllSheetBodies|  All Sheet Bodies 
     |ConvergentSolidBody|  Convergent Solid Body 
     |ConvergentSheetBody|  Convergent Sheet Body 
     |PlanarFace|  Planar Face 
     |CylindricalFace|  Cylindrical Face 
     |ConicalFace|  Conical Face 
     |SphericalFace|  Spherical Face 
     |ToroidalFace|  Toroidal Face 
     |ParametricFace|  Parametric Face 
     |BlendedFace|  Blended Face 
     |OffsetFace|  Offset Face 
     |ExtrudedFace|  Extruded Face 
     |RevolvedFace|  Revolved Face 
     |ForeignFace|  Foreign Face 
     |ConvergentFace|  Convergent Face 
     |LinearEdge|  Linear Edge 
     |CircularEdge|  Circular Edge 
     |EllipticalEdge|  Elliptical Edge 
     |IntersectionEdge|  Intersection Edge 
     |SplineEdge|  Spline Edge 
     |SPCurveEdge|  SP-Curve Edge 
     |ForeignEdge|  Foreign Edge 
     |ConstantParameterEdge|  Constant Parameter Edge 
     |ConvergentEdge|  Convergent Edge 
     |ConvergentFacet|  Convergent Facet 
     |StagedModelStage|  Staged Model Stage 
     |StagedModelStageSet|  Staged Model Stage Set 
     |StructureDesignMemberCorner|  The corner object between members in Structure Designer 
     |TechnicalDataPackagePage|  Technical Data Package Template Page 
     |TechnicalDataPackageViewport|  Technical Data Package Viewport 
     |TechnicalDataPackageViewCarousel|  Technical Data Package View Carousel 
     |TechnicalDataPackageRectangle|  Technical Data Package Template Rectangle 
     |TechnicalDataPackagePDFFormField|  Technical Data Package Template PDF Form Field 
     |TechnicalDataPackageAutomaticTable|  Technical Data Package Template Automatic Table 
     |TechnicalDataPackageViewList|  Technical Data Package Template View List 
     |TechnicalDataPackagePrintView|  Technical Data Package Template Print View 
     |TechnicalDataPackageDiagramArea|  Technical Data Package Template Diagram Area 
     |AllViews|  All views 
     |SectionView|  Drawing Section View 
     |ImportedView|  Drawing Imported View 
     |OrthographicView|  Drawing Orthographic View 
     |AuxiliaryView|  Drawing Auxiliary View 
     |DetailView|  Drawing Detail View 
     |DrawingSheetView|  Drawing Sheet View 
     |ImportedPMILightweightSectionView|  Drawing Imported PMI Lightweight Section View 
     |AllBodyInWhiteDatums|  Body in White Datum 
     |AllWeldingObjects|   Welding Objects 
     |AllWeldingMeasurementObjects|  Measurement Objects 
     |GrooveWeld|  Weld Groove feature 
     |FilletWeld|  Fillet Weld feature 
     |ResistanceSpotWeld|  Weld Point object of Resistance Spot type 
     |ArcSpotWeld|  Weld Point object of Arc Spot type 
     |NutWeld|  Weld Point object of Nut type 
     |StudWeld|  Weld Point object of Stud type 
     |MechanicalClinchWeld|  Weld Point object of Mechanical Clinch type 
     |DollopWeld|  Weld Point object of Dollop type 
     |Custom1Weld|  Weld Point object with no pre-defined type 
     |Custom2Weld|  Weld Point object with no pre-defined type 
     |Custom3Weld|  Weld Point object with no pre-defined type 
     |Custom4Weld|  Weld Point object with no pre-defined type 
     |Custom5Weld|  Weld Point object with no pre-defined type 
     |UserDefinedWeld|  User Defined Weld feature 
     |FillWeld|  Fill feature 
     |WeldingJoint|  Structure Welding Joint feature 
     |WeldBead|  Weld Bead feature 
     |WeldPlugSlot|  Weld Plug Slot feature 
     |SurfaceWeld|  Structure Welding Surface Weld feature 
     |TranslateWeld|  Weld Transform feature 
     |JointMarkWeld|  Joint Mark object 
     |CompoundWeld| Compound Weld  
     |DatumSurface|  Datum Surface object 
     |DatumPin|  Datum Pin object 
     |DatumCustom1|  Weld Datum object with no pre-defined type 
     |DatumCustom2|  Weld Datum object with no pre-defined type 
     |DatumCustom3|  Weld Datum object with no pre-defined type 
     |MeasurementSurface|  Measurement Surface object 
     |MeasurementHole|  Measurement Hole object 
     |MeasurementStud|  Measurement Stud object 
     |MeasurementSlot|  Measurement Slot object 
     |MeasurementTrim|  Measurement Trim object 
     |MeasurementHemmedEdge|  Measurement Hemmed Edge object 
     |MeasurementCustom1|  Measurement object with no pre-defined type 
     |MeasurementCustom2|  Measurement object with no pre-defined type 
     |MeasurementCustom3|  Measurement object with no pre-defined type 
     |AllConicCurves|  Ellipse, Parabola, or Hyperbola 
     |AllCurves|  All types of Curves 
     |Point|  Point 
     |PointCloud|  Point Cloud 
     |Line| Line  
     |Arc|  Arc or Circle 
     |Ellipse|  Ellipse 
     |Parabola|  Parabola 
     |Hyperbola|  Hyperbola 
     |Spline|  Spline 
     |Polyline|  Polyline 
     |Stroke|  A stroke represents a trail of points with speed information defined typically by a touch gesture 
     |CompositesLaminate|  Composites Laminate 
     |CompositesPly|  Composites Ply 
     |AllCompositesObjects|  All Composites Objects 
     |AECGridLine|  AEC grid line 
     |AECLevelLine| 
     |AECSymbol| 
     |AECLineFormat| 
     |DisplayInstance|  Display Instance

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
    DisplayInstance: int
    @staticmethod
    def ValueOf(value: int) -> FilterMember:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass

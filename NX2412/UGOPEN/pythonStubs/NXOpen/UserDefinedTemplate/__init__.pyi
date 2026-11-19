from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.Features
class Collection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of user defined template """
    def ConvertDeformToFeaturetemplate(self, flexFeatureTag: NXOpen.Features.Feature) -> None:
        """
         Converts a deformable feature to feature template definition  
        """
        pass
    def ConvertUdfToFeaturetemplate(self, udfFeatureTag: NXOpen.Features.Feature) -> None:
        """
         Converts a user defined template definition to feature template definition  
        """
        pass
    def CreateDefinitionBuilder(self, user_defined_template_definition: Definition) -> DefinitionBuilder:
        """
         Creates a NXOpen.UserDefinedTemplate.InstantiationBuilder. 
         Returns builder ( DefinitionBuilder NXOpen.UserD):  .
        """
        pass
    def CreateInstantiationBuilder(self, user_defined_template_instantiation: Instantiation) -> InstantiationBuilder:
        """
         Creates a NXOpen.UserDefinedTemplate.InstantiationBuilder. 
         Returns builder ( InstantiationBuilder NXOpen.UserD):  .
        """
        pass
    def CreatePartAttribute(self, category_alias: str, title_alias: str, value: str, units: str, type: str) -> NXOpen.TaggedObject:
        """
         Creates the Part Attribute Object with input parameters 
         Returns createdPartAttribute ( NXOpen.TaggedObject):  Created Part Attribute object .
        """
        pass
    def CreateRelation(self, sourcePartTag: NXOpen.TaggedObject) -> None:
        """
         Creates a relation IMAN_UG_udf between the definition part and the instantiation part in managed mode 
        """
        pass
    def FindDefinitionObject(self, journal_identifier: str) -> Definition:
        """
         Find the User Defined Template Definition object with input name 
         Returns result ( Definition NXOpen.UserD):  User Defined Template Definition object with this identifier .
        """
        pass
    def FindDefinitionObjectInPart(self) -> Definition:
        """
         Find the User Defined Template Definition object in a given part 
         Returns result ( Definition NXOpen.UserD):  User Defined Template Definition object with this identifier .
        """
        pass
    def FindInstantiationObject(self, journal_identifier: str) -> Instantiation:
        """
         Find the User Defined Template Instantiation object with input name 
         Returns result ( Instantiation NXOpen.UserD):  User Defined Template Instantiation object with this identifier .
        """
        pass
    def FindInstantiationObjectFromTemplateFeature(self, templateFeatureTag: NXOpen.Features.Feature) -> Instantiation:
        """
         Find the User Defined Template Instantiation object for a given template feature 
         Returns result ( Instantiation NXOpen.UserD):  User Defined Template Instantiation object with this identifier .
        """
        pass
    def FindObject(self, journal_identifier: str) -> NXOpen.TaggedObject:
        """
         Find the Product Interface Object with input name 
         Returns found ( NXOpen.TaggedObject):  User Defined Template object with this identifier .
        """
        pass
    def SetBuilderAndDefinitionPart(self, builder: InstantiationBuilder, definitionPartTag: NXOpen.TaggedObject) -> None:
        """
         Sets NXOpen.UserDefinedTemplate.InstantiationBuilder and definition part 
        """
        pass
import NXOpen
class ConfigurableObject(NXOpen.NXObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ConfigurableObject """
    class PropertyId(Enum):
        """
        Members Include: 
         |Title|   
         |Cue|  
         |Helpcontext|  Used for the Context Key method of Help button
         |TemplateName|  
         |TemplateLocation|  
         |AllowExplode|  
         |AllowBoolean|  
         |Expanded|  
         |Name|  from label 
         |FileSystem|  from label 
         |Bitmap|  from label 
         |ItemRevision|  from label 
         |Dataset|  from label 
         |Update|  
         |DisplayStyle|  
         |Values|  
         |TooltipImages|  
         |ReturnType|  
         |OriginPoint|  
         |Vector|  
         |XVector|  
         |ZVector|  
         |Radius|  
         |Positive|  
         |MinValue|  
         |MinInclusive|  
         |MaxValue|  
         |MaxInclusive|  
         |Increment|  
         |DecimalPlaces|  
         |ListExpression|  
         |AllowDynamic|  
         |CheckMismatch|  
         |EnsureValue|  
         |ButtonAction|  from button 
         |DatasetType|  from button 
         |HelpUrl|  from button 
         |Tooltip|  from button 
         |UseAlert|  from button 
         |ExternalLibrary|  from button 
         |ClassName|  from button 
         |MethodName|  from button 
         |Parameters|  from button 
         |VisualRules|  from button 
         |JournalFile|  from button 
         |VisEnabled|  dependencies 
         |VisType|  dependencies 
         |VisObject|  dependencies 
         |VisComparison|  dependencies 
         |VisValue|  dependencies 
         |SensEnabled|  dependencies 
         |SensType|  dependencies 
         |SensObject|  dependencies 
         |SensComparison|  dependencies 
         |SensValue|  dependencies 
         |TooltipText|  
         |BooleanOrder|  
         |ReferenceBehavior|  
         |ContentVisibility|  white box or black box 
         |Rollback|  geometry 
         |Optional|  geometry 
         |Target|  geometry 
         |ShowHandle|  point 
         |SelectionScope|  point 
         |Hd3d|  hd3d folder 
         |Hd3dTitle1|  hd3d 
         |Hd3dUrl1|  hd3d 
         |Hd3dIcon1|  hd3d 
         |Hd3dDescription1|  hd3d 
         |Hd3dAnchor1|  hd3d 
         |Hd3dTitle2|  hd3d 
         |Hd3dUrl2|  hd3d 
         |Hd3dIcon2|  hd3d 
         |Hd3dDescription2|  hd3d 
         |Hd3dAnchor2|  hd3d 
         |Hd3dTitle3|  hd3d 
         |Hd3dUrl3|  hd3d 
         |Hd3dIcon3|  hd3d 
         |Hd3dDescription3|  hd3d 
         |Hd3dAnchor3|  hd3d 
         |FreezeWaveUpdate|  PTS dialog properties 
         |EnableCopyClone|  PTS dialog properties 
         |RunRelinker|  PTS dialog properties 
         |RunPartFamilyUpdate|  PTS dialog properties 
         |ShowAssemblyInstances|  PTS dialog properties 
         |UseDropPosition|  PTS dialog properties 
         |LaunchRedefineConstraints|  PTS dialog properties 
         |AllowQuickAccess|  PTS dialog properties 
         |DefaultRefSet|  PTS dialog properties 
         |ActiveRefSet|  PTS dialog properties 
         |ActiveView|  PTS dialog properties 
         |CheckTinyObjects|  PTS dialog properties 
         |CheckMisalignedObjects|  PTS dialog properties 
         |CheckBodyDataStructures|  PTS dialog properties 
         |CheckBodyConsistency|  PTS dialog properties 
         |CheckFaceFaceIntersection|  PTS dialog properties 
         |CheckFaceSmoothness|  PTS dialog properties 
         |CheckFaceSelfIntersection|  PTS dialog properties 
         |CheckFaceSpikesCuts|  PTS dialog properties 
         |CheckEdgeSmoothness|  PTS dialog properties 
         |CheckEdgeTolerances|  PTS dialog properties 
         |CheckOrphanBodies|  PTS dialog properties 
         |CheckInterpartWaveLinks|  PTS dialog properties 
         |CheckInterpartExpressionStatus|  PTS dialog properties 
         |RelinkUnbroken|  PTS dialog relinker properties 
         |IncludeSuppressed|  PTS dialog relinker properties 
         |FaceCurveDirection|  PTS dialog relinker properties 
         |SourceScope|  PTS dialog relinker properties 
         |TargetScope|  PTS dialog relinker properties 
         |RelinkOption|  PTS dialog relinker properties 
         |BreakWaveLinksAfterUpdate|  PTS dialog relinker properties 
         |BreakExpLinksAfterUpdate|  PTS dialog relinker properties 
         |CheckTinyObjectsTol|  PTS dialog checker properties 
         |CheckTinyObjectsLevel|  PTS dialog checker properties 
         |CheckTinyObjectsDesc|  PTS dialog checker properties 
         |CheckMisalignedObjectsTol|  PTS dialog checker properties 
         |CheckMisalignedObjectsLevel|  PTS dialog checker properties 
         |CheckMisalignedObjectsDesc|  PTS dialog checker properties 
         |CheckBodyDataStructuresLevel|  PTS dialog checker properties 
         |CheckBodyDataStructuresDesc|  PTS dialog checker properties 
         |CheckBodyConsistencyLevel|  PTS dialog checker properties 
         |CheckBodyConsistencyDesc|  PTS dialog checker properties 
         |CheckFaceFaceIntersectionLevel|  PTS dialog checker properties 
         |CheckFaceFaceIntersectionDesc|  PTS dialog checker properties 
         |CheckFaceSmoothnessLevel|  PTS dialog checker properties 
         |CheckFaceSmoothnessDesc|  PTS dialog checker properties 
         |CheckFaceSelfIntersectionLevel|  PTS dialog checker properties 
         |CheckFaceSelfIntersectionDesc|  PTS dialog checker properties 
         |CheckFaceSpikesCutsTol|  PTS dialog checker properties 
         |CheckFaceSpikesCutsLevel|  PTS dialog checker properties 
         |CheckFaceSpikesCutsDesc|  PTS dialog checker properties 
         |CheckEdgeSmoothnessTol|  PTS dialog checker properties 
         |CheckEdgeSmoothnessLevel|  PTS dialog checker properties 
         |CheckEdgeSmoothnessDesc|  PTS dialog checker properties 
         |CheckEdgeTolerancesTol|  PTS dialog checker properties 
         |CheckEdgeTolerancesLevel|  PTS dialog checker properties 
         |CheckEdgeTolerancesDesc|  PTS dialog checker properties 
         |CheckOrphanBodiesRefset|  PTS dialog checker properties 
         |CheckOrphanBodiesLevel|  PTS dialog checker properties 
         |CheckOrphanBodiesDesc|  PTS dialog checker properties 
         |CheckInterpartWaveLinksStatus|  PTS dialog checker properties 
         |CheckInterpartWaveLinksLevel|  PTS dialog checker properties 
         |CheckInterpartWaveLinksDesc|  PTS dialog checker properties 
         |CheckInterpartExpressionStatusLevel|  PTS dialog checker properties 
         |CheckInterpartExpressionStatusDesc|  PTS dialog checker properties 
         |LayerCategories|  PTS dialog property 
         |Preview|  Modeling preview option 
         |Positioning|  Feature template positioning option 
         |ExternalState|  PTS expression external state 
         |TemplateOrder|  Hidden property used to store template order 
         |SmartInitialization|  PTS expression smart init 
         |SmartSource|  PTS expression smart init 
         |SmartName|  PTS expression smart init 
         |ActionExecuteOpen|  PTS action execution flag 
         |ActionExecuteClose|  PTS action execution flag 
         |ActionExecuteValue|  PTS action execution flag 
         |ActionNameOpen|  PTS execution action name 
         |ActionNameClose|  PTS execution action name 
         |ActionNameValue|  PTS execution action name 
         |ComparisonType|  PTS Visual rule comparison type 
         |ComparisonName|  PTS Visual rule comparison name 
         |ComparisonOperator|  PTS Visual rule comparison operator 
         |ComparisonValue|  PTS Visual rule comparison value 
         |ComparisonCoordinate|  PTS Visual rule comparison value 
         |ActionState|  PTS Visual rule action onoff 
         |YVector|  
         |Part|  
         |XCoordinate|  
         |YCoordinate|  
         |Maintain|  
         |ReplaceAll|  
         |NameAction|  
         |ReferenceAction|  
         |LayerAction|  
         |Color|  
         |Function|  
         |Operation|  
         |Value|  
         |ActionExecute1|  
         |ActionExecute2|  
         |ActionExecute3|  
         |ActionExecute4|  
         |ActionExecute5|  
         |ActionExecute6|  
         |ActionExecute7|  
         |ActionExecute8|  
         |ActionExecute9|  
         |ActionExecute10|  
         |Operator1|  
         |Operator2|  
         |Operator3|  
         |Operator4|  
         |Operator5|  
         |Operator6|  
         |Operator7|  
         |Operator8|  
         |Operator9|  
         |Operator10|  
         |Value1|  
         |Value2|  
         |Value3|  
         |Value4|  
         |Value5|  
         |Value6|  
         |Value7|  
         |Value8|  
         |Value9|  
         |Value10|  
         |DraftingParts|  Hidden property used to store drafting parts 
         |MotionParts|  Hidden property used to store motion parts 
         |SimParts|  Hidden property used to store sim parts 
         |PmiSettings|  
         |ListImages|  
         |PropertyActive|  
         |Units|  
         |PmiCsysActive|  
         |LayerOption|  
         |PmiCsys|  
         |EnableAddConfig|  
         |EnableMinMaxForKeyin|  
         |PartEdited|  
         |EnableMultiPointSelector|  
         |ActionExecute11|  Start Execute Properties for Cases 11-100 for Construct Switch
         |ActionExecute12|  
         |ActionExecute13|  
         |ActionExecute14|  
         |ActionExecute15|  
         |ActionExecute16|  
         |ActionExecute17|  
         |ActionExecute18|  
         |ActionExecute19|  
         |ActionExecute20|  
         |ActionExecute21|  
         |ActionExecute22|  
         |ActionExecute23|  
         |ActionExecute24|  
         |ActionExecute25|  
         |ActionExecute26|  
         |ActionExecute27|  
         |ActionExecute28|  
         |ActionExecute29|  
         |ActionExecute30|  
         |ActionExecute31|  
         |ActionExecute32|  
         |ActionExecute33|  
         |ActionExecute34|  
         |ActionExecute35|  
         |ActionExecute36|  
         |ActionExecute37|  
         |ActionExecute38|  
         |ActionExecute39|  
         |ActionExecute40|  
         |ActionExecute41|  
         |ActionExecute42|  
         |ActionExecute43|  
         |ActionExecute44|  
         |ActionExecute45|  
         |ActionExecute46|  
         |ActionExecute47|  
         |ActionExecute48|  
         |ActionExecute49|  
         |ActionExecute50|  
         |ActionExecute51|  
         |ActionExecute52|  
         |ActionExecute53|  
         |ActionExecute54|  
         |ActionExecute55|  
         |ActionExecute56|  
         |ActionExecute57|  
         |ActionExecute58|  
         |ActionExecute59|  
         |ActionExecute60|  
         |ActionExecute61|  
         |ActionExecute62|  
         |ActionExecute63|  
         |ActionExecute64|  
         |ActionExecute65|  
         |ActionExecute66|  
         |ActionExecute67|  
         |ActionExecute68|  
         |ActionExecute69|  
         |ActionExecute70|  
         |ActionExecute71|  
         |ActionExecute72|  
         |ActionExecute73|  
         |ActionExecute74|  
         |ActionExecute75|  
         |ActionExecute76|  
         |ActionExecute77|  
         |ActionExecute78|  
         |ActionExecute79|  
         |ActionExecute80|  
         |ActionExecute81|  
         |ActionExecute82|  
         |ActionExecute83|  
         |ActionExecute84|  
         |ActionExecute85|  
         |ActionExecute86|  
         |ActionExecute87|  
         |ActionExecute88|  
         |ActionExecute89|  
         |ActionExecute90|  
         |ActionExecute91|  
         |ActionExecute92|  
         |ActionExecute93|  
         |ActionExecute94|  
         |ActionExecute95|  
         |ActionExecute96|  
         |ActionExecute97|  
         |ActionExecute98|  
         |ActionExecute99|  
         |ActionExecute100|  End execute property for Construct Switch 
         |Operator11|  Start operator property 11-100 for Construct Switch
         |Operator12|  
         |Operator13|  
         |Operator14|  
         |Operator15|  
         |Operator16|  
         |Operator17|  
         |Operator18|  
         |Operator19|  
         |Operator20|  
         |Operator21|  
         |Operator22|  
         |Operator23|  
         |Operator24|  
         |Operator25|  
         |Operator26|  
         |Operator27|  
         |Operator28|  
         |Operator29|  
         |Operator30|  
         |Operator31|  
         |Operator32|  
         |Operator33|  
         |Operator34|  
         |Operator35|  
         |Operator36|  
         |Operator37|  
         |Operator38|  
         |Operator39|  
         |Operator40|  
         |Operator41|  
         |Operator42|  
         |Operator43|  
         |Operator44|  
         |Operator45|  
         |Operator46|  
         |Operator47|  
         |Operator48|  
         |Operator49|  
         |Operator50|  
         |Operator51|  
         |Operator52|  
         |Operator53|  
         |Operator54|  
         |Operator55|  
         |Operator56|  
         |Operator57|  
         |Operator58|  
         |Operator59|  
         |Operator60|  
         |Operator61|  
         |Operator62|  
         |Operator63|  
         |Operator64|  
         |Operator65|  
         |Operator66|  
         |Operator67|  
         |Operator68|  
         |Operator69|  
         |Operator70|  
         |Operator71|  
         |Operator72|  
         |Operator73|  
         |Operator74|  
         |Operator75|  
         |Operator76|  
         |Operator77|  
         |Operator78|  
         |Operator79|  
         |Operator80|  
         |Operator81|  
         |Operator82|  
         |Operator83|  
         |Operator84|  
         |Operator85|  
         |Operator86|  
         |Operator87|  
         |Operator88|  
         |Operator89|  
         |Operator90|  
         |Operator91|  End operator property 11-100 for Construct Switch
         |Operator92|  
         |Operator93|  
         |Operator94|  
         |Operator95|  
         |Operator96|  
         |Operator97|  
         |Operator98|  
         |Operator99|  
         |Operator100|  
         |Value11|  Start of value property 11-100 for Construct Switch 
         |Value12|  
         |Value13|  
         |Value14|  
         |Value15|  
         |Value16|  
         |Value17|  
         |Value18|  
         |Value19|  
         |Value20|  
         |Value21|  
         |Value22|  
         |Value23|  
         |Value24|  
         |Value25|  
         |Value26|  
         |Value27|  
         |Value28|  
         |Value29|  
         |Value30|  
         |Value31|  
         |Value32|  
         |Value33|  
         |Value34|  
         |Value35|  
         |Value36|  
         |Value37|  
         |Value38|  
         |Value39|  
         |Value40|  
         |Value41|  
         |Value42|  
         |Value43|  
         |Value44|  
         |Value45|  
         |Value46|  
         |Value47|  
         |Value48|  
         |Value49|  
         |Value50|  
         |Value51|  
         |Value52|  
         |Value53|  
         |Value54|  
         |Value55|  
         |Value56|  
         |Value57|  
         |Value58|  
         |Value59|  
         |Value60|  
         |Value61|  
         |Value62|  
         |Value63|  
         |Value64|  
         |Value65|  
         |Value66|  
         |Value67|  
         |Value68|  
         |Value69|  
         |Value70|  
         |Value71|  
         |Value72|  
         |Value73|  
         |Value74|  
         |Value75|  
         |Value76|  
         |Value77|  
         |Value78|  
         |Value79|  
         |Value80|  
         |Value81|  
         |Value82|  
         |Value83|  
         |Value84|  
         |Value85|  
         |Value86|  
         |Value87|  
         |Value88|  
         |Value89|  
         |Value90|  
         |Value91|  
         |Value92|  
         |Value93|  
         |Value94|  
         |Value95|  
         |Value96|  
         |Value97|  
         |Value98|  
         |Value99|  
         |Value100|  End of value 11-100 for cases in VisualNodeConstructSwitch 
         |MassPropertiesBehavior|  Configure for mass properties behavior, only apply for deform app 
         |EnablePositionMethod|  
         |HelpButtonSource|  Either Context Key or File System. What to bring up if help button is hit 
         |HelpButtonFileSystem|  What file system to use for the file (Native, Embedded, Teamcenter) 
         |HelpButtonUrl| Stores url or file to open when help button is clicked 
         |HelpButtonDatasetType|  Dataset type for Teamcenter Option of Help Button File System
         |HelpButtonItemRevision|  Revision for the Team Center Option of the Help Button's selected file 
         |HelpButtonDataset|  the File used when Help Button is clicked in Team Center
         |EnableTranslate|  If auto-translate UI comp labels based on NX lanaguage files

        """
        Title: int
        Cue: int
        Helpcontext: int
        TemplateName: int
        TemplateLocation: int
        AllowExplode: int
        AllowBoolean: int
        Expanded: int
        Name: int
        FileSystem: int
        Bitmap: int
        ItemRevision: int
        Dataset: int
        Update: int
        DisplayStyle: int
        Values: int
        TooltipImages: int
        ReturnType: int
        OriginPoint: int
        Vector: int
        XVector: int
        ZVector: int
        Radius: int
        Positive: int
        MinValue: int
        MinInclusive: int
        MaxValue: int
        MaxInclusive: int
        Increment: int
        DecimalPlaces: int
        ListExpression: int
        AllowDynamic: int
        CheckMismatch: int
        EnsureValue: int
        ButtonAction: int
        DatasetType: int
        HelpUrl: int
        Tooltip: int
        UseAlert: int
        ExternalLibrary: int
        ClassName: int
        MethodName: int
        Parameters: int
        VisualRules: int
        JournalFile: int
        VisEnabled: int
        VisType: int
        VisObject: int
        VisComparison: int
        VisValue: int
        SensEnabled: int
        SensType: int
        SensObject: int
        SensComparison: int
        SensValue: int
        TooltipText: int
        BooleanOrder: int
        ReferenceBehavior: int
        ContentVisibility: int
        Rollback: int
        Optional: int
        Target: int
        ShowHandle: int
        SelectionScope: int
        Hd3d: int
        Hd3dTitle1: int
        Hd3dUrl1: int
        Hd3dIcon1: int
        Hd3dDescription1: int
        Hd3dAnchor1: int
        Hd3dTitle2: int
        Hd3dUrl2: int
        Hd3dIcon2: int
        Hd3dDescription2: int
        Hd3dAnchor2: int
        Hd3dTitle3: int
        Hd3dUrl3: int
        Hd3dIcon3: int
        Hd3dDescription3: int
        Hd3dAnchor3: int
        FreezeWaveUpdate: int
        EnableCopyClone: int
        RunRelinker: int
        RunPartFamilyUpdate: int
        ShowAssemblyInstances: int
        UseDropPosition: int
        LaunchRedefineConstraints: int
        AllowQuickAccess: int
        DefaultRefSet: int
        ActiveRefSet: int
        ActiveView: int
        CheckTinyObjects: int
        CheckMisalignedObjects: int
        CheckBodyDataStructures: int
        CheckBodyConsistency: int
        CheckFaceFaceIntersection: int
        CheckFaceSmoothness: int
        CheckFaceSelfIntersection: int
        CheckFaceSpikesCuts: int
        CheckEdgeSmoothness: int
        CheckEdgeTolerances: int
        CheckOrphanBodies: int
        CheckInterpartWaveLinks: int
        CheckInterpartExpressionStatus: int
        RelinkUnbroken: int
        IncludeSuppressed: int
        FaceCurveDirection: int
        SourceScope: int
        TargetScope: int
        RelinkOption: int
        BreakWaveLinksAfterUpdate: int
        BreakExpLinksAfterUpdate: int
        CheckTinyObjectsTol: int
        CheckTinyObjectsLevel: int
        CheckTinyObjectsDesc: int
        CheckMisalignedObjectsTol: int
        CheckMisalignedObjectsLevel: int
        CheckMisalignedObjectsDesc: int
        CheckBodyDataStructuresLevel: int
        CheckBodyDataStructuresDesc: int
        CheckBodyConsistencyLevel: int
        CheckBodyConsistencyDesc: int
        CheckFaceFaceIntersectionLevel: int
        CheckFaceFaceIntersectionDesc: int
        CheckFaceSmoothnessLevel: int
        CheckFaceSmoothnessDesc: int
        CheckFaceSelfIntersectionLevel: int
        CheckFaceSelfIntersectionDesc: int
        CheckFaceSpikesCutsTol: int
        CheckFaceSpikesCutsLevel: int
        CheckFaceSpikesCutsDesc: int
        CheckEdgeSmoothnessTol: int
        CheckEdgeSmoothnessLevel: int
        CheckEdgeSmoothnessDesc: int
        CheckEdgeTolerancesTol: int
        CheckEdgeTolerancesLevel: int
        CheckEdgeTolerancesDesc: int
        CheckOrphanBodiesRefset: int
        CheckOrphanBodiesLevel: int
        CheckOrphanBodiesDesc: int
        CheckInterpartWaveLinksStatus: int
        CheckInterpartWaveLinksLevel: int
        CheckInterpartWaveLinksDesc: int
        CheckInterpartExpressionStatusLevel: int
        CheckInterpartExpressionStatusDesc: int
        LayerCategories: int
        Preview: int
        Positioning: int
        ExternalState: int
        TemplateOrder: int
        SmartInitialization: int
        SmartSource: int
        SmartName: int
        ActionExecuteOpen: int
        ActionExecuteClose: int
        ActionExecuteValue: int
        ActionNameOpen: int
        ActionNameClose: int
        ActionNameValue: int
        ComparisonType: int
        ComparisonName: int
        ComparisonOperator: int
        ComparisonValue: int
        ComparisonCoordinate: int
        ActionState: int
        YVector: int
        Part: int
        XCoordinate: int
        YCoordinate: int
        Maintain: int
        ReplaceAll: int
        NameAction: int
        ReferenceAction: int
        LayerAction: int
        Color: int
        Function: int
        Operation: int
        Value: int
        ActionExecute1: int
        ActionExecute2: int
        ActionExecute3: int
        ActionExecute4: int
        ActionExecute5: int
        ActionExecute6: int
        ActionExecute7: int
        ActionExecute8: int
        ActionExecute9: int
        ActionExecute10: int
        Operator1: int
        Operator2: int
        Operator3: int
        Operator4: int
        Operator5: int
        Operator6: int
        Operator7: int
        Operator8: int
        Operator9: int
        Operator10: int
        Value1: int
        Value2: int
        Value3: int
        Value4: int
        Value5: int
        Value6: int
        Value7: int
        Value8: int
        Value9: int
        Value10: int
        DraftingParts: int
        MotionParts: int
        SimParts: int
        PmiSettings: int
        ListImages: int
        PropertyActive: int
        Units: int
        PmiCsysActive: int
        LayerOption: int
        PmiCsys: int
        EnableAddConfig: int
        EnableMinMaxForKeyin: int
        PartEdited: int
        EnableMultiPointSelector: int
        ActionExecute11: int
        ActionExecute12: int
        ActionExecute13: int
        ActionExecute14: int
        ActionExecute15: int
        ActionExecute16: int
        ActionExecute17: int
        ActionExecute18: int
        ActionExecute19: int
        ActionExecute20: int
        ActionExecute21: int
        ActionExecute22: int
        ActionExecute23: int
        ActionExecute24: int
        ActionExecute25: int
        ActionExecute26: int
        ActionExecute27: int
        ActionExecute28: int
        ActionExecute29: int
        ActionExecute30: int
        ActionExecute31: int
        ActionExecute32: int
        ActionExecute33: int
        ActionExecute34: int
        ActionExecute35: int
        ActionExecute36: int
        ActionExecute37: int
        ActionExecute38: int
        ActionExecute39: int
        ActionExecute40: int
        ActionExecute41: int
        ActionExecute42: int
        ActionExecute43: int
        ActionExecute44: int
        ActionExecute45: int
        ActionExecute46: int
        ActionExecute47: int
        ActionExecute48: int
        ActionExecute49: int
        ActionExecute50: int
        ActionExecute51: int
        ActionExecute52: int
        ActionExecute53: int
        ActionExecute54: int
        ActionExecute55: int
        ActionExecute56: int
        ActionExecute57: int
        ActionExecute58: int
        ActionExecute59: int
        ActionExecute60: int
        ActionExecute61: int
        ActionExecute62: int
        ActionExecute63: int
        ActionExecute64: int
        ActionExecute65: int
        ActionExecute66: int
        ActionExecute67: int
        ActionExecute68: int
        ActionExecute69: int
        ActionExecute70: int
        ActionExecute71: int
        ActionExecute72: int
        ActionExecute73: int
        ActionExecute74: int
        ActionExecute75: int
        ActionExecute76: int
        ActionExecute77: int
        ActionExecute78: int
        ActionExecute79: int
        ActionExecute80: int
        ActionExecute81: int
        ActionExecute82: int
        ActionExecute83: int
        ActionExecute84: int
        ActionExecute85: int
        ActionExecute86: int
        ActionExecute87: int
        ActionExecute88: int
        ActionExecute89: int
        ActionExecute90: int
        ActionExecute91: int
        ActionExecute92: int
        ActionExecute93: int
        ActionExecute94: int
        ActionExecute95: int
        ActionExecute96: int
        ActionExecute97: int
        ActionExecute98: int
        ActionExecute99: int
        ActionExecute100: int
        Operator11: int
        Operator12: int
        Operator13: int
        Operator14: int
        Operator15: int
        Operator16: int
        Operator17: int
        Operator18: int
        Operator19: int
        Operator20: int
        Operator21: int
        Operator22: int
        Operator23: int
        Operator24: int
        Operator25: int
        Operator26: int
        Operator27: int
        Operator28: int
        Operator29: int
        Operator30: int
        Operator31: int
        Operator32: int
        Operator33: int
        Operator34: int
        Operator35: int
        Operator36: int
        Operator37: int
        Operator38: int
        Operator39: int
        Operator40: int
        Operator41: int
        Operator42: int
        Operator43: int
        Operator44: int
        Operator45: int
        Operator46: int
        Operator47: int
        Operator48: int
        Operator49: int
        Operator50: int
        Operator51: int
        Operator52: int
        Operator53: int
        Operator54: int
        Operator55: int
        Operator56: int
        Operator57: int
        Operator58: int
        Operator59: int
        Operator60: int
        Operator61: int
        Operator62: int
        Operator63: int
        Operator64: int
        Operator65: int
        Operator66: int
        Operator67: int
        Operator68: int
        Operator69: int
        Operator70: int
        Operator71: int
        Operator72: int
        Operator73: int
        Operator74: int
        Operator75: int
        Operator76: int
        Operator77: int
        Operator78: int
        Operator79: int
        Operator80: int
        Operator81: int
        Operator82: int
        Operator83: int
        Operator84: int
        Operator85: int
        Operator86: int
        Operator87: int
        Operator88: int
        Operator89: int
        Operator90: int
        Operator91: int
        Operator92: int
        Operator93: int
        Operator94: int
        Operator95: int
        Operator96: int
        Operator97: int
        Operator98: int
        Operator99: int
        Operator100: int
        Value11: int
        Value12: int
        Value13: int
        Value14: int
        Value15: int
        Value16: int
        Value17: int
        Value18: int
        Value19: int
        Value20: int
        Value21: int
        Value22: int
        Value23: int
        Value24: int
        Value25: int
        Value26: int
        Value27: int
        Value28: int
        Value29: int
        Value30: int
        Value31: int
        Value32: int
        Value33: int
        Value34: int
        Value35: int
        Value36: int
        Value37: int
        Value38: int
        Value39: int
        Value40: int
        Value41: int
        Value42: int
        Value43: int
        Value44: int
        Value45: int
        Value46: int
        Value47: int
        Value48: int
        Value49: int
        Value50: int
        Value51: int
        Value52: int
        Value53: int
        Value54: int
        Value55: int
        Value56: int
        Value57: int
        Value58: int
        Value59: int
        Value60: int
        Value61: int
        Value62: int
        Value63: int
        Value64: int
        Value65: int
        Value66: int
        Value67: int
        Value68: int
        Value69: int
        Value70: int
        Value71: int
        Value72: int
        Value73: int
        Value74: int
        Value75: int
        Value76: int
        Value77: int
        Value78: int
        Value79: int
        Value80: int
        Value81: int
        Value82: int
        Value83: int
        Value84: int
        Value85: int
        Value86: int
        Value87: int
        Value88: int
        Value89: int
        Value90: int
        Value91: int
        Value92: int
        Value93: int
        Value94: int
        Value95: int
        Value96: int
        Value97: int
        Value98: int
        Value99: int
        Value100: int
        MassPropertiesBehavior: int
        EnablePositionMethod: int
        HelpButtonSource: int
        HelpButtonFileSystem: int
        HelpButtonUrl: int
        HelpButtonDatasetType: int
        HelpButtonItemRevision: int
        HelpButtonDataset: int
        EnableTranslate: int
        @staticmethod
        def ValueOf(value: int) -> ConfigurableObject.PropertyId:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class UpdateType(Enum):
        """
        Members Include: 
         |NotSet|  
         |ExternalChange|  
         |PartFamily|  

        """
        NotSet: int
        ExternalChange: int
        PartFamily: int
        @staticmethod
        def ValueOf(value: int) -> ConfigurableObject.UpdateType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetLogicalParameter(self, property_id: ConfigurableObject.PropertyId) -> bool:
        """
         Get a logical parameter of the object. 
         Returns value (bool):  .
        """
        pass
    def GetMenuParameter(self, property_id: ConfigurableObject.PropertyId) -> int:
        """
         Get a menu parameter of the object. 
         Returns value (int):  .
        """
        pass
    def GetParameter(self, property_id: ConfigurableObject.PropertyId) -> str:
        """
         Get a parameter of the object. 
         Returns value (str):  .
        """
        pass
    def SetChoiceParameter(self, property_id: ConfigurableObject.PropertyId, choices: List[str]) -> None:
        """
         Set a list of choices for the object. 
        """
        pass
    def SetLogicalParameter(self, property_id: ConfigurableObject.PropertyId, value: bool) -> None:
        """
         Set a logical parameter of the object. 
        """
        pass
    def SetMenuParameter(self, property_id: ConfigurableObject.PropertyId, menuIndex: int) -> None:
        """
         Set a menu parameter of the object. 
        """
        pass
    def SetParameter(self, property_id: ConfigurableObject.PropertyId, value: str) -> None:
        """
         Set a parameter of the object. 
        """
        pass
    def SetTagParameter(self, property_id: ConfigurableObject.PropertyId, referenceObject: NXOpen.NXObject) -> None:
        """
         Set an object tag for the parameter. 
        """
        pass
    def Update(self, updateType: ConfigurableObject.UpdateType) -> None:
        """
         Perform an update for a configurable object. 
        """
        pass
import NXOpen
class ConfigurationManager(NXOpen.Object): 
    """ Provides methods for manipulating the template studio configuration objects in a part.
        Inputs to this feature can be convergent objects."""
    class ItemType(Enum):
        """
        Members Include: 
         |Group|   
         |Tab|  
         |Button|  
         |Label|  
         |Separator|  
         |Layer|  
         |Routing|  
         |Arrangement|  
         |Family|  
         |Number|  
         |String|  
         |Boolean|  
         |Integer|  
         |Reference|  
         |Body|  
         |Sketch|  
         |Geometry|  
         |Extract|  
         |Point|  
         |Position|  
         |Component|  
         |PointExp|  
         |VectorExp|  
         |Optimization|  
         |Feabody|  
         |ParameterTable|  
         |Feaload|  
         |Feamesh|  
         |Feasolution|  
         |Simnumber|  
         |Simfeasolve|  
         |Simfeaviewer|  
         |Simfeareport|  
         |Motionlink|  
         |Motionjoint|  
         |Motionspring|  
         |Motionbushing|  
         |Motiondamper|  
         |Motionforce|  
         |Motiontorque|  
         |Motionmotor|  
         |Motionpackaging|  
         |Motionsolution|  
         |Simresult|  
         |Simfunction|  
         |Simmotionbutton|  
         |Simmotionviewer|  
         |Simmotiongraph|  
         |Simfile|  
         |Udt|  
         |EclassCsys|  
         |EclassDatumaxis|  
         |EclassPoint|  
         |Reposition|  
         |EclassValuerange|  

        """
        Group: int
        Tab: int
        Button: int
        Label: int
        Separator: int
        Layer: int
        Routing: int
        Arrangement: int
        Family: int
        Number: int
        String: int
        Boolean: int
        Integer: int
        Reference: int
        Body: int
        Sketch: int
        Geometry: int
        Extract: int
        Point: int
        Position: int
        Component: int
        PointExp: int
        VectorExp: int
        Optimization: int
        Feabody: int
        ParameterTable: int
        Feaload: int
        Feamesh: int
        Feasolution: int
        Simnumber: int
        Simfeasolve: int
        Simfeaviewer: int
        Simfeareport: int
        Motionlink: int
        Motionjoint: int
        Motionspring: int
        Motionbushing: int
        Motiondamper: int
        Motionforce: int
        Motiontorque: int
        Motionmotor: int
        Motionpackaging: int
        Motionsolution: int
        Simresult: int
        Simfunction: int
        Simmotionbutton: int
        Simmotionviewer: int
        Simmotiongraph: int
        Simfile: int
        Udt: int
        EclassCsys: int
        EclassDatumaxis: int
        EclassPoint: int
        Reposition: int
        EclassValuerange: int
        @staticmethod
        def ValueOf(value: int) -> ConfigurationManager.ItemType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MoveType(Enum):
        """
        Members Include: 
         |Up|   
         |Down|  
         |Out|  reduce group nesting 

        """
        Up: int
        Down: int
        Out: int
        @staticmethod
        def ValueOf(value: int) -> ConfigurationManager.MoveType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TemplateType(Enum):
        """
        Members Include: 
         |NotSet|   
         |Pts|  
         |Fts|  
         |Dts|  

        """
        NotSet: int
        Pts: int
        Fts: int
        Dts: int
        @staticmethod
        def ValueOf(value: int) -> ConfigurationManager.TemplateType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def CreateItemNode(self, item_type: ConfigurationManager.ItemType) -> ConfigurableObject:
        """
         Create a UI item node for the template configuration dialog.
         Returns itemNode ( ConfigurableObject NXOpen.UserD):  .
        """
        pass
    def CreateRootNode(self, template_type: ConfigurationManager.TemplateType) -> ConfigurableObject:
        """
         Create a root node of the template configuration dialog.
         Returns rootNode ( ConfigurableObject NXOpen.UserD):  .
        """
        pass
    def CreateVisualRule(self, rootNode: ConfigurableObject) -> VisualRule:
        """
         Create a visual rule in a template.
         Returns visualRule ( VisualRule NXOpen.UserD):  .
        """
        pass
    def DeleteVisualRule(self, rootNode: ConfigurableObject, ruleName: str) -> None:
        """
         Delete a visual rule in a template.
        """
        pass
    def DragDropNode(self, rootNode: ConfigurableObject, sourceNode: ConfigurableObject, targetNode: ConfigurableObject) -> None:
        """
         Add or move a node in the configuration dialog.
        """
        pass
    def GetRootNode(self) -> ConfigurableObject:
        """
         Find the template root in a part.
         Returns rootNode ( ConfigurableObject NXOpen.UserD):  .
        """
        pass
    def GetRootNodeByType(self, tempateType: int) -> ConfigurableObject:
        """
         Find the template root in a part by type.
         Returns rootNode ( ConfigurableObject NXOpen.UserD):  .
        """
        pass
    def LoadEmbeddedFile(self, embeddedName: str, filename: str) -> None:
        """
         Load a file into the template studio as an embedded file.
        """
        pass
    def MoveItemNode(self, move_type: ConfigurationManager.MoveType, sourceNode: ConfigurableObject) -> None:
        """
         Move a node up or down in the configuration dialog.
        """
        pass
    def PublishPTSData(self, rootNode: ConfigurableObject) -> None:
        """
         Publish PTS data for a part.
        """
        pass
    def RemoveItemNode(self, targetNode: ConfigurableObject) -> None:
        """
         Remove a node in the configuration dialog.
        """
        pass
    def RemovePTSData(self, removeLegacyData: bool) -> None:
        """
         Remove PTS data from a part.
        """
        pass
    def TransferEmbeddedFiles(self, rootNode: ConfigurableObject, target_part: NXOpen.BasePart) -> None:
        """
         Transfer embedded files to the target part.
        """
        pass
    def UpgradeLegacyChecks(self) -> None:
        """
         Upgrade legacy PTS requirement checks into the NX requirements and checks.
        """
        pass
    def UpgradeLegacyData(self, rootNode: ConfigurableObject) -> None:
        """
         Upgrade legacy PTS data into the new format.
        """
        pass
import NXOpen
class DefinitionBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.UserDefinedTemplate.DefinitionBuilder
    """
    @property
    def ConfigurableObject(self) -> ConfigurableObject:
        """
        Getter for property: ( ConfigurableObject NXOpen.UserD) ConfigurableObject
         Returns the ConfigurableObject of User Defined Template Definition   
            
         
        """
        pass
    @ConfigurableObject.setter
    def ConfigurableObject(self, configurableObjectTag: ConfigurableObject):
        """
        Setter for property: ( ConfigurableObject NXOpen.UserD) ConfigurableObject
         Returns the ConfigurableObject of User Defined Template Definition   
            
         
        """
        pass
    @property
    def CreatingDeformation(self) -> bool:
        """
        Getter for property: (bool) CreatingDeformation
         Returns the creating deformation of the User Defined Template Definition   
            
         
        """
        pass
    @CreatingDeformation.setter
    def CreatingDeformation(self, isCreatingDeformation: bool):
        """
        Setter for property: (bool) CreatingDeformation
         Returns the creating deformation of the User Defined Template Definition   
            
         
        """
        pass
    def AddEditableExpressions(self, expressions: List[NXOpen.Expression]) -> None:
        """
         Set expressions for user to edit in User Defined Template 
        """
        pass
    def AddObjects(self, objects: List[NXOpen.NXObject]) -> None:
        """
         Add objects user like to add in User Defined Template 
        """
        pass
    def GetEditableExpressions(self) -> List[NXOpen.Expression]:
        """
         Returns the expressions that can be edited in User Defined Template 
         Returns expressions ( NXOpen.Expression Li): .
        """
        pass
    def GetObjects(self) -> List[NXOpen.NXObject]:
        """
         Return objects user added in User Defined Template 
         Returns objects ( NXOpen.NXObject Li): .
        """
        pass
    def GetReferences(self) -> List[NXOpen.NXObject]:
        """
         Returns the references in User Defined Template 
         Returns references ( NXOpen.NXObject Li): .
        """
        pass
    def RemoveEditableExpressions(self, expressions: List[NXOpen.Expression]) -> None:
        """
         Returns the expressions that can be edited in User Defined Template 
        """
        pass
    def RemoveObjects(self, objects: List[NXOpen.NXObject]) -> None:
        """
         Remove objects user added in User Defined Template 
        """
        pass
    def SetObjectVisibility(self, entity: int, isVisble: bool) -> None:
        """
         Set visibility of object user added in User Defined Template 
        """
        pass
    def SetObjects(self, objects: List[NXOpen.NXObject]) -> None:
        """
         Set objects user like to add in User Defined Template 
        """
        pass
import NXOpen
class Definition(NXOpen.NXObject): 
    """ Represents an User Defined Template Definition object """
    def GetObjects(self) -> List[NXOpen.NXObject]:
        """
         Returns the feature in the User Defined Template object 
         Returns objects ( NXOpen.NXObject Li):  .
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Features
class InstantiationBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.UserDefinedTemplate.InstantiationBuilder
    """
    class JaUserdefinedtemplateinstantiationBooleanOption(Enum):
        """
        Members Include: 
         |NotAllowed|  Boolean option is not allowed 
         |NotSet|  Do not do boolean 
         |Unite|  Unite the solids as tools to a selected target 
         |Subtract|  Subtract the solids as tools to a selected target 
         |UserDefined|  Boolean each body based on the author's choice to a selected target 

        """
        NotAllowed: int
        NotSet: int
        Unite: int
        Subtract: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> InstantiationBuilder.JaUserdefinedtemplateinstantiationBooleanOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class JaUserdefinedtemplateinstantiationExplodeOption(Enum):
        """
        Members Include: 
         |NotAllowed|  Explode is not allowed 
         |NotSet|  Do not explode the template 
         |FeatureGroup|  Explode to feature group 
         |DesignGroup|  Explode to design group 

        """
        NotAllowed: int
        NotSet: int
        FeatureGroup: int
        DesignGroup: int
        @staticmethod
        def ValueOf(value: int) -> InstantiationBuilder.JaUserdefinedtemplateinstantiationExplodeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class JaUserdefinedtemplateinstantiationLayerOption(Enum):
        """
        Members Include: 
         |Work|  Outputs will follow the work parts layer convention 
         |Original|  Outputs will be in the same layer as in authoring part 
         |Specify|  Outputs will be in user specified layer 

        """
        Work: int
        Original: int
        Specify: int
        @staticmethod
        def ValueOf(value: int) -> InstantiationBuilder.JaUserdefinedtemplateinstantiationLayerOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class JaUserdefinedtemplateinstantiationPmiSettingsOption(Enum):
        """
        Members Include: 
         |FromTemplate|  PMI Settings from Template 
         |FromTargetPart|  PMI Settings from Target Part 

        """
        FromTemplate: int
        FromTargetPart: int
        @staticmethod
        def ValueOf(value: int) -> InstantiationBuilder.JaUserdefinedtemplateinstantiationPmiSettingsOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BooleanFlag(self) -> InstantiationBuilder.JaUserdefinedtemplateinstantiationBooleanOption:
        """
        Getter for property: ( InstantiationBuilder.JaUserdefinedtemplateinstantiationBooleanOption NXOpen.UserD) BooleanFlag
         Returns the boolean flag of User Defined Template Instantiation   
            
         
        """
        pass
    @BooleanFlag.setter
    def BooleanFlag(self, booleanFlag: InstantiationBuilder.JaUserdefinedtemplateinstantiationBooleanOption):
        """
        Setter for property: ( InstantiationBuilder.JaUserdefinedtemplateinstantiationBooleanOption NXOpen.UserD) BooleanFlag
         Returns the boolean flag of User Defined Template Instantiation   
            
         
        """
        pass
    @property
    def BooleanTarget(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) BooleanTarget
         Returns the boolean target of User Defined Template Instantiation   
            
         
        """
        pass
    @BooleanTarget.setter
    def BooleanTarget(self, target: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) BooleanTarget
         Returns the boolean target of User Defined Template Instantiation   
            
         
        """
        pass
    @property
    def Component(self) -> NXOpen.Assemblies.Component:
        """
        Getter for property: ( NXOpen.Assemblies.Component) Component
         Returns the occ part of User Defined Template Instantiation   
            
         
        """
        pass
    @Component.setter
    def Component(self, component: NXOpen.Assemblies.Component):
        """
        Setter for property: ( NXOpen.Assemblies.Component) Component
         Returns the occ part of User Defined Template Instantiation   
            
         
        """
        pass
    @property
    def Expandable(self) -> bool:
        """
        Getter for property: (bool) Expandable
         Returns the expand flag of User Defined Template Instantiation   
            
         
        """
        pass
    @property
    def ExplodeFlag(self) -> InstantiationBuilder.JaUserdefinedtemplateinstantiationExplodeOption:
        """
        Getter for property: ( InstantiationBuilder.JaUserdefinedtemplateinstantiationExplodeOption NXOpen.UserD) ExplodeFlag
         Returns the explode flag of User Defined Template Instantiation   
            
         
        """
        pass
    @ExplodeFlag.setter
    def ExplodeFlag(self, explodeFlag: InstantiationBuilder.JaUserdefinedtemplateinstantiationExplodeOption):
        """
        Setter for property: ( InstantiationBuilder.JaUserdefinedtemplateinstantiationExplodeOption NXOpen.UserD) ExplodeFlag
         Returns the explode flag of User Defined Template Instantiation   
            
         
        """
        pass
    @property
    def Explosion(self) -> bool:
        """
        Getter for property: (bool) Explosion
         Returns the property of whether user is allowed to explode User Defined Template instantiation   
            
         
        """
        pass
    @Explosion.setter
    def Explosion(self, is_explodable: bool):
        """
        Setter for property: (bool) Explosion
         Returns the property of whether user is allowed to explode User Defined Template instantiation   
            
         
        """
        pass
    @property
    def ExtraMatchedFlipDir(self) -> bool:
        """
        Getter for property: (bool) ExtraMatchedFlipDir
         Returns the extra matched flip dir for multiple location point relocator   
            
         
        """
        pass
    @ExtraMatchedFlipDir.setter
    def ExtraMatchedFlipDir(self, flip_dir: bool):
        """
        Setter for property: (bool) ExtraMatchedFlipDir
         Returns the extra matched flip dir for multiple location point relocator   
            
         
        """
        pass
    @property
    def ExtraMatchedOriginal(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) ExtraMatchedOriginal
         Returns the extra matched original reference for multiple location point relocator   
            
         
        """
        pass
    @ExtraMatchedOriginal.setter
    def ExtraMatchedOriginal(self, matched_original: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) ExtraMatchedOriginal
         Returns the extra matched original reference for multiple location point relocator   
            
         
        """
        pass
    @property
    def LayerNumber(self) -> int:
        """
        Getter for property: (int) LayerNumber
         Returns the output layer number user specify for User Defined Template instantiation   
            
         
        """
        pass
    @LayerNumber.setter
    def LayerNumber(self, layer_number: int):
        """
        Setter for property: (int) LayerNumber
         Returns the output layer number user specify for User Defined Template instantiation   
            
         
        """
        pass
    @property
    def LayerOption(self) -> InstantiationBuilder.JaUserdefinedtemplateinstantiationLayerOption:
        """
        Getter for property: ( InstantiationBuilder.JaUserdefinedtemplateinstantiationLayerOption NXOpen.UserD) LayerOption
         Returns the property of output layer option of User Defined Template instantiation   
            
         
        """
        pass
    @LayerOption.setter
    def LayerOption(self, layer_option: InstantiationBuilder.JaUserdefinedtemplateinstantiationLayerOption):
        """
        Setter for property: ( InstantiationBuilder.JaUserdefinedtemplateinstantiationLayerOption NXOpen.UserD) LayerOption
         Returns the property of output layer option of User Defined Template instantiation   
            
         
        """
        pass
    @property
    def PmiSettings(self) -> InstantiationBuilder.JaUserdefinedtemplateinstantiationPmiSettingsOption:
        """
        Getter for property: ( InstantiationBuilder.JaUserdefinedtemplateinstantiationPmiSettingsOption NXOpen.UserD) PmiSettings
         Returns the inherit PMI Settings of User Defined Template Instantiation   
            
         
        """
        pass
    @PmiSettings.setter
    def PmiSettings(self, pmiSettings: InstantiationBuilder.JaUserdefinedtemplateinstantiationPmiSettingsOption):
        """
        Setter for property: ( InstantiationBuilder.JaUserdefinedtemplateinstantiationPmiSettingsOption NXOpen.UserD) PmiSettings
         Returns the inherit PMI Settings of User Defined Template Instantiation   
            
         
        """
        pass
    @property
    def ReplacedFlex(self) -> NXOpen.Features.Feature:
        """
        Getter for property: ( NXOpen.Features.Feature) ReplacedFlex
         Returns the replaced flex feature of User Defined Template Instantiation   
            
         
        """
        pass
    @ReplacedFlex.setter
    def ReplacedFlex(self, replacedFlex: NXOpen.Features.Feature):
        """
        Setter for property: ( NXOpen.Features.Feature) ReplacedFlex
         Returns the replaced flex feature of User Defined Template Instantiation   
            
         
        """
        pass
    @property
    def RepositionCsys(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) RepositionCsys
         Returns the reposition coordinate system of User Defined Template Instantiation   
            
         
        """
        pass
    @RepositionCsys.setter
    def RepositionCsys(self, csys: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) RepositionCsys
         Returns the reposition coordinate system of User Defined Template Instantiation   
            
         
        """
        pass
    def AutomatchReference(self, reference: NXOpen.NXObject, references: List[NXOpen.NXObject], matched_references: List[NXOpen.NXObject], is_directions_flipped: List[bool], do_name_match: bool) -> Tuple[NXOpen.NXObject, bool]:
        """
         Find matching reference based on name or other matched references in User Defined Template Instantiation 
         Returns A tuple consisting of (matched_reference, is_direction_flipped). 
         - matched_reference is:  NXOpen.NXObject.
         - is_direction_flipped is: bool.

        """
        pass
    def GetExpressions(self) -> List[NXOpen.Expression]:
        """
         Returns the expressions in User Defined Template 
         Returns expressions ( NXOpen.Expression Li): .
        """
        pass
    def GetExtraMatchedReferences(self) -> List[NXOpen.NXObject]:
        """
         Get extra matched references as multiple location point relocator 
         Returns matched_references ( NXOpen.NXObject Li): .
        """
        pass
    def GetMatchedExpression(self, original_expression: NXOpen.Expression) -> Tuple[NXOpen.Expression, bool]:
        """
         Returns the matched expression of an original expression in User Defined Template 
         Returns A tuple consisting of (matched_expression, can_be_edited). 
         - matched_expression is:  NXOpen.Expression.
         - can_be_edited is: bool.

        """
        pass
    def GetMatchedReference(self, original_reference: NXOpen.NXObject) -> Tuple[NXOpen.NXObject, bool]:
        """
         Returns the matched reference of an original reference in User Defined Template 
         Returns A tuple consisting of (matched_reference, is_direction_flipped). 
         - matched_reference is:  NXOpen.NXObject.
         - is_direction_flipped is: bool.

        """
        pass
    def GetReferences(self) -> List[NXOpen.NXObject]:
        """
         Returns the references in User Defined Template 
         Returns references ( NXOpen.NXObject Li): .
        """
        pass
    def LoadAuthoringPart(self, authoring_part_name: str) -> NXOpen.Part:
        """
         Return the authoring part of User Defined Template object 
         Returns authroing_template_part ( NXOpen.Part): .
        """
        pass
    def SetExtraMatchedReferences(self, matched_references: List[NXOpen.NXObject]) -> None:
        """
         Returns extra matched references as multiple location point relocator 
        """
        pass
    def SetMatchedReference(self, original_reference: NXOpen.NXObject, matched_reference: NXOpen.NXObject, flip_direction: bool) -> None:
        """
         Set the matched reference of an original reference in User Defined Template 
        """
        pass
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
class Instantiation(NXOpen.NXObject): 
    """ Represents an User Defined Template Instantiation object """
    def GetExpressions(self) -> List[NXOpen.Expression]:
        """
         Returns the expressions created by the User Defined Template Instantiation object 
         Returns expressions ( NXOpen.Expression Li):  .
        """
        pass
    def GetFeature(self) -> NXOpen.Features.Feature:
        """
         Returns the feature associated with the user defined template object 
         Returns feature ( NXOpen.Features.Feature):  .
        """
        pass
    def GetObjects(self) -> List[NXOpen.NXObject]:
        """
         Returns the feature in the User Defined Template object 
         Returns objects ( NXOpen.NXObject Li):  .
        """
        pass
    def GetPmis(self) -> List[NXOpen.Annotations.Annotation]:
        """
         Returns the PMIs created by the User Defined Template Instantiation object 
         Returns pmis ( NXOpen.Annotations.Annotation Li):  .
        """
        pass
class ItemNodeArrangement(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeArrangement """
    pass
import NXOpen
class ItemNodeBody(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeBody """
    def SetEntityObject(self, entity: NXOpen.NXObject) -> None:
        """
         Sets the entity object.
        """
        pass
class ItemNodeBoolean(ItemNodeExpression): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeBoolean """
    pass
class ItemNodeButton(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeButton """
    pass
import NXOpen
class ItemNodeCae(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeCae """
    def SetEntityObject(self, entity: NXOpen.NXObject) -> None:
        """
         Sets the entity object.
        """
        pass
import NXOpen
class ItemNodeComponent(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeComponent """
    def SetComponent(self, entity: NXOpen.NXObject) -> None:
        """
         Sets the assembly component.
        """
        pass
import NXOpen
class ItemNodeEclassCsys(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeEclassCsys """
    def SetCsys(self, point: NXOpen.NXObject) -> None:
        """
         Sets the Datum CSYS feature for the item node.
        """
        pass
import NXOpen
class ItemNodeEclassDatumAxis(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeEclassDatumAxis """
    def SetDatumAxis(self, point: NXOpen.NXObject) -> None:
        """
         Sets the Datum Axis feature for the item node.
        """
        pass
    def SetRefDatumAxis(self, refDatumAxis: NXOpen.NXObject) -> None:
        """
         Sets the reference Datum Axis (used for UI selection) for the item node.
        """
        pass
import NXOpen
class ItemNodeEclassPoint(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeEclassPoint """
    def SetPoint(self, point: NXOpen.NXObject) -> None:
        """
         Sets the Datum Axis feature for the item node.
        """
        pass
class ItemNodeEclassValueRange(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeEclassValueRange """
    def GetValues(self) -> Tuple[int, float, float, float, float]:
        """
         Gets the value from the item node ECLASS Value Range 
         Returns A tuple consisting of (valueRangeType, minValue, maxValue, nominalValue, typicalValue). 
         - valueRangeType is: int.
         - minValue is: float. .
         - maxValue is: float. .
         - nominalValue is: float. .
         - typicalValue is: float. .

        """
        pass
    def SetValues(self, valueRangeType: int, minValue: float, maxValue: float, nominalValue: float, typicalValue: float) -> None:
        """
         Sets the value for the item node ECLASS Value Range 
        """
        pass
class ItemNodeExplode(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeExplode """
    pass
import NXOpen
class ItemNodeExpression(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeExpression """
    def SetReferenceExpression(self, expression: NXOpen.Expression) -> None:
        """
         Sets the reference expression for a expression item.
        """
        pass
import NXOpen
class ItemNodeExtract(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeExtract """
    def SetExtract(self, extract: NXOpen.NXObject) -> None:
        """
         Sets the entity object.
        """
        pass
class ItemNodeFamily(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeFamily """
    def CreateFamilyData(self) -> None:
        """
         Create family data used for refine 
        """
        pass
    def FreeFamilyData(self) -> None:
        """
         Clean up family data used for refine 
        """
        pass
    def RefineFamilyMember(self, instance_index: int, name: str, member_index: int) -> None:
        """
         Action to refine family members. 
        """
        pass
    def UpdateFamilyData(self) -> None:
        """
         Update family data used for refine 
        """
        pass
import NXOpen
class ItemNodeFeaBody(ItemNodeCae): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeFeaBody """
    def SetMaterial(self, material: NXOpen.NXObject) -> None:
        """
         Sets the body material.
        """
        pass
class ItemNodeFeaLoad(ItemNodeCae): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeFeaLoad """
    pass
class ItemNodeFeaMesh(ItemNodeCae): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeFeaMesh """
    pass
class ItemNodeFeaSolution(ItemNodeCae): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeFeaSolution """
    pass
class ItemNodeFeatureBoolean(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeFeatureBoolean """
    pass
import NXOpen
class ItemNodeGeometry(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeGeometry """
    def SetWaveLink(self, waveLink: NXOpen.NXObject) -> None:
        """
         Sets the entity object.
        """
        pass
class ItemNodeGroup(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeGroup """
    @property
    def Expanded(self) -> bool:
        """
        Getter for property: (bool) Expanded
         Returns the expand state of the group.  
             
         
        """
        pass
    @Expanded.setter
    def Expanded(self, expanded: bool):
        """
        Setter for property: (bool) Expanded
         Returns the expand state of the group.  
             
         
        """
        pass
class ItemNodeInteger(ItemNodeExpression): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeInteger """
    pass
class ItemNodeLabel(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeLabel """
    pass
class ItemNodeLayerOption(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeLayerOption """
    pass
class ItemNodeLayer(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeLayer """
    def UpdateLayerSetting(self, categoryName: str) -> None:
        """
         Update layer setting 
        """
        pass
class ItemNodeMotionBushing(ItemNodeCae): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeMotionBushing """
    pass
class ItemNodeMotionDamper(ItemNodeCae): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeMotionDamper """
    pass
class ItemNodeMotionForce(ItemNodeCae): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeMotionForce """
    pass
class ItemNodeMotionJoint(ItemNodeCae): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeMotionJoint """
    pass
class ItemNodeMotionLink(ItemNodeCae): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeMotionLink """
    pass
class ItemNodeMotionMotor(ItemNodeCae): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeMotionMotor """
    pass
class ItemNodeMotionPackaging(ItemNodeCae): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeMotionPackaging """
    pass
class ItemNodeMotionSolution(ItemNodeCae): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeMotionSolution """
    class Action(Enum):
        """
        Members Include: 
         |ShowGraph|   
         |NextGraph|   
         |ReturnToModel|   
         |RunSolver|  

        """
        ShowGraph: int
        NextGraph: int
        ReturnToModel: int
        RunSolver: int
        @staticmethod
        def ValueOf(value: int) -> ItemNodeMotionSolution.Action:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def CloseGraphWindows(self) -> None:
        """
         Closes graphing windows.
        """
        pass
    def ExecuteAction(self, action: ItemNodeMotionSolution.Action) -> None:
        """
         Execute Graphing button action.
        """
        pass
class ItemNodeMotionSpring(ItemNodeCae): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeMotionSpring """
    pass
class ItemNodeMotionTorque(ItemNodeCae): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeMotionTorque """
    pass
class ItemNodeNumber(ItemNodeExpression): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeNumber """
    pass
class ItemNodeOptimization(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeOptimization """
    def GetRuleName(self) -> str:
        """
         Set the rule name of the optimization. 
         Returns name (str):  .
        """
        pass
    def SetRuleName(self, name: str) -> None:
        """
         Get the rule name of the optimization. 
        """
        pass
import NXOpen
class ItemNodeParameterTable(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeParameterTable """
    def SetReferenceParameterTable(self, parameterTable: NXOpen.NXObject) -> None:
        """
         Sets the entity object.
        """
        pass
class ItemNodePMISettings(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodePMISettings """
    pass
class ItemNodePointExp(ItemNodeExpression): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodePointExp """
    pass
import NXOpen
class ItemNodePoint(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodePoint """
    def SetPoint(self, point: NXOpen.NXObject) -> None:
        """
         Sets the point feature for the item node.
        """
        pass
class ItemNodePosition(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodePosition """
    pass
import NXOpen
class ItemNodeReference(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeReference """
    def SetAllowCreatedWithoutMatch(self, allowCreatedWithoutMatch: bool) -> None:
        """
         Sets the flag for allowCreatedWithoutMatch.
        """
        pass
    def SetOwningObject(self, objectValue: NXOpen.NXObject) -> None:
        """
         Sets the owning object for highlighting.
        """
        pass
    def SetReferenceObject(self, objectValue: NXOpen.NXObject) -> None:
        """
         Sets the reference object.
        """
        pass
    def SetReferenceObjectName(self, name: str) -> None:
        """
         Sets the reference object name.
        """
        pass
    def SetReferenceType(self, name: str) -> None:
        """
         Sets the reference type.
        """
        pass
class ItemNodeReposition(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeReposition """
    pass
class ItemNodeRouting(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeRouting """
    pass
class ItemNodeSeparator(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeSeparator """
    pass
class ItemNodeSimFeaReport(ItemNodeSim): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeSimFeaReport """
    pass
class ItemNodeSimFeaSolve(ItemNodeSim): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeSimFeaSolve """
    pass
class ItemNodeSimFeaViewer(ItemNodeSim): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeSimFeaViewer """
    pass
class ItemNodeSimFile(ItemNodeSim): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeSimFile """
    def SetFileName(self, fileName: str) -> None:
        """
         Sets the associated file name of a motion object.
        """
        pass
class ItemNodeSimFunction(ItemNodeSim): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeSimFunction """
    def SetFunction(self, functionName: str) -> None:
        """
         Sets the driving function of a motion object.
        """
        pass
class ItemNodeSimMotionButton(ItemNodeSim): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeSimMotionButton """
    pass
class ItemNodeSimMotionGraph(ItemNodeSim): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeSimMotionGraph """
    pass
class ItemNodeSimMotionViewer(ItemNodeSim): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeSimMotionViewer """
    pass
class ItemNodeSimNumber(ItemNodeSim): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeSimNumber """
    def SetDoubleValue(self, dValue: float) -> None:
        """
         Sets the value of a number.
        """
        pass
class ItemNodeSimResult(ItemNodeSim): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeSimResult """
    pass
class ItemNodeSim(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeSim """
    def SetLogicalValue(self, value: bool) -> None:
        """
         Set a logical value for a sim node. 
        """
        pass
import NXOpen
class ItemNodeSketch(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeSketch """
    def SetSketch(self, sketch: NXOpen.NXObject) -> None:
        """
         Sets the entity object.
        """
        pass
class ItemNodeString(ItemNodeExpression): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeString """
    pass
class ItemNodeTab(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeTab """
    pass
import NXOpen
class ItemNodeUDT(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeUDT """
    def SetFeatureGroup(self, featureGroup: NXOpen.NXObject) -> None:
        """
         Sets the entity object.
        """
        pass
class ItemNodeVectorExp(ItemNodeExpression): 
    """ Represents a NXOpen.UserDefinedTemplate.ItemNodeVectorExp """
    pass
class RootNode(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.RootNode """
    @property
    def TemplateType(self) -> int:
        """
        Getter for property: (int) TemplateType
         Returns the type of root template.  
             
         
        """
        pass
    def ExecuteVisualRule(self, visualRuleName: str) -> None:
        """
         Execute a visual rule in the template. 
        """
        pass
    def FixInternalVisualRules(self) -> None:
        """
         Fix internal visual rule commands.
        """
        pass
    def Upgrade(self) -> None:
        """
         Upgrade legacy item.
        """
        pass
import NXOpen
import NXOpen.Features
class TemplateUtils(NXOpen.Object): 
    """ Contains various template utility methods """
    def DeleteReplacedFeature(oldFtFrec: NXOpen.Features.Feature) -> None:
        """
         Delete replaced FT feature 
        """
        pass
    def GetReplacedFeature() -> NXOpen.Features.Feature:
        """
         Replace FT feature 
         Returns oldFtFrec ( NXOpen.Features.Feature): .
        """
        pass
    def SetReplacedFeature(oldFtFrec: NXOpen.Features.Feature) -> None:
        """
         Replace FT feature 
        """
        pass
import NXOpen
class VisualRuleNode(ConfigurableObject): 
    """ Represents a NXOpen.UserDefinedTemplate.VisualRuleNode """
    class NodeType(Enum):
        """
        Members Include: 
         |Start|   
         |Fetch1component|  
         |Fetch1feature|  
         |Fetch1expresion|  
         |Fetchpart|  
         |Fetchfeature|  
         |Fetchbody|  
         |Fetchface|  
         |Fetchsketch|  
         |Fetchobject|  
         |Fetchrefset|  
         |Filterpart|  
         |Filterobject|  
         |Filtergeometry|  
         |Filtersketch|  
         |Filterexpression|  
         |Filterdata|  
         |Filterfeature|  
         |Acthighlight|  
         |Actshowhide|  
         |Actcalculate|  
         |Actconcatenate|  
         |Actvalue|  
         |Actextract|  
         |Actfamilyupdate|  
         |Actnxupdate|  
         |Actsetexpression|  
         |Actsetformula|  
         |Actsetobject|  
         |Actrunvisualrule|  
         |Actevalkfrule|  
         |Actrunmethod|  
         |Actrunjournal|  
         |Actsetattribute|  
         |Actsetlayer|  
         |Actsetcomponent|  
         |Actaddcomponent|  
         |Actremovecomponent|  
         |Actreplacecomponent|  
         |Resultinfowindow|  
         |Resultauthorhtml|  
         |Resultstring|  
         |Resultuilabel|  
         |Resultupdatedialog|  
         |Resultuialert|  
         |Constructconditional|  
         |Constructloop|  
         |Constructloopinput|  
         |Constructswitch|  
         |Constructcompswitch|  
         |Actfit|  

        """
        Start: int
        Fetch1component: int
        Fetch1feature: int
        Fetch1expresion: int
        Fetchpart: int
        Fetchfeature: int
        Fetchbody: int
        Fetchface: int
        Fetchsketch: int
        Fetchobject: int
        Fetchrefset: int
        Filterpart: int
        Filterobject: int
        Filtergeometry: int
        Filtersketch: int
        Filterexpression: int
        Filterdata: int
        Filterfeature: int
        Acthighlight: int
        Actshowhide: int
        Actcalculate: int
        Actconcatenate: int
        Actvalue: int
        Actextract: int
        Actfamilyupdate: int
        Actnxupdate: int
        Actsetexpression: int
        Actsetformula: int
        Actsetobject: int
        Actrunvisualrule: int
        Actevalkfrule: int
        Actrunmethod: int
        Actrunjournal: int
        Actsetattribute: int
        Actsetlayer: int
        Actsetcomponent: int
        Actaddcomponent: int
        Actremovecomponent: int
        Actreplacecomponent: int
        Resultinfowindow: int
        Resultauthorhtml: int
        Resultstring: int
        Resultuilabel: int
        Resultupdatedialog: int
        Resultuialert: int
        Constructconditional: int
        Constructloop: int
        Constructloopinput: int
        Constructswitch: int
        Constructcompswitch: int
        Actfit: int
        @staticmethod
        def ValueOf(value: int) -> VisualRuleNode.NodeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def Connect(self, targetObject: VisualRuleNode) -> None:
        """
         Connect to another visual rule node. 
        """
        pass
    def Disconnect(self, targetObject: VisualRuleNode) -> None:
        """
         Disconnect from another visual rule node. 
        """
        pass
    def GetNodeType(self) -> VisualRuleNode.NodeType:
        """
         Get a visual rule node type. 
         Returns value ( VisualRuleNode.NodeType NXOpen.UserD):  .
        """
        pass
    def SetDescription(self, description: str) -> None:
        """
         Set the visual rule description. 
        """
        pass
    def SetLocation(self, x: float, y: float) -> None:
        """
         Set the visual rule node location. 
        """
        pass
    def SetReferenceObject(self, referenceObject: NXOpen.NXObject) -> None:
        """
         Set the visual rule reference object. 
        """
        pass
    def UpdateDiagram(self) -> None:
        """
         Update visual rule diagram. 
        """
        pass
import NXOpen
class VisualRule(NXOpen.NXObject): 
    """ Represents a NXOpen.UserDefinedTemplate.VisualRule """
    class RuleType(Enum):
        """
        Members Include: 
         |External|  a top level visual rule that can be invoked from actions in the dialog 
         |Internal|  a visual rule that can be called from another visual rule 

        """
        External: int
        Internal: int
        @staticmethod
        def ValueOf(value: int) -> VisualRule.RuleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def CreateRuleNode(self, nodeType: VisualRuleNode.NodeType, xLocation: float, yLocation: float) -> VisualRuleNode:
        """
         Create a visual rule node. 
         Returns ruleNode ( VisualRuleNode NXOpen.UserD):  .
        """
        pass
    def DeleteRuleNode(self, ruleNode: VisualRuleNode) -> None:
        """
         Delete a visual rule node. 
        """
        pass
    def GetRuleName(self) -> str:
        """
         Get the visual rule name. 
         Returns name (str):  .
        """
        pass
    def GetRuleType(self) -> VisualRule.RuleType:
        """
         Get a visual rule type. 
         Returns value ( VisualRule.RuleType NXOpen.UserD):  .
        """
        pass
    def SetRuleName(self, name: str) -> None:
        """
         Set a name of the visual rule. 
        """
        pass
    def SetRuleType(self, value: VisualRule.RuleType) -> None:
        """
         Set the visual rule type. 
        """
        pass

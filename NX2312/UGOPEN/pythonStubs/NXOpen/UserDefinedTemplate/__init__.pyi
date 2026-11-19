from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents a collection of user defined template  <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class Collection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of user defined template """


    ##  Creates a @link NXOpen::UserDefinedTemplate::InstantiationBuilder NXOpen::UserDefinedTemplate::InstantiationBuilder@endlink . 
    ##  @return builder (@link DefinitionBuilder NXOpen.UserDefinedTemplate.DefinitionBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ##  @link NXOpen::UserDefinedTemplate::Definition NXOpen::UserDefinedTemplate::Definition@endlink  to be edited 
    def CreateDefinitionBuilder(part: Collection, user_defined_template_definition: Definition) -> DefinitionBuilder:
        """
         Creates a @link NXOpen::UserDefinedTemplate::InstantiationBuilder NXOpen::UserDefinedTemplate::InstantiationBuilder@endlink . 
         @return builder (@link DefinitionBuilder NXOpen.UserDefinedTemplate.DefinitionBuilder@endlink):  .
        """
        pass
    
    ##  Creates a @link NXOpen::UserDefinedTemplate::InstantiationBuilder NXOpen::UserDefinedTemplate::InstantiationBuilder@endlink . 
    ##  @return builder (@link InstantiationBuilder NXOpen.UserDefinedTemplate.InstantiationBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ##  @link NXOpen::UserDefinedTemplate::Instantiation NXOpen::UserDefinedTemplate::Instantiation@endlink  to be edited 
    def CreateInstantiationBuilder(part: Collection, user_defined_template_instantiation: Instantiation) -> InstantiationBuilder:
        """
         Creates a @link NXOpen::UserDefinedTemplate::InstantiationBuilder NXOpen::UserDefinedTemplate::InstantiationBuilder@endlink . 
         @return builder (@link InstantiationBuilder NXOpen.UserDefinedTemplate.InstantiationBuilder@endlink):  .
        """
        pass
    
    ##  Creates the Part Attribute Object with input parameters 
    ##  @return createdPartAttribute (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  Created Part Attribute object .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ##  Category alias name of a part attribute 
    def CreatePartAttribute(part: Collection, category_alias: str, title_alias: str, value: str, units: str, type: str) -> NXOpen.TaggedObject:
        """
         Creates the Part Attribute Object with input parameters 
         @return createdPartAttribute (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  Created Part Attribute object .
        """
        pass
    
    ##  Creates a relation IMAN_UG_udf between the definition part and the instantiation part in managed mode 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ##  Definition part tag 
    def CreateRelation(part: Collection, sourcePartTag: NXOpen.TaggedObject) -> None:
        """
         Creates a relation IMAN_UG_udf between the definition part and the instantiation part in managed mode 
        """
        pass
    
    ##  Find the User Defined Template Definition object with input name 
    ##  @return result (@link Definition NXOpen.UserDefinedTemplate.Definition@endlink):  User Defined Template Definition object with this identifier .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  Identifier of the User Defined Template Definition object you want 
    def FindDefinitionObject(part: Collection, journal_identifier: str) -> Definition:
        """
         Find the User Defined Template Definition object with input name 
         @return result (@link Definition NXOpen.UserDefinedTemplate.Definition@endlink):  User Defined Template Definition object with this identifier .
        """
        pass
    
    ##  Find the User Defined Template Instantiation object with input name 
    ##  @return result (@link Instantiation NXOpen.UserDefinedTemplate.Instantiation@endlink):  User Defined Template Instantiation object with this identifier .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  Identifier of the User Defined Template Instantiation object you want 
    def FindInstantiationObject(part: Collection, journal_identifier: str) -> Instantiation:
        """
         Find the User Defined Template Instantiation object with input name 
         @return result (@link Instantiation NXOpen.UserDefinedTemplate.Instantiation@endlink):  User Defined Template Instantiation object with this identifier .
        """
        pass
    
    ##  Find the Product Interface Object with input name 
    ##  @return found (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  User Defined Template object with this identifier .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This method has no replacement. It is no longer used or supported.  <br> 

    ## License requirements: None.
    ##  Identifier of the User Defined Template Instantiation object you want 
    def FindObject(part: Collection, journal_identifier: str) -> NXOpen.TaggedObject:
        """
         Find the Product Interface Object with input name 
         @return found (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink):  User Defined Template object with this identifier .
        """
        pass
    
    ##  Sets @link NXOpen::UserDefinedTemplate::InstantiationBuilder NXOpen::UserDefinedTemplate::InstantiationBuilder@endlink  and definition part 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ##  
    def SetBuilderAndDefinitionPart(part: Collection, builder: InstantiationBuilder, definitionPartTag: NXOpen.TaggedObject) -> None:
        """
         Sets @link NXOpen::UserDefinedTemplate::InstantiationBuilder NXOpen::UserDefinedTemplate::InstantiationBuilder@endlink  and definition part 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::UserDefinedTemplate::ConfigurableObject NXOpen::UserDefinedTemplate::ConfigurableObject@endlink   <br> This is the configurable object class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ConfigurableObject(NXOpen.NXObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ConfigurableObject</ja_class> """


    ##  Indicates the type of property for a configuration node 
    ##   
    class PropertyId(Enum):
        """
        Members Include: <Title> <Cue> <Helpcontext> <TemplateName> <TemplateLocation> <AllowExplode> <AllowBoolean> <Expanded> <Name> <FileSystem> <Bitmap> <ItemRevision> <Dataset> <Update> <DisplayStyle> <Values> <TooltipImages> <ReturnType> <OriginPoint> <Vector> <XVector> <ZVector> <Radius> <Positive> <MinValue> <MinInclusive> <MaxValue> <MaxInclusive> <Increment> <DecimalPlaces> <ListExpression> <AllowDynamic> <CheckMismatch> <EnsureValue> <ButtonAction> <DatasetType> <HelpUrl> <Tooltip> <UseAlert> <ExternalLibrary> <ClassName> <MethodName> <Parameters> <VisualRules> <JournalFile> <VisEnabled> <VisType> <VisObject> <VisComparison> <VisValue> <SensEnabled> <SensType> <SensObject> <SensComparison> <SensValue> <TooltipText> <BooleanOrder> <ReferenceBehavior> <ContentVisibility> <Rollback> <Optional> <Target> <ShowHandle> <SelectionScope> <Hd3d> <Hd3dTitle1> <Hd3dUrl1> <Hd3dIcon1> <Hd3dDescription1> <Hd3dAnchor1> <Hd3dTitle2> <Hd3dUrl2> <Hd3dIcon2> <Hd3dDescription2> <Hd3dAnchor2> <Hd3dTitle3> <Hd3dUrl3> <Hd3dIcon3> <Hd3dDescription3> <Hd3dAnchor3> <FreezeWaveUpdate> <EnableCopyClone> <RunRelinker> <RunPartFamilyUpdate> <ShowAssemblyInstances> <UseDropPosition> <LaunchRedefineConstraints> <AllowQuickAccess> <DefaultRefSet> <ActiveRefSet> <ActiveView> <CheckTinyObjects> <CheckMisalignedObjects> <CheckBodyDataStructures> <CheckBodyConsistency> <CheckFaceFaceIntersection> <CheckFaceSmoothness> <CheckFaceSelfIntersection> <CheckFaceSpikesCuts> <CheckEdgeSmoothness> <CheckEdgeTolerances> <CheckOrphanBodies> <CheckInterpartWaveLinks> <CheckInterpartExpressionStatus> <RelinkUnbroken> <IncludeSuppressed> <FaceCurveDirection> <SourceScope> <TargetScope> <RelinkOption> <BreakWaveLinksAfterUpdate> <BreakExpLinksAfterUpdate> <CheckTinyObjectsTol> <CheckTinyObjectsLevel> <CheckTinyObjectsDesc> <CheckMisalignedObjectsTol> <CheckMisalignedObjectsLevel> <CheckMisalignedObjectsDesc> <CheckBodyDataStructuresLevel> <CheckBodyDataStructuresDesc> <CheckBodyConsistencyLevel> <CheckBodyConsistencyDesc> <CheckFaceFaceIntersectionLevel> <CheckFaceFaceIntersectionDesc> <CheckFaceSmoothnessLevel> <CheckFaceSmoothnessDesc> <CheckFaceSelfIntersectionLevel> <CheckFaceSelfIntersectionDesc> <CheckFaceSpikesCutsTol> <CheckFaceSpikesCutsLevel> <CheckFaceSpikesCutsDesc> <CheckEdgeSmoothnessTol> <CheckEdgeSmoothnessLevel> <CheckEdgeSmoothnessDesc> <CheckEdgeTolerancesTol> <CheckEdgeTolerancesLevel> <CheckEdgeTolerancesDesc> <CheckOrphanBodiesRefset> <CheckOrphanBodiesLevel> <CheckOrphanBodiesDesc> <CheckInterpartWaveLinksStatus> <CheckInterpartWaveLinksLevel> <CheckInterpartWaveLinksDesc> <CheckInterpartExpressionStatusLevel> <CheckInterpartExpressionStatusDesc> <LayerCategories> <Preview> <Positioning> <ExternalState> <TemplateOrder> <SmartInitialization> <SmartSource> <SmartName> <ActionExecuteOpen> <ActionExecuteClose> <ActionExecuteValue> <ActionNameOpen> <ActionNameClose> <ActionNameValue> <ComparisonType> <ComparisonName> <ComparisonOperator> <ComparisonValue> <ComparisonCoordinate> <ActionState> <YVector> <Part> <XCoordinate> <YCoordinate> <Maintain> <ReplaceAll> <NameAction> <ReferenceAction> <LayerAction> <Color> <Function> <Operation> <Value> <ActionExecute1> <ActionExecute2> <ActionExecute3> <ActionExecute4> <ActionExecute5> <ActionExecute6> <ActionExecute7> <ActionExecute8> <ActionExecute9> <ActionExecute10> <Operator1> <Operator2> <Operator3> <Operator4> <Operator5> <Operator6> <Operator7> <Operator8> <Operator9> <Operator10> <Value1> <Value2> <Value3> <Value4> <Value5> <Value6> <Value7> <Value8> <Value9> <Value10> <DraftingParts> <MotionParts> <SimParts> <PmiSettings> <ListImages> <PropertyActive> <Units> <PmiCsysActive> <LayerOption> <PmiCsys> <EnableAddConfig> <EnableMinMaxForKeyin> <PartEdited> <EnableMultiPointSelector> <ActionExecute11> <ActionExecute12> <ActionExecute13> <ActionExecute14> <ActionExecute15> <ActionExecute16> <ActionExecute17> <ActionExecute18> <ActionExecute19> <ActionExecute20> <ActionExecute21> <ActionExecute22> <ActionExecute23> <ActionExecute24> <ActionExecute25> <ActionExecute26> <ActionExecute27> <ActionExecute28> <ActionExecute29> <ActionExecute30> <ActionExecute31> <ActionExecute32> <ActionExecute33> <ActionExecute34> <ActionExecute35> <ActionExecute36> <ActionExecute37> <ActionExecute38> <ActionExecute39> <ActionExecute40> <ActionExecute41> <ActionExecute42> <ActionExecute43> <ActionExecute44> <ActionExecute45> <ActionExecute46> <ActionExecute47> <ActionExecute48> <ActionExecute49> <ActionExecute50> <ActionExecute51> <ActionExecute52> <ActionExecute53> <ActionExecute54> <ActionExecute55> <ActionExecute56> <ActionExecute57> <ActionExecute58> <ActionExecute59> <ActionExecute60> <ActionExecute61> <ActionExecute62> <ActionExecute63> <ActionExecute64> <ActionExecute65> <ActionExecute66> <ActionExecute67> <ActionExecute68> <ActionExecute69> <ActionExecute70> <ActionExecute71> <ActionExecute72> <ActionExecute73> <ActionExecute74> <ActionExecute75> <ActionExecute76> <ActionExecute77> <ActionExecute78> <ActionExecute79> <ActionExecute80> <ActionExecute81> <ActionExecute82> <ActionExecute83> <ActionExecute84> <ActionExecute85> <ActionExecute86> <ActionExecute87> <ActionExecute88> <ActionExecute89> <ActionExecute90> <ActionExecute91> <ActionExecute92> <ActionExecute93> <ActionExecute94> <ActionExecute95> <ActionExecute96> <ActionExecute97> <ActionExecute98> <ActionExecute99> <ActionExecute100> <Operator11> <Operator12> <Operator13> <Operator14> <Operator15> <Operator16> <Operator17> <Operator18> <Operator19> <Operator20> <Operator21> <Operator22> <Operator23> <Operator24> <Operator25> <Operator26> <Operator27> <Operator28> <Operator29> <Operator30> <Operator31> <Operator32> <Operator33> <Operator34> <Operator35> <Operator36> <Operator37> <Operator38> <Operator39> <Operator40> <Operator41> <Operator42> <Operator43> <Operator44> <Operator45> <Operator46> <Operator47> <Operator48> <Operator49> <Operator50> <Operator51> <Operator52> <Operator53> <Operator54> <Operator55> <Operator56> <Operator57> <Operator58> <Operator59> <Operator60> <Operator61> <Operator62> <Operator63> <Operator64> <Operator65> <Operator66> <Operator67> <Operator68> <Operator69> <Operator70> <Operator71> <Operator72> <Operator73> <Operator74> <Operator75> <Operator76> <Operator77> <Operator78> <Operator79> <Operator80> <Operator81> <Operator82> <Operator83> <Operator84> <Operator85> <Operator86> <Operator87> <Operator88> <Operator89> <Operator90> <Operator91> <Operator92> <Operator93> <Operator94> <Operator95> <Operator96> <Operator97> <Operator98> <Operator99> <Operator100> <Value11> <Value12> <Value13> <Value14> <Value15> <Value16> <Value17> <Value18> <Value19> <Value20> <Value21> <Value22> <Value23> <Value24> <Value25> <Value26> <Value27> <Value28> <Value29> <Value30> <Value31> <Value32> <Value33> <Value34> <Value35> <Value36> <Value37> <Value38> <Value39> <Value40> <Value41> <Value42> <Value43> <Value44> <Value45> <Value46> <Value47> <Value48> <Value49> <Value50> <Value51> <Value52> <Value53> <Value54> <Value55> <Value56> <Value57> <Value58> <Value59> <Value60> <Value61> <Value62> <Value63> <Value64> <Value65> <Value66> <Value67> <Value68> <Value69> <Value70> <Value71> <Value72> <Value73> <Value74> <Value75> <Value76> <Value77> <Value78> <Value79> <Value80> <Value81> <Value82> <Value83> <Value84> <Value85> <Value86> <Value87> <Value88> <Value89> <Value90> <Value91> <Value92> <Value93> <Value94> <Value95> <Value96> <Value97> <Value98> <Value99> <Value100>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConfigurableObject.PropertyId:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Indicates the type of update to perform 
    ##  
    class UpdateType(Enum):
        """
        Members Include: <NotSet> <ExternalChange> <PartFamily>
        """
        NotSet: int
        ExternalChange: int
        PartFamily: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConfigurableObject.UpdateType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Get a logical parameter of the object. 
    ##  @return value (bool):  .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def GetLogicalParameter(configObject: ConfigurableObject, property_id: ConfigurableObject.PropertyId) -> bool:
        """
         Get a logical parameter of the object. 
         @return value (bool):  .
        """
        pass
    
    ##  Get a menu parameter of the object. 
    ##  @return value (int):  .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def GetMenuParameter(configObject: ConfigurableObject, property_id: ConfigurableObject.PropertyId) -> int:
        """
         Get a menu parameter of the object. 
         @return value (int):  .
        """
        pass
    
    ##  Get a parameter of the object. 
    ##  @return value (str):  .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def GetParameter(configObject: ConfigurableObject, property_id: ConfigurableObject.PropertyId) -> str:
        """
         Get a parameter of the object. 
         @return value (str):  .
        """
        pass
    
    ##  Set a list of choices for the object. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetChoiceParameter(configObject: ConfigurableObject, property_id: ConfigurableObject.PropertyId, choices: List[str]) -> None:
        """
         Set a list of choices for the object. 
        """
        pass
    
    ##  Set a logical parameter of the object. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetLogicalParameter(configObject: ConfigurableObject, property_id: ConfigurableObject.PropertyId, value: bool) -> None:
        """
         Set a logical parameter of the object. 
        """
        pass
    
    ##  Set a menu parameter of the object. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetMenuParameter(configObject: ConfigurableObject, property_id: ConfigurableObject.PropertyId, menuIndex: int) -> None:
        """
         Set a menu parameter of the object. 
        """
        pass
    
    ##  Set a parameter of the object. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetParameter(configObject: ConfigurableObject, property_id: ConfigurableObject.PropertyId, value: str) -> None:
        """
         Set a parameter of the object. 
        """
        pass
    
    ##  Set an object tag for the parameter. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetTagParameter(configObject: ConfigurableObject, property_id: ConfigurableObject.PropertyId, referenceObject: NXOpen.NXObject) -> None:
        """
         Set an object tag for the parameter. 
        """
        pass
    
    ##  Perform an update for a configurable object. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def Update(configObject: ConfigurableObject, updateType: ConfigurableObject.UpdateType) -> None:
        """
         Perform an update for a configurable object. 
        """
        pass
    
import NXOpen
##  Provides methods for manipulating the template studio configuration objects in a part.
##         Inputs to this feature can be convergent objects. <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ConfigurationManager(NXOpen.Object): 
    """ Provides methods for manipulating the template studio configuration objects in a part.
        Inputs to this feature can be convergent objects."""


    ##  Indicates the type of item node being created 
    ##   
    class ItemType(Enum):
        """
        Members Include: <Group> <Tab> <Button> <Label> <Separator> <Layer> <Routing> <Arrangement> <Family> <Number> <String> <Boolean> <Integer> <Reference> <Body> <Sketch> <Geometry> <Extract> <Point> <Position> <Component> <PointExp> <VectorExp> <Optimization> <Feabody> <ParameterTable> <Feaload> <Feamesh> <Feasolution> <Simnumber> <Simfeasolve> <Simfeaviewer> <Simfeareport> <Motionlink> <Motionjoint> <Motionspring> <Motionbushing> <Motiondamper> <Motionforce> <Motiontorque> <Motionmotor> <Motionpackaging> <Motionsolution> <Simresult> <Simfunction> <Simmotionbutton> <Simmotionviewer> <Simmotiongraph> <Simfile> <Udt> <EclassCsys> <EclassDatumaxis> <EclassPoint>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConfigurationManager.ItemType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Indicates where to move the node 
    ##   
    class MoveType(Enum):
        """
        Members Include: <Up> <Down> <Out>
        """
        Up: int
        Down: int
        Out: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConfigurationManager.MoveType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Indicates the type of template being created 
    ##   
    class TemplateType(Enum):
        """
        Members Include: <NotSet> <Pts> <Fts>
        """
        NotSet: int
        Pts: int
        Fts: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConfigurationManager.TemplateType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Create a UI item node for the template configuration dialog.
    ##  @return itemNode (@link ConfigurableObject NXOpen.UserDefinedTemplate.ConfigurableObject@endlink):  .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def CreateItemNode(part: ConfigurationManager, item_type: ConfigurationManager.ItemType) -> ConfigurableObject:
        """
         Create a UI item node for the template configuration dialog.
         @return itemNode (@link ConfigurableObject NXOpen.UserDefinedTemplate.ConfigurableObject@endlink):  .
        """
        pass
    
    ##  Create a root node of the template configuration dialog.
    ##  @return rootNode (@link ConfigurableObject NXOpen.UserDefinedTemplate.ConfigurableObject@endlink):  .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def CreateRootNode(part: ConfigurationManager, template_type: ConfigurationManager.TemplateType) -> ConfigurableObject:
        """
         Create a root node of the template configuration dialog.
         @return rootNode (@link ConfigurableObject NXOpen.UserDefinedTemplate.ConfigurableObject@endlink):  .
        """
        pass
    
    ##  Create a visual rule in a template.
    ##  @return visualRule (@link VisualRule NXOpen.UserDefinedTemplate.VisualRule@endlink):  .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def CreateVisualRule(part: ConfigurationManager, rootNode: ConfigurableObject) -> VisualRule:
        """
         Create a visual rule in a template.
         @return visualRule (@link VisualRule NXOpen.UserDefinedTemplate.VisualRule@endlink):  .
        """
        pass
    
    ##  Delete a visual rule in a template.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def DeleteVisualRule(part: ConfigurationManager, rootNode: ConfigurableObject, ruleName: str) -> None:
        """
         Delete a visual rule in a template.
        """
        pass
    
    ##  Add or move a node in the configuration dialog.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def DragDropNode(part: ConfigurationManager, rootNode: ConfigurableObject, sourceNode: ConfigurableObject, targetNode: ConfigurableObject) -> None:
        """
         Add or move a node in the configuration dialog.
        """
        pass
    
    ##  Find the template root in a part.
    ##  @return rootNode (@link ConfigurableObject NXOpen.UserDefinedTemplate.ConfigurableObject@endlink):  .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRootNode(part: ConfigurationManager) -> ConfigurableObject:
        """
         Find the template root in a part.
         @return rootNode (@link ConfigurableObject NXOpen.UserDefinedTemplate.ConfigurableObject@endlink):  .
        """
        pass
    
    ##  Find the template root in a part by type.
    ##  @return rootNode (@link ConfigurableObject NXOpen.UserDefinedTemplate.ConfigurableObject@endlink):  .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="tempateType"> (int) </param>
    def GetRootNodeByType(part: ConfigurationManager, tempateType: int) -> ConfigurableObject:
        """
         Find the template root in a part by type.
         @return rootNode (@link ConfigurableObject NXOpen.UserDefinedTemplate.ConfigurableObject@endlink):  .
        """
        pass
    
    ##  Load a file into the template studio as an embedded file.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def LoadEmbeddedFile(part: ConfigurationManager, embeddedName: str, filename: str) -> None:
        """
         Load a file into the template studio as an embedded file.
        """
        pass
    
    ##  Move a node up or down in the configuration dialog.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def MoveItemNode(part: ConfigurationManager, move_type: ConfigurationManager.MoveType, sourceNode: ConfigurableObject) -> None:
        """
         Move a node up or down in the configuration dialog.
        """
        pass
    
    ##  Publish PTS data for a part.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ##  
    def PublishPTSData(part: ConfigurationManager, rootNode: ConfigurableObject) -> None:
        """
         Publish PTS data for a part.
        """
        pass
    
    ##  Remove a node in the configuration dialog.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def RemoveItemNode(part: ConfigurationManager, targetNode: ConfigurableObject) -> None:
        """
         Remove a node in the configuration dialog.
        """
        pass
    
    ##  Remove PTS data from a part.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ##  
    def RemovePTSData(part: ConfigurationManager, removeLegacyData: bool) -> None:
        """
         Remove PTS data from a part.
        """
        pass
    
    ##  Transfer embedded files to the target part.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def TransferEmbeddedFiles(part: ConfigurationManager, rootNode: ConfigurableObject, target_part: NXOpen.BasePart) -> None:
        """
         Transfer embedded files to the target part.
        """
        pass
    
    ##  Upgrade legacy PTS requirement checks into the NX requirements and checks.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def UpgradeLegacyChecks(part: ConfigurationManager) -> None:
        """
         Upgrade legacy PTS requirement checks into the NX requirements and checks.
        """
        pass
    
    ##  Upgrade legacy PTS data into the new format.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ##  
    def UpgradeLegacyData(part: ConfigurationManager, rootNode: ConfigurableObject) -> None:
        """
         Upgrade legacy PTS data into the new format.
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::UserDefinedTemplate::DefinitionBuilder NXOpen::UserDefinedTemplate::DefinitionBuilder@endlink 
##      <br> To create a new instance of this class, use @link NXOpen::UserDefinedTemplate::Collection::CreateDefinitionBuilder  NXOpen::UserDefinedTemplate::Collection::CreateDefinitionBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class DefinitionBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.UserDefinedTemplate.DefinitionBuilder</ja_class>
    """


    ## Getter for property: (@link ConfigurableObject NXOpen.UserDefinedTemplate.ConfigurableObject@endlink) ConfigurableObject
    ##   the ConfigurableObject of User Defined Template Definition   
    ##     
    ##  
    ## Getter License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return ConfigurableObject
    @property
    def ConfigurableObject(self) -> ConfigurableObject:
        """
        Getter for property: (@link ConfigurableObject NXOpen.UserDefinedTemplate.ConfigurableObject@endlink) ConfigurableObject
          the ConfigurableObject of User Defined Template Definition   
            
         
        """
        pass
    
    ## Setter for property: (@link ConfigurableObject NXOpen.UserDefinedTemplate.ConfigurableObject@endlink) ConfigurableObject

    ##   the ConfigurableObject of User Defined Template Definition   
    ##     
    ##  
    ## Setter License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ConfigurableObject.setter
    def ConfigurableObject(self, configurableObjectTag: ConfigurableObject):
        """
        Setter for property: (@link ConfigurableObject NXOpen.UserDefinedTemplate.ConfigurableObject@endlink) ConfigurableObject
          the ConfigurableObject of User Defined Template Definition   
            
         
        """
        pass
    
    ##  Set expressions for user to edit in User Defined Template 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="expressions"> (@link NXOpen.Expression List[NXOpen.Expression]@endlink) </param>
    def AddEditableExpressions(builder: DefinitionBuilder, expressions: List[NXOpen.Expression]) -> None:
        """
         Set expressions for user to edit in User Defined Template 
        """
        pass
    
    ##  Add objects user like to add in User Defined Template 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    def AddObjects(builder: DefinitionBuilder, objects: List[NXOpen.NXObject]) -> None:
        """
         Add objects user like to add in User Defined Template 
        """
        pass
    
    ##  Returns the expressions that can be edited in User Defined Template 
    ##  @return expressions (@link NXOpen.Expression List[NXOpen.Expression]@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetEditableExpressions(builder: DefinitionBuilder) -> List[NXOpen.Expression]:
        """
         Returns the expressions that can be edited in User Defined Template 
         @return expressions (@link NXOpen.Expression List[NXOpen.Expression]@endlink): .
        """
        pass
    
    ##  Return objects user added in User Defined Template 
    ##  @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetObjects(builder: DefinitionBuilder) -> List[NXOpen.NXObject]:
        """
         Return objects user added in User Defined Template 
         @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
        """
        pass
    
    ##  Returns the references in User Defined Template 
    ##  @return references (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetReferences(builder: DefinitionBuilder) -> List[NXOpen.NXObject]:
        """
         Returns the references in User Defined Template 
         @return references (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
        """
        pass
    
    ##  Returns the expressions that can be edited in User Defined Template 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="expressions"> (@link NXOpen.Expression List[NXOpen.Expression]@endlink) </param>
    def RemoveEditableExpressions(builder: DefinitionBuilder, expressions: List[NXOpen.Expression]) -> None:
        """
         Returns the expressions that can be edited in User Defined Template 
        """
        pass
    
    ##  Remove objects user added in User Defined Template 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    def RemoveObjects(builder: DefinitionBuilder, objects: List[NXOpen.NXObject]) -> None:
        """
         Remove objects user added in User Defined Template 
        """
        pass
    
    ##  Set visibility of object user added in User Defined Template 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="entity"> (int) </param>
    ## <param name="isVisble"> (bool) </param>
    def SetObjectVisibility(builder: DefinitionBuilder, entity: int, isVisble: bool) -> None:
        """
         Set visibility of object user added in User Defined Template 
        """
        pass
    
    ##  Set objects user like to add in User Defined Template 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    def SetObjects(builder: DefinitionBuilder, objects: List[NXOpen.NXObject]) -> None:
        """
         Set objects user like to add in User Defined Template 
        """
        pass
    
import NXOpen
##  Represents an User Defined Template Definition object  <br> To create or edit an instance of this class, use @link NXOpen::UserDefinedTemplate::DefinitionBuilder  NXOpen::UserDefinedTemplate::DefinitionBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class Definition(NXOpen.NXObject): 
    """ Represents an User Defined Template Definition object """


    ##  Returns the feature in the User Defined Template object 
    ##  @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetObjects(definitions_object: Definition) -> List[NXOpen.NXObject]:
        """
         Returns the feature in the User Defined Template object 
         @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  .
        """
        pass
    
import NXOpen
## 
##     Represents a @link NXOpen::UserDefinedTemplate::InstantiationBuilder NXOpen::UserDefinedTemplate::InstantiationBuilder@endlink 
##      <br> To create a new instance of this class, use @link NXOpen::UserDefinedTemplate::Collection::CreateInstantiationBuilder  NXOpen::UserDefinedTemplate::Collection::CreateInstantiationBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class InstantiationBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.UserDefinedTemplate.InstantiationBuilder</ja_class>
    """


    ##  Boolean options 
    ##  Boolean option is not allowed 
    class JaUserdefinedtemplateinstantiationBooleanOption(Enum):
        """
        Members Include: <NotAllowed> <NotSet> <Unite> <Subtract> <UserDefined>
        """
        NotAllowed: int
        NotSet: int
        Unite: int
        Subtract: int
        UserDefined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> InstantiationBuilder.JaUserdefinedtemplateinstantiationBooleanOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Explode options 
    ##  Explode is not allowed 
    class JaUserdefinedtemplateinstantiationExplodeOption(Enum):
        """
        Members Include: <NotAllowed> <NotSet> <FeatureGroup> <DesignGroup>
        """
        NotAllowed: int
        NotSet: int
        FeatureGroup: int
        DesignGroup: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> InstantiationBuilder.JaUserdefinedtemplateinstantiationExplodeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Output layer options 
    ##  Outputs will follow the work parts layer convention 
    class JaUserdefinedtemplateinstantiationLayerOption(Enum):
        """
        Members Include: <Work> <Original> <Specify>
        """
        Work: int
        Original: int
        Specify: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> InstantiationBuilder.JaUserdefinedtemplateinstantiationLayerOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  PMI Settings options 
    ##  PMI Settings from Template 
    class JaUserdefinedtemplateinstantiationPmiSettingsOption(Enum):
        """
        Members Include: <FromTemplate> <FromTargetPart>
        """
        FromTemplate: int
        FromTargetPart: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> InstantiationBuilder.JaUserdefinedtemplateinstantiationPmiSettingsOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link InstantiationBuilder.JaUserdefinedtemplateinstantiationBooleanOption NXOpen.UserDefinedTemplate.InstantiationBuilder.JaUserdefinedtemplateinstantiationBooleanOption@endlink) BooleanFlag
    ##   the boolean flag of User Defined Template Instantiation   
    ##     
    ##  
    ## Getter License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return InstantiationBuilder.JaUserdefinedtemplateinstantiationBooleanOption
    @property
    def BooleanFlag(self) -> InstantiationBuilder.JaUserdefinedtemplateinstantiationBooleanOption:
        """
        Getter for property: (@link InstantiationBuilder.JaUserdefinedtemplateinstantiationBooleanOption NXOpen.UserDefinedTemplate.InstantiationBuilder.JaUserdefinedtemplateinstantiationBooleanOption@endlink) BooleanFlag
          the boolean flag of User Defined Template Instantiation   
            
         
        """
        pass
    
    ## Setter for property: (@link InstantiationBuilder.JaUserdefinedtemplateinstantiationBooleanOption NXOpen.UserDefinedTemplate.InstantiationBuilder.JaUserdefinedtemplateinstantiationBooleanOption@endlink) BooleanFlag

    ##   the boolean flag of User Defined Template Instantiation   
    ##     
    ##  
    ## Setter License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @BooleanFlag.setter
    def BooleanFlag(self, booleanFlag: InstantiationBuilder.JaUserdefinedtemplateinstantiationBooleanOption):
        """
        Setter for property: (@link InstantiationBuilder.JaUserdefinedtemplateinstantiationBooleanOption NXOpen.UserDefinedTemplate.InstantiationBuilder.JaUserdefinedtemplateinstantiationBooleanOption@endlink) BooleanFlag
          the boolean flag of User Defined Template Instantiation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) BooleanTarget
    ##   the boolean target of User Defined Template Instantiation   
    ##     
    ##  
    ## Getter License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.NXObject
    @property
    def BooleanTarget(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) BooleanTarget
          the boolean target of User Defined Template Instantiation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) BooleanTarget

    ##   the boolean target of User Defined Template Instantiation   
    ##     
    ##  
    ## Setter License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @BooleanTarget.setter
    def BooleanTarget(self, target: NXOpen.NXObject):
        """
        Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) BooleanTarget
          the boolean target of User Defined Template Instantiation   
            
         
        """
        pass
    
    ## Getter for property: (bool) Expandable
    ##   the expand flag of User Defined Template Instantiation   
    ##     
    ##  
    ## Getter License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def Expandable(self) -> bool:
        """
        Getter for property: (bool) Expandable
          the expand flag of User Defined Template Instantiation   
            
         
        """
        pass
    
    ## Getter for property: (@link InstantiationBuilder.JaUserdefinedtemplateinstantiationExplodeOption NXOpen.UserDefinedTemplate.InstantiationBuilder.JaUserdefinedtemplateinstantiationExplodeOption@endlink) ExplodeFlag
    ##   the explode flag of User Defined Template Instantiation   
    ##     
    ##  
    ## Getter License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return InstantiationBuilder.JaUserdefinedtemplateinstantiationExplodeOption
    @property
    def ExplodeFlag(self) -> InstantiationBuilder.JaUserdefinedtemplateinstantiationExplodeOption:
        """
        Getter for property: (@link InstantiationBuilder.JaUserdefinedtemplateinstantiationExplodeOption NXOpen.UserDefinedTemplate.InstantiationBuilder.JaUserdefinedtemplateinstantiationExplodeOption@endlink) ExplodeFlag
          the explode flag of User Defined Template Instantiation   
            
         
        """
        pass
    
    ## Setter for property: (@link InstantiationBuilder.JaUserdefinedtemplateinstantiationExplodeOption NXOpen.UserDefinedTemplate.InstantiationBuilder.JaUserdefinedtemplateinstantiationExplodeOption@endlink) ExplodeFlag

    ##   the explode flag of User Defined Template Instantiation   
    ##     
    ##  
    ## Setter License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ExplodeFlag.setter
    def ExplodeFlag(self, explodeFlag: InstantiationBuilder.JaUserdefinedtemplateinstantiationExplodeOption):
        """
        Setter for property: (@link InstantiationBuilder.JaUserdefinedtemplateinstantiationExplodeOption NXOpen.UserDefinedTemplate.InstantiationBuilder.JaUserdefinedtemplateinstantiationExplodeOption@endlink) ExplodeFlag
          the explode flag of User Defined Template Instantiation   
            
         
        """
        pass
    
    ## Getter for property: (bool) Explosion
    ##   the property of whether user is allowed to explode User Defined Template instantiation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This method has no replacement. It is no longer used or supported.  <br> 

    ## @return bool
    @property
    def Explosion(self) -> bool:
        """
        Getter for property: (bool) Explosion
          the property of whether user is allowed to explode User Defined Template instantiation   
            
         
        """
        pass
    
    ## Setter for property: (bool) Explosion

    ##   the property of whether user is allowed to explode User Defined Template instantiation   
    ##     
    ##  
    ## Setter License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This method has no replacement. It is no longer used or supported.  <br> 

    @Explosion.setter
    def Explosion(self, is_explodable: bool):
        """
        Setter for property: (bool) Explosion
          the property of whether user is allowed to explode User Defined Template instantiation   
            
         
        """
        pass
    
    ## Getter for property: (bool) ExtraMatchedFlipDir
    ##   the extra matched flip dir for multiple location point relocator   
    ##     
    ##  
    ## Getter License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def ExtraMatchedFlipDir(self) -> bool:
        """
        Getter for property: (bool) ExtraMatchedFlipDir
          the extra matched flip dir for multiple location point relocator   
            
         
        """
        pass
    
    ## Setter for property: (bool) ExtraMatchedFlipDir

    ##   the extra matched flip dir for multiple location point relocator   
    ##     
    ##  
    ## Setter License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @ExtraMatchedFlipDir.setter
    def ExtraMatchedFlipDir(self, flip_dir: bool):
        """
        Setter for property: (bool) ExtraMatchedFlipDir
          the extra matched flip dir for multiple location point relocator   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) ExtraMatchedOriginal
    ##   the extra matched original reference for multiple location point relocator   
    ##     
    ##  
    ## Getter License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.NXObject
    @property
    def ExtraMatchedOriginal(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) ExtraMatchedOriginal
          the extra matched original reference for multiple location point relocator   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) ExtraMatchedOriginal

    ##   the extra matched original reference for multiple location point relocator   
    ##     
    ##  
    ## Setter License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @ExtraMatchedOriginal.setter
    def ExtraMatchedOriginal(self, matched_original: NXOpen.NXObject):
        """
        Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) ExtraMatchedOriginal
          the extra matched original reference for multiple location point relocator   
            
         
        """
        pass
    
    ## Getter for property: (int) LayerNumber
    ##   the output layer number user specify for User Defined Template instantiation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return int
    @property
    def LayerNumber(self) -> int:
        """
        Getter for property: (int) LayerNumber
          the output layer number user specify for User Defined Template instantiation   
            
         
        """
        pass
    
    ## Setter for property: (int) LayerNumber

    ##   the output layer number user specify for User Defined Template instantiation   
    ##     
    ##  
    ## Setter License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @LayerNumber.setter
    def LayerNumber(self, layer_number: int):
        """
        Setter for property: (int) LayerNumber
          the output layer number user specify for User Defined Template instantiation   
            
         
        """
        pass
    
    ## Getter for property: (@link InstantiationBuilder.JaUserdefinedtemplateinstantiationLayerOption NXOpen.UserDefinedTemplate.InstantiationBuilder.JaUserdefinedtemplateinstantiationLayerOption@endlink) LayerOption
    ##   the property of output layer option of User Defined Template instantiation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return InstantiationBuilder.JaUserdefinedtemplateinstantiationLayerOption
    @property
    def LayerOption(self) -> InstantiationBuilder.JaUserdefinedtemplateinstantiationLayerOption:
        """
        Getter for property: (@link InstantiationBuilder.JaUserdefinedtemplateinstantiationLayerOption NXOpen.UserDefinedTemplate.InstantiationBuilder.JaUserdefinedtemplateinstantiationLayerOption@endlink) LayerOption
          the property of output layer option of User Defined Template instantiation   
            
         
        """
        pass
    
    ## Setter for property: (@link InstantiationBuilder.JaUserdefinedtemplateinstantiationLayerOption NXOpen.UserDefinedTemplate.InstantiationBuilder.JaUserdefinedtemplateinstantiationLayerOption@endlink) LayerOption

    ##   the property of output layer option of User Defined Template instantiation   
    ##     
    ##  
    ## Setter License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @LayerOption.setter
    def LayerOption(self, layer_option: InstantiationBuilder.JaUserdefinedtemplateinstantiationLayerOption):
        """
        Setter for property: (@link InstantiationBuilder.JaUserdefinedtemplateinstantiationLayerOption NXOpen.UserDefinedTemplate.InstantiationBuilder.JaUserdefinedtemplateinstantiationLayerOption@endlink) LayerOption
          the property of output layer option of User Defined Template instantiation   
            
         
        """
        pass
    
    ## Getter for property: (@link InstantiationBuilder.JaUserdefinedtemplateinstantiationPmiSettingsOption NXOpen.UserDefinedTemplate.InstantiationBuilder.JaUserdefinedtemplateinstantiationPmiSettingsOption@endlink) PmiSettings
    ##   the inherit PMI Settings of User Defined Template Instantiation   
    ##     
    ##  
    ## Getter License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return InstantiationBuilder.JaUserdefinedtemplateinstantiationPmiSettingsOption
    @property
    def PmiSettings(self) -> InstantiationBuilder.JaUserdefinedtemplateinstantiationPmiSettingsOption:
        """
        Getter for property: (@link InstantiationBuilder.JaUserdefinedtemplateinstantiationPmiSettingsOption NXOpen.UserDefinedTemplate.InstantiationBuilder.JaUserdefinedtemplateinstantiationPmiSettingsOption@endlink) PmiSettings
          the inherit PMI Settings of User Defined Template Instantiation   
            
         
        """
        pass
    
    ## Setter for property: (@link InstantiationBuilder.JaUserdefinedtemplateinstantiationPmiSettingsOption NXOpen.UserDefinedTemplate.InstantiationBuilder.JaUserdefinedtemplateinstantiationPmiSettingsOption@endlink) PmiSettings

    ##   the inherit PMI Settings of User Defined Template Instantiation   
    ##     
    ##  
    ## Setter License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @PmiSettings.setter
    def PmiSettings(self, pmiSettings: InstantiationBuilder.JaUserdefinedtemplateinstantiationPmiSettingsOption):
        """
        Setter for property: (@link InstantiationBuilder.JaUserdefinedtemplateinstantiationPmiSettingsOption NXOpen.UserDefinedTemplate.InstantiationBuilder.JaUserdefinedtemplateinstantiationPmiSettingsOption@endlink) PmiSettings
          the inherit PMI Settings of User Defined Template Instantiation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) RepositionCsys
    ##   the reposition coordinate system of User Defined Template Instantiation   
    ##     
    ##  
    ## Getter License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.NXObject
    @property
    def RepositionCsys(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) RepositionCsys
          the reposition coordinate system of User Defined Template Instantiation   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) RepositionCsys

    ##   the reposition coordinate system of User Defined Template Instantiation   
    ##     
    ##  
    ## Setter License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @RepositionCsys.setter
    def RepositionCsys(self, csys: NXOpen.NXObject):
        """
        Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) RepositionCsys
          the reposition coordinate system of User Defined Template Instantiation   
            
         
        """
        pass
    
    ##  Find matching reference based on name or other matched references in User Defined Template Instantiation 
    ##  @return A tuple consisting of (matched_reference, is_direction_flipped). 
    ##  - matched_reference is: @link NXOpen.NXObject NXOpen.NXObject@endlink.
    ##  - is_direction_flipped is: bool.

    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ## 
    ## <param name="reference"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="references"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    ## <param name="matched_references"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    ## <param name="is_directions_flipped"> (List[bool]) </param>
    ## <param name="do_name_match"> (bool) </param>
    @staticmethod
    def AutomatchReference(builder: InstantiationBuilder, reference: NXOpen.NXObject, references: List[NXOpen.NXObject], matched_references: List[NXOpen.NXObject], is_directions_flipped: List[bool], do_name_match: bool) -> Tuple[NXOpen.NXObject, bool]:
        """
         Find matching reference based on name or other matched references in User Defined Template Instantiation 
         @return A tuple consisting of (matched_reference, is_direction_flipped). 
         - matched_reference is: @link NXOpen.NXObject NXOpen.NXObject@endlink.
         - is_direction_flipped is: bool.

        """
        pass
    
    ##  Returns the expressions in User Defined Template 
    ##  @return expressions (@link NXOpen.Expression List[NXOpen.Expression]@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetExpressions(builder: InstantiationBuilder) -> List[NXOpen.Expression]:
        """
         Returns the expressions in User Defined Template 
         @return expressions (@link NXOpen.Expression List[NXOpen.Expression]@endlink): .
        """
        pass
    
    ##  Get extra matched references as multiple location point relocator 
    ##  @return matched_references (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: usr_defined_features ("USER DEFINED FEATURES")
    @staticmethod
    def GetExtraMatchedReferences(builder: InstantiationBuilder) -> List[NXOpen.NXObject]:
        """
         Get extra matched references as multiple location point relocator 
         @return matched_references (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
        """
        pass
    
    ##  Returns the matched expression of an original expression in User Defined Template 
    ##  @return A tuple consisting of (matched_expression, can_be_edited). 
    ##  - matched_expression is: @link NXOpen.Expression NXOpen.Expression@endlink.
    ##  - can_be_edited is: bool.

    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="original_expression"> (@link NXOpen.Expression NXOpen.Expression@endlink) </param>
    @staticmethod
    def GetMatchedExpression(builder: InstantiationBuilder, original_expression: NXOpen.Expression) -> Tuple[NXOpen.Expression, bool]:
        """
         Returns the matched expression of an original expression in User Defined Template 
         @return A tuple consisting of (matched_expression, can_be_edited). 
         - matched_expression is: @link NXOpen.Expression NXOpen.Expression@endlink.
         - can_be_edited is: bool.

        """
        pass
    
    ##  Returns the matched reference of an original reference in User Defined Template 
    ##  @return A tuple consisting of (matched_reference, is_direction_flipped). 
    ##  - matched_reference is: @link NXOpen.NXObject NXOpen.NXObject@endlink.
    ##  - is_direction_flipped is: bool.

    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="original_reference"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    @staticmethod
    def GetMatchedReference(builder: InstantiationBuilder, original_reference: NXOpen.NXObject) -> Tuple[NXOpen.NXObject, bool]:
        """
         Returns the matched reference of an original reference in User Defined Template 
         @return A tuple consisting of (matched_reference, is_direction_flipped). 
         - matched_reference is: @link NXOpen.NXObject NXOpen.NXObject@endlink.
         - is_direction_flipped is: bool.

        """
        pass
    
    ##  Returns the references in User Defined Template 
    ##  @return references (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetReferences(builder: InstantiationBuilder) -> List[NXOpen.NXObject]:
        """
         Returns the references in User Defined Template 
         @return references (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
        """
        pass
    
    ##  Return the authoring part of User Defined Template object 
    ##  @return authroing_template_part (@link NXOpen.Part NXOpen.Part@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ##  Name of the authoring part with full path 
    def LoadAuthoringPart(builder: InstantiationBuilder, authoring_part_name: str) -> NXOpen.Part:
        """
         Return the authoring part of User Defined Template object 
         @return authroing_template_part (@link NXOpen.Part NXOpen.Part@endlink): .
        """
        pass
    
    ##  Returns extra matched references as multiple location point relocator 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ## 
    ## <param name="matched_references"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    def SetExtraMatchedReferences(builder: InstantiationBuilder, matched_references: List[NXOpen.NXObject]) -> None:
        """
         Returns extra matched references as multiple location point relocator 
        """
        pass
    
    ##  Set the matched reference of an original reference in User Defined Template 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: usr_defined_features ("USER DEFINED FEATURES")
    ## 
    ## <param name="original_reference"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="matched_reference"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="flip_direction"> (bool) </param>
    def SetMatchedReference(builder: InstantiationBuilder, original_reference: NXOpen.NXObject, matched_reference: NXOpen.NXObject, flip_direction: bool) -> None:
        """
         Set the matched reference of an original reference in User Defined Template 
        """
        pass
    
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
##  Represents an User Defined Template Instantiation object  <br> To create or edit an instance of this class, use @link NXOpen::UserDefinedTemplate::InstantiationBuilder  NXOpen::UserDefinedTemplate::InstantiationBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class Instantiation(NXOpen.NXObject): 
    """ Represents an User Defined Template Instantiation object """


    ##  Returns the expressions created by the User Defined Template Instantiation object 
    ##  @return expressions (@link NXOpen.Expression List[NXOpen.Expression]@endlink):  .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This method has no replacement. It is no longer used or supported.  <br> 

    ## License requirements: None.
    @staticmethod
    def GetExpressions(user_definied_object: Instantiation) -> List[NXOpen.Expression]:
        """
         Returns the expressions created by the User Defined Template Instantiation object 
         @return expressions (@link NXOpen.Expression List[NXOpen.Expression]@endlink):  .
        """
        pass
    
    ##  Returns the feature associated with the user defined template object 
    ##  @return feature (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink):  .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This method has no replacement. It is no longer used or supported.  <br> 

    ## License requirements: None.
    @staticmethod
    def GetFeature(user_definied_object: Instantiation) -> NXOpen.Features.Feature:
        """
         Returns the feature associated with the user defined template object 
         @return feature (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink):  .
        """
        pass
    
    ##  Returns the feature in the User Defined Template object 
    ##  @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetObjects(instantiation_object: Instantiation) -> List[NXOpen.NXObject]:
        """
         Returns the feature in the User Defined Template object 
         @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  .
        """
        pass
    
    ##  Returns the PMIs created by the User Defined Template Instantiation object 
    ##  @return pmis (@link NXOpen.Annotations.Annotation List[NXOpen.Annotations.Annotation]@endlink):  .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  This method has no replacement. It is no longer used or supported.  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPmis(user_definied_object: Instantiation) -> List[NXOpen.Annotations.Annotation]:
        """
         Returns the PMIs created by the User Defined Template Instantiation object 
         @return pmis (@link NXOpen.Annotations.Annotation List[NXOpen.Annotations.Annotation]@endlink):  .
        """
        pass
    
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeArrangement NXOpen::UserDefinedTemplate::ItemNodeArrangement@endlink   <br> This is the arrangement node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeArrangement(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeArrangement</ja_class> """
    pass


import NXOpen
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeBody NXOpen::UserDefinedTemplate::ItemNodeBody@endlink   <br> This is the body node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeBody(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeBody</ja_class> """


    ##  Sets the entity object.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetEntityObject(itemNode: ItemNodeBody, entity: NXOpen.NXObject) -> None:
        """
         Sets the entity object.
        """
        pass
    
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeBoolean NXOpen::UserDefinedTemplate::ItemNodeBoolean@endlink   <br> This is the boolean expression node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeBoolean(ItemNodeExpression): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeBoolean</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeButton NXOpen::UserDefinedTemplate::ItemNodeButton@endlink   <br> This is the button node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeButton(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeButton</ja_class> """
    pass


import NXOpen
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeCae NXOpen::UserDefinedTemplate::ItemNodeCae@endlink   <br> This is the FEA item node base class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeCae(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeCae</ja_class> """


    ##  Sets the entity object.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetEntityObject(itemNode: ItemNodeCae, entity: NXOpen.NXObject) -> None:
        """
         Sets the entity object.
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeComponent NXOpen::UserDefinedTemplate::ItemNodeComponent@endlink   <br> This is the component node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeComponent(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeComponent</ja_class> """


    ##  Sets the assembly component.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetComponent(itemNode: ItemNodeComponent, entity: NXOpen.NXObject) -> None:
        """
         Sets the assembly component.
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeEclassCsys NXOpen::UserDefinedTemplate::ItemNodeEclassCsys@endlink   <br> Use @link NXOpen::UserDefinedTemplate::ConfigurationManager::CreateItemNode NXOpen::UserDefinedTemplate::ConfigurationManager::CreateItemNode@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class ItemNodeEclassCsys(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeEclassCsys</ja_class> """


    ##  Sets the Datum CSYS feature for the item node.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetCsys(itemNode: ItemNodeEclassCsys, point: NXOpen.NXObject) -> None:
        """
         Sets the Datum CSYS feature for the item node.
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeEclassDatumAxis NXOpen::UserDefinedTemplate::ItemNodeEclassDatumAxis@endlink   <br> Use @link NXOpen::UserDefinedTemplate::ConfigurationManager::CreateItemNode NXOpen::UserDefinedTemplate::ConfigurationManager::CreateItemNode@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class ItemNodeEclassDatumAxis(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeEclassDatumAxis</ja_class> """


    ##  Sets the Datum Axis feature for the item node.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetDatumAxis(itemNode: ItemNodeEclassDatumAxis, point: NXOpen.NXObject) -> None:
        """
         Sets the Datum Axis feature for the item node.
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeEclassPoint NXOpen::UserDefinedTemplate::ItemNodeEclassPoint@endlink   <br> Use @link NXOpen::UserDefinedTemplate::ConfigurationManager::CreateItemNode NXOpen::UserDefinedTemplate::ConfigurationManager::CreateItemNode@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class ItemNodeEclassPoint(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeEclassPoint</ja_class> """


    ##  Sets the Datum Axis feature for the item node.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetPoint(itemNode: ItemNodeEclassPoint, point: NXOpen.NXObject) -> None:
        """
         Sets the Datum Axis feature for the item node.
        """
        pass
    
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeExplode NXOpen::UserDefinedTemplate::ItemNodeExplode@endlink   <br> This is the feature explode node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeExplode(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeExplode</ja_class> """
    pass


import NXOpen
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeExpression NXOpen::UserDefinedTemplate::ItemNodeExpression@endlink   <br> This is the number expression node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeExpression(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeExpression</ja_class> """


    ##  Sets the reference expression for a expression item.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetReferenceExpression(itemNode: ItemNodeExpression, expression: NXOpen.Expression) -> None:
        """
         Sets the reference expression for a expression item.
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeExtract NXOpen::UserDefinedTemplate::ItemNodeExtract@endlink   <br> This is the extract node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeExtract(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeExtract</ja_class> """


    ##  Sets the entity object.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetExtract(itemNode: ItemNodeExtract, extract: NXOpen.NXObject) -> None:
        """
         Sets the entity object.
        """
        pass
    
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeFamily NXOpen::UserDefinedTemplate::ItemNodeFamily@endlink   <br> This is the part family node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeFamily(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeFamily</ja_class> """


    ##  Create family data used for refine 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    def CreateFamilyData(configObject: ItemNodeFamily) -> None:
        """
         Create family data used for refine 
        """
        pass
    
    ##  Clean up family data used for refine 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def FreeFamilyData(configObject: ItemNodeFamily) -> None:
        """
         Clean up family data used for refine 
        """
        pass
    
    ##  Action to refine family members. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  index into family data 
    def RefineFamilyMember(configObject: ItemNodeFamily, instance_index: int, name: str, member_index: int) -> None:
        """
         Action to refine family members. 
        """
        pass
    
    ##  Update family data used for refine 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def UpdateFamilyData(configObject: ItemNodeFamily) -> None:
        """
         Update family data used for refine 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeFeaBody NXOpen::UserDefinedTemplate::ItemNodeFeaBody@endlink   <br> This is the FEA body item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeFeaBody(ItemNodeCae): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeFeaBody</ja_class> """


    ##  Sets the body material.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetMaterial(itemNode: ItemNodeFeaBody, material: NXOpen.NXObject) -> None:
        """
         Sets the body material.
        """
        pass
    
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeFeaLoad NXOpen::UserDefinedTemplate::ItemNodeFeaLoad@endlink   <br> This is the FEA load and constraint item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeFeaLoad(ItemNodeCae): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeFeaLoad</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeFeaMesh NXOpen::UserDefinedTemplate::ItemNodeFeaMesh@endlink   <br> This is the FEA mesh item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeFeaMesh(ItemNodeCae): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeFeaMesh</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeFeaSolution NXOpen::UserDefinedTemplate::ItemNodeFeaSolution@endlink   <br> This is the FEA mesh item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeFeaSolution(ItemNodeCae): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeFeaSolution</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeFeatureBoolean NXOpen::UserDefinedTemplate::ItemNodeFeatureBoolean@endlink   <br> This is the feature boolean operation node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeFeatureBoolean(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeFeatureBoolean</ja_class> """
    pass


import NXOpen
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeGeometry NXOpen::UserDefinedTemplate::ItemNodeGeometry@endlink   <br> This is the Geometry node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeGeometry(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeGeometry</ja_class> """


    ##  Sets the entity object.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetWaveLink(itemNode: ItemNodeGeometry, waveLink: NXOpen.NXObject) -> None:
        """
         Sets the entity object.
        """
        pass
    
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeGroup NXOpen::UserDefinedTemplate::ItemNodeGroup@endlink   <br> This is the collapsible group node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeGroup(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeGroup</ja_class> """


    ## Getter for property: (bool) Expanded
    ##   the expand state of the group.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def Expanded(self) -> bool:
        """
        Getter for property: (bool) Expanded
          the expand state of the group.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Expanded

    ##   the expand state of the group.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @Expanded.setter
    def Expanded(self, expanded: bool):
        """
        Setter for property: (bool) Expanded
          the expand state of the group.  
             
         
        """
        pass
    
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeInteger NXOpen::UserDefinedTemplate::ItemNodeInteger@endlink   <br> This is the integer expression node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeInteger(ItemNodeExpression): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeInteger</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeLabel NXOpen::UserDefinedTemplate::ItemNodeLabel@endlink   <br> This is the collapsible label node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeLabel(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeLabel</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeLayerOption NXOpen::UserDefinedTemplate::ItemNodeLayerOption@endlink   <br> This is the feature layer option node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeLayerOption(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeLayerOption</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeLayer NXOpen::UserDefinedTemplate::ItemNodeLayer@endlink   <br> This is the collapsible layer node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeLayer(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeLayer</ja_class> """


    ##  Update layer setting 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  category name 
    def UpdateLayerSetting(configObject: ItemNodeLayer, categoryName: str) -> None:
        """
         Update layer setting 
        """
        pass
    
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeMotionBushing NXOpen::UserDefinedTemplate::ItemNodeMotionBushing@endlink   <br> This is the Motion bushing item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeMotionBushing(ItemNodeCae): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeMotionBushing</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeMotionDamper NXOpen::UserDefinedTemplate::ItemNodeMotionDamper@endlink   <br> This is the Motion damper item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeMotionDamper(ItemNodeCae): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeMotionDamper</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeMotionForce NXOpen::UserDefinedTemplate::ItemNodeMotionForce@endlink   <br> This is the Motion scalar force item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeMotionForce(ItemNodeCae): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeMotionForce</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeMotionJoint NXOpen::UserDefinedTemplate::ItemNodeMotionJoint@endlink   <br> This is the Motion link item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeMotionJoint(ItemNodeCae): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeMotionJoint</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeMotionLink NXOpen::UserDefinedTemplate::ItemNodeMotionLink@endlink   <br> This is the Motion link item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeMotionLink(ItemNodeCae): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeMotionLink</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeMotionMotor NXOpen::UserDefinedTemplate::ItemNodeMotionMotor@endlink   <br> This is the Motion motor item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeMotionMotor(ItemNodeCae): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeMotionMotor</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeMotionPackaging NXOpen::UserDefinedTemplate::ItemNodeMotionPackaging@endlink   <br> This is the Motion packaging item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeMotionPackaging(ItemNodeCae): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeMotionPackaging</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeMotionSolution NXOpen::UserDefinedTemplate::ItemNodeMotionSolution@endlink   <br> This is the Motion Solution item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeMotionSolution(ItemNodeCae): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeMotionSolution</ja_class> """


    ##  Indicates the type of graph action to execute 
    ##   
    class Action(Enum):
        """
        Members Include: <ShowGraph> <NextGraph> <ReturnToModel> <RunSolver>
        """
        ShowGraph: int
        NextGraph: int
        ReturnToModel: int
        RunSolver: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ItemNodeMotionSolution.Action:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Closes graphing windows.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def CloseGraphWindows(itemNode: ItemNodeMotionSolution) -> None:
        """
         Closes graphing windows.
        """
        pass
    
    ##  Execute Graphing button action.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="action"> (@link ItemNodeMotionSolution.Action NXOpen.UserDefinedTemplate.ItemNodeMotionSolution.Action@endlink) </param>
    def ExecuteAction(itemNode: ItemNodeMotionSolution, action: ItemNodeMotionSolution.Action) -> None:
        """
         Execute Graphing button action.
        """
        pass
    
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeMotionSpring NXOpen::UserDefinedTemplate::ItemNodeMotionSpring@endlink   <br> This is the Motion spring item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeMotionSpring(ItemNodeCae): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeMotionSpring</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeMotionTorque NXOpen::UserDefinedTemplate::ItemNodeMotionTorque@endlink   <br> This is the Motion scalar torque item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeMotionTorque(ItemNodeCae): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeMotionTorque</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeNumber NXOpen::UserDefinedTemplate::ItemNodeNumber@endlink   <br> This is the number expression node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeNumber(ItemNodeExpression): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeNumber</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeOptimization NXOpen::UserDefinedTemplate::ItemNodeOptimization@endlink   <br> This is the optimization node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeOptimization(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeOptimization</ja_class> """


    ##  Set the rule name of the optimization. 
    ##  @return name (str):  .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRuleName(optimizationObject: ItemNodeOptimization) -> str:
        """
         Set the rule name of the optimization. 
         @return name (str):  .
        """
        pass
    
    ##  Get the rule name of the optimization. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetRuleName(optimizationObject: ItemNodeOptimization, name: str) -> None:
        """
         Get the rule name of the optimization. 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeParameterTable NXOpen::UserDefinedTemplate::ItemNodeParameterTable@endlink   <br> This is the parameter table node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeParameterTable(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeParameterTable</ja_class> """


    ##  Sets the entity object.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetReferenceParameterTable(itemNode: ItemNodeParameterTable, parameterTable: NXOpen.NXObject) -> None:
        """
         Sets the entity object.
        """
        pass
    
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodePMISettings NXOpen::UserDefinedTemplate::ItemNodePMISettings@endlink   <br> This is the pmi settings node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodePMISettings(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodePMISettings</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodePointExp NXOpen::UserDefinedTemplate::ItemNodePointExp@endlink   <br> This is the point expression node class.  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class ItemNodePointExp(ItemNodeExpression): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodePointExp</ja_class> """
    pass


import NXOpen
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodePoint NXOpen::UserDefinedTemplate::ItemNodePoint@endlink   <br> This is the point feature node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodePoint(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodePoint</ja_class> """


    ##  Sets the point feature for the item node.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetPoint(itemNode: ItemNodePoint, point: NXOpen.NXObject) -> None:
        """
         Sets the point feature for the item node.
        """
        pass
    
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodePosition NXOpen::UserDefinedTemplate::ItemNodePosition@endlink   <br> This is the feature template positioning node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodePosition(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodePosition</ja_class> """
    pass


import NXOpen
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeReference NXOpen::UserDefinedTemplate::ItemNodeReference@endlink   <br> This is the collapsible reference node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeReference(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeReference</ja_class> """


    ##  Sets the flag for allowCreatedWithoutMatch.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetAllowCreatedWithoutMatch(itemNode: ItemNodeReference, allowCreatedWithoutMatch: bool) -> None:
        """
         Sets the flag for allowCreatedWithoutMatch.
        """
        pass
    
    ##  Sets the owning object for highlighting.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetOwningObject(itemNode: ItemNodeReference, objectValue: NXOpen.NXObject) -> None:
        """
         Sets the owning object for highlighting.
        """
        pass
    
    ##  Sets the reference object.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetReferenceObject(itemNode: ItemNodeReference, objectValue: NXOpen.NXObject) -> None:
        """
         Sets the reference object.
        """
        pass
    
    ##  Sets the reference object name.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetReferenceObjectName(itemNode: ItemNodeReference, name: str) -> None:
        """
         Sets the reference object name.
        """
        pass
    
    ##  Sets the reference type.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetReferenceType(itemNode: ItemNodeReference, name: str) -> None:
        """
         Sets the reference type.
        """
        pass
    
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeRouting NXOpen::UserDefinedTemplate::ItemNodeRouting@endlink   <br> This is the collapsible routing node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeRouting(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeRouting</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeSeparator NXOpen::UserDefinedTemplate::ItemNodeSeparator@endlink   <br> This is the separator node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeSeparator(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeSeparator</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeSimFeaReport NXOpen::UserDefinedTemplate::ItemNodeSimFeaReport@endlink   <br> This is the fea solver item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeSimFeaReport(ItemNodeSim): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeSimFeaReport</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeSimFeaSolve NXOpen::UserDefinedTemplate::ItemNodeSimFeaSolve@endlink   <br> This is the fea solver item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeSimFeaSolve(ItemNodeSim): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeSimFeaSolve</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeSimFeaViewer NXOpen::UserDefinedTemplate::ItemNodeSimFeaViewer@endlink   <br> This is the fea solver item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeSimFeaViewer(ItemNodeSim): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeSimFeaViewer</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeSimFile NXOpen::UserDefinedTemplate::ItemNodeSimFile@endlink   <br> This is the driven data file name item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeSimFile(ItemNodeSim): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeSimFile</ja_class> """


    ##  Sets the associated file name of a motion object.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetFileName(itemNode: ItemNodeSimFile, fileName: str) -> None:
        """
         Sets the associated file name of a motion object.
        """
        pass
    
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeSimFunction NXOpen::UserDefinedTemplate::ItemNodeSimFunction@endlink   <br> This is the driven data function item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeSimFunction(ItemNodeSim): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeSimFunction</ja_class> """


    ##  Sets the driving function of a motion object.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetFunction(itemNode: ItemNodeSimFunction, functionName: str) -> None:
        """
         Sets the driving function of a motion object.
        """
        pass
    
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeSimMotionButton NXOpen::UserDefinedTemplate::ItemNodeSimMotionButton@endlink   <br> This is the fea solver item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeSimMotionButton(ItemNodeSim): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeSimMotionButton</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeSimMotionGraph NXOpen::UserDefinedTemplate::ItemNodeSimMotionGraph@endlink   <br> This is the motion graph item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeSimMotionGraph(ItemNodeSim): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeSimMotionGraph</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeSimMotionViewer NXOpen::UserDefinedTemplate::ItemNodeSimMotionViewer@endlink   <br> This is the motion animation item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeSimMotionViewer(ItemNodeSim): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeSimMotionViewer</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeSimNumber NXOpen::UserDefinedTemplate::ItemNodeSimNumber@endlink   <br> This is the driven data number item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeSimNumber(ItemNodeSim): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeSimNumber</ja_class> """


    ##  Sets the value of a number.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetDoubleValue(itemNode: ItemNodeSimNumber, dValue: float) -> None:
        """
         Sets the value of a number.
        """
        pass
    
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeSimResult NXOpen::UserDefinedTemplate::ItemNodeSimResult@endlink   <br> This is the driven data result item node class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeSimResult(ItemNodeSim): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeSimResult</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeSim NXOpen::UserDefinedTemplate::ItemNodeSim@endlink   <br> This is the sim data item node base class.  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ItemNodeSim(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeSim</ja_class> """


    ##  Set a logical value for a sim node. 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="value"> (bool) </param>
    def SetLogicalValue(itemNode: ItemNodeSim, value: bool) -> None:
        """
         Set a logical value for a sim node. 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeSketch NXOpen::UserDefinedTemplate::ItemNodeSketch@endlink   <br> This is the sketch node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeSketch(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeSketch</ja_class> """


    ##  Sets the entity object.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetSketch(itemNode: ItemNodeSketch, sketch: NXOpen.NXObject) -> None:
        """
         Sets the entity object.
        """
        pass
    
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeString NXOpen::UserDefinedTemplate::ItemNodeString@endlink   <br> This is the string expression node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeString(ItemNodeExpression): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeString</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeTab NXOpen::UserDefinedTemplate::ItemNodeTab@endlink   <br> This is the collapsible tab node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ItemNodeTab(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeTab</ja_class> """
    pass


import NXOpen
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeUDT NXOpen::UserDefinedTemplate::ItemNodeUDT@endlink   <br> This is the UDT node class.  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class ItemNodeUDT(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeUDT</ja_class> """


    ##  Sets the entity object.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetFeatureGroup(itemNode: ItemNodeUDT, featureGroup: NXOpen.NXObject) -> None:
        """
         Sets the entity object.
        """
        pass
    
##  Represents a @link NXOpen::UserDefinedTemplate::ItemNodeVectorExp NXOpen::UserDefinedTemplate::ItemNodeVectorExp@endlink   <br> This is the vector expression node class.  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class ItemNodeVectorExp(ItemNodeExpression): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.ItemNodeVectorExp</ja_class> """
    pass


##  Represents a @link NXOpen::UserDefinedTemplate::RootNode NXOpen::UserDefinedTemplate::RootNode@endlink   <br> This is the root node configurable object class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class RootNode(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.RootNode</ja_class> """


    ## Getter for property: (int) TemplateType
    ##   the type of root template.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return int
    @property
    def TemplateType(self) -> int:
        """
        Getter for property: (int) TemplateType
          the type of root template.  
             
         
        """
        pass
    
    ##  Execute a visual rule in the template. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def ExecuteVisualRule(rootObject: RootNode, visualRuleName: str) -> None:
        """
         Execute a visual rule in the template. 
        """
        pass
    
    ##  Fix internal visual rule commands.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def FixInternalVisualRules(rootObject: RootNode) -> None:
        """
         Fix internal visual rule commands.
        """
        pass
    
    ##  Upgrade legacy item.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Upgrade(rootObject: RootNode) -> None:
        """
         Upgrade legacy item.
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::UserDefinedTemplate::VisualRuleNode NXOpen::UserDefinedTemplate::VisualRuleNode@endlink   <br> This is the visual rule node class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class VisualRuleNode(ConfigurableObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.VisualRuleNode</ja_class> """


    ##  Indicates the type of visual rule node being created 
    ##   
    class NodeType(Enum):
        """
        Members Include: <Start> <Fetch1component> <Fetch1feature> <Fetch1expresion> <Fetchpart> <Fetchfeature> <Fetchbody> <Fetchface> <Fetchsketch> <Fetchobject> <Fetchrefset> <Filterpart> <Filterobject> <Filtergeometry> <Filtersketch> <Filterexpression> <Filterdata> <Filterfeature> <Acthighlight> <Actshowhide> <Actcalculate> <Actconcatenate> <Actvalue> <Actextract> <Actfamilyupdate> <Actnxupdate> <Actsetexpression> <Actsetformula> <Actsetobject> <Actrunvisualrule> <Actevalkfrule> <Actrunmethod> <Actrunjournal> <Actsetattribute> <Actsetlayer> <Actsetcomponent> <Actaddcomponent> <Actremovecomponent> <Actreplacecomponent> <Resultinfowindow> <Resultauthorhtml> <Resultstring> <Resultuilabel> <Resultupdatedialog> <Resultuialert> <Constructconditional> <Constructloop> <Constructloopinput> <Constructswitch> <Constructcompswitch> <Actfit>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> VisualRuleNode.NodeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Connect to another visual rule node. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def Connect(nodeObject: VisualRuleNode, targetObject: VisualRuleNode) -> None:
        """
         Connect to another visual rule node. 
        """
        pass
    
    ##  Disconnect from another visual rule node. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def Disconnect(nodeObject: VisualRuleNode, targetObject: VisualRuleNode) -> None:
        """
         Disconnect from another visual rule node. 
        """
        pass
    
    ##  Get a visual rule node type. 
    ##  @return value (@link VisualRuleNode.NodeType NXOpen.UserDefinedTemplate.VisualRuleNode.NodeType@endlink):  .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNodeType(nodeObject: VisualRuleNode) -> VisualRuleNode.NodeType:
        """
         Get a visual rule node type. 
         @return value (@link VisualRuleNode.NodeType NXOpen.UserDefinedTemplate.VisualRuleNode.NodeType@endlink):  .
        """
        pass
    
    ##  Set the visual rule description. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetDescription(nodeObject: VisualRuleNode, description: str) -> None:
        """
         Set the visual rule description. 
        """
        pass
    
    ##  Set the visual rule node location. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetLocation(nodeObject: VisualRuleNode, x: float, y: float) -> None:
        """
         Set the visual rule node location. 
        """
        pass
    
    ##  Set the visual rule reference object. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetReferenceObject(nodeObject: VisualRuleNode, referenceObject: NXOpen.NXObject) -> None:
        """
         Set the visual rule reference object. 
        """
        pass
    
    ##  Update visual rule diagram. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def UpdateDiagram(nodeObject: VisualRuleNode) -> None:
        """
         Update visual rule diagram. 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::UserDefinedTemplate::VisualRule NXOpen::UserDefinedTemplate::VisualRule@endlink   <br> This is the visual rule object class.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class VisualRule(NXOpen.NXObject): 
    """ Represents a <ja_class>NXOpen.UserDefinedTemplate.VisualRule</ja_class> """


    ##  Indicates if the visual rule is external or internal 
    ##  a top level visual rule that can be invoked from actions in the dialog 
    class RuleType(Enum):
        """
        Members Include: <External> <Internal>
        """
        External: int
        Internal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> VisualRule.RuleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Create a visual rule node. 
    ##  @return ruleNode (@link VisualRuleNode NXOpen.UserDefinedTemplate.VisualRuleNode@endlink):  .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def CreateRuleNode(visualRuleObject: VisualRule, nodeType: VisualRuleNode.NodeType, xLocation: float, yLocation: float) -> VisualRuleNode:
        """
         Create a visual rule node. 
         @return ruleNode (@link VisualRuleNode NXOpen.UserDefinedTemplate.VisualRuleNode@endlink):  .
        """
        pass
    
    ##  Delete a visual rule node. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def DeleteRuleNode(visualRuleObject: VisualRule, ruleNode: VisualRuleNode) -> None:
        """
         Delete a visual rule node. 
        """
        pass
    
    ##  Get the visual rule name. 
    ##  @return name (str):  .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRuleName(visualRuleObject: VisualRule) -> str:
        """
         Get the visual rule name. 
         @return name (str):  .
        """
        pass
    
    ##  Get a visual rule type. 
    ##  @return value (@link VisualRule.RuleType NXOpen.UserDefinedTemplate.VisualRule.RuleType@endlink):  .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRuleType(visualRuleObject: VisualRule) -> VisualRule.RuleType:
        """
         Get a visual rule type. 
         @return value (@link VisualRule.RuleType NXOpen.UserDefinedTemplate.VisualRule.RuleType@endlink):  .
        """
        pass
    
    ##  Set a name of the visual rule. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetRuleName(visualRuleObject: VisualRule, name: str) -> None:
        """
         Set a name of the visual rule. 
        """
        pass
    
    ##  Set the visual rule type. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  
    def SetRuleType(visualRuleObject: VisualRule, value: VisualRule.RuleType) -> None:
        """
         Set the visual rule type. 
        """
        pass
    
## @package NXOpen.UserDefinedTemplate
## Classes, Enums and Structs under NXOpen.UserDefinedTemplate namespace

##  @link ConfigurableObjectPropertyId NXOpen.UserDefinedTemplate.ConfigurableObjectPropertyId @endlink is an alias for @link ConfigurableObject.PropertyId NXOpen.UserDefinedTemplate.ConfigurableObject.PropertyId@endlink
ConfigurableObjectPropertyId = ConfigurableObject.PropertyId


##  @link ConfigurableObjectUpdateType NXOpen.UserDefinedTemplate.ConfigurableObjectUpdateType @endlink is an alias for @link ConfigurableObject.UpdateType NXOpen.UserDefinedTemplate.ConfigurableObject.UpdateType@endlink
ConfigurableObjectUpdateType = ConfigurableObject.UpdateType


##  @link ConfigurationManagerItemType NXOpen.UserDefinedTemplate.ConfigurationManagerItemType @endlink is an alias for @link ConfigurationManager.ItemType NXOpen.UserDefinedTemplate.ConfigurationManager.ItemType@endlink
ConfigurationManagerItemType = ConfigurationManager.ItemType


##  @link ConfigurationManagerMoveType NXOpen.UserDefinedTemplate.ConfigurationManagerMoveType @endlink is an alias for @link ConfigurationManager.MoveType NXOpen.UserDefinedTemplate.ConfigurationManager.MoveType@endlink
ConfigurationManagerMoveType = ConfigurationManager.MoveType


##  @link ConfigurationManagerTemplateType NXOpen.UserDefinedTemplate.ConfigurationManagerTemplateType @endlink is an alias for @link ConfigurationManager.TemplateType NXOpen.UserDefinedTemplate.ConfigurationManager.TemplateType@endlink
ConfigurationManagerTemplateType = ConfigurationManager.TemplateType


##  @link InstantiationBuilderJaUserdefinedtemplateinstantiationBooleanOption NXOpen.UserDefinedTemplate.InstantiationBuilderJaUserdefinedtemplateinstantiationBooleanOption @endlink is an alias for @link InstantiationBuilder.JaUserdefinedtemplateinstantiationBooleanOption NXOpen.UserDefinedTemplate.InstantiationBuilder.JaUserdefinedtemplateinstantiationBooleanOption@endlink
InstantiationBuilderJaUserdefinedtemplateinstantiationBooleanOption = InstantiationBuilder.JaUserdefinedtemplateinstantiationBooleanOption


##  @link InstantiationBuilderJaUserdefinedtemplateinstantiationExplodeOption NXOpen.UserDefinedTemplate.InstantiationBuilderJaUserdefinedtemplateinstantiationExplodeOption @endlink is an alias for @link InstantiationBuilder.JaUserdefinedtemplateinstantiationExplodeOption NXOpen.UserDefinedTemplate.InstantiationBuilder.JaUserdefinedtemplateinstantiationExplodeOption@endlink
InstantiationBuilderJaUserdefinedtemplateinstantiationExplodeOption = InstantiationBuilder.JaUserdefinedtemplateinstantiationExplodeOption


##  @link InstantiationBuilderJaUserdefinedtemplateinstantiationLayerOption NXOpen.UserDefinedTemplate.InstantiationBuilderJaUserdefinedtemplateinstantiationLayerOption @endlink is an alias for @link InstantiationBuilder.JaUserdefinedtemplateinstantiationLayerOption NXOpen.UserDefinedTemplate.InstantiationBuilder.JaUserdefinedtemplateinstantiationLayerOption@endlink
InstantiationBuilderJaUserdefinedtemplateinstantiationLayerOption = InstantiationBuilder.JaUserdefinedtemplateinstantiationLayerOption


##  @link InstantiationBuilderJaUserdefinedtemplateinstantiationPmiSettingsOption NXOpen.UserDefinedTemplate.InstantiationBuilderJaUserdefinedtemplateinstantiationPmiSettingsOption @endlink is an alias for @link InstantiationBuilder.JaUserdefinedtemplateinstantiationPmiSettingsOption NXOpen.UserDefinedTemplate.InstantiationBuilder.JaUserdefinedtemplateinstantiationPmiSettingsOption@endlink
InstantiationBuilderJaUserdefinedtemplateinstantiationPmiSettingsOption = InstantiationBuilder.JaUserdefinedtemplateinstantiationPmiSettingsOption


##  @link ItemNodeMotionSolutionAction NXOpen.UserDefinedTemplate.ItemNodeMotionSolutionAction @endlink is an alias for @link ItemNodeMotionSolution.Action NXOpen.UserDefinedTemplate.ItemNodeMotionSolution.Action@endlink
ItemNodeMotionSolutionAction = ItemNodeMotionSolution.Action


##  @link VisualRuleNodeNodeType NXOpen.UserDefinedTemplate.VisualRuleNodeNodeType @endlink is an alias for @link VisualRuleNode.NodeType NXOpen.UserDefinedTemplate.VisualRuleNode.NodeType@endlink
VisualRuleNodeNodeType = VisualRuleNode.NodeType


##  @link VisualRuleRuleType NXOpen.UserDefinedTemplate.VisualRuleRuleType @endlink is an alias for @link VisualRule.RuleType NXOpen.UserDefinedTemplate.VisualRule.RuleType@endlink
VisualRuleRuleType = VisualRule.RuleType



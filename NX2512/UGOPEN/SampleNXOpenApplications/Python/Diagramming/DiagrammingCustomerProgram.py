#===================================================================================================
#
#        Copyright (c) 2023 Siemens Digital Industries Software.
#                            All Rights Reserved.
#
#===================================================================================================
#
#
#    Code Description:
#
#    A simple NX Open Python application program that creates multiple elements(symbols, connections, tables, etc.) on a diagramming sheet.
#===================================================================================================
#
#    Note:
#  
#    NX Development provides the programming example for illustration only.
#    NX Development assumes you are familiar with the programming language
#    demonstrated in the examples, and the tools used to create and debug NX/Open
#    programs.
#===================================================================================================

import math
import NXOpen
import NXOpen.Diagramming
import NXOpen.PDM
import NXOpen.Schematic
def main() : 

    theSession  = NXOpen.Session.GetSession()
    # ----------------------------------------------
    #   Descrition: Create a new diagramming sheet
    # ----------------------------------------------
    
    fileNew1 = theSession.Parts.FileNew()
    
    fileNew1.TemplateFileName = "@DB/Schematic-mm-A0-Size-template/A"
    
    fileNew1.UseBlankTemplate = False
    
    fileNew1.ApplicationName = "DiagrammingTemplate"
    
    fileNew1.Units = NXOpen.Part.Units.Millimeters
    
    fileNew1.RelationType = "master"
    
    fileNew1.UsesMasterModel = "No"
    
    fileNew1.TemplateType = NXOpen.FileNewTemplateType.Item
    
    fileNew1.TemplatePresentationName = "A0 - Size"
    
    fileNew1.ItemType = "NXL0Sheet"
    
    fileNew1.Specialization = ""
    
    fileNew1.SetCanCreateAltrep(False)

    fileNew1.MasterFileName = ""
    
    fileNew1.MakeDisplayedPart = True
    
    fileNew1.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    partOperationCreateBuilder1 = theSession.PdmSession.CreateCreateOperationBuilder(NXOpen.PDM.PartOperationBuilder.OperationType.Create)
    
    fileNew1.SetPartOperationCreateBuilder(partOperationCreateBuilder1)
    
    partOperationCreateBuilder1.SetOperationSubType(NXOpen.PDM.PartOperationCreateBuilder.OperationSubType.FromTemplate)
    
    partOperationCreateBuilder1.SetModelType("master")
    
    partOperationCreateBuilder1.SetItemType("NXL0Sheet")
    
    logicalobjects1 = partOperationCreateBuilder1.CreateLogicalObjects()
    
    partOperationCreateBuilder1.DefaultDestinationFolder = ":Newstuff"
    
    partOperationCreateBuilder1.SetOperationSubType(NXOpen.PDM.PartOperationCreateBuilder.OperationSubType.FromTemplate)
    
    attributetitles1 = [None] * 1 
    attributetitles1[0] = "DB_PART_NO"
    titlepatterns1 = [None] * 1 
    titlepatterns1[0] = "\"SH\"nnnnnn"
    nXObject1 = partOperationCreateBuilder1.CreateAttributeTitleToNamingPatternMap(attributetitles1, titlepatterns1)
    
    objects1 = [NXOpen.NXObject.Null] * 1 
    objects1[0] = logicalobjects1[0]
    properties1 = [NXOpen.NXObject.Null] * 1 
    properties1[0] = nXObject1
    errorList1 = partOperationCreateBuilder1.AutoAssignAttributesWithNamingPattern(objects1, properties1)
 
    partOperationCreateBuilder1.ValidateLogicalObjectsToCommit()
    
    logicalobjects2 = [NXOpen.PDM.LogicalObject.Null] * 1 
    logicalobjects2[0] = logicalobjects1[0]
    partOperationCreateBuilder1.CreateSpecificationsForLogicalObjects(logicalobjects2)
    
    nXObject2 = fileNew1.Commit()
    
    workPart = theSession.Parts.Work

    displayPart = theSession.Parts.Display
    
    fileNew1.Destroy()

    sheet1 = workPart.DiagrammingManager.Sheets.GetWorkSheet()

    theSession.SheetManager.OpenSheet(sheet1)
    
    theSession.SheetManager.ActiveSheet = sheet1
    
    basePart1 = sheet1.OwningPart
    
    # ----------------------------------------------
    #   Descrition: Create a new engine symbol
    # ----------------------------------------------
    
    nodeBuilder1 = workPart.SchematicManager.CreateNodeBuilder(NXOpen.Schematic.Node.Null)
    
    nodeBuilder1.SymbolId = "Engine:4000 hp, Diesel, Engine/A"
    
    nodeBuilder1.SymbolSourceType = NXOpen.Schematic.SymbolSourceOption.ReuseLibrary

    location1 = NXOpen.Point2d(235.0, 360.0)

    nodeBuilder1.SetLocation(location1)
    
    nXObject4 = nodeBuilder1.Commit()
    
    node1 = nodeBuilder1.GetNode()
    
    symbolid1 = nodeBuilder1.SymbolId
    
    annotation1 = node1.Label
    
    connection1 = nodeBuilder1.SplittedConnection
    
    nodeBuilder1.Destroy()
    
    # ----------------------------------------------
    #   Descrition: Create a new tank symbol 
    # ----------------------------------------------
    
    nodeBuilder3 = workPart.SchematicManager.CreateNodeBuilder(NXOpen.Schematic.Node.Null)
    
    nodeBuilder3.SymbolId = "Standard_tank:Standard_tank/A"
    
    nodeBuilder3.SymbolSourceType = NXOpen.Schematic.SymbolSourceOption.ReuseLibrary

    location2 = NXOpen.Point2d(527.5, 502.5)

    nodeBuilder3.SetLocation(location2)
    
    nXObject7 = nodeBuilder3.Commit()
    
    node2 = nodeBuilder3.GetNode()
    
    symbolid2 = nodeBuilder3.SymbolId
    
    annotation2 = node2.Label
    
    connection2 = nodeBuilder3.SplittedConnection
    
    nodeBuilder3.Destroy()
    
    # ----------------------------------------------
    #   Descrition: Create a new nozzle symbol 
    # ----------------------------------------------
    nodeBuilder5 = workPart.SchematicManager.CreateNodeBuilder(NXOpen.Schematic.Node.Null)
    
    nodeBuilder5.NodeType = NXOpen.Schematic.NodeType.Fitting
    
    nodeBuilder5.SymbolId = "General_nozzle:2\" - General nozzle/A"
    
    nodeBuilder5.SymbolSourceType = NXOpen.Schematic.SymbolSourceOption.ReuseLibrary

    location3 = NXOpen.Point2d(514.80000000000007, 502.5)

    nodeBuilder5.SetLocation(location3)
    
    locationBuilder1 = nodeBuilder5.RelativeLocation
    
    locationBuilder1.Reference = node2
    
    locationBuilder1.SetValueX(0.0, 0.0)
    
    locationBuilder1.SetValueY(0.5, 0.0)
    
    nXObject10 = nodeBuilder5.Commit()
    
    node3 = nodeBuilder5.GetNode()
    
    symbolid3 = nodeBuilder5.SymbolId
    
    annotation3 = node3.Label
    
    connection3 = nodeBuilder5.SplittedConnection
    
    nodeBuilder5.Destroy()
    
    # ----------------------------------------------
    #   Descrition: Create a new run 
    # ----------------------------------------------
    
    runBuilder1 = workPart.SchematicManager.RunsManager.CreateRunBuilder(NXOpen.Schematic.Mechanical.Run.Null)
    
    partOperationCreateBuilder2 = theSession.PdmSession.CreateCreateOperationBuilder(NXOpen.PDM.PartOperationBuilder.OperationType.Create)
    
    partOperationCreateBuilder2.SetOperationSubType(NXOpen.PDM.PartOperationCreateBuilder.OperationSubType.CreateSpecification)
    
    partOperationCreateBuilder2.SetModelType("SLM")
    
    partOperationCreateBuilder2.SetItemType("NXL0Run")
    
    runBuilder1.SetPartOperationCreateBuilder(partOperationCreateBuilder2)
    
    partOperationCreateBuilder2.SetOperationSubType(NXOpen.PDM.PartOperationCreateBuilder.OperationSubType.CreateSpecification)
    
    logicalobjects3 = partOperationCreateBuilder2.CreateLogicalObjects()
    
    partOperationCreateBuilder2.DefaultDestinationFolder = ":Newstuff"
    
    partOperationCreateBuilder2.SetOperationSubType(NXOpen.PDM.PartOperationCreateBuilder.OperationSubType.CreateSpecification)
    
    runBuilder1.ObjectApplication = "Schematics"
    
    runBuilder1.Standalone = True

    runBuilder1.Discipline = "Piping"
    
    runBuilder1.Specification = "None"

    runBuilder1.LineType = "Primary"
    
    attributetitles2 = [None] * 1 
    attributetitles2[0] = "DB_PART_NO"
    titlepatterns2 = [None] * 1 
    titlepatterns2[0] = "\"RU\"nnnnnn"
    nXObject12 = partOperationCreateBuilder2.CreateAttributeTitleToNamingPatternMap(attributetitles2, titlepatterns2)
    
    objects2 = [NXOpen.NXObject.Null] * 1 
    objects2[0] = logicalobjects3[0]
    properties2 = [NXOpen.NXObject.Null] * 1 
    properties2[0] = nXObject12
    errorList2 = partOperationCreateBuilder2.AutoAssignAttributesWithNamingPattern(objects2, properties2)
    
    partOperationCreateBuilder2.ValidateLogicalObjectsToCommit()
    
    logicalobjects4 = [NXOpen.PDM.LogicalObject.Null] * 1 
    logicalobjects4[0] = logicalobjects3[0]
    partOperationCreateBuilder2.CreateSpecificationsForLogicalObjects(logicalobjects4)
    
    nXObject13 = partOperationCreateBuilder2.Commit()
    
    nXObject14 = runBuilder1.Commit()
    
    runBuilder1.Destroy()
    
    # ----------------------------------------------
    #   Descrition: Create a new connection
    # ----------------------------------------------
    
    connectionBuilder1 = workPart.SchematicManager.CreateConnectionBuilder(NXOpen.Schematic.Connection.Null)
    
    connectionDataBuilder2 = connectionBuilder1.CreateConnectionData()
    
    connectionDataBuilder2.StockId = ""
    
    connectionDataBuilder2.InsulationId = ""
    
    connectionBuilder1.EnableInstrumentation = False
    
    disciplines1 = [None] * 1 
    disciplines1[0] = "Piping"
    connectionBuilder1.SetDisciplines(disciplines1)
    
    node4 = nXObject4

    port1 = node4.FindObject("Schematic.Port.P1")

    connectionBuilder1.SetStart(port1)
    
    node5 = nXObject10

    port2 = node5.FindObject("Schematic.Port.P1")

    connectionBuilder1.SetEnd(port2)
    
    points1 = [None] * 4 
    points1[0] = NXOpen.Point2d()
    points1[1] = NXOpen.Point2d()
    points1[2] = NXOpen.Point2d()
    points1[3] = NXOpen.Point2d()
    points1[0] = NXOpen.Point2d(254.05000000000001, 343.99800000000005)
    points1[1] = NXOpen.Point2d(259.05000000000001, 343.99800000000005)
    points1[2] = NXOpen.Point2d(259.05000000000001, 502.5)
    points1[3] = NXOpen.Point2d(508.45000000000005, 502.5)
    connectionBuilder1.SetBendPoints(points1)
    
    nXObject20 = connectionBuilder1.Commit()
    
    connection4 = connectionBuilder1.GetConnection()
    
    elementid1 = connectionBuilder1.ElementId
    
    annotation4 = connection4.Label
    
    connectionBuilder1.Destroy()
    
    # ----------------------------------------------
    #   Descrition: Create a new inline -- ball valve
    # ----------------------------------------------

    nodeBuilder7 = workPart.SchematicManager.CreateNodeBuilder(NXOpen.Schematic.Node.Null)
    
    nodeBuilder7.SymbolId = "Ball_valve:2\", Ball valve/A"
    
    nodeBuilder7.SymbolSourceType = NXOpen.Schematic.SymbolSourceOption.ReuseLibrary  

    location4 = NXOpen.Point2d(352.5, 502.5)

    nodeBuilder7.SetLocation(location4)
    
    connection5 = nXObject20

    nodeBuilder7.SetInlineSymbolLocation(connection5, 2, 0.37469927826784272)
    
    nXObject24 = nodeBuilder7.Commit()
    
    node6 = nodeBuilder7.GetNode()
    
    symbolid4 = nodeBuilder7.SymbolId
    
    annotation5 = node6.Label
    
    connection6 = nodeBuilder7.SplittedConnection
    
    nodeBuilder7.Destroy()
    
    # ----------------------------------------------
    #   Descrition: Create a new inline -- ball valve and directly attach to above one
    # ----------------------------------------------

    nodeBuilder8 = workPart.SchematicManager.CreateNodeBuilder(NXOpen.Schematic.Node.Null)
    
    nodeBuilder8.SymbolId = symbolid4
    
    nodeBuilder8.SymbolSourceType = NXOpen.Schematic.SymbolSourceOption.ReuseLibrary
    
    location5 = NXOpen.Point2d(365.20000000000005, 502.5)

    nodeBuilder8.SetLocation(location5)
    
    node7 = nXObject24

    nodeBuilder8.SetAttachedSymbol("P1", node7, "P2")
    
    nXObject26 = nodeBuilder8.Commit()
    
    node8 = nodeBuilder8.GetNode()
    
    symbolid5 = nodeBuilder8.SymbolId
    
    annotation6 = node8.Label
    
    connection7 = nodeBuilder8.SplittedConnection
    
    nodeBuilder8.Destroy()
        
    # ----------------------------------------------
    #   Descrition: Create a new engine symbol
    # ----------------------------------------------

    nodeBuilder10 = workPart.SchematicManager.CreateNodeBuilder(NXOpen.Schematic.Node.Null)
    
    nodeBuilder10.SymbolId = "Engine:8000 hp, Diesel, Engine/A"
    
    nodeBuilder10.SymbolSourceType = NXOpen.Schematic.SymbolSourceOption.ReuseLibrary

    location6 = NXOpen.Point2d(482.5, 327.99600000000004)

    nodeBuilder10.SetLocation(location6)
    
    nXObject29 = nodeBuilder10.Commit()
    
    node9 = nodeBuilder10.GetNode()
    
    symbolid6 = nodeBuilder10.SymbolId
    
    annotation7 = node9.Label
    
    connection8 = nodeBuilder10.SplittedConnection
    
    nodeBuilder10.Destroy()

    # ----------------------------------------------
    #   Descrition: Create a new connection which will generate a tee
    # ----------------------------------------------
    
    connectionBuilder3 = workPart.SchematicManager.CreateConnectionBuilder(NXOpen.Schematic.Connection.Null)
    
    connectionDataBuilder28 = connectionBuilder3.CreateConnectionData()
    
    connectionDataBuilder28.StockId = ""
    
    connectionDataBuilder28.InsulationId = ""
    
    connectionBuilder3.EnableInstrumentation = False
    
    disciplines3 = [None] * 1 
    disciplines3[0] = "Piping"
    connectionBuilder3.SetDisciplines(disciplines3)
    
    #If the tee or junction will not be auto generated, need below code to create it first.
    #This may not always needed for T auto-generated case, but for common case, better to keep it here.
    # --------------- code start ---------------
    teeBuilder1 = connectionBuilder3.CreateStartJunction(NXOpen.Schematic.Node.Null)
    teeBuilder1.SymbolId = "Equal_tee1:T_100_100_V1/A"
    teeBuilder1.SymbolSourceType= NXOpen.Schematic.SymbolSourceOption.ReuseLibrary
    # --------------- code end ---------------

    connectionBuilder3.SetTeeStartLocation(connection5, 1, 0.57413786576825521)
  
    #If the code of the tee builder creation is kept, need below code to destroy the tee builder
    # --------------- code start ---------------
    teeBuilder1.Destroy()
    # --------------- code end ---------------

    node10 = nXObject29

    port3 = node10.FindObject("Schematic.Port.P4")

    connectionBuilder3.SetEnd(port3)
    
    points2 = [None] * 5 
    points2[0] = NXOpen.Point2d()
    points2[1] = NXOpen.Point2d()
    points2[2] = NXOpen.Point2d()
    points2[3] = NXOpen.Point2d()
    points2[4] = NXOpen.Point2d()
    points2[0] = NXOpen.Point2d(259.05000000000001, 435.0)
    points2[1] = NXOpen.Point2d(265.05000000000001, 435.0)
    points2[2] = NXOpen.Point2d(265.05000000000001, 298.94600000000003)
    points2[3] = NXOpen.Point2d(466.49799999999999, 298.94600000000003)
    points2[4] = NXOpen.Point2d(466.49799999999999, 308.94600000000003)
    connectionBuilder3.SetBendPoints(points2)
    
    nXObject37 = connectionBuilder3.Commit()

    connection9 = connectionBuilder3.SplittedConnection
    
    connection10 = connectionBuilder3.GetConnection()
    
    elementid2 = connectionBuilder3.ElementId
    
    annotation8 = connection10.Label

    connectionBuilder3.Destroy()
    
    # ----------------------------------------------
    #   Descrition: Create a flow direction arrow on a connection
    # ----------------------------------------------
    
    flowDirectionArrowBuilder1 = workPart.SchematicManager.CreateFdaBuilder(NXOpen.Diagramming.Node.Null)
    
    flowDirectionArrowBuilder1.LocationPercent = 0.40928676382987184
    
    flowDirectionArrowBuilder1.LocationSegment = 2
    
    connection11 = nXObject37

    flowDirectionArrowBuilder1.SetConnection(connection11)
    
    nXObject40 = flowDirectionArrowBuilder1.Commit()
    
    flowDirectionArrowBuilder1.Destroy() 
    
    # ----------------------------------------------
    #   Descrition: Create anonther new connection
    # ----------------------------------------------
    
    connectionBuilder5 = workPart.SchematicManager.CreateConnectionBuilder(NXOpen.Schematic.Connection.Null)
    
    connectionDataBuilder54 = connectionBuilder5.CreateConnectionData()
    
    connectionDataBuilder54.StockId = ""
    
    connectionDataBuilder54.InsulationId = ""
    
    connectionBuilder5.EnableInstrumentation = False
    
    disciplines5 = [None] * 1 
    disciplines5[0] = "Piping"
    connectionBuilder5.SetDisciplines(disciplines5)

    port4 = node4.FindObject("Schematic.Port.P3")

    connectionBuilder5.SetStart(port4)
 
    points3 = [None] * 3 
    points3[0] = NXOpen.Point2d()
    points3[1] = NXOpen.Point2d()
    points3[2] = NXOpen.Point2d()
    points3[0] = NXOpen.Point2d(251.00200000000001, 340.95000000000005)
    points3[1] = NXOpen.Point2d(251.00200000000001, 290.0)
    points3[2] = NXOpen.Point2d(170.0, 290.0)
    connectionBuilder5.SetBendPoints(points3)
    
    connectionBuilder5.SetEnd(NXOpen.Schematic.Port.Null)
    
    endlocation4 = NXOpen.Point2d(170.0, 290.0)

    connectionBuilder5.SetEndLocation(endlocation4)
    
    nXObject45 = connectionBuilder5.Commit()
    
    connection12 = connectionBuilder5.GetConnection()
    
    elementid3 = connectionBuilder5.ElementId
    
    annotation9 = connection12.Label
    
    connectionBuilder5.Destroy()
    
    # ----------------------------------------------
    #   Descrition: Create a new off sheet connector
    # ----------------------------------------------
    
    offSheetConnectorBuilder1 = workPart.SchematicManager.CreateOffSheetConnectorBuilder(NXOpen.Schematic.OffSheetConnector.Null)
    
    offSheetConnectorBuilder1.Style = NXOpen.Schematic.OffSheetConnectorBuilder.StyleOption.ChevronIn
    
    offSheetConnectorBuilder1.TextStyleBuilder.TextColorFontWidth.TextFont = "Calibri"
    
    fontIndex1 = workPart.Fonts.AddFont("Calibri", NXOpen.FontCollection.Type.Standard)
    
    offSheetConnectorBuilder1.TextStyleBuilder.TextColorFontWidth.TextStyle = "Regular"
    
    location7 = NXOpen.Point2d(170.0, 290.0)

    offSheetConnectorBuilder1.SetLocation(location7)
    
    connection13 = nXObject45

    offSheetConnectorBuilder1.SetConnection(NXOpen.Schematic.ConnectionEndType.End, connection13)
    
    nXObject46 = offSheetConnectorBuilder1.Commit()
    
    offSheetConnectorBuilder1.Destroy()
    
    # ----------------------------------------------
    #   Descrition: Create a new note
    # ----------------------------------------------
    
    cannedAnnotationBuilder1 = workPart.DiagrammingManager.CreateCannedAnnotationBuilder(NXOpen.Diagramming.Annotation.Null)
    
    cannedAnnotationBuilder1.AnnotationBuilder.TextStyleBuilder.TextAlignment = NXOpen.Diagramming.TextStyleBuilder.TextAlignmentType.Center
    
    fontIndex2 = workPart.Fonts.AddFont("Calibri", NXOpen.FontCollection.Type.Standard)
    
    cannedAnnotationBuilder1.AnnotationBuilder.X = 700.0
    
    cannedAnnotationBuilder1.AnnotationBuilder.Y = 272.5
    
    cannedAnnotationBuilder1.AnnotationBuilder.Text = "My Note"
    
    nXObject47 = cannedAnnotationBuilder1.Commit()
    
    cannedAnnotationBuilder1.Destroy()
    
    # ----------------------------------------------
    #   Descrition: Create a new line geometry 
    # ----------------------------------------------
    
    lineBuilder1 = workPart.DiagrammingManager.Lines.CreateLineBuilder(NXOpen.Diagramming.Geometry.Line.Null)
    
    lineBuilder1.Start.Reference = NXOpen.Diagramming.SheetElement.Null
    
    lineBuilder1.Start.InputValueX = 567.5
    
    lineBuilder1.Start.InputValueY = 292.5
    
    lineBuilder1.End.Reference = NXOpen.Diagramming.SheetElement.Null
    
    lineBuilder1.End.InputValueX = 612.5
    
    lineBuilder1.End.InputValueY = 332.5
    
    nXObject48 = lineBuilder1.Commit()
    
    lineBuilder1.Destroy()
 
    # ----------------------------------------------
    #   Descrition: Create a new rectangle geometry 
    # ----------------------------------------------
    
    rectangleBuilder1 = workPart.DiagrammingManager.Rectangles.CreateRectangleBuilder(NXOpen.Diagramming.Geometry.Rectangle.Null)
    
    rectangleBuilder1.FirstCorner.Reference = NXOpen.Diagramming.SheetElement.Null
    
    rectangleBuilder1.FirstCorner.InputValueX = 622.5
    
    rectangleBuilder1.FirstCorner.InputValueY = 292.5
    
    rectangleBuilder1.SecondCorner.Reference = NXOpen.Diagramming.SheetElement.Null
    
    rectangleBuilder1.SecondCorner.InputValueX = 670.0
    
    rectangleBuilder1.SecondCorner.InputValueY = 332.5
    
    nXObject49 = rectangleBuilder1.Commit()
    
    rectangleBuilder1.Destroy()
    
    # ----------------------------------------------
    #   Descrition: Create a new arc geometry
    # ----------------------------------------------
    
    arcBuilder1 = workPart.DiagrammingManager.Arcs.CreateArcBuilder(NXOpen.Diagramming.Geometry.Arc.Null)
 
    arcBuilder1.StartAngle = 5.0822736021898933
    
    arcBuilder1.EndAngle = 8.8886108751872932
    
    arcBuilder1.Radius = 22.519186608146828
    
    arcBuilder1.MinorRadius = 22.519186608146828
    
    arcBuilder1.Center.InputValueX = 714.35913705583755
    
    arcBuilder1.Center.InputValueY = 319.00380710659897
    
    nXObject50 = arcBuilder1.Commit()
    
    arcBuilder1.Destroy()
    
    # ----------------------------------------------
    #   Descrition: Create a new circle geometry 
    # ----------------------------------------------
    
    arcBuilder3 = workPart.DiagrammingManager.Arcs.CreateArcBuilder(NXOpen.Diagramming.Geometry.Arc.Null)
    
    arcBuilder3.Center.Reference = NXOpen.Diagramming.SheetElement.Null
    
    arcBuilder3.Center.InputValueX = 777.5
    
    arcBuilder3.Center.InputValueY = 320.0
    
    arcBuilder3.StartAngle = 3.7295952571373605
    
    arcBuilder3.EndAngle = 3.7295952571373605
    
    arcBuilder3.Radius = 18.027756377319946
    
    nXObject51 = arcBuilder3.Commit()
    
    arcBuilder3.Destroy()
    
    # ----------------------------------------------
    #   Descrition: Create a new profile geometry 
    # ----------------------------------------------
    
    lineBuilder3 = workPart.DiagrammingManager.Lines.CreateLineBuilder(NXOpen.Diagramming.Geometry.Line.Null)
    
    lineBuilder3.Start.InputValueX = 615.0
    
    lineBuilder3.Start.InputValueY = 372.5
    
    lineBuilder3.End.InputValueX = 657.5
    
    lineBuilder3.End.InputValueY = 405.0
    
    nXObject52 = lineBuilder3.Commit()
    
    lineBuilder3.Destroy()
    
    arcBuilder5 = workPart.DiagrammingManager.Arcs.CreateArcBuilder(NXOpen.Diagramming.Geometry.Arc.Null)
    
    arcBuilder5.StartAngle = 4.0595423492838849
    
    arcBuilder5.EndAngle = 7.8633271562820051
    
    arcBuilder5.Radius = 20.899350155305644
    
    arcBuilder5.Center.InputValueX = 670.19531250000068
    
    arcBuilder5.Center.InputValueY = 388.39843750000017
    
    nXObject53 = arcBuilder5.Commit()
    
    arcBuilder5.Destroy()
    
    # ----------------------------------------------
    #   Descrition: Create a new fill on a rectangle geometry 
    # ----------------------------------------------
    
    fillBuilder1 = workPart.DiagrammingManager.Fills.CreateFillBuilder(NXOpen.Diagramming.Fill.Null)
    
    fillBuilder1.SetOwningSheet(sheet1)
    
    fillBuilder1.RenderingProperties.FillPattern = NXOpen.Diagramming.RenderingPropertiesBuilder.FillPatterns.SolidFill
    
    rectangle1 = nXObject49

    added1 = fillBuilder1.Geometries.Add(rectangle1)
    
    nXObject54 = fillBuilder1.Commit()
    
    fillBuilder1.Destroy()

    # ----------------------------------------------
    #   Descrition: Traverse a run from start to end and print out its information in the log file 
    # ----------------------------------------------
    
    theSession.LogFile.WriteLine("----------------Traverse run start----------------")
    
    currentRun = workPart.SchematicManager.RunsManager.GetActiveRun()
    theSession.LogFile.WriteLine("Current run id is "+ currentRun.Identifier)
    branches = currentRun.GetBranches()
    branch_num = len(branches)
    theSession.LogFile.WriteLine("The run has "+ str(branch_num)+" branches")
    n = 0
    while(n < branch_num):
        orderedObjects = branches[n].GetOrderedObjects()
        obj_num = len(orderedObjects)
        theSession.LogFile.WriteLine("The branch "+ branches[n].Identifier+" has "+ str(obj_num)+" objects")
        m = 0
        if(obj_num >0):
            theSession.LogFile.WriteLine("Below is the branch path from start to end:")
        path = ""
        while(m < obj_num):
            objType = info =  ""
            attrOwner = classificationAttrOwner = stockAttrOwner = insulationAttrOwner = None
            if(isinstance(orderedObjects[m], NXOpen.Schematic.Mechanical.Port)):
                objType = "Port"
                junction = orderedObjects[m].GetOwningJunction()
                if(junction is not None):
                    info = "The owning equipment is "+ junction.Identifier+"."

            elif(isinstance(orderedObjects[m], NXOpen.Schematic.Mechanical.Connection)):
                objType = "Connection"
                startPort = orderedObjects[m].GetStart()
                endPort = orderedObjects[m].GetEnd()
                outletJunctions = orderedObjects[m].GetOutletJunctions()
                attrOwner = orderedObjects[m].GetObjectAttributeOwner()
                stockAttrOwner = orderedObjects[m].GetStockAttributeOwner()               
                insulationAttrOwner = orderedObjects[m].GetInsulationAttributeOwner()

                if(startPort is not None):
                    info += "The connection start port is "+ startPort.Identifier+"."
                if(endPort is not None):
                    info += "The connection end port is "+ endPort.Identifier+"."

                junction_num = len(outletJunctions)
                if(junction_num>0):
                    count = 0
                    info += "The connection has "+ str(junction_num)+ " junction(s): "
                    while(count < junction_num):
                        info+= "Junction "+ str(count+1) +" : "+ outletJunctions[count].Identifier
                        if(count < junction_num -1):
                            info+="\n"
                        count+=1
            elif(isinstance(orderedObjects[m], NXOpen.Schematic.Mechanical.Junction)):
                objType = "Node"
                attrOwner = orderedObjects[m].GetObjectAttributeOwner()
                classificationAttrOwner = orderedObjects[m].GetClassificationAttributeOwner()

            theSession.LogFile.WriteLine("Object "+str(m+1)+" : "+ orderedObjects[m].Identifier)
            if(objType !=""):
                theSession.LogFile.WriteLine("Object Type: "+objType)  
            if(info !=""):
                theSession.LogFile.WriteLine("Object info: "+info)  
              
            theSession.LogFile.WriteLine("--------------------------------------------")
            m+=1
        theSession.LogFile.WriteLine(path)
        n+=1

    theSession.LogFile.WriteLine("----------------Traverse run end----------------")

    #----------------------------------------------
    #  Descrition: Create a new tabular note
    #----------------------------------------------

    tableBuilder1 = workPart.DiagrammingManager.Tables.CreateTableBuilder(NXOpen.Diagramming.Tables.Table.Null)
    
    tableBuilder1.InsertRows(0, 5)
    tableBuilder1.InsertColumns(0, 2)
    table = tableBuilder1.Commit()

    ######################below is optional code to set table settings######################
    #set row/column size start
    rowCount =0
    while rowCount< tableBuilder1.GetNumberOfRows():
        rowBuilder = tableBuilder1.GetRow(rowCount)
        rowBuilder.SizingMethod = NXOpen.Diagramming.Tables.SizingMethod.Fixed
        rowBuilder.Size=20.0
        rowCount+=1

    colCount =0
    while colCount< tableBuilder1.GetNumberOfColumns():
        colBuilder = tableBuilder1.GetColumn(colCount)
        colBuilder.SizingMethod = NXOpen.Diagramming.Tables.SizingMethod.Fixed
        colBuilder.Size=50.0
        colCount+=1

    #set anchor location
    tableSettingsBuilder1 = tableBuilder1.TableSettingsBuilder
    tableSettingsBuilder1.AnchorLocation = NXOpen.Diagramming.Tables.AnchorLocation.TopLeft

    #set header location
    tableSettingsBuilder1.HeaderLocation = NXOpen.Diagramming.Tables.HeaderLocation.Start
    tableSettingsBuilder1.HeaderOrientation = NXOpen.Diagramming.Tables.HeaderOrientation.Horizontal

    #set continuous data
    # continuationDataBuilder1 = tableBuilder1.ContinuationDataBuilder
    # continuationDataBuilder1.Location = NXOpen.Diagramming.Tables.ContinuationLocation.Down
    # continuationDataBuilder1.MaximumSize = 25.0
    # continuationDataBuilder1.Spacing = 10.0

    #set locked
    #tableBuilder1.Locked= True

    #set table style
    cellSettingsBuilder1 = tableBuilder1.CellSettingsBuilder
    cellSettingsBuilder1.ContentAlignment = NXOpen.Diagramming.Tables.ContentAlignment.MiddleLeft
    cellSettingsBuilder1.OverflowBehavior = NXOpen.Diagramming.Tables.OverflowBehavior.Truncate

    textStyleBuilder1 = cellSettingsBuilder1.GetContentTextStyle()
    textStyleBuilder1.TextHeight = 4.0
    textStyleBuilder1.TextAllowWrapping = False
    textStyleBuilder1.TruncationMode = NXOpen.Diagramming.TextStyleBuilder.TruncationModes.Trim

    textColorFontWidthBuilder1 = textStyleBuilder1.TextColorFontWidth
    textColorFontWidthBuilder1.TextColor = workPart.Colors.Find("Red")
    textColorFontWidthBuilder1.TextFont = "Calibri"
    textColorFontWidthBuilder1.TextStyle = "Bold"

    rowCount =0
    colCount =0
    while rowCount< tableBuilder1.GetNumberOfRows():
        while colCount < tableBuilder1.GetNumberOfColumns():
            cellBuilder = tableBuilder1.GetCell(rowCount, colCount)
            cellBuilder.Locked = True
            cellBuilder.Padding = 2.0
            colCount+=1
        rowCount+=1
    
    tableBuilder1.DefaultRightBorder.StrokeColor = workPart.Colors.Find("Medium Blue")
    tableBuilder1.DefaultRightBorder.StrokeOpacity = 1.0
    tableBuilder1.DefaultRightBorder.LineFont = NXOpen.DisplayableObject.ObjectFont.Dashed
    tableBuilder1.DefaultRightBorder.LineWidth = NXOpen.DisplayableObject.ObjectWidth.Three

    tableBuilder1.DefaultBottomBorder.StrokeColor = workPart.Colors.Find("Medium Blue")
    tableBuilder1.DefaultBottomBorder.StrokeOpacity = 1.0
    tableBuilder1.DefaultBottomBorder.LineFont = NXOpen.DisplayableObject.ObjectFont.Dashed
    tableBuilder1.DefaultBottomBorder.LineWidth = NXOpen.DisplayableObject.ObjectWidth.Three

    ######################above is optional code to set table settings######################
 
    tableBuilder1.X = 132.5
    tableBuilder1.Y = 630.0

    table = tableBuilder1.Commit()
    tableBuilder1.Destroy()

    # ----------------------------------------------
    #   Descrition: Set a single cell style
    # ----------------------------------------------
    tableBuilder1 = workPart.DiagrammingManager.Tables.CreateTableBuilder(table)
    cellBuilder = tableBuilder1.GetCell(1, 1)
    cellBuilder.Locked = False
    cellBuilder.Padding = 2.0
    cellSettingsBuilder1 = cellBuilder.GetCellSettings()
    cellSettingsBuilder1.ContentAlignment = NXOpen.Diagramming.Tables.ContentAlignment.TopLeft
    cellSettingsBuilder1.OverflowBehavior = NXOpen.Diagramming.Tables.OverflowBehavior.Wrap

    textStyleBuilder1 = cellSettingsBuilder1.GetContentTextStyle()
    textStyleBuilder1.TextHeight = 5.1749999999999998
    textStyleBuilder1.TextAllowWrapping = True
    textStyleBuilder1.TruncationMode = NXOpen.Diagramming.TextStyleBuilder.TruncationModes.NotSet

    textColorFontWidthBuilder1 = textStyleBuilder1.TextColorFontWidth
    textColorFontWidthBuilder1.TextColor = workPart.Colors.Find("Blue")
    textColorFontWidthBuilder1.TextFont = "Calibri"
    textColorFontWidthBuilder1.TextStyle = "Bold"
    
    renderingPropertiesBuilder1 = cellBuilder.LeftBorder
    renderingPropertiesBuilder2 = cellBuilder.RightBorder
    renderingPropertiesBuilder3 = cellBuilder.TopBorder
    renderingPropertiesBuilder4 = cellBuilder.BottomBorder

    renderingPropertiesBuilder1.StrokeColor = workPart.Colors.Find("Medium Red")
    renderingPropertiesBuilder1.LineFont = NXOpen.DisplayableObject.ObjectFont.Phantom
    renderingPropertiesBuilder1.StrokeOpacity = 1.0
    renderingPropertiesBuilder1.LineWidth = NXOpen.DisplayableObject.ObjectWidth.Four

    renderingPropertiesBuilder2.StrokeColor = workPart.Colors.Find("Medium Red")
    renderingPropertiesBuilder2.StrokeOpacity = 1.0
    renderingPropertiesBuilder2.LineFont = NXOpen.DisplayableObject.ObjectFont.Phantom
    renderingPropertiesBuilder2.LineWidth = NXOpen.DisplayableObject.ObjectWidth.Four

    renderingPropertiesBuilder3.StrokeColor = workPart.Colors.Find("Medium Red")
    renderingPropertiesBuilder3.StrokeOpacity = 1.0
    renderingPropertiesBuilder3.LineFont = NXOpen.DisplayableObject.ObjectFont.Phantom
    renderingPropertiesBuilder3.LineWidth = NXOpen.DisplayableObject.ObjectWidth.Four

    renderingPropertiesBuilder4.StrokeColor = workPart.Colors.Find("Medium Red")
    renderingPropertiesBuilder4.StrokeOpacity = 1.0
    renderingPropertiesBuilder4.LineFont = NXOpen.DisplayableObject.ObjectFont.Phantom
    renderingPropertiesBuilder4.LineWidth = NXOpen.DisplayableObject.ObjectWidth.Four

    table = tableBuilder1.Commit()
    tableBuilder1.Destroy()

    # ----------------------------------------------
    #   Descrition: Insert a text to a single cell
    # ----------------------------------------------
    tableBuilder1 = workPart.DiagrammingManager.Tables.CreateTableBuilder(table)
    
    cellBuilder1 = tableBuilder1.GetCell(1, 0)
    cellBuilder1.Text = "my text"
    cellSettingsBuilder1 = cellBuilder1.GetCellSettings()
    
    textStyleBuilder1 = cellSettingsBuilder1.GetContentTextStyle()
    textStyleBuilder1.TextHeight = 4.0

    textColorFontWidthBuilder1 = textStyleBuilder1.TextColorFontWidth
    textColorFontWidthBuilder1.TextFont = "Calibri"
    textColorFontWidthBuilder1.TextColor = workPart.Colors.Find("Blue")

    table = tableBuilder1.Commit()
    tableBuilder1.Destroy()

    # ----------------------------------------------
    #   Descrition: Cell inherit
    # ----------------------------------------------
    tableBuilder1 = workPart.DiagrammingManager.Tables.CreateTableBuilder(table)
    cell1 = table.GetCell(1,1,False)
    cellBuilder = tableBuilder1.GetCell(4, 1)
    #choose 1 of 3 inherit options (Preferences,CustomerDefaults, Selection)
    #cellBuilder.Inherit(NXOpen.Diagramming.Tables.CellBuilder.InheritOption.Preferences, NXOpen.TaggedObject.Null)
    #cellBuilder.Inherit(NXOpen.Diagramming.Tables.CellBuilder.InheritOption.CustomerDefaults, NXOpen.TaggedObject.Null)
    cellBuilder.Inherit(NXOpen.Diagramming.Tables.CellBuilder.InheritOption.Selection, cell1)

    table = tableBuilder1.Commit()
    tableBuilder1.Destroy()

    # ----------------------------------------------
    #   Descrition: Define the table as a title block
    # ----------------------------------------------
    defineTitleBlockBuilder1 = workPart.DiagrammingManager.TitleBlocks.CreateDefineTitleBlockBuilder(NXOpen.Diagramming.TitleBlock.Null)
    
    tables1 = [NXOpen.Diagramming.Tables.Table.Null] * 1 
    tables1[0] = table
    defineTitleBlockBuilder1.SetTables(tables1)

    titleBlock = defineTitleBlockBuilder1.Commit()
    defineTitleBlockBuilder1.Destroy()


    #----------------------------------------------
    #   Descrition: Create a new objec table - equipment list
    #----------------------------------------------
    
    objectTableBuilder1 = workPart.SchematicManager.CreateObjectTableBuilder(NXOpen.Schematic.ObjectTable.Null)
    
    propertytypes1 = [None] * 4 
    propertytypes1[0] = NXOpen.Schematic.JaSchematicPropertytype.Index
    propertytypes1[1] = NXOpen.Schematic.JaSchematicPropertytype.Quantity
    propertytypes1[2] = NXOpen.Schematic.JaSchematicPropertytype.Id
    propertytypes1[3] = NXOpen.Schematic.JaSchematicPropertytype.Name
    propertykeys1 = [None] * 4 
    propertykeys1[0] = ""
    propertykeys1[1] = ""
    propertykeys1[2] = ""
    propertykeys1[3] = ""
    objectTableBuilder1.InsertPropertyColumns(0, propertytypes1, propertykeys1)
    
    tableBuilder1 = objectTableBuilder1.Table
    tableBuilder1.InsertHeaders(0, 2)
    tableBuilder1.MergeHeaderCells(0, 0, 0, 3)
    
    cellBuilder1 = tableBuilder1.GetHeaderCell(0, 0)
    cellBuilder1.Text = "Equipment List"
    
    cellBuilder2 = tableBuilder1.GetHeaderCell(1, 0)
    cellBuilder2.Text = "Index"
    columnBuilder1 = tableBuilder1.GetColumn(0)
    columnBuilder1.SetWidth(20.0)
    
    cellBuilder3 = tableBuilder1.GetHeaderCell(1, 1)
    cellBuilder3.Text = "Qty"
    columnBuilder2 = tableBuilder1.GetColumn(1)
    columnBuilder2.SetWidth(20.0)
    
    cellBuilder4 = tableBuilder1.GetHeaderCell(1, 2)
    cellBuilder4.Text = "ID"
    columnBuilder3 = tableBuilder1.GetColumn(2)
    columnBuilder3.SetWidth(40.0)
    
    cellBuilder5 = tableBuilder1.GetHeaderCell(1, 3)
    cellBuilder5.Text = "Name" 
    columnBuilder4 = tableBuilder1.GetColumn(3) 
    columnBuilder4.SetWidth(80.0)

    tableBuilder1.X = 370.0
    tableBuilder1.Y = 630.0

    objectTableBuilder1.AddObjectType("ObjectTableNode")
    objectTableBuilder1.AddObjectType("ObjectTableInlineNode")
    
    objectTable = objectTableBuilder1.Commit()
    table1 = objectTable.Table
    objectTableBuilder1.Destroy()
    
    # ----------------------------------------------
    #   Descrition: Associate a new column attribute to the object table
    # ----------------------------------------------
    tableBuilder1 = workPart.DiagrammingManager.Tables.CreateTableBuilder(table1)
    tableBuilder1.InsertColumns(4, 1)
    
    columnBuilder1 = tableBuilder1.GetColumn(4)
    columnBuilder1.Size = 80.0
    columnBuilder1.SizingMethod = NXOpen.Diagramming.Tables.SizingMethod.Fixed
    
    table1 = tableBuilder1.Commit()
    tableBuilder1.Destroy()

    objectTableBuilder1 = workPart.SchematicManager.CreateObjectTableBuilder(objectTable)
    propertyCellRangeBuilder2 = objectTableBuilder1.GetPropertyColumn(4)
    propertyCellRangeBuilder2.PropertyType = NXOpen.Schematic.JaSchematicPropertytype.Symbol
    propertyCellRangeBuilder2.PropertyKey = ""

    objectTable = objectTableBuilder1.Commit()
    table1 = objectTable.Table
    objectTableBuilder1.Destroy()

    # ----------------------------------------------
    #   Descrition: Save the whole sheet
    # ----------------------------------------------
    
    smartSaveContext1 = theSession.PdmSession.CreateSmartSaveContext(NXOpen.PDM.SmartSaveBuilder.SaveType.Save)
    
    smartSaveBuilder1 = theSession.PdmSession.CreateSmartSaveBuilderWithContext(smartSaveContext1)
    
    smartsaveobjects1 = smartSaveBuilder1.GetSmartSaveObjects()
 
    errorList3 = smartSaveBuilder1.AutoAssignAttributes(smartsaveobjects1)
    
    smartSaveBuilder1.ValidateSmartSaveObjects()
    
    nXObject56 = smartSaveBuilder1.Commit()
    
    smartSaveBuilder1.Destroy()
    
    smartSaveContext1.Dispose()
    
if __name__ == '__main__':
    main()

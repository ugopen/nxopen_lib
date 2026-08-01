'/*=================================================================================================
'                                       Copyright 2021 Siemens
'===================================================================================================
'
'    NOTE:  NX Development provides programming examples for illustration only.
'    NX Development assumes you are familiar with the programming language
'    demonstrated in these examples, and the tools used to create and debug NX/Open
'    programs. GTAC support professionals can help explain the functionality of
'    a particular procedure, but neither GTAC nor NX Development will modify
'    these examples to provide added functionality or construction procedures.
'
'File description:
'
'    A Visual Basic class that implements example Routing Cableway Design Rules.
'
'
'===================================================================================================
Option Strict On

Imports System
Imports NXOpen
Imports NXOpen.Assemblies
Imports NXOpen.Routing
Imports NXOpen.Routing.CustomManager
Imports NXOpen.RoutingCommon

Module DesignRules

    Dim theSession As Session = Nothing
    Dim customManager As NXOpen.RoutingCommon.CustomManager = Nothing
    Dim segregationCodeRuleId As Integer = 0
    Dim tierCountAttributeName As String = "TierCount"
    Dim hangerSegregationAttributeName As String = "Cableway Hanger Segregation Code"
    Dim segmentSegregationAttributeName As String = "Cableway Segment Segregation"

    '-----------------------------------------------------------------------------------------------
    ' Called when NX starts up to register the Design Rules.
    Function Startup(ByVal args As String()) As Integer

        If theSession Is Nothing Then
            theSession = Session.GetSession()
        End If

        If customManager Is Nothing Then
            customManager = theSession.RoutingCustomManager()
        End If

        RegisterDesignRules()

        Startup = 0
    End Function

    '------------------------------------------------------------------------------------------
    ' Called from File->Execute->NX Open. Useful for testing.
    Sub Main()

        If theSession Is Nothing Then
            theSession = Session.GetSession()
        End If

        If customManager Is Nothing Then
            customManager = theSession.RoutingCustomManager()
        End If

        RegisterDesignRules()
    End Sub

    '------------------------------------------------------------------------------------------
    ' Called by both Main And Startup to register the Design Rules.
    Sub RegisterDesignRules()

        Dim name As String = "Segregation Code"
        Dim description As String = "The Segregation Code design rule ensures no multi-tier " +
                                    "component has more segregation codes than tiers."

        segregationCodeRuleId = customManager.AddDesignRule(NXOpen.Routing.CustomManager.DesignRuleReason.CablewayValidation,
                                                            name, description, AddressOf SegregationCodeDesignRule)

    End Sub
    '-----------------------------------------------------------------------------------------------
    Private Function GetAttributeValueFromObject(ByVal nxObject As NXObject,
                                                 ByVal attributeName As String) As String

        Dim attributeInformation As NXObject.AttributeInformation = Nothing

        If GetAttributeFromObject(nxObject, attributeName, attributeInformation) Then
            Return attributeInformation.StringValue
        End If

        Return Nothing

    End Function

    '-----------------------------------------------------------------------------------------------
    Private Function GetAttributeFromObject(ByVal nxObject As NXObject,
                                            ByVal attributeName As String,
                                            ByRef attributeInformation As NXObject.AttributeInformation) As Boolean

        If (GetAttributeFromList(nxObject.GetUserAttributes(), attributeName, attributeInformation)) Then
            Return True
        End If

        Return False

    End Function

    '-----------------------------------------------------------------------------------------------
    Private Function GetAttributeFromList(ByVal attributes() As NXObject.AttributeInformation,
                                          ByVal attributeName As String,
                                          ByRef attributeInformation As NXObject.AttributeInformation) As Boolean

        For Each attribute As NXObject.AttributeInformation In attributes

            Dim ucAttributeName As String = attributeName.ToUpper

            Dim titleString As String = attribute.Title

            ' Watch out for attributes with no title.
            If titleString.Length() = 0 Then
                Continue For
            End If

            titleString = titleString.ToUpper()

            ' NOTE: This does not look for aliases on the attribute titles.
            If titleString = ucAttributeName Then
                attributeInformation = attribute
                Return True
            End If
        Next

        Return False

    End Function

    '-----------------------------------------------------------------------------------------------
    ' Returns the stock body (e.g. the cable tray body) if the given component Is a stock component.
    ' Returns the given component if the component Is Not a stock component.
    Function getStockBodyInComponent(ByVal component As Component) As NXObject

        Dim componentPart As Part = CType(component.Prototype, Part)

        If componentPart Is Nothing Or Not componentPart.IsFullyLoaded Then
            Return component
        End If

        Dim stockCollection As StockCollection = componentPart.RouteManager.Stocks

        ' Since all stock components have the same type of stock, we can return the first stock body.
        For Each stock As Stock In stockCollection
            Dim stockBodies() As Body = stock.GetBodies
            If stockBodies.Length > 0 Then
                Return stockBodies(0)
            End If
        Next

        ' If there are no stock, return the given component.
        Return component

    End Function

    '-----------------------------------------------------------------------------------------------
    ' Returns the number of elements in the segregation attribute array if it exists. Returns zero if Not.
    Function getTierCount(ByVal component As Component) As Integer

        Dim nxobject As NXObject = getStockBodyInComponent(component)

        Dim attributeInformation As NXObject.AttributeInformation = Nothing
        If Not GetAttributeFromObject(nxobject, tierCountAttributeName, attributeInformation) Then

        End If

        If attributeInformation.Type = nxobject.AttributeType.Integer Then
            Return attributeInformation.IntegerValue
        End If

        If attributeInformation.Type = nxobject.AttributeType.Real Then
            Return CInt(attributeInformation.RealValue)
        End If

        Return 0
    End Function
    '-----------------------------------------------------------------------------------------------
    ' Returns the number of elements in the segregation attribute array if it exists. Returns zero if Not.
    Function getSegregationCount(ByVal component As Component) As Integer

        Dim nxobject As NXObject = getStockBodyInComponent(component)


        If nxobject.HasUserAttribute(hangerSegregationAttributeName, nxobject.AttributeType.Any, -1) Then
            Return nxobject.GetUserAttributeSize(hangerSegregationAttributeName, nxobject.AttributeType.Any)
        End If

        Return nxobject.GetUserAttributeSize(segmentSegregationAttributeName, nxobject.AttributeType.Any)
    End Function

    '-----------------------------------------------------------------------------------------------
    ' Ensures the tier count Is greater than Or equal too the number of elements in the segregation
    ' attribute array. 
    ' 
    ' In other words, ensures there are Not more segregation codes than there are tiers.
    Sub checkComponentTierCount(ByVal listingWindow As ListingWindow, ByVal indentation As Integer, ByVal component As Component)

        Dim tierCount As Integer = getTierCount(component)
        Dim nSegregationCodes As Integer = getSegregationCount(component)
        If tierCount >= nSegregationCodes Then
            Return
        End If

        indentation += 2
        Dim debugMessage As String = "".PadLeft(indentation) + "TierCount = " + tierCount.ToString() + vbCrLf
        debugMessage += "".PadLeft(indentation) + "Number of Segregation Codes = " + nSegregationCodes.ToString() + vbCrLf
        listingWindow.WriteFullline(debugMessage)

        Dim objects() As NXObject = New NXObject() {CType(component, NXObject)}

        Dim message As String = "Component " + component.DisplayName
        message += " has only " + tierCount.ToString() + " tiers"
        message += " but has " + nSegregationCodes.ToString() + " segregation codes." + vbCrLf
        message += "The number of segregation codes cannot exceed the number of tiers."

        customManager.CreateViolationForReason("Segregation Code", NXOpen.Routing.CustomManager.DesignRuleReason.CablewayValidation,
                                               "Too many segregation codes.", message, objects)

    End Sub

    '-----------------------------------------------------------------------------------------------
    ' Recursively walks down the assembly tree under the given component.
    Sub walkDownAssemblyTree(ByVal listingWindow As ListingWindow, ByVal indentation As Integer, ByVal component As Component)

        If component Is Nothing Then
            Return
        End If

        Dim message As String = "".PadLeft(indentation) + component.DisplayName
        listingWindow.WriteFullline(message)

        ' Verify that the segregation attribute array does Not have more values than there are tiers.
        ' This also works for stock components.
        checkComponentTierCount(listingWindow, indentation, component)

        indentation += 2
        Dim children() As Component = component.GetChildren()
        For Each child As Component In children
            walkDownAssemblyTree(listingWindow, indentation, child)
        Next

    End Sub

    '-----------------------------------------------------------------------------------------------
    Sub SegregationCodeDesignRule(reason As DesignRuleReason, nxObjects() As NXObject)

        If reason <> NXOpen.Routing.CustomManager.DesignRuleReason.CablewayValidation And
           reason <> NXOpen.Routing.CustomManager.DesignRuleReason.Interactive Then
            Return
        End If

        Dim rootComponent As Component = theSession.Parts.Work.ComponentAssembly.RootComponent

        Dim listingWindow As ListingWindow = theSession.ListingWindow
        listingWindow.Open()

        Dim indentation As Integer = 0
        walkDownAssemblyTree(listingWindow, indentation, rootComponent)

    End Sub

    '-----------------------------------------------------------------------------------------------
    ' Tells NX when to unload your application.
    ' For Routing callbacks, plugins, And Design Rules, this MUST return AtTermination.
    Public Function GetUnloadOption(ByVal dummy As String) As Integer
        GetUnloadOption = NXOpen.Session.LibraryUnloadOption.AtTermination
    End Function

End Module

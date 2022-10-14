'===================================================================================================
'               Copyright 2017 Siemens Product Lifecycle Management Software Inc.
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
'    This file Implements a Routing Plugin that Implements Tyco's Entry Size new bundling algorithm
'    For routing wires in Routing Electrical.  The algorithm Is taken from a PDF titled
'    AdapterEntrySizeSelection.pdf on the Tyco Electronics' Raychem web site.
'
'    ALGORITHM:
'
'    For 61 Or fewer wires of all the same size, use the Tyco table data To look up a bundle factor (F).
'    The bundle diameter Is computed As D = F * d, where d Is the wire diameter.
'
'    Otherwise use the formula,
'
'        D = 1.2 * SQRT(SUM(d[i] * d[i] )
'
'    where d[i] Is the diameter For Each wire In the bundle.
'
'
'===================================================================================================
Option Strict On
Imports System
Imports NXOpen
Imports NXOpen.Routing
Imports NXOpen.Routing.CustomManager

Module Tyco

    Dim customManager As CustomManager = Nothing

    '-----------------------------------------------------------------------------------------------
    ' Called when NX starts up to register the plugins.
    Function Startup(ByVal args As String()) As Integer

        If customManager Is Nothing Then
            customManager = Session.GetSession().RouteCustomManager()
        End If

        customManager.SetBundlePlugin(AddressOf BundlePlugin)

        Startup = 0
    End Function

    '------------------------------------------------------------------------------------------
    ' Called from File->Execute->NX Open. Useful for testing.
    Sub Main()

        If customManager Is Nothing Then
            customManager = Session.GetSession().RouteCustomManager()
        End If

        customManager.SetBundlePlugin(AddressOf BundlePlugin)

    End Sub

    '-----------------------------------------------------------------------------------------------
    Function BundlePlugin(ByVal stockDatas As StockData()) As Double

        Dim tolerance As Double = 0.000001

        ' This table Is used if all the wires are the same diameter.
        Dim bundleFactorTable As Double() = New Double() _
        {
            0.00, 1.00, 1.64, 2.00, 2.41,
            2.70, 3.00, 3.00, 3.60, 4.00,
            4.00, 4.00, 4.00, 4.41, 4.41,
            4.70, 4.70, 5.00, 5.00, 5.00,
            5.31, 5.31, 5.61, 5.61, 5.61,
            6.00, 6.00, 6.00, 6.41, 6.41,
            6.41, 6.70, 6.70, 6.70, 7.00,
            7.00, 7.00, 7.00, 7.31, 7.31,
            7.31, 7.61, 7.61, 7.61, 7.61,
            8.00, 8.00, 8.00, 8.00, 8.41,
            8.41, 8.41, 8.41, 8.70, 8.70,
            8.70, 8.70, 9.00, 9.00, 9.00,
            9.00, 9.00
        }

        Dim sizeOfBundleFactorTable As Integer = bundleFactorTable.Length

        Dim sumOfDiameters As Double = 0.0
        Dim sumOfSquares As Double = 0.0
        Dim commonDiameter As Double = -1.0
        Dim equalDiameters As Boolean = True

        For Each stockData As StockData In stockDatas

            Dim wireCrossSections As CrossSection() = stockData.GetCrossSections()
            For Each wireCrossSection As CrossSection In wireCrossSections

                Dim wireCrossSectionCurves As Curve() = wireCrossSection.GetCrossCurves()
                If wireCrossSectionCurves.Length = 0 Then
                    Continue For
                End If

                If Not TypeOf wireCrossSectionCurves(0) Is Arc Then
                    Continue For
                End If

                ' Assume all the cross sections of this stock have the same diameter.
                Dim crossSectionArc As Arc = CType(wireCrossSectionCurves(0), Arc)

                Dim arcDiameter As Double = crossSectionArc.Radius * 2.0

                sumOfDiameters += arcDiameter
                sumOfSquares += arcDiameter * arcDiameter

                If commonDiameter < 0.0 Then

                    commonDiameter = arcDiameter

                ElseIf (equalDiameters And Math.Abs(commonDiameter - arcDiameter) > tolerance)

                    equalDiameters = False

                End If

            Next

        Next

        Dim diameter As Double = 0.0
        If equalDiameters And stockDatas.Length < sizeOfBundleFactorTable Then

            ' If all the wires are the same size, use the Tyco table.
            diameter = bundleFactorTable(stockDatas.Length) * commonDiameter

        Else

            ' Otherwise use the the formula.
            diameter = 1.2 * Math.Sqrt(sumOfSquares)

        End If

        Return diameter

    End Function

    '-----------------------------------------------------------------------------------------------
    ' Tells NX when to unload your application.
    ' For Routing callbacks, plugins, And Design Rules, this MUST return AtTermination.
    Public Function GetUnloadOption(ByVal dummy As String) As Integer
        GetUnloadOption = NXOpen.Session.LibraryUnloadOption.AtTermination
    End Function

End Module

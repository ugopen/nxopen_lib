'/*==================================================================================================
'
'                 Copyright 2012 Siemens Product Lifecycle Management Software Inc.
'
'                                      All Rights Reserved.
'
'====================================================================================================
'File description:
'
'   NX/Open example to show how to create and execute journal to execute Checker and get its results
'   by using NX Open VB.NET.
'
'====================================================================================================
'
'*/


Option Strict Off
Imports System
Imports NXOpen

Module NXJournal
    Sub Main(ByVal args() As String)

        'Get the NX session, work part, display part.
        Dim theSession As Session = Session.GetSession()
        Dim workPart As Part = theSession.Parts.Work
        Dim displayPart As Part = theSession.Parts.Display

        'Get the NX Check-Mate Validator object.
        Dim validators1() As Validate.Validator
        theSession.ValidationManager.FindValidator("Check-Mate", validators1)

        'Get the NX Check-Mate ValidatorOptions, and set options.
        Dim validatorOptions1 As Validate.ValidatorOptions
        validatorOptions1 = validators1(0).ValidatorOptions

        validatorOptions1.SkipChecking = False
        validatorOptions1.SkipCheckingDontLoadPart = False
        validatorOptions1.SaveResultInTeamcenter = Validate.ValidatorOptions.SaveModeTypes.DoNotSave
        validatorOptions1.SavePartFile = Validate.ValidatorOptions.SaveModeTypes.DoNotSave
        validatorOptions1.SaveResultInPart = False

        'Clear part nodes if any.
        validators1(0).ClearPartNodes()

        'Appends the full path of a part file or the current work part.
        validators1(0).AppendPartNode(workPart)

        'Manually add this line to clean all existing tests
        validators1(0).ClearCheckerNodes()

        'Select a checker and append it into the Validator object.
        Dim classnames1(0) As String
        classnames1(0) = "%mqc_report_browseable_features"
        validators1(0).AppendCheckerNodes(classnames1)

        'Execute the Check-Mate checker.
        Dim status1 As Validation.Result
        status1 = validators1(0).Commit()

        'Get a Parser object, and show the checker result.
        Dim parsers1() As Validate.Parser
        theSession.ValidationManager.FindParser("Validation Gadget", parsers1)

        parsers1(0).ClearResultObjects()
        parsers1(0).DataSource = Validate.Parser.DataSourceTypes.MostRecentRun
        parsers1(0).MaxDisplayObjects = 10
        parsers1(0).Commit()
    End Sub
End Module

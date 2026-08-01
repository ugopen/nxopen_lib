#===================================================================================
#
#       Copyright 2014 Siemens Product Lifecycle Management Software Inc.
#                            All Rights Reserved.
#
#===================================================================================
#File description:
#
#   NX/Open example to show how to create and execute journal to execute 
#   Checker and get its results by using NX Open Python.
#
#===================================================================================
#
#*/

import NXOpen
import NXOpen.Validate

def main():

    # Get the NX session, work part, display part.
    theSession = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display

    # Get the NX Check-Mate Validator object.
    validators1 = theSession.ValidationManager.FindValidator("Check-Mate")

    # Get the NX Check-Mate ValidatorOptions, and set options.
    validatorOptions1 = validators1[0].ValidatorOptions

    validatorOptions1.SkipChecking = False
    validatorOptions1.SkipCheckingDontLoadPart = False
    validatorOptions1.SaveResultInTeamcenter = NXOpen.Validate.ValidatorOptions.SaveModeTypes.DoNotSave
    validatorOptions1.SavePartFile = NXOpen.Validate.ValidatorOptions.SaveModeTypes.DoNotSave
    validatorOptions1.SaveResultInPart = False

    # Clear part nodes if any.
    validators1[0].ClearPartNodes()

    # Appends the full path of a part file or the current work part.
    validators1[0].AppendPartNode(workPart)

    # Manually add this line to clean all existing tests
    validators1[0].ClearCheckerNodes()

    # Select a checker and append it into the Validator object.
    classnames1 = [None]
    classnames1[0] = "%mqc_report_browseable_features"
    validators1[0].AppendCheckerNodes(classnames1)

    # Execute the Check-Mate checker.
    status1 = validators1[0].Commit()

    # Get a Parser object, and show the checker result.
    parsers1 = []
    parsers1 = theSession.ValidationManager.FindParser("Validation Gadget")

    parsers1[0].ClearResultObjects()
    parsers1[0].DataSource = NXOpen.Validate.Parser.DataSourceTypes.MostRecentRun
    parsers1[0].MaxDisplayObjects = 10
    parsers1[0].Commit()

if __name__ == "__main__":
    main()

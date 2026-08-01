/*==================================================================================================

                 Copyright 2012 Siemens Product Lifecycle Management Software Inc.

                                      All Rights Reserved.

====================================================================================================
File description:

    NX/Open example to show how to create and execute journal to execute Checker and get its results
    by using NX Open C#.
====================================================================================================

*/

using System;
using NXOpen;

public class NXJournal
{
  public static void Main(string[] args)
  {
    // Get the NX session, work part, display part.
    Session theSession = Session.GetSession();
    Part workPart = theSession.Parts.Work;
    Part displayPart = theSession.Parts.Display;

    // Get the NX Check-Mate Validator object.
    NXOpen.Validate.Validator[] validators1;
    theSession.ValidationManager.FindValidator("Check-Mate", out validators1);

    // Get the NX Check-Mate ValidatorOptions, and set options.
    NXOpen.Validate.ValidatorOptions validatorOptions1;
    validatorOptions1 = validators1[0].ValidatorOptions;

    validatorOptions1.SkipChecking = false;
    validatorOptions1.SkipCheckingDontLoadPart = false;
    validatorOptions1.SaveResultInTeamcenter = NXOpen.Validate.ValidatorOptions.SaveModeTypes.DoNotSave;
    validatorOptions1.SavePartFile = NXOpen.Validate.ValidatorOptions.SaveModeTypes.DoNotSave;
    validatorOptions1.SaveResultInPart = false;

    // Clear part nodes if any.
    validators1[0].ClearPartNodes();

    // Appends the full path of a part file or the current work part.
    validators1[0].AppendPartNode(workPart);

    // Manually add this line to clean all existing tests
    validators1[0].ClearCheckerNodes();

    // Select a checker and append it into the Validator object.
    string[] classnames1 = new string[1];
    classnames1[0] = "%mqc_report_browseable_features";
    validators1[0].AppendCheckerNodes(classnames1);

    // Execute the Check-Mate checker.
    NXOpen.Validation.Result status1;
    status1 = validators1[0].Commit();

    // Get a Parser object, and show the checker result.
    NXOpen.Validate.Parser[] parsers1;
    theSession.ValidationManager.FindParser("Validation Gadget", out parsers1);
    
    parsers1[0].ClearResultObjects();
    parsers1[0].DataSource = NXOpen.Validate.Parser.DataSourceTypes.MostRecentRun;
    parsers1[0].MaxDisplayObjects = 10;
    parsers1[0].Commit();
  }
  public static int GetUnloadOption(string dummy) { return (int)Session.LibraryUnloadOption.Immediately; }
}

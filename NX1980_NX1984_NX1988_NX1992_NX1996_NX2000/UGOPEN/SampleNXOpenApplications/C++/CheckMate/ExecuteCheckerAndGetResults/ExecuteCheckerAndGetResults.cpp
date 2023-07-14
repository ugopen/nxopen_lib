/*==================================================================================================

                 Copyright 2012 Siemens Product Lifecycle Management Software Inc.

                                      All Rights Reserved.

====================================================================================================
File description:
    NX/Open example to show how to create and execute journal to execute Checker and get its results
    by using NX Open C++.
====================================================================================================

*/

#include <uf_defs.h>
#include <NXOpen/NXException.hxx>
#include <NXOpen/Session.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Session.hxx>
#include <NXOpen/Validate_Parser.hxx>
#include <NXOpen/Validate_ValidationManager.hxx>
#include <NXOpen/Validate_Validator.hxx>
#include <NXOpen/Validate_ValidatorOptions.hxx>
using namespace NXOpen;

extern "C" DllExport int ufusr_ask_unload()
{
    return (int)Session::LibraryUnloadOptionImmediately;
}

extern "C" DllExport void ufusr(char *param, int *retCode, int paramLen)
{
    // Get the NX session, work part, display part.
    Session *theSession = Session::GetSession();
    Part *workPart(theSession->Parts()->Work());
    Part *displayPart(theSession->Parts()->Display());

    // Get the NX Check-Mate Validator object.
    std::vector<Validate::Validator *> validators1;
    theSession->ValidationManager()->FindValidator("Check-Mate", validators1);

    // Get the NX Check-Mate ValidatorOptions, and set options.
    Validate::ValidatorOptions *validatorOptions1;
    validatorOptions1 = validators1[0]->ValidatorOptions();

    validatorOptions1->SetSkipChecking(false);
    validatorOptions1->SetSkipCheckingDontLoadPart(false);
    validatorOptions1->SetSaveResultInTeamcenter(Validate::ValidatorOptions::SaveModeTypesDoNotSave);
    validatorOptions1->SetSavePartFile(Validate::ValidatorOptions::SaveModeTypesDoNotSave);
    validatorOptions1->SetSaveResultInPart(false);

    // Clear part nodes if any.
    validators1[0]->ClearPartNodes();

    // Appends the full path of a part file or the current work part.
    validators1[0]->AppendPartNode(workPart);

    // Manually add this line to clean all existing tests
    validators1[0]->ClearCheckerNodes();

    // Select a checker and append it into the Validator object.
    std::vector<NXString> classnames1(1);
    classnames1[0] = "%mqc_report_browseable_features";
    validators1[0]->AppendCheckerNodes(classnames1);

    // Execute the Check-Mate checker.
    Validation::Result status1;
    status1 = validators1[0]->Commit();

    // Get a Parser object, and show the checker result.
    std::vector<Validate::Parser *> parsers1;
    theSession->ValidationManager()->FindParser("Validation Gadget", parsers1);
    parsers1[0]->ClearResultObjects();
    parsers1[0]->SetDataSource(Validate::Parser::DataSourceTypesMostRecentRun);
    parsers1[0]->SetMaxDisplayObjects(10);
    parsers1[0]->Commit();
}

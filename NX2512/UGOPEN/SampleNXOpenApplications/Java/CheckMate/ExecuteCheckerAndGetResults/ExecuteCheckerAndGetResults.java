/*==================================================================================================

                 Copyright 2012 Siemens Product Lifecycle Management Software Inc.

                                      All Rights Reserved.

====================================================================================================
File description:

    NX/Open example to show how to create and execute journal to execute Checker and get its results
    by using NX Open Java.
====================================================================================================

*/


import nxopen.*;

public class ExecuteCheckerAndGetResults
{
  public static void main(String [] args) throws NXException, java.rmi.RemoteException
  {
    Session theSession = (Session)SessionFactory.get("Session");
    Part workPart = theSession.parts().work();
    Part displayPart = theSession.parts().display();

    nxopen.validate.Validator [] validators1 ;
    validators1 = theSession.validationManager().findValidator("Check-Mate");

    nxopen.validate.ValidatorOptions validatorOptions1;
    validatorOptions1 = validators1[0].validatorOptions();

    validatorOptions1.setSkipChecking(false);
    validatorOptions1.setSkipCheckingDontLoadPart(false);
    validatorOptions1.setSaveResultInTeamcenter(nxopen.validate.ValidatorOptions.SaveModeTypes.DO_NOT_SAVE);
    validatorOptions1.setSavePartFile(nxopen.validate.ValidatorOptions.SaveModeTypes.DO_NOT_SAVE);
    validatorOptions1.setSaveResultInPart(false);

    validators1[0].clearPartNodes();

    // Appends the full path of a part file or the current work part.
    validators1[0].appendPartNode(workPart);

    // Manually add this line to clean all existing tests
    validators1[0].clearCheckerNodes();

    String [] classnames1  = new String[1];
    classnames1[0] = "%mqc_report_browseable_features";
    validators1[0].appendCheckerNodes(classnames1);

    nxopen.Validation.Result status1;
    status1 = validators1[0].commit();

    nxopen.validate.Parser [] parsers1 ;
    parsers1 = theSession.validationManager().findParser("Validation Gadget");
    parsers1[0].clearResultObjects();
    parsers1[0].setDataSource(nxopen.validate.Parser.DataSourceTypes.MOST_RECENT_RUN);
    parsers1[0].setMaxDisplayObjects(10);
    parsers1[0].commit();
  }

  public static final int getUnloadOption() { return BaseSession.LibraryUnloadOption.IMMEDIATELY; }

}

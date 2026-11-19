/*=============================================================================
  Copyright 2012 Siemens Product Lifecycle Management Software Inc.
  All Rights Reserved.
===============================================================================
File description: Example of creating a connection with a Teamcenter Server and
then getting some information by making server calls.


=============================================================================*/

// Open C Headers
#include <uf_ugmgr.h>

// NX Open C++ header files
#include <NXOpen/LogFile.hxx>
#include <NXOpen/NXString.hxx>
#include <NXOpen/PDM_PdmSession.hxx>
#include <NXOpen/Session.hxx>

// Local headers
#include "SOAConnectionExample_AppSession.hpp"
#include "SOAConnectionExample_HomeFolder.hpp"
#include "SOAConnectionExample_Query.hpp"

using namespace std;

// Main routine
int main(int argc, char *argv[])
{
    if (argc == 0)
    {
        cout << "No arguments passed" << endl;
        return 0;
    }

    // Start a UGMGR session using Open C API
    int status = 0;
    status = UF_UGMGR_initialize(argc, (const char **)argv);
    if (status != 0)
    {
        cout << "Failed to iniliatize UGMGR session" << endl;
        return 0;
    }
    cout << endl << "UGMGR session started " << endl;

    // Get the Connect String and Discriminator
    NXOpen::Session *theSession = NXOpen::Session::GetSession();
    NXOpen::PDM::PdmSession *thePdmSession = theSession->PdmSession();

    NXOpen::NXString connectString;     // e.g. "http://virtualtc:8080/tc"
    NXOpen::NXString discriminator;     // e.g. "GUID-2928e9d8-2c81-4f6c-a1ec7a7279a3463c"
    thePdmSession->GetTcserverSettings(&connectString, &discriminator);

    cout << endl;
    cout << "Tcserver connect string : " << connectString.GetText() << endl;
    cout << "Tcserver discriminator  : " << discriminator.GetText() << endl;

    // For a new SOA client session, prompt for the username and password
    string username, password;
    cout << endl << "To create a new SOA session, please enter user credentials:" << endl;
    cout << "User Name : ";
    cin >> username;
    cout << "Password  : ";
    cin >> password;

    AppCredentialManager* credentialManager = new AppCredentialManager();
    credentialManager->setUserPassword(username, password, discriminator.GetText());

    // Establish a SOA client session using the connectString
    AppSession session(connectString.GetText(), credentialManager);
    cout << endl << "Created new SOA session" << endl;

    // Note: Below the user will be prompted to enter username and password to login to the new SOA session.
    // However, if you are using Single Sign On, please call AppSession::ssoLogin() method instead to avoid
    // the additional login challenge.

    // Log in
    cout << endl << "Logging in ... " << endl;
    Teamcenter::Soa::Client::Model::User* user = session.login(discriminator.GetText(), credentialManager);
    if (user == NULL)
    {
        cout << "Login failure" << endl;
        return 0;
    }
    cout << endl << "Log in successful" << endl;

    // List the contents of the user's Home folder
    HomeFolder homeFolder;
    homeFolder.listHomeFolder(user, session);

    // Perform a simple query of the database
    Query query;
    query.queryItems(session);

    // Logout of the SOA client session
    session.logout();
    cout << endl << "Logged Out" << endl;

    // Terminate the UGMGR session using Open C API
    UF_UGMGR_terminate();
    cout << endl << "UGMGR session terminated" << endl;

    return 0;
}

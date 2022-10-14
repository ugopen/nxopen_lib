/*=============================================================================
  Copyright 2014 Siemens Product Lifecycle Management Software Inc.
  All Rights Reserved.
===============================================================================
File description: Example of obtaining a pointer to the Teamcnter SOA connection
object that NX is using when running in Teamcenter Integration mode.


=============================================================================*/

// Open C Headers
#include <uf_ugmgr.h>

#include <iostream>

// NX Open C++ header files
#include <NXOpen/PDM_PdmSession.hxx>
#include <NXOpen/Session.hxx>

#include <teamcenter/soa/client/Connection.hxx>

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

    NXOpen::Session *theSession = NXOpen::Session::GetSession();
    NXOpen::PDM::PdmSession *thePdmSession = theSession->PdmSession();

    // Get hold of the SoaConnectionHandle* pointer by calling NXOpen API
    NXOpen::PDM::SoaConnectionHandle *connectionHandle = NULL;
    connectionHandle = thePdmSession->GetSoaConnectionHandle();

    // Now obtain the handle of the SoaConnectionHandle and reinterpret_cast
    // to obtain the Teamcnter SOA Connection pointer
    Teamcenter::Soa::Client::Connection* tcSoaConnection = reinterpret_cast<Teamcenter::Soa::Client::Connection*>(connectionHandle->GetHandle());

    // Print information about the Connection
    cout << endl << "Details of the Connection --------" << endl;

    Teamcenter::Soa::Common::Version clientVersion = tcSoaConnection->getClientVersion();
    cout << "  Client Version       : " << clientVersion.getTeamcenterVersion() << endl;
    cout << "  Client Version Label : " << clientVersion.getTeamcenterVersionLabel() << endl;

    Teamcenter::Soa::Common::Version serverVersion = tcSoaConnection->getServerVersion();
    cout << "  Server Version       : " << clientVersion.getTeamcenterVersion() << endl;
    cout << "  Server Version Label : " << clientVersion.getTeamcenterVersionLabel() << endl;

    cout << "  Locale               : " << tcSoaConnection->getLocale() << endl;
    cout << "  Server Address       : " << tcSoaConnection->getServerAddress() << endl;
    cout << "  Property Policy      : " << tcSoaConnection->getCurrentObjectPropertyPolicy() << endl;

    cout << "  Protocol             : ";
    Teamcenter::Soa::Client::Connection::Protocol protocol = tcSoaConnection->getProtocol();
    switch (protocol)
    {
        case Teamcenter::Soa::Client::Connection::HTTP:
            cout << "HTTP" << endl;
            break;
        case Teamcenter::Soa::Client::Connection::IIOP:
            cout << "IIOP" << endl;
            break;
        case Teamcenter::Soa::Client::Connection::TCCS:
            cout << "TCCS" << endl;
            break;
        default:
            cout << "<Unknown>" << endl;
    }

    cout << "  Binding              : ";
    Teamcenter::Soa::Client::Connection::Binding binding = tcSoaConnection->getBinding();
    switch (binding)
    {
        case Teamcenter::Soa::Client::Connection::REST:
            cout << "REST" << endl;
            break;
        case Teamcenter::Soa::Client::Connection::SOAP:
            cout << "SOAP" << endl;
            break;
        default:
            cout << "<Unknown>" << endl;
    }

    cout << "----------------------------------" << endl;

    // Terminate the UGMGR session using Open C API
    UF_UGMGR_terminate();
    cout << endl << "UGMGR session terminated" << endl;

    return 0;
}

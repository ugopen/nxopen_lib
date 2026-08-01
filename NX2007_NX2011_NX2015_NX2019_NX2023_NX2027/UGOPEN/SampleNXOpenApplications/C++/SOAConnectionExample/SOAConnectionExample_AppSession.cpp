/*=============================================================================
  Copyright 2012 Siemens Product Lifecycle Management Software Inc.
  All Rights Reserved.
===============================================================================
File description: Implementation of AppSession class.


=============================================================================*/

#include <iomanip> 

#include "SOAConnectionExample_AppSession.hpp"

#include <teamcenter/soa/client/NotLoadedException.hxx>
#include <teamcenter/soa/client/ModelObject.hxx>
#include <teamcenter/soa/client/Property.hxx>

#include <teamcenter/soa/common/DateTime.hxx>

#include <teamcenter/services/core/_2006_03/Session.hxx>
#include <teamcenter/services/core/DatamanagementService.hxx>
#include <teamcenter/services/core/SessionService.hxx>

#include <teamcenter/schemas/soa/_2006_03/exceptions/InvalidCredentialsException.hxx>
#include <teamcenter/schemas/soa/_2006_03/exceptions/ServiceException.hxx>

using namespace std;

// --------------------------------------------------------------------------------
// Constructor - Establish a connection
// --------------------------------------------------------------------------------
AppSession::AppSession(std::string host, AppCredentialManager* credentialManager)
{
    Teamcenter::Soa::Client::Connection::Protocol protocol;
    if ( host.compare(0, 4, "http") == 0 )
    {
        protocol = Teamcenter::Soa::Client::Connection::HTTP;
    }
    else
    {
        protocol = Teamcenter::Soa::Client::Connection::IIOP;
    }

    // Create the Connection object, no contact is made with the server until a service request is made
    connection = new Teamcenter::Soa::Client::Connection(host, credentialManager, protocol, Teamcenter::Soa::Client::Connection::REST);
}

// --------------------------------------------------------------------------------
// Destructor
// --------------------------------------------------------------------------------
AppSession::~AppSession()
{
}

// --------------------------------------------------------------------------------
// Returns the connection
// --------------------------------------------------------------------------------
Teamcenter::Soa::Client::Connection* AppSession::GetConnection()
{
    return connection;
}

// --------------------------------------------------------------------------------
// Do login
// --------------------------------------------------------------------------------
Teamcenter::Soa::Client::Model::User* AppSession::login(string discriminator, AppCredentialManager* credentialManager)
{
    Teamcenter::Services::Core::SessionService* sessionService = Teamcenter::Services::Core::SessionService::getService(this->GetConnection());

    try
    {
        // Using the login operation from Teamcenter::Services::Core::_2008_06::Session class.
        Teamcenter::Services::Core::_2006_03::Session::LoginResponse loginResponse = 
            sessionService->login(credentialManager->getUserName(), credentialManager->getPassword(), NULL, NULL, NULL, discriminator);
        return loginResponse.user;
    }
    catch (Teamcenter::Schemas::Soa::_2006_03::Exceptions::InvalidCredentialsException e)
    {
        cout << e.getMessage() << endl;
    }

    return NULL;
}

// --------------------------------------------------------------------------------
// Do SSO login
// --------------------------------------------------------------------------------
Teamcenter::Soa::Client::Model::User* AppSession::loginSSO(string discriminator, AppCredentialManager* credentialManager)
{
    Teamcenter::Services::Core::SessionService* sessionService = Teamcenter::Services::Core::SessionService::getService(this->GetConnection());

    try
    {
        // Using the loginSSO operation from Teamcenter::Services::Core::_2008_06::Session class.
        Teamcenter::Services::Core::_2006_03::Session::LoginResponse loginResponse = 
            sessionService->loginSSO(credentialManager->getUserName(), credentialManager->getPassword(), NULL, NULL, NULL, discriminator);
        return loginResponse.user;
    }
    catch (Teamcenter::Schemas::Soa::_2006_03::Exceptions::InvalidCredentialsException e)
    {
        cout << e.getMessage() << endl;
    }

    return NULL;
}

// --------------------------------------------------------------------------------
// Do logout
// --------------------------------------------------------------------------------
void AppSession::logout()
{
    Teamcenter::Services::Core::SessionService* sessionService = Teamcenter::Services::Core::SessionService::getService(this->GetConnection());

    try
    {
        sessionService->logout();
    }
    catch (Teamcenter::Schemas::Soa::_2006_03::Exceptions::ServiceException e)
    {
        cout << e.getMessage() << endl;
    }
}

// --------------------------------------------------------------------------------
// Print basic information from a list of objects
// --------------------------------------------------------------------------------
void AppSession::printObjects(Teamcenter::Soa::Client::ModelObjectVector & objects)
{
    if (objects.size() == 0)
        return;

    // Ensure that the referenced User objects that we will use below are loaded
    getUsers(objects);

    cout << setw(32) << "Name" << setw(16) << "Owner" << setw(32) << "Last Modified" << endl;
    cout << setw(80) << setfill('-') << "-" << setfill(' ') << endl;

    for (int i = 0; i < objects.size(); i++)
    {
        if (!objects[i]->getType()->isInstanceOf("WorkspaceObject"))
            continue;

        Teamcenter::Soa::Client::ModelObject* wo = objects[i];
        try
        {
            std::string name = wo->getProperty("object_string")->getStringValue();
            Teamcenter::Soa::Client::ModelObject* owner = wo->getProperty("owning_user")->getModelObjectValue();
            std::string username = owner->getProperty("user_name")->getStringValue();
            std::string lmd = wo->getProperty("last_mod_date")->getDateTimeValue().toString();

            cout << setw(32) << name << setw(16) << username << setw(32) << lmd << endl;
        }
        catch (Teamcenter::Soa::Client::NotLoadedException e)
        {
            // Print out a message, and skip to the next item in the folder
            // Could do a DataManagementService.getProperties call at this point
            cout << e.getMessage() << endl;
            cout << "The Object Property Policy ($TC_DATA/soa/policies/Default.xml) is not configured with this property." << endl;
        }
    }
}

// --------------------------------------------------------------------------------
// Ensure that the referenced User objects are loaded
// --------------------------------------------------------------------------------
void AppSession::getUsers(Teamcenter::Soa::Client::ModelObjectVector & objects)
{
    if(objects.size() == 0)
        return;

    Teamcenter::Services::Core::DatamanagementService* dmService = Teamcenter::Services::Core::DatamanagementService::getService(GetConnection());

    Teamcenter::Soa::Client::ModelObjectVector unknownUsers;
    for (int i = 0; i < objects.size(); i++)
    {
        if (!objects[i]->getType()->isInstanceOf("WorkspaceObject"))
            return;

        Teamcenter::Soa::Client::ModelObject* wo = objects[i];
        Teamcenter::Soa::Client::ModelObject* owner = NULL;

        try
        {
            owner = wo->getProperty("owning_user")->getModelObjectValue();
            owner->getProperty("user_name");
        }
        catch (Teamcenter::Soa::Client::NotLoadedException e)
        {
            if ( owner!=NULL )
                unknownUsers.push_back(owner);
        }

        Teamcenter::Soa::Client::StringVector attributes(1, "user_name");

        dmService->getProperties(unknownUsers, attributes);
    }
}


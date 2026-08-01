/*=============================================================================
  Copyright 2012 Siemens Product Lifecycle Management Software Inc.
  All Rights Reserved.
===============================================================================
File description: Implementation of AppCredentialManager class.


=============================================================================*/

#include "SOAConnectionExample_AppCredentialManager.hpp"

using namespace std;

// --------------------------------------------------------------------------------
// Constructor
// --------------------------------------------------------------------------------
AppCredentialManager::AppCredentialManager(): CredentialManager(), credentials( "", "", "", "", "")
{
}

// --------------------------------------------------------------------------------
// Destructor
// --------------------------------------------------------------------------------
AppCredentialManager::~AppCredentialManager()
{
}

// --------------------------------------------------------------------------------
// Return the credential type
// --------------------------------------------------------------------------------
Teamcenter::Soa::Client::CredentialManager::CredentialsType AppCredentialManager::getCredentialType()
{
    return Teamcenter::Soa::Client::CredentialManager::USERPASSWORD;
}

// --------------------------------------------------------------------------------
// Get the credentials. This method will only be called by the framework when a login attempt has failed.
// --------------------------------------------------------------------------------
Teamcenter::Soa::Client::CredentialManager::Credentials AppCredentialManager::getCredentials(
            Teamcenter::Schemas::Soa::_2006_03::Exceptions::InvalidCredentialsException e)
{
    cout << e.getMessage() << endl;
    return credentials;
}

// --------------------------------------------------------------------------------
// Get the credentials. This method is called when a service request is sent without
// a valid session ( e.g. session has expired on the server).
// --------------------------------------------------------------------------------
Teamcenter::Soa::Client::CredentialManager::Credentials AppCredentialManager::getCredentials(
            Teamcenter::Schemas::Soa::_2006_03::Exceptions::InvalidUserException e)
{
    cout << e.getMessage() << endl;
    return credentials;
}

// --------------------------------------------------------------------------------
// Cache the group and role
// --------------------------------------------------------------------------------
void AppCredentialManager::setGroupRole(const std::string& group, const std::string& role)
{
    credentials.group = group;
    credentials.role = role;
}

// --------------------------------------------------------------------------------
// Cache the User and Password
// --------------------------------------------------------------------------------
void AppCredentialManager::setUserPassword(const std::string& user, const std::string& password, const std::string& discriminator)
{
    credentials.username = user;
    credentials.securetoken = password;
    credentials.descriminator = discriminator;
}

// --------------------------------------------------------------------------------
// Get the username
// --------------------------------------------------------------------------------
std::string& AppCredentialManager::getUserName()
{
    return credentials.username;
}

// --------------------------------------------------------------------------------
// Get the password
// --------------------------------------------------------------------------------
std::string& AppCredentialManager::getPassword()
{
    return credentials.securetoken;
}


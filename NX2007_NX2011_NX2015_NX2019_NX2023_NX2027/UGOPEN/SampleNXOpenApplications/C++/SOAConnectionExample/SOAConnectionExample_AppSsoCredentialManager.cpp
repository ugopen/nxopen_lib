/*=============================================================================
  Copyright 2012 Siemens Product Lifecycle Management Software Inc.
  All Rights Reserved.
===============================================================================
File description: Implementation of AppSsoCredentialManager class.


=============================================================================*/

#include "SOAConnectionExample_AppSsoCredentialManager.hpp"

using namespace std;

// --------------------------------------------------------------------------------
// Constructor
// --------------------------------------------------------------------------------
AppSsoCredentialManager::AppSsoCredentialManager(const std::string &ssoServerUrl, const std::string &ssoAppID):
    AppCredentialManager(), Teamcenter::Soa::Client::SsoCredentials(ssoServerUrl, ssoAppID)
{
}

// --------------------------------------------------------------------------------
// Destructor
// --------------------------------------------------------------------------------
AppSsoCredentialManager::~AppSsoCredentialManager()
{
}

// --------------------------------------------------------------------------------
// Return the credential type
// --------------------------------------------------------------------------------
Teamcenter::Soa::Client::CredentialManager::CredentialsType AppSsoCredentialManager::getCredentialType()
{
    return Teamcenter::Soa::Client::CredentialManager::SSO;
}


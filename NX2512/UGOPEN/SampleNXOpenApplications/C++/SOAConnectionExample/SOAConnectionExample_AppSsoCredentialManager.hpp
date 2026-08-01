/*=============================================================================
  Copyright 2014 Siemens Product Lifecycle Management Software Inc.
  All Rights Reserved.
===============================================================================
File description: Declaration of AppSsoCredentialManager class. This class
derives from both AppCredentialManager and Teamcenter::Soa::Client::SsoCredentials classes.


=============================================================================*/

#ifndef APPSSOCREDENTIALMANAGER_H_INCLUDED
#define APPSSOCREDENTIALMANAGER_H_INCLUDED

#include <iostream>

#include "SOAConnectionExample_AppCredentialManager.hpp"
#include <teamcenter/soa/client/SsoCredentials.hxx>

class AppSsoCredentialManager : public AppCredentialManager, public Teamcenter::Soa::Client::SsoCredentials
{
    public:

        AppSsoCredentialManager(const std::string &ssoServerUrl, const std::string &ssoAppID);
        virtual ~AppSsoCredentialManager();

        // Return the credential type
        virtual Teamcenter::Soa::Client::CredentialManager::CredentialsType getCredentialType();

    private:

        AppSsoCredentialManager(): AppCredentialManager(), Teamcenter::Soa::Client::SsoCredentials("", ""){};

        AppSsoCredentialManager& operator=(const AppSsoCredentialManager&);
        AppSsoCredentialManager(const AppSsoCredentialManager&);
};

#endif // APPSSOCREDENTIALMANAGER_H_INCLUDED

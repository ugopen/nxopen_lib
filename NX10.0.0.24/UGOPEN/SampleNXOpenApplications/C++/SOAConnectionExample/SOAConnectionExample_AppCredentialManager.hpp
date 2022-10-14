/*=============================================================================
  Copyright 2012 Siemens Product Lifecycle Management Software Inc.
  All Rights Reserved.
===============================================================================
File description: Declaration of AppCredentialManager class. This class
derives from the Teamcenter::Soa::Client::CredentialManager class.


=============================================================================*/

#ifndef APPCREDENTIALMANAGER_H_INCLUDED
#define APPCREDENTIALMANAGER_H_INCLUDED

#include <iostream>

#include <teamcenter/soa/client/CredentialManager.hxx>

class AppCredentialManager : public Teamcenter::Soa::Client::CredentialManager
{
    public:

        AppCredentialManager();
        virtual ~AppCredentialManager();

        // Return the credential type
        virtual Teamcenter::Soa::Client::CredentialManager::CredentialsType getCredentialType();

        // Get the credentials. This method will only be called by the framework when a login attempt has failed.
        Teamcenter::Soa::Client::CredentialManager::Credentials getCredentials(
                    Teamcenter::Schemas::Soa::_2006_03::Exceptions::InvalidCredentialsException e);

        // Get the credentials. This method will be called when a service request is sent without a valid
        // session ( e.g. session has expired on the server).
        Teamcenter::Soa::Client::CredentialManager::Credentials getCredentials(
                    Teamcenter::Schemas::Soa::_2006_03::Exceptions::InvalidUserException e);

        // Cache the group and role
        void setGroupRole(const std::string& group, const std::string& role);

        // Cache the User and Password
        void setUserPassword(const std::string& user, const std::string& password, const std::string& discriminator);

        // Get the username
        std::string& getUserName();

        // Get the password
        std::string& getPassword();

    private:

        Teamcenter::Soa::Client::CredentialManager::Credentials credentials;

        AppCredentialManager& operator=(const AppCredentialManager&);
        AppCredentialManager(const AppCredentialManager&);
};

#endif // APPCREDENTIALMANAGER_H_INCLUDED

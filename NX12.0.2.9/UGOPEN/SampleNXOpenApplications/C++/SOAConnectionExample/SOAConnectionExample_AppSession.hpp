/*=============================================================================
  Copyright 2012 Siemens Product Lifecycle Management Software Inc.
  All Rights Reserved.
===============================================================================
File description: Declaration of AppSession class.


=============================================================================*/

#ifndef APPSESSION_H_INCLUDED
#define APPSESSION_H_INCLUDED

#include <iostream>

#include "SOAConnectionExample_AppSsoCredentialManager.hpp"

#include <teamcenter/soa/client/Connection.hxx>
#include <teamcenter/soa/client/model/User.hxx>

class AppSession
{
    public:

        AppSession(std::string host, AppCredentialManager* credentialManager);
        ~AppSession();

        // Get the connection
        Teamcenter::Soa::Client::Connection* GetConnection();

        // Login
        Teamcenter::Soa::Client::Model::User* login(std::string discriminator, AppCredentialManager* credentialManager);

        // SSO login
        Teamcenter::Soa::Client::Model::User* loginSSO(std::string discriminator, AppCredentialManager* credentialManager);

        // Logout
        void logout();

        // Print basic information from a list of objects
        void printObjects(Teamcenter::Soa::Client::ModelObjectVector & objects);

    private:

        Teamcenter::Soa::Client::Connection* connection;

        AppSession& operator=(const AppSession &);
        AppSession(const AppSession &);

        void getUsers(Teamcenter::Soa::Client::ModelObjectVector & objects);
};

#endif // APPSESSION_H_INCLUDED

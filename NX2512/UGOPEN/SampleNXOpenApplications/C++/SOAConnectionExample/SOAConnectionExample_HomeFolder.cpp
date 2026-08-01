/*=============================================================================
  Copyright 2012 Siemens Product Lifecycle Management Software Inc.
  All Rights Reserved.
===============================================================================
File description: Implementaion of HomeFolder class


=============================================================================*/

#include <iomanip>

#include "SOAConnectionExample_HomeFolder.hpp"

#include <teamcenter/soa/client/NotLoadedException.hxx>
#include <teamcenter/soa/client/Property.hxx>

#include <teamcenter/services/core/DatamanagementService.hxx>

using namespace std;

// --------------------------------------------------------------------------------
// List items in the Home folder
// --------------------------------------------------------------------------------
void HomeFolder::listHomeFolder(Teamcenter::Soa::Client::ModelObject* user, AppSession & session)
{
    Teamcenter::Soa::Client::ModelObject* homeObject;
    Teamcenter::Soa::Client::Property* prop;

    // Get the service stub
    Teamcenter::Services::Core::DatamanagementService* dmService = Teamcenter::Services::Core::DatamanagementService::getService(session.GetConnection());

    try
    {
        // The "user" was a primary object returned from the login command. The Object Property Policy should be
        // configured to include the 'home_folder' property. However the actual 'home_folder' object was a 
        // secondary object returned from the login request and therefore does not have any properties associated with it.
        // We will need to get those properties explicitly with a 'getProperties' service request.
        prop = user->getProperty("home_folder");
    }
    catch (Teamcenter::Soa::Client::NotLoadedException e)
    {
        cout << e.getMessage();
        cout << "The Object Property Policy ($TC_DATA/soa/policies/Default.xml) is not configured with this property.";
        return;
    }

    try
    {
        homeObject = prop->getModelObjectValue();

        Teamcenter::Soa::Client::ModelObjectVector objects(1, homeObject);
        Teamcenter::Soa::Client::StringVector attributes(1, "contents");

        // *****************************
        // Execute the service operation
        // *****************************
        dmService->getProperties(objects, attributes);

        // The above getProperties call returns a ServiceData object, but it
        // just has pointers to the same object we passed into the method, so the
        // input object have been updated with new property values
        prop = homeObject->getProperty("contents");
    }
    // This should never be thrown, since we just explicitly asked for this
    // property
    catch (Teamcenter::Soa::Client::NotLoadedException e)
    {
    }

    Teamcenter::Soa::Client::ModelObjectVector contents = prop->getModelObjectArrayValue();

    cout << endl << "Home Folder contents:" << endl;
    cout << setw(80) << setfill('=') << "=" << setfill(' ') << endl;
    session.printObjects( contents );
    cout << setw(80) << setfill('=') << "=" << setfill(' ') << endl;
}


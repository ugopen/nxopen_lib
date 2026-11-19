/*=============================================================================
  Copyright 2012 Siemens Product Lifecycle Management Software Inc.
  All Rights Reserved.
===============================================================================
File description: Implementaion of Query class


=============================================================================*/

#include <iomanip>

#include "SOAConnectionExample_Query.hpp"

#include <teamcenter/schemas/soa/_2006_03/exceptions/ServiceException.hxx>

#include <teamcenter/services/query/SavedqueryService.hxx>
#include <teamcenter/services/query/_2006_03/Savedquery.hxx>

using namespace std;

// --------------------------------------------------------------------------------
// Query the database
// --------------------------------------------------------------------------------
void Query::queryItems(AppSession & session)
{
    Teamcenter::Soa::Client::Model::ImanQuery* query = NULL;

    // Get the service stub
    Teamcenter::Services::Query::SavedqueryService* queryService = Teamcenter::Services::Query::SavedqueryService::getService(session.GetConnection());

    try
    {
        // *****************************
        // Execute the service operation
        // *****************************
        Teamcenter::Services::Query::_2006_03::Savedquery::GetSavedQueriesResponse savedQueries = queryService->getSavedQueries();

        if (savedQueries.queries.size() == 0)
        {
            cout << "There are no saved queries in the system." << endl;
            return;
        }

        // Find one called 'Item Name'
        for (int i = 0; i < savedQueries.queries.size(); i++)
        {
            if ( savedQueries.queries[i].name.compare("Item Name") == 0 )
            {
                query = savedQueries.queries[i].query;
                break;
            }
        }
    }
    catch (Teamcenter::Schemas::Soa::_2006_03::Exceptions::ServiceException e)
    {
        cout << "GetSavedQueries service request failed." << endl;
        cout << e.getMessage() << endl;
        return;
    }

    if (query == NULL)
    {
        cout << "There is not an 'Item Name' query." << endl;
        return;
    }

    try
    {
        // Search for all Items, returning a maximum of 25 objects
        std::vector< std::string > entries(1, std::string("Item Name"));
        std::vector< std::string > values(1, std::string("*"));
        int limit = 25;

        // *****************************
        // Execute the service operation
        // *****************************
        Teamcenter::Services::Query::_2006_03::Savedquery::ExecuteSavedQueryResponse found = queryService->executeSavedQuery(query, entries, values, limit);

        cout << endl << "Items found upon query:" << endl;
        cout << setw(80) << setfill('=') << "=" << setfill(' ') << endl;
        session.printObjects( found.objects );
        cout << setw(80) << setfill('=') << "=" << setfill(' ') << endl;
    }
    catch (Teamcenter::Schemas::Soa::_2006_03::Exceptions::ServiceException e)
    {
        cout << "ExecuteSavedQuery service request failed." << endl;
        cout << e.getMessage() << endl;
        return;
    }
}


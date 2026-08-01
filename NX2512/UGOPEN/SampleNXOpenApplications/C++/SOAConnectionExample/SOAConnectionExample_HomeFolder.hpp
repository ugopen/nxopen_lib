/*=============================================================================
  Copyright 2012 Siemens Product Lifecycle Management Software Inc.
  All Rights Reserved.
===============================================================================
File description: Declaration of HomeFolder class


=============================================================================*/

#ifndef HOMEFOLDER_H_INCLUDED
#define HOMEFOLDER_H_INCLUDED

#include <iostream>

#include "SOAConnectionExample_AppSession.hpp"

#include <teamcenter/soa/client/ModelObject.hxx>

class HomeFolder
{
    public:

        void listHomeFolder(Teamcenter::Soa::Client::ModelObject* user, AppSession & session);
};

#endif // HOMEFOLDER_H_INCLUDED

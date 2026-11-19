/*=============================================================================
  Copyright 2012 Siemens Product Lifecycle Management Software Inc.
  All Rights Reserved.
===============================================================================
File description: Declaration of Query class


=============================================================================*/

#ifndef QUERY_H_INCLUDED
#define QUERY_H_INCLUDED

#include <iostream>

#include "SOAConnectionExample_AppSession.hpp"

class Query
{
    public:

        void queryItems(AppSession & session);
};

#endif // QUERY_H_INCLUDED

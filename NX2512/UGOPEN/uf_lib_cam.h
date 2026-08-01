/*******************************************************************************
            Copyright (c) 2013 Siemens Product Lifecycle Management Software Inc.
                     Unpublished - All rights reserved
 *****************************************************************************
 *
 * 
 *

 *
 * File description:
 * 
 *    All functions are retired and moved to uf_cam_retiring
 *
 *    This file contains documentation for the UF_LIB module. This module
 *    allows the Open API programmer to interface with the Libraries that NX
 *    uses for retrieving objects such as Machine Tools, Cutters, Tool
 *    Material and Feeds and Speeds. The programmer can perform functions
 *    such as retrieving objects into NX and asking for the values of
 *    attributes of objects in a Library.
 *
 *    The query syntax:
 *
 *    An application can create a query that contains the constraints which
 *    should be used in selecting objects in the Library. The query must be
 *    specified using the query language.  The language of a query is very
 *    simple. It is a collection of criteria which are connected to each other
 *    with certain logical operators. A criterion has the form:
 *
 *             [Attribute Name] [Relational Operator] [Expression]
 *
 *    where a(n)
 *
 *    [Attribute Name] is a NX name of one of the database attributes of the
 *                     objects being queried,
 *
 *
 *    [Relational Operator] is one of <, <=, ==, !=, >, >=, &=, &!,
 *
 *    [Expression] is an expression made up of (primarily) NX Expression
 *                 SubSystem (ESS) expressions and NX Names.
 *
 *    If the operator is &= or &! then [Expression] is an egrep style regular
 *    expression (see man pages on egrep or TCL regular expressions). We
 *    describe these expressions in more detail below.
 *
 *    The Relational Operators &=  and &! mean String Equal and String Not
 *    Equal, resp.
 *
 *    The logical operators allowed are && and || with && having
 *    precedence over ||.
 *
 *    An NX name is a non database-specific name for an attribute of an object
 *    that is stored in a library. (These names are defined in the Definition
 *    File of the DBC object used for the query.) For example, a query might
 *    use Tool_Diameter to specify the diameter of the tool, whereas, Genius
 *    may use a UNCT of -1001 to denote the tool diameter. In this case
 *    Tool_Diameter is the NX Name.
 *
 *    The query language places very few restrictions on the form of an
 *    [Expression].
 *    The restrictions are:
 *
 *    1) each occurrence of an NX ESS expression must be surrounded by
 *       delimiters and,
 *
 *    2) each occurrence of an NX name must be surrounded by delimiters.
 *       (The delimiters are also defined in the Definition File of the DBC
 *       object used for the query.)
 *
 *    3) the entire [Expression] must be a valid TCL expression.
 *
 *    In the following examples of QRY queries, we use DB( and ) as the NX Name
 *    start and end delimiters, resp., and ESS( and ) as the ESS start and end
 *    delimiters, resp. These are user-defined via the DBC Definition File
 *
 *    Here are 2 examples of QRY queries:
 *
 *    [DB(Tool_Diameter)] >= [0.25] && [DB(Tool_Diameter)] <= [0.50]
 *
 *    [DB(Tool_Diameter)] < [2 * ESS(Corner_Radius)] &&
 *    [DB(Num_Of_Flutes)] == [3 * ESS(Height)] && [DB(Material)] &=
 *    ["^STEEL[123]$"] && [DB(Catalog)] &! ["^.*VENDOR_A.*$"]
 *
 ******************************************************************************/
#ifndef UF_LIB_CAM_H_INCLUDED
#define UF_LIB_CAM_H_INCLUDED

 // The functions in this file are in the process of being removed from the Open C API product and
 // therefor moved to another header file to indicate it.

 // Please replace the include of this header file with this one for now:
 //       # include <uf_cam_retiring.h>

 // Please look at the description of the function to see how it can be replaced with the NXOpen equivalent.

#endif /* UF_LIB_CAM_H_INCLUDED */

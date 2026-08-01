/*****************************************************************************
                                 Copyright 2022 Siemens
                                  All Rights Reserved



File description:
    Open API for Logic Editor and NXOpen communication
*****************************************************************************/

#ifndef UF_RULE_NXOPEN_H_INCLUDED
#define UF_RULE_NXOPEN_H_INCLUDED

/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <libufun_rule_nxopen_exports.h>

/***************************************************************************
   Prototypes for Logic Editor and NXOpen communication
  ***************************************************************************/

/*****************************************************************************
Sets the output for the Execute NXOpen node

Environment: Internal  and  External
See Also:
History:
 ****************************************************************************/
 extern UFUN_RULE_NXOPENEXPORT void UF_RULE_set_node_output(
     int id,                    /* internal identifier of the Execute NXOpen node, obtained from the parameters input of the node */
     const char* resultString   /* the result of the NXOpen program in the format of a Json string */
 );/*<NON_NXOPEN>*/

#undef EXPORTLIBRARY

#endif     /* UF_RULE_NXOPEN_H_INCLUDED */

/*=============================================================================

                    Copyright (c) 2023 Siemens 
                    Unpublished - All rights reserved

===============================================================================
File description: Sample NX/Open Application
===============================================================================

=============================================================================
*/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


class BlockCallingBlock_Util
{

    public static bool m_testMode = true; // This flag is used to indicate to run the 
                                          // The dialog in test mode.  When the Select
                                          // Face button is pushed, we will pass the 
                                          // JournalIdentifier for the face to select
                                          // And then since this satisfies the condition
                                          // for in SubDialog we call the PerformOK
                                          // button.

}

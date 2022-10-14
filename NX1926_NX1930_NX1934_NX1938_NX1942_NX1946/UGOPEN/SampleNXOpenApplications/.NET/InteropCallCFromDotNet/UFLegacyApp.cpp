/*=============================================================================
                  Copyright (c) 2009 Siemens
                      All rights reserved
===============================================================================
UFapp.cxx

Description: Sample code showing interactions with a .NET applications (VBapp)

 
=============================================================================*/
#include <stdio.h>

#include <uf.h>
#include <uf_ui.h>
#include <uf_mb.h>
#include <uf_exit.h>

#define MAX_STRING_SIZE 255

//*********************************************************************************************** 
// Two local functions to be called via wrappers from .NET 
static int myFunction1(void) 
{           

        UF_initialize();     
        UF_print_syslog("BEGIN myFunction1\n",0);      

        UF_print_syslog("END myFunction1\n",0);      

        return(77); 
} 
//*********************************************************************************************** 
static int myFunction2(int value, char *string) 
{     
        int ret1,ret2;     
        char message[MAX_STRING_SIZE] = "";      

        ret1 = ret2 = 0;      

        sprintf_s(message,"value:%d string:%s\n",value,string);      

        UF_initialize();     
        UF_print_syslog("BEGIN myFunction2\n",0);     
        UF_print_syslog(message,0);      

        UF_print_syslog("END myFunction2\n",0);      

        return(value+1); 
}

//*********************************************************************************************** 
// Wrappers for local functions to be called from .NET  

extern "C" __declspec(dllexport) int UFappFunction1(void) 
{     
        return( myFunction1() ); 
}  

//*********************************************************************************************** 
// Another local function to be called from .NET  

extern "C" __declspec(dllexport) int UFappFunction2(int value, char *string) 
{     
        return ( myFunction2(value,string) ); 

} 



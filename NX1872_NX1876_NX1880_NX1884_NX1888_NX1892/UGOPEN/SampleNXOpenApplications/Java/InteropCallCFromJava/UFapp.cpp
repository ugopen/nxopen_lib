/*=============================================================================
                  Copyright (c) 2009 Siemens
                      All rights reserved
===============================================================================
UFapp.cxx

Description: Sample code showing interactions with a Java applications 

 
=============================================================================*/
//
#include <stdio.h>

#include <uf.h>
#include <uf_ui.h>
#include <uf_mb.h>
#include <uf_exit.h>
#include "JavaApp.h"

#define MAX_STRING_SIZE 255

 
//***********************************************************************************************
// Two local functions to be called via Java JNI functions
static int myFunction1(void)
{

    
    UF_initialize();
    UF_print_syslog("BEGIN myFunction1\n",0);

    UF_print_syslog("END myFunction1\n",0);

    return(77);
}
//***********************************************************************************************
static int myFunction2(int value, const char *string)
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
// Java functions

JNIEXPORT jint JNICALL Java_JavaApp_nativeUFappFunction1(JNIEnv *env, jobject obj)
{    // Call the local functions
    int ret = myFunction1();
    return(ret);
}
JNIEXPORT jint JNICALL Java_JavaApp_nativeUFappFunction2(JNIEnv *env, jobject obj, jint a, jstring name)
{
    // Get the characters from the jstring
    const char *str = env->GetStringUTFChars(name, 0);
    // Call the local function
    int ret = myFunction2( (int)a, str );
    // Release memory (required or else memory leaks)
    env->ReleaseStringUTFChars(name, str);
    return ret;
}



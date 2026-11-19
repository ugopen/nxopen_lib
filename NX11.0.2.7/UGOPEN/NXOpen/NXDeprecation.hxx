/*******************************************************************************
               Copyright (c) 2004 Unigraphics Solutions Inc.
                      Unpublished - All Rights Reserved


*******************************************************************************/
#ifndef NXDeprecation_HXX_INCLUDED
#define NXDeprecation_HXX_INCLUDED

//  

#ifdef _MSC_VER 
#pragma once
#pragma warning(1:4996)
#define NX_DEPRECATED(s) __declspec(deprecated(s)) 
#elif __GNUC__  
#define NX_DEPRECATED(s) __attribute__((deprecated))
#else
#define NX_DEPRECATED(s) 
#endif

//  

#endif //NXDeprecation_HXX_INCLUDED

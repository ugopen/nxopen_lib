/*========================================================================================== 

    This material contains trade secrets or otherwise confidential information owned by
    Siemens Industry Software Inc. or its affiliates (collectively, "SISW"), or its licensors.
    Access to and use of this information is strictly limited as set forth in the Customer's
    applicable agreements with SISW.

    Unpublished work Copyright 2022 Siemens

===========================================================================================

==========================================================================================*/
#pragma once

//  

#if __clang__  
#define UGOPENCPP_DEPRECATED(s) __attribute__((deprecated(s)))
#elif defined(_MSC_VER)
#pragma once
#pragma warning(1:4996)
#define UGOPENCPP_DEPRECATED(s) __declspec(deprecated(s)) 
#elif __GNUC__  
#define UGOPENCPP_DEPRECATED(s) __attribute__((deprecated))
#else
#define UGOPENCPP_DEPRECATED(s) 
#endif

//  


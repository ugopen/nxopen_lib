#ifndef NXOpen_CALLBACKTESTNAMESPACE_SUBSPACE_CALLBACKTRANSIENTOBJ_HXX_INCLUDED
#define NXOpen_CALLBACKTESTNAMESPACE_SUBSPACE_CALLBACKTRANSIENTOBJ_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CallbackTestNamespace_Subspace_CallbackTransientObj.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CallbackTestNamespace
    {
        namespace Subspace
        {
            class CallbackTransientObj;
        }
    }
    namespace CallbackTestNamespace
    {
        namespace Subspace
        {
            class CallbackTransientObjImpl;
            /** Test class for testing a class inside a nested namespace  <br> not done yet  <br> 
             <br>  Created in NX5.0.0.  <br>  
            */
            class NXOPENDEBUGSESSIONCPPEXPORT  CallbackTransientObj : public TransientObject
            {
                 /** The struct */
                public:
                struct  Struct1
                {
                    public: /** int value */ int IntValue;
                    public: /** double value */ double DoubleValue;
                    public: Struct1() :
                        IntValue(),
                        DoubleValue()
                    {
                    }
                    /** Constructor for the Struct1 struct. */ 
                    public: Struct1(int intValueInitial /** int value */ , 
                            double doubleValueInitial /** double value */ ) :
                        IntValue(intValueInitial),
                        DoubleValue(doubleValueInitial)
                    {
                    }
                };

                /** The type */
                public: enum ObjType
                {
                    ObjTypeZero/** zero */ ,
                    ObjTypeOne/** one */ 
                };

                private: CallbackTransientObjImpl * m_callbacktransientobj_impl;
                /// \cond NX_NO_DOC 
                public: explicit CallbackTransientObj(void *ptr);
                /// \endcond 
                /** Disposes of object 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual ~CallbackTransientObj();
                /**Returns  the type 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CallbackTestNamespace::Subspace::CallbackTransientObj::ObjType Type
                (
                );
                /**Returns  the int id 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : None */
                public: int IntId
                (
                );
                /**Sets  the int id 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetIntId
                (
                    int id /** id */ 
                );
                /** Sets the struct 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetStruct
                (
                    const NXOpen::CallbackTestNamespace::Subspace::CallbackTransientObj::Struct1 & input /** input */ 
                );
                /** Gets the struct  @return  
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CallbackTestNamespace::Subspace::CallbackTransientObj::Struct1 GetStruct
                (
                );
            }; //lint !e1712 default constructor not defined for class  

        }
    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif

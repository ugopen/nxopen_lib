#ifndef NXOpen_CALLBACKTESTNAMESPACE_SUBSPACE_CALLBACKTRANSIENTOBJB_HXX_INCLUDED
#define NXOpen_CALLBACKTESTNAMESPACE_SUBSPACE_CALLBACKTRANSIENTOBJB_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CallbackTestNamespace_Subspace_CallbackTransientObjB.ja
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
#include <NXOpen/CallbackTestNamespace_Subspace_CallbackTransientObj.hxx>
#include <NXOpen/libnxopendebugsessioncpp_exports.hxx>
namespace NXOpen
{
    namespace CallbackTestNamespace
    {
        namespace Subspace
        {
            class CallbackTransientObjB;
        }
    }
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
            class CallbackTransientObjBImpl;
            /** Test class for testing a class inside a nested namespace  <br> not done yet <br> */
            class NXOPENDEBUGSESSIONCPPEXPORT  CallbackTransientObjB : public CallbackTestNamespace::Subspace::CallbackTransientObj
            {
                 /** The struct */
                public:
                struct  Struct2
                {
                    public: /** boolean value */ bool BooleanValue;
                    public: /** string value */ NXString StringValue;
                    public: Struct2() :
                        BooleanValue(),
                        StringValue()
                    {
                    }
                    /** Constructor for the Struct2 struct. */ 
                    public: Struct2(bool booleanValueInitial /** boolean value */ , 
                            const NXString &stringValueInitial /** string value */ ) :
                        BooleanValue(booleanValueInitial),
                        StringValue(stringValueInitial)
                    {
                    }
                };

                private: CallbackTransientObjBImpl * m_callbacktransientobjb_impl;
                public: explicit CallbackTransientObjB(void *ptr);
                /** Sets the struct  <br> License requirements : None */
                public: void SetStructB
                (
                    const NXOpen::CallbackTestNamespace::Subspace::CallbackTransientObjB::Struct2 & input /** input */ 
                );
                /** Gets the struct  @return   <br> License requirements : None */
                public: NXOpen::CallbackTestNamespace::Subspace::CallbackTransientObjB::Struct2 GetStructB
                (
                );
            }; //lint !e1712 default constructor not defined for class  

        }
    }
}
#undef EXPORTLIBRARY
#endif

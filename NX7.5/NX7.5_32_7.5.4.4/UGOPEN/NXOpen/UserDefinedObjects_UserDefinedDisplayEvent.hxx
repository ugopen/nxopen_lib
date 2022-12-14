#ifndef NXOpen_USERDEFINEDOBJECTS_USERDEFINEDDISPLAYEVENT_HXX_INCLUDED
#define NXOpen_USERDEFINEDOBJECTS_USERDEFINEDDISPLAYEVENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     UserDefinedObjects_UserDefinedDisplayEvent.ja
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
#include <NXOpen/UserDefinedObjects_UserDefinedEvent.hxx>
#include <NXOpen/UserDefinedObjects_UserDefinedObjectDisplayContext.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace UserDefinedObjects
    {
        class UserDefinedDisplayEvent;
    }
    namespace UserDefinedObjects
    {
        class UserDefinedEvent;
    }
    namespace UserDefinedObjects
    {
        class UserDefinedObjectDisplayContext;
    }
    namespace UserDefinedObjects
    {
    }
    namespace UserDefinedObjects
    {
        class UserDefinedDisplayEventImpl;
        /** Implements the Display Event Object for UDO's */
        class NXOPENCPPEXPORT  UserDefinedDisplayEvent : public UserDefinedObjects::UserDefinedEvent
        {
            private: UserDefinedDisplayEventImpl * m_userdefineddisplayevent_impl;
            public: explicit UserDefinedDisplayEvent(void *ptr);
            /** Frees the object from memory.  After this method is
                        called, it is illegal to use the object.  In .NET and Java,
                        his method is automatically called when the object is
                        deleted by the garbage collector.   <br> License requirements : None */
            public: virtual ~UserDefinedDisplayEvent();
            /**Returns  the display context.  <br> License requirements : None */
            public: NXOpen::UserDefinedObjects::UserDefinedObjectDisplayContext * DisplayContext
            (
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif

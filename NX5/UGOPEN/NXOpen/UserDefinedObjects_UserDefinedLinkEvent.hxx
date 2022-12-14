#ifndef NXOpen_USERDEFINEDOBJECTS_USERDEFINEDLINKEVENT_HXX_INCLUDED
#define NXOpen_USERDEFINEDOBJECTS_USERDEFINEDLINKEVENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     UserDefinedObjects_UserDefinedLinkEvent.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/UserDefinedObjects_UserDefinedEvent.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace UserDefinedObjects
    {
        class UserDefinedLinkEvent;
    }
    namespace UserDefinedObjects
    {
        class UserDefinedEvent;
    }
    namespace UserDefinedObjects
    {
    }
    namespace UserDefinedObjects
    {
        /** Implements the Display Event Object for UDO's */
        class NXOPENCPPEXPORT UserDefinedLinkEvent : public UserDefinedObjects::UserDefinedEvent
        {
            public: explicit UserDefinedLinkEvent(void *ptr);
            /** Frees the object from memory.  After this method is
                        called, it is illegal to use the object.  In .NET and Java,
                        his method is automatically called when the object is
                        deleted by the garbage collector.   <br> License requirements : None */
            public: virtual ~UserDefinedLinkEvent();
            /**Returns  the link type.  <br> License requirements : None */
            public: int LinkType
            (
            );
            /**Returns  the link status.  <br> License requirements : None */
            public: int LinkStatus
            (
            );
            /**Returns  the associated object.  <br> License requirements : None */
            public: NXOpen::TaggedObject * AssociatedObject
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif

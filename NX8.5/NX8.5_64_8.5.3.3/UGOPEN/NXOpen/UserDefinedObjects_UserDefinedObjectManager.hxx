#ifndef NXOpen_USERDEFINEDOBJECTS_USERDEFINEDOBJECTMANAGER_HXX_INCLUDED
#define NXOpen_USERDEFINEDOBJECTS_USERDEFINEDOBJECTMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     UserDefinedObjects_UserDefinedObjectManager.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/UserDefinedObjects_UserDefinedClass.hxx>
#include <NXOpen/UserDefinedObjects_UserDefinedObject.hxx>
#include <NXOpen/libnxopencpp_userdefinedobjects_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace UserDefinedObjects
    {
        class UserDefinedObjectManager;
    }
    class BasePart;
    class TaggedObject;
    namespace UserDefinedObjects
    {
        class UserDefinedClass;
    }
    namespace UserDefinedObjects
    {
        class UserDefinedObject;
    }
    namespace UserDefinedObjects
    {
        class UserDefinedObjectManagerImpl;
        /** This class creates and manages UserDefinedObjects  <br> To obtain an instance of this class, refer to @link BasePart  BasePart @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_USERDEFINEDOBJECTSEXPORT  UserDefinedObjectManager
        {
             /** Used to define a link to a UserDefinedObject */
            public:
            struct  LinkedUdoDefinition
            {
                public: /** link type */ NXOpen::UserDefinedObjects::UserDefinedObject::LinkType LinkType;
                public: /** associated udo */ NXOpen::UserDefinedObjects::UserDefinedObject * AssociatedUdo;
                public: /** status */ NXOpen::UserDefinedObjects::UserDefinedObject::LinkStatus Status;
                public: LinkedUdoDefinition() :
                    LinkType((NXOpen::UserDefinedObjects::UserDefinedObject::LinkType)0),
                    AssociatedUdo(),
                    Status((NXOpen::UserDefinedObjects::UserDefinedObject::LinkStatus)0)
                {
                }
                /** Constructor for the LinkedUdoDefinition struct. */ 
                public: LinkedUdoDefinition(NXOpen::UserDefinedObjects::UserDefinedObject::LinkType linkTypeInitial /** link type */ , 
                        NXOpen::UserDefinedObjects::UserDefinedObject * associatedUdoInitial /** associated udo */ , 
                        NXOpen::UserDefinedObjects::UserDefinedObject::LinkStatus statusInitial /** status */ ) :
                    LinkType(linkTypeInitial),
                    AssociatedUdo(associatedUdoInitial),
                    Status(statusInitial)
                {
                }
            };

            private: UserDefinedObjectManagerImpl * m_userdefinedobjectmanager_impl;
            private: NXOpen::BasePart* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit UserDefinedObjectManager(NXOpen::BasePart *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~UserDefinedObjectManager();
            /** 
                      Constructs a new @link UserDefinedObject UserDefinedObject@endlink .
                      @return  The new UserDefinedObject instance 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::UserDefinedObjects::UserDefinedObject * CreateUserDefinedObject
            (
                NXOpen::UserDefinedObjects::UserDefinedClass * udoClass /** The UserDefinedClass used to define the new UserDefinedObject  */
            );
            /** Finds all @link UserDefinedObjects::UserDefinedObject UserDefinedObjects::UserDefinedObject@endlink  instances that use the given @link UserDefinedObjects::UserDefinedClass UserDefinedObjects::UserDefinedClass@endlink .  @return  User Defined Objects of the given class 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::UserDefinedObjects::UserDefinedObject *> GetUdosOfClass
            (
                NXOpen::UserDefinedObjects::UserDefinedClass * udoClass /** The UserDefinedClass we want to find */
            );
            /** Queries an NX Object to see if it can be linked to a @link UserDefinedObjects::UserDefinedObject UserDefinedObjects::UserDefinedObject@endlink  via the given link type  @return  TRUE - This object can be linked to a UDO with the given link type, FALSE - this object can not be NOT linked to a UDO with the given link type 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsObjectLinkable
            (
                NXOpen::TaggedObject * linkObject /** NXObject to query for linkability */,
                NXOpen::UserDefinedObjects::UserDefinedObject::LinkType linkType /** The link type used to link this object to a UDO */
            );
            /** Queries an NX Object to see if it is linked to a @link UserDefinedObjects::UserDefinedObject UserDefinedObjects::UserDefinedObject@endlink  (note this will not
                    tell you if the object is owned by a UDO with an owning link)  @return  TRUE - This object is linked to a UDO, FALSE - this object is NOT linked to a UDO 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsObjectLinkedToUserDefinedObject
            (
                NXOpen::TaggedObject * linkObject /** NXObject to query for links */
            );
            /** Queries an NX Object to find all @link UserDefinedObjects::UserDefinedObject UserDefinedObjects::UserDefinedObject@endlink 's that are linked to the given NXObject (note this will not find owning udos)  @return  The link definitions from UDO's to the NXObject 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::UserDefinedObjects::UserDefinedObjectManager::LinkedUdoDefinition> GetLinksToObject
            (
                NXOpen::TaggedObject * linkObject /** NXObject to query for links */
            );
            /** Queries an NX Object to see if it is owned by a @link UserDefinedObjects::UserDefinedObject UserDefinedObjects::UserDefinedObject@endlink   @return  TRUE - This object is owned by a UDO, FALSE - this object is NOT owned by a UDO 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsObjectOwnedByUserDefinedObject
            (
                NXOpen::TaggedObject * linkObject /** NXObject to query for an owning UDO */
            );
            /** Queries an NX Object to find the @link UserDefinedObjects::UserDefinedObject UserDefinedObjects::UserDefinedObject@endlink  that owns the given NXObject (note this will return null for the owning udo if the object is not owned)  @return  The UDO which owns the NXObject 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::UserDefinedObjects::UserDefinedObject * GetOwningUserDefinedObject
            (
                NXOpen::TaggedObject * linkObject /** NXObject to query for an owning UDO */
            );
        }; //lint !e1712 default constructor not defined for class  

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
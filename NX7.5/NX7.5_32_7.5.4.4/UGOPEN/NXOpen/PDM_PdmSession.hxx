#ifndef NXOpen_PDM_PDMSESSION_HXX_INCLUDED
#define NXOpen_PDM_PDMSESSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PDM_PdmSession.ja
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
#include <NXOpen/PDM_FileManagement.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace PDM
    {
        class PdmSession;
    }
    class Session;
    namespace PDM
    {
        class FileManagement;
    }
    namespace PDM
    {
        class PdmSessionImpl;
        /** Represents the NX Manager session  <br> To obtain an instance of this class, refer to @link Session Session@endlink  <br> */
        class NXOPENCPPEXPORT  PdmSession
        {
            private: PdmSessionImpl * m_pdmsession_impl;
            private: NXOpen::Session* m_owner;
            /** Constructor */
            public: explicit PdmSession(NXOpen::Session *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~PdmSession();
            /**  Returns the connect string and discriminator used by NX session to connect to the Tcserver.
                         The client applications can use these settings to connect to the same Tcserver that NX
                         is using.
                         
                         Tcserver connect string: The connect string is path of the server hosting the services.
                         The connect string for the different transport protocols will be in the following form:
                         4-Tier(HTTP mode): similar to http:
                         2-Tier(IIOP mode): The Tcserver IOR string 
                         
                         Discriminator: The discriminator is a unique identifier and contains unique information related 
                         to a given TC server. This unique identifier (discriminator) is recognized by TC pool manager as
                         the session number that ties the server process to the client. The discriminator functionality 
                         is part of the SOA package. The discriminator allows multiple clients to connect to the same TC server.
                         In 2-Tier(IIOP mode), the discriminator will be an empty string.
                     <br> License requirements : None */
            public: void GetTcserverSettings
            (
                NXString* connectString /** the connection string */,
                NXString* discriminator /** the discriminator */
            );
            /** Sets default folder  <br> License requirements : None */
            public: void SetDefaultFolder
            (
                const NXString & defaultFolderSpec /** Default folder path including default folder name to be set */
            );
            /** Returns a new @link PDM::FileManagement PDM::FileManagement@endlink  object  @return   <br> License requirements : None */
            public: NXOpen::PDM::FileManagement * NewFileManagement
            (
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif

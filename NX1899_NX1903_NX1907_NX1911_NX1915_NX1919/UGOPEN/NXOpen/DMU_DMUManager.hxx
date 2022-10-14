#ifndef NXOpen_DMU_DMUMANAGER_HXX_INCLUDED
#define NXOpen_DMU_DMUMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     DMU_DMUManager.ja
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
#include <NXOpen/libdmuopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace DMU
    {
        class DMUManager;
    }
    class Session;
    namespace DMU
    {
        class SnapshotCollection;
    }
    class Part;
    namespace DMU
    {
        class DMUManagerImpl;
        /** Represents an object that manages DMU application specific objects and preferences.
              <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class DMUOPENCPPEXPORT  DMUManager
        {
            private: DMUManagerImpl * m_dmumanager_impl;
            private: NXOpen::Session* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit DMUManager(NXOpen::Session *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            private: static DMUManager* theDMUManager;
            /** Returns the DMUManager object for the running session which serves as the 'gateway' class for the application API.  
                References to all other objects in this API are obtained either directly or indirectly via methods and properties on this class.  
                Platform Session should be initialized using 'GetSession' method from NXOpen API prior to this call.  
            */
            public: static DMUManager* GetDMUManager(NXOpen::Session *owner);
            public: ~DMUManager();
            /** Creates the @link NXOpen::DMU::SnapshotCollection NXOpen::DMU::SnapshotCollection@endlink  in the part.
                        At max only one instance of @link NXOpen::DMU::SnapshotCollection NXOpen::DMU::SnapshotCollection@endlink 
                        can be created in a part.
                    
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::DMU::SnapshotCollection * CreateSnapshotCollection
            (
                NXOpen::Part * part /** part */ 
            );
            /** Returns the @link NXOpen::DMU::SnapshotCollection NXOpen::DMU::SnapshotCollection@endlink  in the part. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::DMU::SnapshotCollection * GetSnapshotCollection
            (
                NXOpen::Part * part /** part */ 
            );
            /** Resets the changes made to the part, related to the assets which can be captured in the 
                        @link NXOpen::DMU::ISnapshot NXOpen::DMU::ISnapshot@endlink .
                    
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : assemblies ("ASSEMBLIES MODULE") */
            public: void ResetToDesignState
            (
                NXOpen::Part * part /** Part that will get reset to design state*/
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
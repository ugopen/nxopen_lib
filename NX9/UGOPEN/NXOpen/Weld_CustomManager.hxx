#ifndef NXOpen_WELD_CUSTOMMANAGER_HXX_INCLUDED
#define NXOpen_WELD_CUSTOMMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_CustomManager.ja
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
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_weld_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Weld
    {
        class CustomManager;
    }
    class Session;
    namespace Weld
    {
        class EdgePrep;
    }
    class Curve;
    namespace Weld
    {
        class DatumIconBuilder;
    }
    namespace Weld
    {
        class JointExitBuilder;
    }
    namespace Weld
    {
        class WeldJointBuilder;
    }
    namespace Weld
    {
        class WeldObjectBuilder;
    }
    namespace Weld
    {
        class WeldPointExitBuilder;
    }
    namespace Weld
    {
        class CustomManagerImpl;
        /** Represents weld interface to customize the creation of welding joint features.

           <br>  
           The "welding joint handler" customization callback is called after the feature is created.
           One can then set edge preparation parameters, change the color of the feature output curve,
           add attributes to the feature, or any additional customization.

           The "variable bevel handler" customization callback is used to define the limits where a welding joint
           should be split at. 
         
           <br> 
           <br> To obtain an instance of this class, refer to @link Session  Session @endlink  <br> 
         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_WELDEXPORT  CustomManager : public TaggedObjectCollection
        {
            public: /** User defined method that is called whenever a welding joint is created or updated 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            typedef NXOpen::Callback1<void, NXOpen::Weld::JointExitBuilder *> WeldJointHandler;
            public: /** User defined method that returns the angle divisions for a variable bevel. The first value must be 0.0, and the last value 90.0 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            typedef NXOpen::Callback2<void, NXOpen::Weld::WeldJointBuilder *, NXOpen::Curve *> VariableBevelHandler;
            public: /** User defined method that is called whenever a welding joints are created or edited 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : None */
            typedef NXOpen::Callback1<void, NXOpen::Weld::WeldObjectBuilder *> ModifyFeatureHandler;
            public: /** User defined method that is called whenever a welding features are created through Weld Point command. 
             <br>  Created in NX8.0.2.  <br>  
             <br> License requirements : None */
            typedef NXOpen::Callback1<void, NXOpen::Weld::WeldPointExitBuilder *> PointExitHandler;
            public: /** Method called from the part navigator to define the datum surface and pin icon. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            typedef NXOpen::Callback1<void, NXOpen::Weld::DatumIconBuilder *> DatumIconHandler;
            private: CustomManagerImpl * m_custommanager_impl;
            private: NXOpen::Session* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit CustomManager(NXOpen::Session *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~CustomManager();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::Weld::CustomManager::iterator::copy,initializer)
            class iterator
            {
            public:
                /** Value type associated with iterator*/ 

                typedef Weld::EdgePrep * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                { // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::Weld::CustomManager *context) : m_context(context), m_current(NULL_TAG)
                { // coverity[uninit_member]
                }//lint !e1401 m_state is not initialized
                /// \endcond
                /** Copy constructor */
                iterator(const iterator &other): m_context(NULL), m_current(NULL_TAG)
                {
                    copy(other);
                }
                /** Copy constructor */
                iterator &operator =(const iterator &other)
                {
                    if (&other != this)
                        copy(other);
                    return *this;
                }
                /** Tests if the iterator objects on the left side and the right side of the operator are equal. */
                bool operator ==(const iterator &other) const
                {
                    return m_current == other.m_current && m_context == other.m_context;
                }
                /** Tests if the iterator objects on the left side and the right side of the operator are not equal. */
                bool operator !=(const iterator &other) const
                {
                    return !operator == (other);
                }
                /** Return the element currently pointed to by the iterator. */
                NXOPENCPP_WELDEXPORT  value_type operator * ();
                /** Points the iterator to next element. */
                iterator & operator ++()
                {
                    next();
                    return *this;
                }
                /** Points the iterator to next element. */
                iterator operator ++(int)
                {
                    iterator tmp(*this);
                    ++*this;
                    return tmp;
                }
            private:
                void copy(const iterator &other)
                {
                    m_context = other.m_context;
                    m_current = other.m_current;
                    for (int i = 0; i < sizeof(m_state)/sizeof(m_state[0]); i++)
                         m_state[i] = other.m_state[i];
                }
                NXOPENCPP_WELDEXPORT  void next();
                NXOpen::Weld::CustomManager *m_context;
                tag_t m_current;
                unsigned int m_state[8];
            };
            /** Returns an iterator addressing the first element. */
            iterator begin();
            /** Returns an iterator addressing one past the last element. */
            iterator end()
            {
                return iterator(this);
            }
            /** Registers a user defined method that is called whenever a welding joint is created or updated  @return  identifier of registered method (used to unregister the method) 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: int AddWeldJointHandler
            (
                const NXOpen::Weld::CustomManager::WeldJointHandler&  handler /** method to register */
            );
            /** Unregisters the welding joint handler 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void RemoveWeldJointHandler
            (
                int id /** identifier for method to unregister */
            );
            /** Registers a user defined method to define variable bevel angles. The method will be called from the Weld Joint user Interface.  @return  identifier of registered method (used to unregister the method) 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: int AddVariableBevelHandler
            (
                const NXOpen::Weld::CustomManager::VariableBevelHandler&  handler /** method to register */
            );
            /** Unregisters the variable bevel handler 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void RemoveVariableBevelHandler
            (
                int id /** identifier for method to unregister */
            );
            /** Registers a user defined method to be notified when weld features are created or edited.  @return  identifier of registered method (used to unregister the method) 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : None */
            public: int AddModifyFeatureHandler
            (
                const NXOpen::Weld::CustomManager::ModifyFeatureHandler&  handler /** method to register */
            );
            /** Unregisters the modify feature handler 
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : None */
            public: void RemoveModifyFeatureHandler
            (
                int id /** identifier for method to unregister */
            );
            /** Registers a user defined method to be notified when weld point features are created.  @return  identifier of registered method (used to unregister the method) 
             <br>  Created in NX8.0.2.  <br>  
             <br> License requirements : None */
            public: int AddPointExitHandler
            (
                const NXOpen::Weld::CustomManager::PointExitHandler&  handler /** method to register */
            );
            /** Unregisters the point feature handler 
             <br>  Created in NX8.0.2.  <br>  
             <br> License requirements : None */
            public: void RemovePointExitHandler
            (
                int id /** identifier for method to unregister */
            );
            /** Registers a user defined method to be notified when the part navigator is updating the surface or pin datum icon.  @return  identifier of registered method (used to unregister the method) 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: int AddDatumIconHandler
            (
                const NXOpen::Weld::CustomManager::DatumIconHandler&  handler /** method to register */
            );
            /** Unregisters the datum common icon handler 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void RemoveDatumIconHandler
            (
                int id /** identifier for method to unregister */
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

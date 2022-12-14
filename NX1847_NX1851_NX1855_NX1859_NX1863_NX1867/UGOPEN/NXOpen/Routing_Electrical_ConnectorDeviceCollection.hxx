#ifndef NXOpen_ROUTING_ELECTRICAL_CONNECTORDEVICECOLLECTION_HXX_INCLUDED
#define NXOpen_ROUTING_ELECTRICAL_CONNECTORDEVICECOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_Electrical_ConnectorDeviceCollection.ja
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
#include <iterator>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/Routing_Electrical_ConnectorDevice.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_routing_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Routing
    {
        namespace Electrical
        {
            class ConnectorDeviceCollection;
        }
    }
    namespace Routing
    {
        class RouteManager;
    }
    namespace Routing
    {
        namespace Electrical
        {
            class ConnectorDevice;
        }
    }
    namespace Routing
    {
        namespace Electrical
        {
            class HarnessDevice;
        }
    }
    namespace Routing
    {
        namespace Electrical
        {
            class ConnectorDeviceCollectionImpl;
            /** Represents a collection of @link NXOpen::Routing::Electrical::ConnectorDevice NXOpen::Routing::Electrical::ConnectorDevice@endlink  (CD) objects.   <br> To obtain an instance of this class, refer to @link NXOpen::Routing::RouteManager  NXOpen::Routing::RouteManager @endlink  <br> 
             <br>  Created in NX4.0.2.  <br>  
            */
            class NXOPENCPP_ROUTINGEXPORT  ConnectorDeviceCollection : public NXOpen::TaggedObjectCollection
            {
                private: ConnectorDeviceCollectionImpl * m_connectordevicecollection_impl;
                private: NXOpen::Routing::RouteManager* m_owner;
                /// \cond NX_NO_DOC 
                public: explicit ConnectorDeviceCollection(NXOpen::Routing::RouteManager *owner);


                /// \endcond 
                public: 
                /**Returns the tag of this object.  */
                tag_t Tag() const; 
                public: ~ConnectorDeviceCollection();
                /** Iterator for accessing the contents of the collection. */
                //lint -sem(NXOpen::Routing::Electrical::ConnectorDeviceCollection::iterator::copy,initializer)
                class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::Routing::Electrical::ConnectorDevice *>
                {
                public:
                    /** Default constructor */
                    iterator() : m_context(nullptr), m_current(NULL_TAG)
                    {
                        // coverity[uninit_member]
                    } //lint !e1401 m_state is not initialized
                    /// \cond NX_NO_DOC
                    explicit iterator(NXOpen::Routing::Electrical::ConnectorDeviceCollection *context) : m_context(context), m_current(NULL_TAG)
                    {
                        // coverity[uninit_member]
                    }//lint !e1401 m_state is not initialized
                    /// \endcond
                    /** Copy constructor */
                    iterator(const iterator &other): m_context(nullptr), m_current(NULL_TAG)
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
                    NXOPENCPP_ROUTINGEXPORT  value_type operator * () const;
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
                    NXOPENCPP_ROUTINGEXPORT  void next();
                    NXOpen::Routing::Electrical::ConnectorDeviceCollection *m_context;
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
                /** Creates a @link NXOpen::Routing::Electrical::ConnectorDevice NXOpen::Routing::Electrical::ConnectorDevice@endlink .  @return  
                 <br>  Created in NX4.0.2.  <br>  
                 <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
                public: NXOpen::Routing::Electrical::ConnectorDevice * CreateConnectorDevice
                (
                    NXOpen::Routing::Electrical::ConnectorDevice::ComponentType connectorType /** connector type */ ,
                    const NXString & componentName /** component name */ 
                );
                /** Creates a @link NXOpen::Routing::Electrical::ConnectorDevice NXOpen::Routing::Electrical::ConnectorDevice@endlink .  @return  
                 <br>  Created in NX4.0.2.  <br>  
                 <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
                NXOpen::Routing::Electrical::ConnectorDevice * CreateConnectorDevice
                (
                    NXOpen::Routing::Electrical::ConnectorDevice::ComponentType connectorType /** connector type */ ,
                    const char * componentName /** component name */ 
                );
                /** Finds or Creates a @link NXOpen::Routing::Electrical::ConnectorDevice NXOpen::Routing::Electrical::ConnectorDevice@endlink  for given equipmentName and or 
                                connectorName. Builds @link NXOpen::Routing::Electrical::ElectricalDeviceRelationship NXOpen::Routing::Electrical::ElectricalDeviceRelationship@endlink  between 
                                equipment and connector, if equipmentName and connectorName are not NULL.
                                Adds connector to harnessDevice, if connectorName and harnessDevice are not NULL.  @return  
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
                public: NXOpen::Routing::Electrical::ConnectorDevice * CreateConnectorDevice
                (
                    NXOpen::Routing::Electrical::HarnessDevice * harnessDevice /** can be NULL */,
                    const NXString & equipmentName /** can be NULL if connectorName is not NULL */,
                    const NXString & connectorName /** can be NULL if equipmentName is not NULL */,
                    NXOpen::Routing::Electrical::ConnectorDevice::ComponentType connectorType /** connector type */ 
                );
                /** Finds or Creates a @link NXOpen::Routing::Electrical::ConnectorDevice NXOpen::Routing::Electrical::ConnectorDevice@endlink  for given equipmentName and or 
                                connectorName. Builds @link NXOpen::Routing::Electrical::ElectricalDeviceRelationship NXOpen::Routing::Electrical::ElectricalDeviceRelationship@endlink  between 
                                equipment and connector, if equipmentName and connectorName are not NULL.
                                Adds connector to harnessDevice, if connectorName and harnessDevice are not NULL.  @return  
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
                NXOpen::Routing::Electrical::ConnectorDevice * CreateConnectorDevice
                (
                    NXOpen::Routing::Electrical::HarnessDevice * harnessDevice /** can be NULL */,
                    const char * equipmentName /** can be NULL if connectorName is not NULL */,
                    const char * connectorName /** can be NULL if equipmentName is not NULL */,
                    NXOpen::Routing::Electrical::ConnectorDevice::ComponentType connectorType /** connector type */ 
                );
                /** Get connectors from the work part.  @return  
                 <br>  Created in NX4.0.2.  <br>  
                 <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
                public: std::vector<NXOpen::Routing::Electrical::ConnectorDevice *> GetConnectorSingleDevices
                (
                );
                /** Get equipment from the work part.  @return  
                 <br>  Created in NX4.0.2.  <br>  
                 <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
                public: std::vector<NXOpen::Routing::Electrical::ConnectorDevice *> GetEquipmentSingleDevices
                (
                );
                /** Auto assignment is done using one
                            of the three matching methods, Part Name, Component Name or Attribute. 
                 <br>  Created in NX4.0.2.  <br>  
                 <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
                public: void AutoAssignConnectors
                (
                    const std::vector<NXOpen::Routing::Electrical::ConnectorDevice *> & connectors /** connectors */ 
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

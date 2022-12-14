#ifndef NXOpen_ROUTING_ELECTRICAL_ELECTRICALSTOCKDEVICECOLLECTION_HXX_INCLUDED
#define NXOpen_ROUTING_ELECTRICAL_ELECTRICALSTOCKDEVICECOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_Electrical_ElectricalStockDeviceCollection.ja
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
#include <NXOpen/ErrorList.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/Routing_Electrical_ElectricalStockDevice.hxx>
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
            class ElectricalStockDeviceCollection;
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
            class ElectricalStockDevice;
        }
    }
    class ErrorList;
    namespace Routing
    {
        namespace Electrical
        {
            class ElectricalStockDeviceCollectionImpl;
            /** Represents a collection of @link NXOpen::Routing::Electrical::ElectricalStockDevice NXOpen::Routing::Electrical::ElectricalStockDevice@endlink  (ESD) objects.   <br> To obtain an instance of this class, refer to @link NXOpen::Routing::RouteManager  NXOpen::Routing::RouteManager @endlink  <br> 
             <br>  Created in NX4.0.2.  <br>  
            */
            class NXOPENCPP_ROUTINGEXPORT  ElectricalStockDeviceCollection : public NXOpen::TaggedObjectCollection
            {
                private: ElectricalStockDeviceCollectionImpl * m_electricalstockdevicecollection_impl;
                private: NXOpen::Routing::RouteManager* m_owner;
                /// \cond NX_NO_DOC 
                public: explicit ElectricalStockDeviceCollection(NXOpen::Routing::RouteManager *owner);


                /// \endcond 
                public: 
                /**Returns the tag of this object.  */
                tag_t Tag() const; 
                public: ~ElectricalStockDeviceCollection();
                /** Iterator for accessing the contents of the collection. */
                //lint -sem(NXOpen::Routing::Electrical::ElectricalStockDeviceCollection::iterator::copy,initializer)
                class iterator : public std::iterator<std::forward_iterator_tag, NXOpen::Routing::Electrical::ElectricalStockDevice *>
                {
                public:
                    /** Default constructor */
                    iterator() : m_context(nullptr), m_current(NULL_TAG)
                    {
                        // coverity[uninit_member]
                    } //lint !e1401 m_state is not initialized
                    /// \cond NX_NO_DOC
                    explicit iterator(NXOpen::Routing::Electrical::ElectricalStockDeviceCollection *context) : m_context(context), m_current(NULL_TAG)
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
                    NXOpen::Routing::Electrical::ElectricalStockDeviceCollection *m_context;
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
                /** Automatically routes the selected stock devices. Routing can be done
                                on pin, component or mixed level and it is based on shortest length
                                (See @link NXOpen::Routing::Electrical::ElectricalStockDevice NXOpen::Routing::Electrical::ElectricalStockDevice@endlink  for more details).  @return  
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
                public: int AutoRouteConnections
                (
                    NXOpen::Routing::Electrical::ElectricalStockDevice::RouteLevel routeLevel /** route level */ ,
                    NXOpen::Routing::Electrical::ElectricalStockDevice::AutoRouteSel routeSel /** route sel */ ,
                    const std::vector<NXOpen::Routing::Electrical::ElectricalStockDevice *> & stockDevices /** stock devices */ ,
                    NXOpen::ErrorList ** errorList /** Any errors that occurred during Automatic Routing. */
                );
                /** Assign @link NXOpen::Routing::Stock NXOpen::Routing::Stock@endlink  to input stock devices.
                                The assigned @link NXOpen::Routing::Stock NXOpen::Routing::Stock@endlink  is a bundle stock,
                                and the routine will perform the bundling calculations. This routine
                                should also be called after performing @link NXOpen::Routing::Electrical::ElectricalStockDevice::ManuallyRoute NXOpen::Routing::Electrical::ElectricalStockDevice::ManuallyRoute@endlink . 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
                public: void AssignStock
                (
                    const std::vector<NXOpen::Routing::Electrical::ElectricalStockDevice *> & stockDevices /** stock devices */ ,
                    NXOpen::Routing::Electrical::ElectricalStockDevice::RouteTypes routeType /** route type */ 
                );
                /** Removes @link NXOpen::Routing::Stock NXOpen::Routing::Stock@endlink  from input stock devices.
                                Removes all segments from input wires and updates harnesses associated 
                                to wires, resizes and rebuilds bundle stocks for those harnesses. Deletes
                                the @link NXOpen::Routing::Wire NXOpen::Routing::Wire@endlink .  @return  
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
                public: std::vector<NXOpen::Routing::Electrical::ElectricalStockDevice *> RemoveStock
                (
                    const std::vector<NXOpen::Routing::Electrical::ElectricalStockDevice *> & stockDevices /** stock devices */ 
                );
                /** Automatically routes all of the stock devices in the work part. Routing can be done
                                on pin, component or mixed level and it is based on shortest length
                                (See @link NXOpen::Routing::Electrical::ElectricalStockDevice NXOpen::Routing::Electrical::ElectricalStockDevice@endlink  for more details).  @return  
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
                public: int AutoRouteAll
                (
                    NXOpen::Routing::Electrical::ElectricalStockDevice::RouteLevel routeLevel /** route level */ ,
                    NXOpen::Routing::Electrical::ElectricalStockDevice::AutoRouteSel routeSel /** route sel */ ,
                    NXOpen::ErrorList ** errorList /** Any errors that occurred during Automatic Routing. */
                );
                /** Removes all bundle @link NXOpen::Routing::Stock NXOpen::Routing::Stock@endlink  from input stock devices.
                                Removes all segments from input wires and updates harnesses associated 
                                to wires, resizes and rebuilds bundle stocks for those harnesses. Deletes
                                the @link NXOpen::Routing::Wire NXOpen::Routing::Wire@endlink . Use this when no rebundling is 
                                necessary  @return  
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
                public: std::vector<NXOpen::Routing::Electrical::ElectricalStockDevice *> Unroute
                (
                    const std::vector<NXOpen::Routing::Electrical::ElectricalStockDevice *> & stockDevices /** stock devices */ 
                );
                /** Removes all bundle @link NXOpen::Routing::Stock NXOpen::Routing::Stock@endlink  from all stock devices.
                                Removes all segments from input wires and updates harnesses associated 
                                to wires, resizes and rebuilds bundle stocks for those harnesses. Deletes
                                the @link NXOpen::Routing::Wire NXOpen::Routing::Wire@endlink . Use this when no rebundling is 
                                necessary  @return  
                 <br>  Created in NX6.0.0.  <br>  
                 <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
                public: std::vector<NXOpen::Routing::Electrical::ElectricalStockDevice *> UnrouteAll
                (
                );
                /** Returns the electrical stock devices in part. 
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
                public: std::vector<NXOpen::Routing::Electrical::ElectricalStockDevice *> GetElectricalStockDevicesInPart
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

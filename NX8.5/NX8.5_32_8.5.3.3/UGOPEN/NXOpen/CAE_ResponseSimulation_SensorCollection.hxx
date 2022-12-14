#ifndef NXOpen_CAE_RESPONSESIMULATION_SENSORCOLLECTION_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_SENSORCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_SensorCollection.ja
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
#include <NXOpen/CAE_ResponseSimulation_Sensor.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class SensorCollection;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class Manager;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class Sensor;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class SensorBuilder;
        }
    }
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class SensorCollectionImpl;
            /** Represents a collection of response analysis sensor  <br> To obtain an instance of this class, refer to @link CAE::ResponseSimulation::Manager  CAE::ResponseSimulation::Manager @endlink  <br> 
             <br>  Created in NX5.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  SensorCollection : public TaggedObjectCollection
            {
                private: SensorCollectionImpl * m_sensorcollection_impl;
                private: NXOpen::CAE::ResponseSimulation::Manager* m_owner;
                /// \cond NX_NO_DOC 
                public: explicit SensorCollection(NXOpen::CAE::ResponseSimulation::Manager *owner);


                /// \endcond 
                public: 
                /**Returns the tag of this object.  */
                tag_t Tag() const; 
                public: ~SensorCollection();
                /** Iterator for accessing the contents of the collection. */
                //lint -sem(NXOpen::CAE::ResponseSimulation::SensorCollection::iterator::copy,initializer)
                class iterator
                {
                public:
                    /** Value type associated with iterator*/ 

                    typedef CAE::ResponseSimulation::Sensor * value_type;
                    /** Default constructor */
                    iterator() : m_context(NULL), m_current(NULL_TAG)
                    {
                    } //lint !e1401 m_state is not initialized
                    /// \cond NX_NO_DOC
                    explicit iterator(NXOpen::CAE::ResponseSimulation::SensorCollection *context) : m_context(context), m_current(NULL_TAG)
                    {
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
                    NXOPENCPP_CAEEXPORT  value_type operator * ();
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
                    NXOPENCPP_CAEEXPORT  void next();
                    NXOpen::CAE::ResponseSimulation::SensorCollection *m_context;
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
                /** Creates a sensor buider  @return   
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::SensorBuilder * CreateSensorBuilder
                (
                    NXOpen::CAE::ResponseSimulation::Sensor * rsSensor /** rs sensor */ 
                );
                /** Deletes an sensor 
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: void DeleteSensor
                (
                    NXOpen::CAE::ResponseSimulation::Sensor * rsSensor /** rs sensor */ 
                );
                /** Finds an sensor with specified event name  @return   
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::CAE::ResponseSimulation::Sensor * FindObject
                (
                    const NXString & name /** name */ 
                );
                /** Finds an sensor with specified event name  @return   
                 <br>  Created in NX5.0.0.  <br>  
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                NXOpen::CAE::ResponseSimulation::Sensor * FindObject
                (
                    const char * name /** name */ 
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

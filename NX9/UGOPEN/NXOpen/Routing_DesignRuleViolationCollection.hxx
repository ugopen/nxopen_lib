#ifndef NXOpen_ROUTING_DESIGNRULEVIOLATIONCOLLECTION_HXX_INCLUDED
#define NXOpen_ROUTING_DESIGNRULEVIOLATIONCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Routing_DesignRuleViolationCollection.ja
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
        class DesignRuleViolationCollection;
    }
    namespace Routing
    {
        class RouteManager;
    }
    namespace Routing
    {
        class DesignRuleViolation;
    }
    class NXObject;
    namespace Routing
    {
        class DesignRuleViolationCollectionImpl;
        /** Represents a collection of @link DesignRuleViolation DesignRuleViolation@endlink  objects.  <br> To obtain an instance of this class, refer to @link Routing::RouteManager  Routing::RouteManager @endlink  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_ROUTINGEXPORT  DesignRuleViolationCollection : public TaggedObjectCollection
        {
            /** Design Rule Mode */
            public: enum Mode
            {
                ModeConcurrent/** Executes design rules on all concurrently logged objects.
                                                                Use LogConcurrent method on @link Routing::RouteManager Routing::RouteManager@endlink 
                                                                to concurrently logged objects and GetConcurrent method to get all the
                                                                concurrent objects */,
                ModeInteractive/** Execute design rules during next interactive check */,
                ModeBatch/** Executes design rules in a batch process */
            };

            /** Design Rule reason */
            public: enum Reason
            {
                ReasonUnknown/** unknown */ ,
                ReasonCreatePath/** create path */ ,
                ReasonHealPath/** heal path */ ,
                ReasonAssignCorner/** assign corner */ ,
                ReasonAssignStock/** assign stock */ ,
                ReasonRemoveStock/** remove stock */ ,
                ReasonStockStyle/** stock style */ ,
                ReasonPlacePart/** place part */ ,
                ReasonCreateFab/** create fab */ ,
                ReasonQualifyPart/** qualify part */ ,
                ReasonMovePath/** move path */ ,
                ReasonCopyPath/** copy path */ ,
                ReasonDeletePath/** delete path */ ,
                ReasonSubdivideSeg/** subdivide seg */ ,
                ReasonSimplifyPath/** simplify path */ ,
                ReasonRemovePart/** remove part */ ,
                ReasonMovePart/** move part */ ,
                ReasonEditCharx/** edit charx */ ,
                ReasonInteractive/** interactive */ ,
                ReasonBatch/** batch */ ,
                ReasonOrientStock/** orient stock */ ,
                ReasonUnifyPath/** unify path */ ,
                ReasonTransformPath/** transform path */ ,
                ReasonOffsetPath/** offset path */ ,
                ReasonAutoRoutePin/** auto route pin */ ,
                ReasonManualRoutePin/** manual route pin */ ,
                ReasonAutoRouteComp/** auto route comp */ ,
                ReasonManualRouteComp/** manual route comp */ ,
                ReasonImport/** import */ ,
                ReasonPartialAutoRouteComp/** partial auto route comp */ 
            };

            private: DesignRuleViolationCollectionImpl * m_designruleviolationcollection_impl;
            private: NXOpen::Routing::RouteManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit DesignRuleViolationCollection(NXOpen::Routing::RouteManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~DesignRuleViolationCollection();
            /** Iterator for accessing the contents of the collection. */
            //lint -sem(NXOpen::Routing::DesignRuleViolationCollection::iterator::copy,initializer)
            class iterator
            {
            public:
                /** Value type associated with iterator*/ 

                typedef Routing::DesignRuleViolation * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                { // coverity[uninit_member]
                } //lint !e1401 m_state is not initialized
                /// \cond NX_NO_DOC
                explicit iterator(NXOpen::Routing::DesignRuleViolationCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOPENCPP_ROUTINGEXPORT  value_type operator * ();
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
                NXOpen::Routing::DesignRuleViolationCollection *m_context;
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
            /** Creates a @link Routing::DesignRuleViolation Routing::DesignRuleViolation@endlink  object.
                        Once created, you must add the violation to a rule using @link Routing::DesignRule::AddViolations Routing::DesignRule::AddViolations@endlink . @return  
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: NXOpen::Routing::DesignRuleViolation * CreateDesignRuleViolation
            (
                const NXString & shortDescription /**    <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & longDescription /**    <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const std::vector<NXOpen::NXObject *> & objects /** objects */ 
            );
            /** Creates a @link Routing::DesignRuleViolation Routing::DesignRuleViolation@endlink  object.
                        Once created, you must add the violation to a rule using @link Routing::DesignRule::AddViolations Routing::DesignRule::AddViolations@endlink . @return  
             <br>  Created in NX4.0.2.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            NXOpen::Routing::DesignRuleViolation * CreateDesignRuleViolation
            (
                const char * shortDescription /**    <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const char * longDescription /**    <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const std::vector<NXOpen::NXObject *> & objects /** objects */ 
            );
            /** Executes design rules and returns all the violations of the rule  @return  Violations 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : routing_advanced ("Routing Advanced"), routing_base ("Routing Basic") */
            public: std::vector<NXOpen::Routing::DesignRuleViolation *> ReasonExecuteRule
            (
                NXOpen::Routing::DesignRuleViolationCollection::Mode mode /** Design Rule Mode */,
                NXOpen::Routing::DesignRuleViolationCollection::Reason reason /** Design Rule Reason */,
                const std::vector<NXOpen::NXObject *> & objs /**Objects to check the design rule violation against*/
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

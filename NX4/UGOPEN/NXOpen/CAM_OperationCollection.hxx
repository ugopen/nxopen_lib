#ifndef NXOpen_CAM_OPERATIONCOLLECTION_HXX_INCLUDED
#define NXOpen_CAM_OPERATIONCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_OperationCollection.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class OperationCollection;
    }
    namespace CAM
    {
        class CAMSetup;
    }
    namespace CAM
    {
        class Operation;
    }
    namespace CAM
    {
        class NCGroup;
    }
    namespace CAM
    {
        /** Represents the operation collection  <br> To obtain an instance of this class, refer to @link CAMSetup CAMSetup@endlink  <br> */
        class NXOPENCPPEXPORT OperationCollection : public TaggedObjectCollection
        {
            /** Whether use the default name in creation */
            public: enum UseDefaultName
            {
                UseDefaultNameFalse/** don't user the default name */,
                UseDefaultNameTrue/** use the default name */
            };

            private: NXOpen::CAM::CAMSetup* m_owner;
            public: explicit OperationCollection(NXOpen::CAM::CAMSetup *owner): m_owner(owner)
            {
            }
            public: tag_t Tag() const;
            class iterator
            {
            public:
                typedef CAM::Operation * value_type;
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }
                explicit iterator(NXOpen::CAM::OperationCollection *context) : m_context(context), m_current(NULL_TAG)
                {
                }
                iterator(const iterator &other)
                {
                    copy(other);
                }
                iterator &operator =(const iterator &other)
                {
                    if (&other != this)
                        copy(other);
                    return *this;
                }
                bool operator ==(const iterator &other) const
                {
                    return m_current == other.m_current && m_context == other.m_context;
                }
                bool operator !=(const iterator &other) const
                {
                    return !operator == (other);
                }
                NXOPENCPPEXPORT  value_type operator * ();
                iterator & operator ++()
                {
                    next();
                    return *this;
                }
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
                NXOPENCPPEXPORT  void next();
                NXOpen::CAM::OperationCollection *m_context;
                tag_t m_current;
                unsigned int m_state[8];
            };
            iterator begin();
            iterator end()
            {
                return iterator(this);
            }
            /** Finds the CAM.Operation object with the given identifier as recorded in a journal. @return  the found object  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::Operation * FindObject
            (
                const NXString & sid /** the name of the object   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Create an operation of the specified type and subtype under the parent groups. If the value of 
                    use_default_name is true, default name will be used for the created operation; otherwise, the 
                    specified name will be used. @return  the created operation  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::Operation * Create
            (
                NXOpen::CAM::NCGroup * parent_program_group /** the parent program group */,
                NXOpen::CAM::NCGroup * parent_method_group /** the parent method group */,
                NXOpen::CAM::NCGroup * parent_tool_group /** the parent tool group */,
                NXOpen::CAM::NCGroup * parent_geometry_group /** the parent geometry group */,
                const NXString & type_name /** the name of the template type   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & subtype_name /** the name of the template subtype   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::CAM::OperationCollection::UseDefaultName use_default_name /** use default name or not */,
                const NXString & new_operation_name /** the name of the created operation,
                                                                                               only used when use_default_name == true   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
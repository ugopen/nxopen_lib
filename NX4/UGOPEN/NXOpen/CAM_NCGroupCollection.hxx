#ifndef NXOpen_CAM_NCGROUPCOLLECTION_HXX_INCLUDED
#define NXOpen_CAM_NCGROUPCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_NCGroupCollection.ja
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
        class NCGroupCollection;
    }
    namespace CAM
    {
        class CAMSetup;
    }
    namespace CAM
    {
        class NCGroup;
    }
    namespace CAM
    {
        /** Represents the ncgroup collection  <br> To obtain an instance of this class, refer to @link CAMSetup CAMSetup@endlink  <br> */
        class NXOPENCPPEXPORT NCGroupCollection : public TaggedObjectCollection
        {
            /** Whether use the default name in creation */
            public: enum UseDefaultName
            {
                UseDefaultNameFalse/** don't user the default name */,
                UseDefaultNameTrue/** use the default name */
            };

            private: NXOpen::CAM::CAMSetup* m_owner;
            public: explicit NCGroupCollection(NXOpen::CAM::CAMSetup *owner): m_owner(owner)
            {
            }
            public: tag_t Tag() const;
            class iterator
            {
            public:
                typedef CAM::NCGroup * value_type;
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }
                explicit iterator(NXOpen::CAM::NCGroupCollection *context) : m_context(context), m_current(NULL_TAG)
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
                NXOpen::CAM::NCGroupCollection *m_context;
                tag_t m_current;
                unsigned int m_state[8];
            };
            iterator begin();
            iterator end()
            {
                return iterator(this);
            }
            /** Finds the CAM.NCGroup object with the given identifier as recorded in a journal. @return  the found object  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::NCGroup * FindObject
            (
                const NXString & sid /** the name of the object   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Create a program group of the specified type and subtype under the parent group. If the value of 
                    use_default_name is true, default name will be used for the created program group; otherwise, the 
                    specified name will be used. @return  the created program group  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::NCGroup * CreateProgram
            (
                NXOpen::CAM::NCGroup * parent_group /** the parent group */,
                const NXString & type_name /** the name of the template type   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & subtype_name /** the name of the template subtype   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::CAM::NCGroupCollection::UseDefaultName use_default_name /** use the default name or not */,
                const NXString & new_program_name /** the name of the created program group, 
                                                                                    only used when use_default_name == true.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Create a method group of the specified type and subtype under the parent group. If the value of 
                    use_default_name is true, default name will be used for the created method group; otherwise, the 
                    specified name will be used. @return  the created method group  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::NCGroup * CreateMethod
            (
                NXOpen::CAM::NCGroup * parent_group /** the parent group */,
                const NXString & type_name /** the name of the template type   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & subtype_name /** the name of the template subtype   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::CAM::NCGroupCollection::UseDefaultName use_default_name /** use the default name or not */,
                const NXString & new_method_name /** the name of the created method group,
                                                                                      only used when use_default_name == true    <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Create a tool group of the specified type and subtype under the parent group. If the value of 
                    use_default_name is true, default name will be used for the created tool group; otherwise, the 
                    specified name will be used. @return  the created tool group  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::NCGroup * CreateTool
            (
                NXOpen::CAM::NCGroup * parent_group /** the parent group */,
                const NXString & type_name /** the name of the template type   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & subtype_name /** the name of the template subtype   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::CAM::NCGroupCollection::UseDefaultName use_default_name /** use the default name or not */,
                const NXString & new_tool_name /** the name of the created tool group,
                                                                                      only used when use_default_name == true   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Create a geometry group of the specified type and subtype under the parent group. If the value of 
                    use_default_name is true, default name will be used for the created geometry group; otherwise, the 
                    specified name will be used. @return  the created geometry group  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::NCGroup * CreateGeometry
            (
                NXOpen::CAM::NCGroup * parent_group /** the parent group */,
                const NXString & type_name /** the name of the template type   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & subtype_name /** the name of the template subtype   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::CAM::NCGroupCollection::UseDefaultName use_default_name /** use the default name or not */,
                const NXString & new_geometry_name /** the name of the created geometry group, 
                                                                                      only used when use_default_name == true   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif

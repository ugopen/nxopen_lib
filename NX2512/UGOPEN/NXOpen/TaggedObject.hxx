/*******************************************************************************
               Copyright (c) 2003 Unigraphics Solutions Inc.
                      Unpublished - All Rights Reserved


*******************************************************************************/
#ifndef NXOpen_TAGGEDOBJECT_HXX_INCLUDED
#define NXOpen_TAGGEDOBJECT_HXX_INCLUDED

#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _WIN32
// Disable "inherits by dominance" warning
#pragma warning( disable : 4250 )
#endif

#ifndef TAG_T_DEFINED
#define TAG_T_DEFINED
typedef unsigned int tag_t;
typedef tag_t *tag_p_t;
#endif
#ifndef NULL_TAG
#define NULL_TAG      ((tag_t)0)
#endif

namespace NXOpen
{
    class NXObjectManager;
    class NXObjectTable;

    /** An object that has a Tag. */
    class NXOPENCPPEXPORT TaggedObject
    {
    public:
        TaggedObject();
        /** Returns the tag of this object.  The tag of the object is
        an identifier for the object.  It is used when calling C user
        function routines. */
        tag_t Tag() const;

        virtual ~TaggedObject();
        /// @cond NX_NO_DOC
        virtual void initialize();
        void PrintTestData(const char *name, int line);
        /// @endcond 
    private:
        void SetTag(tag_t tag) { m_tag = tag; }
        tag_t m_tag;
        friend class NXOpen::NXObjectManager;
        friend class NXOpen::NXObjectTable;
    };
}
#undef EXPORTLIBRARY

#endif

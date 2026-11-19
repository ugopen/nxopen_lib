/*******************************************************************************
               Copyright (c) 2004 Unigraphics Solutions Inc.
                      Unpublished - All Rights Reserved


*******************************************************************************/
#ifndef NXOpen_TRANSIENTOBJECT_HXX_INCLUDED
#define NXOpen_TRANSIENTOBJECT_HXX_INCLUDED

#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _WIN32
// Disable "inherits by dominance" warning
#pragma warning( disable : 4250 )
#endif

namespace NXOpen
{
    /** An NX transient object */
    class NXOPENCPPEXPORT TransientObject
    {
        /** Handle of the internal object represented by this object.
        This property should not be used by automation programs. */
        public:  void *GetHandle()
        {
            return m_pointer;
        }

        

        /// @cond NX_NO_DOC
        protected: void *m_pointer;
        protected: explicit TransientObject(void *ptr) : m_pointer(ptr)
        {
        }

        protected: TransientObject() : m_pointer(0)
        {
        }

        public: virtual ~TransientObject()
        {
            m_pointer=NULL;
        }

        void PrintTestData(const char *classname, const char *name, int line);
        /// @endcond

    };
}

#undef EXPORTLIBRARY
#endif //NXOpen_TRANSIENTOBJECT_HXX_INCLUDED

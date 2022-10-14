/*******************************************************************************

          Copyright 2010 Siemens Product Lifecycle Management Software Inc.
                            All Rights Reserved.


*******************************************************************************/
#ifndef NXOpen_NXOBJECTMANAGER_HXX_INCLUDED
#define NXOpen_NXOBJECTMANAGER_HXX_INCLUDED

#include <string>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

namespace NXOpen
{
    class NXObjectBuilder
    {
        public: virtual TaggedObject *buildObject() = 0;
    };

    class TransientObjectBuilder
    {
        public: virtual TransientObject *buildObject(void *ptr) = 0;
    };


    /** Maintains a mapping between Tags and objects. This class can be used
        to help use the C user function routines together with objects 
        in the NXOpen namespace. */
    class NXOPENCPPEXPORT NXObjectManager 
    {
        /** Returns the object corresponding to a tag.  The object that is returned
            by this method is unique for given tag while that tag is alive. The Tag
            property of the object will return the tag with which it was obtained by
            this method.  The C user function routines may return
            tags and Get can be used to obtain the corresponding object. */
        public: static TaggedObject *Get(tag_t tag);
        public: static TaggedObject *Get(tag_t tag, const char *className);

        /// @cond NX_NO_DOC
        /** Set the tag for a singleton class, e.g. Session, ...
            For internal use only. */
        public: static void SetSingletonTag(const char *className, TaggedObject *object);
        public: static TransientObject *Construct(const std::string &className, void *ptr);

        public: static void registerBuilder(const std::string &className, NXObjectBuilder *builder);
        public: static void registerBuilder(const std::string &className, TransientObjectBuilder *builder);
        /// @endcond
    };
}

#undef EXPORTLIBRARY

#endif

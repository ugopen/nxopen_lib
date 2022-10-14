/*******************************************************************************
               Copyright (c) 2004 Unigraphics Solutions Inc.
                      Unpublished - All Rights Reserved


*******************************************************************************/
#ifndef NXOpen_TAGGEDOBJECTCOLLECTION_HXX_INCLUDED
#define NXOpen_TAGGEDOBJECTCOLLECTION_HXX_INCLUDED

#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _WIN32
// Disable "inherits by dominance" warning
#pragma warning( disable : 4250 )
#endif

namespace NXOpen
{
    /** A base class for all NXOpen tagged object collections */
    class NXOPENCPPEXPORT TaggedObjectCollection 
    {
        /// @cond NX_NO_DOC
        protected: void initialize() 
        {
        }//lint !e1762 warning member function could be made const 
        /// @endcond 

        public: virtual ~TaggedObjectCollection()
        {
        }
    };
}
#undef EXPORTLIBRARY

#endif // NXOpen_TAGGEDOBJECTCOLLECTION_HXX_INCLUDED


/*******************************************************************************
               Copyright (c) 2003 Unigraphics Solutions Inc.
                      Unpublished - All Rights Reserved


*******************************************************************************/
#ifndef NXOpen_BASESESSION_HXX_INCLUDED
#define NXOpen_BASESESSION_HXX_INCLUDED

#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

namespace NXOpen
{
    /** A base class for NXOpen session objects */
    class NXOPENCPPEXPORT BaseSession : public TaggedObject
    {
    public:
        /// @cond NX_NO_DOC 
        virtual void initialize();

        void SetTestOutput(const char *new_file);
        void SetTestOutput(const char *new_file, int version);
        void CloseTestOutput();
        void CompareTestOutput(const char *master_file, const char *new_file);
        /// @endcond 
    };

 
}

#undef EXPORTLIBRARY
#endif


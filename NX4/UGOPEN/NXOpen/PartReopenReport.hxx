#ifndef NXOpen_PARTREOPENREPORT_HXX_INCLUDED
#define NXOpen_PARTREOPENREPORT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PartReopenReport.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/PartReopenStatus.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class PartReopenReport;
    class PartReopenStatus;
    /** Contains information about a part and its components after it has been
    reopened. Instances of this class are returned from the following reopen
    methods:
    @link BasePart::Reopen BasePart::Reopen@endlink 
    @link BasePart::ReopenAs BasePart::ReopenAs@endlink 
    @link PartCollection::ReopenAll PartCollection::ReopenAll@endlink 
    */
    class NXOPENCPPEXPORT PartReopenReport : public TransientObject
    {
        public: explicit PartReopenReport(void *ptr);
        /** Free resources associated with the instance. After this method
            is called, it is illegal to use the object.  In .NET, this method
            is automatically called when the object is deleted by the garbage
            collector.  <br> License requirements : None */
        public: virtual ~PartReopenReport();
        /**Returns  the number of parts that reopen was attempted on.  <br> License requirements : None */
        public: int NumberReopenParts
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link NumberReopenParts() NumberReopenParts@endlink instead.
        @deprecated
        */
        public: int GetNumberReopenParts
        (
        ) { return this->NumberReopenParts(); }
        /**Returns  whether or not the display part was reopened by the reopen operation.  <br> License requirements : None */
        public: bool WasDisplayPartReopened
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link WasDisplayPartReopened() WasDisplayPartReopened@endlink instead.
        @deprecated
        */
        public: bool GetWasDisplayPartReopened
        (
        ) { return this->WasDisplayPartReopened(); }
        /**Returns  whether or not the work part failed to reset during the reopen operation.  <br> License requirements : None */
        public: bool CouldNotResetWorkPart
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link CouldNotResetWorkPart() CouldNotResetWorkPart@endlink instead.
        @deprecated
        */
        public: bool GetCouldNotResetWorkPart
        (
        ) { return this->CouldNotResetWorkPart(); }
        /**Returns  a list of objects representing information about the parts that were
            reopened during the reopen operation. See
            @link PartReopenStatus PartReopenStatus@endlink .  <br> License requirements : None */
        public: std::vector<NXOpen::PartReopenStatus *> ReopenStatuses
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link ReopenStatuses() ReopenStatuses@endlink instead.
        @deprecated
        */
        public: std::vector<NXOpen::PartReopenStatus *> GetReopenStatuses
        (
        ) { return this->ReopenStatuses(); }
    };
}
#undef EXPORTLIBRARY
#endif

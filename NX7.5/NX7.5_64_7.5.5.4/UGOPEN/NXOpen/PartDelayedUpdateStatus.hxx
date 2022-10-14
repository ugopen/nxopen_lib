#ifndef NXOpen_PARTDELAYEDUPDATESTATUS_HXX_INCLUDED
#define NXOpen_PARTDELAYEDUPDATESTATUS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PartDelayedUpdateStatus.ja
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
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class PartDelayedUpdateStatus;
    class PartDelayedUpdateStatusImpl;
    /** Represents a list of part names with associated delay status codes. The status
    codes serve to communicate delayed update status for the parts that failed to update during
    Load Interpart Data.
    */
    class NXOPENCPPEXPORT  PartDelayedUpdateStatus : public TransientObject
    {
         /** Logical structure of part delayed update status*/
        public:
        struct  DelayStatusInfo
        {
            public: /**The part is delayed because geometry and expressions are delayed.*/bool SessionDelayed;
            public: /**The part is frozen in this session.*/bool ExplicitDelayed;
            public: /**The part is frozen for all sessions.*/bool FrozenDelayed;
            public: /**The part is delayed because it's not in
                                                        the displayed assembly.*/bool NotDisplayedDelayed;
            public: /**The part is deferred delayed.*/bool DeferredDelayed;
            public: /**The part is internal delayed. */bool InternalDelayed;
            public: /** The part is delayed because assembly constraints are delayed. */bool ConstraintDelayed;
            public: DelayStatusInfo() :
                SessionDelayed(),
                ExplicitDelayed(),
                FrozenDelayed(),
                NotDisplayedDelayed(),
                DeferredDelayed(),
                InternalDelayed(),
                ConstraintDelayed()
            {
            }
            /** Constructor for the DelayStatusInfo struct. */ 
            public: DelayStatusInfo(bool sessionDelayedInitial /**The part is delayed because geometry and expressions are delayed.*/, 
                    bool explicitDelayedInitial /**The part is frozen in this session.*/, 
                    bool frozenDelayedInitial /**The part is frozen for all sessions.*/, 
                    bool notDisplayedDelayedInitial /**The part is delayed because it's not in
                                                                the displayed assembly.*/, 
                    bool deferredDelayedInitial /**The part is deferred delayed.*/, 
                    bool internalDelayedInitial /**The part is internal delayed. */, 
                    bool constraintDelayedInitial /** The part is delayed because assembly constraints are delayed. */) :
                SessionDelayed(sessionDelayedInitial),
                ExplicitDelayed(explicitDelayedInitial),
                FrozenDelayed(frozenDelayedInitial),
                NotDisplayedDelayed(notDisplayedDelayedInitial),
                DeferredDelayed(deferredDelayedInitial),
                InternalDelayed(internalDelayedInitial),
                ConstraintDelayed(constraintDelayedInitial)
            {
            }
        };

        private: PartDelayedUpdateStatusImpl * m_partdelayedupdatestatus_impl;
        public: explicit PartDelayedUpdateStatus(void *ptr);
        /** Free resources associated with the instance. After this method
            is called, it is illegal to use the object.  In .NET, this method
            is automatically called when the object is deleted by the garbage
            collector.  <br> License requirements : None */
        public: virtual ~PartDelayedUpdateStatus();
        /**Returns  the number of parts that could not be updated.  <br> License requirements : None */
        public: int NumberDelayedParts
        (
        );
        /** Returns the name of a particular part that could not be updated.  @return   <br> License requirements : None */
        public: NXString GetPartName
        (
            int i /** Index into list of delayed parts */
        );
        /** Returns the delayed update status for a part that failed to update.  @return Logical structure of part delayed update status  <br> License requirements : None */
        public: NXOpen::PartDelayedUpdateStatus::DelayStatusInfo GetDelayedStatus
        (
            int i /** Index into list of delayed parts */
        );
    }; //lint !e1712 default constructor not defined for class  

}
#undef EXPORTLIBRARY
#endif
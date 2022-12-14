#ifndef NXOpen_CAM_NCGROUP_HXX_INCLUDED
#define NXOpen_CAM_NCGROUP_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_NCGroup.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/CAM_CAMObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class NCGroup;
    }
    namespace CAM
    {
        class CAMObject;
    }
    namespace CAM
    {
        class _NCGroupBuilder;
        /** Represents a NC group  <br> To obtain an instance of this class us @link CAM::NCGroupCollection CAM::NCGroupCollection@endlink  <br> */
        class NXOPENCPPEXPORT NCGroup : public CAM::CAMObject
        {
            private: friend class  _NCGroupBuilder;
            protected: NCGroup();
        };
    }
}
#undef EXPORTLIBRARY
#endif

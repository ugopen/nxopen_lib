#ifndef NXOpen_CAM_INSPECTIONSETUP_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONSETUP_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionSetup.ja
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
#include <NXOpen/CAM_CAMSetup.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class InspectionSetup;
    }
    namespace CAM
    {
        class CAMObject;
    }
    namespace CAM
    {
        class InspectionGroupCollection;
    }
    namespace CAM
    {
        class InspectionOperationCollection;
    }
    namespace CAM
    {
        class _InspectionSetupBuilder;
        /** Inspection setup  <br> Use the @link Part Part@endlink  class to get or create an inspection setup <br> */
        class NXOPENCPPEXPORT InspectionSetup : public CAM::CAMObject
        {
            private: friend class  _InspectionSetupBuilder;
            protected: InspectionSetup();
            /** Postprocess  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void Postprocess
            (
                const std::vector<NXOpen::CAM::CAMObject *> & objects /** array of objects */,
                const NXString & machineType /** machine type   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & outfileName /** output file name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::CAM::CAMSetup::OutputUnits outputUnits /** output file unit */
            );
            /** Cut objects  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void CutObjects
            (
                NXOpen::CAM::CAMSetup::View view /** view */,
                const std::vector<NXOpen::CAM::CAMObject *> & objectsToBeMoved /** array of objects to be moved */
            );
            /** Move objects  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void MoveObjects
            (
                NXOpen::CAM::CAMSetup::View view /** view */,
                const std::vector<NXOpen::CAM::CAMObject *> & objectsToBeMoved /** array of objects to be moved */,
                NXOpen::CAM::CAMObject * destinationObject /** the destination object */,
                NXOpen::CAM::CAMSetup::Paste pastePosition /** paste inside or after the destination object */
            );
            /** Buffer objects to the clipboard and prepare for copy later  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void BufferObjects
            (
                NXOpen::CAM::CAMSetup::View view /** view */,
                const std::vector<NXOpen::CAM::CAMObject *> & objectsToBeBuffered /** array of objects to be buffered */
            );
            /** Copy objects  @return  array of new objects  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: std::vector<NXOpen::CAM::CAMObject *> CopyObjects
            (
                NXOpen::CAM::CAMSetup::View view /** view */,
                const std::vector<NXOpen::CAM::CAMObject *> & objectsToBeMoved /** array of objects to be moved */,
                NXOpen::CAM::CAMObject * destinationObject /** the destination object */,
                NXOpen::CAM::CAMSetup::Paste pastePosition /** paste inside or after the destination object */
            );
            /** Generate tool path  <br> License requirements : inspection_programming ("INSPECTION PROGRAMMING") */
            public: void GenerateToolPath
            (
                const std::vector<NXOpen::CAM::CAMObject *> & objects /** array of objects */
            );


            /** Returns the InspectionGroupCollection instance belonging to this setup */
            public: NXOpen::CAM::InspectionGroupCollection *CmmInspectionGroupCollection();
            /** Returns the InspectionOperationCollection instance belonging to this setup */
            public: NXOpen::CAM::InspectionOperationCollection *CmmInspectionOperationCollection();
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif

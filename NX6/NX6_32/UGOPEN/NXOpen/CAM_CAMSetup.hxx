#ifndef NXOpen_CAM_CAMSETUP_HXX_INCLUDED
#define NXOpen_CAM_CAMSETUP_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_CAMSetup.ja
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
#include <NXOpen/CAM_CAMObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class CAMSetup;
    }
    namespace CAM
    {
        class CAMObject;
    }
    namespace CAM
    {
        class FeatureRecognitionBuilder;
    }
    namespace CAM
    {
        class NCGroupCollection;
    }
    namespace CAM
    {
        class ObjectsFeedsBuilder;
    }
    namespace CAM
    {
        class OperationCollection;
    }
    namespace CAM
    {
        class OperationTransformBuilder;
    }
    namespace CAM
    {
        class PreprocessGeometryBuilder;
    }
    namespace CAM
    {
        class ToolPathDivideBuilder;
    }
    namespace CAM
    {
        class ToolPathSplitBuilder;
    }
    namespace CAM
    {
        class _CAMSetupBuilder;
        /** cam setup  <br> Use the @link Part Part@endlink  class to get or create a setup <br> */
        class NXOPENCPPEXPORT CAMSetup : public CAM::CAMObject
        {
            /** Output units used in output clsf and postprocess.*/
            public: enum OutputUnits
            {
                OutputUnitsInch/** use inch as output unit */,
                OutputUnitsMetric/** use metric as output unit */,
                OutputUnitsPostDefined/** use post defined unit as output unit */
            };

            /** Paste position.*/
            public: enum Paste
            {
                PasteBefore/** paste before */,
                PasteInside/** paste inside */,
                PasteAfter/** paste after */
            };

            /** ONT view.*/
            public: enum View
            {
                ViewProgramOrder/** program order */,
                ViewMachineMethod/** machine method */,
                ViewGeometry/** geometry */,
                ViewMachineTool/** machine tool */
            };

            private: friend class  _CAMSetupBuilder;
            protected: CAMSetup();
            /** Show 2D workpiece  <br> License requirements : cam_base ("CAM BASE") */
            public: void Show2dWorkpiece
            (
                const std::vector<NXOpen::CAM::CAMObject *> & objects /** array of objects */
            );
            /** Show ingoing 2D workpiece  <br> License requirements : cam_base ("CAM BASE") */
            public: void Show2dWorkpieceIn
            (
                const std::vector<NXOpen::CAM::CAMObject *> & objects /** array of objects */
            );
            /** Show outgoing 2D workpiece  <br> License requirements : cam_base ("CAM BASE") */
            public: void Show2dWorkpieceOut
            (
                const std::vector<NXOpen::CAM::CAMObject *> & objects /** array of objects */
            );
            /** Show 3D workpiece  <br> License requirements : cam_base ("CAM BASE") */
            public: void Show3dWorkpiece
            (
                const std::vector<NXOpen::CAM::CAMObject *> & objects /** array of objects */
            );
            /** Generate tool path  <br> License requirements : cam_base ("CAM BASE") */
            public: void GenerateToolPath
            (
                const std::vector<NXOpen::CAM::CAMObject *> & objects /** array of objects */
            );
            /** Replay tool path  <br> License requirements : cam_base ("CAM BASE") */
            public: void ReplayToolPath
            (
                const std::vector<NXOpen::CAM::CAMObject *> & objects /** array of objects */
            );
            /** List tool path  <br> License requirements : cam_base ("CAM BASE") */
            public: void ListToolPath
            (
                const std::vector<NXOpen::CAM::CAMObject *> & objects /** array of objects */
            );
            /** Delete tool path  <br> License requirements : cam_base ("CAM BASE") */
            public: void DeleteToolPath
            (
                const std::vector<NXOpen::CAM::CAMObject *> & objects /** array of objects */
            );
            /** Output CLSF  <br> License requirements : cam_base ("CAM BASE") */
            public: void OutputClsf
            (
                const std::vector<NXOpen::CAM::CAMObject *> & objects /** array of objects */,
                const NXString & clsfFormat /** clsf format   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & outfileName /** output file name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::CAM::CAMSetup::OutputUnits outputUnits /** output file unit */
            );
            /** Postprocess  <br> License requirements : cam_base ("CAM BASE") */
            public: void Postprocess
            (
                const std::vector<NXOpen::CAM::CAMObject *> & objects /** array of objects */,
                const NXString & machineType /** machine type   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & outfileName /** output file name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                NXOpen::CAM::CAMSetup::OutputUnits outputUnits /** output file unit */
            );
            /** Cut objects  <br> License requirements : cam_base ("CAM BASE") */
            public: void CutObjects
            (
                NXOpen::CAM::CAMSetup::View view /** view */,
                const std::vector<NXOpen::CAM::CAMObject *> & objectsToBeMoved /** array of objects to be moved */
            );
            /** Move objects  <br> License requirements : cam_base ("CAM BASE") */
            public: void MoveObjects
            (
                NXOpen::CAM::CAMSetup::View view /** view */,
                const std::vector<NXOpen::CAM::CAMObject *> & objectsToBeMoved /** array of objects to be moved */,
                NXOpen::CAM::CAMObject * destinationObject /** the destination object */,
                NXOpen::CAM::CAMSetup::Paste pastePosition /** paste inside or after the destination object */
            );
            /** Buffer objects to the clipboard and prepare for copy later  <br> License requirements : cam_base ("CAM BASE") */
            public: void BufferObjects
            (
                NXOpen::CAM::CAMSetup::View view /** view */,
                const std::vector<NXOpen::CAM::CAMObject *> & objectsToBeBuffered /** array of objects to be buffered */
            );
            /** Copy objects  @return  array of new objects  <br> License requirements : cam_base ("CAM BASE") */
            public: std::vector<NXOpen::CAM::CAMObject *> CopyObjects
            (
                NXOpen::CAM::CAMSetup::View view /** view */,
                const std::vector<NXOpen::CAM::CAMObject *> & objectsToBeMoved /** array of objects to be moved */,
                NXOpen::CAM::CAMObject * destinationObject /** the destination object */,
                NXOpen::CAM::CAMSetup::Paste pastePosition /** paste inside or after the destination object */
            );
            /** Create Tool Path Divide builder  @return  array of new objects  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::ToolPathDivideBuilder * CreateToolPathDivideBuilder
            (
                const std::vector<NXOpen::CAM::CAMObject *> & tpObjectsToDivide /** array of objects to divide */
            );
            /** Tool Path Divide  <br> License requirements : cam_base ("CAM BASE") */
            public: void DivideToolPaths
            (
                const std::vector<NXOpen::CAM::CAMObject *> & objects /** array of objects */,
                NXOpen::CAM::ToolPathDivideBuilder * builder /** builder containing split parameters */
            );
            /** Lock Tool Path  <br> License requirements : cam_base ("CAM BASE") */
            public: void LockToolPaths
            (
                const std::vector<NXOpen::CAM::CAMObject *> & objects /** array of objects */,
                bool lock /** lock the tool path if true, else unlock the tool path */
            );
            /** Lock Tool Path  @return  tool path lock status  <br> License requirements : cam_base ("CAM BASE") */
            public: bool IsToolPathLocked
            (
                NXOpen::CAM::CAMObject * object /** object whose tool path is checked */
            );
            /** Approve objects  <br> License requirements : cam_base ("CAM BASE") */
            public: void ApproveObjects
            (
                const std::vector<NXOpen::CAM::CAMObject *> & objects /** array of objects */
            );
            /** Create Transform builder. 
                    Note: Commit a Transform Builder will apply a transformation.  @return  created Transform Builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::OperationTransformBuilder * CreateOperationTransformBuilder
            (
                const std::vector<NXOpen::CAM::CAMObject *> & objectsToTransform /** array of objects to transform */
            );
            /** Creates a preprocess geometry builder  @return  preprocess geometry builder created  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::PreprocessGeometryBuilder * CreatePreprocessGeometryBuilder
            (
            );
            /** Creates a CAM.FeatureRecognitionBuilder  @return   <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::FeatureRecognitionBuilder * CreateFeatureRecognitionBuilder
            (
                NXOpen::CAM::CAMObject * param /** not used */
            );
            /** Optimize  <br> License requirements : cam_base ("CAM BASE") */
            public: void Optimize
            (
                const std::vector<NXOpen::CAM::CAMObject *> & objects /** array of objects to optimize */,
                bool consolidateTools /** consolidate tools */,
                bool minimizeToolChanges /** minimize tool changes */,
                bool createOptimizationGroup /** create optimization group */
            );
            /** Set Template status  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetTemplateStatus
            (
                const std::vector<NXOpen::CAM::CAMObject *> & objects /** array of objects to adjust */,
                bool useAsParent /** object can be used as a template or not */,
                bool createIfParentCreated /** create if parent is created */
            );
            /** Gouge Check  <br> License requirements : cam_base ("CAM BASE") */
            public: void GougeCheck
            (
                const std::vector<NXOpen::CAM::CAMObject *> & objects /** array of objects to do gouge checking */,
                bool checkForHolderCollision /** check for tool holder collision */
            );
            /** Set Machining Data  @return  array of errors  <br> License requirements : cam_base ("CAM BASE") */
            public: std::vector<NXOpen::CAM::CAMObject::ErrorItem> SetMachiningData
            (
                const std::vector<NXOpen::CAM::CAMObject *> & objects /** array of objects */
            );
            /** Check for suppressed geometry  @return   <br> License requirements : cam_base ("CAM BASE") */
            public: bool HasSuppressedGeom
            (
                NXOpen::CAM::CAMObject * param /** object to test */
            );
            /** Remove suppressed geometry  <br> License requirements : cam_base ("CAM BASE") */
            public: void RemoveSuppressedGeom
            (
                NXOpen::CAM::CAMObject * param /** object to operate on */
            );
            /** Create Tool Path Split by Holder builder  @return  array of new objects  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::ToolPathSplitBuilder * CreateToolPathSplitBuilder
            (
                const std::vector<NXOpen::CAM::CAMObject *> & tpObjectsToDivide /** array of objects to divide */
            );
            /** Tool Path Split by Holder  <br> License requirements : cam_base ("CAM BASE") */
            public: void SplitToolPaths
            (
                const std::vector<NXOpen::CAM::CAMObject *> & objects /** array of objects */,
                NXOpen::CAM::ToolPathSplitBuilder * builder /** builder containing split parameters */
            );
            /** Create Feeds builder.  @return  created object feed builder  <br> License requirements : cam_base ("CAM BASE") */
            public: NXOpen::CAM::ObjectsFeedsBuilder * CreateFeedsBuilder
            (
                const std::vector<NXOpen::CAM::CAMObject *> & params /** array of objects */
            );


            private: NXOpen::CAM::NCGroupCollection *cAMGroupCollection;
            /** Returns the NCGroupCollection instance belonging to this setup */
            public: NXOpen::CAM::NCGroupCollection *CAMGroupCollection()
            {
                return cAMGroupCollection;
            }
            private: NXOpen::CAM::OperationCollection *cAMOperationCollection;
            /** Returns the OperationCollection instance belonging to this setup */
            public: NXOpen::CAM::OperationCollection *CAMOperationCollection()
            {
                return cAMOperationCollection;
            }
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
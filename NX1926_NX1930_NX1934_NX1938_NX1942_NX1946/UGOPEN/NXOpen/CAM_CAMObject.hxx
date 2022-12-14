#ifndef NXOpen_CAM_CAMOBJECT_HXX_INCLUDED
#define NXOpen_CAM_CAMOBJECT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_CAMObject.ja
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
#include <NXOpen/CAM_Path.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_cam_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAM
    {
        class CAMObject;
    }
    namespace CAM
    {
        class Path;
    }
    class NXObject;
    namespace CAM
    {
        class _CAMObjectBuilder;
        class CAMObjectImpl;
        /** Represents interface for all CAM Object  <br> To create or edit an instance of this class, use @link NXOpen::CAM::ParamBuilder  NXOpen::CAM::ParamBuilder @endlink  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  CAMObject : public NXOpen::NXObject
        {
            /** The unit of feed rate */
            public: enum FeedRateUnit
            {
                FeedRateUnitNone/** no feed rate unit*/,
                FeedRateUnitPerMinute/** use per minute as the feed rate unit*/,
                FeedRateUnitPerRevolution/** use per revolution as the feed rate unit */
            };

            /** 
            Represents the CAM attribute type.
            */
            public: enum Attr
            {
                AttrProjDiffTaxis/** proj diff taxis */  = 1,
                AttrProfileFlipMside/** profile flip mside */ ,
                AttrBndSplineTangent/** bnd spline tangent */ ,
                AttrBlankNormalDiffTaxis/** blank normal diff taxis */ ,
                AttrBndHasSleepObj/** bnd has sleep obj */ ,
                AttrClrnrNotParallelTaxis/** clrnr not parallel taxis */ ,
                AttrBndNotParallelFloor/** bnd not parallel floor */ ,
                AttrFloorNotUpToDate/** floor not up to date */ ,
                AttrSingleProfileWithFirstCut/** single profile with first cut */ ,
                AttrCutterConversionProblem/** cutter conversion problem */ ,
                AttrPredefinedDepthConversionProblem/** predefined depth conversion problem */ ,
                AttrAcceptDrivePosition/** accept drive position */  = 100,
                AttrReparametrization/** reparametrization */  = 110,
                AttrBetweenFromStart/** between from start */  = 120,
                AttrCurveCutRange/** curve cut range */  = 130,
                AttrFixGssmCornerData/** fix gssm corner data */  = 140,
                AttrPlmConversion/** plm conversion */  = 150,
                AttrPlmFeedcomp/** plm feedcomp */ ,
                AttrPlmFillet/** plm fillet */ ,
                AttrPlmSlowdown/** plm slowdown */ ,
                AttrPlmGeometry/** plm geometry */ ,
                AttrWedmPoints/** wedm points */  = 160,
                AttrCavityMillInheritTrimBnds/** cavity mill inherit trim bnds */  = 170,
                AttrRtdObsolete/** rtd obsolete */  = 1000,
                AttrZlevelHolderParamChange/** zlevel holder param change */  = 2000,
                AttrNcmObsoleteSeqControl/** ncm obsolete seq control */  = 2100,
                AttrNcmObsoleteCustomFeed/** ncm obsolete custom feed */ ,
                AttrNcmObsoleteLocalRetract/** ncm obsolete local retract */ ,
                AttrNcmClearTraversalZero/** ncm clear traversal zero */ ,
                AttrNcmObsoleteEngretToClearance/** ncm obsolete engret to clearance */ ,
                AttrGmcInvalidNxVersion/** gmc invalid nx version */  = 2201,
                AttrProbingInvalidNxVersion/** probing invalid nx version */ ,
                AttrInspPathInvalidNxVersion/** insp path invalid nx version */  = 2300,
                AttrCustomDataGougingObsolete/** custom data gouging obsolete */ ,
                AttrCustomDataGougingPartObsolete/** custom data gouging part obsolete */ ,
                AttrCustomDataGougingDriveObsolete/** custom data gouging drive obsolete */ ,
                AttrCustomDataIgnoreLoopsObsolete/** custom data ignore loops obsolete */ ,
                AttrCustomDataIgnoreLoopsRemoved/** custom data ignore loops removed */ ,
                AttrLimitToolRunOn/** limit tool run on */  = 2400,
                AttrScoprNcmChangeLinearNormalToPart/** scopr ncm change linear normal to part */ ,
                AttrPossibleToolAxisProblem/** possible tool axis problem */ 
            };

            /** The status of the object */
            public: enum Status
            {
                StatusComplete/** Object path has been output */,
                StatusRepost/** Object path must be post-processed */,
                StatusRegen/** Object path must be regenerated */,
                StatusApproved/** Object path has been approved as is */ = 4
            };

             /** Error Item */
            public:
            struct ErrorItem
            {
                public: /** objecttag */ NXOpen::CAM::CAMObject * ObjectTag;
                public: /** errorcode */ int ErrorCode;
                public: ErrorItem() :
                    ObjectTag(),
                    ErrorCode()
                {
                }
                /** Constructor for the ErrorItem struct. */ 
                public: ErrorItem(NXOpen::CAM::CAMObject * objectTagInitial /** objecttag */ , 
                        int errorCodeInitial /** errorcode */ ) :
                    ObjectTag(objectTagInitial),
                    ErrorCode(errorCodeInitial)
                {
                }
            };

            /** Validation Types */
            public: enum ValidationType
            {
                ValidationTypeGouge/** gouge */  = 1,
                ValidationTypeToolHolderCollision/** tool holder collision */ ,
                ValidationTypeToolRapidCollision/** tool rapid collision */ ,
                ValidationTypeHasPath/** has path */ 
            };

            /** Validation Result */
            public: enum ValidationResult
            {
                ValidationResultNotApplicable/** not applicable */ ,
                ValidationResultOk/** ok */ ,
                ValidationResultNotChecked/** not checked */ ,
                ValidationResultFail/** fail */ 
            };

            private: CAMObjectImpl * m_camobject_impl;
            private: friend class  _CAMObjectBuilder;
            protected: CAMObject();
            public: ~CAMObject();
            /** Set an integer value to the parameter index for the object. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetIntegerValue
            (
                const NXString & title /** the name of the parameter index  */,
                int value /** the integer value  */
            );
            /** Set an integer value to the parameter index for the object. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            void SetIntegerValue
            (
                const char * title /** the name of the parameter index  */,
                int value /** the integer value  */
            );
            /** Set a real value to the parameter index for the object. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetRealValue
            (
                const NXString & title /** the name of the parameter index */,
                double value /** the real value */
            );
            /** Set a real value to the parameter index for the object. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            void SetRealValue
            (
                const char * title /** the name of the parameter index */,
                double value /** the real value */
            );
            /** Set a string value to the parameter index for the object. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetStringValue
            (
                const NXString & title /** the name of the parameter index  */,
                const NXString & value /** the string value */
            );
            /** Set a string value to the parameter index for the object. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            void SetStringValue
            (
                const char * title /** the name of the parameter index  */,
                const char * value /** the string value */
            );
            /** Set a boolean value to the parameter index for the object. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetBooleanValue
            (
                const NXString & title /** the name of the parameter index */,
                bool value /** the boolean value */
            );
            /** Set a boolean value to the parameter index for the object. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            void SetBooleanValue
            (
                const char * title /** the name of the parameter index */,
                bool value /** the boolean value */
            );
            /** Set a object to the parameter index for the object. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetObject
            (
                const NXString & title /** the name of the parameter index */,
                NXOpen::NXObject * value /** the object */
            );
            /** Set a object to the parameter index for the object. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            void SetObject
            (
                const char * title /** the name of the parameter index */,
                NXOpen::NXObject * value /** the object */
            );
            /** Set feed rate value and unit to the parameter index for the object. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetFeedRate
            (
                const NXString & title /** the name of the parameter index */,
                double value /** the feed rate value */,
                NXOpen::CAM::CAMObject::FeedRateUnit unit /** the feed rate unit */
            );
            /** Set feed rate value and unit to the parameter index for the object. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            void SetFeedRate
            (
                const char * title /** the name of the parameter index */,
                double value /** the feed rate value */,
                NXOpen::CAM::CAMObject::FeedRateUnit unit /** the feed rate unit */
            );
            /** Set feed rate value and side to the parameter index for the object, side is only used in wire edm. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetWireEdmFeedRate
            (
                const NXString & title /** the name of the parameter index */,
                double value /** the feed rate value */,
                int side /** Inside = 0, Outside = 1 */
            );
            /** Set feed rate value and side to the parameter index for the object, side is only used in wire edm. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            void SetWireEdmFeedRate
            (
                const char * title /** the name of the parameter index */,
                double value /** the feed rate value */,
                int side /** Inside = 0, Outside = 1 */
            );
            /** Set feed rate display color to the parameter index for the object. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetFeedRateColor
            (
                const NXString & title /** the name of the paramter index  */,
                int value /** the color number*/
            );
            /** Set feed rate display color to the parameter index for the object. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            void SetFeedRateColor
            (
                const char * title /** the name of the paramter index  */,
                int value /** the color number*/
            );
            /** Set integer array value to the parameter index for the object. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetIntegerArrayValue
            (
                const NXString & title /** the name of the parameter index  */,
                const std::vector<int> & value /** the integer array */
            );
            /** Set integer array value to the parameter index for the object. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            void SetIntegerArrayValue
            (
                const char * title /** the name of the parameter index  */,
                const std::vector<int> & value /** the integer array */
            );
            /** Set real array to the parameter index for the object. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetRealArrayValue
            (
                const NXString & title /** the name of the parameter index */,
                const std::vector<double> & value /** the real array */
            );
            /** Set real array to the parameter index for the object. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            void SetRealArrayValue
            (
                const char * title /** the name of the parameter index */,
                const std::vector<double> & value /** the real array */
            );
            /** Set string array to the parameter index for the object 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetStringArrayValue
            (
                const NXString & title /** the name of the parameter index */,
                std::vector<NXString> & value /** the string array */
            );
            /** Set string array to the parameter index for the object 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            void SetStringArrayValue
            (
                const char * title /** the name of the parameter index */,
                std::vector<NXString> & value /** the string array */
            );
            /** Set object array to the parameter index for the object 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetObjectArrayValue
            (
                const NXString & title /** the name of the parameter index */,
                const std::vector<NXOpen::NXObject *> & value /** the object array */
            );
            /** Set object array to the parameter index for the object 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            void SetObjectArrayValue
            (
                const char * title /** the name of the parameter index */,
                const std::vector<NXOpen::NXObject *> & value /** the object array */
            );
            /** Get the integer value of the parameter index from the object.  @return  the integer value 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: int GetIntegerValue
            (
                const NXString & title /** the name of the parameter index */
            );
            /** Get the integer value of the parameter index from the object.  @return  the integer value 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            int GetIntegerValue
            (
                const char * title /** the name of the parameter index */
            );
            /** Get the real value of the parameter index from the object.  @return  the real value 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: double GetRealValue
            (
                const NXString & title /** the name of the parameter index */
            );
            /** Get the real value of the parameter index from the object.  @return  the real value 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            double GetRealValue
            (
                const char * title /** the name of the parameter index */
            );
            /** Get the boolean value of the parameter index from the object   @return  the boolean value 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: bool GetBooleanValue
            (
                const NXString & title /** the name of the parameter index */
            );
            /** Get the boolean value of the parameter index from the object   @return  the boolean value 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            bool GetBooleanValue
            (
                const char * title /** the name of the parameter index */
            );
            /** Get the string value of the parameter index from the object   @return  the string value 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: NXString GetStringValue
            (
                const NXString & title /** the name of the parameter index */
            );
            /** Get the string value of the parameter index from the object   @return  the string value 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            NXString GetStringValue
            (
                const char * title /** the name of the parameter index */
            );
            /** Get the object value of the parameter index from the object   @return  the object value 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::NXObject * GetObject
            (
                const NXString & title /** the name of the parameter index */
            );
            /** Get the object value of the parameter index from the object   @return  the object value 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            NXOpen::NXObject * GetObject
            (
                const char * title /** the name of the parameter index */
            );
            /** Get the feed rate value and unit of the parameter index from the object  @return  the feed rate unit 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::CAM::CAMObject::FeedRateUnit GetFeedRate
            (
                const NXString & title /** the name of the parameter index */,
                double* value /** the feed rate value */
            );
            /** Get the feed rate value and unit of the parameter index from the object  @return  the feed rate unit 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            NXOpen::CAM::CAMObject::FeedRateUnit GetFeedRate
            (
                const char * title /** the name of the parameter index */,
                double* value /** the feed rate value */
            );
            /** Get the feed rate value and side of the parameter index from the object, side is only used in wire edm.  @return  the feed rate side 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: int GetWireEdmFeedRate
            (
                const NXString & title /** the name of the parameter index */,
                double* value /** the feed rate value */
            );
            /** Get the feed rate value and side of the parameter index from the object, side is only used in wire edm.  @return  the feed rate side 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            int GetWireEdmFeedRate
            (
                const char * title /** the name of the parameter index */,
                double* value /** the feed rate value */
            );
            /** Get the feed rate color of the parameter index from the object.  @return  the color number
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: int GetFeedRateColor
            (
                const NXString & title /** the name of the parameter index */
            );
            /** Get the feed rate color of the parameter index from the object.  @return  the color number
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            int GetFeedRateColor
            (
                const char * title /** the name of the parameter index */
            );
            /** Get the integer array value of the parameter index from the object.  @return  the integer array 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: std::vector<int> GetIntegerArrayValue
            (
                const NXString & title /** the name of the parameter index */
            );
            /** Get the integer array value of the parameter index from the object.  @return  the integer array 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            std::vector<int> GetIntegerArrayValue
            (
                const char * title /** the name of the parameter index */
            );
            /** Get the real array value of the parameter index from the object.  @return  the real array 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: std::vector<double> GetRealArrayValue
            (
                const NXString & title /** the name of the parameter index */
            );
            /** Get the real array value of the parameter index from the object.  @return  the real array 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            std::vector<double> GetRealArrayValue
            (
                const char * title /** the name of the parameter index */
            );
            /** Get the string array value of the parameter index from the object.   @return  the string array 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: std::vector<NXString> GetStringArrayValue
            (
                const NXString & title /** the name of the parameter index */
            );
            /** Get the string array value of the parameter index from the object.   @return  the string array 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            std::vector<NXString> GetStringArrayValue
            (
                const char * title /** the name of the parameter index */
            );
            /** Get the object array value of the parameter index from the object.   @return  the object array 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: std::vector<NXOpen::NXObject *> GetObjectArrayValue
            (
                const NXString & title /** the name of the parameter index */
            );
            /** Get the object array value of the parameter index from the object.   @return  the object array 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            std::vector<NXOpen::NXObject *> GetObjectArrayValue
            (
                const char * title /** the name of the parameter index */
            );
            /** Get the status of the input object.  @return  the object's status 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::CAM::CAMObject::Status GetStatus
            (
            );
            /** Remove a specific 911 attribute from an object.  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void Remove911Attribute
            (
                NXOpen::CAM::CAMObject::Attr attrId /** the attribute Id */
            );
            /** Remove all 911 attributes from an object.  
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void RemoveAll911Attributes
            (
            );
            /** Check if a 911 attribute exists in an object.   @return  true -- 911 attribute exists 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: bool Has911Attribute
            (
                NXOpen::CAM::CAMObject::Attr attrId /** the attribute Id */
            );
            /**  Returns the path. Call @link NXOpen::CAM::CAMObject::SavePath NXOpen::CAM::CAMObject::SavePath@endlink  after 
                     calling @link NXOpen::CAM::CAMObject::GetPath NXOpen::CAM::CAMObject::GetPath@endlink .
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::CAM::Path * GetPath
            (
            );
            /** This must be called to establish proper part status 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SavePath
            (
                NXOpen::CAM::Path * theBuilder /** thebuilder */ 
            );
            /** Tells if the object has a path 
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: bool AskPathExists
            (
            );
            /** Create an empty path for the object
             <br>  Created in NX11.0.2.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::CAM::Path * CreateEmptyPath
            (
            );
            /** Change the dialog customization of the object to use the explorer dialog style
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void ConvertToExplorerDialog
            (
            );

            /// \cond NX_NO_DOC 
            /** Save Master Tool Path for AutoQC  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void SaveMasterPath
            (
                bool inThePart /** save the master path in the same part if true, else in master part*/
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Load Master Tool Path from a specified part  @return  true if master path loading was successful 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: bool LoadMasterPathFromPart
            (
                const NXString & masterPathPartName /** Part file with master path */
            );
            /** Load Master Tool Path from a specified part  @return  true if master path loading was successful 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            bool LoadMasterPathFromPart
            (
                const char * masterPathPartName /** Part file with master path */
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Load Master Tool Path  @return  true if master path loading was successful 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: bool LoadMasterPath
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Has Master Tool Path  @return  true if master path exists 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: bool HasMasterPath
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Delete Master Tool Path 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void DeleteMasterPath
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Delete Tool Path 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: void DeleteToolPath
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Get type name of the given object  @return  the string value 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: NXString GetNameOfType
            (
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Get validity status of CAM Object  @return  the validation result 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") OR insp_programming ("INSPECTION PROGRAMMING") */
            public: NXOpen::CAM::CAMObject::ValidationResult GetValidationResult
            (
                NXOpen::CAM::CAMObject::ValidationType validationType /** validationtype */ 
            );

            /// \endcond 
        };
    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif

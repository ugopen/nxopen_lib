#ifndef NXOpen_CAM_UTILS_HXX_INCLUDED
#define NXOpen_CAM_UTILS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_Utils.ja
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
#include <NXOpen/CAM_CompareParts.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class Utils;
    }
    namespace CAM
    {
        class CAMSession;
    }
    namespace CAM
    {
        class CAMObject;
    }
    namespace CAM
    {
        class CompareParts;
    }
    namespace CAM
    {
        class ParamBuilder;
    }
    class Direction;
    class Part;
    class Plane;
    class Point;
    class TaggedObject;
    namespace CAM
    {
        class UtilsImpl;

        /// \cond NX_NO_DOC 
        /** Represents a class that provides CAM utility functions  <br> To obtain an instance of this class, refer to @link NXOpen::CAM::CAMSession  NXOpen::CAM::CAMSession @endlink  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  Utils
        {
            private: UtilsImpl * m_utils_impl;
            private: NXOpen::CAM::CAMSession* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit Utils(NXOpen::CAM::CAMSession *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~Utils();

            /// \cond NX_NO_DOC 
            /** Get the objects to be compared 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void GetObjectsToCompare
            (
                NXOpen::CAM::CompareParts::ObjectTypes type /** type */ ,
                std::vector<NXOpen::CAM::CAMObject *> & userObjects /** userobjects */ ,
                std::vector<NXOpen::CAM::CAMObject *> & objectsToCompare /** objectstocompare */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Get the builders of the objects to be compared 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void GetObjectsToCompareWithPart
            (
                NXOpen::CAM::CompareParts::ObjectTypes type /** type */ ,
                std::vector<NXOpen::CAM::CAMObject *> & userObjects /** userobjects */ ,
                std::vector<NXOpen::Part *> & userObjectParts /** userobjectparts */ ,
                std::vector<NXOpen::CAM::CAMObject *> & objectsToCompare /** objectstocompare */ ,
                std::vector<NXOpen::Part *> & objectsToCompareParts /** objectstocompareparts */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Set the differences 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDiffs
            (
                NXOpen::CAM::CompareParts::ObjectTypes type /** type */ ,
                NXOpen::CAM::CAMObject * userObject /** userobject */ ,
                NXOpen::CAM::CAMObject * compareObject /** compareobject */ ,
                const std::vector<int> & userObjects /** userobjects */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Get the ci id of the input builder  @return  the ci id of the builder. This will be -1 if it is not relevant 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: int GetCiId
            (
                NXOpen::TaggedObject * builderOfInterest /** builderofinterest */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Check if the ci is a context CI
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsContextCi
            (
                int ci /** ci */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** The Compare Parts object
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::CompareParts * GetComparePartsObject
            (
                const NXString & userPart /** userpart */ ,
                const NXString & fileToCompare /** filetocompare */ 
            );
            /** The Compare Parts object
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::CAM::CompareParts * GetComparePartsObject
            (
                const char * userPart /** userpart */ ,
                const char * fileToCompare /** filetocompare */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Utility to Clone a Smart Point
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point * ClonePoint
            (
                NXOpen::Point * intputPoint /** intputpoint */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Utility to Clone a Smart Vector
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Direction * CloneVector
            (
                NXOpen::Direction * intputVector /** intputvector */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Utility to clone a plane 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Plane * ClonePlane
            (
                NXOpen::Plane * inputPlane /** inputplane */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Get the helper builder of param builder 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void GetHelperBuilders
            (
                NXOpen::CAM::ParamBuilder * paramBuilder /** parambuilder */ ,
                std::vector<NXOpen::TaggedObject *> & helperBuilders /** helperbuilders */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Set intent to use inspection functionality with a manufacturing setup 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void SetInspectionIntent
            (
                bool isInspection /** isinspection */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Get the objects to be merged 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void GetObjectsToMerge
            (
                std::vector<NXOpen::CAM::CAMObject *> & ver0Objects /** ver0objects */ ,
                NXOpen::Part ** ver0Part /** ver0part */ ,
                std::vector<NXOpen::CAM::CAMObject *> & ver1Objects /** ver1objects */ ,
                NXOpen::Part ** ver1Part /** ver1part */ ,
                std::vector<NXOpen::CAM::CAMObject *> & ver2Objects /** ver2objects */ ,
                NXOpen::Part ** ver2Part /** ver2part */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Get the objects to be merged 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void GetBuildersToValidate
            (
                std::vector<NXOpen::CAM::ParamBuilder *> & metricBuilders /** metricbuilders */ ,
                std::vector<NXOpen::CAM::ParamBuilder *> & englishBuilders /** englishbuilders */ 
            );

            /// \endcond 

            /// \cond NX_NO_DOC 
            /** Set mismatching doubles 
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMismatchingDoubles
            (
                const std::vector<int> & ciIds /** ciids */ 
            );

            /// \endcond 
        }; //lint !e1712 default constructor not defined for class  


        /// \endcond 
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

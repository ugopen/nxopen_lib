#ifndef NXOpen_REPORT_IMAGESGROUPITEM_HXX_INCLUDED
#define NXOpen_REPORT_IMAGESGROUPITEM_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Report_ImagesGroupItem.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Report_ImagesGroupItem.hxx>
#include <NXOpen/Report_Report.hxx>
#include <NXOpen/Report_ReportImage.hxx>
#include <NXOpen/libnxopencpp_report_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Report
    {
        class ImagesGroupItem;
    }
    class NXObject;
    namespace Report
    {
        class ReportImage;
    }
    namespace Report
    {
        class _ImagesGroupItemBuilder;
        class ImagesGroupItemImpl;
        /** Represents a images group item.   <br> Not support KF.  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_REPORTEXPORT  ImagesGroupItem : public NXOpen::NXObject
        {
            private: ImagesGroupItemImpl * m_imagesgroupitem_impl;
            private: friend class  _ImagesGroupItemBuilder;
            protected: ImagesGroupItem();
            public: ~ImagesGroupItem();
            /** Creates an image in images group.  @return   
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Report::ReportImage * CreateImage
            (
                const NXString & imageFile /** imagefile */ ,
                const NXString & displayName /** displayname */ 
            );
            /** Creates an image in images group.  @return   
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::Report::ReportImage * CreateImage
            (
                const char * imageFile /** imagefile */ ,
                const char * displayName /** displayname */ 
            );
            /** Copy a @link NXOpen::Report::ReportImage NXOpen::Report::ReportImage@endlink  to the this class.  @return  copy of the input image 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Report::ReportImage * CopyImage
            (
                NXOpen::Report::ReportImage * pReportImage /** input image */
            );
            /** Gets all images in images group. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void GetImages
            (
                std::vector<NXOpen::Report::ReportImage *> & pReportImages /** preportimages */ 
            );
            /** Moves the images to the new position. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void MoveImages
            (
                const std::vector<NXOpen::Report::ReportImage *> & pReportImages /** preportimages */ ,
                NXOpen::Report::Report::MoveItemLocation newLocation /** newlocation */ ,
                NXOpen::Report::ReportImage * pReferencedImage /** preferencedimage */ 
            );
            /** Deletes all images in class. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void DeleteImages
            (
            );
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
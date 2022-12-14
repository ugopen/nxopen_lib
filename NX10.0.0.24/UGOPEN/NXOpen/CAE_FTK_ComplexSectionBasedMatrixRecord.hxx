#ifndef NXOpen_CAE_FTK_COMPLEXSECTIONBASEDMATRIXRECORD_HXX_INCLUDED
#define NXOpen_CAE_FTK_COMPLEXSECTIONBASEDMATRIXRECORD_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_FTK_ComplexSectionBasedMatrixRecord.ja
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
#include <NXOpen/CAE_FTK_ComplexSectionBasedMatrixRecord.hxx>
#include <NXOpen/CAE_FTK_SectionBasedMatrixRecord.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        namespace FTK
        {
            class ComplexSectionBasedMatrixRecord;
        }
    }
    namespace CAE
    {
        namespace FTK
        {
            class SectionBasedMatrixRecord;
        }
    }
    namespace CAE
    {
        namespace FTK
        {
            class _ComplexSectionBasedMatrixRecordBuilder;
            class ComplexSectionBasedMatrixRecordImpl;
            /** Represents a section based matrix record which has complex data values.  <br> Not support KF.  <br> 
             <br>  Created in NX10.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  ComplexSectionBasedMatrixRecord : public NXOpen::CAE::FTK::SectionBasedMatrixRecord
            {
                private: ComplexSectionBasedMatrixRecordImpl * m_complexsectionbasedmatrixrecord_impl;
                private: friend class  _ComplexSectionBasedMatrixRecordBuilder;
                protected: ComplexSectionBasedMatrixRecord();
                public: ~ComplexSectionBasedMatrixRecord();
                /** Adds the complex data values for each section. 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void AddSectionData
                (
                    const std::vector<double> & xCoordinatePoints /** X-Coordinate data */,
                    const std::vector<double> & yCoordinateReal /** Real part of Y-Coordinate data */,
                    const std::vector<double> & yCoordinateImag /** Imaginary part of Y-Coordinate data */,
                    double zCoordinatePoint /** Z-Coordinate data */
                );
                /** Gets the complex data values from specific section. 
                 <br>  Created in NX10.0.0.  <br>  
                 <br> License requirements : nx_ftk ("NX Advanced Graphing") */
                public: void GetSectionData
                (
                    int sectionIndex /** Section index */,
                    std::vector<double> & xCoordinatePoints /** X-Coordinate data */,
                    std::vector<double> & yCoordinateReal /** Real part of Y-Coordinate data */,
                    std::vector<double> & yCoordinateImag /** Imaginary part of Y-Coordinate data */,
                    double* zCoordinatePoints /** Z-Coordinate data */
                );
            };
        }
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

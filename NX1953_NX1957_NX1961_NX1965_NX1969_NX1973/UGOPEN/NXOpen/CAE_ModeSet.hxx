#ifndef NXOpen_CAE_MODESET_HXX_INCLUDED
#define NXOpen_CAE_MODESET_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ModeSet.ja
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
#include <NXOpen/CAE_AlternateFemRepresentationSource.hxx>
#include <NXOpen/CAE_IPostScenarioDataSource.hxx>
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
        class ModeSet;
    }
    namespace CAE
    {
        class AlternateFemRepresentationSource;
    }
    namespace CAE
    {
        class IPostScenarioDataSource;
    }
    namespace CAE
    {
        class _ModeSetBuilder;
        class ModeSetImpl;
        /**  @brief  This is the class representing a Mode set.  

           <br> Not support KF.  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ModeSet : public NXOpen::CAE::AlternateFemRepresentationSource, public virtual NXOpen::CAE::IPostScenarioDataSource
        {
             /** Struct for output parameters of get_mode_by_index */
            public:
            struct ModeInfo
            {
                public: /** the label of the mode within the mode set */int Label;
                public: /** the exported index of the mode */int ExportedIndex;
                public: /** the status of the mode */bool Status;
                public: /** the undamped frequency of the mode */double UndampedFrequency;
                public: /** the damping ratio of the mode */double DampingRatio;
                public: /** the real part of the modal mass of the mode */double ModalMassReal;
                public: /** the imaginary part of the modal mass of the mode */double ModalMassImg;
                public: /** the diagonal structural damping of the mode in percentage */double StructuralDamping;
                public: /** structuraldampingfactor */ double StructuralDampingFactor;
                public: /** the structural damping of the mode exists or not*/bool HasStructuralDamping;
                public: /** the diagonal viscous damping of the mode in percentage */double ViscousDamping;
                public: /** the viscous damping of the mode */double ViscousDampingFactor;
                public: /** the viscous damping of the mode exists or not */bool HasViscousDamping;
                public: /** the data source name of the mode */NXString DataSourceName;
                public: /** the annotation of the mode */NXString Annotation;
                public: ModeInfo() :
                    Label(),
                    ExportedIndex(),
                    Status(),
                    UndampedFrequency(),
                    DampingRatio(),
                    ModalMassReal(),
                    ModalMassImg(),
                    StructuralDamping(),
                    StructuralDampingFactor(),
                    HasStructuralDamping(),
                    ViscousDamping(),
                    ViscousDampingFactor(),
                    HasViscousDamping(),
                    DataSourceName(),
                    Annotation()
                {
                }
                /** Constructor for the ModeInfo struct. */ 
                public: ModeInfo(int labelInitial /** the label of the mode within the mode set */, 
                        int exportedIndexInitial /** the exported index of the mode */, 
                        bool statusInitial /** the status of the mode */, 
                        double undampedFrequencyInitial /** the undamped frequency of the mode */, 
                        double dampingRatioInitial /** the damping ratio of the mode */, 
                        double modalMassRealInitial /** the real part of the modal mass of the mode */, 
                        double modalMassImgInitial /** the imaginary part of the modal mass of the mode */, 
                        double structuralDampingInitial /** the diagonal structural damping of the mode in percentage */, 
                        double structuralDampingFactorInitial /** structuraldampingfactor */ , 
                        bool hasStructuralDampingInitial /** the structural damping of the mode exists or not*/, 
                        double viscousDampingInitial /** the diagonal viscous damping of the mode in percentage */, 
                        double viscousDampingFactorInitial /** the viscous damping of the mode */, 
                        bool hasViscousDampingInitial /** the viscous damping of the mode exists or not */, 
                        const NXString &dataSourceNameInitial /** the data source name of the mode */, 
                        const NXString &annotationInitial /** the annotation of the mode */) :
                    Label(labelInitial),
                    ExportedIndex(exportedIndexInitial),
                    Status(statusInitial),
                    UndampedFrequency(undampedFrequencyInitial),
                    DampingRatio(dampingRatioInitial),
                    ModalMassReal(modalMassRealInitial),
                    ModalMassImg(modalMassImgInitial),
                    StructuralDamping(structuralDampingInitial),
                    StructuralDampingFactor(structuralDampingFactorInitial),
                    HasStructuralDamping(hasStructuralDampingInitial),
                    ViscousDamping(viscousDampingInitial),
                    ViscousDampingFactor(viscousDampingFactorInitial),
                    HasViscousDamping(hasViscousDampingInitial),
                    DataSourceName(dataSourceNameInitial),
                    Annotation(annotationInitial)
                {
                }
            };

            private: ModeSetImpl * m_modeset_impl;
            private: friend class  _ModeSetBuilder;
            protected: ModeSet();
            public: ~ModeSet();
            /** Get the number of modes.  @return  The number of modes. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: int GetNumberOfModes
            (
            );
            /** Get the data of a mode. 
             <br>  @deprecated Deprecated in NX1872.0.0.  Use @link GetModeInfoByIndex GetModeInfoByIndex@endlink  instead. <br>  

             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NX_DEPRECATED("Deprecated in NX1872.0.0.  Use GetModeInfoByIndex instead.") void GetModeByIndex
            (
                int index /** the index of the mode */,
                int* label /** the label of the mode */,
                bool* status /** the status of the mode */,
                double* undampedFrequency /** the undamped frequency of the mode */,
                double* dampingRatio /** the damping ratio of the mode */,
                double* modalMassReal /** the real part of the modal mass of the mode */,
                double* modalMassImg /** the imaginary part of the modal mass of the mode */,
                NXString* annotation /** the annotation of the mode */
            );
            /** Get the data of a mode.  @return  the output structure containing all the mode info 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::ModeSet::ModeInfo GetModeInfoByIndex
            (
                int index /** the index of the mode within the mode set */
            );
            /** Modify the status of a mode in the main data source.
                     This method should be followed by a subsequent call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
                     If your application sets multiple information to the mode set, then @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink 
                     should be called only once after setting all the new information of the mode set. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetModeStatus
            (
                int label /** the label of the mode */,
                bool status /** the status of the mode */
            );
            /** Modify the status of a mode in the specified data source. 
                     This method should be followed by a subsequent call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
                     If your application sets multiple information to the mode set, then @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink 
                     should be called only once after setting all the new information of the mode set. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetModeStatus
            (
                const NXString & dataSourceName /** the data source name of the mode */,
                int label /** the label of the mode */,
                bool status /** the status of the mode */
            );
            /** Modify the status of a mode in the specified data source. 
                     This method should be followed by a subsequent call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
                     If your application sets multiple information to the mode set, then @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink 
                     should be called only once after setting all the new information of the mode set. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            void SetModeStatus
            (
                const char * dataSourceName /** the data source name of the mode */,
                int label /** the label of the mode */,
                bool status /** the status of the mode */
            );
            /** Modify the undamped frequency of a mode in the main data source. 
                     This method should be followed by a subsequent call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
                     If your application sets multiple information to the mode set, then @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink 
                     should be called only once after setting all the new information of the mode set. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetModeUndampedFrequency
            (
                int label /** the label of the mode */,
                double undampedFrequency /** the undamped frequency of the mode */
            );
            /** Modify the undamped frequency of a mode in the specified data source. 
                     This method should be followed by a subsequent call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
                     If your application sets multiple information to the mode set, then @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink 
                     should be called only once after setting all the new information of the mode set. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetModeUndampedFrequency
            (
                const NXString & dataSourceName /** the data source name of the mode */,
                int label /** the label of the mode */,
                double undampedFrequency /** the undamped frequency of the mode */
            );
            /** Modify the undamped frequency of a mode in the specified data source. 
                     This method should be followed by a subsequent call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
                     If your application sets multiple information to the mode set, then @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink 
                     should be called only once after setting all the new information of the mode set. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            void SetModeUndampedFrequency
            (
                const char * dataSourceName /** the data source name of the mode */,
                int label /** the label of the mode */,
                double undampedFrequency /** the undamped frequency of the mode */
            );
            /** Modify the damping ratio of a mode in the main data source. 
                     This method should be followed by a subsequent call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
                     If your application sets multiple information to the mode set, then @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink 
                     should be called only once after setting all the new information of the mode set. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetModeDampingRatio
            (
                int label /** the label of the mode */,
                double dampingRatio /** the damping ratio of the mode */
            );
            /** Modify the damping ratio of a mode in the specified data source. 
                     This method should be followed by a subsequent call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
                     If your application sets multiple information to the mode set, then @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink 
                     should be called only once after setting all the new information of the mode set. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetModeDampingRatio
            (
                const NXString & dataSourceName /** the data source name of the mode */,
                int label /** the label of the mode */,
                double dampingRatio /** the damping ratio of the mode */
            );
            /** Modify the damping ratio of a mode in the specified data source. 
                     This method should be followed by a subsequent call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
                     If your application sets multiple information to the mode set, then @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink 
                     should be called only once after setting all the new information of the mode set. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            void SetModeDampingRatio
            (
                const char * dataSourceName /** the data source name of the mode */,
                int label /** the label of the mode */,
                double dampingRatio /** the damping ratio of the mode */
            );
            /** Modify the modal mass of a mode in the main data source. 
                     This method should be followed by a subsequent call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
                     If your application sets multiple information to the mode set, then @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink 
                     should be called only once after setting all the new information of the mode set. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetModeModalMass
            (
                int label /** the label of the mode */,
                double modalMassReal /** the real part of the modal mass of the mode */,
                double modalMassImg /** the imaginary part of the modal mass of the mode */
            );
            /** Modify the modal mass of a mode. 
                     This method should be followed by a subsequent call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
                     If your application sets multiple information to the mode set, then @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink 
                     should be called only once after setting all the new information of the mode set. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetModeModalMass
            (
                const NXString & dataSourceName /** the data source name of the mode */,
                int label /** the label of the mode */,
                double modalMassReal /** the real part of the modal mass of the mode */,
                double modalMassImg /** the imaginary part of the modal mass of the mode */
            );
            /** Modify the modal mass of a mode. 
                     This method should be followed by a subsequent call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
                     If your application sets multiple information to the mode set, then @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink 
                     should be called only once after setting all the new information of the mode set. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            void SetModeModalMass
            (
                const char * dataSourceName /** the data source name of the mode */,
                int label /** the label of the mode */,
                double modalMassReal /** the real part of the modal mass of the mode */,
                double modalMassImg /** the imaginary part of the modal mass of the mode */
            );
            /** Modify the annotation of a mode in the main data source. 
                     This method should be followed by a subsequent call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
                     If your application sets multiple information to the mode set, then @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink 
                     should be called only once after setting all the new information of the mode set. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetModeAnnotation
            (
                int label /** the label of the mode */,
                const NXString & annotation /** the annotation of the mode */
            );
            /** Modify the annotation of a mode in the main data source. 
                     This method should be followed by a subsequent call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
                     If your application sets multiple information to the mode set, then @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink 
                     should be called only once after setting all the new information of the mode set. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            void SetModeAnnotation
            (
                int label /** the label of the mode */,
                const char * annotation /** the annotation of the mode */
            );
            /** Modify the annotation of a mode in the specified data source. 
                     This method should be followed by a subsequent call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
                     If your application sets multiple information to the mode set, then @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink 
                     should be called only once after setting all the new information of the mode set. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetModeAnnotation
            (
                const NXString & dataSourceName /** the data source name of the mode */,
                int label /** the label of the mode */,
                const NXString & annotation /** the annotation of the mode */
            );
            /** Modify the annotation of a mode in the specified data source. 
                     This method should be followed by a subsequent call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
                     If your application sets multiple information to the mode set, then @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink 
                     should be called only once after setting all the new information of the mode set. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            void SetModeAnnotation
            (
                const char * dataSourceName /** the data source name of the mode */,
                int label /** the label of the mode */,
                const char * annotation /** the annotation of the mode */
            );
            /** Modify the structural damping factor of a mode in the main data source.
                     This method should be followed by a subsequent call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
                     If your application sets multiple information to the mode set, then @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink 
                     should be called only once after setting all the new information of the mode set. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetModeStructuralDampingFactor
            (
                int label /** the label of the mode */,
                double structuralDampingFactor /** the structural damping factor */
            );
            /** Modify the structural damping factor of a mode in a companion data source. 
                     This method should be followed by a subsequent call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
                     If your application sets multiple information to the mode set, then @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink 
                     should be called only once after setting all the new information of the mode set. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetModeStructuralDampingFactor
            (
                const NXString & dataSourceName /** the data source name of the mode */,
                int label /** the label of the mode */,
                double structuralDampingFactor /** the structural damping factor */
            );
            /** Modify the structural damping factor of a mode in a companion data source. 
                     This method should be followed by a subsequent call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
                     If your application sets multiple information to the mode set, then @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink 
                     should be called only once after setting all the new information of the mode set. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            void SetModeStructuralDampingFactor
            (
                const char * dataSourceName /** the data source name of the mode */,
                int label /** the label of the mode */,
                double structuralDampingFactor /** the structural damping factor */
            );
            /** Modify the viscous damping factor of a mode in the main data source.
                     This method should be followed by a subsequent call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
                     If your application sets multiple information to the mode set, then @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink 
                     should be called only once after setting all the new information of the mode set. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetModeViscousDampingFactor
            (
                int label /** the label of the mode */,
                double viscousDampingFactor /** the viscous damping factor */
            );
            /** Modify the viscous damping factor of a mode in a companion data source. 
                     This method should be followed by a subsequent call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
                     If your application sets multiple information to the mode set, then @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink 
                     should be called only once after setting all the new information of the mode set. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: void SetModeViscousDampingFactor
            (
                const NXString & dataSourceName /** the data source name of the mode */,
                int label /** the label of the mode */,
                double viscousDampingFactor /** the viscous damping factor */
            );
            /** Modify the viscous damping factor of a mode in a companion data source. 
                     This method should be followed by a subsequent call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
                     If your application sets multiple information to the mode set, then @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink 
                     should be called only once after setting all the new information of the mode set. 
             <br>  Created in NX1926.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            void SetModeViscousDampingFactor
            (
                const char * dataSourceName /** the data source name of the mode */,
                int label /** the label of the mode */,
                double viscousDampingFactor /** the viscous damping factor */
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
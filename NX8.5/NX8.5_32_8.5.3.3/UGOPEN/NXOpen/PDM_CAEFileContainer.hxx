#ifndef NXOpen_PDM_CAEFILECONTAINER_HXX_INCLUDED
#define NXOpen_PDM_CAEFILECONTAINER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PDM_CAEFileContainer.ja
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
#include <NXOpen/PDM_CAEFileContainer.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_pdm_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PDM
    {
        class CAEFileContainer;
    }
    namespace PDM
    {
        class CAEFileContainerImpl;
        /**  @brief  This class is a File Container class for uploading JT files created by NX CAE Post Processing to Teamcenter. 
        	Users can add the JT file names and their corresponding dataset names to this container class.
        	Once all the JT file names are added, this class can be used to upload the JT files to Teamcenter.
        	The class can be used to upload only to a a single part at a time.
        	 

           <br> Use @link PDM::PdmSession PDM::PdmSession@endlink  to get the instance of this class.  <br> 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_PDMEXPORT  CAEFileContainer : public TransientObject
        {
            private: CAEFileContainerImpl * m_caefilecontainer_impl;
            /// \cond NX_NO_DOC 
            public: explicit CAEFileContainer(void *ptr);
            /// \endcond 
            /** Free resources associated with the instance. After this method
                    is called, it is illegal to use the object.  In .NET, this method
                    is automatically called when the object is deleted by the garbage
                    collector. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: virtual ~CAEFileContainer();
            /** Get the part tag of the owning part of the class @link PDM::CAEFileContainer PDM::CAEFileContainer@endlink . @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXString GetOwningPart
            (
            );
            /** Sets the part tag of the owning part of the class @link PDM::CAEFileContainer PDM::CAEFileContainer@endlink .
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetOwningPart
            (
                const NXString & partspec /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Sets the part tag of the owning part of the class @link PDM::CAEFileContainer PDM::CAEFileContainer@endlink .
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetOwningPart
            (
                const char * partspec /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**  Add a file to the list of files in the file container class @link PDM::CAEFileContainer PDM::CAEFileContainer@endlink .
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void AddFile
            (
                const NXString & datasetname /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & filename /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**  Add a file to the list of files in the file container class @link PDM::CAEFileContainer PDM::CAEFileContainer@endlink .
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void AddFile
            (
                const char * datasetname /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const char * filename /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**  Delete a file from the list of files in the file container class @link PDM::CAEFileContainer PDM::CAEFileContainer@endlink .
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void DeleteFile
            (
                const NXString & datasetname /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const NXString & filename /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**  Delete a file from the list of files in the file container class @link PDM::CAEFileContainer PDM::CAEFileContainer@endlink .
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void DeleteFile
            (
                const char * datasetname /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                const char * filename /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**  Upload CAE files to Teamcenter, independent of a standard file->save.  
                    Upload all the files in the file container class @link PDM::CAEFileContainer PDM::CAEFileContainer@endlink  using this function.
            	    The JT files should be present in the temporary directory of the system prior to calling this function.
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void DoUpload
            (
            );
        }; //lint !e1712 default constructor not defined for class  

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

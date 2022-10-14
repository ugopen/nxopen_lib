#ifndef NXOpen_IFCIMPORTER_HXX_INCLUDED
#define NXOpen_IFCIMPORTER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     IfcImporter.ja
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
#include <NXOpen/BaseImporter.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class IfcImporter;
    class BaseImporter;
    class _IfcImporterBuilder;
    class IfcImporterImpl;
    /**
        Represents a @link NXOpen::IfcImporter NXOpen::IfcImporter@endlink  to be used when importing IFC Data
        This class is created using @link NXOpen::DexManager NXOpen::DexManager@endlink .
        NULL object will be returned from Commit()  <br> To create a new instance of this class, use @link NXOpen::DexManager::CreateIfcImporter  NXOpen::DexManager::CreateIfcImporter @endlink  <br> 
    Default values.
    <table border="1"> 
     
    <tr><th> 
    Property</th>  <th> 
    Value</th> </tr>
    <tr><td> 
     
    BuildingControls </td> <td> 
     
    1 </td> </tr> 

    <tr><td> 
     
    Deltax </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    Deltay </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    Deltaz </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    Electrical </td> <td> 
     
    1 </td> </tr> 

    <tr><td> 
     
    Hvac </td> <td> 
     
    1 </td> </tr> 

    <tr><td> 
     
    ImportFacetsAsXTBrepOrConvergent </td> <td> 
     
    XTBrep </td> </tr> 

    <tr><td> 
     
    Messages </td> <td> 
     
    None </td> </tr> 

    <tr><td> 
     
    MoveModelData </td> <td> 
     
    To000 </td> </tr> 

    <tr><td> 
     
    Optimize </td> <td> 
     
    1 </td> </tr> 

    <tr><td> 
     
    PlumbingFireProtection </td> <td> 
     
    1 </td> </tr> 

    <tr><td> 
     
    ProductExtension </td> <td> 
     
    1 </td> </tr> 

    <tr><td> 
     
    RotateAroundZByDegrees </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    SharedBldgServicesElements </td> <td> 
     
    1 </td> </tr> 

    <tr><td> 
     
    SharedBuildingElements </td> <td> 
     
    1 </td> </tr> 

    <tr><td> 
     
    SharedComponentElements </td> <td> 
     
    1 </td> </tr> 

    <tr><td> 
     
    SharedFacilitiesElements </td> <td> 
     
    1 </td> </tr> 

    <tr><td> 
     
    ShowInformationWindowFlag </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    StructuralAnalysis </td> <td> 
     
    1 </td> </tr> 

    <tr><td> 
     
    StructuralElements </td> <td> 
     
    1 </td> </tr> 

    </table>  

     <br>  Created in NX1872.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  IfcImporter : public NXOpen::BaseImporter
    {
        /** Convert facets to xtbrep or convergent */
        public: enum ImportFacetsAsXTBrepOrConvergentEnum
        {
            ImportFacetsAsXTBrepOrConvergentEnumXTBrep/** xtbrep */ ,
            ImportFacetsAsXTBrepOrConvergentEnumConvergentBodies/** convergent bodies */ 
        };

        /** Messages output when opening the file. */
        public: enum MoveDataEnum
        {
            MoveDataEnumByDeltamm/** by deltamm */ ,
            MoveDataEnumTo000/** to000 */ 
        };

        /** Messages output when opening the file. */
        public: enum MessageEnum
        {
            MessageEnumNone/** none */ ,
            MessageEnumInformational/** informational */ ,
            MessageEnumWarning/** warning */ ,
            MessageEnumError/** error */ ,
            MessageEnumDebug/** debug */ ,
            MessageEnumAll/** all */ 
        };

        private: IfcImporterImpl * m_ifcimporter_impl;
        private: friend class  _IfcImporterBuilder;
        protected: IfcImporter();
        public: ~IfcImporter();
        /**Returns  the functions get and set the option to convert facets to xtbrep or convergent 
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::IfcImporter::ImportFacetsAsXTBrepOrConvergentEnum ImportFacetsAsXTBrepOrConvergent
        (
        );
        /**Sets  the functions get and set the option to convert facets to xtbrep or convergent 
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: void SetImportFacetsAsXTBrepOrConvergent
        (
            NXOpen::IfcImporter::ImportFacetsAsXTBrepOrConvergentEnum importFacetsAsXTBrepOrConvergent /** importfacetsasxtbreporconvergent */ 
        );
        /**Returns  the OptimizeBrep option - if set to true then xtbrep will be optimized e.g. faces merged together 
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: bool Optimize
        (
        );
        /**Sets  the OptimizeBrep option - if set to true then xtbrep will be optimized e.g. faces merged together 
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: void SetOptimize
        (
            bool optimize /** optimize */ 
        );
        /**Returns  the move model data 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::IfcImporter::MoveDataEnum MoveModelData
        (
        );
        /**Sets  the move model data 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void SetMoveModelData
        (
            NXOpen::IfcImporter::MoveDataEnum moveModelData /** movemodeldata */ 
        );
        /**Returns  the deltax 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: double Deltax
        (
        );
        /**Sets  the deltax 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void SetDeltax
        (
            double deltax /** deltax */ 
        );
        /**Returns  the deltay 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: double Deltay
        (
        );
        /**Sets  the deltay 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void SetDeltay
        (
            double deltay /** deltay */ 
        );
        /**Returns  the deltaz 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: double Deltaz
        (
        );
        /**Sets  the deltaz 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void SetDeltaz
        (
            double deltaz /** deltaz */ 
        );
        /**Returns  the rotate around Z by degrees 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: double RotateAroundZByDegrees
        (
        );
        /**Sets  the rotate around Z by degrees 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void SetRotateAroundZByDegrees
        (
            double rotateAroundZByDegrees /** rotatearoundzbydegrees */ 
        );
        /**Returns  the output file - name of a file to which we are importing part 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: NXString OutputFile
        (
        );
        /**Sets  the output file - name of a file to which we are importing part 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void SetOutputFile
        (
            const NXString & filename /** filename */ 
        );
        /**Sets  the output file - name of a file to which we are importing part 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        void SetOutputFile
        (
            const char * filename /** filename */ 
        );
        /**Returns  the message level for syslog messages when loading Ifc files 
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::IfcImporter::MessageEnum Messages
        (
        );
        /**Sets  the message level for syslog messages when loading Ifc files 
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: void SetMessages
        (
            NXOpen::IfcImporter::MessageEnum messages /** messages */ 
        );
        /**Returns  the information flag - set this to true to display info in window
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: bool ShowInformationWindowFlag
        (
        );
        /**Sets  the information flag - set this to true to display info in window
         <br>  Created in NX1872.0.0.  <br>  
         <br> License requirements : None */
        public: void SetShowInformationWindowFlag
        (
            bool doingInformationWindow /** doinginformationwindow */ 
        );
        /**Returns  the building controls 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: bool BuildingControls
        (
        );
        /**Sets  the building controls 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void SetBuildingControls
        (
            bool buildingControls /** buildingcontrols */ 
        );
        /**Returns  the plumbing fire protection 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: bool PlumbingFireProtection
        (
        );
        /**Sets  the plumbing fire protection 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void SetPlumbingFireProtection
        (
            bool plumbingFireProtection /** plumbingfireprotection */ 
        );
        /**Returns  the structural elements 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: bool StructuralElements
        (
        );
        /**Sets  the structural elements 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void SetStructuralElements
        (
            bool structuralElements /** structuralelements */ 
        );
        /**Returns  the structural analysis 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: bool StructuralAnalysis
        (
        );
        /**Sets  the structural analysis 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void SetStructuralAnalysis
        (
            bool structuralAnalysis /** structuralanalysis */ 
        );
        /**Returns  the h vac 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: bool Hvac
        (
        );
        /**Sets  the h vac 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void SetHvac
        (
            bool hvac /** hvac */ 
        );
        /**Returns  the electrical 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: bool Electrical
        (
        );
        /**Sets  the electrical 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void SetElectrical
        (
            bool electrical /** electrical */ 
        );
        /**Returns  the shared bldg services elements 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: bool SharedBldgServicesElements
        (
        );
        /**Sets  the shared bldg services elements 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void SetSharedBldgServicesElements
        (
            bool sharedBldgServicesElements /** sharedbldgserviceselements */ 
        );
        /**Returns  the shared component elements 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: bool SharedComponentElements
        (
        );
        /**Sets  the shared component elements 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void SetSharedComponentElements
        (
            bool sharedComponentElements /** sharedcomponentelements */ 
        );
        /**Returns  the shared building elements 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: bool SharedBuildingElements
        (
        );
        /**Sets  the shared building elements 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void SetSharedBuildingElements
        (
            bool sharedBuildingElements /** sharedbuildingelements */ 
        );
        /**Returns  the shared facilities elements 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: bool SharedFacilitiesElements
        (
        );
        /**Sets  the shared facilities elements 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void SetSharedFacilitiesElements
        (
            bool sharedFacilitiesElements /** sharedfacilitieselements */ 
        );
        /**Returns  the product extension 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: bool ProductExtension
        (
        );
        /**Sets  the product extension 
         <br>  Created in NX1899.0.0.  <br>  
         <br> License requirements : None */
        public: void SetProductExtension
        (
            bool productExtension /** productextension */ 
        );
    };
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
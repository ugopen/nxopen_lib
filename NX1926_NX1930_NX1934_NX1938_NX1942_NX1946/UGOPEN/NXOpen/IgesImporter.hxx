#ifndef NXOpen_IGESIMPORTER_HXX_INCLUDED
#define NXOpen_IGESIMPORTER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     IgesImporter.ja
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
#include <NXOpen/ObjectTypeSelector.hxx>
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
    class IgesImporter;
    class BaseImporter;
    class ObjectTypeSelector;
    class _IgesImporterBuilder;
    class IgesImporterImpl;
    /**
        Represents a @link NXOpen::IgesImporter NXOpen::IgesImporter@endlink  to be used when importing the IGES Data
        This class is created using @link NXOpen::DexManager NXOpen::DexManager@endlink .
        NULL object will be returned from Commit()  <br> To create a new instance of this class, use @link NXOpen::DexManager::CreateIgesImporter  NXOpen::DexManager::CreateIgesImporter @endlink  <br> 
    Default values.
    <list type="table"> 
     
    <listheader><term> 
    Property</term>  <description> 
    Value</description> </listheader>
    <item><term> 
     
    CopiousData </term> <description> 
     
    CubicNURBBestfitSpline </description> </item> 

    <item><term> 
     
    FlattenAssembly </term> <description> 
     
    0 </description> </item> 

    <item><term> 
     
    GeomFixupTol </term> <description> 
     
    0 </description> </item> 

    <item><term> 
     
    ImportTo </term> <description> 
     
    WorkPart </description> </item> 

    <item><term> 
     
    ImportToTeamcenter </term> <description> 
     
    0 </description> </item> 

    <item><term> 
     
    LayerDefault </term> <description> 
     
    0 </description> </item> 

    <item><term> 
     
    MapViewDep </term> <description> 
     
    0 </description> </item> 

    <item><term> 
     
    Optimize </term> <description> 
     
    0 </description> </item> 

    <item><term> 
     
    ProcessHoldFlag </term> <description> 
     
    0 </description> </item> 

    <item><term> 
     
    SewSurfaces </term> <description> 
     
    0 </description> </item> 

    <item><term> 
     
    SimplifyGeometry </term> <description> 
     
    0 </description> </item> 

    <item><term> 
     
    SmoothBSurf </term> <description> 
     
    0 </description> </item> 

    <item><term> 
     
    SurfTrimTol </term> <description> 
     
    0.0254 </description> </item> 

    </list> 

     <br>  Created in NX6.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  IgesImporter : public NXOpen::BaseImporter
    {
        /** Import To Option */
        public: enum ImportToEnum
        {
            ImportToEnumWorkPart/** import iges file to work part */,
            ImportToEnumNewPart/** import iges file to new part */
        };

        /** Copious Data Option */
        public: enum CopiousDataEnum
        {
            CopiousDataEnumCubicNURBBestfitSpline/** map copious data to Cubic Nurb best fit spline */,
            CopiousDataEnumLinearNURBSpline/** map copious data to Linear Nurb spline */,
            CopiousDataEnumGroupofLines/** Group of lines */
        };

        private: IgesImporterImpl * m_igesimporter_impl;
        private: friend class  _IgesImporterBuilder;
        protected: IgesImporter();
        public: ~IgesImporter();
        /** Returns the save settings - this will save the settings to a file specified 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SaveSettings
        (
            const NXString & filename /** filename */ 
        );
        /** Returns the save settings - this will save the settings to a file specified 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        void SaveSettings
        (
            const char * filename /** filename */ 
        );
        /**Returns  the import to - this option will determine the destination for imported iges file. it can
                    either be new part or work part. 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::IgesImporter::ImportToEnum ImportTo
        (
        );
        /**Sets  the import to - this option will determine the destination for imported iges file. it can
                    either be new part or work part. 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetImportTo
        (
            NXOpen::IgesImporter::ImportToEnum importTo /** importto */ 
        );
        /**Returns  the flatten assembly - if set to true then assembly structure will not be retained 
         <br>  Created in NX7.0.0.  <br>  
         <br> License requirements : None */
        public: bool ImportToTeamcenter
        (
        );
        /**Sets  the flatten assembly - if set to true then assembly structure will not be retained 
         <br>  Created in NX7.0.0.  <br>  
         <br> License requirements : None */
        public: void SetImportToTeamcenter
        (
            bool importToTeamcenter /** importtoteamcenter */ 
        );
        /**Returns  the settings file - definition file for default options 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXString SettingsFile
        (
        );
        /**Sets  the settings file - definition file for default options 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetSettingsFile
        (
            const NXString & filename /** filename */ 
        );
        /**Sets  the settings file - definition file for default options 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        void SetSettingsFile
        (
            const char * filename /** filename */ 
        );
        /**Returns  the objectTypes - this is subcomponent being used to set object types filters. This
                    will be used to filter objects based on the types 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::ObjectTypeSelector * ObjectTypes
        (
        );
        /**Returns  the layerMask - comma spearate list of enabled layers 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXString LayerMask
        (
        );
        /**Sets  the layerMask - comma spearate list of enabled layers 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetLayerMask
        (
            const NXString & layerMask /** layermask */ 
        );
        /**Sets  the layerMask - comma spearate list of enabled layers 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        void SetLayerMask
        (
            const char * layerMask /** layermask */ 
        );
        /**Returns  the copious data mapping 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::IgesImporter::CopiousDataEnum CopiousData
        (
        );
        /**Sets  the copious data mapping 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetCopiousData
        (
            NXOpen::IgesImporter::CopiousDataEnum copiousData /** copiousdata */ 
        );
        /**Returns  the map view dep - set to true if you want to map view dependent/modified entity to model object 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: bool MapViewDep
        (
        );
        /**Sets  the map view dep - set to true if you want to map view dependent/modified entity to model object 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetMapViewDep
        (
            bool mapViewDep /** mapviewdep */ 
        );
        /**Returns  the smooth bsurf - set the flag to true if b-surfaced are required to be smoothed
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: bool SmoothBSurf
        (
        );
        /**Sets  the smooth bsurf - set the flag to true if b-surfaced are required to be smoothed
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetSmoothBSurf
        (
            bool smoothBSurf /** smoothbsurf */ 
        );
        /**Returns  the flatten assembly - if set to true then assembly structure will not be retained 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: bool FlattenAssembly
        (
        );
        /**Sets  the flatten assembly - if set to true then assembly structure will not be retained 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetFlattenAssembly
        (
            bool flattenAssembly /** flattenassembly */ 
        );
        /**Returns  the sew surfaces - set this to true if automatic sewing of surfaces is desired 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: bool SewSurfaces
        (
        );
        /**Sets  the sew surfaces - set this to true if automatic sewing of surfaces is desired 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetSewSurfaces
        (
            bool sewSurfaces /** sewsurfaces */ 
        );
        /**Returns  the simplify geometry - set this to true if automatic simplification of geometry is desired 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: bool SimplifyGeometry
        (
        );
        /**Sets  the simplify geometry - set this to true if automatic simplification of geometry is desired 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetSimplifyGeometry
        (
            bool simplifyGeometry /** simplifygeometry */ 
        );
        /**Returns  the optimize - set this to true if automatic optimize geometry  
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: bool Optimize
        (
        );
        /**Sets  the optimize - set this to true if automatic optimize geometry  
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetOptimize
        (
            bool optimize /** optimize */ 
        );
        /**Returns  the layer default for level 0 in iges
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: int LayerDefault
        (
        );
        /**Sets  the layer default for level 0 in iges
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetLayerDefault
        (
            int layerDefault /** layerdefault */ 
        );
        /**Returns  the surf trim tol - surface trimming tolerance
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: double SurfTrimTol
        (
        );
        /**Sets  the surf trim tol - surface trimming tolerance
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetSurfTrimTol
        (
            double surfTrimTol /** surftrimtol */ 
        );
        /**Returns  the geometry fixup tol 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: double GeomFixupTol
        (
        );
        /**Sets  the geometry fixup tol 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetGeomFixupTol
        (
            double geomFixupTol /** geomfixuptol */ 
        );
        /**Returns  the file open flag - set this to false if doing file import
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: bool FileOpenFlag
        (
        );
        /**Sets  the file open flag - set this to false if doing file import
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetFileOpenFlag
        (
            bool doingFileOpen /** doingfileopen */ 
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

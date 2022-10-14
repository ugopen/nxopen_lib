#ifndef NXOpen_CAE_HOTSPOTRECIPEBUILDER_HXX_INCLUDED
#define NXOpen_CAE_HOTSPOTRECIPEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_HotspotRecipeBuilder.ja
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
#include <NXOpen/CAE_Result.hxx>
#include <NXOpen/Builder.hxx>
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
        class HotspotRecipeBuilder;
    }
    class Builder;
    namespace CAE
    {
        class HotspotRecipe;
    }
    class TaggedObject;
    namespace CAE
    {
        class _HotspotRecipeBuilderBuilder;
        class HotspotRecipeBuilderImpl;
        /**
            Represents a @link NXOpen::CAE::HotspotRecipeBuilder NXOpen::CAE::HotspotRecipeBuilder@endlink 
             <br> To create a new instance of this class, use @link NXOpen::CAE::ResultManager::CreateHotspotRecipeBuilder  NXOpen::CAE::ResultManager::CreateHotspotRecipeBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        IsSortRangeAboveRes </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        IsSortRangeBelowRes </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        IsSortSelectedEntities </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        MaxNumRegions </td> <td> 
         
        10 </td> </tr> 

        <tr><td> 
         
        NeighborOffset </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        OffsetTypeMinMax </td> <td> 
         
        ByValueOffset </td> </tr> 

        <tr><td> 
         
        SortAboveParamVal </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        SortBelowParamVal </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        SpanOfRegion </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        ThresholdValue </td> <td> 
         
        0 </td> </tr> 

        </table>  

         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  HotspotRecipeBuilder : public NXOpen::Builder
        {
            /** Sorting methods*/
            public: enum EnumSortingMethod
            {
                EnumSortingMethodThreshold/** threshold */ ,
                EnumSortingMethodRange/** range */ ,
                EnumSortingMethodMinimumResult/** minimum result */ ,
                EnumSortingMethodMaximumResults/** maximum results */ 
            };

            /** Sort min-max methods with following types*/
            public: enum EnumOffsetTypeMinMax
            {
                EnumOffsetTypeMinMaxByValueOffset/** by value offset */ ,
                EnumOffsetTypeMinMaxByPercentageOffset/** by percentage offset */ ,
                EnumOffsetTypeMinMaxByNumberofEntities/** by numberof entities */ 
            };

            /** Threshold Type*/
            public: enum EnumThresholdType
            {
                EnumThresholdTypeMaxOffset/** max offset */ ,
                EnumThresholdTypeMinOffset/** min offset */ ,
                EnumThresholdTypeMaxFactor/** max factor */ ,
                EnumThresholdTypeMinFactor/** min factor */ 
            };

            private: HotspotRecipeBuilderImpl * m_hotspotrecipebuilder_impl;
            private: friend class  _HotspotRecipeBuilderBuilder;
            protected: HotspotRecipeBuilder();
            public: ~HotspotRecipeBuilder();
            /**Returns  the name str 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXString RecipeName
            (
            );
            /**Sets  the name str 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetRecipeName
            (
                const NXString & nameStr /** namestr */ 
            );
            /**Sets  the name str 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetRecipeName
            (
                const char * nameStr /** namestr */ 
            );
            /**Returns  the enum result loc 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::Result::Location ResultLocation
            (
            );
            /**Sets  the enum result loc 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetResultLocation
            (
                NXOpen::CAE::Result::Location enumResultLoc /** enumresultloc */ 
            );
            /** Gets the enum result type  @return  
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXString GetResultQuantity
            (
            );
            /** Sets the enum result type 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetResultQuantity
            (
                const NXString & resultQuantity /** resultquantity */ 
            );
            /** Sets the enum result type 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            void SetResultQuantity
            (
                const char * resultQuantity /** resultquantity */ 
            );
            /**Returns  the e data type filter 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::Result::DataType DataTypeFilter
            (
            );
            /**Sets  the e data type filter 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetDataTypeFilter
            (
                NXOpen::CAE::Result::DataType eDataTypeFilter /** edatatypefilter */ 
            );
            /**Returns  the enum res comp 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::Result::Component ResultComponent
            (
            );
            /**Sets  the enum res comp 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetResultComponent
            (
                NXOpen::CAE::Result::Component enumResComp /** enumrescomp */ 
            );
            /**Returns  the enum sort method 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::HotspotRecipeBuilder::EnumSortingMethod SortMethod
            (
            );
            /**Sets  the enum sort method 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetSortMethod
            (
                NXOpen::CAE::HotspotRecipeBuilder::EnumSortingMethod enumSortMethod /** enumsortmethod */ 
            );
            /**Returns  the d threshold val 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: double ThresholdValue
            (
            );
            /**Sets  the d threshold val 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetThresholdValue
            (
                double dThresholdVal /** dthresholdval */ 
            );
            /**Returns  the enum threshold type 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::HotspotRecipeBuilder::EnumThresholdType ThresholdType
            (
            );
            /**Sets  the enum threshold type 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetThresholdType
            (
                NXOpen::CAE::HotspotRecipeBuilder::EnumThresholdType enumThresholdType /** enumthresholdtype */ 
            );
            /**Returns  the i neighbor offset 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: double NeighborOffset
            (
            );
            /**Sets  the i neighbor offset 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetNeighborOffset
            (
                double dNeighborOffset /** dneighboroffset */ 
            );
            /**Returns  the i span region 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: int SpanOfRegion
            (
            );
            /**Sets  the i span region 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetSpanOfRegion
            (
                int iSpanRegion /** ispanregion */ 
            );
            /**Returns  the toggle sort below 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsSortRangeBelowRes
            (
            );
            /**Sets  the toggle sort below 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetSortRangeBelowRes
            (
                bool toggleSortBelow /** togglesortbelow */ 
            );
            /**Returns  the toggle sort above 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsSortRangeAboveRes
            (
            );
            /**Sets  the toggle sort above 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetSortRangeAboveRes
            (
                bool toggleSortAbove /** togglesortabove */ 
            );
            /**Returns  the enum sort min max res by 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::HotspotRecipeBuilder::EnumOffsetTypeMinMax OffsetTypeMinMax
            (
            );
            /**Sets  the enum sort min max res by 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetOffsetTypeMinMax
            (
                NXOpen::CAE::HotspotRecipeBuilder::EnumOffsetTypeMinMax offsetType /** offsettype */ 
            );
            /**Returns  the d sort below 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: double SortBelowParamVal
            (
            );
            /**Sets  the d sort below 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetSortBelowParamVal
            (
                double dSortBelow /** dsortbelow */ 
            );
            /**Returns  the d sort above 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: double SortAboveParamVal
            (
            );
            /**Sets  the d sort above 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetSortAboveParamVal
            (
                double dSortAbove /** dsortabove */ 
            );
            /**Returns  the i max regions 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: int MaxNumRegions
            (
            );
            /**Sets  the i max regions 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetMaxNumRegions
            (
                int iMaxRegions /** imaxregions */ 
            );
            /** Gets the offset for sorting min/max params 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: double GetOffsetForMinMax
            (
            );
            /** Sets the offset for sorting min/max params 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetOffsetForMinMax
            (
                double offsetByValue /** offsetbyvalue */ 
            );
            /**Returns  the toggle select entities 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsSortSelectedEntities
            (
            );
            /**Sets  the toggle select entities 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetSortSelectedEntities
            (
                bool toggleSelectEntities /** toggleselectentities */ 
            );
            /** Gets the entity objects for extracting result data. Objects passed to this method 
                        are of the type defined by 
                        JA_SFRES_Location.
                    
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::TaggedObject *> GetEntityObjects
            (
            );
            /** Sets the entity objects for extracting result data. Objects passed to this method 
                        are of the type defined by 
                        JA_SFRES_Location.
                    
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void SetEntityObjects
            (
                const std::vector<NXOpen::TaggedObject *> & entityObjs /** entityobjs */ 
            );
            /** Init the builder from recipe
                    
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void InitFromRecipe
            (
                NXOpen::CAE::HotspotRecipe * recipe /** recipe */ 
            );
            /** Gets Result Quantity type.
                    
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::Result::Quantity GetResultQuantityType
            (
            );
            /** Sets Result Quantity Type.
                    
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetResultQuantityType
            (
                NXOpen::CAE::Result::Quantity resQuan /** resquan */ 
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
#ifndef NXOpen_ANNOTATIONS_PMIMANAGER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiManager.ja
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
#include <NXOpen/Annotations_ArbitraryAreaSeedBuilder.hxx>
#include <NXOpen/Annotations_RegionBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class PmiManager;
    }
    class Part;
    namespace Annotations
    {
        class Annotation;
    }
    namespace Annotations
    {
        class ArbitraryAreaSeedBuilder;
    }
    namespace Annotations
    {
        class Pmi;
    }
    namespace Annotations
    {
        class PmiAttributeCollection;
    }
    namespace Annotations
    {
        class PmiCollection;
    }
    namespace Annotations
    {
        class Region;
    }
    namespace Annotations
    {
        class RegionBuilder;
    }
    class View;
    namespace Annotations
    {
        /** Represents an object that manages PMI objects.  <br> To obtain an instance of this class, refer to @link Part Part@endlink  <br> */
        class NXOPENCPPEXPORT PmiManager
        {
            private: NXOpen::Part* m_owner;
            public: explicit PmiManager(NXOpen::Part *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Creates copies of input PMI objects in the part. 
                         <br> 
                        Client must perform update @link Update::DoUpdate Update::DoUpdate@endlink  after calling 
                        this method.  <br>   @return  Copies of PMI objects  <br> License requirements : geometric_tol ("GDT") */
            public: std::vector<NXOpen::Annotations::Pmi *> CopyObjects
            (
                const std::vector<NXOpen::Annotations::Pmi *> & inputObjects /** PMI objects to be copied */
            );
            /** Creates copies of input PMI Display Instance objects in the part.             
                         <br>             
                        Client must perform update @link Update::DoUpdate Update::DoUpdate@endlink ()
                        after calling this method.  <br>   @return  Copies of PMI Display Instance objects  <br> License requirements : geometric_tol ("GDT") */
            public: std::vector<NXOpen::Annotations::Annotation *> CopyDisplayInstanceObjects
            (
                const std::vector<NXOpen::Annotations::Annotation *> & inputObjects /** PMI Display Instance objects to be copied */,
                NXOpen::View * view /** View in which PMI Display Instance are copied. */
            );
            /** Cuts the input PMI Display Instance objects in the part. Cut operation makes the PMI
                        Display Instance object invisible in the view of cut and makes it visible in 
                        the view of paste.                      
                         <br>                
                        Client must perform update @link Update::DoUpdate Update::DoUpdate@endlink () after calling this 
                        method.  <br>   <br> License requirements : geometric_tol ("GDT") */
            public: void CutDisplayInstanceObjects
            (
                const std::vector<NXOpen::Annotations::Annotation *> & inputObjects /** PMI Display Instance objects to be cut */,
                const std::vector<NXOpen::View *> & cutViews /** List of cut views. Each PMI Display Instance
                                                                              object is cut from the corresponding view 
                                                                              in the list. 
                                                                              */,
                NXOpen::View * viewOfPaste /** View in which PMI Display Instances are pasted. */
            );
            /** Restores the unpasted PMI objects in the part. 
                         <br> 
                        This method is used by NX user interface to restore PMI objects that
                        were cut but not pasted. If called by an automation program, this
                        method can cause unexpected results.  <br>   <br> License requirements : geometric_tol ("GDT") */
            public: void RestoreUnpastedObjects
            (
            );
            /** The flag indicating whether the annotation is an inherited PMI on the drawing 
                        sheet/view. Inherited PMI is the associative copy of the PMI display 
                        instance in modeling.  @return   <br> License requirements : None */
            public: bool IsInheritedPmi
            (
                NXOpen::Annotations::Annotation * object /** Annotation to examine */
            );
            /** Returns the inherited PMI parent. The parent is the PMI Display Instance in modeling.  @return  Parent PMI Display Instance  <br> License requirements : None */
            public: NXOpen::Annotations::Annotation * GetInheritParent
            (
                NXOpen::Annotations::Annotation * inheritedPmi /** Inherited PMI */
            );
            /** Returns the PMI Display Instance parent. The parent is the PMI Object.  @return  Parent PMI object  <br> License requirements : None */
            public: NXOpen::Annotations::Pmi * GetDisplayInstanceParent
            (
                NXOpen::Annotations::Annotation * displayInstance /** PMI Display Instance */
            );
            /** Creates a @link Annotations::RegionBuilder Annotations::RegionBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::RegionBuilder * CreateRegionBuilder
            (
                NXOpen::Annotations::Region * region /** the region to be edited,
                                                                              if NULL,  then create a region */
            );
            /** Creates a @link Annotations::ArbitraryAreaSeedBuilder Annotations::ArbitraryAreaSeedBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::ArbitraryAreaSeedBuilder * CreateArbitraryAreaSeedBuilder
            (
            );
            /** Deletes or replaces one annotation with another.
                         <br> 
                        This will adjust the requirements ID of the annotation if one annotation replaces
                        another. This method may be used in NX generated automation programs but it is not
                        intended to be used in a customer  written automation program.
                         <br>   <br> License requirements : None */
            public: void DeleteReplaceAnnotation
            (
                NXOpen::Annotations::Annotation * oldAnnotation /** @link Annotations::Annotation Annotations::Annotation@endlink  Annotation or Dimension Set to be deleted */,
                NXOpen::Annotations::Annotation * newAnnotation /** @link Annotations::Annotation Annotations::Annotation@endlink  to replace the deleted annootation, can be NULL */
            );


            private: NXOpen::Annotations::PmiCollection *pmis;
            /** Pmi collection */
            public: NXOpen::Annotations::PmiCollection *Pmis()
            {
                return pmis;
            }
            private: NXOpen::Annotations::PmiAttributeCollection *pmiAttributes;
            /** PmiAttribute collection */
            public: NXOpen::Annotations::PmiAttributeCollection *PmiAttributes()
            {
                return pmiAttributes;
            }
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif

#ifndef NXOpen_ANNOTATIONS_PMIATTRIBUTECOLLECTION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIATTRIBUTECOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiAttributeCollection.ja
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
#include <NXOpen/Annotations_BalloonNoteBuilder.hxx>
#include <NXOpen/Annotations_CompanyProprietaryInformationBuilder.hxx>
#include <NXOpen/Annotations_CoordinateNoteBuilder.hxx>
#include <NXOpen/Annotations_EnterpriseIdentificationBuilder.hxx>
#include <NXOpen/Annotations_ExportControlBuilder.hxx>
#include <NXOpen/Annotations_GeneralNoteBuilder.hxx>
#include <NXOpen/Annotations_GovernmentSecurityInformationBuilder.hxx>
#include <NXOpen/Annotations_LocatorDesignatorBuilder.hxx>
#include <NXOpen/Annotations_MaterialSpecificationBuilder.hxx>
#include <NXOpen/Annotations_PartIdentificationBuilder.hxx>
#include <NXOpen/Annotations_PmiAttributeBuilder.hxx>
#include <NXOpen/Annotations_PmiAttributeValueIntegerBuilder.hxx>
#include <NXOpen/Annotations_PmiAttributeValueListBuilder.hxx>
#include <NXOpen/Annotations_PmiAttributeValueMultipleStringBuilder.hxx>
#include <NXOpen/Annotations_PmiAttributeValueNumberBuilder.hxx>
#include <NXOpen/Annotations_PmiAttributeValueStringBuilder.hxx>
#include <NXOpen/Annotations_PmiAttributeValueUrlBuilder.hxx>
#include <NXOpen/Annotations_PmiIntegerBuilder.hxx>
#include <NXOpen/Annotations_PmiNumberBuilder.hxx>
#include <NXOpen/Annotations_PmiStringBuilder.hxx>
#include <NXOpen/Annotations_PmiUrlNoteBuilder.hxx>
#include <NXOpen/Annotations_PmiUserDefinedBuilder.hxx>
#include <NXOpen/Annotations_ProcessSpecificationBuilder.hxx>
#include <NXOpen/Annotations_SpecificNoteBuilder.hxx>
#include <NXOpen/Annotations_SurfaceFinishBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class PmiAttributeCollection;
    }
    namespace Annotations
    {
        class PmiManager;
    }
    namespace Annotations
    {
        class PmiAttribute;
    }
    namespace Annotations
    {
        class BalloonNote;
    }
    namespace Annotations
    {
        class BalloonNoteBuilder;
    }
    namespace Annotations
    {
        class CompanyProprietaryInformation;
    }
    namespace Annotations
    {
        class CompanyProprietaryInformationBuilder;
    }
    namespace Annotations
    {
        class CoordinateNote;
    }
    namespace Annotations
    {
        class CoordinateNoteBuilder;
    }
    namespace Annotations
    {
        class EnterpriseIdentification;
    }
    namespace Annotations
    {
        class EnterpriseIdentificationBuilder;
    }
    namespace Annotations
    {
        class ExportControl;
    }
    namespace Annotations
    {
        class ExportControlBuilder;
    }
    namespace Annotations
    {
        class GeneralNote;
    }
    namespace Annotations
    {
        class GeneralNoteBuilder;
    }
    namespace Annotations
    {
        class GovernmentSecurityInformation;
    }
    namespace Annotations
    {
        class GovernmentSecurityInformationBuilder;
    }
    namespace Annotations
    {
        class LocatorDesignator;
    }
    namespace Annotations
    {
        class LocatorDesignatorBuilder;
    }
    namespace Annotations
    {
        class MaterialSpecification;
    }
    namespace Annotations
    {
        class MaterialSpecificationBuilder;
    }
    namespace Annotations
    {
        class PartIdentification;
    }
    namespace Annotations
    {
        class PartIdentificationBuilder;
    }
    namespace Annotations
    {
        class PmiAttributeBuilder;
    }
    namespace Annotations
    {
        class PmiAttributeValueInteger;
    }
    namespace Annotations
    {
        class PmiAttributeValueIntegerBuilder;
    }
    namespace Annotations
    {
        class PmiAttributeValueList;
    }
    namespace Annotations
    {
        class PmiAttributeValueListBuilder;
    }
    namespace Annotations
    {
        class PmiAttributeValueMultipleString;
    }
    namespace Annotations
    {
        class PmiAttributeValueMultipleStringBuilder;
    }
    namespace Annotations
    {
        class PmiAttributeValueNumber;
    }
    namespace Annotations
    {
        class PmiAttributeValueNumberBuilder;
    }
    namespace Annotations
    {
        class PmiAttributeValueString;
    }
    namespace Annotations
    {
        class PmiAttributeValueStringBuilder;
    }
    namespace Annotations
    {
        class PmiAttributeValueUrl;
    }
    namespace Annotations
    {
        class PmiAttributeValueUrlBuilder;
    }
    namespace Annotations
    {
        class PmiInteger;
    }
    namespace Annotations
    {
        class PmiIntegerBuilder;
    }
    namespace Annotations
    {
        class PmiNumber;
    }
    namespace Annotations
    {
        class PmiNumberBuilder;
    }
    namespace Annotations
    {
        class PmiString;
    }
    namespace Annotations
    {
        class PmiStringBuilder;
    }
    namespace Annotations
    {
        class PmiUrlNote;
    }
    namespace Annotations
    {
        class PmiUrlNoteBuilder;
    }
    namespace Annotations
    {
        class PmiUserDefined;
    }
    namespace Annotations
    {
        class PmiUserDefinedBuilder;
    }
    namespace Annotations
    {
        class ProcessSpecification;
    }
    namespace Annotations
    {
        class ProcessSpecificationBuilder;
    }
    namespace Annotations
    {
        class SpecificNote;
    }
    namespace Annotations
    {
        class SpecificNoteBuilder;
    }
    namespace Annotations
    {
        class SurfaceFinish;
    }
    namespace Annotations
    {
        class SurfaceFinishBuilder;
    }
    class TaggedObject;
    namespace Annotations
    {
        /** Represents a collection of @link Annotations::PmiAttribute Annotations::PmiAttribute@endlink  objects.  <br> To obtain an instance of this class, refer to @link Annotations::PmiManager Annotations::PmiManager@endlink  <br> */
        class NXOPENCPPEXPORT PmiAttributeCollection : public TaggedObjectCollection
        {
            private: NXOpen::Annotations::PmiManager* m_owner;
            public: explicit PmiAttributeCollection(NXOpen::Annotations::PmiManager *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Iterator for accessing the contents of the collection. */
            class iterator
            {
            public:
                typedef Annotations::PmiAttribute * value_type;
                /** Default constructor */
                iterator() : m_context(NULL), m_current(NULL_TAG)
                {
                }//lint !e1401 m_state is not initialized 
                explicit iterator(NXOpen::Annotations::PmiAttributeCollection *context) : m_context(context), m_current(NULL_TAG)
                {
                }//lint !e1401 m_state is not initialized 
                iterator(const iterator &other): m_context(NULL), m_current(NULL_TAG)
                {
                    copy(other);
                }
                /** Copy constructor */
                iterator &operator =(const iterator &other)
                {
                    if (&other != this)
                        copy(other);
                    return *this;
                }
                /** Tests if the iterator objects on the left side and the right side of the operator are equal. */
                bool operator ==(const iterator &other) const
                {
                    return m_current == other.m_current && m_context == other.m_context;
                }
                /** Tests if the iterator objects on the left side and the right side of the operator are not equal. */
                bool operator !=(const iterator &other) const
                {
                    return !operator == (other);
                }
                /** Return the element currently pointed to by the iterator. */
                NXOPENCPPEXPORT  value_type operator * ();
                /** Points the iterator to next element. */
                iterator & operator ++()
                {
                    next();
                    return *this;
                }
                /** Points the iterator to next element. */
                iterator operator ++(int)
                {
                    iterator tmp(*this);
                    ++*this;
                    return tmp;
                }
            private:
                void copy(const iterator &other)
                {
                    m_context = other.m_context;
                    m_current = other.m_current;
                    for (int i = 0; i < sizeof(m_state)/sizeof(m_state[0]); i++)
                         m_state[i] = other.m_state[i];
                }
                NXOPENCPPEXPORT  void next();
                NXOpen::Annotations::PmiAttributeCollection *m_context;
                tag_t m_current;
                unsigned int m_state[8];
            };
            /** Returns an iterator addressing the first element. */
            iterator begin();
            /** Returns an iterator addressing one past the last element. */
            iterator end()
            {
                return iterator(this);
            }
            /** Creates a @link Annotations::PmiAttributeBuilder Annotations::PmiAttributeBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::PmiAttributeBuilder * CreatePmiAttributeBuilder
            (
                NXOpen::Annotations::PmiAttribute * pmiAttr /** pmi base class*/
            );
            /** Creates a @link Annotations::PmiUserDefinedBuilder Annotations::PmiUserDefinedBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::PmiUserDefinedBuilder * CreatePmiUserDefinedBuilder
            (
                NXOpen::Annotations::PmiUserDefined * userDefined /** user defined */
            );
            /** Creates a @link Annotations::PmiIntegerBuilder Annotations::PmiIntegerBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::PmiIntegerBuilder * CreatePmiIntegerBuilder
            (
                NXOpen::Annotations::PmiInteger * pmiInteger /** integer*/
            );
            /** Creates a @link Annotations::PmiStringBuilder Annotations::PmiStringBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::PmiStringBuilder * CreatePmiStringBuilder
            (
                NXOpen::Annotations::PmiString * pmiString /** string */
            );
            /** Creates a @link Annotations::PmiNumberBuilder Annotations::PmiNumberBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::PmiNumberBuilder * CreatePmiNumberBuilder
            (
                NXOpen::Annotations::PmiNumber * pmiNumber /** number */
            );
            /** Creates a @link Annotations::PmiUrlNoteBuilder Annotations::PmiUrlNoteBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::PmiUrlNoteBuilder * CreatePmiUrlNoteBuilder
            (
                NXOpen::Annotations::PmiUrlNote * pmiUrlNote /** url note */
            );
            /** Creates a @link Annotations::GovernmentSecurityInformationBuilder Annotations::GovernmentSecurityInformationBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::GovernmentSecurityInformationBuilder * CreateGovernmentSecurityInformationBuilder
            (
                NXOpen::Annotations::GovernmentSecurityInformation * governmentSecurityInformation /** eMarking government */
            );
            /** Creates a @link Annotations::CompanyProprietaryInformationBuilder Annotations::CompanyProprietaryInformationBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::CompanyProprietaryInformationBuilder * CreateCompanyProprietaryInformationBuilder
            (
                NXOpen::Annotations::CompanyProprietaryInformation * companyProprietaryInformation /** company proprietary */
            );
            /** Creates a @link Annotations::GeneralNoteBuilder Annotations::GeneralNoteBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::GeneralNoteBuilder * CreateGeneralNoteBuilder
            (
                NXOpen::Annotations::GeneralNote * generalNote /** general note*/
            );
            /** Creates a @link Annotations::SurfaceFinishBuilder Annotations::SurfaceFinishBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::SurfaceFinishBuilder * CreateSurfaceFinishBuilder
            (
                NXOpen::Annotations::SurfaceFinish * surfaceFinish /** surface finish*/
            );
            /** Creates a @link Annotations::SpecificNoteBuilder Annotations::SpecificNoteBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::SpecificNoteBuilder * CreateSpecificNoteBuilder
            (
                NXOpen::Annotations::SpecificNote * specificNote /** specific note*/
            );
            /** Creates a @link Annotations::CoordinateNoteBuilder Annotations::CoordinateNoteBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::CoordinateNoteBuilder * CreateCoordinateNoteBuilder
            (
                NXOpen::Annotations::CoordinateNote * coordinateNote /** coordinate note*/
            );
            /** Creates a @link Annotations::EnterpriseIdentificationBuilder Annotations::EnterpriseIdentificationBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::EnterpriseIdentificationBuilder * CreateEnterpriseIdentificationBuilder
            (
                NXOpen::Annotations::EnterpriseIdentification * enterpriseIdentification /** enterprise identification*/
            );
            /** Creates a @link Annotations::PartIdentificationBuilder Annotations::PartIdentificationBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::PartIdentificationBuilder * CreatePartIdentificationBuilder
            (
                NXOpen::Annotations::PartIdentification * partIdentification /** part identification */
            );
            /** Creates a @link Annotations::ProcessSpecificationBuilder Annotations::ProcessSpecificationBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::ProcessSpecificationBuilder * CreateProcessSpecificationBuilder
            (
                NXOpen::Annotations::ProcessSpecification * processSpecification /** process specification */
            );
            /** Creates a @link Annotations::MaterialSpecificationBuilder Annotations::MaterialSpecificationBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::MaterialSpecificationBuilder * CreateMaterialSpecificationBuilder
            (
                NXOpen::Annotations::MaterialSpecification * materialSpecification /** material specification */
            );
            /** Creates a @link Annotations::LocatorDesignatorBuilder Annotations::LocatorDesignatorBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::LocatorDesignatorBuilder * CreateLocatorDesignatorBuilder
            (
                NXOpen::Annotations::LocatorDesignator * locatorDesignator /** locator designator */
            );
            /** Creates a @link Annotations::BalloonNoteBuilder Annotations::BalloonNoteBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::BalloonNoteBuilder * CreateBalloonNoteBuilder
            (
                NXOpen::Annotations::BalloonNote * balloonNote /** balloon note */
            );
            /** Creates a @link Annotations::PmiAttributeValueStringBuilder Annotations::PmiAttributeValueStringBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::PmiAttributeValueStringBuilder * CreatePmiAttributeValueStringBuilder
            (
                NXOpen::Annotations::PmiAttributeValueString * pmiAttributeValueString /** string value */
            );
            /** Creates a @link Annotations::PmiAttributeValueMultipleStringBuilder Annotations::PmiAttributeValueMultipleStringBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::PmiAttributeValueMultipleStringBuilder * CreatePmiAttributeValueMultipleStringBuilder
            (
                NXOpen::Annotations::PmiAttributeValueMultipleString * pmiAttributeValueMultipleString /** multiple string value */
            );
            /** Creates a @link Annotations::PmiAttributeValueIntegerBuilder Annotations::PmiAttributeValueIntegerBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::PmiAttributeValueIntegerBuilder * CreatePmiAttributeValueIntegerBuilder
            (
                NXOpen::Annotations::PmiAttributeValueInteger * pmiAttributeValueInteger /** integer value */
            );
            /** Creates a @link Annotations::PmiAttributeValueListBuilder Annotations::PmiAttributeValueListBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::PmiAttributeValueListBuilder * CreatePmiAttributeValueListBuilder
            (
                NXOpen::Annotations::PmiAttributeValueList * pmiAttributeValueList /** list value */
            );
            /** Creates a @link Annotations::PmiAttributeValueUrlBuilder Annotations::PmiAttributeValueUrlBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::PmiAttributeValueUrlBuilder * CreatePmiAttributeValueUrlBuilder
            (
                NXOpen::Annotations::PmiAttributeValueUrl * pmiAttributeValueUrl /** list value */
            );
            /** Creates a @link Annotations::PmiAttributeValueNumberBuilder Annotations::PmiAttributeValueNumberBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::PmiAttributeValueNumberBuilder * CreatePmiAttributeValueNumberBuilder
            (
                NXOpen::Annotations::PmiAttributeValueNumber * pmiAttributeValueNumber /** number value */
            );
            /** Creates a @link Annotations::ExportControlBuilder Annotations::ExportControlBuilder@endlink   @return   <br> License requirements : None */
            public: NXOpen::Annotations::ExportControlBuilder * CreateExportControlBuilder
            (
                NXOpen::Annotations::ExportControl * exportControl /** export control */
            );
            /** Finds the @link Annotations::PmiAttribute Annotations::PmiAttribute@endlink  with the given identifier as recorded in a journal. 
                        An object may not return the same value as its JournalIdentifier in different versions of 
                        the software. However newer versions of the software should find the same object when 
                        FindObject is passed older versions of its journal identifier. In general, this method 
                        should not be used in handwritten code and exists to support record and playback of journals.
                        
                        An exception will be thrown if no object can be found with the given journal identifier.  @return  PMI with this identifier  <br> License requirements : None */
            public: NXOpen::TaggedObject * FindObject
            (
                const NXString & journalIdentifier /** Identifier of the pmi   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
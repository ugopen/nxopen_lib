#ifndef NXOpen_EXPRESSIONCOLLECTION_HXX_INCLUDED
#define NXOpen_EXPRESSIONCOLLECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ExpressionCollection.ja
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
#include <NXOpen/BasePart.hxx>
#include <NXOpen/SuppressByExpressionBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/TaggedObjectCollection.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class ExpressionCollection;
    class BasePart;
    class Expression;
    class SuppressByExpressionBuilder;
    class Unit;
    /** Represents a collection of expressions.  <br> To obtain an instance of this class, refer to @link BasePart BasePart@endlink  <br> */
    class NXOPENCPPEXPORT ExpressionCollection : public TaggedObjectCollection
    {
        /** Indicates the mode for importing expressions. */
        public: enum ImportMode
        {
            ImportModeReplace/** Overwrite existing expressions if the imported values differ */,
            ImportModeDontReplace/** Don't overwrite existing expressions. New expressions are created */,
            ImportModeDeleteImports/** Delete all expressions in the imported file */
        };

        /** Indicates the mode for exporting expressions. */
        public: enum ExportMode
        {
            ExportModeWorkPart/** All expressions in the given part */,
            ExportModeAllInAssyTree/** All expressions in the given part, and in its components */,
            ExportModeAllParts/** All expressions in All parts in the session */
        };

        /** Indicates the mode for sorting expressions. */
        public: enum SortType
        {
            SortTypeAlphaNum/** Alphabetic order, with numbers in numerical order */,
            SortTypeTimeStamp/** Creation order - earliest first */,
            SortTypeReverseTimeStamp/** Creation order - latest first */
        };

        private: NXOpen::BasePart* m_owner;
        public: explicit ExpressionCollection(NXOpen::BasePart *owner): m_owner(owner)
        {
        }
        public: 
        /**Returns the tag of this object.  */
        tag_t Tag() const; 
        /** Iterator for accessing the contents of the collection. */
        class iterator
        {
        public:
            typedef Expression * value_type;
            /** Default constructor */
            iterator() : m_context(NULL), m_current(NULL_TAG)
            {
            }//lint !e1401 m_state is not initialized 
            explicit iterator(NXOpen::ExpressionCollection *context) : m_context(context), m_current(NULL_TAG)
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
            NXOpen::ExpressionCollection *m_context;
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
        /** Creates an expression  @return  the new expression  <br> License requirements : None */
        public: NXOpen::Expression * Create
        (
            const NXString & string /** the equation for the expression.  Must be in the format: name = right_hand_side.
                                               For example, "x = 1.2 * y + z".   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Creates an expression with units.  @return  the new expression  <br> License requirements : None */
        public: NXOpen::Expression * CreateWithUnits
        (
            const NXString & string /** the equation for the expression.  Must be in the format: name = right_hand_side.
                                               For example, "x = 1.2 * y + z".   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            NXOpen::Unit * unitType /** units for the expression */
        );
        /** Creates a system expression.  After creating a system expression, you should
            associate it with an object, such as a sketch dimension.  System expressions are
            deleted when the object they are associated with is deleted.  @return  the new expression  <br> License requirements : None */
        public: NXOpen::Expression * CreateSystemExpression
        (
            const NXString & string /** the equation or right-hand-side for the expression.
                                               You can specify a name for the equation by providing a
                                               string in the format: name = right_hand_side.
                                               For example, "x = 1.2 * y + z".  If you do not
                                               provide a name, a name will be assigned automatically.
                                               For example, if the string is "1.2 * y + z", a
                                               name will be assigned automatically.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Creates a system expression with units.  After creating a system expression, you should
            associate it with an object, such as a sketch dimension.  System expressions are
            deleted when the object they are associated with is deleted.  @return  the new expression  <br> License requirements : None */
        public: NXOpen::Expression * CreateSystemExpressionWithUnits
        (
            const NXString & string /** the equation or right-hand-side for the expression.
                                               You can specify a name for the equation by providing a
                                               string in the format: name = right_hand_side.
                                               For example, "x = 1.2 * y + z".  If you do not
                                               provide a name, a name will be assigned automatically.
                                               For example, if the string is "1.2 * y + z", a
                                               name will be assigned automatically.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            NXOpen::Unit * unitType /** units for the expression */
        );
        /** Creates an expression of the specified type.  @return  the new expression  <br> License requirements : None */
        public: NXOpen::Expression * CreateExpression
        (
            const NXString & expressionType /** The type of the expression, such as "Number", "String", "Boolean", "Integer", "Point" and "Vector"   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            const NXString & string /** the equation for the expression.  Must be in the format: name = right_hand_side.
                                               For example, "x = 1.2 * y + z".   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Creates a system expression of the specified type.  After creating a system expression,
            you should associate it with an object, such as a sketch dimension.  System expressions are
            deleted when the object they are associated with is deleted.  @return  the new expression  <br> License requirements : None */
        public: NXOpen::Expression * CreateSystemExpression
        (
            const NXString & expressionType /** The type of the expression, such as "Number", "String", "Boolean", "Integer", "Point" and "Vector"   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            const NXString & string /** the equation or right-hand-side for the expression.
                                               You can specify a name for the equation by providing a
                                               string in the format: name = right_hand_side.
                                               For example, "x = 1.2 * y + z".  If you do not
                                               provide a name, a name will be assigned automatically.
                                               For example, if the string is "1.2 * y + z", a
                                               name will be assigned automatically.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Edits an expression. Note, there is no difference between this method and
            editing the expression via @link Expression::SetRightHandSide Expression::SetRightHandSide@endlink 
            if the ExpressionCollection is owned by the part that owns the expression.  <br> License requirements : None */
        public: void Edit
        (
            NXOpen::Expression * expression /** The expression to be edited,
                         Note: if this expression is not owned by the part that owns
                         the ExpressionCollection, a new expression will be created
                         in the part that owns the ExpressionCollection */,
            const NXString & newRightHandSide /** What you want to change the expression to   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Edits an expression with units. Changing the units on an existing expression
            is only allowed when the expression is not referenced yet.

             <br> Note, if you do not change the units, there is no difference between this method and
            editing the expression via @link Expression::SetRightHandSide Expression::SetRightHandSide@endlink 
            if the ExpressionCollection is owned by the part that owns the expression.  <br>   <br> License requirements : None */
        public: void EditWithUnits
        (
            NXOpen::Expression * expression /** The expression to be edited,
                         Note: if this expression is not owned by the part that owns
                         the ExpressionCollection, a new expression will be created
                         in the part that owns the ExpressionCollection */,
            NXOpen::Unit * unitType /** units for the expression */,
            const NXString & newRightHandSide /** What you want to change the expression to   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Deletes an expression  <br> License requirements : None */
        public: void Delete
        (
            NXOpen::Expression * expression /** The expression to be deleted */
        );
        /** Finds the @link  Expression   Expression @endlink  with the given identifier as recorded in a journal.
            An object may not return the same value as its JournalIdentifier in different versions of
            the software. However newer versions of the software should find the same object when
            FindObject is passed older versions of its journal identifier. In general, this method
            should not be used in handwritten code and exists to support record and playback of journals.

            An exception will be thrown if no object can be found with the given journal identifier.  @return  Expression found  <br> License requirements : None */
        public: NXOpen::Expression * FindObject
        (
            const NXString & journalIdentifier /** Identifier to be found   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Imports expressions from a file. Input a file specification.  When calling this method, changes are not applied to the system
            until @link Update::DoUpdate Update::DoUpdate@endlink  is called.   <br> License requirements : None */
        public: void ImportFromFile
        (
            const NXString & fileName /** File name specification to import expressions from   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            NXOpen::ExpressionCollection::ImportMode importMode /** import mode */,
            bool* expModified /** TRUE if any expressions were affected by the import */,
            std::vector<NXString> & errorMessages /** translated list of error messages */
        );
        /** Exports the expressions to a text file, or, if 'file_name' is NULL,
            list the expressions in the listing window. Throws an exception
            if there is any error.
             <br>  NOTE: if the file already exists, an exception is thrown and the
                   file is not overwritten. <br>  <br> License requirements : None */
        public: void ExportToFile
        (
            NXOpen::ExpressionCollection::ExportMode exportMode /** export mode */,
            const NXString & fileName /** File name specification to export expressions into.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            NXOpen::ExpressionCollection::SortType sortType /** How to sort the exported expressions */
        );
        /** Returns a list of parts that are referenced from expressions in the part "owning_part". @return  array of part names  <br> License requirements : None */
        public: std::vector<NXString> GetInterpartReferences
        (
        );
        /** Removes the interpart references from a part. If a part name
            is given, then it removes the references to that part. If part_name
            is NULL, it removes all references to all parts.

             <br> References on the RHS are replaced by a numerical value, References
            on the LHS are deleted. E.g.  <br> 

                 <br> x = comp::len + z  --\> x = 3 + z <br> 

                 <br> comp::height=5  --\> (deleted) <br> 

             <br> The function returns TRUE is any references were removed, and FALSE
            otherwise.   <br>   @return  whether any changes were made  <br> License requirements : None */
        public: bool RemoveInterpartReferences
        (
            const NXString & partName /** Part name to remove references for   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Changes all of the references in the part "owning_part" from expressions
            in the part "old_part_name" to expressions in the part "new_part_name". <br> License requirements : None */
        public: void ChangeInterpartReferences
        (
            const NXString & oldPartName /** Part name whose references are being replaced   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            const NXString & newPartName /** New part name to reference   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Returns an array of visible expressions in the part.   @return  array of expressions  <br> License requirements : None */
        public: std::vector<NXOpen::Expression *> GetVisibleExpressions
        (
        );
        /** Changes the name of the expression.  <br> License requirements : None */
        public: void Rename
        (
            NXOpen::Expression * expression /** expression to be renamed */,
            const NXString & newName /** new name of the expression   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Changes the name of the expression without marking system expressions as user expressions.  <br> License requirements : None */
        public: void SystemRename
        (
            NXOpen::Expression * expression /** expression to be renamed */,
            const NXString & newName /** new name of the expression   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Creates a @link SuppressByExpressionBuilder SuppressByExpressionBuilder@endlink   @return  SuppressByExpressionBuilder object  <br> License requirements : None */
        public: NXOpen::SuppressByExpressionBuilder * CreateSuppressByExpressionBuilder
        (
        );
        public: virtual void initialize();
    };
}
#undef EXPORTLIBRARY
#endif
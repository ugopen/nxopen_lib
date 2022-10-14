/*******************************************************************************
                    Copyright (c) 2006 UGS Corp.
                 Unpublished - All rights reserved


*******************************************************************************/
#ifndef NXOpen_Callback_HXX_INCLUDED
#define NXOpen_Callback_HXX_INCLUDED

#ifdef _MSC_VER
#pragma once
#endif

#include <vector>
#include <typeinfo>

namespace NXOpen
{
    /** A base class for all NXOpen callback classes */
    class BaseCallback
    {
    public:
        /** BaseCallback destructor */
        virtual ~BaseCallback()
        {
        }
        /** Function interface for clone operation. Derived classes will define this function to implement a
            deep copy operation. */
        virtual BaseCallback *Clone() const = 0;
        /** Function interface for equality operation. */
        virtual bool Equals(const BaseCallback& other) const = 0;
    };

    /** Template base class for callbacks with no input arguments. The return type of the callback function is the template type Result. */
    template <class Result>
    class Callback0 : public BaseCallback
    {
    public:
        /** Return type of callback function */
        typedef Result ResultType;
        /** Callback0 destructor */
        virtual ~Callback0()
        {
        }
        /** Pure virtual function defining function call operator interface. Derived callback classes will implement this 
            function to invoke the callback function (or functions) attached to the callback class instance. */
        virtual Result operator() () const = 0;
    };


    /** Template class for callbacks with no input arguments. The return type of the callback function is the template type Result. */
    template <class Result>
    class Callback0Function : public Callback0<Result>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback0Function<Result> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (*FunctionType)();
        /** Constructor. */
        Callback0Function(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback function attached to this Callback0Function instance. */
        virtual Result operator()() const
        {
            return m_fn();
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        FunctionType m_fn;
    };

#if defined(_WIN32) && !defined(_WIN64)
    /** Template class for callbacks with no input arguments. The return type of the callback function is the template type Result. 
        The callback function is invoked using the __stdcall calling convention. */
    template <class Result>
    class Callback0StdCallFunction : public Callback0<Result>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback0StdCallFunction<Result> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (__stdcall *FunctionType)();
        /** Constructor. */
        Callback0StdCallFunction(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback function attached to this Callback0StdCallFunction instance. */
        virtual Result operator()() const
        {
            return m_fn();
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        FunctionType m_fn;
    };
#endif

    /** Template class for callbacks with no input arguments that are member functions of a class. Template type T is the class
        that the callback function is a member function of. The return type of the callback function is the template type Result. */
    template <class T, class Result>
    class Callback0MemberFunction : public Callback0<Result>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback0MemberFunction<T, Result> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (T::*FunctionType)();
        /** Constructor. */
        Callback0MemberFunction(T *object, FunctionType fn) : m_object(object), m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback member function attached to this Callback0MemberFunction instance. */
        virtual Result operator()() const
        {
            return (m_object->*m_fn)();
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                    m_object == static_cast<const MyClass &>(other).m_object && 
                    m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        T *m_object;
        FunctionType m_fn;
    };


    /** Template class for callbacks with no input arguments. This template class manages a list of callback functions. 
        The return type of the callback function is the template type Result. */
    template <class Result>
    class Callback0List : public Callback0<Result>
    {
    private:
        typedef Callback0<Result> BaseClass;
        typedef Callback0List<Result> MyClass;
        typedef std::vector<BaseClass *> FunctionVector;
        typedef typename FunctionVector::iterator iterator;
    public:
        /** Constructor */
        Callback0List() : m_functions()
        {
        }
        /** Function call operator for invoking callback functions in list. Callbacks are invoked in the order 
            they were added to the list. */
        virtual Result operator()() const
        {
            FunctionVector copy = m_functions;
            if (copy.size() == 0)
                throw "bom";
            for (typename FunctionVector::iterator it = copy.begin(); it != copy.end() - 1; ++it)
                (*(*it))();
            return (*copy.back())();
        }
        /** Function to add callback function to list of callback functions. */
        void Add(const BaseClass &fn)
        {
            m_functions.push_back(static_cast<BaseClass *>(fn.Clone()));
        }
        /** Function to remove the callback function from the list of callback functions. Uses the Equals method on the callback 
            function to find the matching callback function in the list. Finds the first matching callback function in the 
            list and removes it. */
        bool Remove(const BaseClass &fn)
        {
            for (typename FunctionVector::iterator it = m_functions.begin(); it != m_functions.end(); ++it)
                if ((*it)->Equals(fn))
                {
                    m_functions.erase(it);
                    return true;
                }
            return false;
        }
        /** Callback0List destructor. Deletes all the callbacks in the list of callbacks. */
        virtual ~Callback0List()
        {
            for (typename FunctionVector::iterator it = m_functions.begin(); it != m_functions.end(); ++it)
                delete *it;
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return false;
        }
    private:
        FunctionVector m_functions;
    };

    /** Helper template function to create an instance of a Callback0MemberFunction. The template type T is the class
        that the callback is a member function of. The return type of the callback function is the template type Result. */
    template <class T, class Result>
    Callback0MemberFunction<T, Result> make_callback(T *object, Result (T::*fn)())
    {
        return Callback0MemberFunction<T, Result>(object, fn);
    }

    /** Helper template function to create an instance of a Callback0Function. */
    template <class Result>
    Callback0Function<Result> make_callback(Result (*fn)())
    {
        return Callback0Function<Result>(fn);
    }

#if defined(_WIN32) && !defined(_WIN64)
    /** Helper template function to create an instance of a Callback0StdCallFunction. The callback function is invoked 
        using the __stdcall calling convention. The return type of the callback function is the template type Result. */
    template <class Result>
    Callback0StdCallFunction<Result> make_callback(Result (__stdcall *fn)())
    {
        return Callback0StdCallFunction<Result>(fn);
    }
#endif

    /** Template base class for callbacks with one input argument. The return type of the callback function is the template type Result. */
    template <class Result, class Arg1>
    class Callback1 : public BaseCallback
    {
    public:
        /** Return type of callback function */
        typedef Result ResultType;
        /** Type of first input argument of callback function */
        typedef Arg1 Arg1Type;
        virtual ~Callback1()
        {
        }
        /** Pure virtual function defining function call operator interface. Derived callback classes will implement this 
            function to invoke the callback function (or functions) attached to the callback class instance. */
        virtual Result operator() (Arg1 a1) const = 0;
    };

    /** Template class for callbacks with one input argument. The return type of the callback function is the template type Result. */
    template <class Result, class Arg1>
    class Callback1Function : public Callback1<Result, Arg1>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback1Function<Result, Arg1> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (*FunctionType)(Arg1);
        /** Constructor. */
        Callback1Function(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback function attached to this Callback1Function instance. */
        virtual Result operator()(Arg1 a1) const
        {
            return m_fn(a1);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        FunctionType m_fn;
    };

#if defined(_WIN32) && !defined(_WIN64)
    /** Template class for callbacks with one input argument. The return type of the callback function is the template type Result. 
        The callback function is invoked using the __stdcall calling convention. */
    template <class Result, class Arg1>
    class Callback1StdCallFunction : public Callback1<Result, Arg1>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback1StdCallFunction<Result, Arg1> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (__stdcall *FunctionType)(Arg1);
        /** Constructor. */
        Callback1StdCallFunction(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback function attached to this Callback1StdCallFunction instance. */
        virtual Result operator()(Arg1 a1) const
        {
            return m_fn(a1);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        FunctionType m_fn;
    };
#endif

    /** Template class for callbacks with one input argument that are member functions of a class. Template type T is the class
        that the callback function is a member function of. The return type of the callback function is the template type Result. */
    template <class T, class Result, class Arg1>
    class Callback1MemberFunction : public Callback1<Result, Arg1>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback1MemberFunction<T, Result, Arg1> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (T::*FunctionType)(Arg1);
        /** Constructor. */
        Callback1MemberFunction(T *object, FunctionType fn) : m_object(object), m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback member function attached to this Callback1MemberFunction instance. */
        virtual Result operator()(Arg1 a1) const
        {
            return (m_object->*m_fn)(a1);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                    m_object == static_cast<const MyClass &>(other).m_object && 
                    m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        T *m_object;
        FunctionType m_fn;
    };


    /** Template class for callbacks with one input argument. This template class manages a list of callback functions. 
        The return type of the callback function is the template type Result. */
    template <class Result, class Arg1>
    class Callback1List : public Callback1<Result, Arg1>
    {
    private:
        typedef Callback1<Result, Arg1> BaseClass;
        typedef Callback1List<Result, Arg1> MyClass;
        typedef std::vector<BaseClass *> FunctionVector;
        typedef typename FunctionVector::iterator iterator;
    public:
        /** Constructor. */
        Callback1List() : m_functions()
        {
        }
        /** Function call operator for invoking callback functions in list. Callbacks are invoked in the order 
            they were added to the list. */
        virtual Result operator()(Arg1 a1) const
        {
            FunctionVector copy = m_functions;
            if (copy.size() == 0)
                throw "bom";
            for (typename FunctionVector::iterator it = copy.begin(); it != copy.end() - 1; ++it)
                (*(*it))(a1);
            return (*copy.back())(a1);
        }
        /** Function to add callback function to list of callback functions. */
        void Add(const BaseClass &fn)
        {
            m_functions.push_back(static_cast<BaseClass *>(fn.Clone()));
        }
        /** Function to remove the callback function from the list of callback functions. Uses the Equals method on the callback 
            function to find the matching callback function in the list. Finds the first matching callback function in the 
            list and removes it. */
        bool Remove(const BaseClass &fn)
        {
            for (typename FunctionVector::iterator it = m_functions.begin(); it != m_functions.end(); ++it)
                if ((*it)->Equals(fn))
                {
                    m_functions.erase(it);
                    return true;
                }
            return false;
        }
        /** Callback1List destructor. Deletes all the callbacks in the list of callbacks. */
        virtual ~Callback1List()
        {
            for (typename FunctionVector::iterator it = m_functions.begin(); it != m_functions.end(); ++it)
                delete *it;
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return false;
        }
    private:
        FunctionVector m_functions;
    };

    //template <class Result, class Arg1>
    //class Callback1List : public Callback1<Result, Arg1>
    //{
    //private:
    //    typedef Callback1<Result, Arg1> BaseClass;
    //    typedef Callback1List<Result, Arg1> MyClass;
    //    typedef std::vector<BaseClass *> FunctionVector;
    //    typedef typename FunctionVector::iterator iterator;
    //public:
    //    Callback1List() : m_functions()
    //    {
    //    }
    //    virtual void operator()(Arg1 a1) const
    //    {
    //        FunctionVector copy = m_functions;
    //        if (copy.size() == 0)
    //            return;
    //        for (typename FunctionVector::iterator it = copy.begin(); it != copy.end() - 1; ++it)
    //            (*(*it))(a1);
    //        return;
    //    }
    //    void Add(const BaseClass &fn)
    //    {
    //        m_functions.push_back(static_cast<BaseClass *>(fn.Clone()));
    //    }
    //    bool Remove(const BaseClass &fn)
    //    {
    //        for (typename FunctionVector::iterator it = m_functions.begin(); it != m_functions.end(); ++it)
    //            if ((*it)->Equals(fn))
    //            {
    //                m_functions.erase(it);
    //                return true;
    //            }
    //        return false;
    //    }
    //    ~Callback1List()
    //    {
    //        for (typename FunctionVector::iterator it = m_functions.begin(); it != m_functions.end(); ++it)
    //            delete *it;
    //    }
    //    virtual BaseCallback *Clone() const
    //    {
    //        return new MyClass(*this);
    //    }
    //    virtual bool Equals(const BaseCallback& other) const
    //    {
    //        return false;
    //    }
    //private:
    //    FunctionVector m_functions;
    //};

    /** Helper template function to create an instance of a Callback1MemberFunction. The template type T is the class
        that the callback is a member function of. The return type of the callback function is the template type Result. */
    template <class T, class Result, class Arg1>
    Callback1MemberFunction<T, Result, Arg1> make_callback(T *object, Result (T::*fn)(Arg1))
    {
        return Callback1MemberFunction<T, Result, Arg1>(object, fn);
    }

    /** Helper template function to create an instance of a Callback1Function. The return type of the callback function is the template type Result. */
    template <class Result, class Arg1>
    Callback1Function<Result, Arg1> make_callback(Result (*fn)(Arg1))
    {
        return Callback1Function<Result, Arg1>(fn);
    }

    //template <class Result, class Arg1>
    //Callback1Function<Result ( Arg1 ) > make_callback(Result (*fn)(Arg1))
    //{
    //    return Callback1Function<Result ( Arg1 ) >(fn);
    //}

#if defined(_WIN32) && !defined(_WIN64)
    template <class Result, class Arg1>
    Callback1StdCallFunction<Result, Arg1> make_callback(Result (__stdcall *fn)(Arg1))
    {
        return Callback1StdCallFunction<Result, Arg1>(fn);
    }
#endif

    /** Template base class for callbacks with two input arguments. The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2>
    class Callback2 : public BaseCallback
    {
    public:
        /** Return type of callback function */
        typedef Result ResultType;
        /** Type of first input argument of callback function */
        typedef Arg1 Arg1Type;
        /** Type of second input argument of callback function */
        typedef Arg2 Arg2Type;
        virtual ~Callback2()
        {
        }
        /** Pure virtual function defining function call operator interface. Derived callback classes will implement this 
            function to invoke the callback function (or functions) attached to the callback class instance. */
        virtual Result operator() (Arg1 a1, Arg2 a2) const = 0;
    };

    /** Template class for callbacks with two input arguments. The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2>
    class Callback2Function : public Callback2<Result, Arg1, Arg2>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback2Function<Result, Arg1, Arg2> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (*FunctionType)(Arg1, Arg2);
        /** Constructor. */
        Callback2Function(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback function attached to this Callback2Function instance. */
        virtual Result operator()(Arg1 a1, Arg2 a2) const
        {
            return m_fn(a1, a2);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        FunctionType m_fn;
    };

#if defined(_WIN32) && !defined(_WIN64)
    /** Template class for callbacks with two input arguments. The return type of the callback function is the template type Result. 
        The callback function is invoked using the __stdcall calling convention. */
    template <class Result, class Arg1, class Arg2>
    class Callback2StdCallFunction : public Callback2<Result, Arg1, Arg2>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback2StdCallFunction<Result, Arg1, Arg2> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (__stdcall *FunctionType)(Arg1, Arg2);
        /** Constructor. */
        Callback2StdCallFunction(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback function attached to this Callback2StdCallFunction instance. */
        virtual Result operator()(Arg1 a1, Arg2 a2) const
        {
            return m_fn(a1, a2);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        FunctionType m_fn;
    };
#endif

    /** Template class for callbacks with two input arguments that are member functions of a class. Template type T is the class
        that the callback function is a member function of. The return type of the callback function is the template type Result. */
    template <class T, class Result, class Arg1, class Arg2>
    class Callback2MemberFunction : public Callback2<Result, Arg1, Arg2>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback2MemberFunction<T, Result, Arg1, Arg2> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (T::*FunctionType)(Arg1, Arg2);
        /** Constructor. */
        Callback2MemberFunction(T *object, FunctionType fn) : m_object(object), m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback member function attached to this Callback2MemberFunction instance. */
        virtual Result operator()(Arg1 a1, Arg2 a2) const
        {
            return (m_object->*m_fn)(a1, a2);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                    m_object == static_cast<const MyClass &>(other).m_object && 
                    m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        T *m_object;
        FunctionType m_fn;
    };


    /** Template class for callbacks with two input arguments. This template class manages a list of callback functions. 
        The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2>
    class Callback2List : public Callback2<Result, Arg1, Arg2>
    {
    private:
        typedef Callback2<Result, Arg1, Arg2> BaseClass;
        typedef Callback2List<Result, Arg1, Arg2> MyClass;
        typedef std::vector<BaseClass *> FunctionVector;
        typedef typename FunctionVector::iterator iterator;
    public:
        /** Constructor. */
        Callback2List() : m_functions()
        {
        }
        /** Function call operator for invoking callback functions in list. Callbacks are invoked in the order 
            they were added to the list. */
        virtual Result operator()(Arg1 a1, Arg2 a2) const
        {
            FunctionVector copy = m_functions;
            if (copy.size() == 0)
                throw "bom";
            for (typename FunctionVector::iterator it = copy.begin(); it != copy.end() - 1; ++it)
                (*(*it))(a1, a2);
            return (*copy.back())(a1, a2);
        }
        /** Function to add callback function to list of callback functions. */
        void Add(const BaseClass &fn)
        {
            m_functions.push_back(static_cast<BaseClass *>(fn.Clone()));
        }
        /** Function to remove the callback function from the list of callback functions. Uses the Equals method on the callback 
            function to find the matching callback function in the list. Finds the first matching callback function in the 
            list and removes it. */
        bool Remove(const BaseClass &fn)
        {
            for (typename FunctionVector::iterator it = m_functions.begin(); it != m_functions.end(); ++it)
                if ((*it)->Equals(fn))
                {
                    m_functions.erase(it);
                    return true;
                }
            return false;
        }
        /** Callback2List destructor. Deletes all the callbacks in the list of callbacks. */
        virtual ~Callback2List()
        {
            for (typename FunctionVector::iterator it = m_functions.begin(); it != m_functions.end(); ++it)
                delete *it;
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return false;
        }
    private:
        FunctionVector m_functions;
    };

    /** Helper template function to create an instance of a Callback2MemberFunction. The template type T is the class
        that the callback is a member function of. The return type of the callback function is the template type Result. */
    template <class T, class Result, class Arg1, class Arg2>
    Callback2MemberFunction<T, Result, Arg1, Arg2> make_callback(T *object, Result (T::*fn)(Arg1, Arg2))
    {
        return Callback2MemberFunction<T, Result, Arg1, Arg2>(object, fn);
    }

    /** Helper template function to create an instance of a Callback2Function. */
    template <class Result, class Arg1, class Arg2>
    Callback2Function<Result, Arg1, Arg2> make_callback(Result (*fn)(Arg1, Arg2))
    {
        return Callback2Function<Result, Arg1, Arg2>(fn);
    }

#if defined(_WIN32) && !defined(_WIN64)
    template <class Result, class Arg1, class Arg2>
    Callback2StdCallFunction<Result, Arg1, Arg2> make_callback(Result (__stdcall *fn)(Arg1, Arg2))
    {
        return Callback2StdCallFunction<Result, Arg1, Arg2>(fn);
    }
#endif

    /** Template base class for callbacks with three input arguments. The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3>
    class Callback3 : public BaseCallback
    {
    public:
        /** Return type of callback function */
        typedef Result ResultType;
        /** Type of first input argument of callback function */
        typedef Arg1 Arg1Type;
        /** Type of second input argument of callback function */
        typedef Arg2 Arg2Type;
        /** Type of third input argument of callback function */
        typedef Arg3 Arg3Type;
        virtual ~Callback3()
        {
        }
        /** Pure virtual function defining function call operator interface. Derived callback classes will implement this 
            function to invoke the callback function (or functions) attached to the callback class instance. */
        virtual Result operator() (Arg1 a1, Arg2 a2, Arg3 a3) const = 0;
    };

    /** Template class for callbacks with three input arguments. The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3>
    class Callback3Function : public Callback3<Result, Arg1, Arg2, Arg3>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback3Function<Result, Arg1, Arg2, Arg3> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (*FunctionType)(Arg1, Arg2, Arg3);
        /** Constructor. */
        Callback3Function(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback function attached to this Callback3Function instance. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3) const
        {
            return m_fn(a1, a2, a3);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        FunctionType m_fn;
    };

#if defined(_WIN32) && !defined(_WIN64)
    template <class Result, class Arg1, class Arg2, class Arg3>
    class Callback3StdCallFunction : public Callback3<Result, Arg1, Arg2, Arg3>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback3StdCallFunction<Result, Arg1, Arg2, Arg3> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (__stdcall *FunctionType)(Arg1, Arg2, Arg3);
        /** Constructor. */
        Callback3StdCallFunction(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback function attached to this Callback3StdCallFunction instance. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3) const
        {
            return m_fn(a1, a2, a3);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        FunctionType m_fn;
    };
#endif

    /** Template class for callbacks with three input arguments that are member functions of a class. Template type T is the class
        that the callback function is a member function of. The return type of the callback function is the template type Result. */
    template <class T, class Result, class Arg1, class Arg2, class Arg3>
    class Callback3MemberFunction : public Callback3<Result, Arg1, Arg2, Arg3>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback3MemberFunction<T, Result, Arg1, Arg2, Arg3> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (T::*FunctionType)(Arg1, Arg2, Arg3);
        /** Constructor. */
        Callback3MemberFunction(T *object, FunctionType fn) : m_object(object), m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback member function attached to this Callback3MemberFunction instance. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3) const
        {
            return (m_object->*m_fn)(a1, a2, a3);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                    m_object == static_cast<const MyClass &>(other).m_object && 
                    m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        T *m_object;
        FunctionType m_fn;
    };


    /** Template class for callbacks with three input arguments. This template class manages a list of callback functions. 
        The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3>
    class Callback3List : public Callback3<Result, Arg1, Arg2, Arg3>
    {
    private:
        typedef Callback3<Result, Arg1, Arg2, Arg3> BaseClass;
        typedef Callback3List<Result, Arg1, Arg2, Arg3> MyClass;
        typedef std::vector<BaseClass *> FunctionVector;
        typedef typename FunctionVector::iterator iterator;
    public:
        /** Constructor. */
        Callback3List() : m_functions()
        {
        }
        /** Function call operator for invoking callback functions in list. Callbacks are invoked in the order 
            they were added to the list. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3) const
        {
            FunctionVector copy = m_functions;
            if (copy.size() == 0)
                throw "bom";
            for (typename FunctionVector::iterator it = copy.begin(); it != copy.end() - 1; ++it)
                (*(*it))(a1, a2, a3);
            return (*copy.back())(a1, a2, a3);
        }
        /** Function to add callback function to list of callback functions. */
        void Add(const BaseClass &fn)
        {
            m_functions.push_back(static_cast<BaseClass *>(fn.Clone()));
        }
        /** Function to remove the callback function from the list of callback functions. Uses the Equals method on the callback 
            function to find the matching callback function in the list. Finds the first matching callback function in the 
            list and removes it. */
        bool Remove(const BaseClass &fn)
        {
            for (typename FunctionVector::iterator it = m_functions.begin(); it != m_functions.end(); ++it)
                if ((*it)->Equals(fn))
                {
                    m_functions.erase(it);
                    return true;
                }
            return false;
        }
        /** Callback3List destructor. Deletes all the callbacks in the list of callbacks. */
        virtual ~Callback3List()
        {
            for (typename FunctionVector::iterator it = m_functions.begin(); it != m_functions.end(); ++it)
                delete *it;
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return false;
        }
    private:
        FunctionVector m_functions;
    };

    /** Helper template function to create an instance of a Callback3MemberFunction. The template type T is the class
        that the callback is a member function of. The return type of the callback function is the template type Result. */
    template <class T, class Result, class Arg1, class Arg2, class Arg3>
    Callback3MemberFunction<T, Result, Arg1, Arg2, Arg3> make_callback(T *object, Result (T::*fn)(Arg1, Arg2, Arg3))
    {
        return Callback3MemberFunction<T, Result, Arg1, Arg2, Arg3>(object, fn);
    }

    /** Helper template function to create an instance of a Callback3Function. The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3>
    Callback3Function<Result, Arg1, Arg2, Arg3> make_callback(Result (*fn)(Arg1, Arg2, Arg3))
    {
        return Callback3Function<Result, Arg1, Arg2, Arg3>(fn);
    }

#if defined(_WIN32) && !defined(_WIN64)
    template <class Result, class Arg1, class Arg2, class Arg3>
    Callback3StdCallFunction<Result, Arg1, Arg2, Arg3> make_callback(Result (__stdcall *fn)(Arg1, Arg2, Arg3))
    {
        return Callback3StdCallFunction<Result, Arg1, Arg2, Arg3>(fn);
    }
#endif

    /** Template base class for callbacks with four input arguments. The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4>
    class Callback4 : public BaseCallback
    {
    public:
        /** Return type of callback function */
        typedef Result ResultType;
        /** Type of first input argument of callback function */
        typedef Arg1 Arg1Type;
        /** Type of second input argument of callback function */
        typedef Arg2 Arg2Type;
        /** Type of third input argument of callback function */
        typedef Arg3 Arg3Type;
        /** Type of fourth input argument of callback function */
        typedef Arg4 Arg4Type;
        virtual ~Callback4()
        {
        }
        /** Pure virtual function defining function call operator interface. Derived callback classes will implement this 
            function to invoke the callback function (or functions) attached to the callback class instance. */
        virtual Result operator() (Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4) const = 0;
    };

    /** Template class for callbacks with four input arguments. The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4>
    class Callback4Function : public Callback4<Result, Arg1, Arg2, Arg3, Arg4>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback4Function<Result, Arg1, Arg2, Arg3, Arg4> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (*FunctionType)(Arg1, Arg2, Arg3, Arg4);
        /** Constructor. */
        Callback4Function(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback function attached to this Callback4Function instance. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4) const
        {
            return m_fn(a1, a2, a3, a4);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        FunctionType m_fn;
    };

#if defined(_WIN32) && !defined(_WIN64)
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4>
    class Callback4StdCallFunction : public Callback4<Result, Arg1, Arg2, Arg3, Arg4>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback4StdCallFunction<Result, Arg1, Arg2, Arg3, Arg4> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (__stdcall *FunctionType)(Arg1, Arg2, Arg3, Arg4);
        /** Constructor. */
        Callback4StdCallFunction(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback function attached to this Callback4StdCallFunction instance. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4) const
        {
            return m_fn(a1, a2, a3, a4);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        FunctionType m_fn;
    };
#endif

    /** Template class for callbacks with four input arguments that are member functions of a class. Template type T is the class
        that the callback function is a member function of. The return type of the callback function is the template type Result. */
    template <class T, class Result, class Arg1, class Arg2, class Arg3, class Arg4>
    class Callback4MemberFunction : public Callback4<Result, Arg1, Arg2, Arg3, Arg4>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback4MemberFunction<T, Result, Arg1, Arg2, Arg3, Arg4> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (T::*FunctionType)(Arg1, Arg2, Arg3, Arg4);
        /** Constructor. */
        Callback4MemberFunction(T *object, FunctionType fn) : m_object(object), m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback member function attached to this Callback4MemberFunction instance. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4) const
        {
            return (m_object->*m_fn)(a1, a2, a3, a4);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                    m_object == static_cast<const MyClass &>(other).m_object && 
                    m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        T *m_object;
        FunctionType m_fn;
    };


    /** Template class for callbacks with four input arguments. This template class manages a list of callback functions. 
        The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4>
    class Callback4List : public Callback4<Result, Arg1, Arg2, Arg3, Arg4>
    {
    private:
        typedef Callback4<Result, Arg1, Arg2, Arg3, Arg4> BaseClass;
        typedef Callback4List<Result, Arg1, Arg2, Arg3, Arg4> MyClass;
        typedef std::vector<BaseClass *> FunctionVector;
        typedef typename FunctionVector::iterator iterator;
    public:
        /** Constructor. */
        Callback4List() : m_functions()
        {
        }
        /** Function call operator for invoking callback functions in list. Callbacks are invoked in the order 
            they were added to the list. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4) const
        {
            FunctionVector copy = m_functions;
            if (copy.size() == 0)
                throw "bom";
            for (typename FunctionVector::iterator it = copy.begin(); it != copy.end() - 1; ++it)
                (*(*it))(a1, a2, a3, a4);
            return (*copy.back())(a1, a2, a3, a4);
        }
        /** Function to add callback function to list of callback functions. */
        void Add(const BaseClass &fn)
        {
            m_functions.push_back(static_cast<BaseClass *>(fn.Clone()));
        }
        /** Function to remove the callback function from the list of callback functions. Uses the Equals method on the callback 
            function to find the matching callback function in the list. Finds the first matching callback function in the 
            list and removes it. */
        bool Remove(const BaseClass &fn)
        {
            for (typename FunctionVector::iterator it = m_functions.begin(); it != m_functions.end(); ++it)
                if ((*it)->Equals(fn))
                {
                    m_functions.erase(it);
                    return true;
                }
            return false;
        }
        /** Callback4List destructor. Deletes all the callbacks in the list of callbacks. */
        virtual ~Callback4List()
        {
            for (typename FunctionVector::iterator it = m_functions.begin(); it != m_functions.end(); ++it)
                delete *it;
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return false;
        }
    private:
        FunctionVector m_functions;
    };

    /** Helper template function to create an instance of a Callback4MemberFunction. The template type T is the class
        that the callback is a member function of. The return type of the callback function is the template type Result. */
    template <class T, class Result, class Arg1, class Arg2, class Arg3, class Arg4>
    Callback4MemberFunction<T, Result, Arg1, Arg2, Arg3, Arg4> make_callback(T *object, Result (T::*fn)(Arg1, Arg2, Arg3, Arg4))
    {
        return Callback4MemberFunction<T, Result, Arg1, Arg2, Arg3, Arg4>(object, fn);
    }

    /** Helper template function to create an instance of a Callback4Function. The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4>
    Callback4Function<Result, Arg1, Arg2, Arg3, Arg4> make_callback(Result (*fn)(Arg1, Arg2, Arg3, Arg4))
    {
        return Callback4Function<Result, Arg1, Arg2, Arg3, Arg4>(fn);
    }

#if defined(_WIN32) && !defined(_WIN64)
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4>
    Callback4StdCallFunction<Result, Arg1, Arg2, Arg3, Arg4> make_callback(Result (__stdcall *fn)(Arg1, Arg2, Arg3, Arg4))
    {
        return Callback4StdCallFunction<Result, Arg1, Arg2, Arg3, Arg4>(fn);
    }
#endif

    /** Template base class for callbacks with five input arguments. The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5>
    class Callback5 : public BaseCallback
    {
    public:
        /** Return type of callback function */
        typedef Result ResultType;
        /** Type of first input argument of callback function */
        typedef Arg1 Arg1Type;
        /** Type of second input argument of callback function */
        typedef Arg2 Arg2Type;
        /** Type of third input argument of callback function */
        typedef Arg3 Arg3Type;
        /** Type of fourth input argument of callback function */
        typedef Arg4 Arg4Type;
        /** Type of fifth input argument of callback function */
        typedef Arg5 Arg5Type;
        virtual ~Callback5()
        {
        }
        /** Pure virtual function defining function call operator interface. Derived callback classes will implement this 
            function to invoke the callback function (or functions) attached to the callback class instance. */
        virtual Result operator() (Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4, Arg5 a5) const = 0;
    };

    /** Template class for callbacks with five input arguments. The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5>
    class Callback5Function : public Callback5<Result, Arg1, Arg2, Arg3, Arg4, Arg5>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback5Function<Result, Arg1, Arg2, Arg3, Arg4, Arg5> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (*FunctionType)(Arg1, Arg2, Arg3, Arg4, Arg5);
        /** Constructor. */
        Callback5Function(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback function attached to this Callback5Function instance. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4, Arg5 a5) const
        {
            return m_fn(a1, a2, a3, a4, a5);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        FunctionType m_fn;
    };

#if defined(_WIN32) && !defined(_WIN64)
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5>
    class Callback5StdCallFunction : public Callback5<Result, Arg1, Arg2, Arg3, Arg4, Arg5>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback5StdCallFunction<Result, Arg1, Arg2, Arg3, Arg4, Arg5> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (__stdcall *FunctionType)(Arg1, Arg2, Arg3, Arg4, Arg5);
        /** Constructor. */
        Callback5StdCallFunction(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback function attached to this Callback5StdCallFunction instance. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4, Arg5 a5) const
        {
            return m_fn(a1, a2, a3, a4, a5);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        FunctionType m_fn;
    };
#endif

    /** Template class for callbacks with five input arguments that are member functions of a class. Template type T is the class
        that the callback function is a member function of. The return type of the callback function is the template type Result. */
    template <class T, class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5>
    class Callback5MemberFunction : public Callback5<Result, Arg1, Arg2, Arg3, Arg4, Arg5>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback5MemberFunction<T, Result, Arg1, Arg2, Arg3, Arg4, Arg5> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (T::*FunctionType)(Arg1, Arg2, Arg3, Arg4, Arg5);
        /** Constructor. */
        Callback5MemberFunction(T *object, FunctionType fn) : m_object(object), m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback member function attached to this Callback5MemberFunction instance. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4, Arg5 a5) const
        {
            return (m_object->*m_fn)(a1, a2, a3, a4, a5);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                    m_object == static_cast<const MyClass &>(other).m_object && 
                    m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        T *m_object;
        FunctionType m_fn;
    };


    /** Template class for callbacks with five input arguments. This template class manages a list of callback functions. 
        The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5>
    class Callback5List : public Callback5<Result, Arg1, Arg2, Arg3, Arg4, Arg5>
    {
    private:
        typedef Callback5<Result, Arg1, Arg2, Arg3, Arg4, Arg5> BaseClass;
        typedef Callback5List<Result, Arg1, Arg2, Arg3, Arg4, Arg5> MyClass;
        typedef std::vector<BaseClass *> FunctionVector;
        typedef typename FunctionVector::iterator iterator;
    public:
        /** Constructor. */
        Callback5List() : m_functions()
        {
        }
        /** Function call operator for invoking callback functions in list. Callbacks are invoked in the order 
            they were added to the list. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4, Arg5 a5) const
        {
            FunctionVector copy = m_functions;
            if (copy.size() == 0)
                throw "bom";
            for (typename FunctionVector::iterator it = copy.begin(); it != copy.end() - 1; ++it)
                (*(*it))(a1, a2, a3, a4, a5);
            return (*copy.back())(a1, a2, a3, a4);
        }
        /** Function to add callback function to list of callback functions. */
        void Add(const BaseClass &fn)
        {
            m_functions.push_back(static_cast<BaseClass *>(fn.Clone()));
        }
        /** Function to remove the callback function from the list of callback functions. Uses the Equals method on the callback 
            function to find the matching callback function in the list. Finds the first matching callback function in the 
            list and removes it. */
        bool Remove(const BaseClass &fn)
        {
            for (typename FunctionVector::iterator it = m_functions.begin(); it != m_functions.end(); ++it)
                if ((*it)->Equals(fn))
                {
                    m_functions.erase(it);
                    return true;
                }
            return false;
        }
        /** Callback5List destructor. Deletes all the callbacks in the list of callbacks. */
        virtual ~Callback5List()
        {
            for (typename FunctionVector::iterator it = m_functions.begin(); it != m_functions.end(); ++it)
                delete *it;
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return false;
        }
    private:
        FunctionVector m_functions;
    };

    /** Helper template function to create an instance of a Callback5MemberFunction. The template type T is the class
        that the callback is a member function of. The return type of the callback function is the template type Result. */
    template <class T, class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5>
    Callback5MemberFunction<T, Result, Arg1, Arg2, Arg3, Arg4, Arg5> make_callback(T *object, Result (T::*fn)(Arg1, Arg2, Arg3, Arg4, Arg5))
    {
        return Callback5MemberFunction<T, Result, Arg1, Arg2, Arg3, Arg4, Arg5>(object, fn);
    }

    /** Helper template function to create an instance of a Callback5Function. The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5>
    Callback5Function<Result, Arg1, Arg2, Arg3, Arg4, Arg5> make_callback(Result (*fn)(Arg1, Arg2, Arg3, Arg4, Arg5))
    {
        return Callback5Function<Result, Arg1, Arg2, Arg3, Arg4, Arg5>(fn);
    }

#if defined(_WIN32) && !defined(_WIN64)
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5>
    Callback5StdCallFunction<Result, Arg1, Arg2, Arg3, Arg4, Arg5> make_callback(Result (__stdcall *fn)(Arg1, Arg2, Arg3, Arg4, Arg5))
    {
        return Callback5StdCallFunction<Result, Arg1, Arg2, Arg3, Arg4, Arg5>(fn);
    }
#endif
//=========Callback6========

    /** Template base class for callbacks with six input arguments. The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6>
    class Callback6 : public BaseCallback
    {
    public:
        /** Return type of callback function */
        typedef Result ResultType;
        /** Type of first input argument of callback function */
        typedef Arg1 Arg1Type;
        /** Type of second input argument of callback function */
        typedef Arg2 Arg2Type;
        /** Type of third input argument of callback function */
        typedef Arg3 Arg3Type;
        /** Type of fourth input argument of callback function */
        typedef Arg4 Arg4Type;
        /** Type of fifth input argument of callback function */
        typedef Arg5 Arg5Type;
        /** Type of sixth input argument of callback function */
        typedef Arg6 Arg6Type;
                
        virtual ~Callback6()
        {
        }
        /** Pure virtual function defining function call operator interface. Derived callback classes will implement this 
            function to invoke the callback function (or functions) attached to the callback class instance. */
        virtual Result operator() (Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4, Arg5 a5, Arg6 a6) const = 0;
    };

    /** Template class for callbacks with six input arguments. The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6>
    class Callback6Function : public Callback6<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback6Function<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (*FunctionType)(Arg1, Arg2, Arg3, Arg4, Arg5, Arg6);
        /** Constructor. */
        Callback6Function(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback function attached to this Callback6Function instance. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4, Arg5 a5, Arg6 a6) const
        {
            return m_fn(a1, a2, a3, a4, a5, a6);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        FunctionType m_fn;
    };

#if defined(_WIN32) && !defined(_WIN64)
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6>
    class Callback6StdCallFunction : public Callback6<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback6StdCallFunction<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (__stdcall *FunctionType)(Arg1, Arg2, Arg3, Arg4, Arg5, Arg6);
        /** Constructor. */
        Callback6StdCallFunction(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback function attached to this Callback6StdCallFunction instance. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4, Arg5 a5, Arg6 a6) const
        {
            return m_fn(a1, a2, a3, a4, a5, a6);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        FunctionType m_fn;
    };
#endif

    /** Template class for callbacks with six input arguments that are member functions of a class. Template type T is the class
        that the callback function is a member function of. The return type of the callback function is the template type Result. */
    template <class T, class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6>
    class Callback6MemberFunction : public Callback6<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback6MemberFunction<T, Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (T::*FunctionType)(Arg1, Arg2, Arg3, Arg4, Arg5, Arg6);
        /** Constructor. */
        Callback6MemberFunction(T *object, FunctionType fn) : m_object(object), m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback member function attached to this Callback6MemberFunction instance. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4, Arg5 a5, Arg6 a6) const
        {
            return (m_object->*m_fn)(a1, a2, a3, a4, a5, a6);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                    m_object == static_cast<const MyClass &>(other).m_object && 
                    m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        T *m_object;
        FunctionType m_fn;
    };


    /** Template class for callbacks with six input arguments. This template class manages a list of callback functions. 
        The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6>
    class Callback6List : public Callback6<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6>
    {
    private:
        typedef Callback6<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6> BaseClass;
        typedef Callback6List<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6> MyClass;
        typedef std::vector<BaseClass *> FunctionVector;
        typedef typename FunctionVector::iterator iterator;
    public:
        /** Constructor. */
        Callback6List() : m_functions()
        {
        }
        /** Function call operator for invoking callback functions in list. Callbacks are invoked in the order 
            they were added to the list. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4, Arg5 a5, Arg6 a6) const
        {
            FunctionVector copy = m_functions;
            if (copy.size() == 0)
                throw "bom";
            for (typename FunctionVector::iterator it = copy.begin(); it != copy.end() - 1; ++it)
                (*(*it))(a1, a2, a3, a4, a5, a6);
            return (*copy.back())(a1, a2, a3, a4, a5, a6);
        }
        /** Function to add callback function to list of callback functions. */
        void Add(const BaseClass &fn)
        {
            m_functions.push_back(static_cast<BaseClass *>(fn.Clone()));
        }
        /** Function to remove the callback function from the list of callback functions. Uses the Equals method on the callback 
            function to find the matching callback function in the list. Finds the first matching callback function in the 
            list and removes it. */
        bool Remove(const BaseClass &fn)
        {
            for (typename FunctionVector::iterator it = m_functions.begin(); it != m_functions.end(); ++it)
                if ((*it)->Equals(fn))
                {
                    m_functions.erase(it);
                    return true;
                }
            return false;
        }
        /** Callback6List destructor. Deletes all the callbacks in the list of callbacks. */
        virtual ~Callback6List()
        {
            for (typename FunctionVector::iterator it = m_functions.begin(); it != m_functions.end(); ++it)
                delete *it;
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return false;
        }
    private:
        FunctionVector m_functions;
    };

    /** Helper template function to create an instance of a Callback6MemberFunction. The template type T is the class
        that the callback is a member function of. The return type of the callback function is the template type Result. */
    template <class T, class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6>
    Callback6MemberFunction<T, Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6> make_callback(T *object, Result (T::*fn)(Arg1, Arg2, Arg3, Arg4, Arg5, Arg6))
    {
        return Callback6MemberFunction<T, Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6>(object, fn);
    }

    /** Helper template function to create an instance of a Callback6Function. The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6>
    Callback6Function<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6> make_callback(Result (*fn)(Arg1, Arg2, Arg3, Arg4, Arg5, Arg6))
    {
        return Callback6Function<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6>(fn);
    }

#if defined(_WIN32) && !defined(_WIN64)
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6>
    Callback6StdCallFunction<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6> make_callback(Result (__stdcall *fn)(Arg1, Arg2, Arg3, Arg4, Arg5, Arg6))
    {
        return Callback6StdCallFunction<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6>(fn);
    }
#endif

//=========Callback7========

    /** Template base class for callbacks with seven input arguments. The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6, class Arg7>
    class Callback7 : public BaseCallback
    {
    public:
        /** Return type of callback function */
        typedef Result ResultType;
        /** Type of first input argument of callback function */
        typedef Arg1 Arg1Type;
        /** Type of second input argument of callback function */
        typedef Arg2 Arg2Type;
        /** Type of third input argument of callback function */
        typedef Arg3 Arg3Type;
        /** Type of fourth input argument of callback function */
        typedef Arg4 Arg4Type;
        /** Type of fifth input argument of callback function */
        typedef Arg5 Arg5Type;
        /** Type of sixth input argument of callback function */
        typedef Arg6 Arg6Type;
        /** Type of seventh input argument of callback function */
        typedef Arg7 Arg7Type;
                
        virtual ~Callback7()
        {
        }
        /** Pure virtual function defining function call operator interface. Derived callback classes will implement this 
            function to invoke the callback function (or functions) attached to the callback class instance. */
        virtual Result operator() (Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4, Arg5 a5, Arg6 a6, Arg7 a7) const = 0;
    };

    /** Template class for callbacks with seven input arguments. The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6, class Arg7>
    class Callback7Function : public Callback7<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback7Function<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (*FunctionType)(Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7);
        /** Constructor. */
        Callback7Function(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback function attached to this Callback7Function instance. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4, Arg5 a5, Arg6 a6, Arg7 a7) const
        {
            return m_fn(a1, a2, a3, a4, a5, a6, a7);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        FunctionType m_fn;
    };

#if defined(_WIN32) && !defined(_WIN64)
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6, class Arg7>
    class Callback7StdCallFunction : public Callback7<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback7StdCallFunction<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (__stdcall *FunctionType)(Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7);
        /** Constructor. */
        Callback7StdCallFunction(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback function attached to this Callback7StdCallFunction instance. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4, Arg5 a5, Arg6 a6, Arg7 a7) const
        {
            return m_fn(a1, a2, a3, a4, a5, a6, a7);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        FunctionType m_fn;
    };
#endif

    /** Template class for callbacks with seven input arguments that are member functions of a class. Template type T is the class
        that the callback function is a member function of. The return type of the callback function is the template type Result. */
    template <class T, class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6, class Arg7>
    class Callback7MemberFunction : public Callback7<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback7MemberFunction<T, Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (T::*FunctionType)(Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7);
        /** Constructor. */
        Callback7MemberFunction(T *object, FunctionType fn) : m_object(object), m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback member function attached to this Callback7MemberFunction instance. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4, Arg5 a5, Arg6 a6, Arg7 a7) const
        {
            return (m_object->*m_fn)(a1, a2, a3, a4, a5, a6, a7);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                    m_object == static_cast<const MyClass &>(other).m_object && 
                    m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        T *m_object;
        FunctionType m_fn;
    };


    /** Template class for callbacks with seven input arguments. This template class manages a list of callback functions. 
        The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6, class Arg7>
    class Callback7List : public Callback7<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7>
    {
    private:
        typedef Callback7<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7> BaseClass;
        typedef Callback7List<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7> MyClass;
        typedef std::vector<BaseClass *> FunctionVector;
        typedef typename FunctionVector::iterator iterator;
    public:
        /** Constructor. */
        Callback7List() : m_functions()
        {
        }
        /** Function call operator for invoking callback functions in list. Callbacks are invoked in the order 
            they were added to the list. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4, Arg5 a5, Arg6 a6, Arg7 a7) const
        {
            FunctionVector copy = m_functions;
            if (copy.size() == 0)
                throw "bom";
            for (typename FunctionVector::iterator it = copy.begin(); it != copy.end() - 1; ++it)
                (*(*it))(a1, a2, a3, a4, a5, a6, a7);
            return (*copy.back())(a1, a2, a3, a4, a5, a6, a7);
        }
        /** Function to add callback function to list of callback functions. */
        void Add(const BaseClass &fn)
        {
            m_functions.push_back(static_cast<BaseClass *>(fn.Clone()));
        }
        /** Function to remove the callback function from the list of callback functions. Uses the Equals method on the callback 
            function to find the matching callback function in the list. Finds the first matching callback function in the 
            list and removes it. */
        bool Remove(const BaseClass &fn)
        {
            for (typename FunctionVector::iterator it = m_functions.begin(); it != m_functions.end(); ++it)
                if ((*it)->Equals(fn))
                {
                    m_functions.erase(it);
                    return true;
                }
            return false;
        }
        /** Callback7List destructor. Deletes all the callbacks in the list of callbacks. */
        virtual ~Callback7List()
        {
            for (typename FunctionVector::iterator it = m_functions.begin(); it != m_functions.end(); ++it)
                delete *it;
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return false;
        }
    private:
        FunctionVector m_functions;
    };

    /** Helper template function to create an instance of a Callback7MemberFunction. The template type T is the class
        that the callback is a member function of. The return type of the callback function is the template type Result. */
    template <class T, class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6, class Arg7>
    Callback7MemberFunction<T, Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7> make_callback(T *object, Result (T::*fn)(Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7))
    {
        return Callback7MemberFunction<T, Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7>(object, fn);
    }

    /** Helper template function to create an instance of a Callback7Function. The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6, class Arg7>
    Callback7Function<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7> make_callback(Result (*fn)(Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7))
    {
        return Callback7Function<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7>(fn);
    }

#if defined(_WIN32) && !defined(_WIN64)
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6, class Arg7>
    Callback7StdCallFunction<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7> make_callback(Result (__stdcall *fn)(Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7))
    {
        return Callback7StdCallFunction<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7>(fn);
    }
#endif

//=========Callback8========

    /** Template base class for callbacks with eight input arguments. The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6, class Arg7, class Arg8>
    class Callback8 : public BaseCallback
    {
    public:
        /** Return type of callback function */
        typedef Result ResultType;
        /** Type of first input argument of callback function */
        typedef Arg1 Arg1Type;
        /** Type of second input argument of callback function */
        typedef Arg2 Arg2Type;
        /** Type of third input argument of callback function */
        typedef Arg3 Arg3Type;
        /** Type of fourth input argument of callback function */
        typedef Arg4 Arg4Type;
        /** Type of fifth input argument of callback function */
        typedef Arg5 Arg5Type;
        /** Type of sixth input argument of callback function */
        typedef Arg6 Arg6Type;
        /** Type of seventh input argument of callback function */
        typedef Arg7 Arg7Type;
        /** Type of eighth input argument of callback function */
        typedef Arg8 Arg8Type;
        
        virtual ~Callback8()
        {
        }
        /** Pure virtual function defining function call operator interface. Derived callback classes will implement this 
            function to invoke the callback function (or functions) attached to the callback class instance. */
        virtual Result operator() (Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4, Arg5 a5, Arg6 a6, Arg7 a7, Arg8 a8) const = 0;
    };

    /** Template class for callbacks with eight input arguments. The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6, class Arg7, class Arg8>
    class Callback8Function : public Callback8<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback8Function<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (*FunctionType)(Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8);
        /** Constructor. */
        Callback8Function(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback function attached to this Callback8Function instance. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4, Arg5 a5, Arg6 a6, Arg7 a7, Arg8 a8) const
        {
            return m_fn(a1, a2, a3, a4, a5, a6, a7, a8);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        FunctionType m_fn;
    };

#if defined(_WIN32) && !defined(_WIN64)
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6, class Arg7, class Arg8>
    class Callback8StdCallFunction : public Callback8<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback8StdCallFunction<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (__stdcall *FunctionType)(Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8);
        /** Constructor. */
        Callback8StdCallFunction(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback function attached to this Callback8StdCallFunction instance. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4, Arg5 a5, Arg6 a6, Arg7 a7, Arg8 a8) const
        {
            return m_fn(a1, a2, a3, a4, a5, a6, a7, a8);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        FunctionType m_fn;
    };
#endif

    /** Template class for callbacks with eight input arguments that are member functions of a class. Template type T is the class
        that the callback function is a member function of. The return type of the callback function is the template type Result. */
    template <class T, class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6, class Arg7, class Arg8>
    class Callback8MemberFunction : public Callback8<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8>
    {
    public:
        /** Template typedef of class signature. Used to simplify implementation of callback framework methods. */
        typedef Callback8MemberFunction<T, Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8> MyClass;
        /** Function signature for callback function attached to this template callback class. */
        typedef Result (T::*FunctionType)(Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8);
        /** Constructor. */
        Callback8MemberFunction(T *object, FunctionType fn) : m_object(object), m_fn(fn)
        {
        }
        /** Function call operator function to invoke callback member function attached to this Callback8MemberFunction instance. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4, Arg5 a5, Arg6 a6, Arg7 a7, Arg8 a8) const
        {
            return (m_object->*m_fn)(a1, a2, a3, a4, a5, a6, a7, a8);
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return typeid(*this) == typeid(other) && 
                    m_object == static_cast<const MyClass &>(other).m_object && 
                    m_fn == static_cast<const MyClass &>(other).m_fn;
        }
    private:
        T *m_object;
        FunctionType m_fn;
    };


    /** Template class for callbacks with eight input arguments. This template class manages a list of callback functions. 
        The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6, class Arg7, class Arg8>
    class Callback8List : public Callback8<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8>
    {
    private:
        typedef Callback8<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8> BaseClass;
        typedef Callback8List<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8> MyClass;
        typedef std::vector<BaseClass *> FunctionVector;
        typedef typename FunctionVector::iterator iterator;
    public:
        /** Constructor. */
        Callback8List() : m_functions()
        {
        }
        /** Function call operator for invoking callback functions in list. Callbacks are invoked in the order 
            they were added to the list. */
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4, Arg5 a5, Arg6 a6, Arg7 a7, Arg8 a8) const
        {
            FunctionVector copy = m_functions;
            if (copy.size() == 0)
                throw "bom";
            for (typename FunctionVector::iterator it = copy.begin(); it != copy.end() - 1; ++it)
                (*(*it))(a1, a2, a3, a4, a5, a6, a7, a8);
            return (*copy.back())(a1, a2, a3, a4, a5, a6, a7, a8);
        }
        /** Function to add callback function to list of callback functions. */
        void Add(const BaseClass &fn)
        {
            m_functions.push_back(static_cast<BaseClass *>(fn.Clone()));
        }
        /** Function to remove the callback function from the list of callback functions. Uses the Equals method on the callback 
            function to find the matching callback function in the list. Finds the first matching callback function in the 
            list and removes it. */
        bool Remove(const BaseClass &fn)
        {
            for (typename FunctionVector::iterator it = m_functions.begin(); it != m_functions.end(); ++it)
                if ((*it)->Equals(fn))
                {
                    m_functions.erase(it);
                    return true;
                }
            return false;
        }
        /** Callback8List destructor. Deletes all the callbacks in the list of callbacks. */
        virtual ~Callback8List()
        {
            for (typename FunctionVector::iterator it = m_functions.begin(); it != m_functions.end(); ++it)
                delete *it;
        }
        virtual BaseCallback *Clone() const
        {
            return new MyClass(*this);
        }
        virtual bool Equals(const BaseCallback& other) const
        {
            return false;
        }
    private:
        FunctionVector m_functions;
    };

    /** Helper template function to create an instance of a Callback8MemberFunction. The template type T is the class
        that the callback is a member function of. The return type of the callback function is the template type Result. */
    template <class T, class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6, class Arg7, class Arg8>
    Callback8MemberFunction<T, Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8> make_callback(T *object, Result (T::*fn)(Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8))
    {
        return Callback8MemberFunction<T, Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8>(object, fn);
    }

    /** Helper template function to create an instance of a Callback8Function. The return type of the callback function is the template type Result. */
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6, class Arg7, class Arg8>
    Callback8Function<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8> make_callback(Result (*fn)(Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8))
    {
        return Callback8Function<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8>(fn);
    }

#if defined(_WIN32) && !defined(_WIN64)
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5, class Arg6, class Arg7, class Arg8>
    Callback8StdCallFunction<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8> make_callback(Result (__stdcall *fn)(Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8))
    {
        return Callback8StdCallFunction<Result, Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8>(fn);
    }
#endif
}
#endif

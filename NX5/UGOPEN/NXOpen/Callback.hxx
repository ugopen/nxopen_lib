/*******************************************************************************
                    Copyright (c) 2006 UGS Corp.
                 Unpublished - All rights reserved


*******************************************************************************/
#ifndef NXOpen_Callback_HXX_INCLUDED
#define NXOpen_Callback_HXX_INCLUDED

#include <vector>
#include <typeinfo>

namespace NXOpen
{
    class BaseCallback
    {
    public:
        virtual ~BaseCallback()
        {
        }
        virtual BaseCallback *Clone() const = 0;
        virtual bool Equals(const BaseCallback& other) const = 0;
    };

    template <class Result>
    class Callback0 : public BaseCallback
    {
    public:
        typedef Result ResultType;
        virtual ~Callback0()
        {
        }
        virtual Result operator() () const = 0;
    };

    template <class Result>
    class Callback0Function : public Callback0<Result>
    {
    public:
        typedef Callback0Function<Result> MyClass;
        typedef Result (*FunctionType)();
        Callback0Function(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
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

#if defined(_WIN32) || defined(_WIN64)
    template <class Result>
    class Callback0StdCallFunction : public Callback0<Result>
    {
    public:
        typedef Callback0StdCallFunction<Result> MyClass;
        typedef Result (__stdcall *FunctionType)();
        Callback0StdCallFunction(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
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

    template <class T, class Result>
    class Callback0MemberFunction : public Callback0<Result>
    {
    public:
        typedef Callback0MemberFunction<T, Result> MyClass;
        typedef Result (T::*FunctionType)();
        Callback0MemberFunction(T *object, FunctionType fn) : m_object(object), m_fn(fn)
        {
        }
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


    template <class Result>
    class Callback0List : public Callback0<Result>
    {
    private:
        typedef Callback0<Result> BaseClass;
        typedef Callback0List<Result> MyClass;
        typedef std::vector<BaseClass *> FunctionVector;
        typedef typename FunctionVector::iterator iterator;
    public:
        Callback0List() : m_functions()
        {
        }
        virtual Result operator()() const
        {
            FunctionVector copy = m_functions;
            if (copy.size() == 0)
                throw "bom";
            for (typename FunctionVector::iterator it = copy.begin(); it != copy.end() - 1; ++it)
                (*(*it))();
            return (*copy.back())();
        }
        void Add(const BaseClass &fn)
        {
            m_functions.push_back(static_cast<BaseClass *>(fn.Clone()));
        }
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
        ~Callback0List()
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

    template <class T, class Result>
    Callback0MemberFunction<T, Result> make_callback(T *object, Result (T::*fn)())
    {
        return Callback0MemberFunction<T, Result>(object, fn);
    }

    template <class Result>
    Callback0Function<Result> make_callback(Result (*fn)())
    {
        return Callback0Function<Result>(fn);
    }

#if defined(_WIN32) || defined(_WIN64)
    template <class Result>
    Callback0StdCallFunction<Result> make_callback(Result (__stdcall *fn)())
    {
        return Callback0StdCallFunction<Result>(fn);
    }
#endif

    template <class Result, class Arg1>
    class Callback1 : public BaseCallback
    {
    public:
        typedef Result ResultType;
        typedef Arg1 Arg1Type;
        virtual ~Callback1()
        {
        }
        virtual Result operator() (Arg1 a1) const = 0;
    };

    template <class Result, class Arg1>
    class Callback1Function : public Callback1<Result, Arg1>
    {
    public:
        typedef Callback1Function<Result, Arg1> MyClass;
        typedef Result (*FunctionType)(Arg1);
        Callback1Function(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
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

#if defined(_WIN32) || defined(_WIN64)
    template <class Result, class Arg1>
    class Callback1StdCallFunction : public Callback1<Result, Arg1>
    {
    public:
        typedef Callback1StdCallFunction<Result, Arg1> MyClass;
        typedef Result (__stdcall *FunctionType)(Arg1);
        Callback1StdCallFunction(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
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

    template <class T, class Result, class Arg1>
    class Callback1MemberFunction : public Callback1<Result, Arg1>
    {
    public:
        typedef Callback1MemberFunction<T, Result, Arg1> MyClass;
        typedef Result (T::*FunctionType)(Arg1);
        Callback1MemberFunction(T *object, FunctionType fn) : m_object(object), m_fn(fn)
        {
        }
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


    template <class Result, class Arg1>
    class Callback1List : public Callback1<Result, Arg1>
    {
    private:
        typedef Callback1<Result, Arg1> BaseClass;
        typedef Callback1List<Result, Arg1> MyClass;
        typedef std::vector<BaseClass *> FunctionVector;
        typedef typename FunctionVector::iterator iterator;
    public:
        Callback1List() : m_functions()
        {
        }
        virtual Result operator()(Arg1 a1) const
        {
            FunctionVector copy = m_functions;
            if (copy.size() == 0)
                throw "bom";
            for (typename FunctionVector::iterator it = copy.begin(); it != copy.end() - 1; ++it)
                (*(*it))(a1);
            return (*copy.back())(a1);
        }
        void Add(const BaseClass &fn)
        {
            m_functions.push_back(static_cast<BaseClass *>(fn.Clone()));
        }
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
        ~Callback1List()
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

    template <class T, class Result, class Arg1>
    Callback1MemberFunction<T, Result, Arg1> make_callback(T *object, Result (T::*fn)(Arg1))
    {
        return Callback1MemberFunction<T, Result, Arg1>(object, fn);
    }

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

#if defined(_WIN32) || defined(_WIN64)
    template <class Result, class Arg1>
    Callback1StdCallFunction<Result, Arg1> make_callback(Result (__stdcall *fn)(Arg1))
    {
        return Callback1StdCallFunction<Result, Arg1>(fn);
    }
#endif

    template <class Result, class Arg1, class Arg2>
    class Callback2 : public BaseCallback
    {
    public:
        typedef Result ResultType;
        typedef Arg1 Arg1Type;
        typedef Arg2 Arg2Type;
        virtual ~Callback2()
        {
        }
        virtual Result operator() (Arg1 a1, Arg2 a2) const = 0;
    };

    template <class Result, class Arg1, class Arg2>
    class Callback2Function : public Callback2<Result, Arg1, Arg2>
    {
    public:
        typedef Callback2Function<Result, Arg1, Arg2> MyClass;
        typedef Result (*FunctionType)(Arg1, Arg2);
        Callback2Function(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
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

#if defined(_WIN32) || defined(_WIN64)
    template <class Result, class Arg1, class Arg2>
    class Callback2StdCallFunction : public Callback2<Result, Arg1, Arg2>
    {
    public:
        typedef Callback2StdCallFunction<Result, Arg1, Arg2> MyClass;
        typedef Result (__stdcall *FunctionType)(Arg1, Arg2);
        Callback2StdCallFunction(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
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

    template <class T, class Result, class Arg1, class Arg2>
    class Callback2MemberFunction : public Callback2<Result, Arg1, Arg2>
    {
    public:
        typedef Callback2MemberFunction<T, Result, Arg1, Arg2> MyClass;
        typedef Result (T::*FunctionType)(Arg1, Arg2);
        Callback2MemberFunction(T *object, FunctionType fn) : m_object(object), m_fn(fn)
        {
        }
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


    template <class Result, class Arg1, class Arg2>
    class Callback2List : public Callback2<Result, Arg1, Arg2>
    {
    private:
        typedef Callback2<Result, Arg1, Arg2> BaseClass;
        typedef Callback2List<Result, Arg1, Arg2> MyClass;
        typedef std::vector<BaseClass *> FunctionVector;
        typedef typename FunctionVector::iterator iterator;
    public:
        Callback2List() : m_functions()
        {
        }
        virtual Result operator()(Arg1 a1, Arg2 a2) const
        {
            FunctionVector copy = m_functions;
            if (copy.size() == 0)
                throw "bom";
            for (typename FunctionVector::iterator it = copy.begin(); it != copy.end() - 1; ++it)
                (*(*it))(a1, a2);
            return (*copy.back())(a1, a2);
        }
        void Add(const BaseClass &fn)
        {
            m_functions.push_back(static_cast<BaseClass *>(fn.Clone()));
        }
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
        ~Callback2List()
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

    template <class T, class Result, class Arg1, class Arg2>
    Callback2MemberFunction<T, Result, Arg1, Arg2> make_callback(T *object, Result (T::*fn)(Arg1, Arg2))
    {
        return Callback2MemberFunction<T, Result, Arg1, Arg2>(object, fn);
    }

    template <class Result, class Arg1, class Arg2>
    Callback2Function<Result, Arg1, Arg2> make_callback(Result (*fn)(Arg1, Arg2))
    {
        return Callback2Function<Result, Arg1, Arg2>(fn);
    }

#if defined(_WIN32) || defined(_WIN64)
    template <class Result, class Arg1, class Arg2>
    Callback2StdCallFunction<Result, Arg1, Arg2> make_callback(Result (__stdcall *fn)(Arg1, Arg2))
    {
        return Callback2StdCallFunction<Result, Arg1, Arg2>(fn);
    }
#endif

    template <class Result, class Arg1, class Arg2, class Arg3>
    class Callback3 : public BaseCallback
    {
    public:
        typedef Result ResultType;
        typedef Arg1 Arg1Type;
        typedef Arg2 Arg2Type;
        typedef Arg3 Arg3Type;
        virtual ~Callback3()
        {
        }
        virtual Result operator() (Arg1 a1, Arg2 a2, Arg3 a3) const = 0;
    };

    template <class Result, class Arg1, class Arg2, class Arg3>
    class Callback3Function : public Callback3<Result, Arg1, Arg2, Arg3>
    {
    public:
        typedef Callback3Function<Result, Arg1, Arg2, Arg3> MyClass;
        typedef Result (*FunctionType)(Arg1, Arg2, Arg3);
        Callback3Function(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
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

#if defined(_WIN32) || defined(_WIN64)
    template <class Result, class Arg1, class Arg2, class Arg3>
    class Callback3StdCallFunction : public Callback3<Result, Arg1, Arg2, Arg3>
    {
    public:
        typedef Callback3StdCallFunction<Result, Arg1, Arg2, Arg3> MyClass;
        typedef Result (__stdcall *FunctionType)(Arg1, Arg2, Arg3);
        Callback3StdCallFunction(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
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

    template <class T, class Result, class Arg1, class Arg2, class Arg3>
    class Callback3MemberFunction : public Callback3<Result, Arg1, Arg2, Arg3>
    {
    public:
        typedef Callback3MemberFunction<T, Result, Arg1, Arg2, Arg3> MyClass;
        typedef Result (T::*FunctionType)(Arg1, Arg2, Arg3);
        Callback3MemberFunction(T *object, FunctionType fn) : m_object(object), m_fn(fn)
        {
        }
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


    template <class Result, class Arg1, class Arg2, class Arg3>
    class Callback3List : public Callback3<Result, Arg1, Arg2, Arg3>
    {
    private:
        typedef Callback3<Result, Arg1, Arg2, Arg3> BaseClass;
        typedef Callback3List<Result, Arg1, Arg2, Arg3> MyClass;
        typedef std::vector<BaseClass *> FunctionVector;
        typedef typename FunctionVector::iterator iterator;
    public:
        Callback3List() : m_functions()
        {
        }
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3) const
        {
            FunctionVector copy = m_functions;
            if (copy.size() == 0)
                throw "bom";
            for (typename FunctionVector::iterator it = copy.begin(); it != copy.end() - 1; ++it)
                (*(*it))(a1, a2, a3);
            return (*copy.back())(a1, a2, a3);
        }
        void Add(const BaseClass &fn)
        {
            m_functions.push_back(static_cast<BaseClass *>(fn.Clone()));
        }
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
        ~Callback3List()
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

    template <class T, class Result, class Arg1, class Arg2, class Arg3>
    Callback3MemberFunction<T, Result, Arg1, Arg2, Arg3> make_callback(T *object, Result (T::*fn)(Arg1, Arg2, Arg3))
    {
        return Callback3MemberFunction<T, Result, Arg1, Arg2, Arg3>(object, fn);
    }

    template <class Result, class Arg1, class Arg2, class Arg3>
    Callback3Function<Result, Arg1, Arg2, Arg3> make_callback(Result (*fn)(Arg1, Arg2, Arg3))
    {
        return Callback3Function<Result, Arg1, Arg2, Arg3>(fn);
    }

#if defined(_WIN32) || defined(_WIN64)
    template <class Result, class Arg1, class Arg2, class Arg3>
    Callback3StdCallFunction<Result, Arg1, Arg2, Arg3> make_callback(Result (__stdcall *fn)(Arg1, Arg2, Arg3))
    {
        return Callback3StdCallFunction<Result, Arg1, Arg2, Arg3>(fn);
    }
#endif

    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4>
    class Callback4 : public BaseCallback
    {
    public:
        typedef Result ResultType;
        typedef Arg1 Arg1Type;
        typedef Arg2 Arg2Type;
        typedef Arg3 Arg3Type;
        typedef Arg4 Arg4Type;
        virtual ~Callback4()
        {
        }
        virtual Result operator() (Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4) const = 0;
    };

    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4>
    class Callback4Function : public Callback4<Result, Arg1, Arg2, Arg3, Arg4>
    {
    public:
        typedef Callback4Function<Result, Arg1, Arg2, Arg3, Arg4> MyClass;
        typedef Result (*FunctionType)(Arg1, Arg2, Arg3, Arg4);
        Callback4Function(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
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

#if defined(_WIN32) || defined(_WIN64)
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4>
    class Callback4StdCallFunction : public Callback4<Result, Arg1, Arg2, Arg3, Arg4>
    {
    public:
        typedef Callback4StdCallFunction<Result, Arg1, Arg2, Arg3, Arg4> MyClass;
        typedef Result (__stdcall *FunctionType)(Arg1, Arg2, Arg3, Arg4);
        Callback4StdCallFunction(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
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

    template <class T, class Result, class Arg1, class Arg2, class Arg3, class Arg4>
    class Callback4MemberFunction : public Callback4<Result, Arg1, Arg2, Arg3, Arg4>
    {
    public:
        typedef Callback4MemberFunction<T, Result, Arg1, Arg2, Arg3, Arg4> MyClass;
        typedef Result (T::*FunctionType)(Arg1, Arg2, Arg3, Arg4);
        Callback4MemberFunction(T *object, FunctionType fn) : m_object(object), m_fn(fn)
        {
        }
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


    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4>
    class Callback4List : public Callback4<Result, Arg1, Arg2, Arg3, Arg4>
    {
    private:
        typedef Callback4<Result, Arg1, Arg2, Arg3, Arg4> BaseClass;
        typedef Callback4List<Result, Arg1, Arg2, Arg3, Arg4> MyClass;
        typedef std::vector<BaseClass *> FunctionVector;
        typedef typename FunctionVector::iterator iterator;
    public:
        Callback4List() : m_functions()
        {
        }
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4) const
        {
            FunctionVector copy = m_functions;
            if (copy.size() == 0)
                throw "bom";
            for (typename FunctionVector::iterator it = copy.begin(); it != copy.end() - 1; ++it)
                (*(*it))(a1, a2, a3, a4);
            return (*copy.back())(a1, a2, a3, a4);
        }
        void Add(const BaseClass &fn)
        {
            m_functions.push_back(static_cast<BaseClass *>(fn.Clone()));
        }
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
        ~Callback4List()
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

    template <class T, class Result, class Arg1, class Arg2, class Arg3, class Arg4>
    Callback4MemberFunction<T, Result, Arg1, Arg2, Arg3, Arg4> make_callback(T *object, Result (T::*fn)(Arg1, Arg2, Arg3, Arg4))
    {
        return Callback4MemberFunction<T, Result, Arg1, Arg2, Arg3, Arg4>(object, fn);
    }

    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4>
    Callback4Function<Result, Arg1, Arg2, Arg3, Arg4> make_callback(Result (*fn)(Arg1, Arg2, Arg3, Arg4))
    {
        return Callback4Function<Result, Arg1, Arg2, Arg3, Arg4>(fn);
    }

#if defined(_WIN32) || defined(_WIN64)
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4>
    Callback4StdCallFunction<Result, Arg1, Arg2, Arg3, Arg4> make_callback(Result (__stdcall *fn)(Arg1, Arg2, Arg3, Arg4))
    {
        return Callback4StdCallFunction<Result, Arg1, Arg2, Arg3, Arg4>(fn);
    }
#endif

    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5>
    class Callback5 : public BaseCallback
    {
    public:
        typedef Result ResultType;
        typedef Arg1 Arg1Type;
        typedef Arg2 Arg2Type;
        typedef Arg3 Arg3Type;
        typedef Arg4 Arg4Type;
        typedef Arg5 Arg5Type;
        virtual ~Callback5()
        {
        }
        virtual Result operator() (Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4, Arg5 a5) const = 0;
    };

    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5>
    class Callback5Function : public Callback5<Result, Arg1, Arg2, Arg3, Arg4, Arg5>
    {
    public:
        typedef Callback5Function<Result, Arg1, Arg2, Arg3, Arg4, Arg5> MyClass;
        typedef Result (*FunctionType)(Arg1, Arg2, Arg3, Arg4, Arg5);
        Callback5Function(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
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

#if defined(_WIN32) || defined(_WIN64)
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5>
    class Callback5StdCallFunction : public Callback5<Result, Arg1, Arg2, Arg3, Arg4, Arg5>
    {
    public:
        typedef Callback5StdCallFunction<Result, Arg1, Arg2, Arg3, Arg4, Arg5> MyClass;
        typedef Result (__stdcall *FunctionType)(Arg1, Arg2, Arg3, Arg4, Arg5);
        Callback5StdCallFunction(FunctionType fn) 
            /*lint --e(1931) */ // ok to use as conversion
            : m_fn(fn)
        {
        }
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

    template <class T, class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5>
    class Callback5MemberFunction : public Callback5<Result, Arg1, Arg2, Arg3, Arg4, Arg5>
    {
    public:
        typedef Callback5MemberFunction<T, Result, Arg1, Arg2, Arg3, Arg4, Arg5> MyClass;
        typedef Result (T::*FunctionType)(Arg1, Arg2, Arg3, Arg4, Arg5);
        Callback5MemberFunction(T *object, FunctionType fn) : m_object(object), m_fn(fn)
        {
        }
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


    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5>
    class Callback5List : public Callback5<Result, Arg1, Arg2, Arg3, Arg4, Arg5>
    {
    private:
        typedef Callback5<Result, Arg1, Arg2, Arg3, Arg4, Arg5> BaseClass;
        typedef Callback5List<Result, Arg1, Arg2, Arg3, Arg4, Arg5> MyClass;
        typedef std::vector<BaseClass *> FunctionVector;
        typedef typename FunctionVector::iterator iterator;
    public:
        Callback5List() : m_functions()
        {
        }
        virtual Result operator()(Arg1 a1, Arg2 a2, Arg3 a3, Arg4 a4, Arg5 a5) const
        {
            FunctionVector copy = m_functions;
            if (copy.size() == 0)
                throw "bom";
            for (typename FunctionVector::iterator it = copy.begin(); it != copy.end() - 1; ++it)
                (*(*it))(a1, a2, a3, a4, a5);
            return (*copy.back())(a1, a2, a3, a4);
        }
        void Add(const BaseClass &fn)
        {
            m_functions.push_back(static_cast<BaseClass *>(fn.Clone()));
        }
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
        ~Callback5List()
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

    template <class T, class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5>
    Callback5MemberFunction<T, Result, Arg1, Arg2, Arg3, Arg4, Arg5> make_callback(T *object, Result (T::*fn)(Arg1, Arg2, Arg3, Arg4, Arg5))
    {
        return Callback5MemberFunction<T, Result, Arg1, Arg2, Arg3, Arg4, Arg5>(object, fn);
    }

    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5>
    Callback5Function<Result, Arg1, Arg2, Arg3, Arg4, Arg5> make_callback(Result (*fn)(Arg1, Arg2, Arg3, Arg4, Arg5))
    {
        return Callback5Function<Result, Arg1, Arg2, Arg3, Arg4, Arg5>(fn);
    }

#if defined(_WIN32) || defined(_WIN64)
    template <class Result, class Arg1, class Arg2, class Arg3, class Arg4, class Arg5>
    Callback5StdCallFunction<Result, Arg1, Arg2, Arg3, Arg4, Arg5> make_callback(Result (__stdcall *fn)(Arg1, Arg2, Arg3, Arg4, Arg5))
    {
        return Callback5StdCallFunction<Result, Arg1, Arg2, Arg3, Arg4, Arg5>(fn);
    }
#endif
}
#endif

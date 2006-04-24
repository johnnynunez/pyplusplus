// This file has been generated by pyplusplus.

// Copyright 2004 Roman Yakovenko.
// Distributed under the Boost Software License, Version 1.0. (See
// accompanying file LICENSE_1_0.txt or copy at
// http://www.boost.org/LICENSE_1_0.txt)

#include "boost/python.hpp"
#ifdef _MSC_VER
    #pragma hdrstop
#endif //_MSC_VER

#include "unittests/data/user_text_to_be_exported.hpp"

namespace bp = boost::python;

struct data_wrapper : user_text::data, bp::wrapper< user_text::data > {

    data_wrapper(user_text::data const & arg )
    : user_text::data( arg )
      , bp::wrapper< user_text::data >()
    {}

    data_wrapper()
    : user_text::data()
      , bp::wrapper< user_text::data >()
    {}

    /*wrapper code*/

};

BOOST_PYTHON_MODULE(user_text){
    if( true ){
        typedef bp::class_< data_wrapper > data_exposer_t;
        data_exposer_t data_exposer = data_exposer_t( "data" );
        bp::scope data_scope( data_exposer );
        /*class code*/
    }
}

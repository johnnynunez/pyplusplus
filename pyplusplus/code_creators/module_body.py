# Copyright 2004 Roman Yakovenko.
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

import os
import compound

class module_body_t(compound.compound_t):
    def __init__( self, name, parent=None ):
        compound.compound_t.__init__(self, parent)
        self._name = name
    
    def _get_name(self):
        return self._name
    name = property( _get_name )
        
    def _create_impl(self):
        result = []
        result.append( "BOOST_PYTHON_MODULE(%s){" % self.name )
        result.append( compound.compound_t.create_internal_code( self.creators ) )
        result.append( "}" )
        return os.linesep.join( result )
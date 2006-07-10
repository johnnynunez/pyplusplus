# Copyright 2004 Roman Yakovenko.
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

"""
This package provides users with simple and convinient interface to pyplusplus
functionality.

L{module_builder_t} class is the main class. Please read it's documentation first.
Also take a look on tutorials. You can find them on pyplusplus 
U{web site<http://www.language-binding.net>}
"""

from builder import module_builder_t

#aliases for functionality located in pygccxml.parser module
from pygccxml.parser import COMPILATION_MODE
from pygccxml.parser import create_cached_source_fc
from pygccxml.parser import create_gccxml_fc
from pygccxml.parser import create_source_fc
from pygccxml.parser import create_text_fc
from pygccxml.parser import directory_cache_t
from pygccxml.parser import file_cache_t
from pygccxml.parser import file_configuration_t
from pygccxml.declarations import mdecl_wrapper_t

#aliases for functionality located in decl_wrappers package

from pyplusplus.decl_wrappers import calldef_t
from pyplusplus.decl_wrappers import member_function_t
from pyplusplus.decl_wrappers import constructor_t
from pyplusplus.decl_wrappers import destructor_t
from pyplusplus.decl_wrappers import member_operator_t
from pyplusplus.decl_wrappers import casting_operator_t
from pyplusplus.decl_wrappers import free_function_t
from pyplusplus.decl_wrappers import free_operator_t
from pyplusplus.decl_wrappers import class_declaration_t
from pyplusplus.decl_wrappers import class_t
from pyplusplus.decl_wrappers import enumeration_t
from pyplusplus.decl_wrappers import namespace_t
from pyplusplus.decl_wrappers import typedef_t
from pyplusplus.decl_wrappers import variable_t
from pyplusplus.decl_wrappers import scopedef_t

from pyplusplus.decl_wrappers import print_declarations

import call_policies

from pygccxml import utils as __pygccxml_utils
from pyplusplus import _logging_ as __pyplusplus_logging

def set_logger_level( level ):
    for l in __pygccxml_utils.loggers.all:
        l.setLevel( level )
    __pyplusplus_logging.logger.setLevel( level )
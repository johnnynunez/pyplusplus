# Copyright 2004 Roman Yakovenko.
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

import os
import sys
import unittest
import fundamental_tester_base
from pygccxml import declarations

class tester_t(fundamental_tester_base.fundamental_tester_base_t):
    EXTENSION_NAME = 'member_functions'
    
    def __init__( self, *args ):
        fundamental_tester_base.fundamental_tester_base_t.__init__( 
            self
            , tester_t.EXTENSION_NAME
            , *args )
                                                                    
    def customize(self, mb ):
        names = [
            'protected_protected_derived_t'
            , 'protected_public_derived_t'
            , 'protected_base_t'
            , 'public_derived_t'
            , 'public_base_t'
            , 'private_derived_t'
            , 'private_base_t'
        ]

        mb.classes( lambda decl: decl.name in names ).always_expose_using_scope = True
        #will reporoduce bug
        mb.class_('callable_t').always_expose_using_scope = True
        
    def create_test_class_inst(self, class_ ):
        class tester_impl_t( class_ ):
            def __init__(self):
                class_.__init__( self )

            def pure_virtual(self, x):
                return x + x

            def pure_virtual_overloaded( self, *args ):
                assert 1 <= len(args) <= 2
                if 1 == len( args ):
                    return args[0] + args[0]
                else:
                    return args[0] + args[1]

            def pure_virtual_const( self, x ):
                return x + x

            def pure_virtual_const_overloaded( self, *args ):
                assert 1 <= len(args) <= 2
                if 1 == len( args ):
                    return args[0] + args[0]
                else:
                    return args[0] + args[1]

        return tester_impl_t()

    def _test_instance( self, inst, class_defined_in_cpp):
        self.failUnless( 23 == inst.regular( 23 ) )
        self.failUnless( 9 == inst.regular_overloaded( 3 ) )    
        self.failUnless( 15 == inst.regular_overloaded( 3, 5 ) )    

        self.failUnless( 23 == inst.regular_const( 23 ) )
        self.failUnless( 9 == inst.regular_const_overloaded( 3 ) )    
        self.failUnless( 15 == inst.regular_const_overloaded( 3, 5 ) )    

        self.failUnless( 23 == inst.virtual_( 23 ) )
        self.failUnless( 9 == inst.virtual_overloaded( 3 ) )    
        self.failUnless( 15 == inst.virtual_overloaded( 3, 5 ) )    

        self.failUnless( 23 == inst.virtual_const( 23 ) )
        self.failUnless( 9 == inst.virtual_const_overloaded( 3 ) )    
        self.failUnless( 15 == inst.virtual_const_overloaded( 3, 5 ) )    
        
        if class_defined_in_cpp:
            self.failUnless( 23 == inst.pure_virtual( 23 ) )
            self.failUnless( 9 == inst.pure_virtual_overloaded( 3 ) )    
            self.failUnless( 15 == inst.pure_virtual_overloaded( 3, 5 ) )    
    
            self.failUnless( 23 == inst.pure_virtual_const( 23 ) )
            self.failUnless( 9 == inst.pure_virtual_const_overloaded( 3 ) )    
            self.failUnless( 15 == inst.pure_virtual_const_overloaded( 3, 5 ) )    
        else:
            self.failUnless( 46 == inst.pure_virtual( 23 ) )
            self.failUnless( 6 == inst.pure_virtual_overloaded( 3 ) )    
            self.failUnless( 8 == inst.pure_virtual_overloaded( 3, 5 ) )    
    
            self.failUnless( 46 == inst.pure_virtual_const( 23 ) )
            self.failUnless( 6 == inst.pure_virtual_const_overloaded( 3 ) )    
            self.failUnless( 8 == inst.pure_virtual_const_overloaded( 3, 5 ) )    
    
    def run_tests(self, module):        
        derived = module.protected_public_derived_t()
        self._test_instance( derived, True )
        derived = module.protected_protected_derived_t()
        self._test_instance( derived, True )
        derived = self.create_test_class_inst( module.protected_base_t )
        self._test_instance( derived, False )
        derived = self.create_test_class_inst( module.public_derived_t )
        self._test_instance( derived, False )
        derived = self.create_test_class_inst( module.public_base_t )
        self._test_instance( derived, False )
    
def create_suite():
    suite = unittest.TestSuite()    
    suite.addTest( unittest.makeSuite(tester_t))
    return suite

def run_suite():
    unittest.TextTestRunner(verbosity=2).run( create_suite() )

if __name__ == "__main__":
    run_suite()
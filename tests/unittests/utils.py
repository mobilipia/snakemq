#! -*- coding: utf-8 -*-
"""
@author: David Siroky (siroky@dasir.cz)
@license: MIT License (see LICENSE.txt or 
          U{http://www.opensource.org/licenses/mit-license.php})
"""

import unittest

##########################################################################
##########################################################################

class TestCase(unittest.TestCase):
    def shortDescription(self):
        return str(self)

    ######### missing asserts

    # py2.6 does not have assertNotIn
    if not hasattr(unittest.TestCase, "assertNotIn"):
        def assertNotIn(self, a, b):
            return self.assertTrue(a not in b, (a, b))

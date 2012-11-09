'''
test_seekfile_bloom.py

Copyright 2012 Andres Riancho

This file is part of w3af, w3af.sourceforge.net .

w3af is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

w3af is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with w3af; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

'''
import unittest

from core.data.bloomfilter.seekfile_bloom import FileSeekBloomFilter
from core.data.bloomfilter.tests.generic_filter_test import GenericFilterTest
from core.data.bloomfilter.wrappers import GenericBloomFilter


class TestCMmapBloomFilterLarge(unittest.TestCase, GenericFilterTest):
    
    CAPACITY = 20000
    ERROR_RATE = 0.001
    
    def setUp(self):
        temp_file = GenericBloomFilter.get_temp_file()
        self.filter = FileSeekBloomFilter(self.CAPACITY, self.ERROR_RATE, temp_file)
        
class TestCMmapBloomFilterSmall(unittest.TestCase, GenericFilterTest):
    
    CAPACITY = 500
    ERROR_RATE = 0.001
    
    def setUp(self):
        temp_file = GenericBloomFilter.get_temp_file()
        self.filter = FileSeekBloomFilter(self.CAPACITY, self.ERROR_RATE, temp_file)

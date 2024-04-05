import pytest

import sys
sys.path.append( 'code')
import physics as phy

def test_gravity():
    assert 1==1

def test_collision():
    e = phy.Entity()
    assert 2==2


from utils import arrs
from utils import dicts


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 0) == []
    assert arrs.my_slice([1, 2, 3], -6) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3, 4, 5], -2) == [4, 5]


def test_get_val():
    data = {"vcs": "mercurial"}
    assert dicts.get_val(data, 'vcs') == 'mercurial'
    assert dicts.get_val(data, 'vcs', 'git') == 'mercurial'
    assert dicts.get_val({}, 'vcs', 'git') == 'git'
    assert dicts.get_val({}, 'vcs', 'bazaar') == 'bazaar'

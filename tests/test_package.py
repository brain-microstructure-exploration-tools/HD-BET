from __future__ import annotations

import importlib.metadata

import hd_bet as m


def test_version():
    assert importlib.metadata.version("hd_bet") == m.__version__

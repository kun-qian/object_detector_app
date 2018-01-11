#!usr/bin/env python3
# -*- coding: utf-8 -*-


class VideoSource(object):

    def __init__(self, id, src):
        self._id = id
        self._src = src

    @property
    def id(self):
        return self._id

    @property
    def src(self):
        return self._src

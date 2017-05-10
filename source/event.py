#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Event:

  """Store info about parsed input log events"""

  def __init__(self, timestamp, level, subsystem, message):
    self.timestamp = timestamp
    self.level = level
    self.subsystem = subsystem
    self.message = message

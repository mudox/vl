#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BaseOutLine:

  """base event class"""

  def __init__(self, message):
    self.message = message


class OutLine(BaseOutLine):

  """the log line reprent the starting of a log event"""

  def __init__(self, timestamp, level, subsystem, message):
    super(OutLine, self).__init__(message)

    self.timestamp = timestamp
    self.level = level
    self.subsystem = subsystem


class ContinuedOutLine(BaseOutLine):

  """the log line represents continued line of a log event"""

  def __init__(self, startLine, message):
    if startLine is None or not isinstance(startLine, OutLine):
      raise ValueError('need an valid OutLine object as startLine: %s' % startLine)

    super(ContinuedOutLine, self).__init__(message)
    self._mainLine = startLine

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from out_line import OutLine, ContinuedOutLine


class Parser:

  _previousLogLine = None

  """parse input lines into Event objects"""

  def __init__(self):
    # pattern `[time] [level] [subsystem] message`
    pattern = r'''
    ^
    \[ (?P<timestamp>    [^]]+ ) \]                                                 # timestamp
    \s
    \[ (?P<level>        VERBOSE | INFO | DEBUG | WARN | ERROR  | CRITICAL ) \]     # level
    \s
    \[ (?P<subsystem>    [^]]+ ) \]                                                 # subsystem
    \s
    (?P<message> .* )
    $
    '''
    self._pattern = re.compile(pattern, re.VERBOSE)

  def parse(self, line):
    """parse the argument, a log line, into one of BaseOutLine derived object

    :line: the input log line
    :returns: a OutLine or ContinuedOutLine object

    """

    match = self._pattern.match(line)

    if match:
      line = OutLine(*match.groups())
      self._previousLogLine = line
      return line
    else:
      return ContinuedOutLine(self._previousLogLine, line)

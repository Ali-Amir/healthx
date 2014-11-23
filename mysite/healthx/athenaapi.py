#!/usr/bin/env python2

#    Copyright 2014 athenahealth, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you
#   may not use this file except in compliance with the License.  You
#   may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
#   implied.  See the License for the specific language governing
#   permissions and limitations under the License.

import httplib
import base64
import json
import urllib
import athenahealthapi
import datetime
from io import StringIO

def getPatientData():
  key = 'he92p22duzyc7zttxr29jvkz'
  secret = 'FwmCHrRz6wmW8dr'
  practiceid = 195900
  version = 'preview1'
  api = athenahealthapi.APIConnection(version, key, secret, practiceid)

  ccda = api.GET('/patients/{0}/ccda'.format(2846), {
    'departmentid': 150,
    'purpose': 'internal',
    'xmloutput': 'N',
    'limit': 1,
  })

  from lxml import etree
  print ccda[0]
  parser = etree.XMLParser(ns_clean=True)
  tree = etree.parse(StringIO(ccda[0]['ccda']), parser)
  print ccda[0]['ccda']

  return etree.tostring(tree.getroot(), pretty_print=True, method="html")

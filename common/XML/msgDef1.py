#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Tue Jul 12 16:13:57 2022 by generateDS.py version 2.40.8.
# Python 3.9.7 (default, Sep 16 2021, 13:09:58)  [GCC 7.5.0]
#
# Command line options:
#   ('-o', 'msgDef1.py')
#
# Command line arguments:
#   V2G_CI_MsgDef.xsd
#
# Command line:
#   /home/nikos/anaconda3/bin/generateDS.py -o "msgDef1.py" V2G_CI_MsgDef.xsd
#
# Current working directory (os.getcwd()):
#   schemas
#

import sys

try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
from six.moves import zip_longest
import os
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
from lxml import etree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
TagNamePrefix = ""
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the _exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#
#
try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ModulenotfoundExp_ :
    GenerateDSNamespaceDefs_ = {"V2G_Message":'\n xmlns:ns7="urn:iso:15118:2:2013:MsgDef"\n xmlns:ns5="urn:iso:15118:2:2013:MsgBody"\n xmlns:ns8="urn:iso:15118:2:2013:MsgHeader"\n xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes"\n xmlns:xmlsig="http://www.w3.org/2000/09/xmldsig#"',}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ModulenotfoundExp_ :
    GenerateDSNamespaceTypePrefixes_ = {
        "MessageHeaderType":"ns7",
        "BodyType":"ns7",
        "V2G_Message":"ns7",
        
        
    }

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ModulenotfoundExp_ :

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ModulenotfoundExp_ :
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ModulenotfoundExp_ as exp:
    try:
        from generatedssupersuper import GeneratedsSuperSuper
    except ModulenotfoundExp_ as exp:
        class GeneratedsSuperSuper(object):
            pass
    
    class GeneratedsSuper(GeneratedsSuperSuper):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def __str__(self):
            settings = {
                'str_pretty_print': True,
                'str_indent_level': 0,
                'str_namespaceprefix': '',
                'str_name': self.__class__.__name__,
                'str_namespacedefs': '',
            }
            for n in settings:
                if hasattr(self, n):
                    settings[n] = getattr(self, n)
            if sys.version_info.major == 2:
                from StringIO import StringIO
            else:
                from io import StringIO
            output = StringIO()
            self.export(
                output,
                settings['str_indent_level'],
                pretty_print=settings['str_pretty_print'],
                namespaceprefix_=settings['str_namespaceprefix'],
                name_=settings['str_name'],
                namespacedef_=settings['str_namespacedefs']
            )
            strval = output.getvalue()
            output.close()
            return strval
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data).decode('ascii')
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % int(input_data)
        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival
        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value
        def gds_format_integer_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer values')
            return values
        def gds_format_float(self, input_data, input_name=''):
            return ('%.15f' % float(input_data)).rstrip('0')
        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_
        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value
        def gds_format_float_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values
        def gds_format_decimal(self, input_data, input_name=''):
            return_value = '%s' % input_data
            if '.' in return_value:
                return_value = return_value.rstrip('0')
                if return_value.endswith('.'):
                    return_value = return_value.rstrip('.')
            return return_value
        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value
        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value
        def gds_format_decimal_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return ' '.join([self.gds_format_decimal(item) for item in input_data])
        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values
        def gds_format_double(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_
        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value
        def gds_format_double_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval
        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                value = self.gds_parse_boolean(value, node, input_name)
                if value not in (True, 1, False, 0, ):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values
        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt
        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue
        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()
        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1
        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()
        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None :
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))
        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content
        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))
        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring
        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result
        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')
            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))
        def __ne__(self, other):
            return not self.__eq__(other)
        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass
        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        if prefix == 'xml':
            namespace = 'http://www.w3.org/XML/1998/namespace'
        else:
            namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, reverse_mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, reverse_mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#


class DC_EVErrorCodeType(str, Enum):
    NO_ERROR='NO_ERROR'
    FAILED_RESS_TEMPERATURE_INHIBIT='FAILED_RESSTemperatureInhibit'
    FAILED_EV_SHIFT_POSITION='FAILED_EVShiftPosition'
    FAILED__CHARGER_CONNECTOR_LOCK_FAULT='FAILED_ChargerConnectorLockFault'
    FAILED_EVRESS_MALFUNCTION='FAILED_EVRESSMalfunction'
    FAILED__CHARGING_CURRENTDIFFERENTIAL='FAILED_ChargingCurrentdifferential'
    FAILED__CHARGING_VOLTAGE_OUT_OF_RANGE='FAILED_ChargingVoltageOutOfRange'
    RESERVED_A='Reserved_A'
    RESERVED_B='Reserved_B'
    RESERVED_C='Reserved_C'
    FAILED__CHARGING_SYSTEM_INCOMPATIBILITY='FAILED_ChargingSystemIncompatibility'
    NO_DATA='NoData'


class DC_EVSEStatusCodeType(str, Enum):
    EVSE__NOT_READY='EVSE_NotReady'
    EVSE__READY='EVSE_Ready'
    EVSE__SHUTDOWN='EVSE_Shutdown'
    EVSE__UTILITY_INTERRUPT_EVENT='EVSE_UtilityInterruptEvent'
    EVSE__ISOLATION_MONITORING_ACTIVE='EVSE_IsolationMonitoringActive'
    EVSE__EMERGENCY_SHUTDOWN='EVSE_EmergencyShutdown'
    EVSE__MALFUNCTION='EVSE_Malfunction'
    RESERVED__8='Reserved_8'
    RESERVED__9='Reserved_9'
    RESERVED_A='Reserved_A'
    RESERVED_B='Reserved_B'
    RESERVED_C='Reserved_C'


class EVSENotificationType(str, Enum):
    NONE='None'
    STOP_CHARGING='StopCharging'
    RE_NEGOTIATION='ReNegotiation'


class EVSEProcessingType(str, Enum):
    FINISHED='Finished'
    ONGOING='Ongoing'
    ONGOING__WAITING_FOR_CUSTOMER_INTERACTION='Ongoing_WaitingForCustomerInteraction'


class EnergyTransferModeType(str, Enum):
    AC_SINGLE_PHASE_CORE='AC_single_phase_core'
    AC_THREE_PHASE_CORE='AC_three_phase_core'
    DC_CORE='DC_core'
    DC_EXTENDED='DC_extended'
    DC_COMBO_CORE='DC_combo_core'
    DC_UNIQUE='DC_unique'


class chargeProgressType(str, Enum):
    START='Start'
    STOP='Stop'
    RENEGOTIATE='Renegotiate'


class chargingSessionType(str, Enum):
    TERMINATE='Terminate'
    PAUSE='Pause'


class costKindType(str, Enum):
    RELATIVE_PRICE_PERCENTAGE='relativePricePercentage'
    RENEWABLE_GENERATION_PERCENTAGE='RenewableGenerationPercentage'
    CARBON_DIOXIDE_EMISSION='CarbonDioxideEmission'


class faultCodeType(str, Enum):
    PARSING_ERROR='ParsingError'
    NO_TLS_ROOT_CERTIFICAT_AVAILABLE='NoTLSRootCertificatAvailable'
    UNKNOWN_ERROR='UnknownError'


class isolationLevelType(str, Enum):
    INVALID='Invalid'
    VALID='Valid'
    WARNING='Warning'
    FAULT='Fault'
    NO_IMD='No_IMD'


class paymentOptionType(str, Enum):
    CONTRACT='Contract'
    EXTERNAL_PAYMENT='ExternalPayment'


class responseCodeType(str, Enum):
    OK='OK'
    OK__NEW_SESSION_ESTABLISHED='OK_NewSessionEstablished'
    OK__OLD_SESSION_JOINED='OK_OldSessionJoined'
    OK__CERTIFICATE_EXPIRES_SOON='OK_CertificateExpiresSoon'
    FAILED='FAILED'
    FAILED__SEQUENCE_ERROR='FAILED_SequenceError'
    FAILED__SERVICE_ID_INVALID='FAILED_ServiceIDInvalid'
    FAILED__UNKNOWN_SESSION='FAILED_UnknownSession'
    FAILED__SERVICE_SELECTION_INVALID='FAILED_ServiceSelectionInvalid'
    FAILED__PAYMENT_SELECTION_INVALID='FAILED_PaymentSelectionInvalid'
    FAILED__CERTIFICATE_EXPIRED='FAILED_CertificateExpired'
    FAILED__SIGNATURE_ERROR='FAILED_SignatureError'
    FAILED__NO_CERTIFICATE_AVAILABLE='FAILED_NoCertificateAvailable'
    FAILED__CERT_CHAIN_ERROR='FAILED_CertChainError'
    FAILED__CHALLENGE_INVALID='FAILED_ChallengeInvalid'
    FAILED__CONTRACT_CANCELED='FAILED_ContractCanceled'
    FAILED__WRONG_CHARGE_PARAMETER='FAILED_WrongChargeParameter'
    FAILED__POWER_DELIVERY_NOT_APPLIED='FAILED_PowerDeliveryNotApplied'
    FAILED__TARIFF_SELECTION_INVALID='FAILED_TariffSelectionInvalid'
    FAILED__CHARGING_PROFILE_INVALID='FAILED_ChargingProfileInvalid'
    FAILED__METERING_SIGNATURE_NOT_VALID='FAILED_MeteringSignatureNotValid'
    FAILED__NO_CHARGE_SERVICE_SELECTED='FAILED_NoChargeServiceSelected'
    FAILED__WRONG_ENERGY_TRANSFER_MODE='FAILED_WrongEnergyTransferMode'
    FAILED__CONTACTOR_ERROR='FAILED_ContactorError'
    FAILED__CERTIFICATE_NOT_ALLOWED_AT_THIS_EVSE='FAILED_CertificateNotAllowedAtThisEVSE'
    FAILED__CERTIFICATE_REVOKED='FAILED_CertificateRevoked'


class serviceCategoryType(str, Enum):
    EV_CHARGING='EVCharging'
    INTERNET='Internet'
    CONTRACT_CERTIFICATE='ContractCertificate'
    OTHER_CUSTOM='OtherCustom'


class unitSymbolType(str, Enum):
    H='h' # Time in hours
    M='m' # Time in minutes
    S='s' # Time in seconds
    A='A' # Current in Ampere
    V='V' # Voltage in Volt
    W='W' # Active power in Watt
    WH='Wh' # Real energy in Watt hours


class valueType(str, Enum):
    BOOL='bool'
    BYTE='byte'
    SHORT='short'
    INT='int'
    PHYSICAL_VALUE='physicalValue'
    STRING='string'


class V2G_Message(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Header=None, Body=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns7"
        self.Header = Header
        self.Header_nsprefix_ = "ns7"
        self.Body = Body
        self.Body_nsprefix_ = "ns7"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, V2G_Message)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if V2G_Message.subclass:
            return V2G_Message.subclass(*args_, **kwargs_)
        else:
            return V2G_Message(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Header(self):
        return self.Header
    def set_Header(self, Header):
        self.Header = Header
    def get_Body(self):
        return self.Body
    def set_Body(self, Body):
        self.Body = Body
    def _hasContent(self):
        if (
            self.Header is not None or
            self.Body is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ns8="urn:iso:15118:2:2013:MsgHeader"  xmlns:ns5="urn:iso:15118:2:2013:MsgBody" ', name_='V2G_Message', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('V2G_Message')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'V2G_Message':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='V2G_Message')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='V2G_Message', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='V2G_Message'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ns8="urn:iso:15118:2:2013:MsgHeader"  xmlns:ns5="urn:iso:15118:2:2013:MsgBody" ', name_='V2G_Message', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Header is not None:
            namespaceprefix_ = self.Header_nsprefix_ + ':' if (UseCapturedNS_ and self.Header_nsprefix_) else ''
            self.Header.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Header', pretty_print=pretty_print)
        if self.Body is not None:
            namespaceprefix_ = self.Body_nsprefix_ + ':' if (UseCapturedNS_ and self.Body_nsprefix_) else ''
            self.Body.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Body', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Header':
            obj_ = MessageHeaderType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Header = obj_
            obj_.original_tagname_ = 'Header'
        elif nodeName_ == 'Body':
            obj_ = BodyType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Body = obj_
            obj_.original_tagname_ = 'Body'
# end class V2G_Message


class MessageHeaderType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, SessionID=None, Notification=None, Signature=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns7"
        self.SessionID = SessionID
        self.validate_sessionIDType(self.SessionID)
        self.SessionID_nsprefix_ = "ns8"
        self.Notification = Notification
        self.Notification_nsprefix_ = "ns6"
        self.Signature = Signature
        self.Signature_nsprefix_ = "xmlsig"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MessageHeaderType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MessageHeaderType.subclass:
            return MessageHeaderType.subclass(*args_, **kwargs_)
        else:
            return MessageHeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_SessionID(self):
        return self.SessionID
    def set_SessionID(self, SessionID):
        self.SessionID = SessionID
    def get_Notification(self):
        return self.Notification
    def set_Notification(self, Notification):
        self.Notification = Notification
    def get_Signature(self):
        return self.Signature
    def set_Signature(self, Signature):
        self.Signature = Signature
    def validate_sessionIDType(self, value):
        result = True
        # Validate type sessionIDType, a restriction on xs:hexBinary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on sessionIDType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.SessionID is not None or
            self.Notification is not None or
            self.Signature is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns8="urn:iso:15118:2:2013:MsgHeader" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes"  xmlns:xmlsig="http://www.w3.org/2000/09/xmldsig#" ', name_='MessageHeaderType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MessageHeaderType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MessageHeaderType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MessageHeaderType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MessageHeaderType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MessageHeaderType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns8="urn:iso:15118:2:2013:MsgHeader" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes"  xmlns:xmlsig="http://www.w3.org/2000/09/xmldsig#" ', name_='MessageHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.SessionID is not None:
            namespaceprefix_ = self.SessionID_nsprefix_ + ':' if (UseCapturedNS_ and self.SessionID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSessionID>%s</%sSessionID>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SessionID), input_name='SessionID')), namespaceprefix_ , eol_))
        if self.Notification is not None:
            namespaceprefix_ = self.Notification_nsprefix_ + ':' if (UseCapturedNS_ and self.Notification_nsprefix_) else ''
            self.Notification.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Notification', pretty_print=pretty_print)
        if self.Signature is not None:
            namespaceprefix_ = self.Signature_nsprefix_ + ':' if (UseCapturedNS_ and self.Signature_nsprefix_) else ''
            self.Signature.export(outfile, level, namespaceprefix_='xmlsig:', namespacedef_='', name_='Signature', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'SessionID':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SessionID')
            value_ = self.gds_validate_string(value_, node, 'SessionID')
            self.SessionID = value_
            self.SessionID_nsprefix_ = child_.prefix
            # validate type sessionIDType
            self.validate_sessionIDType(self.SessionID)
        elif nodeName_ == 'Notification':
            obj_ = NotificationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Notification = obj_
            obj_.original_tagname_ = 'Notification'
        elif nodeName_ == 'Signature':
            obj_ = SignatureType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Signature = obj_
            obj_.original_tagname_ = 'Signature'
# end class MessageHeaderType


class ServiceType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ServiceID=None, ServiceName=None, ServiceCategory=None, ServiceScope=None, FreeService=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ServiceID = ServiceID
        self.validate_serviceIDType(self.ServiceID)
        self.ServiceID_nsprefix_ = None
        self.ServiceName = ServiceName
        self.validate_serviceNameType(self.ServiceName)
        self.ServiceName_nsprefix_ = None
        self.ServiceCategory = ServiceCategory
        self.validate_serviceCategoryType(self.ServiceCategory)
        self.ServiceCategory_nsprefix_ = None
        self.ServiceScope = ServiceScope
        self.validate_serviceScopeType(self.ServiceScope)
        self.ServiceScope_nsprefix_ = None
        self.FreeService = FreeService
        self.FreeService_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ServiceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ServiceType.subclass:
            return ServiceType.subclass(*args_, **kwargs_)
        else:
            return ServiceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ServiceID(self):
        return self.ServiceID
    def set_ServiceID(self, ServiceID):
        self.ServiceID = ServiceID
    def get_ServiceName(self):
        return self.ServiceName
    def set_ServiceName(self, ServiceName):
        self.ServiceName = ServiceName
    def get_ServiceCategory(self):
        return self.ServiceCategory
    def set_ServiceCategory(self, ServiceCategory):
        self.ServiceCategory = ServiceCategory
    def get_ServiceScope(self):
        return self.ServiceScope
    def set_ServiceScope(self, ServiceScope):
        self.ServiceScope = ServiceScope
    def get_FreeService(self):
        return self.FreeService
    def set_FreeService(self, FreeService):
        self.FreeService = FreeService
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def validate_serviceIDType(self, value):
        result = True
        # Validate type serviceIDType, a restriction on xs:unsignedShort.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def validate_serviceNameType(self, value):
        result = True
        # Validate type serviceNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on serviceNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_serviceCategoryType(self, value):
        result = True
        # Validate type serviceCategoryType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['EVCharging', 'Internet', 'ContractCertificate', 'OtherCustom']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on serviceCategoryType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_serviceScopeType(self, value):
        result = True
        # Validate type serviceScopeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 64:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on serviceScopeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.ServiceID is not None or
            self.ServiceName is not None or
            self.ServiceCategory is not None or
            self.ServiceScope is not None or
            self.FreeService is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='ServiceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ServiceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ServiceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ServiceType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ServiceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ServiceType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='ServiceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ServiceID is not None:
            namespaceprefix_ = self.ServiceID_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sServiceID>%s</%sServiceID>%s' % (namespaceprefix_ , self.gds_format_integer(self.ServiceID, input_name='ServiceID'), namespaceprefix_ , eol_))
        if self.ServiceName is not None:
            namespaceprefix_ = self.ServiceName_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sServiceName>%s</%sServiceName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ServiceName), input_name='ServiceName')), namespaceprefix_ , eol_))
        if self.ServiceCategory is not None:
            namespaceprefix_ = self.ServiceCategory_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceCategory_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sServiceCategory>%s</%sServiceCategory>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ServiceCategory), input_name='ServiceCategory')), namespaceprefix_ , eol_))
        if self.ServiceScope is not None:
            namespaceprefix_ = self.ServiceScope_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceScope_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sServiceScope>%s</%sServiceScope>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ServiceScope), input_name='ServiceScope')), namespaceprefix_ , eol_))
        if self.FreeService is not None:
            namespaceprefix_ = self.FreeService_nsprefix_ + ':' if (UseCapturedNS_ and self.FreeService_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sFreeService>%s</%sFreeService>%s' % (namespaceprefix_ , self.gds_format_boolean(self.FreeService, input_name='FreeService'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ServiceID' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'ServiceID')
            ival_ = self.gds_validate_integer(ival_, node, 'ServiceID')
            self.ServiceID = ival_
            self.ServiceID_nsprefix_ = child_.prefix
            # validate type serviceIDType
            self.validate_serviceIDType(self.ServiceID)
        elif nodeName_ == 'ServiceName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ServiceName')
            value_ = self.gds_validate_string(value_, node, 'ServiceName')
            self.ServiceName = value_
            self.ServiceName_nsprefix_ = child_.prefix
            # validate type serviceNameType
            self.validate_serviceNameType(self.ServiceName)
        elif nodeName_ == 'ServiceCategory':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ServiceCategory')
            value_ = self.gds_validate_string(value_, node, 'ServiceCategory')
            self.ServiceCategory = value_
            self.ServiceCategory_nsprefix_ = child_.prefix
            # validate type serviceCategoryType
            self.validate_serviceCategoryType(self.ServiceCategory)
        elif nodeName_ == 'ServiceScope':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ServiceScope')
            value_ = self.gds_validate_string(value_, node, 'ServiceScope')
            self.ServiceScope = value_
            self.ServiceScope_nsprefix_ = child_.prefix
            # validate type serviceScopeType
            self.validate_serviceScopeType(self.ServiceScope)
        elif nodeName_ == 'FreeService':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'FreeService')
            ival_ = self.gds_validate_boolean(ival_, node, 'FreeService')
            self.FreeService = ival_
            self.FreeService_nsprefix_ = child_.prefix
# end class ServiceType


class ServiceListType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Service=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Service is None:
            self.Service = []
        else:
            self.Service = Service
        self.Service_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ServiceListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ServiceListType.subclass:
            return ServiceListType.subclass(*args_, **kwargs_)
        else:
            return ServiceListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Service(self):
        return self.Service
    def set_Service(self, Service):
        self.Service = Service
    def add_Service(self, value):
        self.Service.append(value)
    def insert_Service_at(self, index, value):
        self.Service.insert(index, value)
    def replace_Service_at(self, index, value):
        self.Service[index] = value
    def _hasContent(self):
        if (
            self.Service
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='ServiceListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ServiceListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ServiceListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ServiceListType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ServiceListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ServiceListType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='ServiceListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Service_ in self.Service:
            namespaceprefix_ = self.Service_nsprefix_ + ':' if (UseCapturedNS_ and self.Service_nsprefix_) else ''
            Service_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Service', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Service':
            class_obj_ = self.get_class_obj_(child_, ServiceType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Service.append(obj_)
            obj_.original_tagname_ = 'Service'
# end class ServiceListType


class SelectedServiceListType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, SelectedService=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if SelectedService is None:
            self.SelectedService = []
        else:
            self.SelectedService = SelectedService
        self.SelectedService_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SelectedServiceListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SelectedServiceListType.subclass:
            return SelectedServiceListType.subclass(*args_, **kwargs_)
        else:
            return SelectedServiceListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_SelectedService(self):
        return self.SelectedService
    def set_SelectedService(self, SelectedService):
        self.SelectedService = SelectedService
    def add_SelectedService(self, value):
        self.SelectedService.append(value)
    def insert_SelectedService_at(self, index, value):
        self.SelectedService.insert(index, value)
    def replace_SelectedService_at(self, index, value):
        self.SelectedService[index] = value
    def _hasContent(self):
        if (
            self.SelectedService
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='SelectedServiceListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SelectedServiceListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SelectedServiceListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SelectedServiceListType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SelectedServiceListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SelectedServiceListType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='SelectedServiceListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for SelectedService_ in self.SelectedService:
            namespaceprefix_ = self.SelectedService_nsprefix_ + ':' if (UseCapturedNS_ and self.SelectedService_nsprefix_) else ''
            SelectedService_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SelectedService', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'SelectedService':
            obj_ = SelectedServiceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SelectedService.append(obj_)
            obj_.original_tagname_ = 'SelectedService'
# end class SelectedServiceListType


class SelectedServiceType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ServiceID=None, ParameterSetID=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ServiceID = ServiceID
        self.validate_serviceIDType(self.ServiceID)
        self.ServiceID_nsprefix_ = None
        self.ParameterSetID = ParameterSetID
        self.ParameterSetID_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SelectedServiceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SelectedServiceType.subclass:
            return SelectedServiceType.subclass(*args_, **kwargs_)
        else:
            return SelectedServiceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ServiceID(self):
        return self.ServiceID
    def set_ServiceID(self, ServiceID):
        self.ServiceID = ServiceID
    def get_ParameterSetID(self):
        return self.ParameterSetID
    def set_ParameterSetID(self, ParameterSetID):
        self.ParameterSetID = ParameterSetID
    def validate_serviceIDType(self, value):
        result = True
        # Validate type serviceIDType, a restriction on xs:unsignedShort.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def _hasContent(self):
        if (
            self.ServiceID is not None or
            self.ParameterSetID is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='SelectedServiceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SelectedServiceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SelectedServiceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SelectedServiceType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SelectedServiceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SelectedServiceType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='SelectedServiceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ServiceID is not None:
            namespaceprefix_ = self.ServiceID_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sServiceID>%s</%sServiceID>%s' % (namespaceprefix_ , self.gds_format_integer(self.ServiceID, input_name='ServiceID'), namespaceprefix_ , eol_))
        if self.ParameterSetID is not None:
            namespaceprefix_ = self.ParameterSetID_nsprefix_ + ':' if (UseCapturedNS_ and self.ParameterSetID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sParameterSetID>%s</%sParameterSetID>%s' % (namespaceprefix_ , self.gds_format_integer(self.ParameterSetID, input_name='ParameterSetID'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ServiceID' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'ServiceID')
            ival_ = self.gds_validate_integer(ival_, node, 'ServiceID')
            self.ServiceID = ival_
            self.ServiceID_nsprefix_ = child_.prefix
            # validate type serviceIDType
            self.validate_serviceIDType(self.ServiceID)
        elif nodeName_ == 'ParameterSetID' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'ParameterSetID')
            ival_ = self.gds_validate_integer(ival_, node, 'ParameterSetID')
            self.ParameterSetID = ival_
            self.ParameterSetID_nsprefix_ = child_.prefix
# end class SelectedServiceType


class ServiceParameterListType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ParameterSet=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if ParameterSet is None:
            self.ParameterSet = []
        else:
            self.ParameterSet = ParameterSet
        self.ParameterSet_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ServiceParameterListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ServiceParameterListType.subclass:
            return ServiceParameterListType.subclass(*args_, **kwargs_)
        else:
            return ServiceParameterListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ParameterSet(self):
        return self.ParameterSet
    def set_ParameterSet(self, ParameterSet):
        self.ParameterSet = ParameterSet
    def add_ParameterSet(self, value):
        self.ParameterSet.append(value)
    def insert_ParameterSet_at(self, index, value):
        self.ParameterSet.insert(index, value)
    def replace_ParameterSet_at(self, index, value):
        self.ParameterSet[index] = value
    def _hasContent(self):
        if (
            self.ParameterSet
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='ServiceParameterListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ServiceParameterListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ServiceParameterListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ServiceParameterListType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ServiceParameterListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ServiceParameterListType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='ServiceParameterListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for ParameterSet_ in self.ParameterSet:
            namespaceprefix_ = self.ParameterSet_nsprefix_ + ':' if (UseCapturedNS_ and self.ParameterSet_nsprefix_) else ''
            ParameterSet_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ParameterSet', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ParameterSet':
            obj_ = ParameterSetType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParameterSet.append(obj_)
            obj_.original_tagname_ = 'ParameterSet'
# end class ServiceParameterListType


class ParameterSetType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ParameterSetID=None, Parameter=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ParameterSetID = ParameterSetID
        self.ParameterSetID_nsprefix_ = None
        if Parameter is None:
            self.Parameter = []
        else:
            self.Parameter = Parameter
        self.Parameter_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ParameterSetType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ParameterSetType.subclass:
            return ParameterSetType.subclass(*args_, **kwargs_)
        else:
            return ParameterSetType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ParameterSetID(self):
        return self.ParameterSetID
    def set_ParameterSetID(self, ParameterSetID):
        self.ParameterSetID = ParameterSetID
    def get_Parameter(self):
        return self.Parameter
    def set_Parameter(self, Parameter):
        self.Parameter = Parameter
    def add_Parameter(self, value):
        self.Parameter.append(value)
    def insert_Parameter_at(self, index, value):
        self.Parameter.insert(index, value)
    def replace_Parameter_at(self, index, value):
        self.Parameter[index] = value
    def _hasContent(self):
        if (
            self.ParameterSetID is not None or
            self.Parameter
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='ParameterSetType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ParameterSetType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ParameterSetType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ParameterSetType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ParameterSetType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ParameterSetType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='ParameterSetType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ParameterSetID is not None:
            namespaceprefix_ = self.ParameterSetID_nsprefix_ + ':' if (UseCapturedNS_ and self.ParameterSetID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sParameterSetID>%s</%sParameterSetID>%s' % (namespaceprefix_ , self.gds_format_integer(self.ParameterSetID, input_name='ParameterSetID'), namespaceprefix_ , eol_))
        for Parameter_ in self.Parameter:
            namespaceprefix_ = self.Parameter_nsprefix_ + ':' if (UseCapturedNS_ and self.Parameter_nsprefix_) else ''
            Parameter_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Parameter', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ParameterSetID' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'ParameterSetID')
            ival_ = self.gds_validate_integer(ival_, node, 'ParameterSetID')
            self.ParameterSetID = ival_
            self.ParameterSetID_nsprefix_ = child_.prefix
        elif nodeName_ == 'Parameter':
            obj_ = ParameterType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Parameter.append(obj_)
            obj_.original_tagname_ = 'Parameter'
# end class ParameterSetType


class ParameterType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Name=None, boolValue=None, byteValue=None, shortValue=None, intValue=None, physicalValue=None, stringValue=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Name = _cast(None, Name)
        self.Name_nsprefix_ = None
        self.boolValue = boolValue
        self.boolValue_nsprefix_ = None
        self.byteValue = byteValue
        self.byteValue_nsprefix_ = None
        self.shortValue = shortValue
        self.shortValue_nsprefix_ = None
        self.intValue = intValue
        self.intValue_nsprefix_ = None
        self.physicalValue = physicalValue
        self.physicalValue_nsprefix_ = None
        self.stringValue = stringValue
        self.stringValue_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ParameterType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ParameterType.subclass:
            return ParameterType.subclass(*args_, **kwargs_)
        else:
            return ParameterType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_boolValue(self):
        return self.boolValue
    def set_boolValue(self, boolValue):
        self.boolValue = boolValue
    def get_byteValue(self):
        return self.byteValue
    def set_byteValue(self, byteValue):
        self.byteValue = byteValue
    def get_shortValue(self):
        return self.shortValue
    def set_shortValue(self, shortValue):
        self.shortValue = shortValue
    def get_intValue(self):
        return self.intValue
    def set_intValue(self, intValue):
        self.intValue = intValue
    def get_physicalValue(self):
        return self.physicalValue
    def set_physicalValue(self, physicalValue):
        self.physicalValue = physicalValue
    def get_stringValue(self):
        return self.stringValue
    def set_stringValue(self, stringValue):
        self.stringValue = stringValue
    def get_Name(self):
        return self.Name
    def set_Name(self, Name):
        self.Name = Name
    def _hasContent(self):
        if (
            self.boolValue is not None or
            self.byteValue is not None or
            self.shortValue is not None or
            self.intValue is not None or
            self.physicalValue is not None or
            self.stringValue is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='ParameterType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ParameterType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ParameterType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ParameterType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ParameterType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ParameterType'):
        if self.Name is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            outfile.write(' Name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Name), input_name='Name')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='ParameterType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.boolValue is not None:
            namespaceprefix_ = self.boolValue_nsprefix_ + ':' if (UseCapturedNS_ and self.boolValue_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sboolValue>%s</%sboolValue>%s' % (namespaceprefix_ , self.gds_format_boolean(self.boolValue, input_name='boolValue'), namespaceprefix_ , eol_))
        if self.byteValue is not None:
            namespaceprefix_ = self.byteValue_nsprefix_ + ':' if (UseCapturedNS_ and self.byteValue_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbyteValue>%s</%sbyteValue>%s' % (namespaceprefix_ , self.gds_format_integer(self.byteValue, input_name='byteValue'), namespaceprefix_ , eol_))
        if self.shortValue is not None:
            namespaceprefix_ = self.shortValue_nsprefix_ + ':' if (UseCapturedNS_ and self.shortValue_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sshortValue>%s</%sshortValue>%s' % (namespaceprefix_ , self.gds_format_integer(self.shortValue, input_name='shortValue'), namespaceprefix_ , eol_))
        if self.intValue is not None:
            namespaceprefix_ = self.intValue_nsprefix_ + ':' if (UseCapturedNS_ and self.intValue_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sintValue>%s</%sintValue>%s' % (namespaceprefix_ , self.gds_format_integer(self.intValue, input_name='intValue'), namespaceprefix_ , eol_))
        if self.physicalValue is not None:
            namespaceprefix_ = self.physicalValue_nsprefix_ + ':' if (UseCapturedNS_ and self.physicalValue_nsprefix_) else ''
            self.physicalValue.export(outfile, level, namespaceprefix_, namespacedef_='', name_='physicalValue', pretty_print=pretty_print)
        if self.stringValue is not None:
            namespaceprefix_ = self.stringValue_nsprefix_ + ':' if (UseCapturedNS_ and self.stringValue_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstringValue>%s</%sstringValue>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.stringValue), input_name='stringValue')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Name', node)
        if value is not None and 'Name' not in already_processed:
            already_processed.add('Name')
            self.Name = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'boolValue':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'boolValue')
            ival_ = self.gds_validate_boolean(ival_, node, 'boolValue')
            self.boolValue = ival_
            self.boolValue_nsprefix_ = child_.prefix
        elif nodeName_ == 'byteValue' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'byteValue')
            ival_ = self.gds_validate_integer(ival_, node, 'byteValue')
            self.byteValue = ival_
            self.byteValue_nsprefix_ = child_.prefix
        elif nodeName_ == 'shortValue' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'shortValue')
            ival_ = self.gds_validate_integer(ival_, node, 'shortValue')
            self.shortValue = ival_
            self.shortValue_nsprefix_ = child_.prefix
        elif nodeName_ == 'intValue' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'intValue')
            ival_ = self.gds_validate_integer(ival_, node, 'intValue')
            self.intValue = ival_
            self.intValue_nsprefix_ = child_.prefix
        elif nodeName_ == 'physicalValue':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.physicalValue = obj_
            obj_.original_tagname_ = 'physicalValue'
        elif nodeName_ == 'stringValue':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'stringValue')
            value_ = self.gds_validate_string(value_, node, 'stringValue')
            self.stringValue = value_
            self.stringValue_nsprefix_ = child_.prefix
# end class ParameterType


class ChargeServiceType(ServiceType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = ServiceType
    def __init__(self, ServiceID=None, ServiceName=None, ServiceCategory=None, ServiceScope=None, FreeService=None, SupportedEnergyTransferMode=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("ChargeServiceType"), self).__init__(ServiceID, ServiceName, ServiceCategory, ServiceScope, FreeService,  **kwargs_)
        self.SupportedEnergyTransferMode = SupportedEnergyTransferMode
        self.SupportedEnergyTransferMode_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ChargeServiceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ChargeServiceType.subclass:
            return ChargeServiceType.subclass(*args_, **kwargs_)
        else:
            return ChargeServiceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_SupportedEnergyTransferMode(self):
        return self.SupportedEnergyTransferMode
    def set_SupportedEnergyTransferMode(self, SupportedEnergyTransferMode):
        self.SupportedEnergyTransferMode = SupportedEnergyTransferMode
    def _hasContent(self):
        if (
            self.SupportedEnergyTransferMode is not None or
            super(ChargeServiceType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='ChargeServiceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ChargeServiceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ChargeServiceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ChargeServiceType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ChargeServiceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ChargeServiceType'):
        super(ChargeServiceType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ChargeServiceType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='ChargeServiceType', fromsubclass_=False, pretty_print=True):
        super(ChargeServiceType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.SupportedEnergyTransferMode is not None:
            namespaceprefix_ = self.SupportedEnergyTransferMode_nsprefix_ + ':' if (UseCapturedNS_ and self.SupportedEnergyTransferMode_nsprefix_) else ''
            self.SupportedEnergyTransferMode.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SupportedEnergyTransferMode', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(ChargeServiceType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'SupportedEnergyTransferMode':
            obj_ = SupportedEnergyTransferModeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SupportedEnergyTransferMode = obj_
            obj_.original_tagname_ = 'SupportedEnergyTransferMode'
        super(ChargeServiceType, self)._buildChildren(child_, node, nodeName_, True)
# end class ChargeServiceType


class SupportedEnergyTransferModeType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, EnergyTransferMode=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if EnergyTransferMode is None:
            self.EnergyTransferMode = []
        else:
            self.EnergyTransferMode = EnergyTransferMode
        self.EnergyTransferMode_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SupportedEnergyTransferModeType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SupportedEnergyTransferModeType.subclass:
            return SupportedEnergyTransferModeType.subclass(*args_, **kwargs_)
        else:
            return SupportedEnergyTransferModeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_EnergyTransferMode(self):
        return self.EnergyTransferMode
    def set_EnergyTransferMode(self, EnergyTransferMode):
        self.EnergyTransferMode = EnergyTransferMode
    def add_EnergyTransferMode(self, value):
        self.EnergyTransferMode.append(value)
    def insert_EnergyTransferMode_at(self, index, value):
        self.EnergyTransferMode.insert(index, value)
    def replace_EnergyTransferMode_at(self, index, value):
        self.EnergyTransferMode[index] = value
    def validate_EnergyTransferModeType(self, value):
        result = True
        # Validate type EnergyTransferModeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['AC_single_phase_core', 'AC_three_phase_core', 'DC_core', 'DC_extended', 'DC_combo_core', 'DC_unique']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on EnergyTransferModeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.EnergyTransferMode
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='SupportedEnergyTransferModeType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SupportedEnergyTransferModeType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SupportedEnergyTransferModeType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SupportedEnergyTransferModeType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SupportedEnergyTransferModeType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SupportedEnergyTransferModeType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='SupportedEnergyTransferModeType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for EnergyTransferMode_ in self.EnergyTransferMode:
            namespaceprefix_ = self.EnergyTransferMode_nsprefix_ + ':' if (UseCapturedNS_ and self.EnergyTransferMode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEnergyTransferMode>%s</%sEnergyTransferMode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(EnergyTransferMode_), input_name='EnergyTransferMode')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'EnergyTransferMode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'EnergyTransferMode')
            value_ = self.gds_validate_string(value_, node, 'EnergyTransferMode')
            self.EnergyTransferMode.append(value_)
            self.EnergyTransferMode_nsprefix_ = child_.prefix
            # validate type EnergyTransferModeType
            self.validate_EnergyTransferModeType(self.EnergyTransferMode[-1])
# end class SupportedEnergyTransferModeType


class ContractSignatureEncryptedPrivateKeyType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Id=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ContractSignatureEncryptedPrivateKeyType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ContractSignatureEncryptedPrivateKeyType.subclass:
            return ContractSignatureEncryptedPrivateKeyType.subclass(*args_, **kwargs_)
        else:
            return ContractSignatureEncryptedPrivateKeyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_privateKeyType(self, value):
        result = True
        return result
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ContractSignatureEncryptedPrivateKeyType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ContractSignatureEncryptedPrivateKeyType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ContractSignatureEncryptedPrivateKeyType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ContractSignatureEncryptedPrivateKeyType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ContractSignatureEncryptedPrivateKeyType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ContractSignatureEncryptedPrivateKeyType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ContractSignatureEncryptedPrivateKeyType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class ContractSignatureEncryptedPrivateKeyType


class DiffieHellmanPublickeyType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Id=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DiffieHellmanPublickeyType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DiffieHellmanPublickeyType.subclass:
            return DiffieHellmanPublickeyType.subclass(*args_, **kwargs_)
        else:
            return DiffieHellmanPublickeyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_dHpublickeyType(self, value):
        result = True
        return result
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DiffieHellmanPublickeyType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DiffieHellmanPublickeyType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DiffieHellmanPublickeyType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DiffieHellmanPublickeyType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DiffieHellmanPublickeyType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DiffieHellmanPublickeyType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DiffieHellmanPublickeyType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class DiffieHellmanPublickeyType


class EMAIDType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Id=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, EMAIDType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if EMAIDType.subclass:
            return EMAIDType.subclass(*args_, **kwargs_)
        else:
            return EMAIDType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_eMAIDType(self, value):
        result = True
        # Validate type eMAIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on eMAIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 14:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on eMAIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='EMAIDType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('EMAIDType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'EMAIDType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='EMAIDType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='EMAIDType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='EMAIDType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='EMAIDType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class EMAIDType


class CertificateChainType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Id=None, Certificate=None, SubCertificates=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.Certificate = Certificate
        self.validate_certificateType(self.Certificate)
        self.Certificate_nsprefix_ = None
        self.SubCertificates = SubCertificates
        self.SubCertificates_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CertificateChainType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CertificateChainType.subclass:
            return CertificateChainType.subclass(*args_, **kwargs_)
        else:
            return CertificateChainType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Certificate(self):
        return self.Certificate
    def set_Certificate(self, Certificate):
        self.Certificate = Certificate
    def get_SubCertificates(self):
        return self.SubCertificates
    def set_SubCertificates(self, SubCertificates):
        self.SubCertificates = SubCertificates
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def validate_certificateType(self, value):
        result = True
        # Validate type certificateType, a restriction on xs:base64Binary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 800:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on certificateType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.Certificate is not None or
            self.SubCertificates is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:ns5="urn:iso:15118:2:2013:MsgBody" ', name_='CertificateChainType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CertificateChainType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CertificateChainType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CertificateChainType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CertificateChainType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CertificateChainType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='CertificateChainType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Certificate is not None:
            namespaceprefix_ = self.Certificate_nsprefix_ + ':' if (UseCapturedNS_ and self.Certificate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCertificate>%s</%sCertificate>%s' % (namespaceprefix_ , self.gds_format_base64(self.Certificate, input_name='Certificate'), namespaceprefix_ , eol_))
        if self.SubCertificates is not None:
            namespaceprefix_ = self.SubCertificates_nsprefix_ + ':' if (UseCapturedNS_ and self.SubCertificates_nsprefix_) else ''
            self.SubCertificates.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SubCertificates', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Certificate':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Certificate')
            else:
                bval_ = None
            self.Certificate = bval_
            self.Certificate_nsprefix_ = child_.prefix
            # validate type certificateType
            self.validate_certificateType(self.Certificate)
        elif nodeName_ == 'SubCertificates':
            obj_ = SubCertificatesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SubCertificates = obj_
            obj_.original_tagname_ = 'SubCertificates'
# end class CertificateChainType


class SubCertificatesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Certificate=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Certificate is None:
            self.Certificate = []
        else:
            self.Certificate = Certificate
        self.Certificate_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SubCertificatesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SubCertificatesType.subclass:
            return SubCertificatesType.subclass(*args_, **kwargs_)
        else:
            return SubCertificatesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Certificate(self):
        return self.Certificate
    def set_Certificate(self, Certificate):
        self.Certificate = Certificate
    def add_Certificate(self, value):
        self.Certificate.append(value)
    def insert_Certificate_at(self, index, value):
        self.Certificate.insert(index, value)
    def replace_Certificate_at(self, index, value):
        self.Certificate[index] = value
    def validate_certificateType(self, value):
        result = True
        # Validate type certificateType, a restriction on xs:base64Binary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 800:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on certificateType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.Certificate
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='SubCertificatesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SubCertificatesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SubCertificatesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SubCertificatesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SubCertificatesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SubCertificatesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='SubCertificatesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Certificate_ in self.Certificate:
            namespaceprefix_ = self.Certificate_nsprefix_ + ':' if (UseCapturedNS_ and self.Certificate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCertificate>%s</%sCertificate>%s' % (namespaceprefix_ , self.gds_format_base64(Certificate_, input_name='Certificate'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Certificate':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Certificate')
            else:
                bval_ = None
            self.Certificate.append(bval_)
            self.Certificate_nsprefix_ = child_.prefix
            # validate type certificateType
            self.validate_certificateType(self.Certificate[-1])
# end class SubCertificatesType


class ListOfRootCertificateIDsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, RootCertificateID=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if RootCertificateID is None:
            self.RootCertificateID = []
        else:
            self.RootCertificateID = RootCertificateID
        self.RootCertificateID_nsprefix_ = "xmlsig"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ListOfRootCertificateIDsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ListOfRootCertificateIDsType.subclass:
            return ListOfRootCertificateIDsType.subclass(*args_, **kwargs_)
        else:
            return ListOfRootCertificateIDsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_RootCertificateID(self):
        return self.RootCertificateID
    def set_RootCertificateID(self, RootCertificateID):
        self.RootCertificateID = RootCertificateID
    def add_RootCertificateID(self, value):
        self.RootCertificateID.append(value)
    def insert_RootCertificateID_at(self, index, value):
        self.RootCertificateID.insert(index, value)
    def replace_RootCertificateID_at(self, index, value):
        self.RootCertificateID[index] = value
    def _hasContent(self):
        if (
            self.RootCertificateID
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:xmlsig="http://www.w3.org/2000/09/xmldsig#" ', name_='ListOfRootCertificateIDsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ListOfRootCertificateIDsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ListOfRootCertificateIDsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ListOfRootCertificateIDsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ListOfRootCertificateIDsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ListOfRootCertificateIDsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:xmlsig="http://www.w3.org/2000/09/xmldsig#" ', name_='ListOfRootCertificateIDsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for RootCertificateID_ in self.RootCertificateID:
            namespaceprefix_ = self.RootCertificateID_nsprefix_ + ':' if (UseCapturedNS_ and self.RootCertificateID_nsprefix_) else ''
            RootCertificateID_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='RootCertificateID', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'RootCertificateID':
            obj_ = X509IssuerSerialType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.RootCertificateID.append(obj_)
            obj_.original_tagname_ = 'RootCertificateID'
# end class ListOfRootCertificateIDsType


class MeterInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, MeterID=None, MeterReading=None, SigMeterReading=None, MeterStatus=None, TMeter=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.MeterID = MeterID
        self.validate_meterIDType(self.MeterID)
        self.MeterID_nsprefix_ = None
        self.MeterReading = MeterReading
        self.MeterReading_nsprefix_ = None
        self.SigMeterReading = SigMeterReading
        self.validate_sigMeterReadingType(self.SigMeterReading)
        self.SigMeterReading_nsprefix_ = None
        self.MeterStatus = MeterStatus
        self.validate_meterStatusType(self.MeterStatus)
        self.MeterStatus_nsprefix_ = None
        self.TMeter = TMeter
        self.TMeter_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MeterInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MeterInfoType.subclass:
            return MeterInfoType.subclass(*args_, **kwargs_)
        else:
            return MeterInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_MeterID(self):
        return self.MeterID
    def set_MeterID(self, MeterID):
        self.MeterID = MeterID
    def get_MeterReading(self):
        return self.MeterReading
    def set_MeterReading(self, MeterReading):
        self.MeterReading = MeterReading
    def get_SigMeterReading(self):
        return self.SigMeterReading
    def set_SigMeterReading(self, SigMeterReading):
        self.SigMeterReading = SigMeterReading
    def get_MeterStatus(self):
        return self.MeterStatus
    def set_MeterStatus(self, MeterStatus):
        self.MeterStatus = MeterStatus
    def get_TMeter(self):
        return self.TMeter
    def set_TMeter(self, TMeter):
        self.TMeter = TMeter
    def validate_meterIDType(self, value):
        result = True
        # Validate type meterIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on meterIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_sigMeterReadingType(self, value):
        result = True
        # Validate type sigMeterReadingType, a restriction on xs:base64Binary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 64:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on sigMeterReadingType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_meterStatusType(self, value):
        result = True
        # Validate type meterStatusType, a restriction on xs:short.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def _hasContent(self):
        if (
            self.MeterID is not None or
            self.MeterReading is not None or
            self.SigMeterReading is not None or
            self.MeterStatus is not None or
            self.TMeter is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='MeterInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MeterInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MeterInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MeterInfoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MeterInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MeterInfoType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='MeterInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.MeterID is not None:
            namespaceprefix_ = self.MeterID_nsprefix_ + ':' if (UseCapturedNS_ and self.MeterID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMeterID>%s</%sMeterID>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.MeterID), input_name='MeterID')), namespaceprefix_ , eol_))
        if self.MeterReading is not None:
            namespaceprefix_ = self.MeterReading_nsprefix_ + ':' if (UseCapturedNS_ and self.MeterReading_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMeterReading>%s</%sMeterReading>%s' % (namespaceprefix_ , self.gds_format_integer(self.MeterReading, input_name='MeterReading'), namespaceprefix_ , eol_))
        if self.SigMeterReading is not None:
            namespaceprefix_ = self.SigMeterReading_nsprefix_ + ':' if (UseCapturedNS_ and self.SigMeterReading_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSigMeterReading>%s</%sSigMeterReading>%s' % (namespaceprefix_ , self.gds_format_base64(self.SigMeterReading, input_name='SigMeterReading'), namespaceprefix_ , eol_))
        if self.MeterStatus is not None:
            namespaceprefix_ = self.MeterStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.MeterStatus_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMeterStatus>%s</%sMeterStatus>%s' % (namespaceprefix_ , self.gds_format_integer(self.MeterStatus, input_name='MeterStatus'), namespaceprefix_ , eol_))
        if self.TMeter is not None:
            namespaceprefix_ = self.TMeter_nsprefix_ + ':' if (UseCapturedNS_ and self.TMeter_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTMeter>%s</%sTMeter>%s' % (namespaceprefix_ , self.gds_format_integer(self.TMeter, input_name='TMeter'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'MeterID':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'MeterID')
            value_ = self.gds_validate_string(value_, node, 'MeterID')
            self.MeterID = value_
            self.MeterID_nsprefix_ = child_.prefix
            # validate type meterIDType
            self.validate_meterIDType(self.MeterID)
        elif nodeName_ == 'MeterReading' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'MeterReading')
            ival_ = self.gds_validate_integer(ival_, node, 'MeterReading')
            self.MeterReading = ival_
            self.MeterReading_nsprefix_ = child_.prefix
        elif nodeName_ == 'SigMeterReading':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'SigMeterReading')
            else:
                bval_ = None
            self.SigMeterReading = bval_
            self.SigMeterReading_nsprefix_ = child_.prefix
            # validate type sigMeterReadingType
            self.validate_sigMeterReadingType(self.SigMeterReading)
        elif nodeName_ == 'MeterStatus' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'MeterStatus')
            ival_ = self.gds_validate_integer(ival_, node, 'MeterStatus')
            self.MeterStatus = ival_
            self.MeterStatus_nsprefix_ = child_.prefix
            # validate type meterStatusType
            self.validate_meterStatusType(self.MeterStatus)
        elif nodeName_ == 'TMeter' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'TMeter')
            ival_ = self.gds_validate_integer(ival_, node, 'TMeter')
            self.TMeter = ival_
            self.TMeter_nsprefix_ = child_.prefix
# end class MeterInfoType


class PhysicalValueType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Multiplier=None, Unit=None, Value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Multiplier = Multiplier
        self.validate_unitMultiplierType(self.Multiplier)
        self.Multiplier_nsprefix_ = None
        self.Unit = Unit
        self.validate_unitSymbolType(self.Unit)
        self.Unit_nsprefix_ = None
        self.Value = Value
        self.Value_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PhysicalValueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PhysicalValueType.subclass:
            return PhysicalValueType.subclass(*args_, **kwargs_)
        else:
            return PhysicalValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Multiplier(self):
        return self.Multiplier
    def set_Multiplier(self, Multiplier):
        self.Multiplier = Multiplier
    def get_Unit(self):
        return self.Unit
    def set_Unit(self, Unit):
        self.Unit = Unit
    def get_Value(self):
        return self.Value
    def set_Value(self, Value):
        self.Value = Value
    def validate_unitMultiplierType(self, value):
        result = True
        # Validate type unitMultiplierType, a restriction on xs:byte.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < -3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on unitMultiplierType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on unitMultiplierType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_unitSymbolType(self, value):
        result = True
        # Validate type unitSymbolType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['h', 'm', 's', 'A', 'V', 'W', 'Wh']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on unitSymbolType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.Multiplier is not None or
            self.Unit is not None or
            self.Value is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='PhysicalValueType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PhysicalValueType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PhysicalValueType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PhysicalValueType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PhysicalValueType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PhysicalValueType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='PhysicalValueType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Multiplier is not None:
            namespaceprefix_ = self.Multiplier_nsprefix_ + ':' if (UseCapturedNS_ and self.Multiplier_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMultiplier>%s</%sMultiplier>%s' % (namespaceprefix_ , self.gds_format_integer(self.Multiplier, input_name='Multiplier'), namespaceprefix_ , eol_))
        if self.Unit is not None:
            namespaceprefix_ = self.Unit_nsprefix_ + ':' if (UseCapturedNS_ and self.Unit_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sUnit>%s</%sUnit>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Unit), input_name='Unit')), namespaceprefix_ , eol_))
        if self.Value is not None:
            namespaceprefix_ = self.Value_nsprefix_ + ':' if (UseCapturedNS_ and self.Value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValue>%s</%sValue>%s' % (namespaceprefix_ , self.gds_format_integer(self.Value, input_name='Value'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Multiplier' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Multiplier')
            ival_ = self.gds_validate_integer(ival_, node, 'Multiplier')
            self.Multiplier = ival_
            self.Multiplier_nsprefix_ = child_.prefix
            # validate type unitMultiplierType
            self.validate_unitMultiplierType(self.Multiplier)
        elif nodeName_ == 'Unit':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Unit')
            value_ = self.gds_validate_string(value_, node, 'Unit')
            self.Unit = value_
            self.Unit_nsprefix_ = child_.prefix
            # validate type unitSymbolType
            self.validate_unitSymbolType(self.Unit)
        elif nodeName_ == 'Value' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Value')
            ival_ = self.gds_validate_integer(ival_, node, 'Value')
            self.Value = ival_
            self.Value_nsprefix_ = child_.prefix
# end class PhysicalValueType


class NotificationType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, FaultCode=None, FaultMsg=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.FaultCode = FaultCode
        self.validate_faultCodeType(self.FaultCode)
        self.FaultCode_nsprefix_ = None
        self.FaultMsg = FaultMsg
        self.validate_faultMsgType(self.FaultMsg)
        self.FaultMsg_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NotificationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NotificationType.subclass:
            return NotificationType.subclass(*args_, **kwargs_)
        else:
            return NotificationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_FaultCode(self):
        return self.FaultCode
    def set_FaultCode(self, FaultCode):
        self.FaultCode = FaultCode
    def get_FaultMsg(self):
        return self.FaultMsg
    def set_FaultMsg(self, FaultMsg):
        self.FaultMsg = FaultMsg
    def validate_faultCodeType(self, value):
        result = True
        # Validate type faultCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['ParsingError', 'NoTLSRootCertificatAvailable', 'UnknownError']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on faultCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_faultMsgType(self, value):
        result = True
        # Validate type faultMsgType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 64:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on faultMsgType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.FaultCode is not None or
            self.FaultMsg is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='NotificationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NotificationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NotificationType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NotificationType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NotificationType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NotificationType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='NotificationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.FaultCode is not None:
            namespaceprefix_ = self.FaultCode_nsprefix_ + ':' if (UseCapturedNS_ and self.FaultCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sFaultCode>%s</%sFaultCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.FaultCode), input_name='FaultCode')), namespaceprefix_ , eol_))
        if self.FaultMsg is not None:
            namespaceprefix_ = self.FaultMsg_nsprefix_ + ':' if (UseCapturedNS_ and self.FaultMsg_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sFaultMsg>%s</%sFaultMsg>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.FaultMsg), input_name='FaultMsg')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'FaultCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'FaultCode')
            value_ = self.gds_validate_string(value_, node, 'FaultCode')
            self.FaultCode = value_
            self.FaultCode_nsprefix_ = child_.prefix
            # validate type faultCodeType
            self.validate_faultCodeType(self.FaultCode)
        elif nodeName_ == 'FaultMsg':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'FaultMsg')
            value_ = self.gds_validate_string(value_, node, 'FaultMsg')
            self.FaultMsg = value_
            self.FaultMsg_nsprefix_ = child_.prefix
            # validate type faultMsgType
            self.validate_faultMsgType(self.FaultMsg)
# end class NotificationType


class SASchedulesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SASchedulesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SASchedulesType.subclass:
            return SASchedulesType.subclass(*args_, **kwargs_)
        else:
            return SASchedulesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SASchedulesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SASchedulesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SASchedulesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SASchedulesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SASchedulesType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SASchedulesType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SASchedulesType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class SASchedulesType


class SAScheduleListType(SASchedulesType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = SASchedulesType
    def __init__(self, SAScheduleTuple=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("SAScheduleListType"), self).__init__( **kwargs_)
        if SAScheduleTuple is None:
            self.SAScheduleTuple = []
        else:
            self.SAScheduleTuple = SAScheduleTuple
        self.SAScheduleTuple_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SAScheduleListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SAScheduleListType.subclass:
            return SAScheduleListType.subclass(*args_, **kwargs_)
        else:
            return SAScheduleListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_SAScheduleTuple(self):
        return self.SAScheduleTuple
    def set_SAScheduleTuple(self, SAScheduleTuple):
        self.SAScheduleTuple = SAScheduleTuple
    def add_SAScheduleTuple(self, value):
        self.SAScheduleTuple.append(value)
    def insert_SAScheduleTuple_at(self, index, value):
        self.SAScheduleTuple.insert(index, value)
    def replace_SAScheduleTuple_at(self, index, value):
        self.SAScheduleTuple[index] = value
    def _hasContent(self):
        if (
            self.SAScheduleTuple or
            super(SAScheduleListType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='SAScheduleListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SAScheduleListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SAScheduleListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SAScheduleListType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SAScheduleListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SAScheduleListType'):
        super(SAScheduleListType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SAScheduleListType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='SAScheduleListType', fromsubclass_=False, pretty_print=True):
        super(SAScheduleListType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for SAScheduleTuple_ in self.SAScheduleTuple:
            namespaceprefix_ = self.SAScheduleTuple_nsprefix_ + ':' if (UseCapturedNS_ and self.SAScheduleTuple_nsprefix_) else ''
            SAScheduleTuple_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SAScheduleTuple', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(SAScheduleListType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'SAScheduleTuple':
            obj_ = SAScheduleTupleType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SAScheduleTuple.append(obj_)
            obj_.original_tagname_ = 'SAScheduleTuple'
        super(SAScheduleListType, self)._buildChildren(child_, node, nodeName_, True)
# end class SAScheduleListType


class SAScheduleTupleType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, SAScheduleTupleID=None, PMaxSchedule=None, SalesTariff=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.SAScheduleTupleID = SAScheduleTupleID
        self.validate_SAIDType(self.SAScheduleTupleID)
        self.SAScheduleTupleID_nsprefix_ = None
        self.PMaxSchedule = PMaxSchedule
        self.PMaxSchedule_nsprefix_ = None
        self.SalesTariff = SalesTariff
        self.SalesTariff_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SAScheduleTupleType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SAScheduleTupleType.subclass:
            return SAScheduleTupleType.subclass(*args_, **kwargs_)
        else:
            return SAScheduleTupleType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_SAScheduleTupleID(self):
        return self.SAScheduleTupleID
    def set_SAScheduleTupleID(self, SAScheduleTupleID):
        self.SAScheduleTupleID = SAScheduleTupleID
    def get_PMaxSchedule(self):
        return self.PMaxSchedule
    def set_PMaxSchedule(self, PMaxSchedule):
        self.PMaxSchedule = PMaxSchedule
    def get_SalesTariff(self):
        return self.SalesTariff
    def set_SalesTariff(self, SalesTariff):
        self.SalesTariff = SalesTariff
    def validate_SAIDType(self, value):
        result = True
        # Validate type SAIDType, a restriction on xs:unsignedByte.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on SAIDType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on SAIDType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.SAScheduleTupleID is not None or
            self.PMaxSchedule is not None or
            self.SalesTariff is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='SAScheduleTupleType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SAScheduleTupleType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SAScheduleTupleType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SAScheduleTupleType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SAScheduleTupleType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SAScheduleTupleType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='SAScheduleTupleType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.SAScheduleTupleID is not None:
            namespaceprefix_ = self.SAScheduleTupleID_nsprefix_ + ':' if (UseCapturedNS_ and self.SAScheduleTupleID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSAScheduleTupleID>%s</%sSAScheduleTupleID>%s' % (namespaceprefix_ , self.gds_format_integer(self.SAScheduleTupleID, input_name='SAScheduleTupleID'), namespaceprefix_ , eol_))
        if self.PMaxSchedule is not None:
            namespaceprefix_ = self.PMaxSchedule_nsprefix_ + ':' if (UseCapturedNS_ and self.PMaxSchedule_nsprefix_) else ''
            self.PMaxSchedule.export(outfile, level, namespaceprefix_, namespacedef_='', name_='PMaxSchedule', pretty_print=pretty_print)
        if self.SalesTariff is not None:
            namespaceprefix_ = self.SalesTariff_nsprefix_ + ':' if (UseCapturedNS_ and self.SalesTariff_nsprefix_) else ''
            self.SalesTariff.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SalesTariff', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'SAScheduleTupleID' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'SAScheduleTupleID')
            ival_ = self.gds_validate_integer(ival_, node, 'SAScheduleTupleID')
            self.SAScheduleTupleID = ival_
            self.SAScheduleTupleID_nsprefix_ = child_.prefix
            # validate type SAIDType
            self.validate_SAIDType(self.SAScheduleTupleID)
        elif nodeName_ == 'PMaxSchedule':
            obj_ = PMaxScheduleType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.PMaxSchedule = obj_
            obj_.original_tagname_ = 'PMaxSchedule'
        elif nodeName_ == 'SalesTariff':
            obj_ = SalesTariffType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SalesTariff = obj_
            obj_.original_tagname_ = 'SalesTariff'
# end class SAScheduleTupleType


class SalesTariffType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Id=None, SalesTariffID=None, SalesTariffDescription=None, NumEPriceLevels=None, SalesTariffEntry=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.SalesTariffID = SalesTariffID
        self.validate_SAIDType(self.SalesTariffID)
        self.SalesTariffID_nsprefix_ = None
        self.SalesTariffDescription = SalesTariffDescription
        self.validate_tariffDescriptionType(self.SalesTariffDescription)
        self.SalesTariffDescription_nsprefix_ = None
        self.NumEPriceLevels = NumEPriceLevels
        self.NumEPriceLevels_nsprefix_ = None
        if SalesTariffEntry is None:
            self.SalesTariffEntry = []
        else:
            self.SalesTariffEntry = SalesTariffEntry
        self.SalesTariffEntry_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SalesTariffType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SalesTariffType.subclass:
            return SalesTariffType.subclass(*args_, **kwargs_)
        else:
            return SalesTariffType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_SalesTariffID(self):
        return self.SalesTariffID
    def set_SalesTariffID(self, SalesTariffID):
        self.SalesTariffID = SalesTariffID
    def get_SalesTariffDescription(self):
        return self.SalesTariffDescription
    def set_SalesTariffDescription(self, SalesTariffDescription):
        self.SalesTariffDescription = SalesTariffDescription
    def get_NumEPriceLevels(self):
        return self.NumEPriceLevels
    def set_NumEPriceLevels(self, NumEPriceLevels):
        self.NumEPriceLevels = NumEPriceLevels
    def get_SalesTariffEntry(self):
        return self.SalesTariffEntry
    def set_SalesTariffEntry(self, SalesTariffEntry):
        self.SalesTariffEntry = SalesTariffEntry
    def add_SalesTariffEntry(self, value):
        self.SalesTariffEntry.append(value)
    def insert_SalesTariffEntry_at(self, index, value):
        self.SalesTariffEntry.insert(index, value)
    def replace_SalesTariffEntry_at(self, index, value):
        self.SalesTariffEntry[index] = value
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def validate_SAIDType(self, value):
        result = True
        # Validate type SAIDType, a restriction on xs:unsignedByte.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on SAIDType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on SAIDType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_tariffDescriptionType(self, value):
        result = True
        # Validate type tariffDescriptionType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tariffDescriptionType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.SalesTariffID is not None or
            self.SalesTariffDescription is not None or
            self.NumEPriceLevels is not None or
            self.SalesTariffEntry
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='SalesTariffType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SalesTariffType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SalesTariffType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SalesTariffType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SalesTariffType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SalesTariffType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='SalesTariffType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.SalesTariffID is not None:
            namespaceprefix_ = self.SalesTariffID_nsprefix_ + ':' if (UseCapturedNS_ and self.SalesTariffID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSalesTariffID>%s</%sSalesTariffID>%s' % (namespaceprefix_ , self.gds_format_integer(self.SalesTariffID, input_name='SalesTariffID'), namespaceprefix_ , eol_))
        if self.SalesTariffDescription is not None:
            namespaceprefix_ = self.SalesTariffDescription_nsprefix_ + ':' if (UseCapturedNS_ and self.SalesTariffDescription_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSalesTariffDescription>%s</%sSalesTariffDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SalesTariffDescription), input_name='SalesTariffDescription')), namespaceprefix_ , eol_))
        if self.NumEPriceLevels is not None:
            namespaceprefix_ = self.NumEPriceLevels_nsprefix_ + ':' if (UseCapturedNS_ and self.NumEPriceLevels_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumEPriceLevels>%s</%sNumEPriceLevels>%s' % (namespaceprefix_ , self.gds_format_integer(self.NumEPriceLevels, input_name='NumEPriceLevels'), namespaceprefix_ , eol_))
        for SalesTariffEntry_ in self.SalesTariffEntry:
            namespaceprefix_ = self.SalesTariffEntry_nsprefix_ + ':' if (UseCapturedNS_ and self.SalesTariffEntry_nsprefix_) else ''
            SalesTariffEntry_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SalesTariffEntry', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'SalesTariffID' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'SalesTariffID')
            ival_ = self.gds_validate_integer(ival_, node, 'SalesTariffID')
            self.SalesTariffID = ival_
            self.SalesTariffID_nsprefix_ = child_.prefix
            # validate type SAIDType
            self.validate_SAIDType(self.SalesTariffID)
        elif nodeName_ == 'SalesTariffDescription':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SalesTariffDescription')
            value_ = self.gds_validate_string(value_, node, 'SalesTariffDescription')
            self.SalesTariffDescription = value_
            self.SalesTariffDescription_nsprefix_ = child_.prefix
            # validate type tariffDescriptionType
            self.validate_tariffDescriptionType(self.SalesTariffDescription)
        elif nodeName_ == 'NumEPriceLevels' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NumEPriceLevels')
            ival_ = self.gds_validate_integer(ival_, node, 'NumEPriceLevels')
            self.NumEPriceLevels = ival_
            self.NumEPriceLevels_nsprefix_ = child_.prefix
        elif nodeName_ == 'SalesTariffEntry':
            obj_ = SalesTariffEntryType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SalesTariffEntry.append(obj_)
            obj_.original_tagname_ = 'SalesTariffEntry'
# end class SalesTariffType


class PMaxScheduleType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, PMaxScheduleEntry=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if PMaxScheduleEntry is None:
            self.PMaxScheduleEntry = []
        else:
            self.PMaxScheduleEntry = PMaxScheduleEntry
        self.PMaxScheduleEntry_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PMaxScheduleType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PMaxScheduleType.subclass:
            return PMaxScheduleType.subclass(*args_, **kwargs_)
        else:
            return PMaxScheduleType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_PMaxScheduleEntry(self):
        return self.PMaxScheduleEntry
    def set_PMaxScheduleEntry(self, PMaxScheduleEntry):
        self.PMaxScheduleEntry = PMaxScheduleEntry
    def add_PMaxScheduleEntry(self, value):
        self.PMaxScheduleEntry.append(value)
    def insert_PMaxScheduleEntry_at(self, index, value):
        self.PMaxScheduleEntry.insert(index, value)
    def replace_PMaxScheduleEntry_at(self, index, value):
        self.PMaxScheduleEntry[index] = value
    def _hasContent(self):
        if (
            self.PMaxScheduleEntry
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='PMaxScheduleType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PMaxScheduleType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PMaxScheduleType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PMaxScheduleType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PMaxScheduleType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PMaxScheduleType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='PMaxScheduleType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for PMaxScheduleEntry_ in self.PMaxScheduleEntry:
            namespaceprefix_ = self.PMaxScheduleEntry_nsprefix_ + ':' if (UseCapturedNS_ and self.PMaxScheduleEntry_nsprefix_) else ''
            PMaxScheduleEntry_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='PMaxScheduleEntry', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'PMaxScheduleEntry':
            obj_ = PMaxScheduleEntryType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.PMaxScheduleEntry.append(obj_)
            obj_.original_tagname_ = 'PMaxScheduleEntry'
# end class PMaxScheduleType


class EntryType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, TimeInterval=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.TimeInterval = TimeInterval
        self.TimeInterval_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, EntryType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if EntryType.subclass:
            return EntryType.subclass(*args_, **kwargs_)
        else:
            return EntryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_TimeInterval(self):
        return self.TimeInterval
    def set_TimeInterval(self, TimeInterval):
        self.TimeInterval = TimeInterval
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def _hasContent(self):
        if (
            self.TimeInterval is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='EntryType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('EntryType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'EntryType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='EntryType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='EntryType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='EntryType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='EntryType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.TimeInterval is not None:
            self.TimeInterval.export(outfile, level, namespaceprefix_, namespacedef_='', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'TimeInterval':
            type_name_ = child_.attrib.get(
                '{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()["" + type_name_]
                obj_ = class_.factory()
                obj_.build(child_, gds_collector_=gds_collector_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <TimeInterval> element')
            self.TimeInterval = obj_
            obj_.original_tagname_ = 'TimeInterval'
        elif nodeName_ == 'RelativeTimeInterval':
            obj_ = RelativeTimeIntervalType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TimeInterval = obj_
            obj_.original_tagname_ = 'RelativeTimeInterval'
# end class EntryType


class SalesTariffEntryType(EntryType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = EntryType
    def __init__(self, TimeInterval=None, EPriceLevel=None, ConsumptionCost=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("SalesTariffEntryType"), self).__init__(TimeInterval,  **kwargs_)
        self.EPriceLevel = EPriceLevel
        self.EPriceLevel_nsprefix_ = None
        if ConsumptionCost is None:
            self.ConsumptionCost = []
        else:
            self.ConsumptionCost = ConsumptionCost
        self.ConsumptionCost_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SalesTariffEntryType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SalesTariffEntryType.subclass:
            return SalesTariffEntryType.subclass(*args_, **kwargs_)
        else:
            return SalesTariffEntryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_EPriceLevel(self):
        return self.EPriceLevel
    def set_EPriceLevel(self, EPriceLevel):
        self.EPriceLevel = EPriceLevel
    def get_ConsumptionCost(self):
        return self.ConsumptionCost
    def set_ConsumptionCost(self, ConsumptionCost):
        self.ConsumptionCost = ConsumptionCost
    def add_ConsumptionCost(self, value):
        self.ConsumptionCost.append(value)
    def insert_ConsumptionCost_at(self, index, value):
        self.ConsumptionCost.insert(index, value)
    def replace_ConsumptionCost_at(self, index, value):
        self.ConsumptionCost[index] = value
    def _hasContent(self):
        if (
            self.EPriceLevel is not None or
            self.ConsumptionCost or
            super(SalesTariffEntryType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='SalesTariffEntryType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SalesTariffEntryType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SalesTariffEntryType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SalesTariffEntryType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SalesTariffEntryType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SalesTariffEntryType'):
        super(SalesTariffEntryType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SalesTariffEntryType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='SalesTariffEntryType', fromsubclass_=False, pretty_print=True):
        super(SalesTariffEntryType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.EPriceLevel is not None:
            namespaceprefix_ = self.EPriceLevel_nsprefix_ + ':' if (UseCapturedNS_ and self.EPriceLevel_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEPriceLevel>%s</%sEPriceLevel>%s' % (namespaceprefix_ , self.gds_format_integer(self.EPriceLevel, input_name='EPriceLevel'), namespaceprefix_ , eol_))
        for ConsumptionCost_ in self.ConsumptionCost:
            namespaceprefix_ = self.ConsumptionCost_nsprefix_ + ':' if (UseCapturedNS_ and self.ConsumptionCost_nsprefix_) else ''
            ConsumptionCost_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ConsumptionCost', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(SalesTariffEntryType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'EPriceLevel' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'EPriceLevel')
            ival_ = self.gds_validate_integer(ival_, node, 'EPriceLevel')
            self.EPriceLevel = ival_
            self.EPriceLevel_nsprefix_ = child_.prefix
        elif nodeName_ == 'ConsumptionCost':
            obj_ = ConsumptionCostType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ConsumptionCost.append(obj_)
            obj_.original_tagname_ = 'ConsumptionCost'
        super(SalesTariffEntryType, self)._buildChildren(child_, node, nodeName_, True)
# end class SalesTariffEntryType


class PMaxScheduleEntryType(EntryType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = EntryType
    def __init__(self, TimeInterval=None, PMax=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("PMaxScheduleEntryType"), self).__init__(TimeInterval,  **kwargs_)
        self.PMax = PMax
        self.PMax_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PMaxScheduleEntryType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PMaxScheduleEntryType.subclass:
            return PMaxScheduleEntryType.subclass(*args_, **kwargs_)
        else:
            return PMaxScheduleEntryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_PMax(self):
        return self.PMax
    def set_PMax(self, PMax):
        self.PMax = PMax
    def _hasContent(self):
        if (
            self.PMax is not None or
            super(PMaxScheduleEntryType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='PMaxScheduleEntryType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PMaxScheduleEntryType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PMaxScheduleEntryType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PMaxScheduleEntryType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PMaxScheduleEntryType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PMaxScheduleEntryType'):
        super(PMaxScheduleEntryType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PMaxScheduleEntryType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='PMaxScheduleEntryType', fromsubclass_=False, pretty_print=True):
        super(PMaxScheduleEntryType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.PMax is not None:
            namespaceprefix_ = self.PMax_nsprefix_ + ':' if (UseCapturedNS_ and self.PMax_nsprefix_) else ''
            self.PMax.export(outfile, level, namespaceprefix_, namespacedef_='', name_='PMax', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(PMaxScheduleEntryType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'PMax':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.PMax = obj_
            obj_.original_tagname_ = 'PMax'
        super(PMaxScheduleEntryType, self)._buildChildren(child_, node, nodeName_, True)
# end class PMaxScheduleEntryType


class IntervalType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, IntervalType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if IntervalType.subclass:
            return IntervalType.subclass(*args_, **kwargs_)
        else:
            return IntervalType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='IntervalType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('IntervalType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'IntervalType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='IntervalType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='IntervalType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='IntervalType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='IntervalType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class IntervalType


class RelativeTimeIntervalType(IntervalType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = IntervalType
    def __init__(self, start=None, duration=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("RelativeTimeIntervalType"), self).__init__( **kwargs_)
        self.start = start
        self.validate_startType(self.start)
        self.start_nsprefix_ = None
        self.duration = duration
        self.validate_durationType(self.duration)
        self.duration_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RelativeTimeIntervalType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RelativeTimeIntervalType.subclass:
            return RelativeTimeIntervalType.subclass(*args_, **kwargs_)
        else:
            return RelativeTimeIntervalType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_start(self):
        return self.start
    def set_start(self, start):
        self.start = start
    def get_duration(self):
        return self.duration
    def set_duration(self, duration):
        self.duration = duration
    def validate_startType(self, value):
        result = True
        # Validate type startType, a restriction on xs:unsignedInt.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on startType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 16777214:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on startType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_durationType(self, value):
        result = True
        # Validate type durationType, a restriction on xs:unsignedInt.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on durationType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 86400:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on durationType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.start is not None or
            self.duration is not None or
            super(RelativeTimeIntervalType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='RelativeTimeIntervalType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RelativeTimeIntervalType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RelativeTimeIntervalType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RelativeTimeIntervalType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RelativeTimeIntervalType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RelativeTimeIntervalType'):
        super(RelativeTimeIntervalType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RelativeTimeIntervalType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='RelativeTimeIntervalType', fromsubclass_=False, pretty_print=True):
        super(RelativeTimeIntervalType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.start is not None:
            namespaceprefix_ = self.start_nsprefix_ + ':' if (UseCapturedNS_ and self.start_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstart>%s</%sstart>%s' % (namespaceprefix_ , self.gds_format_integer(self.start, input_name='start'), namespaceprefix_ , eol_))
        if self.duration is not None:
            namespaceprefix_ = self.duration_nsprefix_ + ':' if (UseCapturedNS_ and self.duration_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sduration>%s</%sduration>%s' % (namespaceprefix_ , self.gds_format_integer(self.duration, input_name='duration'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(RelativeTimeIntervalType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'start' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'start')
            ival_ = self.gds_validate_integer(ival_, node, 'start')
            self.start = ival_
            self.start_nsprefix_ = child_.prefix
            # validate type startType
            self.validate_startType(self.start)
        elif nodeName_ == 'duration' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'duration')
            ival_ = self.gds_validate_integer(ival_, node, 'duration')
            self.duration = ival_
            self.duration_nsprefix_ = child_.prefix
            # validate type durationType
            self.validate_durationType(self.duration)
        super(RelativeTimeIntervalType, self)._buildChildren(child_, node, nodeName_, True)
# end class RelativeTimeIntervalType


class ConsumptionCostType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, startValue=None, Cost=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.startValue = startValue
        self.startValue_nsprefix_ = None
        if Cost is None:
            self.Cost = []
        else:
            self.Cost = Cost
        self.Cost_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ConsumptionCostType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ConsumptionCostType.subclass:
            return ConsumptionCostType.subclass(*args_, **kwargs_)
        else:
            return ConsumptionCostType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_startValue(self):
        return self.startValue
    def set_startValue(self, startValue):
        self.startValue = startValue
    def get_Cost(self):
        return self.Cost
    def set_Cost(self, Cost):
        self.Cost = Cost
    def add_Cost(self, value):
        self.Cost.append(value)
    def insert_Cost_at(self, index, value):
        self.Cost.insert(index, value)
    def replace_Cost_at(self, index, value):
        self.Cost[index] = value
    def _hasContent(self):
        if (
            self.startValue is not None or
            self.Cost
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='ConsumptionCostType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ConsumptionCostType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ConsumptionCostType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ConsumptionCostType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ConsumptionCostType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ConsumptionCostType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='ConsumptionCostType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.startValue is not None:
            namespaceprefix_ = self.startValue_nsprefix_ + ':' if (UseCapturedNS_ and self.startValue_nsprefix_) else ''
            self.startValue.export(outfile, level, namespaceprefix_, namespacedef_='', name_='startValue', pretty_print=pretty_print)
        for Cost_ in self.Cost:
            namespaceprefix_ = self.Cost_nsprefix_ + ':' if (UseCapturedNS_ and self.Cost_nsprefix_) else ''
            Cost_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Cost', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'startValue':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.startValue = obj_
            obj_.original_tagname_ = 'startValue'
        elif nodeName_ == 'Cost':
            obj_ = CostType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Cost.append(obj_)
            obj_.original_tagname_ = 'Cost'
# end class ConsumptionCostType


class CostType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, costKind=None, amount=None, amountMultiplier=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.costKind = costKind
        self.validate_costKindType(self.costKind)
        self.costKind_nsprefix_ = None
        self.amount = amount
        self.amount_nsprefix_ = None
        self.amountMultiplier = amountMultiplier
        self.validate_unitMultiplierType(self.amountMultiplier)
        self.amountMultiplier_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CostType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CostType.subclass:
            return CostType.subclass(*args_, **kwargs_)
        else:
            return CostType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_costKind(self):
        return self.costKind
    def set_costKind(self, costKind):
        self.costKind = costKind
    def get_amount(self):
        return self.amount
    def set_amount(self, amount):
        self.amount = amount
    def get_amountMultiplier(self):
        return self.amountMultiplier
    def set_amountMultiplier(self, amountMultiplier):
        self.amountMultiplier = amountMultiplier
    def validate_costKindType(self, value):
        result = True
        # Validate type costKindType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['relativePricePercentage', 'RenewableGenerationPercentage', 'CarbonDioxideEmission']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on costKindType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_unitMultiplierType(self, value):
        result = True
        # Validate type unitMultiplierType, a restriction on xs:byte.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < -3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on unitMultiplierType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on unitMultiplierType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.costKind is not None or
            self.amount is not None or
            self.amountMultiplier is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='CostType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CostType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CostType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CostType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CostType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CostType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='CostType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.costKind is not None:
            namespaceprefix_ = self.costKind_nsprefix_ + ':' if (UseCapturedNS_ and self.costKind_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scostKind>%s</%scostKind>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.costKind), input_name='costKind')), namespaceprefix_ , eol_))
        if self.amount is not None:
            namespaceprefix_ = self.amount_nsprefix_ + ':' if (UseCapturedNS_ and self.amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%samount>%s</%samount>%s' % (namespaceprefix_ , self.gds_format_integer(self.amount, input_name='amount'), namespaceprefix_ , eol_))
        if self.amountMultiplier is not None:
            namespaceprefix_ = self.amountMultiplier_nsprefix_ + ':' if (UseCapturedNS_ and self.amountMultiplier_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%samountMultiplier>%s</%samountMultiplier>%s' % (namespaceprefix_ , self.gds_format_integer(self.amountMultiplier, input_name='amountMultiplier'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'costKind':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'costKind')
            value_ = self.gds_validate_string(value_, node, 'costKind')
            self.costKind = value_
            self.costKind_nsprefix_ = child_.prefix
            # validate type costKindType
            self.validate_costKindType(self.costKind)
        elif nodeName_ == 'amount' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'amount')
            ival_ = self.gds_validate_integer(ival_, node, 'amount')
            self.amount = ival_
            self.amount_nsprefix_ = child_.prefix
        elif nodeName_ == 'amountMultiplier' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'amountMultiplier')
            ival_ = self.gds_validate_integer(ival_, node, 'amountMultiplier')
            self.amountMultiplier = ival_
            self.amountMultiplier_nsprefix_ = child_.prefix
            # validate type unitMultiplierType
            self.validate_unitMultiplierType(self.amountMultiplier)
# end class CostType


class EVSEStatusType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, NotificationMaxDelay=None, EVSENotification=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.NotificationMaxDelay = NotificationMaxDelay
        self.NotificationMaxDelay_nsprefix_ = None
        self.EVSENotification = EVSENotification
        self.validate_EVSENotificationType(self.EVSENotification)
        self.EVSENotification_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, EVSEStatusType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if EVSEStatusType.subclass:
            return EVSEStatusType.subclass(*args_, **kwargs_)
        else:
            return EVSEStatusType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_NotificationMaxDelay(self):
        return self.NotificationMaxDelay
    def set_NotificationMaxDelay(self, NotificationMaxDelay):
        self.NotificationMaxDelay = NotificationMaxDelay
    def get_EVSENotification(self):
        return self.EVSENotification
    def set_EVSENotification(self, EVSENotification):
        self.EVSENotification = EVSENotification
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def validate_EVSENotificationType(self, value):
        result = True
        # Validate type EVSENotificationType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['None', 'StopCharging', 'ReNegotiation']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on EVSENotificationType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.NotificationMaxDelay is not None or
            self.EVSENotification is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='EVSEStatusType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('EVSEStatusType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'EVSEStatusType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='EVSEStatusType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='EVSEStatusType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='EVSEStatusType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='EVSEStatusType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.NotificationMaxDelay is not None:
            namespaceprefix_ = self.NotificationMaxDelay_nsprefix_ + ':' if (UseCapturedNS_ and self.NotificationMaxDelay_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNotificationMaxDelay>%s</%sNotificationMaxDelay>%s' % (namespaceprefix_ , self.gds_format_integer(self.NotificationMaxDelay, input_name='NotificationMaxDelay'), namespaceprefix_ , eol_))
        if self.EVSENotification is not None:
            namespaceprefix_ = self.EVSENotification_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSENotification_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEVSENotification>%s</%sEVSENotification>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.EVSENotification), input_name='EVSENotification')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'NotificationMaxDelay' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NotificationMaxDelay')
            ival_ = self.gds_validate_integer(ival_, node, 'NotificationMaxDelay')
            self.NotificationMaxDelay = ival_
            self.NotificationMaxDelay_nsprefix_ = child_.prefix
        elif nodeName_ == 'EVSENotification':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'EVSENotification')
            value_ = self.gds_validate_string(value_, node, 'EVSENotification')
            self.EVSENotification = value_
            self.EVSENotification_nsprefix_ = child_.prefix
            # validate type EVSENotificationType
            self.validate_EVSENotificationType(self.EVSENotification)
# end class EVSEStatusType


class AC_EVSEStatusType(EVSEStatusType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = EVSEStatusType
    def __init__(self, NotificationMaxDelay=None, EVSENotification=None, RCD=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("AC_EVSEStatusType"), self).__init__(NotificationMaxDelay, EVSENotification,  **kwargs_)
        self.RCD = RCD
        self.RCD_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AC_EVSEStatusType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AC_EVSEStatusType.subclass:
            return AC_EVSEStatusType.subclass(*args_, **kwargs_)
        else:
            return AC_EVSEStatusType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_RCD(self):
        return self.RCD
    def set_RCD(self, RCD):
        self.RCD = RCD
    def _hasContent(self):
        if (
            self.RCD is not None or
            super(AC_EVSEStatusType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='AC_EVSEStatusType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AC_EVSEStatusType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AC_EVSEStatusType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AC_EVSEStatusType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AC_EVSEStatusType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AC_EVSEStatusType'):
        super(AC_EVSEStatusType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AC_EVSEStatusType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='AC_EVSEStatusType', fromsubclass_=False, pretty_print=True):
        super(AC_EVSEStatusType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.RCD is not None:
            namespaceprefix_ = self.RCD_nsprefix_ + ':' if (UseCapturedNS_ and self.RCD_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRCD>%s</%sRCD>%s' % (namespaceprefix_ , self.gds_format_boolean(self.RCD, input_name='RCD'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(AC_EVSEStatusType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'RCD':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'RCD')
            ival_ = self.gds_validate_boolean(ival_, node, 'RCD')
            self.RCD = ival_
            self.RCD_nsprefix_ = child_.prefix
        super(AC_EVSEStatusType, self)._buildChildren(child_, node, nodeName_, True)
# end class AC_EVSEStatusType


class EVStatusType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, EVStatusType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if EVStatusType.subclass:
            return EVStatusType.subclass(*args_, **kwargs_)
        else:
            return EVStatusType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='EVStatusType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('EVStatusType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'EVStatusType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='EVStatusType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='EVStatusType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='EVStatusType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='EVStatusType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class EVStatusType


class DC_EVSEStatusType(EVSEStatusType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = EVSEStatusType
    def __init__(self, NotificationMaxDelay=None, EVSENotification=None, EVSEIsolationStatus=None, EVSEStatusCode=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("DC_EVSEStatusType"), self).__init__(NotificationMaxDelay, EVSENotification,  **kwargs_)
        self.EVSEIsolationStatus = EVSEIsolationStatus
        self.validate_isolationLevelType(self.EVSEIsolationStatus)
        self.EVSEIsolationStatus_nsprefix_ = None
        self.EVSEStatusCode = EVSEStatusCode
        self.validate_DC_EVSEStatusCodeType(self.EVSEStatusCode)
        self.EVSEStatusCode_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DC_EVSEStatusType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DC_EVSEStatusType.subclass:
            return DC_EVSEStatusType.subclass(*args_, **kwargs_)
        else:
            return DC_EVSEStatusType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_EVSEIsolationStatus(self):
        return self.EVSEIsolationStatus
    def set_EVSEIsolationStatus(self, EVSEIsolationStatus):
        self.EVSEIsolationStatus = EVSEIsolationStatus
    def get_EVSEStatusCode(self):
        return self.EVSEStatusCode
    def set_EVSEStatusCode(self, EVSEStatusCode):
        self.EVSEStatusCode = EVSEStatusCode
    def validate_isolationLevelType(self, value):
        result = True
        # Validate type isolationLevelType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Invalid', 'Valid', 'Warning', 'Fault', 'No_IMD']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on isolationLevelType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_DC_EVSEStatusCodeType(self, value):
        result = True
        # Validate type DC_EVSEStatusCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['EVSE_NotReady', 'EVSE_Ready', 'EVSE_Shutdown', 'EVSE_UtilityInterruptEvent', 'EVSE_IsolationMonitoringActive', 'EVSE_EmergencyShutdown', 'EVSE_Malfunction', 'Reserved_8', 'Reserved_9', 'Reserved_A', 'Reserved_B', 'Reserved_C']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on DC_EVSEStatusCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.EVSEIsolationStatus is not None or
            self.EVSEStatusCode is not None or
            super(DC_EVSEStatusType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='DC_EVSEStatusType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DC_EVSEStatusType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DC_EVSEStatusType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DC_EVSEStatusType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DC_EVSEStatusType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DC_EVSEStatusType'):
        super(DC_EVSEStatusType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DC_EVSEStatusType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='DC_EVSEStatusType', fromsubclass_=False, pretty_print=True):
        super(DC_EVSEStatusType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.EVSEIsolationStatus is not None:
            namespaceprefix_ = self.EVSEIsolationStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEIsolationStatus_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEVSEIsolationStatus>%s</%sEVSEIsolationStatus>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.EVSEIsolationStatus), input_name='EVSEIsolationStatus')), namespaceprefix_ , eol_))
        if self.EVSEStatusCode is not None:
            namespaceprefix_ = self.EVSEStatusCode_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEStatusCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEVSEStatusCode>%s</%sEVSEStatusCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.EVSEStatusCode), input_name='EVSEStatusCode')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(DC_EVSEStatusType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'EVSEIsolationStatus':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'EVSEIsolationStatus')
            value_ = self.gds_validate_string(value_, node, 'EVSEIsolationStatus')
            self.EVSEIsolationStatus = value_
            self.EVSEIsolationStatus_nsprefix_ = child_.prefix
            # validate type isolationLevelType
            self.validate_isolationLevelType(self.EVSEIsolationStatus)
        elif nodeName_ == 'EVSEStatusCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'EVSEStatusCode')
            value_ = self.gds_validate_string(value_, node, 'EVSEStatusCode')
            self.EVSEStatusCode = value_
            self.EVSEStatusCode_nsprefix_ = child_.prefix
            # validate type DC_EVSEStatusCodeType
            self.validate_DC_EVSEStatusCodeType(self.EVSEStatusCode)
        super(DC_EVSEStatusType, self)._buildChildren(child_, node, nodeName_, True)
# end class DC_EVSEStatusType


class DC_EVStatusType(EVStatusType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = EVStatusType
    def __init__(self, EVReady=None, EVErrorCode=None, EVRESSSOC=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("DC_EVStatusType"), self).__init__( **kwargs_)
        self.EVReady = EVReady
        self.EVReady_nsprefix_ = None
        self.EVErrorCode = EVErrorCode
        self.validate_DC_EVErrorCodeType(self.EVErrorCode)
        self.EVErrorCode_nsprefix_ = None
        self.EVRESSSOC = EVRESSSOC
        self.validate_percentValueType(self.EVRESSSOC)
        self.EVRESSSOC_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DC_EVStatusType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DC_EVStatusType.subclass:
            return DC_EVStatusType.subclass(*args_, **kwargs_)
        else:
            return DC_EVStatusType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_EVReady(self):
        return self.EVReady
    def set_EVReady(self, EVReady):
        self.EVReady = EVReady
    def get_EVErrorCode(self):
        return self.EVErrorCode
    def set_EVErrorCode(self, EVErrorCode):
        self.EVErrorCode = EVErrorCode
    def get_EVRESSSOC(self):
        return self.EVRESSSOC
    def set_EVRESSSOC(self, EVRESSSOC):
        self.EVRESSSOC = EVRESSSOC
    def validate_DC_EVErrorCodeType(self, value):
        result = True
        # Validate type DC_EVErrorCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['NO_ERROR', 'FAILED_RESSTemperatureInhibit', 'FAILED_EVShiftPosition', 'FAILED_ChargerConnectorLockFault', 'FAILED_EVRESSMalfunction', 'FAILED_ChargingCurrentdifferential', 'FAILED_ChargingVoltageOutOfRange', 'Reserved_A', 'Reserved_B', 'Reserved_C', 'FAILED_ChargingSystemIncompatibility', 'NoData']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on DC_EVErrorCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_percentValueType(self, value):
        result = True
        # Validate type percentValueType, a restriction on xs:byte.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on percentValueType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on percentValueType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.EVReady is not None or
            self.EVErrorCode is not None or
            self.EVRESSSOC is not None or
            super(DC_EVStatusType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='DC_EVStatusType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DC_EVStatusType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DC_EVStatusType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DC_EVStatusType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DC_EVStatusType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DC_EVStatusType'):
        super(DC_EVStatusType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DC_EVStatusType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='DC_EVStatusType', fromsubclass_=False, pretty_print=True):
        super(DC_EVStatusType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.EVReady is not None:
            namespaceprefix_ = self.EVReady_nsprefix_ + ':' if (UseCapturedNS_ and self.EVReady_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEVReady>%s</%sEVReady>%s' % (namespaceprefix_ , self.gds_format_boolean(self.EVReady, input_name='EVReady'), namespaceprefix_ , eol_))
        if self.EVErrorCode is not None:
            namespaceprefix_ = self.EVErrorCode_nsprefix_ + ':' if (UseCapturedNS_ and self.EVErrorCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEVErrorCode>%s</%sEVErrorCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.EVErrorCode), input_name='EVErrorCode')), namespaceprefix_ , eol_))
        if self.EVRESSSOC is not None:
            namespaceprefix_ = self.EVRESSSOC_nsprefix_ + ':' if (UseCapturedNS_ and self.EVRESSSOC_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEVRESSSOC>%s</%sEVRESSSOC>%s' % (namespaceprefix_ , self.gds_format_integer(self.EVRESSSOC, input_name='EVRESSSOC'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(DC_EVStatusType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'EVReady':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'EVReady')
            ival_ = self.gds_validate_boolean(ival_, node, 'EVReady')
            self.EVReady = ival_
            self.EVReady_nsprefix_ = child_.prefix
        elif nodeName_ == 'EVErrorCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'EVErrorCode')
            value_ = self.gds_validate_string(value_, node, 'EVErrorCode')
            self.EVErrorCode = value_
            self.EVErrorCode_nsprefix_ = child_.prefix
            # validate type DC_EVErrorCodeType
            self.validate_DC_EVErrorCodeType(self.EVErrorCode)
        elif nodeName_ == 'EVRESSSOC' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'EVRESSSOC')
            ival_ = self.gds_validate_integer(ival_, node, 'EVRESSSOC')
            self.EVRESSSOC = ival_
            self.EVRESSSOC_nsprefix_ = child_.prefix
            # validate type percentValueType
            self.validate_percentValueType(self.EVRESSSOC)
        super(DC_EVStatusType, self)._buildChildren(child_, node, nodeName_, True)
# end class DC_EVStatusType


class EVChargeParameterType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, DepartureTime=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.DepartureTime = DepartureTime
        self.DepartureTime_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, EVChargeParameterType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if EVChargeParameterType.subclass:
            return EVChargeParameterType.subclass(*args_, **kwargs_)
        else:
            return EVChargeParameterType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_DepartureTime(self):
        return self.DepartureTime
    def set_DepartureTime(self, DepartureTime):
        self.DepartureTime = DepartureTime
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def _hasContent(self):
        if (
            self.DepartureTime is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='EVChargeParameterType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('EVChargeParameterType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'EVChargeParameterType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='EVChargeParameterType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='EVChargeParameterType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='EVChargeParameterType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='EVChargeParameterType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.DepartureTime is not None:
            namespaceprefix_ = self.DepartureTime_nsprefix_ + ':' if (UseCapturedNS_ and self.DepartureTime_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDepartureTime>%s</%sDepartureTime>%s' % (namespaceprefix_ , self.gds_format_integer(self.DepartureTime, input_name='DepartureTime'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'DepartureTime' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'DepartureTime')
            ival_ = self.gds_validate_integer(ival_, node, 'DepartureTime')
            self.DepartureTime = ival_
            self.DepartureTime_nsprefix_ = child_.prefix
# end class EVChargeParameterType


class AC_EVChargeParameterType(EVChargeParameterType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = EVChargeParameterType
    def __init__(self, DepartureTime=None, EAmount=None, EVMaxVoltage=None, EVMaxCurrent=None, EVMinCurrent=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("AC_EVChargeParameterType"), self).__init__(DepartureTime,  **kwargs_)
        self.EAmount = EAmount
        self.EAmount_nsprefix_ = None
        self.EVMaxVoltage = EVMaxVoltage
        self.EVMaxVoltage_nsprefix_ = None
        self.EVMaxCurrent = EVMaxCurrent
        self.EVMaxCurrent_nsprefix_ = None
        self.EVMinCurrent = EVMinCurrent
        self.EVMinCurrent_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AC_EVChargeParameterType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AC_EVChargeParameterType.subclass:
            return AC_EVChargeParameterType.subclass(*args_, **kwargs_)
        else:
            return AC_EVChargeParameterType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_EAmount(self):
        return self.EAmount
    def set_EAmount(self, EAmount):
        self.EAmount = EAmount
    def get_EVMaxVoltage(self):
        return self.EVMaxVoltage
    def set_EVMaxVoltage(self, EVMaxVoltage):
        self.EVMaxVoltage = EVMaxVoltage
    def get_EVMaxCurrent(self):
        return self.EVMaxCurrent
    def set_EVMaxCurrent(self, EVMaxCurrent):
        self.EVMaxCurrent = EVMaxCurrent
    def get_EVMinCurrent(self):
        return self.EVMinCurrent
    def set_EVMinCurrent(self, EVMinCurrent):
        self.EVMinCurrent = EVMinCurrent
    def _hasContent(self):
        if (
            self.EAmount is not None or
            self.EVMaxVoltage is not None or
            self.EVMaxCurrent is not None or
            self.EVMinCurrent is not None or
            super(AC_EVChargeParameterType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='AC_EVChargeParameterType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AC_EVChargeParameterType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AC_EVChargeParameterType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AC_EVChargeParameterType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AC_EVChargeParameterType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AC_EVChargeParameterType'):
        super(AC_EVChargeParameterType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AC_EVChargeParameterType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='AC_EVChargeParameterType', fromsubclass_=False, pretty_print=True):
        super(AC_EVChargeParameterType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.EAmount is not None:
            namespaceprefix_ = self.EAmount_nsprefix_ + ':' if (UseCapturedNS_ and self.EAmount_nsprefix_) else ''
            self.EAmount.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EAmount', pretty_print=pretty_print)
        if self.EVMaxVoltage is not None:
            namespaceprefix_ = self.EVMaxVoltage_nsprefix_ + ':' if (UseCapturedNS_ and self.EVMaxVoltage_nsprefix_) else ''
            self.EVMaxVoltage.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVMaxVoltage', pretty_print=pretty_print)
        if self.EVMaxCurrent is not None:
            namespaceprefix_ = self.EVMaxCurrent_nsprefix_ + ':' if (UseCapturedNS_ and self.EVMaxCurrent_nsprefix_) else ''
            self.EVMaxCurrent.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVMaxCurrent', pretty_print=pretty_print)
        if self.EVMinCurrent is not None:
            namespaceprefix_ = self.EVMinCurrent_nsprefix_ + ':' if (UseCapturedNS_ and self.EVMinCurrent_nsprefix_) else ''
            self.EVMinCurrent.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVMinCurrent', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(AC_EVChargeParameterType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'EAmount':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EAmount = obj_
            obj_.original_tagname_ = 'EAmount'
        elif nodeName_ == 'EVMaxVoltage':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVMaxVoltage = obj_
            obj_.original_tagname_ = 'EVMaxVoltage'
        elif nodeName_ == 'EVMaxCurrent':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVMaxCurrent = obj_
            obj_.original_tagname_ = 'EVMaxCurrent'
        elif nodeName_ == 'EVMinCurrent':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVMinCurrent = obj_
            obj_.original_tagname_ = 'EVMinCurrent'
        super(AC_EVChargeParameterType, self)._buildChildren(child_, node, nodeName_, True)
# end class AC_EVChargeParameterType


class DC_EVChargeParameterType(EVChargeParameterType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = EVChargeParameterType
    def __init__(self, DepartureTime=None, DC_EVStatus=None, EVMaximumCurrentLimit=None, EVMaximumPowerLimit=None, EVMaximumVoltageLimit=None, EVEnergyCapacity=None, EVEnergyRequest=None, FullSOC=None, BulkSOC=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("DC_EVChargeParameterType"), self).__init__(DepartureTime,  **kwargs_)
        self.DC_EVStatus = DC_EVStatus
        self.DC_EVStatus_nsprefix_ = None
        self.EVMaximumCurrentLimit = EVMaximumCurrentLimit
        self.EVMaximumCurrentLimit_nsprefix_ = None
        self.EVMaximumPowerLimit = EVMaximumPowerLimit
        self.EVMaximumPowerLimit_nsprefix_ = None
        self.EVMaximumVoltageLimit = EVMaximumVoltageLimit
        self.EVMaximumVoltageLimit_nsprefix_ = None
        self.EVEnergyCapacity = EVEnergyCapacity
        self.EVEnergyCapacity_nsprefix_ = None
        self.EVEnergyRequest = EVEnergyRequest
        self.EVEnergyRequest_nsprefix_ = None
        self.FullSOC = FullSOC
        self.validate_percentValueType(self.FullSOC)
        self.FullSOC_nsprefix_ = None
        self.BulkSOC = BulkSOC
        self.validate_percentValueType(self.BulkSOC)
        self.BulkSOC_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DC_EVChargeParameterType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DC_EVChargeParameterType.subclass:
            return DC_EVChargeParameterType.subclass(*args_, **kwargs_)
        else:
            return DC_EVChargeParameterType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_DC_EVStatus(self):
        return self.DC_EVStatus
    def set_DC_EVStatus(self, DC_EVStatus):
        self.DC_EVStatus = DC_EVStatus
    def get_EVMaximumCurrentLimit(self):
        return self.EVMaximumCurrentLimit
    def set_EVMaximumCurrentLimit(self, EVMaximumCurrentLimit):
        self.EVMaximumCurrentLimit = EVMaximumCurrentLimit
    def get_EVMaximumPowerLimit(self):
        return self.EVMaximumPowerLimit
    def set_EVMaximumPowerLimit(self, EVMaximumPowerLimit):
        self.EVMaximumPowerLimit = EVMaximumPowerLimit
    def get_EVMaximumVoltageLimit(self):
        return self.EVMaximumVoltageLimit
    def set_EVMaximumVoltageLimit(self, EVMaximumVoltageLimit):
        self.EVMaximumVoltageLimit = EVMaximumVoltageLimit
    def get_EVEnergyCapacity(self):
        return self.EVEnergyCapacity
    def set_EVEnergyCapacity(self, EVEnergyCapacity):
        self.EVEnergyCapacity = EVEnergyCapacity
    def get_EVEnergyRequest(self):
        return self.EVEnergyRequest
    def set_EVEnergyRequest(self, EVEnergyRequest):
        self.EVEnergyRequest = EVEnergyRequest
    def get_FullSOC(self):
        return self.FullSOC
    def set_FullSOC(self, FullSOC):
        self.FullSOC = FullSOC
    def get_BulkSOC(self):
        return self.BulkSOC
    def set_BulkSOC(self, BulkSOC):
        self.BulkSOC = BulkSOC
    def validate_percentValueType(self, value):
        result = True
        # Validate type percentValueType, a restriction on xs:byte.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on percentValueType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on percentValueType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.DC_EVStatus is not None or
            self.EVMaximumCurrentLimit is not None or
            self.EVMaximumPowerLimit is not None or
            self.EVMaximumVoltageLimit is not None or
            self.EVEnergyCapacity is not None or
            self.EVEnergyRequest is not None or
            self.FullSOC is not None or
            self.BulkSOC is not None or
            super(DC_EVChargeParameterType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='DC_EVChargeParameterType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DC_EVChargeParameterType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DC_EVChargeParameterType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DC_EVChargeParameterType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DC_EVChargeParameterType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DC_EVChargeParameterType'):
        super(DC_EVChargeParameterType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DC_EVChargeParameterType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='DC_EVChargeParameterType', fromsubclass_=False, pretty_print=True):
        super(DC_EVChargeParameterType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.DC_EVStatus is not None:
            namespaceprefix_ = self.DC_EVStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.DC_EVStatus_nsprefix_) else ''
            self.DC_EVStatus.export(outfile, level, namespaceprefix_, namespacedef_='', name_='DC_EVStatus', pretty_print=pretty_print)
        if self.EVMaximumCurrentLimit is not None:
            namespaceprefix_ = self.EVMaximumCurrentLimit_nsprefix_ + ':' if (UseCapturedNS_ and self.EVMaximumCurrentLimit_nsprefix_) else ''
            self.EVMaximumCurrentLimit.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVMaximumCurrentLimit', pretty_print=pretty_print)
        if self.EVMaximumPowerLimit is not None:
            namespaceprefix_ = self.EVMaximumPowerLimit_nsprefix_ + ':' if (UseCapturedNS_ and self.EVMaximumPowerLimit_nsprefix_) else ''
            self.EVMaximumPowerLimit.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVMaximumPowerLimit', pretty_print=pretty_print)
        if self.EVMaximumVoltageLimit is not None:
            namespaceprefix_ = self.EVMaximumVoltageLimit_nsprefix_ + ':' if (UseCapturedNS_ and self.EVMaximumVoltageLimit_nsprefix_) else ''
            self.EVMaximumVoltageLimit.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVMaximumVoltageLimit', pretty_print=pretty_print)
        if self.EVEnergyCapacity is not None:
            namespaceprefix_ = self.EVEnergyCapacity_nsprefix_ + ':' if (UseCapturedNS_ and self.EVEnergyCapacity_nsprefix_) else ''
            self.EVEnergyCapacity.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVEnergyCapacity', pretty_print=pretty_print)
        if self.EVEnergyRequest is not None:
            namespaceprefix_ = self.EVEnergyRequest_nsprefix_ + ':' if (UseCapturedNS_ and self.EVEnergyRequest_nsprefix_) else ''
            self.EVEnergyRequest.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVEnergyRequest', pretty_print=pretty_print)
        if self.FullSOC is not None:
            namespaceprefix_ = self.FullSOC_nsprefix_ + ':' if (UseCapturedNS_ and self.FullSOC_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sFullSOC>%s</%sFullSOC>%s' % (namespaceprefix_ , self.gds_format_integer(self.FullSOC, input_name='FullSOC'), namespaceprefix_ , eol_))
        if self.BulkSOC is not None:
            namespaceprefix_ = self.BulkSOC_nsprefix_ + ':' if (UseCapturedNS_ and self.BulkSOC_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBulkSOC>%s</%sBulkSOC>%s' % (namespaceprefix_ , self.gds_format_integer(self.BulkSOC, input_name='BulkSOC'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(DC_EVChargeParameterType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'DC_EVStatus':
            obj_ = DC_EVStatusType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DC_EVStatus = obj_
            obj_.original_tagname_ = 'DC_EVStatus'
        elif nodeName_ == 'EVMaximumCurrentLimit':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVMaximumCurrentLimit = obj_
            obj_.original_tagname_ = 'EVMaximumCurrentLimit'
        elif nodeName_ == 'EVMaximumPowerLimit':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVMaximumPowerLimit = obj_
            obj_.original_tagname_ = 'EVMaximumPowerLimit'
        elif nodeName_ == 'EVMaximumVoltageLimit':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVMaximumVoltageLimit = obj_
            obj_.original_tagname_ = 'EVMaximumVoltageLimit'
        elif nodeName_ == 'EVEnergyCapacity':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVEnergyCapacity = obj_
            obj_.original_tagname_ = 'EVEnergyCapacity'
        elif nodeName_ == 'EVEnergyRequest':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVEnergyRequest = obj_
            obj_.original_tagname_ = 'EVEnergyRequest'
        elif nodeName_ == 'FullSOC' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'FullSOC')
            ival_ = self.gds_validate_integer(ival_, node, 'FullSOC')
            self.FullSOC = ival_
            self.FullSOC_nsprefix_ = child_.prefix
            # validate type percentValueType
            self.validate_percentValueType(self.FullSOC)
        elif nodeName_ == 'BulkSOC' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'BulkSOC')
            ival_ = self.gds_validate_integer(ival_, node, 'BulkSOC')
            self.BulkSOC = ival_
            self.BulkSOC_nsprefix_ = child_.prefix
            # validate type percentValueType
            self.validate_percentValueType(self.BulkSOC)
        super(DC_EVChargeParameterType, self)._buildChildren(child_, node, nodeName_, True)
# end class DC_EVChargeParameterType


class EVSEChargeParameterType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, EVSEChargeParameterType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if EVSEChargeParameterType.subclass:
            return EVSEChargeParameterType.subclass(*args_, **kwargs_)
        else:
            return EVSEChargeParameterType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='EVSEChargeParameterType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('EVSEChargeParameterType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'EVSEChargeParameterType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='EVSEChargeParameterType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='EVSEChargeParameterType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='EVSEChargeParameterType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='EVSEChargeParameterType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class EVSEChargeParameterType


class AC_EVSEChargeParameterType(EVSEChargeParameterType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = EVSEChargeParameterType
    def __init__(self, AC_EVSEStatus=None, EVSENominalVoltage=None, EVSEMaxCurrent=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("AC_EVSEChargeParameterType"), self).__init__( **kwargs_)
        self.AC_EVSEStatus = AC_EVSEStatus
        self.AC_EVSEStatus_nsprefix_ = None
        self.EVSENominalVoltage = EVSENominalVoltage
        self.EVSENominalVoltage_nsprefix_ = None
        self.EVSEMaxCurrent = EVSEMaxCurrent
        self.EVSEMaxCurrent_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AC_EVSEChargeParameterType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AC_EVSEChargeParameterType.subclass:
            return AC_EVSEChargeParameterType.subclass(*args_, **kwargs_)
        else:
            return AC_EVSEChargeParameterType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_AC_EVSEStatus(self):
        return self.AC_EVSEStatus
    def set_AC_EVSEStatus(self, AC_EVSEStatus):
        self.AC_EVSEStatus = AC_EVSEStatus
    def get_EVSENominalVoltage(self):
        return self.EVSENominalVoltage
    def set_EVSENominalVoltage(self, EVSENominalVoltage):
        self.EVSENominalVoltage = EVSENominalVoltage
    def get_EVSEMaxCurrent(self):
        return self.EVSEMaxCurrent
    def set_EVSEMaxCurrent(self, EVSEMaxCurrent):
        self.EVSEMaxCurrent = EVSEMaxCurrent
    def _hasContent(self):
        if (
            self.AC_EVSEStatus is not None or
            self.EVSENominalVoltage is not None or
            self.EVSEMaxCurrent is not None or
            super(AC_EVSEChargeParameterType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='AC_EVSEChargeParameterType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AC_EVSEChargeParameterType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AC_EVSEChargeParameterType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AC_EVSEChargeParameterType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AC_EVSEChargeParameterType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AC_EVSEChargeParameterType'):
        super(AC_EVSEChargeParameterType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AC_EVSEChargeParameterType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='AC_EVSEChargeParameterType', fromsubclass_=False, pretty_print=True):
        super(AC_EVSEChargeParameterType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.AC_EVSEStatus is not None:
            namespaceprefix_ = self.AC_EVSEStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.AC_EVSEStatus_nsprefix_) else ''
            self.AC_EVSEStatus.export(outfile, level, namespaceprefix_, namespacedef_='', name_='AC_EVSEStatus', pretty_print=pretty_print)
        if self.EVSENominalVoltage is not None:
            namespaceprefix_ = self.EVSENominalVoltage_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSENominalVoltage_nsprefix_) else ''
            self.EVSENominalVoltage.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVSENominalVoltage', pretty_print=pretty_print)
        if self.EVSEMaxCurrent is not None:
            namespaceprefix_ = self.EVSEMaxCurrent_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEMaxCurrent_nsprefix_) else ''
            self.EVSEMaxCurrent.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVSEMaxCurrent', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(AC_EVSEChargeParameterType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'AC_EVSEStatus':
            obj_ = AC_EVSEStatusType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.AC_EVSEStatus = obj_
            obj_.original_tagname_ = 'AC_EVSEStatus'
        elif nodeName_ == 'EVSENominalVoltage':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSENominalVoltage = obj_
            obj_.original_tagname_ = 'EVSENominalVoltage'
        elif nodeName_ == 'EVSEMaxCurrent':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSEMaxCurrent = obj_
            obj_.original_tagname_ = 'EVSEMaxCurrent'
        super(AC_EVSEChargeParameterType, self)._buildChildren(child_, node, nodeName_, True)
# end class AC_EVSEChargeParameterType


class DC_EVSEChargeParameterType(EVSEChargeParameterType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = EVSEChargeParameterType
    def __init__(self, DC_EVSEStatus=None, EVSEMaximumCurrentLimit=None, EVSEMaximumPowerLimit=None, EVSEMaximumVoltageLimit=None, EVSEMinimumCurrentLimit=None, EVSEMinimumVoltageLimit=None, EVSECurrentRegulationTolerance=None, EVSEPeakCurrentRipple=None, EVSEEnergyToBeDelivered=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("DC_EVSEChargeParameterType"), self).__init__( **kwargs_)
        self.DC_EVSEStatus = DC_EVSEStatus
        self.DC_EVSEStatus_nsprefix_ = None
        self.EVSEMaximumCurrentLimit = EVSEMaximumCurrentLimit
        self.EVSEMaximumCurrentLimit_nsprefix_ = None
        self.EVSEMaximumPowerLimit = EVSEMaximumPowerLimit
        self.EVSEMaximumPowerLimit_nsprefix_ = None
        self.EVSEMaximumVoltageLimit = EVSEMaximumVoltageLimit
        self.EVSEMaximumVoltageLimit_nsprefix_ = None
        self.EVSEMinimumCurrentLimit = EVSEMinimumCurrentLimit
        self.EVSEMinimumCurrentLimit_nsprefix_ = None
        self.EVSEMinimumVoltageLimit = EVSEMinimumVoltageLimit
        self.EVSEMinimumVoltageLimit_nsprefix_ = None
        self.EVSECurrentRegulationTolerance = EVSECurrentRegulationTolerance
        self.EVSECurrentRegulationTolerance_nsprefix_ = None
        self.EVSEPeakCurrentRipple = EVSEPeakCurrentRipple
        self.EVSEPeakCurrentRipple_nsprefix_ = None
        self.EVSEEnergyToBeDelivered = EVSEEnergyToBeDelivered
        self.EVSEEnergyToBeDelivered_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DC_EVSEChargeParameterType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DC_EVSEChargeParameterType.subclass:
            return DC_EVSEChargeParameterType.subclass(*args_, **kwargs_)
        else:
            return DC_EVSEChargeParameterType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_DC_EVSEStatus(self):
        return self.DC_EVSEStatus
    def set_DC_EVSEStatus(self, DC_EVSEStatus):
        self.DC_EVSEStatus = DC_EVSEStatus
    def get_EVSEMaximumCurrentLimit(self):
        return self.EVSEMaximumCurrentLimit
    def set_EVSEMaximumCurrentLimit(self, EVSEMaximumCurrentLimit):
        self.EVSEMaximumCurrentLimit = EVSEMaximumCurrentLimit
    def get_EVSEMaximumPowerLimit(self):
        return self.EVSEMaximumPowerLimit
    def set_EVSEMaximumPowerLimit(self, EVSEMaximumPowerLimit):
        self.EVSEMaximumPowerLimit = EVSEMaximumPowerLimit
    def get_EVSEMaximumVoltageLimit(self):
        return self.EVSEMaximumVoltageLimit
    def set_EVSEMaximumVoltageLimit(self, EVSEMaximumVoltageLimit):
        self.EVSEMaximumVoltageLimit = EVSEMaximumVoltageLimit
    def get_EVSEMinimumCurrentLimit(self):
        return self.EVSEMinimumCurrentLimit
    def set_EVSEMinimumCurrentLimit(self, EVSEMinimumCurrentLimit):
        self.EVSEMinimumCurrentLimit = EVSEMinimumCurrentLimit
    def get_EVSEMinimumVoltageLimit(self):
        return self.EVSEMinimumVoltageLimit
    def set_EVSEMinimumVoltageLimit(self, EVSEMinimumVoltageLimit):
        self.EVSEMinimumVoltageLimit = EVSEMinimumVoltageLimit
    def get_EVSECurrentRegulationTolerance(self):
        return self.EVSECurrentRegulationTolerance
    def set_EVSECurrentRegulationTolerance(self, EVSECurrentRegulationTolerance):
        self.EVSECurrentRegulationTolerance = EVSECurrentRegulationTolerance
    def get_EVSEPeakCurrentRipple(self):
        return self.EVSEPeakCurrentRipple
    def set_EVSEPeakCurrentRipple(self, EVSEPeakCurrentRipple):
        self.EVSEPeakCurrentRipple = EVSEPeakCurrentRipple
    def get_EVSEEnergyToBeDelivered(self):
        return self.EVSEEnergyToBeDelivered
    def set_EVSEEnergyToBeDelivered(self, EVSEEnergyToBeDelivered):
        self.EVSEEnergyToBeDelivered = EVSEEnergyToBeDelivered
    def _hasContent(self):
        if (
            self.DC_EVSEStatus is not None or
            self.EVSEMaximumCurrentLimit is not None or
            self.EVSEMaximumPowerLimit is not None or
            self.EVSEMaximumVoltageLimit is not None or
            self.EVSEMinimumCurrentLimit is not None or
            self.EVSEMinimumVoltageLimit is not None or
            self.EVSECurrentRegulationTolerance is not None or
            self.EVSEPeakCurrentRipple is not None or
            self.EVSEEnergyToBeDelivered is not None or
            super(DC_EVSEChargeParameterType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='DC_EVSEChargeParameterType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DC_EVSEChargeParameterType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DC_EVSEChargeParameterType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DC_EVSEChargeParameterType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DC_EVSEChargeParameterType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DC_EVSEChargeParameterType'):
        super(DC_EVSEChargeParameterType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DC_EVSEChargeParameterType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='DC_EVSEChargeParameterType', fromsubclass_=False, pretty_print=True):
        super(DC_EVSEChargeParameterType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.DC_EVSEStatus is not None:
            namespaceprefix_ = self.DC_EVSEStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.DC_EVSEStatus_nsprefix_) else ''
            self.DC_EVSEStatus.export(outfile, level, namespaceprefix_, namespacedef_='', name_='DC_EVSEStatus', pretty_print=pretty_print)
        if self.EVSEMaximumCurrentLimit is not None:
            namespaceprefix_ = self.EVSEMaximumCurrentLimit_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEMaximumCurrentLimit_nsprefix_) else ''
            self.EVSEMaximumCurrentLimit.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVSEMaximumCurrentLimit', pretty_print=pretty_print)
        if self.EVSEMaximumPowerLimit is not None:
            namespaceprefix_ = self.EVSEMaximumPowerLimit_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEMaximumPowerLimit_nsprefix_) else ''
            self.EVSEMaximumPowerLimit.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVSEMaximumPowerLimit', pretty_print=pretty_print)
        if self.EVSEMaximumVoltageLimit is not None:
            namespaceprefix_ = self.EVSEMaximumVoltageLimit_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEMaximumVoltageLimit_nsprefix_) else ''
            self.EVSEMaximumVoltageLimit.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVSEMaximumVoltageLimit', pretty_print=pretty_print)
        if self.EVSEMinimumCurrentLimit is not None:
            namespaceprefix_ = self.EVSEMinimumCurrentLimit_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEMinimumCurrentLimit_nsprefix_) else ''
            self.EVSEMinimumCurrentLimit.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVSEMinimumCurrentLimit', pretty_print=pretty_print)
        if self.EVSEMinimumVoltageLimit is not None:
            namespaceprefix_ = self.EVSEMinimumVoltageLimit_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEMinimumVoltageLimit_nsprefix_) else ''
            self.EVSEMinimumVoltageLimit.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVSEMinimumVoltageLimit', pretty_print=pretty_print)
        if self.EVSECurrentRegulationTolerance is not None:
            namespaceprefix_ = self.EVSECurrentRegulationTolerance_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSECurrentRegulationTolerance_nsprefix_) else ''
            self.EVSECurrentRegulationTolerance.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVSECurrentRegulationTolerance', pretty_print=pretty_print)
        if self.EVSEPeakCurrentRipple is not None:
            namespaceprefix_ = self.EVSEPeakCurrentRipple_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEPeakCurrentRipple_nsprefix_) else ''
            self.EVSEPeakCurrentRipple.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVSEPeakCurrentRipple', pretty_print=pretty_print)
        if self.EVSEEnergyToBeDelivered is not None:
            namespaceprefix_ = self.EVSEEnergyToBeDelivered_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEEnergyToBeDelivered_nsprefix_) else ''
            self.EVSEEnergyToBeDelivered.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVSEEnergyToBeDelivered', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(DC_EVSEChargeParameterType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'DC_EVSEStatus':
            obj_ = DC_EVSEStatusType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DC_EVSEStatus = obj_
            obj_.original_tagname_ = 'DC_EVSEStatus'
        elif nodeName_ == 'EVSEMaximumCurrentLimit':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSEMaximumCurrentLimit = obj_
            obj_.original_tagname_ = 'EVSEMaximumCurrentLimit'
        elif nodeName_ == 'EVSEMaximumPowerLimit':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSEMaximumPowerLimit = obj_
            obj_.original_tagname_ = 'EVSEMaximumPowerLimit'
        elif nodeName_ == 'EVSEMaximumVoltageLimit':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSEMaximumVoltageLimit = obj_
            obj_.original_tagname_ = 'EVSEMaximumVoltageLimit'
        elif nodeName_ == 'EVSEMinimumCurrentLimit':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSEMinimumCurrentLimit = obj_
            obj_.original_tagname_ = 'EVSEMinimumCurrentLimit'
        elif nodeName_ == 'EVSEMinimumVoltageLimit':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSEMinimumVoltageLimit = obj_
            obj_.original_tagname_ = 'EVSEMinimumVoltageLimit'
        elif nodeName_ == 'EVSECurrentRegulationTolerance':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSECurrentRegulationTolerance = obj_
            obj_.original_tagname_ = 'EVSECurrentRegulationTolerance'
        elif nodeName_ == 'EVSEPeakCurrentRipple':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSEPeakCurrentRipple = obj_
            obj_.original_tagname_ = 'EVSEPeakCurrentRipple'
        elif nodeName_ == 'EVSEEnergyToBeDelivered':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSEEnergyToBeDelivered = obj_
            obj_.original_tagname_ = 'EVSEEnergyToBeDelivered'
        super(DC_EVSEChargeParameterType, self)._buildChildren(child_, node, nodeName_, True)
# end class DC_EVSEChargeParameterType


class EVPowerDeliveryParameterType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, EVPowerDeliveryParameterType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if EVPowerDeliveryParameterType.subclass:
            return EVPowerDeliveryParameterType.subclass(*args_, **kwargs_)
        else:
            return EVPowerDeliveryParameterType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='EVPowerDeliveryParameterType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('EVPowerDeliveryParameterType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'EVPowerDeliveryParameterType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='EVPowerDeliveryParameterType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='EVPowerDeliveryParameterType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='EVPowerDeliveryParameterType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='EVPowerDeliveryParameterType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class EVPowerDeliveryParameterType


class DC_EVPowerDeliveryParameterType(EVPowerDeliveryParameterType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = EVPowerDeliveryParameterType
    def __init__(self, DC_EVStatus=None, BulkChargingComplete=None, ChargingComplete=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("DC_EVPowerDeliveryParameterType"), self).__init__( **kwargs_)
        self.DC_EVStatus = DC_EVStatus
        self.DC_EVStatus_nsprefix_ = None
        self.BulkChargingComplete = BulkChargingComplete
        self.BulkChargingComplete_nsprefix_ = None
        self.ChargingComplete = ChargingComplete
        self.ChargingComplete_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DC_EVPowerDeliveryParameterType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DC_EVPowerDeliveryParameterType.subclass:
            return DC_EVPowerDeliveryParameterType.subclass(*args_, **kwargs_)
        else:
            return DC_EVPowerDeliveryParameterType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_DC_EVStatus(self):
        return self.DC_EVStatus
    def set_DC_EVStatus(self, DC_EVStatus):
        self.DC_EVStatus = DC_EVStatus
    def get_BulkChargingComplete(self):
        return self.BulkChargingComplete
    def set_BulkChargingComplete(self, BulkChargingComplete):
        self.BulkChargingComplete = BulkChargingComplete
    def get_ChargingComplete(self):
        return self.ChargingComplete
    def set_ChargingComplete(self, ChargingComplete):
        self.ChargingComplete = ChargingComplete
    def _hasContent(self):
        if (
            self.DC_EVStatus is not None or
            self.BulkChargingComplete is not None or
            self.ChargingComplete is not None or
            super(DC_EVPowerDeliveryParameterType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='DC_EVPowerDeliveryParameterType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DC_EVPowerDeliveryParameterType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DC_EVPowerDeliveryParameterType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DC_EVPowerDeliveryParameterType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DC_EVPowerDeliveryParameterType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DC_EVPowerDeliveryParameterType'):
        super(DC_EVPowerDeliveryParameterType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DC_EVPowerDeliveryParameterType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='DC_EVPowerDeliveryParameterType', fromsubclass_=False, pretty_print=True):
        super(DC_EVPowerDeliveryParameterType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.DC_EVStatus is not None:
            namespaceprefix_ = self.DC_EVStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.DC_EVStatus_nsprefix_) else ''
            self.DC_EVStatus.export(outfile, level, namespaceprefix_, namespacedef_='', name_='DC_EVStatus', pretty_print=pretty_print)
        if self.BulkChargingComplete is not None:
            namespaceprefix_ = self.BulkChargingComplete_nsprefix_ + ':' if (UseCapturedNS_ and self.BulkChargingComplete_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBulkChargingComplete>%s</%sBulkChargingComplete>%s' % (namespaceprefix_ , self.gds_format_boolean(self.BulkChargingComplete, input_name='BulkChargingComplete'), namespaceprefix_ , eol_))
        if self.ChargingComplete is not None:
            namespaceprefix_ = self.ChargingComplete_nsprefix_ + ':' if (UseCapturedNS_ and self.ChargingComplete_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sChargingComplete>%s</%sChargingComplete>%s' % (namespaceprefix_ , self.gds_format_boolean(self.ChargingComplete, input_name='ChargingComplete'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(DC_EVPowerDeliveryParameterType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'DC_EVStatus':
            obj_ = DC_EVStatusType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DC_EVStatus = obj_
            obj_.original_tagname_ = 'DC_EVStatus'
        elif nodeName_ == 'BulkChargingComplete':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'BulkChargingComplete')
            ival_ = self.gds_validate_boolean(ival_, node, 'BulkChargingComplete')
            self.BulkChargingComplete = ival_
            self.BulkChargingComplete_nsprefix_ = child_.prefix
        elif nodeName_ == 'ChargingComplete':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'ChargingComplete')
            ival_ = self.gds_validate_boolean(ival_, node, 'ChargingComplete')
            self.ChargingComplete = ival_
            self.ChargingComplete_nsprefix_ = child_.prefix
        super(DC_EVPowerDeliveryParameterType, self)._buildChildren(child_, node, nodeName_, True)
# end class DC_EVPowerDeliveryParameterType


class ChargingProfileType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ProfileEntry=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if ProfileEntry is None:
            self.ProfileEntry = []
        else:
            self.ProfileEntry = ProfileEntry
        self.ProfileEntry_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ChargingProfileType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ChargingProfileType.subclass:
            return ChargingProfileType.subclass(*args_, **kwargs_)
        else:
            return ChargingProfileType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ProfileEntry(self):
        return self.ProfileEntry
    def set_ProfileEntry(self, ProfileEntry):
        self.ProfileEntry = ProfileEntry
    def add_ProfileEntry(self, value):
        self.ProfileEntry.append(value)
    def insert_ProfileEntry_at(self, index, value):
        self.ProfileEntry.insert(index, value)
    def replace_ProfileEntry_at(self, index, value):
        self.ProfileEntry[index] = value
    def _hasContent(self):
        if (
            self.ProfileEntry
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='ChargingProfileType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ChargingProfileType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ChargingProfileType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ChargingProfileType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ChargingProfileType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ChargingProfileType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='ChargingProfileType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for ProfileEntry_ in self.ProfileEntry:
            namespaceprefix_ = self.ProfileEntry_nsprefix_ + ':' if (UseCapturedNS_ and self.ProfileEntry_nsprefix_) else ''
            ProfileEntry_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ProfileEntry', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ProfileEntry':
            obj_ = ProfileEntryType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ProfileEntry.append(obj_)
            obj_.original_tagname_ = 'ProfileEntry'
# end class ChargingProfileType


class ProfileEntryType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ChargingProfileEntryStart=None, ChargingProfileEntryMaxPower=None, ChargingProfileEntryMaxNumberOfPhasesInUse=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ChargingProfileEntryStart = ChargingProfileEntryStart
        self.ChargingProfileEntryStart_nsprefix_ = None
        self.ChargingProfileEntryMaxPower = ChargingProfileEntryMaxPower
        self.ChargingProfileEntryMaxPower_nsprefix_ = None
        self.ChargingProfileEntryMaxNumberOfPhasesInUse = ChargingProfileEntryMaxNumberOfPhasesInUse
        self.validate_maxNumPhasesType(self.ChargingProfileEntryMaxNumberOfPhasesInUse)
        self.ChargingProfileEntryMaxNumberOfPhasesInUse_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ProfileEntryType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ProfileEntryType.subclass:
            return ProfileEntryType.subclass(*args_, **kwargs_)
        else:
            return ProfileEntryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ChargingProfileEntryStart(self):
        return self.ChargingProfileEntryStart
    def set_ChargingProfileEntryStart(self, ChargingProfileEntryStart):
        self.ChargingProfileEntryStart = ChargingProfileEntryStart
    def get_ChargingProfileEntryMaxPower(self):
        return self.ChargingProfileEntryMaxPower
    def set_ChargingProfileEntryMaxPower(self, ChargingProfileEntryMaxPower):
        self.ChargingProfileEntryMaxPower = ChargingProfileEntryMaxPower
    def get_ChargingProfileEntryMaxNumberOfPhasesInUse(self):
        return self.ChargingProfileEntryMaxNumberOfPhasesInUse
    def set_ChargingProfileEntryMaxNumberOfPhasesInUse(self, ChargingProfileEntryMaxNumberOfPhasesInUse):
        self.ChargingProfileEntryMaxNumberOfPhasesInUse = ChargingProfileEntryMaxNumberOfPhasesInUse
    def validate_maxNumPhasesType(self, value):
        result = True
        # Validate type maxNumPhasesType, a restriction on xs:byte.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on maxNumPhasesType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on maxNumPhasesType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.ChargingProfileEntryStart is not None or
            self.ChargingProfileEntryMaxPower is not None or
            self.ChargingProfileEntryMaxNumberOfPhasesInUse is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='ProfileEntryType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ProfileEntryType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ProfileEntryType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ProfileEntryType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ProfileEntryType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ProfileEntryType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='ProfileEntryType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ChargingProfileEntryStart is not None:
            namespaceprefix_ = self.ChargingProfileEntryStart_nsprefix_ + ':' if (UseCapturedNS_ and self.ChargingProfileEntryStart_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sChargingProfileEntryStart>%s</%sChargingProfileEntryStart>%s' % (namespaceprefix_ , self.gds_format_integer(self.ChargingProfileEntryStart, input_name='ChargingProfileEntryStart'), namespaceprefix_ , eol_))
        if self.ChargingProfileEntryMaxPower is not None:
            namespaceprefix_ = self.ChargingProfileEntryMaxPower_nsprefix_ + ':' if (UseCapturedNS_ and self.ChargingProfileEntryMaxPower_nsprefix_) else ''
            self.ChargingProfileEntryMaxPower.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ChargingProfileEntryMaxPower', pretty_print=pretty_print)
        if self.ChargingProfileEntryMaxNumberOfPhasesInUse is not None:
            namespaceprefix_ = self.ChargingProfileEntryMaxNumberOfPhasesInUse_nsprefix_ + ':' if (UseCapturedNS_ and self.ChargingProfileEntryMaxNumberOfPhasesInUse_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sChargingProfileEntryMaxNumberOfPhasesInUse>%s</%sChargingProfileEntryMaxNumberOfPhasesInUse>%s' % (namespaceprefix_ , self.gds_format_integer(self.ChargingProfileEntryMaxNumberOfPhasesInUse, input_name='ChargingProfileEntryMaxNumberOfPhasesInUse'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ChargingProfileEntryStart' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'ChargingProfileEntryStart')
            ival_ = self.gds_validate_integer(ival_, node, 'ChargingProfileEntryStart')
            self.ChargingProfileEntryStart = ival_
            self.ChargingProfileEntryStart_nsprefix_ = child_.prefix
        elif nodeName_ == 'ChargingProfileEntryMaxPower':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ChargingProfileEntryMaxPower = obj_
            obj_.original_tagname_ = 'ChargingProfileEntryMaxPower'
        elif nodeName_ == 'ChargingProfileEntryMaxNumberOfPhasesInUse' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'ChargingProfileEntryMaxNumberOfPhasesInUse')
            ival_ = self.gds_validate_integer(ival_, node, 'ChargingProfileEntryMaxNumberOfPhasesInUse')
            self.ChargingProfileEntryMaxNumberOfPhasesInUse = ival_
            self.ChargingProfileEntryMaxNumberOfPhasesInUse_nsprefix_ = child_.prefix
            # validate type maxNumPhasesType
            self.validate_maxNumPhasesType(self.ChargingProfileEntryMaxNumberOfPhasesInUse)
# end class ProfileEntryType


class PaymentOptionListType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, PaymentOption=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if PaymentOption is None:
            self.PaymentOption = []
        else:
            self.PaymentOption = PaymentOption
        self.PaymentOption_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PaymentOptionListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PaymentOptionListType.subclass:
            return PaymentOptionListType.subclass(*args_, **kwargs_)
        else:
            return PaymentOptionListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_PaymentOption(self):
        return self.PaymentOption
    def set_PaymentOption(self, PaymentOption):
        self.PaymentOption = PaymentOption
    def add_PaymentOption(self, value):
        self.PaymentOption.append(value)
    def insert_PaymentOption_at(self, index, value):
        self.PaymentOption.insert(index, value)
    def replace_PaymentOption_at(self, index, value):
        self.PaymentOption[index] = value
    def validate_paymentOptionType(self, value):
        result = True
        # Validate type paymentOptionType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Contract', 'ExternalPayment']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on paymentOptionType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.PaymentOption
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='PaymentOptionListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PaymentOptionListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PaymentOptionListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PaymentOptionListType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PaymentOptionListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PaymentOptionListType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='PaymentOptionListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for PaymentOption_ in self.PaymentOption:
            namespaceprefix_ = self.PaymentOption_nsprefix_ + ':' if (UseCapturedNS_ and self.PaymentOption_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPaymentOption>%s</%sPaymentOption>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(PaymentOption_), input_name='PaymentOption')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'PaymentOption':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PaymentOption')
            value_ = self.gds_validate_string(value_, node, 'PaymentOption')
            self.PaymentOption.append(value_)
            self.PaymentOption_nsprefix_ = child_.prefix
            # validate type paymentOptionType
            self.validate_paymentOptionType(self.PaymentOption[-1])
# end class PaymentOptionListType


class SignatureType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Id=None, SignedInfo=None, SignatureValue=None, KeyInfo=None, Object=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.SignedInfo = SignedInfo
        self.SignedInfo_nsprefix_ = "xmlsig"
        self.SignatureValue = SignatureValue
        self.SignatureValue_nsprefix_ = "xmlsig"
        self.KeyInfo = KeyInfo
        self.KeyInfo_nsprefix_ = "xmlsig"
        if Object is None:
            self.Object = []
        else:
            self.Object = Object
        self.Object_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignatureType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignatureType.subclass:
            return SignatureType.subclass(*args_, **kwargs_)
        else:
            return SignatureType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_SignedInfo(self):
        return self.SignedInfo
    def set_SignedInfo(self, SignedInfo):
        self.SignedInfo = SignedInfo
    def get_SignatureValue(self):
        return self.SignatureValue
    def set_SignatureValue(self, SignatureValue):
        self.SignatureValue = SignatureValue
    def get_KeyInfo(self):
        return self.KeyInfo
    def set_KeyInfo(self, KeyInfo):
        self.KeyInfo = KeyInfo
    def get_Object(self):
        return self.Object
    def set_Object(self, Object):
        self.Object = Object
    def add_Object(self, value):
        self.Object.append(value)
    def insert_Object_at(self, index, value):
        self.Object.insert(index, value)
    def replace_Object_at(self, index, value):
        self.Object[index] = value
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def _hasContent(self):
        if (
            self.SignedInfo is not None or
            self.SignatureValue is not None or
            self.KeyInfo is not None or
            self.Object
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#" ', name_='SignatureType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignatureType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignatureType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignatureType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignatureType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignatureType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#" ', name_='SignatureType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.SignedInfo is not None:
            namespaceprefix_ = self.SignedInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.SignedInfo_nsprefix_) else ''
            self.SignedInfo.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignedInfo', pretty_print=pretty_print)
        if self.SignatureValue is not None:
            namespaceprefix_ = self.SignatureValue_nsprefix_ + ':' if (UseCapturedNS_ and self.SignatureValue_nsprefix_) else ''
            self.SignatureValue.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureValue', pretty_print=pretty_print)
        if self.KeyInfo is not None:
            namespaceprefix_ = self.KeyInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.KeyInfo_nsprefix_) else ''
            self.KeyInfo.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='KeyInfo', pretty_print=pretty_print)
        for Object_ in self.Object:
            namespaceprefix_ = self.Object_nsprefix_ + ':' if (UseCapturedNS_ and self.Object_nsprefix_) else ''
            Object_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Object', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'SignedInfo':
            obj_ = SignedInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SignedInfo = obj_
            obj_.original_tagname_ = 'SignedInfo'
        elif nodeName_ == 'SignatureValue':
            obj_ = SignatureValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SignatureValue = obj_
            obj_.original_tagname_ = 'SignatureValue'
        elif nodeName_ == 'KeyInfo':
            obj_ = KeyInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.KeyInfo = obj_
            obj_.original_tagname_ = 'KeyInfo'
        elif nodeName_ == 'Object':
            obj_ = ObjectType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Object.append(obj_)
            obj_.original_tagname_ = 'Object'
# end class SignatureType


class SignatureValueType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Id=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignatureValueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignatureValueType.subclass:
            return SignatureValueType.subclass(*args_, **kwargs_)
        else:
            return SignatureValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureValueType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignatureValueType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignatureValueType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignatureValueType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignatureValueType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignatureValueType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureValueType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class SignatureValueType


class SignedInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Id=None, CanonicalizationMethod=None, SignatureMethod=None, Reference=None, gds_collector_=None, **kwargs_):
        
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.CanonicalizationMethod = CanonicalizationMethod
        self.CanonicalizationMethod_nsprefix_ = "xmlsig"
        self.SignatureMethod = SignatureMethod
        self.SignatureMethod_nsprefix_ = "xmlsig"
        if Reference is None:
            self.Reference = []
        else:
            self.Reference = Reference
        self.Reference_nsprefix_ = "xmlsig"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignedInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignedInfoType.subclass:
            return SignedInfoType.subclass(*args_, **kwargs_)
        else:
            return SignedInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_CanonicalizationMethod(self):
        return self.CanonicalizationMethod
    def set_CanonicalizationMethod(self, CanonicalizationMethod):
        self.CanonicalizationMethod = CanonicalizationMethod
    def get_SignatureMethod(self):
        return self.SignatureMethod
    def set_SignatureMethod(self, SignatureMethod):
        self.SignatureMethod = SignatureMethod
    def get_Reference(self):
        return self.Reference
    def set_Reference(self, Reference):
        self.Reference = Reference
    def add_Reference(self, value):
        self.Reference.append(value)
    def insert_Reference_at(self, index, value):
        self.Reference.insert(index, value)
    def replace_Reference_at(self, index, value):
        self.Reference[index] = value
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def _hasContent(self):
        if (
            self.CanonicalizationMethod is not None or
            self.SignatureMethod is not None or
            self.Reference
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:xmlsig="http://www.w3.org/2000/09/xmldsig#" xmlns:ns4="http://www.w3.org/2000/09/xmldsig#" ', name_='SignedInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignedInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignedInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignedInfoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignedInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignedInfoType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#" ', name_='SignedInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CanonicalizationMethod is not None:
            namespaceprefix_ = self.CanonicalizationMethod_nsprefix_ + ':' if (UseCapturedNS_ and self.CanonicalizationMethod_nsprefix_) else ''
            self.CanonicalizationMethod.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='CanonicalizationMethod', pretty_print=pretty_print)
        if self.SignatureMethod is not None:
            namespaceprefix_ = self.SignatureMethod_nsprefix_ + ':' if (UseCapturedNS_ and self.SignatureMethod_nsprefix_) else ''
            self.SignatureMethod.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureMethod', pretty_print=pretty_print)
        for Reference_ in self.Reference:
            namespaceprefix_ = self.Reference_nsprefix_ + ':' if (UseCapturedNS_ and self.Reference_nsprefix_) else ''
            Reference_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Reference', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CanonicalizationMethod':
            obj_ = CanonicalizationMethodType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CanonicalizationMethod = obj_
            obj_.original_tagname_ = 'CanonicalizationMethod'
        elif nodeName_ == 'SignatureMethod':
            obj_ = SignatureMethodType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SignatureMethod = obj_
            obj_.original_tagname_ = 'SignatureMethod'
        elif nodeName_ == 'Reference':
            obj_ = ReferenceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Reference.append(obj_)
            obj_.original_tagname_ = 'Reference'
# end class SignedInfoType


class CanonicalizationMethodType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Algorithm=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Algorithm = _cast(None, Algorithm)
        self.Algorithm_nsprefix_ = None
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CanonicalizationMethodType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CanonicalizationMethodType.subclass:
            return CanonicalizationMethodType.subclass(*args_, **kwargs_)
        else:
            return CanonicalizationMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def add_anytypeobjs_(self, value): self.anytypeobjs_.append(value)
    def insert_anytypeobjs_(self, index, value): self._anytypeobjs_[index] = value
    def get_Algorithm(self):
        return self.Algorithm
    def set_Algorithm(self, Algorithm):
        self.Algorithm = Algorithm
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            self.anytypeobjs_ or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody"  xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='CanonicalizationMethodType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CanonicalizationMethodType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CanonicalizationMethodType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CanonicalizationMethodType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CanonicalizationMethodType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='CanonicalizationMethodType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (quote_attrib(self.Algorithm), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody"  xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='CanonicalizationMethodType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if not fromsubclass_:
            for obj_ in self.anytypeobjs_:
                showIndent(outfile, level, pretty_print)
                outfile.write(obj_)
                outfile.write('\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class CanonicalizationMethodType


class SignatureMethodType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Algorithm=None, HMACOutputLength=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Algorithm = _cast(None, Algorithm)
        self.Algorithm_nsprefix_ = None
        self.HMACOutputLength = HMACOutputLength
        self.validate_HMACOutputLengthType(self.HMACOutputLength)
        self.HMACOutputLength_nsprefix_ = "ds"
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignatureMethodType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignatureMethodType.subclass:
            return SignatureMethodType.subclass(*args_, **kwargs_)
        else:
            return SignatureMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_HMACOutputLength(self):
        return self.HMACOutputLength
    def set_HMACOutputLength(self, HMACOutputLength):
        self.HMACOutputLength = HMACOutputLength
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def add_anytypeobjs_(self, value): self.anytypeobjs_.append(value)
    def insert_anytypeobjs_(self, index, value): self._anytypeobjs_[index] = value
    def get_Algorithm(self):
        return self.Algorithm
    def set_Algorithm(self, Algorithm):
        self.Algorithm = Algorithm
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_HMACOutputLengthType(self, value):
        result = True
        # Validate type HMACOutputLengthType, a restriction on integer.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def _hasContent(self):
        if (
            self.HMACOutputLength is not None or
            self.anytypeobjs_ or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#"  xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='SignatureMethodType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignatureMethodType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignatureMethodType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignatureMethodType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignatureMethodType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignatureMethodType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (quote_attrib(self.Algorithm), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#"  xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='SignatureMethodType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.HMACOutputLength is not None:
            namespaceprefix_ = self.HMACOutputLength_nsprefix_ + ':' if (UseCapturedNS_ and self.HMACOutputLength_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sHMACOutputLength>%s</%sHMACOutputLength>%s' % (namespaceprefix_ , self.gds_format_integer(self.HMACOutputLength, input_name='HMACOutputLength'), namespaceprefix_ , eol_))
        if not fromsubclass_:
            for obj_ in self.anytypeobjs_:
                showIndent(outfile, level, pretty_print)
                outfile.write(obj_)
                outfile.write('\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'HMACOutputLength' and child_.text is not None:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'HMACOutputLength')
            ival_ = self.gds_validate_integer(ival_, node, 'HMACOutputLength')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeInteger, 'HMACOutputLength', ival_)
            self.content_.append(obj_)
            self.HMACOutputLength_nsprefix_ = child_.prefix
        elif nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class SignatureMethodType


class ReferenceType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Id=None, URI=None, Type=None, Transforms=None, DigestMethod=None, DigestValue=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.URI = _cast(None, URI)
        self.URI_nsprefix_ = None
        self.Type = _cast(None, Type)
        self.Type_nsprefix_ = None
        self.Transforms = Transforms
        self.Transforms_nsprefix_ = "xmlsig"
        self.DigestMethod = DigestMethod
        self.DigestMethod_nsprefix_ = "xmlsig"
        self.DigestValue = DigestValue
        self.DigestValue_nsprefix_ = "xmlsig"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ReferenceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ReferenceType.subclass:
            return ReferenceType.subclass(*args_, **kwargs_)
        else:
            return ReferenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Transforms(self):
        return self.Transforms
    def set_Transforms(self, Transforms):
        self.Transforms = Transforms
    def get_DigestMethod(self):
        return self.DigestMethod
    def set_DigestMethod(self, DigestMethod):
        self.DigestMethod = DigestMethod
    def get_DigestValue(self):
        return self.DigestValue
    def set_DigestValue(self, DigestValue):
        self.DigestValue = DigestValue
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def get_URI(self):
        return self.URI
    def set_URI(self, URI):
        self.URI = URI
    def get_Type(self):
        return self.Type
    def set_Type(self, Type):
        self.Type = Type
    def _hasContent(self):
        if (
            self.Transforms is not None or
            self.DigestMethod is not None or
            self.DigestValue is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#" ', name_='ReferenceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ReferenceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ReferenceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ReferenceType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ReferenceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='ReferenceType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
        if self.URI is not None and 'URI' not in already_processed:
            already_processed.add('URI')
            outfile.write(' URI=%s' % (quote_attrib(self.URI), ))
        if self.Type is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            outfile.write(' Type=%s' % (quote_attrib(self.Type), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#" ', name_='ReferenceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Transforms is not None:
            namespaceprefix_ = self.Transforms_nsprefix_ + ':' if (UseCapturedNS_ and self.Transforms_nsprefix_) else ''
            self.Transforms.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Transforms', pretty_print=pretty_print)
        if self.DigestMethod is not None:
            namespaceprefix_ = self.DigestMethod_nsprefix_ + ':' if (UseCapturedNS_ and self.DigestMethod_nsprefix_) else ''
            self.DigestMethod.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='DigestMethod', pretty_print=pretty_print)
        if self.DigestValue is not None:
            namespaceprefix_ = self.DigestValue_nsprefix_ + ':' if (UseCapturedNS_ and self.DigestValue_nsprefix_) else ''
            self.DigestValue.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='DigestValue', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
        value = find_attr_value_('URI', node)
        if value is not None and 'URI' not in already_processed:
            already_processed.add('URI')
            self.URI = value
        value = find_attr_value_('Type', node)
        if value is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            self.Type = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Transforms':
            obj_ = TransformsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Transforms = obj_
            obj_.original_tagname_ = 'Transforms'
        elif nodeName_ == 'DigestMethod':
            obj_ = DigestMethodType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DigestMethod = obj_
            obj_.original_tagname_ = 'DigestMethod'
        elif nodeName_ == 'DigestValue':
            obj_ = DigestValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DigestValue = obj_
            obj_.original_tagname_ = 'DigestValue'
# end class ReferenceType


class TransformsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Transform=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ds"
        if Transform is None:
            self.Transform = []
        else:
            self.Transform = Transform
        self.Transform_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TransformsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TransformsType.subclass:
            return TransformsType.subclass(*args_, **kwargs_)
        else:
            return TransformsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Transform(self):
        return self.Transform
    def set_Transform(self, Transform):
        self.Transform = Transform
    def add_Transform(self, value):
        self.Transform.append(value)
    def insert_Transform_at(self, index, value):
        self.Transform.insert(index, value)
    def replace_Transform_at(self, index, value):
        self.Transform[index] = value
    def _hasContent(self):
        if (
            self.Transform
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#" ', name_='TransformsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TransformsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TransformsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TransformsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TransformsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='TransformsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#" ', name_='TransformsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Transform_ in self.Transform:
            namespaceprefix_ = self.Transform_nsprefix_ + ':' if (UseCapturedNS_ and self.Transform_nsprefix_) else ''
            Transform_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Transform', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Transform':
            obj_ = TransformType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Transform.append(obj_)
            obj_.original_tagname_ = 'Transform'
# end class TransformsType


class TransformType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Algorithm=None, anytypeobjs_=None, XPath=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Algorithm = _cast(None, Algorithm)
        self.Algorithm_nsprefix_ = None
        self.anytypeobjs_ = anytypeobjs_
        if XPath is None:
            self.XPath = []
        else:
            self.XPath = XPath
        self.XPath_nsprefix_ = None
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TransformType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TransformType.subclass:
            return TransformType.subclass(*args_, **kwargs_)
        else:
            return TransformType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def get_XPath(self):
        return self.XPath
    def set_XPath(self, XPath):
        self.XPath = XPath
    def add_XPath(self, value):
        self.XPath.append(value)
    def insert_XPath_at(self, index, value):
        self.XPath.insert(index, value)
    def replace_XPath_at(self, index, value):
        self.XPath[index] = value
    def get_Algorithm(self):
        return self.Algorithm
    def set_Algorithm(self, Algorithm):
        self.Algorithm = Algorithm
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            self.anytypeobjs_ is not None or
            self.XPath or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody"  xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='TransformType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TransformType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TransformType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TransformType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TransformType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='TransformType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (quote_attrib(self.Algorithm), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody"  xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='TransformType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for XPath_ in self.XPath:
            namespaceprefix_ = self.XPath_nsprefix_ + ':' if (UseCapturedNS_ and self.XPath_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sXPath>%s</%sXPath>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(XPath_), input_name='XPath')), namespaceprefix_ , eol_))
        if not fromsubclass_:
            if self.anytypeobjs_ is not None:
                content_ = self.anytypeobjs_
                outfile.write(content_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        elif nodeName_ == 'XPath' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'XPath')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'XPath')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeString, 'XPath', valuestr_)
            self.content_.append(obj_)
            self.XPath_nsprefix_ = child_.prefix
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class TransformType


class DigestMethodType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Algorithm=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Algorithm = _cast(None, Algorithm)
        self.Algorithm_nsprefix_ = None
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DigestMethodType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DigestMethodType.subclass:
            return DigestMethodType.subclass(*args_, **kwargs_)
        else:
            return DigestMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def add_anytypeobjs_(self, value): self.anytypeobjs_.append(value)
    def insert_anytypeobjs_(self, index, value): self._anytypeobjs_[index] = value
    def get_Algorithm(self):
        return self.Algorithm
    def set_Algorithm(self, Algorithm):
        self.Algorithm = Algorithm
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            self.anytypeobjs_ or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody"  xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='DigestMethodType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DigestMethodType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DigestMethodType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DigestMethodType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DigestMethodType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='DigestMethodType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (quote_attrib(self.Algorithm), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody"  xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='DigestMethodType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if not fromsubclass_:
            for obj_ in self.anytypeobjs_:
                showIndent(outfile, level, pretty_print)
                outfile.write(obj_)
                outfile.write('\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class DigestMethodType


class KeyInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Id=None, KeyName=None, KeyValue=None, RetrievalMethod=None, X509Data=None, PGPData=None, SPKIData=None, MgmtData=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        if KeyName is None:
            self.KeyName = []
        else:
            self.KeyName = KeyName
        self.KeyName_nsprefix_ = "ds"
        if KeyValue is None:
            self.KeyValue = []
        else:
            self.KeyValue = KeyValue
        self.KeyValue_nsprefix_ = "ds"
        if RetrievalMethod is None:
            self.RetrievalMethod = []
        else:
            self.RetrievalMethod = RetrievalMethod
        self.RetrievalMethod_nsprefix_ = "ds"
        if X509Data is None:
            self.X509Data = []
        else:
            self.X509Data = X509Data
        self.X509Data_nsprefix_ = "ds"
        if PGPData is None:
            self.PGPData = []
        else:
            self.PGPData = PGPData
        self.PGPData_nsprefix_ = "ds"
        if SPKIData is None:
            self.SPKIData = []
        else:
            self.SPKIData = SPKIData
        self.SPKIData_nsprefix_ = "ds"
        if MgmtData is None:
            self.MgmtData = []
        else:
            self.MgmtData = MgmtData
        self.MgmtData_nsprefix_ = "ds"
        self.anytypeobjs_ = anytypeobjs_
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, KeyInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if KeyInfoType.subclass:
            return KeyInfoType.subclass(*args_, **kwargs_)
        else:
            return KeyInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_KeyName(self):
        return self.KeyName
    def set_KeyName(self, KeyName):
        self.KeyName = KeyName
    def add_KeyName(self, value):
        self.KeyName.append(value)
    def insert_KeyName_at(self, index, value):
        self.KeyName.insert(index, value)
    def replace_KeyName_at(self, index, value):
        self.KeyName[index] = value
    def get_KeyValue(self):
        return self.KeyValue
    def set_KeyValue(self, KeyValue):
        self.KeyValue = KeyValue
    def add_KeyValue(self, value):
        self.KeyValue.append(value)
    def insert_KeyValue_at(self, index, value):
        self.KeyValue.insert(index, value)
    def replace_KeyValue_at(self, index, value):
        self.KeyValue[index] = value
    def get_RetrievalMethod(self):
        return self.RetrievalMethod
    def set_RetrievalMethod(self, RetrievalMethod):
        self.RetrievalMethod = RetrievalMethod
    def add_RetrievalMethod(self, value):
        self.RetrievalMethod.append(value)
    def insert_RetrievalMethod_at(self, index, value):
        self.RetrievalMethod.insert(index, value)
    def replace_RetrievalMethod_at(self, index, value):
        self.RetrievalMethod[index] = value
    def get_X509Data(self):
        return self.X509Data
    def set_X509Data(self, X509Data):
        self.X509Data = X509Data
    def add_X509Data(self, value):
        self.X509Data.append(value)
    def insert_X509Data_at(self, index, value):
        self.X509Data.insert(index, value)
    def replace_X509Data_at(self, index, value):
        self.X509Data[index] = value
    def get_PGPData(self):
        return self.PGPData
    def set_PGPData(self, PGPData):
        self.PGPData = PGPData
    def add_PGPData(self, value):
        self.PGPData.append(value)
    def insert_PGPData_at(self, index, value):
        self.PGPData.insert(index, value)
    def replace_PGPData_at(self, index, value):
        self.PGPData[index] = value
    def get_SPKIData(self):
        return self.SPKIData
    def set_SPKIData(self, SPKIData):
        self.SPKIData = SPKIData
    def add_SPKIData(self, value):
        self.SPKIData.append(value)
    def insert_SPKIData_at(self, index, value):
        self.SPKIData.insert(index, value)
    def replace_SPKIData_at(self, index, value):
        self.SPKIData[index] = value
    def get_MgmtData(self):
        return self.MgmtData
    def set_MgmtData(self, MgmtData):
        self.MgmtData = MgmtData
    def add_MgmtData(self, value):
        self.MgmtData.append(value)
    def insert_MgmtData_at(self, index, value):
        self.MgmtData.insert(index, value)
    def replace_MgmtData_at(self, index, value):
        self.MgmtData[index] = value
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            self.KeyName or
            self.KeyValue or
            self.RetrievalMethod or
            self.X509Data or
            self.PGPData or
            self.SPKIData or
            self.MgmtData or
            self.anytypeobjs_ is not None or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#"  xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='KeyInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('KeyInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'KeyInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='KeyInfoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='KeyInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='KeyInfoType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#"  xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='KeyInfoType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for KeyName_ in self.KeyName:
            namespaceprefix_ = self.KeyName_nsprefix_ + ':' if (UseCapturedNS_ and self.KeyName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sKeyName>%s</%sKeyName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(KeyName_), input_name='KeyName')), namespaceprefix_ , eol_))
        for KeyValue_ in self.KeyValue:
            namespaceprefix_ = self.KeyValue_nsprefix_ + ':' if (UseCapturedNS_ and self.KeyValue_nsprefix_) else ''
            KeyValue_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='KeyValue', pretty_print=pretty_print)
        for RetrievalMethod_ in self.RetrievalMethod:
            namespaceprefix_ = self.RetrievalMethod_nsprefix_ + ':' if (UseCapturedNS_ and self.RetrievalMethod_nsprefix_) else ''
            RetrievalMethod_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='RetrievalMethod', pretty_print=pretty_print)
        for X509Data_ in self.X509Data:
            namespaceprefix_ = self.X509Data_nsprefix_ + ':' if (UseCapturedNS_ and self.X509Data_nsprefix_) else ''
            X509Data_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='X509Data', pretty_print=pretty_print)
        for PGPData_ in self.PGPData:
            namespaceprefix_ = self.PGPData_nsprefix_ + ':' if (UseCapturedNS_ and self.PGPData_nsprefix_) else ''
            PGPData_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='PGPData', pretty_print=pretty_print)
        for SPKIData_ in self.SPKIData:
            namespaceprefix_ = self.SPKIData_nsprefix_ + ':' if (UseCapturedNS_ and self.SPKIData_nsprefix_) else ''
            SPKIData_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SPKIData', pretty_print=pretty_print)
        for MgmtData_ in self.MgmtData:
            namespaceprefix_ = self.MgmtData_nsprefix_ + ':' if (UseCapturedNS_ and self.MgmtData_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMgmtData>%s</%sMgmtData>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(MgmtData_), input_name='MgmtData')), namespaceprefix_ , eol_))
        if not fromsubclass_:
            if self.anytypeobjs_ is not None:
                content_ = self.anytypeobjs_
                outfile.write(content_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'KeyName' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'KeyName')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'KeyName')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeString, 'KeyName', valuestr_)
            self.content_.append(obj_)
            self.KeyName_nsprefix_ = child_.prefix
        elif nodeName_ == 'KeyValue':
            obj_ = KeyValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'KeyValue', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_KeyValue'):
              self.add_KeyValue(obj_.value)
            elif hasattr(self, 'set_KeyValue'):
              self.set_KeyValue(obj_.value)
        elif nodeName_ == 'RetrievalMethod':
            obj_ = RetrievalMethodType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'RetrievalMethod', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_RetrievalMethod'):
              self.add_RetrievalMethod(obj_.value)
            elif hasattr(self, 'set_RetrievalMethod'):
              self.set_RetrievalMethod(obj_.value)
        elif nodeName_ == 'X509Data':
            obj_ = X509DataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'X509Data', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_X509Data'):
              self.add_X509Data(obj_.value)
            elif hasattr(self, 'set_X509Data'):
              self.set_X509Data(obj_.value)
        elif nodeName_ == 'PGPData':
            obj_ = PGPDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'PGPData', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_PGPData'):
              self.add_PGPData(obj_.value)
            elif hasattr(self, 'set_PGPData'):
              self.set_PGPData(obj_.value)
        elif nodeName_ == 'SPKIData':
            obj_ = SPKIDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'SPKIData', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_SPKIData'):
              self.add_SPKIData(obj_.value)
            elif hasattr(self, 'set_SPKIData'):
              self.set_SPKIData(obj_.value)
        elif nodeName_ == 'MgmtData' and child_.text is not None:
            valuestr_ = child_.text
            valuestr_ = self.gds_parse_string(valuestr_, node, 'MgmtData')
            valuestr_ = self.gds_validate_string(valuestr_, node, 'MgmtData')
            obj_ = self.mixedclass_(MixedContainer.CategorySimple,
                MixedContainer.TypeString, 'MgmtData', valuestr_)
            self.content_.append(obj_)
            self.MgmtData_nsprefix_ = child_.prefix
        elif nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class KeyInfoType


class KeyValueType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, DSAKeyValue=None, RSAKeyValue=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.DSAKeyValue = DSAKeyValue
        self.DSAKeyValue_nsprefix_ = "ds"
        self.RSAKeyValue = RSAKeyValue
        self.RSAKeyValue_nsprefix_ = "ds"
        self.anytypeobjs_ = anytypeobjs_
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, KeyValueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if KeyValueType.subclass:
            return KeyValueType.subclass(*args_, **kwargs_)
        else:
            return KeyValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_DSAKeyValue(self):
        return self.DSAKeyValue
    def set_DSAKeyValue(self, DSAKeyValue):
        self.DSAKeyValue = DSAKeyValue
    def get_RSAKeyValue(self):
        return self.RSAKeyValue
    def set_RSAKeyValue(self, RSAKeyValue):
        self.RSAKeyValue = RSAKeyValue
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            self.DSAKeyValue is not None or
            self.RSAKeyValue is not None or
            self.anytypeobjs_ is not None or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#"  xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='KeyValueType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('KeyValueType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'KeyValueType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='KeyValueType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='KeyValueType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='KeyValueType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#"  xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='KeyValueType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.DSAKeyValue is not None:
            namespaceprefix_ = self.DSAKeyValue_nsprefix_ + ':' if (UseCapturedNS_ and self.DSAKeyValue_nsprefix_) else ''
            self.DSAKeyValue.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='DSAKeyValue', pretty_print=pretty_print)
        if self.RSAKeyValue is not None:
            namespaceprefix_ = self.RSAKeyValue_nsprefix_ + ':' if (UseCapturedNS_ and self.RSAKeyValue_nsprefix_) else ''
            self.RSAKeyValue.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='RSAKeyValue', pretty_print=pretty_print)
        if not fromsubclass_:
            if self.anytypeobjs_ is not None:
                content_ = self.anytypeobjs_
                outfile.write(content_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'DSAKeyValue':
            obj_ = DSAKeyValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'DSAKeyValue', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_DSAKeyValue'):
              self.add_DSAKeyValue(obj_.value)
            elif hasattr(self, 'set_DSAKeyValue'):
              self.set_DSAKeyValue(obj_.value)
        elif nodeName_ == 'RSAKeyValue':
            obj_ = RSAKeyValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'RSAKeyValue', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_RSAKeyValue'):
              self.add_RSAKeyValue(obj_.value)
            elif hasattr(self, 'set_RSAKeyValue'):
              self.set_RSAKeyValue(obj_.value)
        elif nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class KeyValueType


class RetrievalMethodType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, URI=None, Type=None, Transforms=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ds"
        self.URI = _cast(None, URI)
        self.URI_nsprefix_ = None
        self.Type = _cast(None, Type)
        self.Type_nsprefix_ = None
        self.Transforms = Transforms
        self.Transforms_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RetrievalMethodType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RetrievalMethodType.subclass:
            return RetrievalMethodType.subclass(*args_, **kwargs_)
        else:
            return RetrievalMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Transforms(self):
        return self.Transforms
    def set_Transforms(self, Transforms):
        self.Transforms = Transforms
    def get_URI(self):
        return self.URI
    def set_URI(self, URI):
        self.URI = URI
    def get_Type(self):
        return self.Type
    def set_Type(self, Type):
        self.Type = Type
    def _hasContent(self):
        if (
            self.Transforms is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#" ', name_='RetrievalMethodType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RetrievalMethodType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RetrievalMethodType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RetrievalMethodType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RetrievalMethodType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='RetrievalMethodType'):
        if self.URI is not None and 'URI' not in already_processed:
            already_processed.add('URI')
            outfile.write(' URI=%s' % (quote_attrib(self.URI), ))
        if self.Type is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            outfile.write(' Type=%s' % (quote_attrib(self.Type), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#" ', name_='RetrievalMethodType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Transforms is not None:
            namespaceprefix_ = self.Transforms_nsprefix_ + ':' if (UseCapturedNS_ and self.Transforms_nsprefix_) else ''
            self.Transforms.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Transforms', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('URI', node)
        if value is not None and 'URI' not in already_processed:
            already_processed.add('URI')
            self.URI = value
        value = find_attr_value_('Type', node)
        if value is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            self.Type = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Transforms':
            obj_ = TransformsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Transforms = obj_
            obj_.original_tagname_ = 'Transforms'
# end class RetrievalMethodType


class X509DataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, X509IssuerSerial=None, X509SKI=None, X509SubjectName=None, X509Certificate=None, X509CRL=None, anytypeobjs_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if X509IssuerSerial is None:
            self.X509IssuerSerial = []
        else:
            self.X509IssuerSerial = X509IssuerSerial
        self.X509IssuerSerial_nsprefix_ = "ds"
        if X509SKI is None:
            self.X509SKI = []
        else:
            self.X509SKI = X509SKI
        self.X509SKI_nsprefix_ = None
        if X509SubjectName is None:
            self.X509SubjectName = []
        else:
            self.X509SubjectName = X509SubjectName
        self.X509SubjectName_nsprefix_ = None
        if X509Certificate is None:
            self.X509Certificate = []
        else:
            self.X509Certificate = X509Certificate
        self.X509Certificate_nsprefix_ = None
        if X509CRL is None:
            self.X509CRL = []
        else:
            self.X509CRL = X509CRL
        self.X509CRL_nsprefix_ = None
        self.anytypeobjs_ = anytypeobjs_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, X509DataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if X509DataType.subclass:
            return X509DataType.subclass(*args_, **kwargs_)
        else:
            return X509DataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_X509IssuerSerial(self):
        return self.X509IssuerSerial
    def set_X509IssuerSerial(self, X509IssuerSerial):
        self.X509IssuerSerial = X509IssuerSerial
    def add_X509IssuerSerial(self, value):
        self.X509IssuerSerial.append(value)
    def insert_X509IssuerSerial_at(self, index, value):
        self.X509IssuerSerial.insert(index, value)
    def replace_X509IssuerSerial_at(self, index, value):
        self.X509IssuerSerial[index] = value
    def get_X509SKI(self):
        return self.X509SKI
    def set_X509SKI(self, X509SKI):
        self.X509SKI = X509SKI
    def add_X509SKI(self, value):
        self.X509SKI.append(value)
    def insert_X509SKI_at(self, index, value):
        self.X509SKI.insert(index, value)
    def replace_X509SKI_at(self, index, value):
        self.X509SKI[index] = value
    def get_X509SubjectName(self):
        return self.X509SubjectName
    def set_X509SubjectName(self, X509SubjectName):
        self.X509SubjectName = X509SubjectName
    def add_X509SubjectName(self, value):
        self.X509SubjectName.append(value)
    def insert_X509SubjectName_at(self, index, value):
        self.X509SubjectName.insert(index, value)
    def replace_X509SubjectName_at(self, index, value):
        self.X509SubjectName[index] = value
    def get_X509Certificate(self):
        return self.X509Certificate
    def set_X509Certificate(self, X509Certificate):
        self.X509Certificate = X509Certificate
    def add_X509Certificate(self, value):
        self.X509Certificate.append(value)
    def insert_X509Certificate_at(self, index, value):
        self.X509Certificate.insert(index, value)
    def replace_X509Certificate_at(self, index, value):
        self.X509Certificate[index] = value
    def get_X509CRL(self):
        return self.X509CRL
    def set_X509CRL(self, X509CRL):
        self.X509CRL = X509CRL
    def add_X509CRL(self, value):
        self.X509CRL.append(value)
    def insert_X509CRL_at(self, index, value):
        self.X509CRL.insert(index, value)
    def replace_X509CRL_at(self, index, value):
        self.X509CRL[index] = value
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def _hasContent(self):
        if (
            self.X509IssuerSerial or
            self.X509SKI or
            self.X509SubjectName or
            self.X509Certificate or
            self.X509CRL or
            self.anytypeobjs_ is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#"  xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='X509DataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('X509DataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'X509DataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='X509DataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='X509DataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='X509DataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#"  xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='X509DataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for X509IssuerSerial_ in self.X509IssuerSerial:
            namespaceprefix_ = self.X509IssuerSerial_nsprefix_ + ':' if (UseCapturedNS_ and self.X509IssuerSerial_nsprefix_) else ''
            X509IssuerSerial_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='X509IssuerSerial', pretty_print=pretty_print)
        for X509SKI_ in self.X509SKI:
            namespaceprefix_ = self.X509SKI_nsprefix_ + ':' if (UseCapturedNS_ and self.X509SKI_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sX509SKI>%s</%sX509SKI>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(X509SKI_), input_name='X509SKI')), namespaceprefix_ , eol_))
        for X509SubjectName_ in self.X509SubjectName:
            namespaceprefix_ = self.X509SubjectName_nsprefix_ + ':' if (UseCapturedNS_ and self.X509SubjectName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sX509SubjectName>%s</%sX509SubjectName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(X509SubjectName_), input_name='X509SubjectName')), namespaceprefix_ , eol_))
        for X509Certificate_ in self.X509Certificate:
            namespaceprefix_ = self.X509Certificate_nsprefix_ + ':' if (UseCapturedNS_ and self.X509Certificate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sX509Certificate>%s</%sX509Certificate>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(X509Certificate_), input_name='X509Certificate')), namespaceprefix_ , eol_))
        for X509CRL_ in self.X509CRL:
            namespaceprefix_ = self.X509CRL_nsprefix_ + ':' if (UseCapturedNS_ and self.X509CRL_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sX509CRL>%s</%sX509CRL>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(X509CRL_), input_name='X509CRL')), namespaceprefix_ , eol_))
        if not fromsubclass_:
            if self.anytypeobjs_ is not None:
                content_ = self.anytypeobjs_
                outfile.write(content_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'X509IssuerSerial':
            obj_ = X509IssuerSerialType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.X509IssuerSerial.append(obj_)
            obj_.original_tagname_ = 'X509IssuerSerial'
        elif nodeName_ == 'X509SKI':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'X509SKI')
            value_ = self.gds_validate_string(value_, node, 'X509SKI')
            self.X509SKI.append(value_)
            self.X509SKI_nsprefix_ = child_.prefix
        elif nodeName_ == 'X509SubjectName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'X509SubjectName')
            value_ = self.gds_validate_string(value_, node, 'X509SubjectName')
            self.X509SubjectName.append(value_)
            self.X509SubjectName_nsprefix_ = child_.prefix
        elif nodeName_ == 'X509Certificate':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'X509Certificate')
            value_ = self.gds_validate_string(value_, node, 'X509Certificate')
            self.X509Certificate.append(value_)
            self.X509Certificate_nsprefix_ = child_.prefix
        elif nodeName_ == 'X509CRL':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'X509CRL')
            value_ = self.gds_validate_string(value_, node, 'X509CRL')
            self.X509CRL.append(value_)
            self.X509CRL_nsprefix_ = child_.prefix
        else:
            content_ = self.gds_build_any(child_, 'X509DataType')
            self.set_anytypeobjs_(content_)
# end class X509DataType


class X509IssuerSerialType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, X509IssuerName=None, X509SerialNumber=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.X509IssuerName = X509IssuerName
        self.X509IssuerName_nsprefix_ = None
        self.X509SerialNumber = X509SerialNumber
        self.X509SerialNumber_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, X509IssuerSerialType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if X509IssuerSerialType.subclass:
            return X509IssuerSerialType.subclass(*args_, **kwargs_)
        else:
            return X509IssuerSerialType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_X509IssuerName(self):
        return self.X509IssuerName
    def set_X509IssuerName(self, X509IssuerName):
        self.X509IssuerName = X509IssuerName
    def get_X509SerialNumber(self):
        return self.X509SerialNumber
    def set_X509SerialNumber(self, X509SerialNumber):
        self.X509SerialNumber = X509SerialNumber
    def _hasContent(self):
        if (
            self.X509IssuerName is not None or
            self.X509SerialNumber is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody"  xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='X509IssuerSerialType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('X509IssuerSerialType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'X509IssuerSerialType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='X509IssuerSerialType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='X509IssuerSerialType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='X509IssuerSerialType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody"  xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='X509IssuerSerialType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.X509IssuerName is not None:
            namespaceprefix_ = self.X509IssuerName_nsprefix_ + ':' if (UseCapturedNS_ and self.X509IssuerName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sX509IssuerName>%s</%sX509IssuerName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.X509IssuerName), input_name='X509IssuerName')), namespaceprefix_ , eol_))
        if self.X509SerialNumber is not None:
            namespaceprefix_ = self.X509SerialNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.X509SerialNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sX509SerialNumber>%s</%sX509SerialNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.X509SerialNumber), input_name='X509SerialNumber')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'X509IssuerName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'X509IssuerName')
            value_ = self.gds_validate_string(value_, node, 'X509IssuerName')
            self.X509IssuerName = value_
            self.X509IssuerName_nsprefix_ = child_.prefix
        elif nodeName_ == 'X509SerialNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'X509SerialNumber')
            value_ = self.gds_validate_string(value_, node, 'X509SerialNumber')
            self.X509SerialNumber = value_
            self.X509SerialNumber_nsprefix_ = child_.prefix
# end class X509IssuerSerialType


class PGPDataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, PGPKeyID=None, PGPKeyPacket=None, anytypeobjs_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.PGPKeyID = PGPKeyID
        self.PGPKeyID_nsprefix_ = None
        self.PGPKeyPacket = PGPKeyPacket
        self.PGPKeyPacket_nsprefix_ = None
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PGPDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PGPDataType.subclass:
            return PGPDataType.subclass(*args_, **kwargs_)
        else:
            return PGPDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_PGPKeyID(self):
        return self.PGPKeyID
    def set_PGPKeyID(self, PGPKeyID):
        self.PGPKeyID = PGPKeyID
    def get_PGPKeyPacket(self):
        return self.PGPKeyPacket
    def set_PGPKeyPacket(self, PGPKeyPacket):
        self.PGPKeyPacket = PGPKeyPacket
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def add_anytypeobjs_(self, value): self.anytypeobjs_.append(value)
    def insert_anytypeobjs_(self, index, value): self._anytypeobjs_[index] = value
    def _hasContent(self):
        if (
            self.PGPKeyID is not None or
            self.PGPKeyPacket is not None or
            self.anytypeobjs_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody"  xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='PGPDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PGPDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PGPDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PGPDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PGPDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='PGPDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody"  xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='PGPDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.PGPKeyID is not None:
            namespaceprefix_ = self.PGPKeyID_nsprefix_ + ':' if (UseCapturedNS_ and self.PGPKeyID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPGPKeyID>%s</%sPGPKeyID>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PGPKeyID), input_name='PGPKeyID')), namespaceprefix_ , eol_))
        if self.PGPKeyPacket is not None:
            namespaceprefix_ = self.PGPKeyPacket_nsprefix_ + ':' if (UseCapturedNS_ and self.PGPKeyPacket_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPGPKeyPacket>%s</%sPGPKeyPacket>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PGPKeyPacket), input_name='PGPKeyPacket')), namespaceprefix_ , eol_))
        if not fromsubclass_:
            for obj_ in self.anytypeobjs_:
                showIndent(outfile, level, pretty_print)
                outfile.write(obj_)
                outfile.write('\n')
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'PGPKeyID':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PGPKeyID')
            value_ = self.gds_validate_string(value_, node, 'PGPKeyID')
            self.PGPKeyID = value_
            self.PGPKeyID_nsprefix_ = child_.prefix
        elif nodeName_ == 'PGPKeyPacket':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PGPKeyPacket')
            value_ = self.gds_validate_string(value_, node, 'PGPKeyPacket')
            self.PGPKeyPacket = value_
            self.PGPKeyPacket_nsprefix_ = child_.prefix
        else:
            content_ = self.gds_build_any(child_, 'PGPDataType')
            self.anytypeobjs_.append(content_)
# end class PGPDataType


class SPKIDataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, SPKISexp=None, anytypeobjs_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if SPKISexp is None:
            self.SPKISexp = []
        else:
            self.SPKISexp = SPKISexp
        self.SPKISexp_nsprefix_ = None
        self.anytypeobjs_ = anytypeobjs_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SPKIDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SPKIDataType.subclass:
            return SPKIDataType.subclass(*args_, **kwargs_)
        else:
            return SPKIDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_SPKISexp(self):
        return self.SPKISexp
    def set_SPKISexp(self, SPKISexp):
        self.SPKISexp = SPKISexp
    def add_SPKISexp(self, value):
        self.SPKISexp.append(value)
    def insert_SPKISexp_at(self, index, value):
        self.SPKISexp.insert(index, value)
    def replace_SPKISexp_at(self, index, value):
        self.SPKISexp[index] = value
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def _hasContent(self):
        if (
            self.SPKISexp or
            self.anytypeobjs_ is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody"  xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='SPKIDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SPKIDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SPKIDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SPKIDataType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SPKIDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SPKIDataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody"  xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='SPKIDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for SPKISexp_ in self.SPKISexp:
            namespaceprefix_ = self.SPKISexp_nsprefix_ + ':' if (UseCapturedNS_ and self.SPKISexp_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSPKISexp>%s</%sSPKISexp>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(SPKISexp_), input_name='SPKISexp')), namespaceprefix_ , eol_))
        if not fromsubclass_:
            if self.anytypeobjs_ is not None:
                content_ = self.anytypeobjs_
                outfile.write(content_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'SPKISexp':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SPKISexp')
            value_ = self.gds_validate_string(value_, node, 'SPKISexp')
            self.SPKISexp.append(value_)
            self.SPKISexp_nsprefix_ = child_.prefix
        else:
            content_ = self.gds_build_any(child_, 'SPKIDataType')
            self.set_anytypeobjs_(content_)
# end class SPKIDataType


class ObjectType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Id=None, MimeType=None, Encoding=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.MimeType = _cast(None, MimeType)
        self.MimeType_nsprefix_ = None
        self.Encoding = _cast(None, Encoding)
        self.Encoding_nsprefix_ = None
        self.anytypeobjs_ = anytypeobjs_
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ObjectType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ObjectType.subclass:
            return ObjectType.subclass(*args_, **kwargs_)
        else:
            return ObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def get_MimeType(self):
        return self.MimeType
    def set_MimeType(self, MimeType):
        self.MimeType = MimeType
    def get_Encoding(self):
        return self.Encoding
    def set_Encoding(self, Encoding):
        self.Encoding = Encoding
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            self.anytypeobjs_ is not None or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody"  xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='ObjectType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ObjectType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ObjectType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ObjectType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ObjectType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='ObjectType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
        if self.MimeType is not None and 'MimeType' not in already_processed:
            already_processed.add('MimeType')
            outfile.write(' MimeType=%s' % (quote_attrib(self.MimeType), ))
        if self.Encoding is not None and 'Encoding' not in already_processed:
            already_processed.add('Encoding')
            outfile.write(' Encoding=%s' % (quote_attrib(self.Encoding), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody"  xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='ObjectType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if not fromsubclass_:
            if self.anytypeobjs_ is not None:
                content_ = self.anytypeobjs_
                outfile.write(content_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
        value = find_attr_value_('MimeType', node)
        if value is not None and 'MimeType' not in already_processed:
            already_processed.add('MimeType')
            self.MimeType = value
        value = find_attr_value_('Encoding', node)
        if value is not None and 'Encoding' not in already_processed:
            already_processed.add('Encoding')
            self.Encoding = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class ObjectType


class ManifestType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Id=None, Reference=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ds"
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        if Reference is None:
            self.Reference = []
        else:
            self.Reference = Reference
        self.Reference_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ManifestType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ManifestType.subclass:
            return ManifestType.subclass(*args_, **kwargs_)
        else:
            return ManifestType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Reference(self):
        return self.Reference
    def set_Reference(self, Reference):
        self.Reference = Reference
    def add_Reference(self, value):
        self.Reference.append(value)
    def insert_Reference_at(self, index, value):
        self.Reference.insert(index, value)
    def replace_Reference_at(self, index, value):
        self.Reference[index] = value
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def _hasContent(self):
        if (
            self.Reference
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#" ', name_='ManifestType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ManifestType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ManifestType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ManifestType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ManifestType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='ManifestType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#" ', name_='ManifestType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Reference_ in self.Reference:
            namespaceprefix_ = self.Reference_nsprefix_ + ':' if (UseCapturedNS_ and self.Reference_nsprefix_) else ''
            Reference_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Reference', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Reference':
            obj_ = ReferenceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Reference.append(obj_)
            obj_.original_tagname_ = 'Reference'
# end class ManifestType


class SignaturePropertiesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Id=None, SignatureProperty=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ds"
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        if SignatureProperty is None:
            self.SignatureProperty = []
        else:
            self.SignatureProperty = SignatureProperty
        self.SignatureProperty_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignaturePropertiesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignaturePropertiesType.subclass:
            return SignaturePropertiesType.subclass(*args_, **kwargs_)
        else:
            return SignaturePropertiesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_SignatureProperty(self):
        return self.SignatureProperty
    def set_SignatureProperty(self, SignatureProperty):
        self.SignatureProperty = SignatureProperty
    def add_SignatureProperty(self, value):
        self.SignatureProperty.append(value)
    def insert_SignatureProperty_at(self, index, value):
        self.SignatureProperty.insert(index, value)
    def replace_SignatureProperty_at(self, index, value):
        self.SignatureProperty[index] = value
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def _hasContent(self):
        if (
            self.SignatureProperty
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#" ', name_='SignaturePropertiesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignaturePropertiesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignaturePropertiesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignaturePropertiesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignaturePropertiesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignaturePropertiesType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#" ', name_='SignaturePropertiesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for SignatureProperty_ in self.SignatureProperty:
            namespaceprefix_ = self.SignatureProperty_nsprefix_ + ':' if (UseCapturedNS_ and self.SignatureProperty_nsprefix_) else ''
            SignatureProperty_.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureProperty', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'SignatureProperty':
            obj_ = SignaturePropertyType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SignatureProperty.append(obj_)
            obj_.original_tagname_ = 'SignatureProperty'
# end class SignaturePropertiesType


class SignaturePropertyType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Target=None, Id=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Target = _cast(None, Target)
        self.Target_nsprefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.anytypeobjs_ = anytypeobjs_
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignaturePropertyType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignaturePropertyType.subclass:
            return SignaturePropertyType.subclass(*args_, **kwargs_)
        else:
            return SignaturePropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def get_Target(self):
        return self.Target
    def set_Target(self, Target):
        self.Target = Target
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            self.anytypeobjs_ is not None or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            self.content_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody"  xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='SignaturePropertyType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignaturePropertyType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignaturePropertyType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignaturePropertyType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignaturePropertyType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignaturePropertyType'):
        if self.Target is not None and 'Target' not in already_processed:
            already_processed.add('Target')
            outfile.write(' Target=%s' % (quote_attrib(self.Target), ))
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:None="urn:iso:15118:2:2013:MsgBody"  xmlns:ds="http://www.w3.org/2000/09/xmldsig#"', name_='SignaturePropertyType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if not fromsubclass_:
            if self.anytypeobjs_ is not None:
                content_ = self.anytypeobjs_
                outfile.write(content_)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Target', node)
        if value is not None and 'Target' not in already_processed:
            already_processed.add('Target')
            self.Target = value
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == '':
            obj_ = __ANY__.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, '', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_'):
              self.add_(obj_.value)
            elif hasattr(self, 'set_'):
              self.set_(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class SignaturePropertyType


class DSAKeyValueType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, P=None, Q=None, G=None, Y=None, J=None, Seed=None, PgenCounter=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ds"
        self.P = P
        self.validate_CryptoBinary(self.P)
        self.P_nsprefix_ = "ds"
        self.Q = Q
        self.validate_CryptoBinary(self.Q)
        self.Q_nsprefix_ = "ds"
        self.G = G
        self.validate_CryptoBinary(self.G)
        self.G_nsprefix_ = "ds"
        self.Y = Y
        self.validate_CryptoBinary(self.Y)
        self.Y_nsprefix_ = "ds"
        self.J = J
        self.validate_CryptoBinary(self.J)
        self.J_nsprefix_ = "ds"
        self.Seed = Seed
        self.validate_CryptoBinary(self.Seed)
        self.Seed_nsprefix_ = "ds"
        self.PgenCounter = PgenCounter
        self.validate_CryptoBinary(self.PgenCounter)
        self.PgenCounter_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DSAKeyValueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DSAKeyValueType.subclass:
            return DSAKeyValueType.subclass(*args_, **kwargs_)
        else:
            return DSAKeyValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_P(self):
        return self.P
    def set_P(self, P):
        self.P = P
    def get_Q(self):
        return self.Q
    def set_Q(self, Q):
        self.Q = Q
    def get_G(self):
        return self.G
    def set_G(self, G):
        self.G = G
    def get_Y(self):
        return self.Y
    def set_Y(self, Y):
        self.Y = Y
    def get_J(self):
        return self.J
    def set_J(self, J):
        self.J = J
    def get_Seed(self):
        return self.Seed
    def set_Seed(self, Seed):
        self.Seed = Seed
    def get_PgenCounter(self):
        return self.PgenCounter
    def set_PgenCounter(self, PgenCounter):
        self.PgenCounter = PgenCounter
    def validate_CryptoBinary(self, value):
        result = True
        # Validate type CryptoBinary, a restriction on base64Binary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            pass
        return result
    def _hasContent(self):
        if (
            self.P is not None or
            self.Q is not None or
            self.G is not None or
            self.Y is not None or
            self.J is not None or
            self.Seed is not None or
            self.PgenCounter is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#" ', name_='DSAKeyValueType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DSAKeyValueType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DSAKeyValueType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DSAKeyValueType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DSAKeyValueType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='DSAKeyValueType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#" ', name_='DSAKeyValueType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.P is not None:
            namespaceprefix_ = self.P_nsprefix_ + ':' if (UseCapturedNS_ and self.P_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sP>%s</%sP>%s' % (namespaceprefix_ , self.gds_format_base64(self.P, input_name='P'), namespaceprefix_ , eol_))
        if self.Q is not None:
            namespaceprefix_ = self.Q_nsprefix_ + ':' if (UseCapturedNS_ and self.Q_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sQ>%s</%sQ>%s' % (namespaceprefix_ , self.gds_format_base64(self.Q, input_name='Q'), namespaceprefix_ , eol_))
        if self.G is not None:
            namespaceprefix_ = self.G_nsprefix_ + ':' if (UseCapturedNS_ and self.G_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sG>%s</%sG>%s' % (namespaceprefix_ , self.gds_format_base64(self.G, input_name='G'), namespaceprefix_ , eol_))
        if self.Y is not None:
            namespaceprefix_ = self.Y_nsprefix_ + ':' if (UseCapturedNS_ and self.Y_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sY>%s</%sY>%s' % (namespaceprefix_ , self.gds_format_base64(self.Y, input_name='Y'), namespaceprefix_ , eol_))
        if self.J is not None:
            namespaceprefix_ = self.J_nsprefix_ + ':' if (UseCapturedNS_ and self.J_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sJ>%s</%sJ>%s' % (namespaceprefix_ , self.gds_format_base64(self.J, input_name='J'), namespaceprefix_ , eol_))
        if self.Seed is not None:
            namespaceprefix_ = self.Seed_nsprefix_ + ':' if (UseCapturedNS_ and self.Seed_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSeed>%s</%sSeed>%s' % (namespaceprefix_ , self.gds_format_base64(self.Seed, input_name='Seed'), namespaceprefix_ , eol_))
        if self.PgenCounter is not None:
            namespaceprefix_ = self.PgenCounter_nsprefix_ + ':' if (UseCapturedNS_ and self.PgenCounter_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPgenCounter>%s</%sPgenCounter>%s' % (namespaceprefix_ , self.gds_format_base64(self.PgenCounter, input_name='PgenCounter'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'P':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'P')
            else:
                bval_ = None
            self.P = bval_
            self.P_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.P)
        elif nodeName_ == 'Q':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Q')
            else:
                bval_ = None
            self.Q = bval_
            self.Q_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.Q)
        elif nodeName_ == 'G':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'G')
            else:
                bval_ = None
            self.G = bval_
            self.G_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.G)
        elif nodeName_ == 'Y':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Y')
            else:
                bval_ = None
            self.Y = bval_
            self.Y_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.Y)
        elif nodeName_ == 'J':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'J')
            else:
                bval_ = None
            self.J = bval_
            self.J_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.J)
        elif nodeName_ == 'Seed':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Seed')
            else:
                bval_ = None
            self.Seed = bval_
            self.Seed_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.Seed)
        elif nodeName_ == 'PgenCounter':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'PgenCounter')
            else:
                bval_ = None
            self.PgenCounter = bval_
            self.PgenCounter_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.PgenCounter)
# end class DSAKeyValueType


class RSAKeyValueType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Modulus=None, Exponent=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ds"
        self.Modulus = Modulus
        self.validate_CryptoBinary(self.Modulus)
        self.Modulus_nsprefix_ = "ds"
        self.Exponent = Exponent
        self.validate_CryptoBinary(self.Exponent)
        self.Exponent_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RSAKeyValueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RSAKeyValueType.subclass:
            return RSAKeyValueType.subclass(*args_, **kwargs_)
        else:
            return RSAKeyValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Modulus(self):
        return self.Modulus
    def set_Modulus(self, Modulus):
        self.Modulus = Modulus
    def get_Exponent(self):
        return self.Exponent
    def set_Exponent(self, Exponent):
        self.Exponent = Exponent
    def validate_CryptoBinary(self, value):
        result = True
        # Validate type CryptoBinary, a restriction on base64Binary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            pass
        return result
    def _hasContent(self):
        if (
            self.Modulus is not None or
            self.Exponent is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#" ', name_='RSAKeyValueType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RSAKeyValueType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RSAKeyValueType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RSAKeyValueType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RSAKeyValueType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='RSAKeyValueType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_=' xmlns:ds="http://www.w3.org/2000/09/xmldsig#" ', name_='RSAKeyValueType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Modulus is not None:
            namespaceprefix_ = self.Modulus_nsprefix_ + ':' if (UseCapturedNS_ and self.Modulus_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sModulus>%s</%sModulus>%s' % (namespaceprefix_ , self.gds_format_base64(self.Modulus, input_name='Modulus'), namespaceprefix_ , eol_))
        if self.Exponent is not None:
            namespaceprefix_ = self.Exponent_nsprefix_ + ':' if (UseCapturedNS_ and self.Exponent_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sExponent>%s</%sExponent>%s' % (namespaceprefix_ , self.gds_format_base64(self.Exponent, input_name='Exponent'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Modulus':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Modulus')
            else:
                bval_ = None
            self.Modulus = bval_
            self.Modulus_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.Modulus)
        elif nodeName_ == 'Exponent':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Exponent')
            else:
                bval_ = None
            self.Exponent = bval_
            self.Exponent_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.Exponent)
# end class RSAKeyValueType


class BodyType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, BodyElement=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.BodyElement = BodyElement
        self.BodyElement_nsprefix_ = "ns5"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, BodyType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if BodyType.subclass:
            return BodyType.subclass(*args_, **kwargs_)
        else:
            return BodyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_BodyElement(self):
        return self.BodyElement
    def set_BodyElement(self, BodyElement):
        self.BodyElement = BodyElement
    def _hasContent(self):
        if (
            self.BodyElement is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='BodyType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('BodyType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'BodyType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='BodyType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='BodyType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='BodyType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='BodyType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.BodyElement is not None:
            self.BodyElement.export(outfile, level, namespaceprefix_, namespacedef_='', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'BodyElement':
            type_name_ = child_.attrib.get(
                '{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()["" + type_name_]
                obj_ = class_.factory()
                obj_.build(child_, gds_collector_=gds_collector_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <BodyElement> element')
            self.BodyElement = obj_
            obj_.original_tagname_ = 'BodyElement'
        elif nodeName_ == 'SessionSetupReq':
            obj_ = SessionSetupReqType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'SessionSetupReq'
        elif nodeName_ == 'SessionSetupRes':
            obj_ = SessionSetupResType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'SessionSetupRes'
        elif nodeName_ == 'ServiceDiscoveryReq':
            obj_ = ServiceDiscoveryReqType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'ServiceDiscoveryReq'
        elif nodeName_ == 'ServiceDiscoveryRes':
            obj_ = ServiceDiscoveryResType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'ServiceDiscoveryRes'
        elif nodeName_ == 'ServiceDetailReq':
            obj_ = ServiceDetailReqType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'ServiceDetailReq'
        elif nodeName_ == 'ServiceDetailRes':
            obj_ = ServiceDetailResType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'ServiceDetailRes'
        elif nodeName_ == 'PaymentServiceSelectionReq':
            obj_ = PaymentServiceSelectionReqType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'PaymentServiceSelectionReq'
        elif nodeName_ == 'PaymentServiceSelectionRes':
            obj_ = PaymentServiceSelectionResType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'PaymentServiceSelectionRes'
        elif nodeName_ == 'PaymentDetailsReq':
            obj_ = PaymentDetailsReqType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'PaymentDetailsReq'
        elif nodeName_ == 'PaymentDetailsRes':
            obj_ = PaymentDetailsResType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'PaymentDetailsRes'
        elif nodeName_ == 'AuthorizationReq':
            obj_ = AuthorizationReqType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'AuthorizationReq'
        elif nodeName_ == 'AuthorizationRes':
            obj_ = AuthorizationResType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'AuthorizationRes'
        elif nodeName_ == 'ChargeParameterDiscoveryReq':
            obj_ = ChargeParameterDiscoveryReqType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'ChargeParameterDiscoveryReq'
        elif nodeName_ == 'ChargeParameterDiscoveryRes':
            obj_ = ChargeParameterDiscoveryResType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'ChargeParameterDiscoveryRes'
        elif nodeName_ == 'PowerDeliveryReq':
            obj_ = PowerDeliveryReqType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'PowerDeliveryReq'
        elif nodeName_ == 'PowerDeliveryRes':
            obj_ = PowerDeliveryResType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'PowerDeliveryRes'
        elif nodeName_ == 'MeteringReceiptReq':
            obj_ = MeteringReceiptReqType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'MeteringReceiptReq'
        elif nodeName_ == 'MeteringReceiptRes':
            obj_ = MeteringReceiptResType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'MeteringReceiptRes'
        elif nodeName_ == 'SessionStopReq':
            obj_ = SessionStopReqType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'SessionStopReq'
        elif nodeName_ == 'SessionStopRes':
            obj_ = SessionStopResType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'SessionStopRes'
        elif nodeName_ == 'CertificateUpdateReq':
            obj_ = CertificateUpdateReqType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'CertificateUpdateReq'
        elif nodeName_ == 'CertificateUpdateRes':
            obj_ = CertificateUpdateResType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'CertificateUpdateRes'
        elif nodeName_ == 'CertificateInstallationReq':
            obj_ = CertificateInstallationReqType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'CertificateInstallationReq'
        elif nodeName_ == 'CertificateInstallationRes':
            obj_ = CertificateInstallationResType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'CertificateInstallationRes'
        elif nodeName_ == 'ChargingStatusReq':
            obj_ = ChargingStatusReqType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'ChargingStatusReq'
        elif nodeName_ == 'ChargingStatusRes':
            obj_ = ChargingStatusResType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'ChargingStatusRes'
        elif nodeName_ == 'CableCheckReq':
            obj_ = CableCheckReqType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'CableCheckReq'
        elif nodeName_ == 'CableCheckRes':
            obj_ = CableCheckResType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'CableCheckRes'
        elif nodeName_ == 'PreChargeReq':
            obj_ = PreChargeReqType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'PreChargeReq'
        elif nodeName_ == 'PreChargeRes':
            obj_ = PreChargeResType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'PreChargeRes'
        elif nodeName_ == 'CurrentDemandReq':
            obj_ = CurrentDemandReqType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'CurrentDemandReq'
        elif nodeName_ == 'CurrentDemandRes':
            obj_ = CurrentDemandResType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'CurrentDemandRes'
        elif nodeName_ == 'WeldingDetectionReq':
            obj_ = WeldingDetectionReqType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'WeldingDetectionReq'
        elif nodeName_ == 'WeldingDetectionRes':
            obj_ = WeldingDetectionResType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BodyElement = obj_
            obj_.original_tagname_ = 'WeldingDetectionRes'
# end class BodyType


class BodyBaseType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, BodyBaseType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if BodyBaseType.subclass:
            return BodyBaseType.subclass(*args_, **kwargs_)
        else:
            return BodyBaseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody"', name_='BodyBaseType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('BodyBaseType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'BodyBaseType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='BodyBaseType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='BodyBaseType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='BodyBaseType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody"', name_='BodyBaseType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class BodyBaseType


class SessionSetupReqType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, EVCCID=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("SessionSetupReqType"), self).__init__( **kwargs_)
        self.EVCCID = EVCCID
        self.validate_evccIDType(self.EVCCID)
        self.EVCCID_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SessionSetupReqType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SessionSetupReqType.subclass:
            return SessionSetupReqType.subclass(*args_, **kwargs_)
        else:
            return SessionSetupReqType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_EVCCID(self):
        return self.EVCCID
    def set_EVCCID(self, EVCCID):
        self.EVCCID = EVCCID
    def validate_evccIDType(self, value):
        result = True
        # Validate type evccIDType, a restriction on xs:hexBinary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on evccIDType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.EVCCID is not None or
            super(SessionSetupReqType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='SessionSetupReqType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SessionSetupReqType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SessionSetupReqType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SessionSetupReqType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SessionSetupReqType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SessionSetupReqType'):
        super(SessionSetupReqType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SessionSetupReqType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='SessionSetupReqType', fromsubclass_=False, pretty_print=True):
        super(SessionSetupReqType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.EVCCID is not None:
            namespaceprefix_ = self.EVCCID_nsprefix_ + ':' if (UseCapturedNS_ and self.EVCCID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEVCCID>%s</%sEVCCID>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.EVCCID), input_name='EVCCID')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(SessionSetupReqType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'EVCCID':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'EVCCID')
            value_ = self.gds_validate_string(value_, node, 'EVCCID')
            self.EVCCID = value_
            self.EVCCID_nsprefix_ = child_.prefix
            # validate type evccIDType
            self.validate_evccIDType(self.EVCCID)
        super(SessionSetupReqType, self)._buildChildren(child_, node, nodeName_, True)
# end class SessionSetupReqType


class SessionSetupResType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, ResponseCode=None, EVSEID=None, EVSETimeStamp=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("SessionSetupResType"), self).__init__( **kwargs_)
        self.ResponseCode = ResponseCode
        self.validate_responseCodeType(self.ResponseCode)
        self.ResponseCode_nsprefix_ = "ns6"
        self.EVSEID = EVSEID
        self.validate_evseIDType(self.EVSEID)
        self.EVSEID_nsprefix_ = "ns6"
        self.EVSETimeStamp = EVSETimeStamp
        self.EVSETimeStamp_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SessionSetupResType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SessionSetupResType.subclass:
            return SessionSetupResType.subclass(*args_, **kwargs_)
        else:
            return SessionSetupResType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ResponseCode(self):
        return self.ResponseCode
    def set_ResponseCode(self, ResponseCode):
        self.ResponseCode = ResponseCode
    def get_EVSEID(self):
        return self.EVSEID
    def set_EVSEID(self, EVSEID):
        self.EVSEID = EVSEID
    def get_EVSETimeStamp(self):
        return self.EVSETimeStamp
    def set_EVSETimeStamp(self, EVSETimeStamp):
        self.EVSETimeStamp = EVSETimeStamp
    def validate_responseCodeType(self, value):
        result = True
        # Validate type responseCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['OK', 'OK_NewSessionEstablished', 'OK_OldSessionJoined', 'OK_CertificateExpiresSoon', 'FAILED', 'FAILED_SequenceError', 'FAILED_ServiceIDInvalid', 'FAILED_UnknownSession', 'FAILED_ServiceSelectionInvalid', 'FAILED_PaymentSelectionInvalid', 'FAILED_CertificateExpired', 'FAILED_SignatureError', 'FAILED_NoCertificateAvailable', 'FAILED_CertChainError', 'FAILED_ChallengeInvalid', 'FAILED_ContractCanceled', 'FAILED_WrongChargeParameter', 'FAILED_PowerDeliveryNotApplied', 'FAILED_TariffSelectionInvalid', 'FAILED_ChargingProfileInvalid', 'FAILED_MeteringSignatureNotValid', 'FAILED_NoChargeServiceSelected', 'FAILED_WrongEnergyTransferMode', 'FAILED_ContactorError', 'FAILED_CertificateNotAllowedAtThisEVSE', 'FAILED_CertificateRevoked']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on responseCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_evseIDType(self, value):
        result = True
        # Validate type evseIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 37:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on evseIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on evseIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.ResponseCode is not None or
            self.EVSEID is not None or
            self.EVSETimeStamp is not None or
            super(SessionSetupResType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes"  xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='SessionSetupResType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SessionSetupResType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SessionSetupResType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SessionSetupResType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SessionSetupResType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SessionSetupResType'):
        super(SessionSetupResType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SessionSetupResType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes"  xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='SessionSetupResType', fromsubclass_=False, pretty_print=True):
        super(SessionSetupResType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ResponseCode is not None:
            namespaceprefix_ = self.ResponseCode_nsprefix_ + ':' if (UseCapturedNS_ and self.ResponseCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sResponseCode>%s</%sResponseCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ResponseCode), input_name='ResponseCode')), namespaceprefix_ , eol_))
        if self.EVSEID is not None:
            namespaceprefix_ = self.EVSEID_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEVSEID>%s</%sEVSEID>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.EVSEID), input_name='EVSEID')), namespaceprefix_ , eol_))
        if self.EVSETimeStamp is not None:
            namespaceprefix_ = self.EVSETimeStamp_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSETimeStamp_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEVSETimeStamp>%s</%sEVSETimeStamp>%s' % (namespaceprefix_ , self.gds_format_integer(self.EVSETimeStamp, input_name='EVSETimeStamp'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(SessionSetupResType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ResponseCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ResponseCode')
            value_ = self.gds_validate_string(value_, node, 'ResponseCode')
            self.ResponseCode = value_
            self.ResponseCode_nsprefix_ = child_.prefix
            # validate type responseCodeType
            self.validate_responseCodeType(self.ResponseCode)
        elif nodeName_ == 'EVSEID':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'EVSEID')
            value_ = self.gds_validate_string(value_, node, 'EVSEID')
            self.EVSEID = value_
            self.EVSEID_nsprefix_ = child_.prefix
            # validate type evseIDType
            self.validate_evseIDType(self.EVSEID)
        elif nodeName_ == 'EVSETimeStamp' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'EVSETimeStamp')
            ival_ = self.gds_validate_integer(ival_, node, 'EVSETimeStamp')
            self.EVSETimeStamp = ival_
            self.EVSETimeStamp_nsprefix_ = child_.prefix
        super(SessionSetupResType, self)._buildChildren(child_, node, nodeName_, True)
# end class SessionSetupResType


class ServiceDiscoveryReqType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, ServiceScope=None, ServiceCategory=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("ServiceDiscoveryReqType"), self).__init__( **kwargs_)
        self.ServiceScope = ServiceScope
        self.validate_serviceScopeType(self.ServiceScope)
        self.ServiceScope_nsprefix_ = "ns6"
        self.ServiceCategory = ServiceCategory
        self.validate_serviceCategoryType(self.ServiceCategory)
        self.ServiceCategory_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ServiceDiscoveryReqType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ServiceDiscoveryReqType.subclass:
            return ServiceDiscoveryReqType.subclass(*args_, **kwargs_)
        else:
            return ServiceDiscoveryReqType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ServiceScope(self):
        return self.ServiceScope
    def set_ServiceScope(self, ServiceScope):
        self.ServiceScope = ServiceScope
    def get_ServiceCategory(self):
        return self.ServiceCategory
    def set_ServiceCategory(self, ServiceCategory):
        self.ServiceCategory = ServiceCategory
    def validate_serviceScopeType(self, value):
        result = True
        # Validate type serviceScopeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 64:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on serviceScopeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_serviceCategoryType(self, value):
        result = True
        # Validate type serviceCategoryType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['EVCharging', 'Internet', 'ContractCertificate', 'OtherCustom']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on serviceCategoryType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.ServiceScope is not None or
            self.ServiceCategory is not None or
            super(ServiceDiscoveryReqType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='ServiceDiscoveryReqType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ServiceDiscoveryReqType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ServiceDiscoveryReqType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ServiceDiscoveryReqType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ServiceDiscoveryReqType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ServiceDiscoveryReqType'):
        super(ServiceDiscoveryReqType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ServiceDiscoveryReqType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='ServiceDiscoveryReqType', fromsubclass_=False, pretty_print=True):
        super(ServiceDiscoveryReqType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ServiceScope is not None:
            namespaceprefix_ = self.ServiceScope_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceScope_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sServiceScope>%s</%sServiceScope>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ServiceScope), input_name='ServiceScope')), namespaceprefix_ , eol_))
        if self.ServiceCategory is not None:
            namespaceprefix_ = self.ServiceCategory_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceCategory_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sServiceCategory>%s</%sServiceCategory>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ServiceCategory), input_name='ServiceCategory')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(ServiceDiscoveryReqType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ServiceScope':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ServiceScope')
            value_ = self.gds_validate_string(value_, node, 'ServiceScope')
            self.ServiceScope = value_
            self.ServiceScope_nsprefix_ = child_.prefix
            # validate type serviceScopeType
            self.validate_serviceScopeType(self.ServiceScope)
        elif nodeName_ == 'ServiceCategory':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ServiceCategory')
            value_ = self.gds_validate_string(value_, node, 'ServiceCategory')
            self.ServiceCategory = value_
            self.ServiceCategory_nsprefix_ = child_.prefix
            # validate type serviceCategoryType
            self.validate_serviceCategoryType(self.ServiceCategory)
        super(ServiceDiscoveryReqType, self)._buildChildren(child_, node, nodeName_, True)
# end class ServiceDiscoveryReqType


class ServiceDiscoveryResType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, ResponseCode=None, PaymentOptionList=None, ChargeService=None, ServiceList=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("ServiceDiscoveryResType"), self).__init__( **kwargs_)
        self.ResponseCode = ResponseCode
        self.validate_responseCodeType(self.ResponseCode)
        self.ResponseCode_nsprefix_ = "ns6"
        self.PaymentOptionList = PaymentOptionList
        self.PaymentOptionList_nsprefix_ = "ns6"
        self.ChargeService = ChargeService
        self.ChargeService_nsprefix_ = "ns6"
        self.ServiceList = ServiceList
        self.ServiceList_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ServiceDiscoveryResType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ServiceDiscoveryResType.subclass:
            return ServiceDiscoveryResType.subclass(*args_, **kwargs_)
        else:
            return ServiceDiscoveryResType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ResponseCode(self):
        return self.ResponseCode
    def set_ResponseCode(self, ResponseCode):
        self.ResponseCode = ResponseCode
    def get_PaymentOptionList(self):
        return self.PaymentOptionList
    def set_PaymentOptionList(self, PaymentOptionList):
        self.PaymentOptionList = PaymentOptionList
    def get_ChargeService(self):
        return self.ChargeService
    def set_ChargeService(self, ChargeService):
        self.ChargeService = ChargeService
    def get_ServiceList(self):
        return self.ServiceList
    def set_ServiceList(self, ServiceList):
        self.ServiceList = ServiceList
    def validate_responseCodeType(self, value):
        result = True
        # Validate type responseCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['OK', 'OK_NewSessionEstablished', 'OK_OldSessionJoined', 'OK_CertificateExpiresSoon', 'FAILED', 'FAILED_SequenceError', 'FAILED_ServiceIDInvalid', 'FAILED_UnknownSession', 'FAILED_ServiceSelectionInvalid', 'FAILED_PaymentSelectionInvalid', 'FAILED_CertificateExpired', 'FAILED_SignatureError', 'FAILED_NoCertificateAvailable', 'FAILED_CertChainError', 'FAILED_ChallengeInvalid', 'FAILED_ContractCanceled', 'FAILED_WrongChargeParameter', 'FAILED_PowerDeliveryNotApplied', 'FAILED_TariffSelectionInvalid', 'FAILED_ChargingProfileInvalid', 'FAILED_MeteringSignatureNotValid', 'FAILED_NoChargeServiceSelected', 'FAILED_WrongEnergyTransferMode', 'FAILED_ContactorError', 'FAILED_CertificateNotAllowedAtThisEVSE', 'FAILED_CertificateRevoked']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on responseCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.ResponseCode is not None or
            self.PaymentOptionList is not None or
            self.ChargeService is not None or
            self.ServiceList is not None or
            super(ServiceDiscoveryResType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='ServiceDiscoveryResType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ServiceDiscoveryResType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ServiceDiscoveryResType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ServiceDiscoveryResType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ServiceDiscoveryResType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ServiceDiscoveryResType'):
        super(ServiceDiscoveryResType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ServiceDiscoveryResType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='ServiceDiscoveryResType', fromsubclass_=False, pretty_print=True):
        super(ServiceDiscoveryResType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ResponseCode is not None:
            namespaceprefix_ = self.ResponseCode_nsprefix_ + ':' if (UseCapturedNS_ and self.ResponseCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sResponseCode>%s</%sResponseCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ResponseCode), input_name='ResponseCode')), namespaceprefix_ , eol_))
        if self.PaymentOptionList is not None:
            namespaceprefix_ = self.PaymentOptionList_nsprefix_ + ':' if (UseCapturedNS_ and self.PaymentOptionList_nsprefix_) else ''
            self.PaymentOptionList.export(outfile, level, namespaceprefix_, namespacedef_='', name_='PaymentOptionList', pretty_print=pretty_print)
        if self.ChargeService is not None:
            namespaceprefix_ = self.ChargeService_nsprefix_ + ':' if (UseCapturedNS_ and self.ChargeService_nsprefix_) else ''
            self.ChargeService.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ChargeService', pretty_print=pretty_print)
        if self.ServiceList is not None:
            namespaceprefix_ = self.ServiceList_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceList_nsprefix_) else ''
            self.ServiceList.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ServiceList', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(ServiceDiscoveryResType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ResponseCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ResponseCode')
            value_ = self.gds_validate_string(value_, node, 'ResponseCode')
            self.ResponseCode = value_
            self.ResponseCode_nsprefix_ = child_.prefix
            # validate type responseCodeType
            self.validate_responseCodeType(self.ResponseCode)
        elif nodeName_ == 'PaymentOptionList':
            obj_ = PaymentOptionListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.PaymentOptionList = obj_
            obj_.original_tagname_ = 'PaymentOptionList'
        elif nodeName_ == 'ChargeService':
            obj_ = ChargeServiceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ChargeService = obj_
            obj_.original_tagname_ = 'ChargeService'
        elif nodeName_ == 'ServiceList':
            obj_ = ServiceListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ServiceList = obj_
            obj_.original_tagname_ = 'ServiceList'
        super(ServiceDiscoveryResType, self)._buildChildren(child_, node, nodeName_, True)
# end class ServiceDiscoveryResType


class ServiceDetailReqType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, ServiceID=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("ServiceDetailReqType"), self).__init__( **kwargs_)
        self.ServiceID = ServiceID
        self.validate_serviceIDType(self.ServiceID)
        self.ServiceID_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ServiceDetailReqType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ServiceDetailReqType.subclass:
            return ServiceDetailReqType.subclass(*args_, **kwargs_)
        else:
            return ServiceDetailReqType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ServiceID(self):
        return self.ServiceID
    def set_ServiceID(self, ServiceID):
        self.ServiceID = ServiceID
    def validate_serviceIDType(self, value):
        result = True
        # Validate type serviceIDType, a restriction on xs:unsignedShort.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def _hasContent(self):
        if (
            self.ServiceID is not None or
            super(ServiceDetailReqType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='ServiceDetailReqType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ServiceDetailReqType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ServiceDetailReqType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ServiceDetailReqType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ServiceDetailReqType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ServiceDetailReqType'):
        super(ServiceDetailReqType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ServiceDetailReqType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='ServiceDetailReqType', fromsubclass_=False, pretty_print=True):
        super(ServiceDetailReqType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ServiceID is not None:
            namespaceprefix_ = self.ServiceID_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sServiceID>%s</%sServiceID>%s' % (namespaceprefix_ , self.gds_format_integer(self.ServiceID, input_name='ServiceID'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(ServiceDetailReqType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ServiceID' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'ServiceID')
            ival_ = self.gds_validate_integer(ival_, node, 'ServiceID')
            self.ServiceID = ival_
            self.ServiceID_nsprefix_ = child_.prefix
            # validate type serviceIDType
            self.validate_serviceIDType(self.ServiceID)
        super(ServiceDetailReqType, self)._buildChildren(child_, node, nodeName_, True)
# end class ServiceDetailReqType


class ServiceDetailResType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, ResponseCode=None, ServiceID=None, ServiceParameterList=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("ServiceDetailResType"), self).__init__( **kwargs_)
        self.ResponseCode = ResponseCode
        self.validate_responseCodeType(self.ResponseCode)
        self.ResponseCode_nsprefix_ = "ns6"
        self.ServiceID = ServiceID
        self.validate_serviceIDType(self.ServiceID)
        self.ServiceID_nsprefix_ = "ns6"
        self.ServiceParameterList = ServiceParameterList
        self.ServiceParameterList_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ServiceDetailResType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ServiceDetailResType.subclass:
            return ServiceDetailResType.subclass(*args_, **kwargs_)
        else:
            return ServiceDetailResType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ResponseCode(self):
        return self.ResponseCode
    def set_ResponseCode(self, ResponseCode):
        self.ResponseCode = ResponseCode
    def get_ServiceID(self):
        return self.ServiceID
    def set_ServiceID(self, ServiceID):
        self.ServiceID = ServiceID
    def get_ServiceParameterList(self):
        return self.ServiceParameterList
    def set_ServiceParameterList(self, ServiceParameterList):
        self.ServiceParameterList = ServiceParameterList
    def validate_responseCodeType(self, value):
        result = True
        # Validate type responseCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['OK', 'OK_NewSessionEstablished', 'OK_OldSessionJoined', 'OK_CertificateExpiresSoon', 'FAILED', 'FAILED_SequenceError', 'FAILED_ServiceIDInvalid', 'FAILED_UnknownSession', 'FAILED_ServiceSelectionInvalid', 'FAILED_PaymentSelectionInvalid', 'FAILED_CertificateExpired', 'FAILED_SignatureError', 'FAILED_NoCertificateAvailable', 'FAILED_CertChainError', 'FAILED_ChallengeInvalid', 'FAILED_ContractCanceled', 'FAILED_WrongChargeParameter', 'FAILED_PowerDeliveryNotApplied', 'FAILED_TariffSelectionInvalid', 'FAILED_ChargingProfileInvalid', 'FAILED_MeteringSignatureNotValid', 'FAILED_NoChargeServiceSelected', 'FAILED_WrongEnergyTransferMode', 'FAILED_ContactorError', 'FAILED_CertificateNotAllowedAtThisEVSE', 'FAILED_CertificateRevoked']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on responseCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_serviceIDType(self, value):
        result = True
        # Validate type serviceIDType, a restriction on xs:unsignedShort.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def _hasContent(self):
        if (
            self.ResponseCode is not None or
            self.ServiceID is not None or
            self.ServiceParameterList is not None or
            super(ServiceDetailResType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='ServiceDetailResType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ServiceDetailResType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ServiceDetailResType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ServiceDetailResType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ServiceDetailResType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ServiceDetailResType'):
        super(ServiceDetailResType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ServiceDetailResType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='ServiceDetailResType', fromsubclass_=False, pretty_print=True):
        super(ServiceDetailResType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ResponseCode is not None:
            namespaceprefix_ = self.ResponseCode_nsprefix_ + ':' if (UseCapturedNS_ and self.ResponseCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sResponseCode>%s</%sResponseCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ResponseCode), input_name='ResponseCode')), namespaceprefix_ , eol_))
        if self.ServiceID is not None:
            namespaceprefix_ = self.ServiceID_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sServiceID>%s</%sServiceID>%s' % (namespaceprefix_ , self.gds_format_integer(self.ServiceID, input_name='ServiceID'), namespaceprefix_ , eol_))
        if self.ServiceParameterList is not None:
            namespaceprefix_ = self.ServiceParameterList_nsprefix_ + ':' if (UseCapturedNS_ and self.ServiceParameterList_nsprefix_) else ''
            self.ServiceParameterList.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ServiceParameterList', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(ServiceDetailResType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ResponseCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ResponseCode')
            value_ = self.gds_validate_string(value_, node, 'ResponseCode')
            self.ResponseCode = value_
            self.ResponseCode_nsprefix_ = child_.prefix
            # validate type responseCodeType
            self.validate_responseCodeType(self.ResponseCode)
        elif nodeName_ == 'ServiceID' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'ServiceID')
            ival_ = self.gds_validate_integer(ival_, node, 'ServiceID')
            self.ServiceID = ival_
            self.ServiceID_nsprefix_ = child_.prefix
            # validate type serviceIDType
            self.validate_serviceIDType(self.ServiceID)
        elif nodeName_ == 'ServiceParameterList':
            obj_ = ServiceParameterListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ServiceParameterList = obj_
            obj_.original_tagname_ = 'ServiceParameterList'
        super(ServiceDetailResType, self)._buildChildren(child_, node, nodeName_, True)
# end class ServiceDetailResType


class PaymentServiceSelectionReqType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, SelectedPaymentOption=None, SelectedServiceList=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("PaymentServiceSelectionReqType"), self).__init__( **kwargs_)
        self.SelectedPaymentOption = SelectedPaymentOption
        self.validate_paymentOptionType(self.SelectedPaymentOption)
        self.SelectedPaymentOption_nsprefix_ = "ns6"
        self.SelectedServiceList = SelectedServiceList
        self.SelectedServiceList_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PaymentServiceSelectionReqType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PaymentServiceSelectionReqType.subclass:
            return PaymentServiceSelectionReqType.subclass(*args_, **kwargs_)
        else:
            return PaymentServiceSelectionReqType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_SelectedPaymentOption(self):
        return self.SelectedPaymentOption
    def set_SelectedPaymentOption(self, SelectedPaymentOption):
        self.SelectedPaymentOption = SelectedPaymentOption
    def get_SelectedServiceList(self):
        return self.SelectedServiceList
    def set_SelectedServiceList(self, SelectedServiceList):
        self.SelectedServiceList = SelectedServiceList
    def validate_paymentOptionType(self, value):
        result = True
        # Validate type paymentOptionType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Contract', 'ExternalPayment']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on paymentOptionType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.SelectedPaymentOption is not None or
            self.SelectedServiceList is not None or
            super(PaymentServiceSelectionReqType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='PaymentServiceSelectionReqType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PaymentServiceSelectionReqType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PaymentServiceSelectionReqType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PaymentServiceSelectionReqType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PaymentServiceSelectionReqType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PaymentServiceSelectionReqType'):
        super(PaymentServiceSelectionReqType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PaymentServiceSelectionReqType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='PaymentServiceSelectionReqType', fromsubclass_=False, pretty_print=True):
        super(PaymentServiceSelectionReqType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.SelectedPaymentOption is not None:
            namespaceprefix_ = self.SelectedPaymentOption_nsprefix_ + ':' if (UseCapturedNS_ and self.SelectedPaymentOption_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSelectedPaymentOption>%s</%sSelectedPaymentOption>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SelectedPaymentOption), input_name='SelectedPaymentOption')), namespaceprefix_ , eol_))
        if self.SelectedServiceList is not None:
            namespaceprefix_ = self.SelectedServiceList_nsprefix_ + ':' if (UseCapturedNS_ and self.SelectedServiceList_nsprefix_) else ''
            self.SelectedServiceList.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SelectedServiceList', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(PaymentServiceSelectionReqType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'SelectedPaymentOption':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SelectedPaymentOption')
            value_ = self.gds_validate_string(value_, node, 'SelectedPaymentOption')
            self.SelectedPaymentOption = value_
            self.SelectedPaymentOption_nsprefix_ = child_.prefix
            # validate type paymentOptionType
            self.validate_paymentOptionType(self.SelectedPaymentOption)
        elif nodeName_ == 'SelectedServiceList':
            obj_ = SelectedServiceListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SelectedServiceList = obj_
            obj_.original_tagname_ = 'SelectedServiceList'
        super(PaymentServiceSelectionReqType, self)._buildChildren(child_, node, nodeName_, True)
# end class PaymentServiceSelectionReqType


class PaymentServiceSelectionResType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, ResponseCode=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("PaymentServiceSelectionResType"), self).__init__( **kwargs_)
        self.ResponseCode = ResponseCode
        self.validate_responseCodeType(self.ResponseCode)
        self.ResponseCode_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PaymentServiceSelectionResType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PaymentServiceSelectionResType.subclass:
            return PaymentServiceSelectionResType.subclass(*args_, **kwargs_)
        else:
            return PaymentServiceSelectionResType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ResponseCode(self):
        return self.ResponseCode
    def set_ResponseCode(self, ResponseCode):
        self.ResponseCode = ResponseCode
    def validate_responseCodeType(self, value):
        result = True
        # Validate type responseCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['OK', 'OK_NewSessionEstablished', 'OK_OldSessionJoined', 'OK_CertificateExpiresSoon', 'FAILED', 'FAILED_SequenceError', 'FAILED_ServiceIDInvalid', 'FAILED_UnknownSession', 'FAILED_ServiceSelectionInvalid', 'FAILED_PaymentSelectionInvalid', 'FAILED_CertificateExpired', 'FAILED_SignatureError', 'FAILED_NoCertificateAvailable', 'FAILED_CertChainError', 'FAILED_ChallengeInvalid', 'FAILED_ContractCanceled', 'FAILED_WrongChargeParameter', 'FAILED_PowerDeliveryNotApplied', 'FAILED_TariffSelectionInvalid', 'FAILED_ChargingProfileInvalid', 'FAILED_MeteringSignatureNotValid', 'FAILED_NoChargeServiceSelected', 'FAILED_WrongEnergyTransferMode', 'FAILED_ContactorError', 'FAILED_CertificateNotAllowedAtThisEVSE', 'FAILED_CertificateRevoked']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on responseCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.ResponseCode is not None or
            super(PaymentServiceSelectionResType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='PaymentServiceSelectionResType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PaymentServiceSelectionResType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PaymentServiceSelectionResType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PaymentServiceSelectionResType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PaymentServiceSelectionResType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PaymentServiceSelectionResType'):
        super(PaymentServiceSelectionResType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PaymentServiceSelectionResType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='PaymentServiceSelectionResType', fromsubclass_=False, pretty_print=True):
        super(PaymentServiceSelectionResType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ResponseCode is not None:
            namespaceprefix_ = self.ResponseCode_nsprefix_ + ':' if (UseCapturedNS_ and self.ResponseCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sResponseCode>%s</%sResponseCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ResponseCode), input_name='ResponseCode')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(PaymentServiceSelectionResType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ResponseCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ResponseCode')
            value_ = self.gds_validate_string(value_, node, 'ResponseCode')
            self.ResponseCode = value_
            self.ResponseCode_nsprefix_ = child_.prefix
            # validate type responseCodeType
            self.validate_responseCodeType(self.ResponseCode)
        super(PaymentServiceSelectionResType, self)._buildChildren(child_, node, nodeName_, True)
# end class PaymentServiceSelectionResType


class PaymentDetailsReqType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, eMAID=None, ContractSignatureCertChain=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("PaymentDetailsReqType"), self).__init__( **kwargs_)
        self.eMAID = eMAID
        self.validate_eMAIDType(self.eMAID)
        self.eMAID_nsprefix_ = "ns6"
        self.ContractSignatureCertChain = ContractSignatureCertChain
        self.ContractSignatureCertChain_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PaymentDetailsReqType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PaymentDetailsReqType.subclass:
            return PaymentDetailsReqType.subclass(*args_, **kwargs_)
        else:
            return PaymentDetailsReqType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_eMAID(self):
        return self.eMAID
    def set_eMAID(self, eMAID):
        self.eMAID = eMAID
    def get_ContractSignatureCertChain(self):
        return self.ContractSignatureCertChain
    def set_ContractSignatureCertChain(self, ContractSignatureCertChain):
        self.ContractSignatureCertChain = ContractSignatureCertChain
    def validate_eMAIDType(self, value):
        result = True
        # Validate type eMAIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on eMAIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 14:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on eMAIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.eMAID is not None or
            self.ContractSignatureCertChain is not None or
            super(PaymentDetailsReqType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='PaymentDetailsReqType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PaymentDetailsReqType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PaymentDetailsReqType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PaymentDetailsReqType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PaymentDetailsReqType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PaymentDetailsReqType'):
        super(PaymentDetailsReqType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PaymentDetailsReqType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='PaymentDetailsReqType', fromsubclass_=False, pretty_print=True):
        super(PaymentDetailsReqType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.eMAID is not None:
            namespaceprefix_ = self.eMAID_nsprefix_ + ':' if (UseCapturedNS_ and self.eMAID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%seMAID>%s</%seMAID>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.eMAID), input_name='eMAID')), namespaceprefix_ , eol_))
        if self.ContractSignatureCertChain is not None:
            namespaceprefix_ = self.ContractSignatureCertChain_nsprefix_ + ':' if (UseCapturedNS_ and self.ContractSignatureCertChain_nsprefix_) else ''
            self.ContractSignatureCertChain.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ContractSignatureCertChain', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(PaymentDetailsReqType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'eMAID':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'eMAID')
            value_ = self.gds_validate_string(value_, node, 'eMAID')
            self.eMAID = value_
            self.eMAID_nsprefix_ = child_.prefix
            # validate type eMAIDType
            self.validate_eMAIDType(self.eMAID)
        elif nodeName_ == 'ContractSignatureCertChain':
            obj_ = CertificateChainType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ContractSignatureCertChain = obj_
            obj_.original_tagname_ = 'ContractSignatureCertChain'
        super(PaymentDetailsReqType, self)._buildChildren(child_, node, nodeName_, True)
# end class PaymentDetailsReqType


class PaymentDetailsResType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, ResponseCode=None, GenChallenge=None, EVSETimeStamp=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("PaymentDetailsResType"), self).__init__( **kwargs_)
        self.ResponseCode = ResponseCode
        self.validate_responseCodeType(self.ResponseCode)
        self.ResponseCode_nsprefix_ = "ns6"
        self.GenChallenge = GenChallenge
        self.validate_genChallengeType(self.GenChallenge)
        self.GenChallenge_nsprefix_ = "ns6"
        self.EVSETimeStamp = EVSETimeStamp
        self.EVSETimeStamp_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PaymentDetailsResType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PaymentDetailsResType.subclass:
            return PaymentDetailsResType.subclass(*args_, **kwargs_)
        else:
            return PaymentDetailsResType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ResponseCode(self):
        return self.ResponseCode
    def set_ResponseCode(self, ResponseCode):
        self.ResponseCode = ResponseCode
    def get_GenChallenge(self):
        return self.GenChallenge
    def set_GenChallenge(self, GenChallenge):
        self.GenChallenge = GenChallenge
    def get_EVSETimeStamp(self):
        return self.EVSETimeStamp
    def set_EVSETimeStamp(self, EVSETimeStamp):
        self.EVSETimeStamp = EVSETimeStamp
    def validate_responseCodeType(self, value):
        result = True
        # Validate type responseCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['OK', 'OK_NewSessionEstablished', 'OK_OldSessionJoined', 'OK_CertificateExpiresSoon', 'FAILED', 'FAILED_SequenceError', 'FAILED_ServiceIDInvalid', 'FAILED_UnknownSession', 'FAILED_ServiceSelectionInvalid', 'FAILED_PaymentSelectionInvalid', 'FAILED_CertificateExpired', 'FAILED_SignatureError', 'FAILED_NoCertificateAvailable', 'FAILED_CertChainError', 'FAILED_ChallengeInvalid', 'FAILED_ContractCanceled', 'FAILED_WrongChargeParameter', 'FAILED_PowerDeliveryNotApplied', 'FAILED_TariffSelectionInvalid', 'FAILED_ChargingProfileInvalid', 'FAILED_MeteringSignatureNotValid', 'FAILED_NoChargeServiceSelected', 'FAILED_WrongEnergyTransferMode', 'FAILED_ContactorError', 'FAILED_CertificateNotAllowedAtThisEVSE', 'FAILED_CertificateRevoked']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on responseCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_genChallengeType(self, value):
        result = True
        # Validate type genChallengeType, a restriction on xs:base64Binary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) != 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on genChallengeType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.ResponseCode is not None or
            self.GenChallenge is not None or
            self.EVSETimeStamp is not None or
            super(PaymentDetailsResType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes"  xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='PaymentDetailsResType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PaymentDetailsResType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PaymentDetailsResType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PaymentDetailsResType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PaymentDetailsResType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PaymentDetailsResType'):
        super(PaymentDetailsResType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PaymentDetailsResType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes"  xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='PaymentDetailsResType', fromsubclass_=False, pretty_print=True):
        super(PaymentDetailsResType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ResponseCode is not None:
            namespaceprefix_ = self.ResponseCode_nsprefix_ + ':' if (UseCapturedNS_ and self.ResponseCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sResponseCode>%s</%sResponseCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ResponseCode), input_name='ResponseCode')), namespaceprefix_ , eol_))
        if self.GenChallenge is not None:
            namespaceprefix_ = self.GenChallenge_nsprefix_ + ':' if (UseCapturedNS_ and self.GenChallenge_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sGenChallenge>%s</%sGenChallenge>%s' % (namespaceprefix_ , self.gds_format_base64(self.GenChallenge, input_name='GenChallenge'), namespaceprefix_ , eol_))
        if self.EVSETimeStamp is not None:
            namespaceprefix_ = self.EVSETimeStamp_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSETimeStamp_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEVSETimeStamp>%s</%sEVSETimeStamp>%s' % (namespaceprefix_ , self.gds_format_integer(self.EVSETimeStamp, input_name='EVSETimeStamp'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(PaymentDetailsResType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ResponseCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ResponseCode')
            value_ = self.gds_validate_string(value_, node, 'ResponseCode')
            self.ResponseCode = value_
            self.ResponseCode_nsprefix_ = child_.prefix
            # validate type responseCodeType
            self.validate_responseCodeType(self.ResponseCode)
        elif nodeName_ == 'GenChallenge':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'GenChallenge')
            else:
                bval_ = None
            self.GenChallenge = bval_
            self.GenChallenge_nsprefix_ = child_.prefix
            # validate type genChallengeType
            self.validate_genChallengeType(self.GenChallenge)
        elif nodeName_ == 'EVSETimeStamp' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'EVSETimeStamp')
            ival_ = self.gds_validate_integer(ival_, node, 'EVSETimeStamp')
            self.EVSETimeStamp = ival_
            self.EVSETimeStamp_nsprefix_ = child_.prefix
        super(PaymentDetailsResType, self)._buildChildren(child_, node, nodeName_, True)
# end class PaymentDetailsResType


class AuthorizationReqType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, Id=None, GenChallenge=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("AuthorizationReqType"), self).__init__( **kwargs_)
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.GenChallenge = GenChallenge
        self.validate_genChallengeType(self.GenChallenge)
        self.GenChallenge_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AuthorizationReqType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AuthorizationReqType.subclass:
            return AuthorizationReqType.subclass(*args_, **kwargs_)
        else:
            return AuthorizationReqType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_GenChallenge(self):
        return self.GenChallenge
    def set_GenChallenge(self, GenChallenge):
        self.GenChallenge = GenChallenge
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def validate_genChallengeType(self, value):
        result = True
        # Validate type genChallengeType, a restriction on xs:base64Binary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) != 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on genChallengeType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.GenChallenge is not None or
            super(AuthorizationReqType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='AuthorizationReqType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AuthorizationReqType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AuthorizationReqType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AuthorizationReqType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AuthorizationReqType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AuthorizationReqType'):
        super(AuthorizationReqType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AuthorizationReqType')
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='AuthorizationReqType', fromsubclass_=False, pretty_print=True):
        super(AuthorizationReqType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.GenChallenge is not None:
            namespaceprefix_ = self.GenChallenge_nsprefix_ + ':' if (UseCapturedNS_ and self.GenChallenge_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sGenChallenge>%s</%sGenChallenge>%s' % (namespaceprefix_ , self.gds_format_base64(self.GenChallenge, input_name='GenChallenge'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
        super(AuthorizationReqType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'GenChallenge':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'GenChallenge')
            else:
                bval_ = None
            self.GenChallenge = bval_
            self.GenChallenge_nsprefix_ = child_.prefix
            # validate type genChallengeType
            self.validate_genChallengeType(self.GenChallenge)
        super(AuthorizationReqType, self)._buildChildren(child_, node, nodeName_, True)
# end class AuthorizationReqType


class AuthorizationResType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, ResponseCode=None, EVSEProcessing=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("AuthorizationResType"), self).__init__( **kwargs_)
        self.ResponseCode = ResponseCode
        self.validate_responseCodeType(self.ResponseCode)
        self.ResponseCode_nsprefix_ = "ns6"
        self.EVSEProcessing = EVSEProcessing
        self.validate_EVSEProcessingType(self.EVSEProcessing)
        self.EVSEProcessing_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AuthorizationResType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AuthorizationResType.subclass:
            return AuthorizationResType.subclass(*args_, **kwargs_)
        else:
            return AuthorizationResType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ResponseCode(self):
        return self.ResponseCode
    def set_ResponseCode(self, ResponseCode):
        self.ResponseCode = ResponseCode
    def get_EVSEProcessing(self):
        return self.EVSEProcessing
    def set_EVSEProcessing(self, EVSEProcessing):
        self.EVSEProcessing = EVSEProcessing
    def validate_responseCodeType(self, value):
        result = True
        # Validate type responseCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['OK', 'OK_NewSessionEstablished', 'OK_OldSessionJoined', 'OK_CertificateExpiresSoon', 'FAILED', 'FAILED_SequenceError', 'FAILED_ServiceIDInvalid', 'FAILED_UnknownSession', 'FAILED_ServiceSelectionInvalid', 'FAILED_PaymentSelectionInvalid', 'FAILED_CertificateExpired', 'FAILED_SignatureError', 'FAILED_NoCertificateAvailable', 'FAILED_CertChainError', 'FAILED_ChallengeInvalid', 'FAILED_ContractCanceled', 'FAILED_WrongChargeParameter', 'FAILED_PowerDeliveryNotApplied', 'FAILED_TariffSelectionInvalid', 'FAILED_ChargingProfileInvalid', 'FAILED_MeteringSignatureNotValid', 'FAILED_NoChargeServiceSelected', 'FAILED_WrongEnergyTransferMode', 'FAILED_ContactorError', 'FAILED_CertificateNotAllowedAtThisEVSE', 'FAILED_CertificateRevoked']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on responseCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_EVSEProcessingType(self, value):
        result = True
        # Validate type EVSEProcessingType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Finished', 'Ongoing', 'Ongoing_WaitingForCustomerInteraction']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on EVSEProcessingType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.ResponseCode is not None or
            self.EVSEProcessing is not None or
            super(AuthorizationResType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='AuthorizationResType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AuthorizationResType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AuthorizationResType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AuthorizationResType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AuthorizationResType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AuthorizationResType'):
        super(AuthorizationResType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AuthorizationResType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='AuthorizationResType', fromsubclass_=False, pretty_print=True):
        super(AuthorizationResType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ResponseCode is not None:
            namespaceprefix_ = self.ResponseCode_nsprefix_ + ':' if (UseCapturedNS_ and self.ResponseCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sResponseCode>%s</%sResponseCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ResponseCode), input_name='ResponseCode')), namespaceprefix_ , eol_))
        if self.EVSEProcessing is not None:
            namespaceprefix_ = self.EVSEProcessing_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEProcessing_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEVSEProcessing>%s</%sEVSEProcessing>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.EVSEProcessing), input_name='EVSEProcessing')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(AuthorizationResType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ResponseCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ResponseCode')
            value_ = self.gds_validate_string(value_, node, 'ResponseCode')
            self.ResponseCode = value_
            self.ResponseCode_nsprefix_ = child_.prefix
            # validate type responseCodeType
            self.validate_responseCodeType(self.ResponseCode)
        elif nodeName_ == 'EVSEProcessing':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'EVSEProcessing')
            value_ = self.gds_validate_string(value_, node, 'EVSEProcessing')
            self.EVSEProcessing = value_
            self.EVSEProcessing_nsprefix_ = child_.prefix
            # validate type EVSEProcessingType
            self.validate_EVSEProcessingType(self.EVSEProcessing)
        super(AuthorizationResType, self)._buildChildren(child_, node, nodeName_, True)
# end class AuthorizationResType


class ChargeParameterDiscoveryReqType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, MaxEntriesSAScheduleTuple=None, RequestedEnergyTransferMode=None, EVChargeParameter=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("ChargeParameterDiscoveryReqType"), self).__init__( **kwargs_)
        self.MaxEntriesSAScheduleTuple = MaxEntriesSAScheduleTuple
        self.MaxEntriesSAScheduleTuple_nsprefix_ = None
        self.RequestedEnergyTransferMode = RequestedEnergyTransferMode
        self.validate_EnergyTransferModeType(self.RequestedEnergyTransferMode)
        self.RequestedEnergyTransferMode_nsprefix_ = "ns6"
        self.EVChargeParameter = EVChargeParameter
        self.EVChargeParameter_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ChargeParameterDiscoveryReqType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ChargeParameterDiscoveryReqType.subclass:
            return ChargeParameterDiscoveryReqType.subclass(*args_, **kwargs_)
        else:
            return ChargeParameterDiscoveryReqType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_MaxEntriesSAScheduleTuple(self):
        return self.MaxEntriesSAScheduleTuple
    def set_MaxEntriesSAScheduleTuple(self, MaxEntriesSAScheduleTuple):
        self.MaxEntriesSAScheduleTuple = MaxEntriesSAScheduleTuple
    def get_RequestedEnergyTransferMode(self):
        return self.RequestedEnergyTransferMode
    def set_RequestedEnergyTransferMode(self, RequestedEnergyTransferMode):
        self.RequestedEnergyTransferMode = RequestedEnergyTransferMode
    def get_EVChargeParameter(self):
        return self.EVChargeParameter
    def set_EVChargeParameter(self, EVChargeParameter):
        self.EVChargeParameter = EVChargeParameter
    def validate_EnergyTransferModeType(self, value):
        result = True
        # Validate type EnergyTransferModeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['AC_single_phase_core', 'AC_three_phase_core', 'DC_core', 'DC_extended', 'DC_combo_core', 'DC_unique']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on EnergyTransferModeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.MaxEntriesSAScheduleTuple is not None or
            self.RequestedEnergyTransferMode is not None or
            self.EVChargeParameter is not None or
            super(ChargeParameterDiscoveryReqType, self)._hasContent()
        ):
            return True
        else:
            return FalseChargeParameterDiscoveryReq
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:None="urn:iso:15118:2:2013:MsgBody"  xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='ChargeParameterDiscoveryReqType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ChargeParameterDiscoveryReqType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ChargeParameterDiscoveryReqType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ChargeParameterDiscoveryReqType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ChargeParameterDiscoveryReqType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ChargeParameterDiscoveryReqType'):
        super(ChargeParameterDiscoveryReqType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ChargeParameterDiscoveryReqType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:None="urn:iso:15118:2:2013:MsgBody"  xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='ChargeParameterDiscoveryReqType', fromsubclass_=False, pretty_print=True):
        super(ChargeParameterDiscoveryReqType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.MaxEntriesSAScheduleTuple is not None:
            namespaceprefix_ = self.MaxEntriesSAScheduleTuple_nsprefix_ + ':' if (UseCapturedNS_ and self.MaxEntriesSAScheduleTuple_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMaxEntriesSAScheduleTuple>%s</%sMaxEntriesSAScheduleTuple>%s' % (namespaceprefix_ , self.gds_format_integer(self.MaxEntriesSAScheduleTuple, input_name='MaxEntriesSAScheduleTuple'), namespaceprefix_ , eol_))
        if self.RequestedEnergyTransferMode is not None:
            namespaceprefix_ = self.RequestedEnergyTransferMode_nsprefix_ + ':' if (UseCapturedNS_ and self.RequestedEnergyTransferMode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRequestedEnergyTransferMode>%s</%sRequestedEnergyTransferMode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.RequestedEnergyTransferMode), input_name='RequestedEnergyTransferMode')), namespaceprefix_ , eol_))
        if self.EVChargeParameter is not None:
            self.EVChargeParameter.export(outfile, level, namespaceprefix_, namespacedef_='', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(ChargeParameterDiscoveryReqType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'MaxEntriesSAScheduleTuple' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'MaxEntriesSAScheduleTuple')
            ival_ = self.gds_validate_integer(ival_, node, 'MaxEntriesSAScheduleTuple')
            self.MaxEntriesSAScheduleTuple = ival_
            self.MaxEntriesSAScheduleTuple_nsprefix_ = child_.prefix
        elif nodeName_ == 'RequestedEnergyTransferMode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RequestedEnergyTransferMode')
            value_ = self.gds_validate_string(value_, node, 'RequestedEnergyTransferMode')
            self.RequestedEnergyTransferMode = value_
            self.RequestedEnergyTransferMode_nsprefix_ = child_.prefix
            # validate type EnergyTransferModeType
            self.validate_EnergyTransferModeType(self.RequestedEnergyTransferMode)
        elif nodeName_ == 'EVChargeParameter':
            type_name_ = child_.attrib.get(
                '{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()["" + type_name_]
                obj_ = class_.factory()
                obj_.build(child_, gds_collector_=gds_collector_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <EVChargeParameter> element')
            self.EVChargeParameter = obj_
            obj_.original_tagname_ = 'EVChargeParameter'
        elif nodeName_ == 'AC_EVChargeParameter':
            obj_ = AC_EVChargeParameterType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVChargeParameter = obj_
            obj_.original_tagname_ = 'AC_EVChargeParameter'
        elif nodeName_ == 'DC_EVChargeParameter':
            obj_ = DC_EVChargeParameterType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVChargeParameter = obj_
            obj_.original_tagname_ = 'DC_EVChargeParameter'
        super(ChargeParameterDiscoveryReqType, self)._buildChildren(child_, node, nodeName_, True)
# end class ChargeParameterDiscoveryReqType


class ChargeParameterDiscoveryResType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, ResponseCode=None, EVSEProcessing=None, SASchedules=None, EVSEChargeParameter=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("ChargeParameterDiscoveryResType"), self).__init__( **kwargs_)
        self.ResponseCode = ResponseCode
        self.validate_responseCodeType(self.ResponseCode)
        self.ResponseCode_nsprefix_ = "ns6"
        self.EVSEProcessing = EVSEProcessing
        self.validate_EVSEProcessingType(self.EVSEProcessing)
        self.EVSEProcessing_nsprefix_ = "ns6"
        self.SASchedules = SASchedules
        self.SASchedules_nsprefix_ = "ns6"
        self.EVSEChargeParameter = EVSEChargeParameter
        self.EVSEChargeParameter_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ChargeParameterDiscoveryResType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ChargeParameterDiscoveryResType.subclass:
            return ChargeParameterDiscoveryResType.subclass(*args_, **kwargs_)
        else:
            return ChargeParameterDiscoveryResType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ResponseCode(self):
        return self.ResponseCode
    def set_ResponseCode(self, ResponseCode):
        self.ResponseCode = ResponseCode
    def get_EVSEProcessing(self):
        return self.EVSEProcessing
    def set_EVSEProcessing(self, EVSEProcessing):
        self.EVSEProcessing = EVSEProcessing
    def get_SASchedules(self):
        return self.SASchedules
    def set_SASchedules(self, SASchedules):
        self.SASchedules = SASchedules
    def get_EVSEChargeParameter(self):
        return self.EVSEChargeParameter
    def set_EVSEChargeParameter(self, EVSEChargeParameter):
        self.EVSEChargeParameter = EVSEChargeParameter
    def validate_responseCodeType(self, value):
        result = True
        # Validate type responseCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['OK', 'OK_NewSessionEstablished', 'OK_OldSessionJoined', 'OK_CertificateExpiresSoon', 'FAILED', 'FAILED_SequenceError', 'FAILED_ServiceIDInvalid', 'FAILED_UnknownSession', 'FAILED_ServiceSelectionInvalid', 'FAILED_PaymentSelectionInvalid', 'FAILED_CertificateExpired', 'FAILED_SignatureError', 'FAILED_NoCertificateAvailable', 'FAILED_CertChainError', 'FAILED_ChallengeInvalid', 'FAILED_ContractCanceled', 'FAILED_WrongChargeParameter', 'FAILED_PowerDeliveryNotApplied', 'FAILED_TariffSelectionInvalid', 'FAILED_ChargingProfileInvalid', 'FAILED_MeteringSignatureNotValid', 'FAILED_NoChargeServiceSelected', 'FAILED_WrongEnergyTransferMode', 'FAILED_ContactorError', 'FAILED_CertificateNotAllowedAtThisEVSE', 'FAILED_CertificateRevoked']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on responseCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_EVSEProcessingType(self, value):
        result = True
        # Validate type EVSEProcessingType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Finished', 'Ongoing', 'Ongoing_WaitingForCustomerInteraction']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on EVSEProcessingType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.ResponseCode is not None or
            self.EVSEProcessing is not None or
            self.SASchedules is not None or
            self.EVSEChargeParameter is not None or
            super(ChargeParameterDiscoveryResType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='ChargeParameterDiscoveryResType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ChargeParameterDiscoveryResType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ChargeParameterDiscoveryResType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ChargeParameterDiscoveryResType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ChargeParameterDiscoveryResType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ChargeParameterDiscoveryResType'):
        super(ChargeParameterDiscoveryResType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ChargeParameterDiscoveryResType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='ChargeParameterDiscoveryResType', fromsubclass_=False, pretty_print=True):
        super(ChargeParameterDiscoveryResType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ResponseCode is not None:
            namespaceprefix_ = self.ResponseCode_nsprefix_ + ':' if (UseCapturedNS_ and self.ResponseCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sResponseCode>%s</%sResponseCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ResponseCode), input_name='ResponseCode')), namespaceprefix_ , eol_))
        if self.EVSEProcessing is not None:
            namespaceprefix_ = self.EVSEProcessing_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEProcessing_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEVSEProcessing>%s</%sEVSEProcessing>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.EVSEProcessing), input_name='EVSEProcessing')), namespaceprefix_ , eol_))
        if self.SASchedules is not None:
            self.SASchedules.export(outfile, level, namespaceprefix_, namespacedef_='', pretty_print=pretty_print)
        if self.EVSEChargeParameter is not None:
            self.EVSEChargeParameter.export(outfile, level, namespaceprefix_, namespacedef_='', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(ChargeParameterDiscoveryResType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ResponseCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ResponseCode')
            value_ = self.gds_validate_string(value_, node, 'ResponseCode')
            self.ResponseCode = value_
            self.ResponseCode_nsprefix_ = child_.prefix
            # validate type responseCodeType
            self.validate_responseCodeType(self.ResponseCode)
        elif nodeName_ == 'EVSEProcessing':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'EVSEProcessing')
            value_ = self.gds_validate_string(value_, node, 'EVSEProcessing')
            self.EVSEProcessing = value_
            self.EVSEProcessing_nsprefix_ = child_.prefix
            # validate type EVSEProcessingType
            self.validate_EVSEProcessingType(self.EVSEProcessing)
        elif nodeName_ == 'SASchedules':
            type_name_ = child_.attrib.get(
                '{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()["" + type_name_]
                obj_ = class_.factory()
                obj_.build(child_, gds_collector_=gds_collector_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <SASchedules> element')
            self.SASchedules = obj_
            obj_.original_tagname_ = 'SASchedules'
        elif nodeName_ == 'SAScheduleList':
            obj_ = SAScheduleListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SASchedules = obj_
            obj_.original_tagname_ = 'SAScheduleList'
        elif nodeName_ == 'EVSEChargeParameter':
            type_name_ = child_.attrib.get(
                '{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()["" + type_name_]
                obj_ = class_.factory()
                obj_.build(child_, gds_collector_=gds_collector_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <EVSEChargeParameter> element')
            self.EVSEChargeParameter = obj_
            obj_.original_tagname_ = 'EVSEChargeParameter'
        elif nodeName_ == 'AC_EVSEChargeParameter':
            obj_ = AC_EVSEChargeParameterType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSEChargeParameter = obj_
            obj_.original_tagname_ = 'AC_EVSEChargeParameter'
        elif nodeName_ == 'DC_EVSEChargeParameter':
            obj_ = DC_EVSEChargeParameterType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSEChargeParameter = obj_
            obj_.original_tagname_ = 'DC_EVSEChargeParameter'
        super(ChargeParameterDiscoveryResType, self)._buildChildren(child_, node, nodeName_, True)
# end class ChargeParameterDiscoveryResType


class PowerDeliveryReqType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, ChargeProgress=None, SAScheduleTupleID=None, ChargingProfile=None, EVPowerDeliveryParameter=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("PowerDeliveryReqType"), self).__init__( **kwargs_)
        self.ChargeProgress = ChargeProgress
        self.validate_chargeProgressType(self.ChargeProgress)
        self.ChargeProgress_nsprefix_ = "ns6"
        self.SAScheduleTupleID = SAScheduleTupleID
        self.validate_SAIDType(self.SAScheduleTupleID)
        self.SAScheduleTupleID_nsprefix_ = "ns6"
        self.ChargingProfile = ChargingProfile
        self.ChargingProfile_nsprefix_ = "ns6"
        self.EVPowerDeliveryParameter = EVPowerDeliveryParameter
        self.EVPowerDeliveryParameter_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PowerDeliveryReqType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PowerDeliveryReqType.subclass:
            return PowerDeliveryReqType.subclass(*args_, **kwargs_)
        else:
            return PowerDeliveryReqType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ChargeProgress(self):
        return self.ChargeProgress
    def set_ChargeProgress(self, ChargeProgress):
        self.ChargeProgress = ChargeProgress
    def get_SAScheduleTupleID(self):
        return self.SAScheduleTupleID
    def set_SAScheduleTupleID(self, SAScheduleTupleID):
        self.SAScheduleTupleID = SAScheduleTupleID
    def get_ChargingProfile(self):
        return self.ChargingProfile
    def set_ChargingProfile(self, ChargingProfile):
        self.ChargingProfile = ChargingProfile
    def get_EVPowerDeliveryParameter(self):
        return self.EVPowerDeliveryParameter
    def set_EVPowerDeliveryParameter(self, EVPowerDeliveryParameter):
        self.EVPowerDeliveryParameter = EVPowerDeliveryParameter
    def validate_chargeProgressType(self, value):
        result = True
        # Validate type chargeProgressType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Start', 'Stop', 'Renegotiate']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on chargeProgressType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_SAIDType(self, value):
        result = True
        # Validate type SAIDType, a restriction on xs:unsignedByte.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on SAIDType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on SAIDType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.ChargeProgress is not None or
            self.SAScheduleTupleID is not None or
            self.ChargingProfile is not None or
            self.EVPowerDeliveryParameter is not None or
            super(PowerDeliveryReqType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='PowerDeliveryReqType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PowerDeliveryReqType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PowerDeliveryReqType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PowerDeliveryReqType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PowerDeliveryReqType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PowerDeliveryReqType'):
        super(PowerDeliveryReqType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PowerDeliveryReqType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='PowerDeliveryReqType', fromsubclass_=False, pretty_print=True):
        super(PowerDeliveryReqType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ChargeProgress is not None:
            namespaceprefix_ = self.ChargeProgress_nsprefix_ + ':' if (UseCapturedNS_ and self.ChargeProgress_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sChargeProgress>%s</%sChargeProgress>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ChargeProgress), input_name='ChargeProgress')), namespaceprefix_ , eol_))
        if self.SAScheduleTupleID is not None:
            namespaceprefix_ = self.SAScheduleTupleID_nsprefix_ + ':' if (UseCapturedNS_ and self.SAScheduleTupleID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSAScheduleTupleID>%s</%sSAScheduleTupleID>%s' % (namespaceprefix_ , self.gds_format_integer(self.SAScheduleTupleID, input_name='SAScheduleTupleID'), namespaceprefix_ , eol_))
        if self.ChargingProfile is not None:
            namespaceprefix_ = self.ChargingProfile_nsprefix_ + ':' if (UseCapturedNS_ and self.ChargingProfile_nsprefix_) else ''
            self.ChargingProfile.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ChargingProfile', pretty_print=pretty_print)
        if self.EVPowerDeliveryParameter is not None:
            self.EVPowerDeliveryParameter.export(outfile, level, namespaceprefix_, namespacedef_='', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(PowerDeliveryReqType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ChargeProgress':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ChargeProgress')
            value_ = self.gds_validate_string(value_, node, 'ChargeProgress')
            self.ChargeProgress = value_
            self.ChargeProgress_nsprefix_ = child_.prefix
            # validate type chargeProgressType
            self.validate_chargeProgressType(self.ChargeProgress)
        elif nodeName_ == 'SAScheduleTupleID' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'SAScheduleTupleID')
            ival_ = self.gds_validate_integer(ival_, node, 'SAScheduleTupleID')
            self.SAScheduleTupleID = ival_
            self.SAScheduleTupleID_nsprefix_ = child_.prefix
            # validate type SAIDType
            self.validate_SAIDType(self.SAScheduleTupleID)
        elif nodeName_ == 'ChargingProfile':
            obj_ = ChargingProfileType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ChargingProfile = obj_
            obj_.original_tagname_ = 'ChargingProfile'
        elif nodeName_ == 'EVPowerDeliveryParameter':
            type_name_ = child_.attrib.get(
                '{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()["" + type_name_]
                obj_ = class_.factory()
                obj_.build(child_, gds_collector_=gds_collector_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <EVPowerDeliveryParameter> element')
            self.EVPowerDeliveryParameter = obj_
            obj_.original_tagname_ = 'EVPowerDeliveryParameter'
        elif nodeName_ == 'DC_EVPowerDeliveryParameter':
            obj_ = DC_EVPowerDeliveryParameterType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVPowerDeliveryParameter = obj_
            obj_.original_tagname_ = 'DC_EVPowerDeliveryParameter'
        super(PowerDeliveryReqType, self)._buildChildren(child_, node, nodeName_, True)
# end class PowerDeliveryReqType


class PowerDeliveryResType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, ResponseCode=None, EVSEStatus=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("PowerDeliveryResType"), self).__init__( **kwargs_)
        self.ResponseCode = ResponseCode
        self.validate_responseCodeType(self.ResponseCode)
        self.ResponseCode_nsprefix_ = "ns6"
        self.EVSEStatus = EVSEStatus
        self.EVSEStatus_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PowerDeliveryResType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PowerDeliveryResType.subclass:
            return PowerDeliveryResType.subclass(*args_, **kwargs_)
        else:
            return PowerDeliveryResType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ResponseCode(self):
        return self.ResponseCode
    def set_ResponseCode(self, ResponseCode):
        self.ResponseCode = ResponseCode
    def get_EVSEStatus(self):
        return self.EVSEStatus
    def set_EVSEStatus(self, EVSEStatus):
        self.EVSEStatus = EVSEStatus
    def validate_responseCodeType(self, value):
        result = True
        # Validate type responseCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['OK', 'OK_NewSessionEstablished', 'OK_OldSessionJoined', 'OK_CertificateExpiresSoon', 'FAILED', 'FAILED_SequenceError', 'FAILED_ServiceIDInvalid', 'FAILED_UnknownSession', 'FAILED_ServiceSelectionInvalid', 'FAILED_PaymentSelectionInvalid', 'FAILED_CertificateExpired', 'FAILED_SignatureError', 'FAILED_NoCertificateAvailable', 'FAILED_CertChainError', 'FAILED_ChallengeInvalid', 'FAILED_ContractCanceled', 'FAILED_WrongChargeParameter', 'FAILED_PowerDeliveryNotApplied', 'FAILED_TariffSelectionInvalid', 'FAILED_ChargingProfileInvalid', 'FAILED_MeteringSignatureNotValid', 'FAILED_NoChargeServiceSelected', 'FAILED_WrongEnergyTransferMode', 'FAILED_ContactorError', 'FAILED_CertificateNotAllowedAtThisEVSE', 'FAILED_CertificateRevoked']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on responseCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.ResponseCode is not None or
            self.EVSEStatus is not None or
            super(PowerDeliveryResType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='PowerDeliveryResType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PowerDeliveryResType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PowerDeliveryResType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PowerDeliveryResType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PowerDeliveryResType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PowerDeliveryResType'):
        super(PowerDeliveryResType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PowerDeliveryResType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='PowerDeliveryResType', fromsubclass_=False, pretty_print=True):
        super(PowerDeliveryResType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ResponseCode is not None:
            namespaceprefix_ = self.ResponseCode_nsprefix_ + ':' if (UseCapturedNS_ and self.ResponseCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sResponseCode>%s</%sResponseCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ResponseCode), input_name='ResponseCode')), namespaceprefix_ , eol_))
        if self.EVSEStatus is not None:
            self.EVSEStatus.export(outfile, level, namespaceprefix_, namespacedef_='', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(PowerDeliveryResType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ResponseCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ResponseCode')
            value_ = self.gds_validate_string(value_, node, 'ResponseCode')
            self.ResponseCode = value_
            self.ResponseCode_nsprefix_ = child_.prefix
            # validate type responseCodeType
            self.validate_responseCodeType(self.ResponseCode)
        elif nodeName_ == 'EVSEStatus':
            type_name_ = child_.attrib.get(
                '{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()["" + type_name_]
                obj_ = class_.factory()
                obj_.build(child_, gds_collector_=gds_collector_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <EVSEStatus> element')
            self.EVSEStatus = obj_
            obj_.original_tagname_ = 'EVSEStatus'
        elif nodeName_ == 'AC_EVSEStatus':
            obj_ = AC_EVSEStatusType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSEStatus = obj_
            obj_.original_tagname_ = 'AC_EVSEStatus'
        elif nodeName_ == 'DC_EVSEStatus':
            obj_ = DC_EVSEStatusType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSEStatus = obj_
            obj_.original_tagname_ = 'DC_EVSEStatus'
        super(PowerDeliveryResType, self)._buildChildren(child_, node, nodeName_, True)
# end class PowerDeliveryResType


class MeteringReceiptReqType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, Id=None, SessionID=None, SAScheduleTupleID=None, MeterInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("MeteringReceiptReqType"), self).__init__( **kwargs_)
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.SessionID = SessionID
        self.validate_sessionIDType(self.SessionID)
        self.SessionID_nsprefix_ = "ns6"
        self.SAScheduleTupleID = SAScheduleTupleID
        self.validate_SAIDType(self.SAScheduleTupleID)
        self.SAScheduleTupleID_nsprefix_ = "ns6"
        self.MeterInfo = MeterInfo
        self.MeterInfo_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MeteringReceiptReqType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MeteringReceiptReqType.subclass:
            return MeteringReceiptReqType.subclass(*args_, **kwargs_)
        else:
            return MeteringReceiptReqType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_SessionID(self):
        return self.SessionID
    def set_SessionID(self, SessionID):
        self.SessionID = SessionID
    def get_SAScheduleTupleID(self):
        return self.SAScheduleTupleID
    def set_SAScheduleTupleID(self, SAScheduleTupleID):
        self.SAScheduleTupleID = SAScheduleTupleID
    def get_MeterInfo(self):
        return self.MeterInfo
    def set_MeterInfo(self, MeterInfo):
        self.MeterInfo = MeterInfo
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def validate_sessionIDType(self, value):
        result = True
        # Validate type sessionIDType, a restriction on xs:hexBinary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on sessionIDType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_SAIDType(self, value):
        result = True
        # Validate type SAIDType, a restriction on xs:unsignedByte.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on SAIDType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on SAIDType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.SessionID is not None or
            self.SAScheduleTupleID is not None or
            self.MeterInfo is not None or
            super(MeteringReceiptReqType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='MeteringReceiptReqType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MeteringReceiptReqType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MeteringReceiptReqType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MeteringReceiptReqType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MeteringReceiptReqType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MeteringReceiptReqType'):
        super(MeteringReceiptReqType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MeteringReceiptReqType')
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='MeteringReceiptReqType', fromsubclass_=False, pretty_print=True):
        super(MeteringReceiptReqType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.SessionID is not None:
            namespaceprefix_ = self.SessionID_nsprefix_ + ':' if (UseCapturedNS_ and self.SessionID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSessionID>%s</%sSessionID>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SessionID), input_name='SessionID')), namespaceprefix_ , eol_))
        if self.SAScheduleTupleID is not None:
            namespaceprefix_ = self.SAScheduleTupleID_nsprefix_ + ':' if (UseCapturedNS_ and self.SAScheduleTupleID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSAScheduleTupleID>%s</%sSAScheduleTupleID>%s' % (namespaceprefix_ , self.gds_format_integer(self.SAScheduleTupleID, input_name='SAScheduleTupleID'), namespaceprefix_ , eol_))
        if self.MeterInfo is not None:
            namespaceprefix_ = self.MeterInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.MeterInfo_nsprefix_) else ''
            self.MeterInfo.export(outfile, level, namespaceprefix_, namespacedef_='', name_='MeterInfo', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
        super(MeteringReceiptReqType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'SessionID':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SessionID')
            value_ = self.gds_validate_string(value_, node, 'SessionID')
            self.SessionID = value_
            self.SessionID_nsprefix_ = child_.prefix
            # validate type sessionIDType
            self.validate_sessionIDType(self.SessionID)
        elif nodeName_ == 'SAScheduleTupleID' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'SAScheduleTupleID')
            ival_ = self.gds_validate_integer(ival_, node, 'SAScheduleTupleID')
            self.SAScheduleTupleID = ival_
            self.SAScheduleTupleID_nsprefix_ = child_.prefix
            # validate type SAIDType
            self.validate_SAIDType(self.SAScheduleTupleID)
        elif nodeName_ == 'MeterInfo':
            obj_ = MeterInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.MeterInfo = obj_
            obj_.original_tagname_ = 'MeterInfo'
        super(MeteringReceiptReqType, self)._buildChildren(child_, node, nodeName_, True)
# end class MeteringReceiptReqType


class MeteringReceiptResType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, ResponseCode=None, EVSEStatus=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("MeteringReceiptResType"), self).__init__( **kwargs_)
        self.ResponseCode = ResponseCode
        self.validate_responseCodeType(self.ResponseCode)
        self.ResponseCode_nsprefix_ = "ns6"
        self.EVSEStatus = EVSEStatus
        self.EVSEStatus_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MeteringReceiptResType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MeteringReceiptResType.subclass:
            return MeteringReceiptResType.subclass(*args_, **kwargs_)
        else:
            return MeteringReceiptResType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ResponseCode(self):
        return self.ResponseCode
    def set_ResponseCode(self, ResponseCode):
        self.ResponseCode = ResponseCode
    def get_EVSEStatus(self):
        return self.EVSEStatus
    def set_EVSEStatus(self, EVSEStatus):
        self.EVSEStatus = EVSEStatus
    def validate_responseCodeType(self, value):
        result = True
        # Validate type responseCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['OK', 'OK_NewSessionEstablished', 'OK_OldSessionJoined', 'OK_CertificateExpiresSoon', 'FAILED', 'FAILED_SequenceError', 'FAILED_ServiceIDInvalid', 'FAILED_UnknownSession', 'FAILED_ServiceSelectionInvalid', 'FAILED_PaymentSelectionInvalid', 'FAILED_CertificateExpired', 'FAILED_SignatureError', 'FAILED_NoCertificateAvailable', 'FAILED_CertChainError', 'FAILED_ChallengeInvalid', 'FAILED_ContractCanceled', 'FAILED_WrongChargeParameter', 'FAILED_PowerDeliveryNotApplied', 'FAILED_TariffSelectionInvalid', 'FAILED_ChargingProfileInvalid', 'FAILED_MeteringSignatureNotValid', 'FAILED_NoChargeServiceSelected', 'FAILED_WrongEnergyTransferMode', 'FAILED_ContactorError', 'FAILED_CertificateNotAllowedAtThisEVSE', 'FAILED_CertificateRevoked']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on responseCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.ResponseCode is not None or
            self.EVSEStatus is not None or
            super(MeteringReceiptResType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='MeteringReceiptResType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MeteringReceiptResType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MeteringReceiptResType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MeteringReceiptResType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MeteringReceiptResType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MeteringReceiptResType'):
        super(MeteringReceiptResType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MeteringReceiptResType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='MeteringReceiptResType', fromsubclass_=False, pretty_print=True):
        super(MeteringReceiptResType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ResponseCode is not None:
            namespaceprefix_ = self.ResponseCode_nsprefix_ + ':' if (UseCapturedNS_ and self.ResponseCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sResponseCode>%s</%sResponseCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ResponseCode), input_name='ResponseCode')), namespaceprefix_ , eol_))
        if self.EVSEStatus is not None:
            self.EVSEStatus.export(outfile, level, namespaceprefix_, namespacedef_='', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(MeteringReceiptResType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ResponseCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ResponseCode')
            value_ = self.gds_validate_string(value_, node, 'ResponseCode')
            self.ResponseCode = value_
            self.ResponseCode_nsprefix_ = child_.prefix
            # validate type responseCodeType
            self.validate_responseCodeType(self.ResponseCode)
        elif nodeName_ == 'EVSEStatus':
            type_name_ = child_.attrib.get(
                '{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()["" + type_name_]
                obj_ = class_.factory()
                obj_.build(child_, gds_collector_=gds_collector_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <EVSEStatus> element')
            self.EVSEStatus = obj_
            obj_.original_tagname_ = 'EVSEStatus'
        elif nodeName_ == 'AC_EVSEStatus':
            obj_ = AC_EVSEStatusType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSEStatus = obj_
            obj_.original_tagname_ = 'AC_EVSEStatus'
        elif nodeName_ == 'DC_EVSEStatus':
            obj_ = DC_EVSEStatusType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSEStatus = obj_
            obj_.original_tagname_ = 'DC_EVSEStatus'
        super(MeteringReceiptResType, self)._buildChildren(child_, node, nodeName_, True)
# end class MeteringReceiptResType


class SessionStopReqType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, ChargingSession=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("SessionStopReqType"), self).__init__( **kwargs_)
        self.ChargingSession = ChargingSession
        self.validate_chargingSessionType(self.ChargingSession)
        self.ChargingSession_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SessionStopReqType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SessionStopReqType.subclass:
            return SessionStopReqType.subclass(*args_, **kwargs_)
        else:
            return SessionStopReqType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ChargingSession(self):
        return self.ChargingSession
    def set_ChargingSession(self, ChargingSession):
        self.ChargingSession = ChargingSession
    def validate_chargingSessionType(self, value):
        result = True
        # Validate type chargingSessionType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Terminate', 'Pause']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on chargingSessionType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.ChargingSession is not None or
            super(SessionStopReqType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='SessionStopReqType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SessionStopReqType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SessionStopReqType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SessionStopReqType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SessionStopReqType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SessionStopReqType'):
        super(SessionStopReqType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SessionStopReqType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='SessionStopReqType', fromsubclass_=False, pretty_print=True):
        super(SessionStopReqType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ChargingSession is not None:
            namespaceprefix_ = self.ChargingSession_nsprefix_ + ':' if (UseCapturedNS_ and self.ChargingSession_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sChargingSession>%s</%sChargingSession>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ChargingSession), input_name='ChargingSession')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(SessionStopReqType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ChargingSession':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ChargingSession')
            value_ = self.gds_validate_string(value_, node, 'ChargingSession')
            self.ChargingSession = value_
            self.ChargingSession_nsprefix_ = child_.prefix
            # validate type chargingSessionType
            self.validate_chargingSessionType(self.ChargingSession)
        super(SessionStopReqType, self)._buildChildren(child_, node, nodeName_, True)
# end class SessionStopReqType


class SessionStopResType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, ResponseCode=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("SessionStopResType"), self).__init__( **kwargs_)
        self.ResponseCode = ResponseCode
        self.validate_responseCodeType(self.ResponseCode)
        self.ResponseCode_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SessionStopResType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SessionStopResType.subclass:
            return SessionStopResType.subclass(*args_, **kwargs_)
        else:
            return SessionStopResType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ResponseCode(self):
        return self.ResponseCode
    def set_ResponseCode(self, ResponseCode):
        self.ResponseCode = ResponseCode
    def validate_responseCodeType(self, value):
        result = True
        # Validate type responseCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['OK', 'OK_NewSessionEstablished', 'OK_OldSessionJoined', 'OK_CertificateExpiresSoon', 'FAILED', 'FAILED_SequenceError', 'FAILED_ServiceIDInvalid', 'FAILED_UnknownSession', 'FAILED_ServiceSelectionInvalid', 'FAILED_PaymentSelectionInvalid', 'FAILED_CertificateExpired', 'FAILED_SignatureError', 'FAILED_NoCertificateAvailable', 'FAILED_CertChainError', 'FAILED_ChallengeInvalid', 'FAILED_ContractCanceled', 'FAILED_WrongChargeParameter', 'FAILED_PowerDeliveryNotApplied', 'FAILED_TariffSelectionInvalid', 'FAILED_ChargingProfileInvalid', 'FAILED_MeteringSignatureNotValid', 'FAILED_NoChargeServiceSelected', 'FAILED_WrongEnergyTransferMode', 'FAILED_ContactorError', 'FAILED_CertificateNotAllowedAtThisEVSE', 'FAILED_CertificateRevoked']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on responseCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.ResponseCode is not None or
            super(SessionStopResType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='SessionStopResType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SessionStopResType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SessionStopResType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SessionStopResType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SessionStopResType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SessionStopResType'):
        super(SessionStopResType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SessionStopResType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='SessionStopResType', fromsubclass_=False, pretty_print=True):
        super(SessionStopResType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ResponseCode is not None:
            namespaceprefix_ = self.ResponseCode_nsprefix_ + ':' if (UseCapturedNS_ and self.ResponseCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sResponseCode>%s</%sResponseCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ResponseCode), input_name='ResponseCode')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(SessionStopResType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ResponseCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ResponseCode')
            value_ = self.gds_validate_string(value_, node, 'ResponseCode')
            self.ResponseCode = value_
            self.ResponseCode_nsprefix_ = child_.prefix
            # validate type responseCodeType
            self.validate_responseCodeType(self.ResponseCode)
        super(SessionStopResType, self)._buildChildren(child_, node, nodeName_, True)
# end class SessionStopResType


class CertificateUpdateReqType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, Id=None, ContractSignatureCertChain=None, eMAID=None, ListOfRootCertificateIDs=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("CertificateUpdateReqType"), self).__init__( **kwargs_)
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.ContractSignatureCertChain = ContractSignatureCertChain
        self.ContractSignatureCertChain_nsprefix_ = "ns6"
        self.eMAID = eMAID
        self.validate_eMAIDType(self.eMAID)
        self.eMAID_nsprefix_ = "ns6"
        self.ListOfRootCertificateIDs = ListOfRootCertificateIDs
        self.ListOfRootCertificateIDs_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CertificateUpdateReqType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CertificateUpdateReqType.subclass:
            return CertificateUpdateReqType.subclass(*args_, **kwargs_)
        else:
            return CertificateUpdateReqType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ContractSignatureCertChain(self):
        return self.ContractSignatureCertChain
    def set_ContractSignatureCertChain(self, ContractSignatureCertChain):
        self.ContractSignatureCertChain = ContractSignatureCertChain
    def get_eMAID(self):
        return self.eMAID
    def set_eMAID(self, eMAID):
        self.eMAID = eMAID
    def get_ListOfRootCertificateIDs(self):
        return self.ListOfRootCertificateIDs
    def set_ListOfRootCertificateIDs(self, ListOfRootCertificateIDs):
        self.ListOfRootCertificateIDs = ListOfRootCertificateIDs
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def validate_eMAIDType(self, value):
        result = True
        # Validate type eMAIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on eMAIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 14:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on eMAIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.ContractSignatureCertChain is not None or
            self.eMAID is not None or
            self.ListOfRootCertificateIDs is not None or
            super(CertificateUpdateReqType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='CertificateUpdateReqType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CertificateUpdateReqType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CertificateUpdateReqType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CertificateUpdateReqType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CertificateUpdateReqType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CertificateUpdateReqType'):
        super(CertificateUpdateReqType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CertificateUpdateReqType')
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='CertificateUpdateReqType', fromsubclass_=False, pretty_print=True):
        super(CertificateUpdateReqType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ContractSignatureCertChain is not None:
            namespaceprefix_ = self.ContractSignatureCertChain_nsprefix_ + ':' if (UseCapturedNS_ and self.ContractSignatureCertChain_nsprefix_) else ''
            self.ContractSignatureCertChain.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ContractSignatureCertChain', pretty_print=pretty_print)
        if self.eMAID is not None:
            namespaceprefix_ = self.eMAID_nsprefix_ + ':' if (UseCapturedNS_ and self.eMAID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%seMAID>%s</%seMAID>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.eMAID), input_name='eMAID')), namespaceprefix_ , eol_))
        if self.ListOfRootCertificateIDs is not None:
            namespaceprefix_ = self.ListOfRootCertificateIDs_nsprefix_ + ':' if (UseCapturedNS_ and self.ListOfRootCertificateIDs_nsprefix_) else ''
            self.ListOfRootCertificateIDs.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ListOfRootCertificateIDs', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
        super(CertificateUpdateReqType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ContractSignatureCertChain':
            obj_ = CertificateChainType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ContractSignatureCertChain = obj_
            obj_.original_tagname_ = 'ContractSignatureCertChain'
        elif nodeName_ == 'eMAID':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'eMAID')
            value_ = self.gds_validate_string(value_, node, 'eMAID')
            self.eMAID = value_
            self.eMAID_nsprefix_ = child_.prefix
            # validate type eMAIDType
            self.validate_eMAIDType(self.eMAID)
        elif nodeName_ == 'ListOfRootCertificateIDs':
            obj_ = ListOfRootCertificateIDsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ListOfRootCertificateIDs = obj_
            obj_.original_tagname_ = 'ListOfRootCertificateIDs'
        super(CertificateUpdateReqType, self)._buildChildren(child_, node, nodeName_, True)
# end class CertificateUpdateReqType


class CertificateUpdateResType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, ResponseCode=None, SAProvisioningCertificateChain=None, ContractSignatureCertChain=None, ContractSignatureEncryptedPrivateKey=None, DHpublickey=None, eMAID=None, RetryCounter=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("CertificateUpdateResType"), self).__init__( **kwargs_)
        self.ResponseCode = ResponseCode
        self.validate_responseCodeType(self.ResponseCode)
        self.ResponseCode_nsprefix_ = "ns6"
        self.SAProvisioningCertificateChain = SAProvisioningCertificateChain
        self.SAProvisioningCertificateChain_nsprefix_ = "ns6"
        self.ContractSignatureCertChain = ContractSignatureCertChain
        self.ContractSignatureCertChain_nsprefix_ = "ns6"
        self.ContractSignatureEncryptedPrivateKey = ContractSignatureEncryptedPrivateKey
        self.ContractSignatureEncryptedPrivateKey_nsprefix_ = "ns6"
        self.DHpublickey = DHpublickey
        self.DHpublickey_nsprefix_ = "ns6"
        self.eMAID = eMAID
        self.eMAID_nsprefix_ = "ns6"
        self.RetryCounter = RetryCounter
        self.RetryCounter_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CertificateUpdateResType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CertificateUpdateResType.subclass:
            return CertificateUpdateResType.subclass(*args_, **kwargs_)
        else:
            return CertificateUpdateResType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ResponseCode(self):
        return self.ResponseCode
    def set_ResponseCode(self, ResponseCode):
        self.ResponseCode = ResponseCode
    def get_SAProvisioningCertificateChain(self):
        return self.SAProvisioningCertificateChain
    def set_SAProvisioningCertificateChain(self, SAProvisioningCertificateChain):
        self.SAProvisioningCertificateChain = SAProvisioningCertificateChain
    def get_ContractSignatureCertChain(self):
        return self.ContractSignatureCertChain
    def set_ContractSignatureCertChain(self, ContractSignatureCertChain):
        self.ContractSignatureCertChain = ContractSignatureCertChain
    def get_ContractSignatureEncryptedPrivateKey(self):
        return self.ContractSignatureEncryptedPrivateKey
    def set_ContractSignatureEncryptedPrivateKey(self, ContractSignatureEncryptedPrivateKey):
        self.ContractSignatureEncryptedPrivateKey = ContractSignatureEncryptedPrivateKey
    def get_DHpublickey(self):
        return self.DHpublickey
    def set_DHpublickey(self, DHpublickey):
        self.DHpublickey = DHpublickey
    def get_eMAID(self):
        return self.eMAID
    def set_eMAID(self, eMAID):
        self.eMAID = eMAID
    def get_RetryCounter(self):
        return self.RetryCounter
    def set_RetryCounter(self, RetryCounter):
        self.RetryCounter = RetryCounter
    def validate_responseCodeType(self, value):
        result = True
        # Validate type responseCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['OK', 'OK_NewSessionEstablished', 'OK_OldSessionJoined', 'OK_CertificateExpiresSoon', 'FAILED', 'FAILED_SequenceError', 'FAILED_ServiceIDInvalid', 'FAILED_UnknownSession', 'FAILED_ServiceSelectionInvalid', 'FAILED_PaymentSelectionInvalid', 'FAILED_CertificateExpired', 'FAILED_SignatureError', 'FAILED_NoCertificateAvailable', 'FAILED_CertChainError', 'FAILED_ChallengeInvalid', 'FAILED_ContractCanceled', 'FAILED_WrongChargeParameter', 'FAILED_PowerDeliveryNotApplied', 'FAILED_TariffSelectionInvalid', 'FAILED_ChargingProfileInvalid', 'FAILED_MeteringSignatureNotValid', 'FAILED_NoChargeServiceSelected', 'FAILED_WrongEnergyTransferMode', 'FAILED_ContactorError', 'FAILED_CertificateNotAllowedAtThisEVSE', 'FAILED_CertificateRevoked']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on responseCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.ResponseCode is not None or
            self.SAProvisioningCertificateChain is not None or
            self.ContractSignatureCertChain is not None or
            self.ContractSignatureEncryptedPrivateKey is not None or
            self.DHpublickey is not None or
            self.eMAID is not None or
            self.RetryCounter is not None or
            super(CertificateUpdateResType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes"  xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='CertificateUpdateResType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CertificateUpdateResType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CertificateUpdateResType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CertificateUpdateResType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CertificateUpdateResType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CertificateUpdateResType'):
        super(CertificateUpdateResType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CertificateUpdateResType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes"  xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='CertificateUpdateResType', fromsubclass_=False, pretty_print=True):
        super(CertificateUpdateResType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ResponseCode is not None:
            namespaceprefix_ = self.ResponseCode_nsprefix_ + ':' if (UseCapturedNS_ and self.ResponseCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sResponseCode>%s</%sResponseCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ResponseCode), input_name='ResponseCode')), namespaceprefix_ , eol_))
        if self.SAProvisioningCertificateChain is not None:
            namespaceprefix_ = self.SAProvisioningCertificateChain_nsprefix_ + ':' if (UseCapturedNS_ and self.SAProvisioningCertificateChain_nsprefix_) else ''
            self.SAProvisioningCertificateChain.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SAProvisioningCertificateChain', pretty_print=pretty_print)
        if self.ContractSignatureCertChain is not None:
            namespaceprefix_ = self.ContractSignatureCertChain_nsprefix_ + ':' if (UseCapturedNS_ and self.ContractSignatureCertChain_nsprefix_) else ''
            self.ContractSignatureCertChain.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ContractSignatureCertChain', pretty_print=pretty_print)
        if self.ContractSignatureEncryptedPrivateKey is not None:
            namespaceprefix_ = self.ContractSignatureEncryptedPrivateKey_nsprefix_ + ':' if (UseCapturedNS_ and self.ContractSignatureEncryptedPrivateKey_nsprefix_) else ''
            self.ContractSignatureEncryptedPrivateKey.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ContractSignatureEncryptedPrivateKey', pretty_print=pretty_print)
        if self.DHpublickey is not None:
            namespaceprefix_ = self.DHpublickey_nsprefix_ + ':' if (UseCapturedNS_ and self.DHpublickey_nsprefix_) else ''
            self.DHpublickey.export(outfile, level, namespaceprefix_, namespacedef_='', name_='DHpublickey', pretty_print=pretty_print)
        if self.eMAID is not None:
            namespaceprefix_ = self.eMAID_nsprefix_ + ':' if (UseCapturedNS_ and self.eMAID_nsprefix_) else ''
            self.eMAID.export(outfile, level, namespaceprefix_, namespacedef_='', name_='eMAID', pretty_print=pretty_print)
        if self.RetryCounter is not None:
            namespaceprefix_ = self.RetryCounter_nsprefix_ + ':' if (UseCapturedNS_ and self.RetryCounter_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRetryCounter>%s</%sRetryCounter>%s' % (namespaceprefix_ , self.gds_format_integer(self.RetryCounter, input_name='RetryCounter'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(CertificateUpdateResType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ResponseCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ResponseCode')
            value_ = self.gds_validate_string(value_, node, 'ResponseCode')
            self.ResponseCode = value_
            self.ResponseCode_nsprefix_ = child_.prefix
            # validate type responseCodeType
            self.validate_responseCodeType(self.ResponseCode)
        elif nodeName_ == 'SAProvisioningCertificateChain':
            obj_ = CertificateChainType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SAProvisioningCertificateChain = obj_
            obj_.original_tagname_ = 'SAProvisioningCertificateChain'
        elif nodeName_ == 'ContractSignatureCertChain':
            obj_ = CertificateChainType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ContractSignatureCertChain = obj_
            obj_.original_tagname_ = 'ContractSignatureCertChain'
        elif nodeName_ == 'ContractSignatureEncryptedPrivateKey':
            obj_ = ContractSignatureEncryptedPrivateKeyType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ContractSignatureEncryptedPrivateKey = obj_
            obj_.original_tagname_ = 'ContractSignatureEncryptedPrivateKey'
        elif nodeName_ == 'DHpublickey':
            obj_ = DiffieHellmanPublickeyType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DHpublickey = obj_
            obj_.original_tagname_ = 'DHpublickey'
        elif nodeName_ == 'eMAID':
            obj_ = EMAIDType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.eMAID = obj_
            obj_.original_tagname_ = 'eMAID'
        elif nodeName_ == 'RetryCounter' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'RetryCounter')
            ival_ = self.gds_validate_integer(ival_, node, 'RetryCounter')
            self.RetryCounter = ival_
            self.RetryCounter_nsprefix_ = child_.prefix
        super(CertificateUpdateResType, self)._buildChildren(child_, node, nodeName_, True)
# end class CertificateUpdateResType


class CertificateInstallationReqType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, Id=None, OEMProvisioningCert=None, ListOfRootCertificateIDs=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("CertificateInstallationReqType"), self).__init__( **kwargs_)
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.OEMProvisioningCert = OEMProvisioningCert
        self.validate_certificateType(self.OEMProvisioningCert)
        self.OEMProvisioningCert_nsprefix_ = "ns6"
        self.ListOfRootCertificateIDs = ListOfRootCertificateIDs
        self.ListOfRootCertificateIDs_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CertificateInstallationReqType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CertificateInstallationReqType.subclass:
            return CertificateInstallationReqType.subclass(*args_, **kwargs_)
        else:
            return CertificateInstallationReqType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_OEMProvisioningCert(self):
        return self.OEMProvisioningCert
    def set_OEMProvisioningCert(self, OEMProvisioningCert):
        self.OEMProvisioningCert = OEMProvisioningCert
    def get_ListOfRootCertificateIDs(self):
        return self.ListOfRootCertificateIDs
    def set_ListOfRootCertificateIDs(self, ListOfRootCertificateIDs):
        self.ListOfRootCertificateIDs = ListOfRootCertificateIDs
    def get_Id(self):
        return self.Id
    def set_Id(self, Id):
        self.Id = Id
    def validate_certificateType(self, value):
        result = True
        # Validate type certificateType, a restriction on xs:base64Binary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if len(value) > 800:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on certificateType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.OEMProvisioningCert is not None or
            self.ListOfRootCertificateIDs is not None or
            super(CertificateInstallationReqType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='CertificateInstallationReqType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CertificateInstallationReqType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CertificateInstallationReqType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CertificateInstallationReqType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CertificateInstallationReqType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CertificateInstallationReqType'):
        super(CertificateInstallationReqType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CertificateInstallationReqType')
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='CertificateInstallationReqType', fromsubclass_=False, pretty_print=True):
        super(CertificateInstallationReqType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.OEMProvisioningCert is not None:
            namespaceprefix_ = self.OEMProvisioningCert_nsprefix_ + ':' if (UseCapturedNS_ and self.OEMProvisioningCert_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sOEMProvisioningCert>%s</%sOEMProvisioningCert>%s' % (namespaceprefix_ , self.gds_format_base64(self.OEMProvisioningCert, input_name='OEMProvisioningCert'), namespaceprefix_ , eol_))
        if self.ListOfRootCertificateIDs is not None:
            namespaceprefix_ = self.ListOfRootCertificateIDs_nsprefix_ + ':' if (UseCapturedNS_ and self.ListOfRootCertificateIDs_nsprefix_) else ''
            self.ListOfRootCertificateIDs.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ListOfRootCertificateIDs', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
        super(CertificateInstallationReqType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'OEMProvisioningCert':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'OEMProvisioningCert')
            else:
                bval_ = None
            self.OEMProvisioningCert = bval_
            self.OEMProvisioningCert_nsprefix_ = child_.prefix
            # validate type certificateType
            self.validate_certificateType(self.OEMProvisioningCert)
        elif nodeName_ == 'ListOfRootCertificateIDs':
            obj_ = ListOfRootCertificateIDsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ListOfRootCertificateIDs = obj_
            obj_.original_tagname_ = 'ListOfRootCertificateIDs'
        super(CertificateInstallationReqType, self)._buildChildren(child_, node, nodeName_, True)
# end class CertificateInstallationReqType


class CertificateInstallationResType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, ResponseCode=None, SAProvisioningCertificateChain=None, ContractSignatureCertChain=None, ContractSignatureEncryptedPrivateKey=None, DHpublickey=None, eMAID=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("CertificateInstallationResType"), self).__init__( **kwargs_)
        self.ResponseCode = ResponseCode
        self.validate_responseCodeType(self.ResponseCode)
        self.ResponseCode_nsprefix_ = "ns6"
        self.SAProvisioningCertificateChain = SAProvisioningCertificateChain
        self.SAProvisioningCertificateChain_nsprefix_ = "ns6"
        self.ContractSignatureCertChain = ContractSignatureCertChain
        self.ContractSignatureCertChain_nsprefix_ = "ns6"
        self.ContractSignatureEncryptedPrivateKey = ContractSignatureEncryptedPrivateKey
        self.ContractSignatureEncryptedPrivateKey_nsprefix_ = "ns6"
        self.DHpublickey = DHpublickey
        self.DHpublickey_nsprefix_ = "ns6"
        self.eMAID = eMAID
        self.eMAID_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CertificateInstallationResType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CertificateInstallationResType.subclass:
            return CertificateInstallationResType.subclass(*args_, **kwargs_)
        else:
            return CertificateInstallationResType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ResponseCode(self):
        return self.ResponseCode
    def set_ResponseCode(self, ResponseCode):
        self.ResponseCode = ResponseCode
    def get_SAProvisioningCertificateChain(self):
        return self.SAProvisioningCertificateChain
    def set_SAProvisioningCertificateChain(self, SAProvisioningCertificateChain):
        self.SAProvisioningCertificateChain = SAProvisioningCertificateChain
    def get_ContractSignatureCertChain(self):
        return self.ContractSignatureCertChain
    def set_ContractSignatureCertChain(self, ContractSignatureCertChain):
        self.ContractSignatureCertChain = ContractSignatureCertChain
    def get_ContractSignatureEncryptedPrivateKey(self):
        return self.ContractSignatureEncryptedPrivateKey
    def set_ContractSignatureEncryptedPrivateKey(self, ContractSignatureEncryptedPrivateKey):
        self.ContractSignatureEncryptedPrivateKey = ContractSignatureEncryptedPrivateKey
    def get_DHpublickey(self):
        return self.DHpublickey
    def set_DHpublickey(self, DHpublickey):
        self.DHpublickey = DHpublickey
    def get_eMAID(self):
        return self.eMAID
    def set_eMAID(self, eMAID):
        self.eMAID = eMAID
    def validate_responseCodeType(self, value):
        result = True
        # Validate type responseCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['OK', 'OK_NewSessionEstablished', 'OK_OldSessionJoined', 'OK_CertificateExpiresSoon', 'FAILED', 'FAILED_SequenceError', 'FAILED_ServiceIDInvalid', 'FAILED_UnknownSession', 'FAILED_ServiceSelectionInvalid', 'FAILED_PaymentSelectionInvalid', 'FAILED_CertificateExpired', 'FAILED_SignatureError', 'FAILED_NoCertificateAvailable', 'FAILED_CertChainError', 'FAILED_ChallengeInvalid', 'FAILED_ContractCanceled', 'FAILED_WrongChargeParameter', 'FAILED_PowerDeliveryNotApplied', 'FAILED_TariffSelectionInvalid', 'FAILED_ChargingProfileInvalid', 'FAILED_MeteringSignatureNotValid', 'FAILED_NoChargeServiceSelected', 'FAILED_WrongEnergyTransferMode', 'FAILED_ContactorError', 'FAILED_CertificateNotAllowedAtThisEVSE', 'FAILED_CertificateRevoked']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on responseCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.ResponseCode is not None or
            self.SAProvisioningCertificateChain is not None or
            self.ContractSignatureCertChain is not None or
            self.ContractSignatureEncryptedPrivateKey is not None or
            self.DHpublickey is not None or
            self.eMAID is not None or
            super(CertificateInstallationResType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='CertificateInstallationResType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CertificateInstallationResType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CertificateInstallationResType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CertificateInstallationResType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CertificateInstallationResType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CertificateInstallationResType'):
        super(CertificateInstallationResType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CertificateInstallationResType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='CertificateInstallationResType', fromsubclass_=False, pretty_print=True):
        super(CertificateInstallationResType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ResponseCode is not None:
            namespaceprefix_ = self.ResponseCode_nsprefix_ + ':' if (UseCapturedNS_ and self.ResponseCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sResponseCode>%s</%sResponseCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ResponseCode), input_name='ResponseCode')), namespaceprefix_ , eol_))
        if self.SAProvisioningCertificateChain is not None:
            namespaceprefix_ = self.SAProvisioningCertificateChain_nsprefix_ + ':' if (UseCapturedNS_ and self.SAProvisioningCertificateChain_nsprefix_) else ''
            self.SAProvisioningCertificateChain.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SAProvisioningCertificateChain', pretty_print=pretty_print)
        if self.ContractSignatureCertChain is not None:
            namespaceprefix_ = self.ContractSignatureCertChain_nsprefix_ + ':' if (UseCapturedNS_ and self.ContractSignatureCertChain_nsprefix_) else ''
            self.ContractSignatureCertChain.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ContractSignatureCertChain', pretty_print=pretty_print)
        if self.ContractSignatureEncryptedPrivateKey is not None:
            namespaceprefix_ = self.ContractSignatureEncryptedPrivateKey_nsprefix_ + ':' if (UseCapturedNS_ and self.ContractSignatureEncryptedPrivateKey_nsprefix_) else ''
            self.ContractSignatureEncryptedPrivateKey.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ContractSignatureEncryptedPrivateKey', pretty_print=pretty_print)
        if self.DHpublickey is not None:
            namespaceprefix_ = self.DHpublickey_nsprefix_ + ':' if (UseCapturedNS_ and self.DHpublickey_nsprefix_) else ''
            self.DHpublickey.export(outfile, level, namespaceprefix_, namespacedef_='', name_='DHpublickey', pretty_print=pretty_print)
        if self.eMAID is not None:
            namespaceprefix_ = self.eMAID_nsprefix_ + ':' if (UseCapturedNS_ and self.eMAID_nsprefix_) else ''
            self.eMAID.export(outfile, level, namespaceprefix_, namespacedef_='', name_='eMAID', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(CertificateInstallationResType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ResponseCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ResponseCode')
            value_ = self.gds_validate_string(value_, node, 'ResponseCode')
            self.ResponseCode = value_
            self.ResponseCode_nsprefix_ = child_.prefix
            # validate type responseCodeType
            self.validate_responseCodeType(self.ResponseCode)
        elif nodeName_ == 'SAProvisioningCertificateChain':
            obj_ = CertificateChainType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SAProvisioningCertificateChain = obj_
            obj_.original_tagname_ = 'SAProvisioningCertificateChain'
        elif nodeName_ == 'ContractSignatureCertChain':
            obj_ = CertificateChainType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ContractSignatureCertChain = obj_
            obj_.original_tagname_ = 'ContractSignatureCertChain'
        elif nodeName_ == 'ContractSignatureEncryptedPrivateKey':
            obj_ = ContractSignatureEncryptedPrivateKeyType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ContractSignatureEncryptedPrivateKey = obj_
            obj_.original_tagname_ = 'ContractSignatureEncryptedPrivateKey'
        elif nodeName_ == 'DHpublickey':
            obj_ = DiffieHellmanPublickeyType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DHpublickey = obj_
            obj_.original_tagname_ = 'DHpublickey'
        elif nodeName_ == 'eMAID':
            obj_ = EMAIDType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.eMAID = obj_
            obj_.original_tagname_ = 'eMAID'
        super(CertificateInstallationResType, self)._buildChildren(child_, node, nodeName_, True)
# end class CertificateInstallationResType


class ChargingStatusReqType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("ChargingStatusReqType"), self).__init__( **kwargs_)
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ChargingStatusReqType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ChargingStatusReqType.subclass:
            return ChargingStatusReqType.subclass(*args_, **kwargs_)
        else:
            return ChargingStatusReqType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def _hasContent(self):
        if (
            super(ChargingStatusReqType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody"', name_='ChargingStatusReqType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ChargingStatusReqType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ChargingStatusReqType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ChargingStatusReqType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ChargingStatusReqType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ChargingStatusReqType'):
        super(ChargingStatusReqType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ChargingStatusReqType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody"', name_='ChargingStatusReqType', fromsubclass_=False, pretty_print=True):
        super(ChargingStatusReqType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(ChargingStatusReqType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(ChargingStatusReqType, self)._buildChildren(child_, node, nodeName_, True)
        pass
# end class ChargingStatusReqType


class ChargingStatusResType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, ResponseCode=None, EVSEID=None, SAScheduleTupleID=None, EVSEMaxCurrent=None, MeterInfo=None, ReceiptRequired=None, AC_EVSEStatus=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("ChargingStatusResType"), self).__init__( **kwargs_)
        self.ResponseCode = ResponseCode
        self.validate_responseCodeType(self.ResponseCode)
        self.ResponseCode_nsprefix_ = "ns6"
        self.EVSEID = EVSEID
        self.validate_evseIDType(self.EVSEID)
        self.EVSEID_nsprefix_ = "ns6"
        self.SAScheduleTupleID = SAScheduleTupleID
        self.validate_SAIDType(self.SAScheduleTupleID)
        self.SAScheduleTupleID_nsprefix_ = "ns6"
        self.EVSEMaxCurrent = EVSEMaxCurrent
        self.EVSEMaxCurrent_nsprefix_ = "ns6"
        self.MeterInfo = MeterInfo
        self.MeterInfo_nsprefix_ = "ns6"
        self.ReceiptRequired = ReceiptRequired
        self.ReceiptRequired_nsprefix_ = None
        self.AC_EVSEStatus = AC_EVSEStatus
        self.AC_EVSEStatus_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ChargingStatusResType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ChargingStatusResType.subclass:
            return ChargingStatusResType.subclass(*args_, **kwargs_)
        else:
            return ChargingStatusResType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ResponseCode(self):
        return self.ResponseCode
    def set_ResponseCode(self, ResponseCode):
        self.ResponseCode = ResponseCode
    def get_EVSEID(self):
        return self.EVSEID
    def set_EVSEID(self, EVSEID):
        self.EVSEID = EVSEID
    def get_SAScheduleTupleID(self):
        return self.SAScheduleTupleID
    def set_SAScheduleTupleID(self, SAScheduleTupleID):
        self.SAScheduleTupleID = SAScheduleTupleID
    def get_EVSEMaxCurrent(self):
        return self.EVSEMaxCurrent
    def set_EVSEMaxCurrent(self, EVSEMaxCurrent):
        self.EVSEMaxCurrent = EVSEMaxCurrent
    def get_MeterInfo(self):
        return self.MeterInfo
    def set_MeterInfo(self, MeterInfo):
        self.MeterInfo = MeterInfo
    def get_ReceiptRequired(self):
        return self.ReceiptRequired
    def set_ReceiptRequired(self, ReceiptRequired):
        self.ReceiptRequired = ReceiptRequired
    def get_AC_EVSEStatus(self):
        return self.AC_EVSEStatus
    def set_AC_EVSEStatus(self, AC_EVSEStatus):
        self.AC_EVSEStatus = AC_EVSEStatus
    def validate_responseCodeType(self, value):
        result = True
        # Validate type responseCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['OK', 'OK_NewSessionEstablished', 'OK_OldSessionJoined', 'OK_CertificateExpiresSoon', 'FAILED', 'FAILED_SequenceError', 'FAILED_ServiceIDInvalid', 'FAILED_UnknownSession', 'FAILED_ServiceSelectionInvalid', 'FAILED_PaymentSelectionInvalid', 'FAILED_CertificateExpired', 'FAILED_SignatureError', 'FAILED_NoCertificateAvailable', 'FAILED_CertChainError', 'FAILED_ChallengeInvalid', 'FAILED_ContractCanceled', 'FAILED_WrongChargeParameter', 'FAILED_PowerDeliveryNotApplied', 'FAILED_TariffSelectionInvalid', 'FAILED_ChargingProfileInvalid', 'FAILED_MeteringSignatureNotValid', 'FAILED_NoChargeServiceSelected', 'FAILED_WrongEnergyTransferMode', 'FAILED_ContactorError', 'FAILED_CertificateNotAllowedAtThisEVSE', 'FAILED_CertificateRevoked']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on responseCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_evseIDType(self, value):
        result = True
        # Validate type evseIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 37:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on evseIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on evseIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_SAIDType(self, value):
        result = True
        # Validate type SAIDType, a restriction on xs:unsignedByte.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on SAIDType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on SAIDType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.ResponseCode is not None or
            self.EVSEID is not None or
            self.SAScheduleTupleID is not None or
            self.EVSEMaxCurrent is not None or
            self.MeterInfo is not None or
            self.ReceiptRequired is not None or
            self.AC_EVSEStatus is not None or
            super(ChargingStatusResType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes"  xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='ChargingStatusResType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ChargingStatusResType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ChargingStatusResType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ChargingStatusResType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ChargingStatusResType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ChargingStatusResType'):
        super(ChargingStatusResType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ChargingStatusResType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes"  xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='ChargingStatusResType', fromsubclass_=False, pretty_print=True):
        super(ChargingStatusResType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ResponseCode is not None:
            namespaceprefix_ = self.ResponseCode_nsprefix_ + ':' if (UseCapturedNS_ and self.ResponseCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sResponseCode>%s</%sResponseCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ResponseCode), input_name='ResponseCode')), namespaceprefix_ , eol_))
        if self.EVSEID is not None:
            namespaceprefix_ = self.EVSEID_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEVSEID>%s</%sEVSEID>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.EVSEID), input_name='EVSEID')), namespaceprefix_ , eol_))
        if self.SAScheduleTupleID is not None:
            namespaceprefix_ = self.SAScheduleTupleID_nsprefix_ + ':' if (UseCapturedNS_ and self.SAScheduleTupleID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSAScheduleTupleID>%s</%sSAScheduleTupleID>%s' % (namespaceprefix_ , self.gds_format_integer(self.SAScheduleTupleID, input_name='SAScheduleTupleID'), namespaceprefix_ , eol_))
        if self.EVSEMaxCurrent is not None:
            namespaceprefix_ = self.EVSEMaxCurrent_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEMaxCurrent_nsprefix_) else ''
            self.EVSEMaxCurrent.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVSEMaxCurrent', pretty_print=pretty_print)
        if self.MeterInfo is not None:
            namespaceprefix_ = self.MeterInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.MeterInfo_nsprefix_) else ''
            self.MeterInfo.export(outfile, level, namespaceprefix_, namespacedef_='', name_='MeterInfo', pretty_print=pretty_print)
        if self.ReceiptRequired is not None:
            namespaceprefix_ = self.ReceiptRequired_nsprefix_ + ':' if (UseCapturedNS_ and self.ReceiptRequired_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sReceiptRequired>%s</%sReceiptRequired>%s' % (namespaceprefix_ , self.gds_format_boolean(self.ReceiptRequired, input_name='ReceiptRequired'), namespaceprefix_ , eol_))
        if self.AC_EVSEStatus is not None:
            namespaceprefix_ = self.AC_EVSEStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.AC_EVSEStatus_nsprefix_) else ''
            self.AC_EVSEStatus.export(outfile, level, namespaceprefix_, namespacedef_='', name_='AC_EVSEStatus', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(ChargingStatusResType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ResponseCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ResponseCode')
            value_ = self.gds_validate_string(value_, node, 'ResponseCode')
            self.ResponseCode = value_
            self.ResponseCode_nsprefix_ = child_.prefix
            # validate type responseCodeType
            self.validate_responseCodeType(self.ResponseCode)
        elif nodeName_ == 'EVSEID':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'EVSEID')
            value_ = self.gds_validate_string(value_, node, 'EVSEID')
            self.EVSEID = value_
            self.EVSEID_nsprefix_ = child_.prefix
            # validate type evseIDType
            self.validate_evseIDType(self.EVSEID)
        elif nodeName_ == 'SAScheduleTupleID' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'SAScheduleTupleID')
            ival_ = self.gds_validate_integer(ival_, node, 'SAScheduleTupleID')
            self.SAScheduleTupleID = ival_
            self.SAScheduleTupleID_nsprefix_ = child_.prefix
            # validate type SAIDType
            self.validate_SAIDType(self.SAScheduleTupleID)
        elif nodeName_ == 'EVSEMaxCurrent':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSEMaxCurrent = obj_
            obj_.original_tagname_ = 'EVSEMaxCurrent'
        elif nodeName_ == 'MeterInfo':
            obj_ = MeterInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.MeterInfo = obj_
            obj_.original_tagname_ = 'MeterInfo'
        elif nodeName_ == 'ReceiptRequired':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'ReceiptRequired')
            ival_ = self.gds_validate_boolean(ival_, node, 'ReceiptRequired')
            self.ReceiptRequired = ival_
            self.ReceiptRequired_nsprefix_ = child_.prefix
        elif nodeName_ == 'AC_EVSEStatus':
            obj_ = AC_EVSEStatusType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.AC_EVSEStatus = obj_
            obj_.original_tagname_ = 'AC_EVSEStatus'
        super(ChargingStatusResType, self)._buildChildren(child_, node, nodeName_, True)
# end class ChargingStatusResType


class CableCheckReqType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, DC_EVStatus=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("CableCheckReqType"), self).__init__( **kwargs_)
        self.DC_EVStatus = DC_EVStatus
        self.DC_EVStatus_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CableCheckReqType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CableCheckReqType.subclass:
            return CableCheckReqType.subclass(*args_, **kwargs_)
        else:
            return CableCheckReqType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_DC_EVStatus(self):
        return self.DC_EVStatus
    def set_DC_EVStatus(self, DC_EVStatus):
        self.DC_EVStatus = DC_EVStatus
    def _hasContent(self):
        if (
            self.DC_EVStatus is not None or
            super(CableCheckReqType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='CableCheckReqType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CableCheckReqType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CableCheckReqType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CableCheckReqType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CableCheckReqType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CableCheckReqType'):
        super(CableCheckReqType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CableCheckReqType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='CableCheckReqType', fromsubclass_=False, pretty_print=True):
        super(CableCheckReqType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.DC_EVStatus is not None:
            namespaceprefix_ = self.DC_EVStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.DC_EVStatus_nsprefix_) else ''
            self.DC_EVStatus.export(outfile, level, namespaceprefix_, namespacedef_='', name_='DC_EVStatus', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(CableCheckReqType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'DC_EVStatus':
            obj_ = DC_EVStatusType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DC_EVStatus = obj_
            obj_.original_tagname_ = 'DC_EVStatus'
        super(CableCheckReqType, self)._buildChildren(child_, node, nodeName_, True)
# end class CableCheckReqType


class CableCheckResType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, ResponseCode=None, DC_EVSEStatus=None, EVSEProcessing=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("CableCheckResType"), self).__init__( **kwargs_)
        self.ResponseCode = ResponseCode
        self.validate_responseCodeType(self.ResponseCode)
        self.ResponseCode_nsprefix_ = "ns6"
        self.DC_EVSEStatus = DC_EVSEStatus
        self.DC_EVSEStatus_nsprefix_ = "ns6"
        self.EVSEProcessing = EVSEProcessing
        self.validate_EVSEProcessingType(self.EVSEProcessing)
        self.EVSEProcessing_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CableCheckResType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CableCheckResType.subclass:
            return CableCheckResType.subclass(*args_, **kwargs_)
        else:
            return CableCheckResType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ResponseCode(self):
        return self.ResponseCode
    def set_ResponseCode(self, ResponseCode):
        self.ResponseCode = ResponseCode
    def get_DC_EVSEStatus(self):
        return self.DC_EVSEStatus
    def set_DC_EVSEStatus(self, DC_EVSEStatus):
        self.DC_EVSEStatus = DC_EVSEStatus
    def get_EVSEProcessing(self):
        return self.EVSEProcessing
    def set_EVSEProcessing(self, EVSEProcessing):
        self.EVSEProcessing = EVSEProcessing
    def validate_responseCodeType(self, value):
        result = True
        # Validate type responseCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['OK', 'OK_NewSessionEstablished', 'OK_OldSessionJoined', 'OK_CertificateExpiresSoon', 'FAILED', 'FAILED_SequenceError', 'FAILED_ServiceIDInvalid', 'FAILED_UnknownSession', 'FAILED_ServiceSelectionInvalid', 'FAILED_PaymentSelectionInvalid', 'FAILED_CertificateExpired', 'FAILED_SignatureError', 'FAILED_NoCertificateAvailable', 'FAILED_CertChainError', 'FAILED_ChallengeInvalid', 'FAILED_ContractCanceled', 'FAILED_WrongChargeParameter', 'FAILED_PowerDeliveryNotApplied', 'FAILED_TariffSelectionInvalid', 'FAILED_ChargingProfileInvalid', 'FAILED_MeteringSignatureNotValid', 'FAILED_NoChargeServiceSelected', 'FAILED_WrongEnergyTransferMode', 'FAILED_ContactorError', 'FAILED_CertificateNotAllowedAtThisEVSE', 'FAILED_CertificateRevoked']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on responseCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_EVSEProcessingType(self, value):
        result = True
        # Validate type EVSEProcessingType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Finished', 'Ongoing', 'Ongoing_WaitingForCustomerInteraction']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on EVSEProcessingType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.ResponseCode is not None or
            self.DC_EVSEStatus is not None or
            self.EVSEProcessing is not None or
            super(CableCheckResType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='CableCheckResType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CableCheckResType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CableCheckResType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CableCheckResType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CableCheckResType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CableCheckResType'):
        super(CableCheckResType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CableCheckResType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='CableCheckResType', fromsubclass_=False, pretty_print=True):
        super(CableCheckResType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ResponseCode is not None:
            namespaceprefix_ = self.ResponseCode_nsprefix_ + ':' if (UseCapturedNS_ and self.ResponseCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sResponseCode>%s</%sResponseCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ResponseCode), input_name='ResponseCode')), namespaceprefix_ , eol_))
        if self.DC_EVSEStatus is not None:
            namespaceprefix_ = self.DC_EVSEStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.DC_EVSEStatus_nsprefix_) else ''
            self.DC_EVSEStatus.export(outfile, level, namespaceprefix_, namespacedef_='', name_='DC_EVSEStatus', pretty_print=pretty_print)
        if self.EVSEProcessing is not None:
            namespaceprefix_ = self.EVSEProcessing_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEProcessing_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEVSEProcessing>%s</%sEVSEProcessing>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.EVSEProcessing), input_name='EVSEProcessing')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(CableCheckResType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ResponseCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ResponseCode')
            value_ = self.gds_validate_string(value_, node, 'ResponseCode')
            self.ResponseCode = value_
            self.ResponseCode_nsprefix_ = child_.prefix
            # validate type responseCodeType
            self.validate_responseCodeType(self.ResponseCode)
        elif nodeName_ == 'DC_EVSEStatus':
            obj_ = DC_EVSEStatusType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DC_EVSEStatus = obj_
            obj_.original_tagname_ = 'DC_EVSEStatus'
        elif nodeName_ == 'EVSEProcessing':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'EVSEProcessing')
            value_ = self.gds_validate_string(value_, node, 'EVSEProcessing')
            self.EVSEProcessing = value_
            self.EVSEProcessing_nsprefix_ = child_.prefix
            # validate type EVSEProcessingType
            self.validate_EVSEProcessingType(self.EVSEProcessing)
        super(CableCheckResType, self)._buildChildren(child_, node, nodeName_, True)
# end class CableCheckResType


class PreChargeReqType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, DC_EVStatus=None, EVTargetVoltage=None, EVTargetCurrent=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("PreChargeReqType"), self).__init__( **kwargs_)
        self.DC_EVStatus = DC_EVStatus
        self.DC_EVStatus_nsprefix_ = "ns6"
        self.EVTargetVoltage = EVTargetVoltage
        self.EVTargetVoltage_nsprefix_ = "ns6"
        self.EVTargetCurrent = EVTargetCurrent
        self.EVTargetCurrent_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PreChargeReqType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PreChargeReqType.subclass:
            return PreChargeReqType.subclass(*args_, **kwargs_)
        else:
            return PreChargeReqType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_DC_EVStatus(self):
        return self.DC_EVStatus
    def set_DC_EVStatus(self, DC_EVStatus):
        self.DC_EVStatus = DC_EVStatus
    def get_EVTargetVoltage(self):
        return self.EVTargetVoltage
    def set_EVTargetVoltage(self, EVTargetVoltage):
        self.EVTargetVoltage = EVTargetVoltage
    def get_EVTargetCurrent(self):
        return self.EVTargetCurrent
    def set_EVTargetCurrent(self, EVTargetCurrent):
        self.EVTargetCurrent = EVTargetCurrent
    def _hasContent(self):
        if (
            self.DC_EVStatus is not None or
            self.EVTargetVoltage is not None or
            self.EVTargetCurrent is not None or
            super(PreChargeReqType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='PreChargeReqType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PreChargeReqType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PreChargeReqType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PreChargeReqType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PreChargeReqType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PreChargeReqType'):
        super(PreChargeReqType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PreChargeReqType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='PreChargeReqType', fromsubclass_=False, pretty_print=True):
        super(PreChargeReqType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.DC_EVStatus is not None:
            namespaceprefix_ = self.DC_EVStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.DC_EVStatus_nsprefix_) else ''
            self.DC_EVStatus.export(outfile, level, namespaceprefix_, namespacedef_='', name_='DC_EVStatus', pretty_print=pretty_print)
        if self.EVTargetVoltage is not None:
            namespaceprefix_ = self.EVTargetVoltage_nsprefix_ + ':' if (UseCapturedNS_ and self.EVTargetVoltage_nsprefix_) else ''
            self.EVTargetVoltage.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVTargetVoltage', pretty_print=pretty_print)
        if self.EVTargetCurrent is not None:
            namespaceprefix_ = self.EVTargetCurrent_nsprefix_ + ':' if (UseCapturedNS_ and self.EVTargetCurrent_nsprefix_) else ''
            self.EVTargetCurrent.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVTargetCurrent', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(PreChargeReqType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'DC_EVStatus':
            obj_ = DC_EVStatusType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DC_EVStatus = obj_
            obj_.original_tagname_ = 'DC_EVStatus'
        elif nodeName_ == 'EVTargetVoltage':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVTargetVoltage = obj_
            obj_.original_tagname_ = 'EVTargetVoltage'
        elif nodeName_ == 'EVTargetCurrent':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVTargetCurrent = obj_
            obj_.original_tagname_ = 'EVTargetCurrent'
        super(PreChargeReqType, self)._buildChildren(child_, node, nodeName_, True)
# end class PreChargeReqType


class PreChargeResType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, ResponseCode=None, DC_EVSEStatus=None, EVSEPresentVoltage=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("PreChargeResType"), self).__init__( **kwargs_)
        self.ResponseCode = ResponseCode
        self.validate_responseCodeType(self.ResponseCode)
        self.ResponseCode_nsprefix_ = "ns6"
        self.DC_EVSEStatus = DC_EVSEStatus
        self.DC_EVSEStatus_nsprefix_ = "ns6"
        self.EVSEPresentVoltage = EVSEPresentVoltage
        self.EVSEPresentVoltage_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PreChargeResType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PreChargeResType.subclass:
            return PreChargeResType.subclass(*args_, **kwargs_)
        else:
            return PreChargeResType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ResponseCode(self):
        return self.ResponseCode
    def set_ResponseCode(self, ResponseCode):
        self.ResponseCode = ResponseCode
    def get_DC_EVSEStatus(self):
        return self.DC_EVSEStatus
    def set_DC_EVSEStatus(self, DC_EVSEStatus):
        self.DC_EVSEStatus = DC_EVSEStatus
    def get_EVSEPresentVoltage(self):
        return self.EVSEPresentVoltage
    def set_EVSEPresentVoltage(self, EVSEPresentVoltage):
        self.EVSEPresentVoltage = EVSEPresentVoltage
    def validate_responseCodeType(self, value):
        result = True
        # Validate type responseCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['OK', 'OK_NewSessionEstablished', 'OK_OldSessionJoined', 'OK_CertificateExpiresSoon', 'FAILED', 'FAILED_SequenceError', 'FAILED_ServiceIDInvalid', 'FAILED_UnknownSession', 'FAILED_ServiceSelectionInvalid', 'FAILED_PaymentSelectionInvalid', 'FAILED_CertificateExpired', 'FAILED_SignatureError', 'FAILED_NoCertificateAvailable', 'FAILED_CertChainError', 'FAILED_ChallengeInvalid', 'FAILED_ContractCanceled', 'FAILED_WrongChargeParameter', 'FAILED_PowerDeliveryNotApplied', 'FAILED_TariffSelectionInvalid', 'FAILED_ChargingProfileInvalid', 'FAILED_MeteringSignatureNotValid', 'FAILED_NoChargeServiceSelected', 'FAILED_WrongEnergyTransferMode', 'FAILED_ContactorError', 'FAILED_CertificateNotAllowedAtThisEVSE', 'FAILED_CertificateRevoked']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on responseCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.ResponseCode is not None or
            self.DC_EVSEStatus is not None or
            self.EVSEPresentVoltage is not None or
            super(PreChargeResType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='PreChargeResType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PreChargeResType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PreChargeResType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PreChargeResType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PreChargeResType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PreChargeResType'):
        super(PreChargeResType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PreChargeResType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='PreChargeResType', fromsubclass_=False, pretty_print=True):
        super(PreChargeResType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ResponseCode is not None:
            namespaceprefix_ = self.ResponseCode_nsprefix_ + ':' if (UseCapturedNS_ and self.ResponseCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sResponseCode>%s</%sResponseCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ResponseCode), input_name='ResponseCode')), namespaceprefix_ , eol_))
        if self.DC_EVSEStatus is not None:
            namespaceprefix_ = self.DC_EVSEStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.DC_EVSEStatus_nsprefix_) else ''
            self.DC_EVSEStatus.export(outfile, level, namespaceprefix_, namespacedef_='', name_='DC_EVSEStatus', pretty_print=pretty_print)
        if self.EVSEPresentVoltage is not None:
            namespaceprefix_ = self.EVSEPresentVoltage_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEPresentVoltage_nsprefix_) else ''
            self.EVSEPresentVoltage.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVSEPresentVoltage', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(PreChargeResType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ResponseCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ResponseCode')
            value_ = self.gds_validate_string(value_, node, 'ResponseCode')
            self.ResponseCode = value_
            self.ResponseCode_nsprefix_ = child_.prefix
            # validate type responseCodeType
            self.validate_responseCodeType(self.ResponseCode)
        elif nodeName_ == 'DC_EVSEStatus':
            obj_ = DC_EVSEStatusType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DC_EVSEStatus = obj_
            obj_.original_tagname_ = 'DC_EVSEStatus'
        elif nodeName_ == 'EVSEPresentVoltage':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSEPresentVoltage = obj_
            obj_.original_tagname_ = 'EVSEPresentVoltage'
        super(PreChargeResType, self)._buildChildren(child_, node, nodeName_, True)
# end class PreChargeResType


class CurrentDemandReqType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, DC_EVStatus=None, EVTargetCurrent=None, EVMaximumVoltageLimit=None, EVMaximumCurrentLimit=None, EVMaximumPowerLimit=None, BulkChargingComplete=None, ChargingComplete=None, RemainingTimeToFullSoC=None, RemainingTimeToBulkSoC=None, EVTargetVoltage=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("CurrentDemandReqType"), self).__init__( **kwargs_)
        self.DC_EVStatus = DC_EVStatus
        self.DC_EVStatus_nsprefix_ = "ns6"
        self.EVTargetCurrent = EVTargetCurrent
        self.EVTargetCurrent_nsprefix_ = "ns6"
        self.EVMaximumVoltageLimit = EVMaximumVoltageLimit
        self.EVMaximumVoltageLimit_nsprefix_ = "ns6"
        self.EVMaximumCurrentLimit = EVMaximumCurrentLimit
        self.EVMaximumCurrentLimit_nsprefix_ = "ns6"
        self.EVMaximumPowerLimit = EVMaximumPowerLimit
        self.EVMaximumPowerLimit_nsprefix_ = "ns6"
        self.BulkChargingComplete = BulkChargingComplete
        self.BulkChargingComplete_nsprefix_ = None
        self.ChargingComplete = ChargingComplete
        self.ChargingComplete_nsprefix_ = None
        self.RemainingTimeToFullSoC = RemainingTimeToFullSoC
        self.RemainingTimeToFullSoC_nsprefix_ = "ns6"
        self.RemainingTimeToBulkSoC = RemainingTimeToBulkSoC
        self.RemainingTimeToBulkSoC_nsprefix_ = "ns6"
        self.EVTargetVoltage = EVTargetVoltage
        self.EVTargetVoltage_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CurrentDemandReqType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CurrentDemandReqType.subclass:
            return CurrentDemandReqType.subclass(*args_, **kwargs_)
        else:
            return CurrentDemandReqType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_DC_EVStatus(self):
        return self.DC_EVStatus
    def set_DC_EVStatus(self, DC_EVStatus):
        self.DC_EVStatus = DC_EVStatus
    def get_EVTargetCurrent(self):
        return self.EVTargetCurrent
    def set_EVTargetCurrent(self, EVTargetCurrent):
        self.EVTargetCurrent = EVTargetCurrent
    def get_EVMaximumVoltageLimit(self):
        return self.EVMaximumVoltageLimit
    def set_EVMaximumVoltageLimit(self, EVMaximumVoltageLimit):
        self.EVMaximumVoltageLimit = EVMaximumVoltageLimit
    def get_EVMaximumCurrentLimit(self):
        return self.EVMaximumCurrentLimit
    def set_EVMaximumCurrentLimit(self, EVMaximumCurrentLimit):
        self.EVMaximumCurrentLimit = EVMaximumCurrentLimit
    def get_EVMaximumPowerLimit(self):
        return self.EVMaximumPowerLimit
    def set_EVMaximumPowerLimit(self, EVMaximumPowerLimit):
        self.EVMaximumPowerLimit = EVMaximumPowerLimit
    def get_BulkChargingComplete(self):
        return self.BulkChargingComplete
    def set_BulkChargingComplete(self, BulkChargingComplete):
        self.BulkChargingComplete = BulkChargingComplete
    def get_ChargingComplete(self):
        return self.ChargingComplete
    def set_ChargingComplete(self, ChargingComplete):
        self.ChargingComplete = ChargingComplete
    def get_RemainingTimeToFullSoC(self):
        return self.RemainingTimeToFullSoC
    def set_RemainingTimeToFullSoC(self, RemainingTimeToFullSoC):
        self.RemainingTimeToFullSoC = RemainingTimeToFullSoC
    def get_RemainingTimeToBulkSoC(self):
        return self.RemainingTimeToBulkSoC
    def set_RemainingTimeToBulkSoC(self, RemainingTimeToBulkSoC):
        self.RemainingTimeToBulkSoC = RemainingTimeToBulkSoC
    def get_EVTargetVoltage(self):
        return self.EVTargetVoltage
    def set_EVTargetVoltage(self, EVTargetVoltage):
        self.EVTargetVoltage = EVTargetVoltage
    def _hasContent(self):
        if (
            self.DC_EVStatus is not None or
            self.EVTargetCurrent is not None or
            self.EVMaximumVoltageLimit is not None or
            self.EVMaximumCurrentLimit is not None or
            self.EVMaximumPowerLimit is not None or
            self.BulkChargingComplete is not None or
            self.ChargingComplete is not None or
            self.RemainingTimeToFullSoC is not None or
            self.RemainingTimeToBulkSoC is not None or
            self.EVTargetVoltage is not None or
            super(CurrentDemandReqType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes"  xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='CurrentDemandReqType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CurrentDemandReqType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CurrentDemandReqType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CurrentDemandReqType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CurrentDemandReqType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CurrentDemandReqType'):
        super(CurrentDemandReqType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CurrentDemandReqType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes"  xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='CurrentDemandReqType', fromsubclass_=False, pretty_print=True):
        super(CurrentDemandReqType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.DC_EVStatus is not None:
            namespaceprefix_ = self.DC_EVStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.DC_EVStatus_nsprefix_) else ''
            self.DC_EVStatus.export(outfile, level, namespaceprefix_, namespacedef_='', name_='DC_EVStatus', pretty_print=pretty_print)
        if self.EVTargetCurrent is not None:
            namespaceprefix_ = self.EVTargetCurrent_nsprefix_ + ':' if (UseCapturedNS_ and self.EVTargetCurrent_nsprefix_) else ''
            self.EVTargetCurrent.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVTargetCurrent', pretty_print=pretty_print)
        if self.EVMaximumVoltageLimit is not None:
            namespaceprefix_ = self.EVMaximumVoltageLimit_nsprefix_ + ':' if (UseCapturedNS_ and self.EVMaximumVoltageLimit_nsprefix_) else ''
            self.EVMaximumVoltageLimit.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVMaximumVoltageLimit', pretty_print=pretty_print)
        if self.EVMaximumCurrentLimit is not None:
            namespaceprefix_ = self.EVMaximumCurrentLimit_nsprefix_ + ':' if (UseCapturedNS_ and self.EVMaximumCurrentLimit_nsprefix_) else ''
            self.EVMaximumCurrentLimit.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVMaximumCurrentLimit', pretty_print=pretty_print)
        if self.EVMaximumPowerLimit is not None:
            namespaceprefix_ = self.EVMaximumPowerLimit_nsprefix_ + ':' if (UseCapturedNS_ and self.EVMaximumPowerLimit_nsprefix_) else ''
            self.EVMaximumPowerLimit.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVMaximumPowerLimit', pretty_print=pretty_print)
        if self.BulkChargingComplete is not None:
            namespaceprefix_ = self.BulkChargingComplete_nsprefix_ + ':' if (UseCapturedNS_ and self.BulkChargingComplete_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBulkChargingComplete>%s</%sBulkChargingComplete>%s' % (namespaceprefix_ , self.gds_format_boolean(self.BulkChargingComplete, input_name='BulkChargingComplete'), namespaceprefix_ , eol_))
        if self.ChargingComplete is not None:
            namespaceprefix_ = self.ChargingComplete_nsprefix_ + ':' if (UseCapturedNS_ and self.ChargingComplete_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sChargingComplete>%s</%sChargingComplete>%s' % (namespaceprefix_ , self.gds_format_boolean(self.ChargingComplete, input_name='ChargingComplete'), namespaceprefix_ , eol_))
        if self.RemainingTimeToFullSoC is not None:
            namespaceprefix_ = self.RemainingTimeToFullSoC_nsprefix_ + ':' if (UseCapturedNS_ and self.RemainingTimeToFullSoC_nsprefix_) else ''
            self.RemainingTimeToFullSoC.export(outfile, level, namespaceprefix_, namespacedef_='', name_='RemainingTimeToFullSoC', pretty_print=pretty_print)
        if self.RemainingTimeToBulkSoC is not None:
            namespaceprefix_ = self.RemainingTimeToBulkSoC_nsprefix_ + ':' if (UseCapturedNS_ and self.RemainingTimeToBulkSoC_nsprefix_) else ''
            self.RemainingTimeToBulkSoC.export(outfile, level, namespaceprefix_, namespacedef_='', name_='RemainingTimeToBulkSoC', pretty_print=pretty_print)
        if self.EVTargetVoltage is not None:
            namespaceprefix_ = self.EVTargetVoltage_nsprefix_ + ':' if (UseCapturedNS_ and self.EVTargetVoltage_nsprefix_) else ''
            self.EVTargetVoltage.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVTargetVoltage', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(CurrentDemandReqType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'DC_EVStatus':
            obj_ = DC_EVStatusType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DC_EVStatus = obj_
            obj_.original_tagname_ = 'DC_EVStatus'
        elif nodeName_ == 'EVTargetCurrent':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVTargetCurrent = obj_
            obj_.original_tagname_ = 'EVTargetCurrent'
        elif nodeName_ == 'EVMaximumVoltageLimit':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVMaximumVoltageLimit = obj_
            obj_.original_tagname_ = 'EVMaximumVoltageLimit'
        elif nodeName_ == 'EVMaximumCurrentLimit':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVMaximumCurrentLimit = obj_
            obj_.original_tagname_ = 'EVMaximumCurrentLimit'
        elif nodeName_ == 'EVMaximumPowerLimit':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVMaximumPowerLimit = obj_
            obj_.original_tagname_ = 'EVMaximumPowerLimit'
        elif nodeName_ == 'BulkChargingComplete':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'BulkChargingComplete')
            ival_ = self.gds_validate_boolean(ival_, node, 'BulkChargingComplete')
            self.BulkChargingComplete = ival_
            self.BulkChargingComplete_nsprefix_ = child_.prefix
        elif nodeName_ == 'ChargingComplete':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'ChargingComplete')
            ival_ = self.gds_validate_boolean(ival_, node, 'ChargingComplete')
            self.ChargingComplete = ival_
            self.ChargingComplete_nsprefix_ = child_.prefix
        elif nodeName_ == 'RemainingTimeToFullSoC':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.RemainingTimeToFullSoC = obj_
            obj_.original_tagname_ = 'RemainingTimeToFullSoC'
        elif nodeName_ == 'RemainingTimeToBulkSoC':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.RemainingTimeToBulkSoC = obj_
            obj_.original_tagname_ = 'RemainingTimeToBulkSoC'
        elif nodeName_ == 'EVTargetVoltage':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVTargetVoltage = obj_
            obj_.original_tagname_ = 'EVTargetVoltage'
        super(CurrentDemandReqType, self)._buildChildren(child_, node, nodeName_, True)
# end class CurrentDemandReqType


class CurrentDemandResType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, ResponseCode=None, DC_EVSEStatus=None, EVSEPresentVoltage=None, EVSEPresentCurrent=None, EVSECurrentLimitAchieved=None, EVSEVoltageLimitAchieved=None, EVSEPowerLimitAchieved=None, EVSEMaximumVoltageLimit=None, EVSEMaximumCurrentLimit=None, EVSEMaximumPowerLimit=None, EVSEID=None, SAScheduleTupleID=None, MeterInfo=None, ReceiptRequired=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(globals().get("CurrentDemandResType"), self).__init__( **kwargs_)
        self.ResponseCode = ResponseCode
        self.validate_responseCodeType(self.ResponseCode)
        self.ResponseCode_nsprefix_ = "ns6"
        self.DC_EVSEStatus = DC_EVSEStatus
        self.DC_EVSEStatus_nsprefix_ = "ns6"
        self.EVSEPresentVoltage = EVSEPresentVoltage
        self.EVSEPresentVoltage_nsprefix_ = "ns6"
        self.EVSEPresentCurrent = EVSEPresentCurrent
        self.EVSEPresentCurrent_nsprefix_ = "ns6"
        self.EVSECurrentLimitAchieved = EVSECurrentLimitAchieved
        self.EVSECurrentLimitAchieved_nsprefix_ = None
        self.EVSEVoltageLimitAchieved = EVSEVoltageLimitAchieved
        self.EVSEVoltageLimitAchieved_nsprefix_ = None
        self.EVSEPowerLimitAchieved = EVSEPowerLimitAchieved
        self.EVSEPowerLimitAchieved_nsprefix_ = None
        self.EVSEMaximumVoltageLimit = EVSEMaximumVoltageLimit
        self.EVSEMaximumVoltageLimit_nsprefix_ = "ns6"
        self.EVSEMaximumCurrentLimit = EVSEMaximumCurrentLimit
        self.EVSEMaximumCurrentLimit_nsprefix_ = "ns6"
        self.EVSEMaximumPowerLimit = EVSEMaximumPowerLimit
        self.EVSEMaximumPowerLimit_nsprefix_ = "ns6"
        self.EVSEID = EVSEID
        self.validate_evseIDType(self.EVSEID)
        self.EVSEID_nsprefix_ = "ns6"
        self.SAScheduleTupleID = SAScheduleTupleID
        self.validate_SAIDType(self.SAScheduleTupleID)
        self.SAScheduleTupleID_nsprefix_ = "ns6"
        self.MeterInfo = MeterInfo
        self.MeterInfo_nsprefix_ = "ns6"
        self.ReceiptRequired = ReceiptRequired
        self.ReceiptRequired_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CurrentDemandResType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CurrentDemandResType.subclass:
            return CurrentDemandResType.subclass(*args_, **kwargs_)
        else:
            return CurrentDemandResType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ResponseCode(self):
        return self.ResponseCode
    def set_ResponseCode(self, ResponseCode):
        self.ResponseCode = ResponseCode
    def get_DC_EVSEStatus(self):
        return self.DC_EVSEStatus
    def set_DC_EVSEStatus(self, DC_EVSEStatus):
        self.DC_EVSEStatus = DC_EVSEStatus
    def get_EVSEPresentVoltage(self):
        return self.EVSEPresentVoltage
    def set_EVSEPresentVoltage(self, EVSEPresentVoltage):
        self.EVSEPresentVoltage = EVSEPresentVoltage
    def get_EVSEPresentCurrent(self):
        return self.EVSEPresentCurrent
    def set_EVSEPresentCurrent(self, EVSEPresentCurrent):
        self.EVSEPresentCurrent = EVSEPresentCurrent
    def get_EVSECurrentLimitAchieved(self):
        return self.EVSECurrentLimitAchieved
    def set_EVSECurrentLimitAchieved(self, EVSECurrentLimitAchieved):
        self.EVSECurrentLimitAchieved = EVSECurrentLimitAchieved
    def get_EVSEVoltageLimitAchieved(self):
        return self.EVSEVoltageLimitAchieved
    def set_EVSEVoltageLimitAchieved(self, EVSEVoltageLimitAchieved):
        self.EVSEVoltageLimitAchieved = EVSEVoltageLimitAchieved
    def get_EVSEPowerLimitAchieved(self):
        return self.EVSEPowerLimitAchieved
    def set_EVSEPowerLimitAchieved(self, EVSEPowerLimitAchieved):
        self.EVSEPowerLimitAchieved = EVSEPowerLimitAchieved
    def get_EVSEMaximumVoltageLimit(self):
        return self.EVSEMaximumVoltageLimit
    def set_EVSEMaximumVoltageLimit(self, EVSEMaximumVoltageLimit):
        self.EVSEMaximumVoltageLimit = EVSEMaximumVoltageLimit
    def get_EVSEMaximumCurrentLimit(self):
        return self.EVSEMaximumCurrentLimit
    def set_EVSEMaximumCurrentLimit(self, EVSEMaximumCurrentLimit):
        self.EVSEMaximumCurrentLimit = EVSEMaximumCurrentLimit
    def get_EVSEMaximumPowerLimit(self):
        return self.EVSEMaximumPowerLimit
    def set_EVSEMaximumPowerLimit(self, EVSEMaximumPowerLimit):
        self.EVSEMaximumPowerLimit = EVSEMaximumPowerLimit
    def get_EVSEID(self):
        return self.EVSEID
    def set_EVSEID(self, EVSEID):
        self.EVSEID = EVSEID
    def get_SAScheduleTupleID(self):
        return self.SAScheduleTupleID
    def set_SAScheduleTupleID(self, SAScheduleTupleID):
        self.SAScheduleTupleID = SAScheduleTupleID
    def get_MeterInfo(self):
        return self.MeterInfo
    def set_MeterInfo(self, MeterInfo):
        self.MeterInfo = MeterInfo
    def get_ReceiptRequired(self):
        return self.ReceiptRequired
    def set_ReceiptRequired(self, ReceiptRequired):
        self.ReceiptRequired = ReceiptRequired
    def validate_responseCodeType(self, value):
        result = True
        # Validate type responseCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['OK', 'OK_NewSessionEstablished', 'OK_OldSessionJoined', 'OK_CertificateExpiresSoon', 'FAILED', 'FAILED_SequenceError', 'FAILED_ServiceIDInvalid', 'FAILED_UnknownSession', 'FAILED_ServiceSelectionInvalid', 'FAILED_PaymentSelectionInvalid', 'FAILED_CertificateExpired', 'FAILED_SignatureError', 'FAILED_NoCertificateAvailable', 'FAILED_CertChainError', 'FAILED_ChallengeInvalid', 'FAILED_ContractCanceled', 'FAILED_WrongChargeParameter', 'FAILED_PowerDeliveryNotApplied', 'FAILED_TariffSelectionInvalid', 'FAILED_ChargingProfileInvalid', 'FAILED_MeteringSignatureNotValid', 'FAILED_NoChargeServiceSelected', 'FAILED_WrongEnergyTransferMode', 'FAILED_ContactorError', 'FAILED_CertificateNotAllowedAtThisEVSE', 'FAILED_CertificateRevoked']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on responseCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_evseIDType(self, value):
        result = True
        # Validate type evseIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 37:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on evseIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on evseIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_SAIDType(self, value):
        result = True
        # Validate type SAIDType, a restriction on xs:unsignedByte.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on SAIDType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on SAIDType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.ResponseCode is not None or
            self.DC_EVSEStatus is not None or
            self.EVSEPresentVoltage is not None or
            self.EVSEPresentCurrent is not None or
            self.EVSECurrentLimitAchieved is not None or
            self.EVSEVoltageLimitAchieved is not None or
            self.EVSEPowerLimitAchieved is not None or
            self.EVSEMaximumVoltageLimit is not None or
            self.EVSEMaximumCurrentLimit is not None or
            self.EVSEMaximumPowerLimit is not None or
            self.EVSEID is not None or
            self.SAScheduleTupleID is not None or
            self.MeterInfo is not None or
            self.ReceiptRequired is not None or
            super(CurrentDemandResType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes"  xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='CurrentDemandResType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CurrentDemandResType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CurrentDemandResType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CurrentDemandResType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CurrentDemandResType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CurrentDemandResType'):
        super(CurrentDemandResType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CurrentDemandResType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes"  xmlns:None="urn:iso:15118:2:2013:MsgBody" ', name_='CurrentDemandResType', fromsubclass_=False, pretty_print=True):
        super(CurrentDemandResType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ResponseCode is not None:
            namespaceprefix_ = self.ResponseCode_nsprefix_ + ':' if (UseCapturedNS_ and self.ResponseCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sResponseCode>%s</%sResponseCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ResponseCode), input_name='ResponseCode')), namespaceprefix_ , eol_))
        if self.DC_EVSEStatus is not None:
            namespaceprefix_ = self.DC_EVSEStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.DC_EVSEStatus_nsprefix_) else ''
            self.DC_EVSEStatus.export(outfile, level, namespaceprefix_, namespacedef_='', name_='DC_EVSEStatus', pretty_print=pretty_print)
        if self.EVSEPresentVoltage is not None:
            namespaceprefix_ = self.EVSEPresentVoltage_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEPresentVoltage_nsprefix_) else ''
            self.EVSEPresentVoltage.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVSEPresentVoltage', pretty_print=pretty_print)
        if self.EVSEPresentCurrent is not None:
            namespaceprefix_ = self.EVSEPresentCurrent_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEPresentCurrent_nsprefix_) else ''
            self.EVSEPresentCurrent.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVSEPresentCurrent', pretty_print=pretty_print)
        if self.EVSECurrentLimitAchieved is not None:
            namespaceprefix_ = self.EVSECurrentLimitAchieved_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSECurrentLimitAchieved_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEVSECurrentLimitAchieved>%s</%sEVSECurrentLimitAchieved>%s' % (namespaceprefix_ , self.gds_format_boolean(self.EVSECurrentLimitAchieved, input_name='EVSECurrentLimitAchieved'), namespaceprefix_ , eol_))
        if self.EVSEVoltageLimitAchieved is not None:
            namespaceprefix_ = self.EVSEVoltageLimitAchieved_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEVoltageLimitAchieved_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEVSEVoltageLimitAchieved>%s</%sEVSEVoltageLimitAchieved>%s' % (namespaceprefix_ , self.gds_format_boolean(self.EVSEVoltageLimitAchieved, input_name='EVSEVoltageLimitAchieved'), namespaceprefix_ , eol_))
        if self.EVSEPowerLimitAchieved is not None:
            namespaceprefix_ = self.EVSEPowerLimitAchieved_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEPowerLimitAchieved_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEVSEPowerLimitAchieved>%s</%sEVSEPowerLimitAchieved>%s' % (namespaceprefix_ , self.gds_format_boolean(self.EVSEPowerLimitAchieved, input_name='EVSEPowerLimitAchieved'), namespaceprefix_ , eol_))
        if self.EVSEMaximumVoltageLimit is not None:
            namespaceprefix_ = self.EVSEMaximumVoltageLimit_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEMaximumVoltageLimit_nsprefix_) else ''
            self.EVSEMaximumVoltageLimit.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVSEMaximumVoltageLimit', pretty_print=pretty_print)
        if self.EVSEMaximumCurrentLimit is not None:
            namespaceprefix_ = self.EVSEMaximumCurrentLimit_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEMaximumCurrentLimit_nsprefix_) else ''
            self.EVSEMaximumCurrentLimit.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVSEMaximumCurrentLimit', pretty_print=pretty_print)
        if self.EVSEMaximumPowerLimit is not None:
            namespaceprefix_ = self.EVSEMaximumPowerLimit_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEMaximumPowerLimit_nsprefix_) else ''
            self.EVSEMaximumPowerLimit.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVSEMaximumPowerLimit', pretty_print=pretty_print)
        if self.EVSEID is not None:
            namespaceprefix_ = self.EVSEID_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEVSEID>%s</%sEVSEID>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.EVSEID), input_name='EVSEID')), namespaceprefix_ , eol_))
        if self.SAScheduleTupleID is not None:
            namespaceprefix_ = self.SAScheduleTupleID_nsprefix_ + ':' if (UseCapturedNS_ and self.SAScheduleTupleID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSAScheduleTupleID>%s</%sSAScheduleTupleID>%s' % (namespaceprefix_ , self.gds_format_integer(self.SAScheduleTupleID, input_name='SAScheduleTupleID'), namespaceprefix_ , eol_))
        if self.MeterInfo is not None:
            namespaceprefix_ = self.MeterInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.MeterInfo_nsprefix_) else ''
            self.MeterInfo.export(outfile, level, namespaceprefix_, namespacedef_='', name_='MeterInfo', pretty_print=pretty_print)
        if self.ReceiptRequired is not None:
            namespaceprefix_ = self.ReceiptRequired_nsprefix_ + ':' if (UseCapturedNS_ and self.ReceiptRequired_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sReceiptRequired>%s</%sReceiptRequired>%s' % (namespaceprefix_ , self.gds_format_boolean(self.ReceiptRequired, input_name='ReceiptRequired'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(CurrentDemandResType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ResponseCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ResponseCode')
            value_ = self.gds_validate_string(value_, node, 'ResponseCode')
            self.ResponseCode = value_
            self.ResponseCode_nsprefix_ = child_.prefix
            # validate type responseCodeType
            self.validate_responseCodeType(self.ResponseCode)
        elif nodeName_ == 'DC_EVSEStatus':
            obj_ = DC_EVSEStatusType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DC_EVSEStatus = obj_
            obj_.original_tagname_ = 'DC_EVSEStatus'
        elif nodeName_ == 'EVSEPresentVoltage':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSEPresentVoltage = obj_
            obj_.original_tagname_ = 'EVSEPresentVoltage'
        elif nodeName_ == 'EVSEPresentCurrent':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSEPresentCurrent = obj_
            obj_.original_tagname_ = 'EVSEPresentCurrent'
        elif nodeName_ == 'EVSECurrentLimitAchieved':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'EVSECurrentLimitAchieved')
            ival_ = self.gds_validate_boolean(ival_, node, 'EVSECurrentLimitAchieved')
            self.EVSECurrentLimitAchieved = ival_
            self.EVSECurrentLimitAchieved_nsprefix_ = child_.prefix
        elif nodeName_ == 'EVSEVoltageLimitAchieved':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'EVSEVoltageLimitAchieved')
            ival_ = self.gds_validate_boolean(ival_, node, 'EVSEVoltageLimitAchieved')
            self.EVSEVoltageLimitAchieved = ival_
            self.EVSEVoltageLimitAchieved_nsprefix_ = child_.prefix
        elif nodeName_ == 'EVSEPowerLimitAchieved':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'EVSEPowerLimitAchieved')
            ival_ = self.gds_validate_boolean(ival_, node, 'EVSEPowerLimitAchieved')
            self.EVSEPowerLimitAchieved = ival_
            self.EVSEPowerLimitAchieved_nsprefix_ = child_.prefix
        elif nodeName_ == 'EVSEMaximumVoltageLimit':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSEMaximumVoltageLimit = obj_
            obj_.original_tagname_ = 'EVSEMaximumVoltageLimit'
        elif nodeName_ == 'EVSEMaximumCurrentLimit':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSEMaximumCurrentLimit = obj_
            obj_.original_tagname_ = 'EVSEMaximumCurrentLimit'
        elif nodeName_ == 'EVSEMaximumPowerLimit':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSEMaximumPowerLimit = obj_
            obj_.original_tagname_ = 'EVSEMaximumPowerLimit'
        elif nodeName_ == 'EVSEID':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'EVSEID')
            value_ = self.gds_validate_string(value_, node, 'EVSEID')
            self.EVSEID = value_
            self.EVSEID_nsprefix_ = child_.prefix
            # validate type evseIDType
            self.validate_evseIDType(self.EVSEID)
        elif nodeName_ == 'SAScheduleTupleID' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'SAScheduleTupleID')
            ival_ = self.gds_validate_integer(ival_, node, 'SAScheduleTupleID')
            self.SAScheduleTupleID = ival_
            self.SAScheduleTupleID_nsprefix_ = child_.prefix
            # validate type SAIDType
            self.validate_SAIDType(self.SAScheduleTupleID)
        elif nodeName_ == 'MeterInfo':
            obj_ = MeterInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.MeterInfo = obj_
            obj_.original_tagname_ = 'MeterInfo'
        elif nodeName_ == 'ReceiptRequired':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'ReceiptRequired')
            ival_ = self.gds_validate_boolean(ival_, node, 'ReceiptRequired')
            self.ReceiptRequired = ival_
            self.ReceiptRequired_nsprefix_ = child_.prefix
        super(CurrentDemandResType, self)._buildChildren(child_, node, nodeName_, True)
# end class CurrentDemandResType


class WeldingDetectionReqType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, DC_EVStatus=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("WeldingDetectionReqType"), self).__init__( **kwargs_)
        self.DC_EVStatus = DC_EVStatus
        self.DC_EVStatus_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, WeldingDetectionReqType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if WeldingDetectionReqType.subclass:
            return WeldingDetectionReqType.subclass(*args_, **kwargs_)
        else:
            return WeldingDetectionReqType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_DC_EVStatus(self):
        return self.DC_EVStatus
    def set_DC_EVStatus(self, DC_EVStatus):
        self.DC_EVStatus = DC_EVStatus
    def _hasContent(self):
        if (
            self.DC_EVStatus is not None or
            super(WeldingDetectionReqType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='WeldingDetectionReqType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('WeldingDetectionReqType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'WeldingDetectionReqType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='WeldingDetectionReqType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='WeldingDetectionReqType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='WeldingDetectionReqType'):
        super(WeldingDetectionReqType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='WeldingDetectionReqType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='WeldingDetectionReqType', fromsubclass_=False, pretty_print=True):
        super(WeldingDetectionReqType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.DC_EVStatus is not None:
            namespaceprefix_ = self.DC_EVStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.DC_EVStatus_nsprefix_) else ''
            self.DC_EVStatus.export(outfile, level, namespaceprefix_, namespacedef_='', name_='DC_EVStatus', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(WeldingDetectionReqType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'DC_EVStatus':
            obj_ = DC_EVStatusType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DC_EVStatus = obj_
            obj_.original_tagname_ = 'DC_EVStatus'
        super(WeldingDetectionReqType, self)._buildChildren(child_, node, nodeName_, True)
# end class WeldingDetectionReqType


class WeldingDetectionResType(BodyBaseType):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = BodyBaseType
    def __init__(self, ResponseCode=None, DC_EVSEStatus=None, EVSEPresentVoltage=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ns5"
        super(globals().get("WeldingDetectionResType"), self).__init__( **kwargs_)
        self.ResponseCode = ResponseCode
        self.validate_responseCodeType(self.ResponseCode)
        self.ResponseCode_nsprefix_ = "ns6"
        self.DC_EVSEStatus = DC_EVSEStatus
        self.DC_EVSEStatus_nsprefix_ = "ns6"
        self.EVSEPresentVoltage = EVSEPresentVoltage
        self.EVSEPresentVoltage_nsprefix_ = "ns6"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, WeldingDetectionResType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if WeldingDetectionResType.subclass:
            return WeldingDetectionResType.subclass(*args_, **kwargs_)
        else:
            return WeldingDetectionResType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ResponseCode(self):
        return self.ResponseCode
    def set_ResponseCode(self, ResponseCode):
        self.ResponseCode = ResponseCode
    def get_DC_EVSEStatus(self):
        return self.DC_EVSEStatus
    def set_DC_EVSEStatus(self, DC_EVSEStatus):
        self.DC_EVSEStatus = DC_EVSEStatus
    def get_EVSEPresentVoltage(self):
        return self.EVSEPresentVoltage
    def set_EVSEPresentVoltage(self, EVSEPresentVoltage):
        self.EVSEPresentVoltage = EVSEPresentVoltage
    def validate_responseCodeType(self, value):
        result = True
        # Validate type responseCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['OK', 'OK_NewSessionEstablished', 'OK_OldSessionJoined', 'OK_CertificateExpiresSoon', 'FAILED', 'FAILED_SequenceError', 'FAILED_ServiceIDInvalid', 'FAILED_UnknownSession', 'FAILED_ServiceSelectionInvalid', 'FAILED_PaymentSelectionInvalid', 'FAILED_CertificateExpired', 'FAILED_SignatureError', 'FAILED_NoCertificateAvailable', 'FAILED_CertChainError', 'FAILED_ChallengeInvalid', 'FAILED_ContractCanceled', 'FAILED_WrongChargeParameter', 'FAILED_PowerDeliveryNotApplied', 'FAILED_TariffSelectionInvalid', 'FAILED_ChargingProfileInvalid', 'FAILED_MeteringSignatureNotValid', 'FAILED_NoChargeServiceSelected', 'FAILED_WrongEnergyTransferMode', 'FAILED_ContactorError', 'FAILED_CertificateNotAllowedAtThisEVSE', 'FAILED_CertificateRevoked']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on responseCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.ResponseCode is not None or
            self.DC_EVSEStatus is not None or
            self.EVSEPresentVoltage is not None or
            super(WeldingDetectionResType, self)._hasContent()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='WeldingDetectionResType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('WeldingDetectionResType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'WeldingDetectionResType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='WeldingDetectionResType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='WeldingDetectionResType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='WeldingDetectionResType'):
        super(WeldingDetectionResType, self)._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='WeldingDetectionResType')
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:ns5="urn:iso:15118:2:2013:MsgBody" xmlns:ns6="urn:iso:15118:2:2013:MsgDataTypes" ', name_='WeldingDetectionResType', fromsubclass_=False, pretty_print=True):
        super(WeldingDetectionResType, self)._exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ResponseCode is not None:
            namespaceprefix_ = self.ResponseCode_nsprefix_ + ':' if (UseCapturedNS_ and self.ResponseCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sResponseCode>%s</%sResponseCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ResponseCode), input_name='ResponseCode')), namespaceprefix_ , eol_))
        if self.DC_EVSEStatus is not None:
            namespaceprefix_ = self.DC_EVSEStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.DC_EVSEStatus_nsprefix_) else ''
            self.DC_EVSEStatus.export(outfile, level, namespaceprefix_, namespacedef_='', name_='DC_EVSEStatus', pretty_print=pretty_print)
        if self.EVSEPresentVoltage is not None:
            namespaceprefix_ = self.EVSEPresentVoltage_nsprefix_ + ':' if (UseCapturedNS_ and self.EVSEPresentVoltage_nsprefix_) else ''
            self.EVSEPresentVoltage.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EVSEPresentVoltage', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        super(WeldingDetectionResType, self)._buildAttributes(node, attrs, already_processed)
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ResponseCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ResponseCode')
            value_ = self.gds_validate_string(value_, node, 'ResponseCode')
            self.ResponseCode = value_
            self.ResponseCode_nsprefix_ = child_.prefix
            # validate type responseCodeType
            self.validate_responseCodeType(self.ResponseCode)
        elif nodeName_ == 'DC_EVSEStatus':
            obj_ = DC_EVSEStatusType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DC_EVSEStatus = obj_
            obj_.original_tagname_ = 'DC_EVSEStatus'
        elif nodeName_ == 'EVSEPresentVoltage':
            obj_ = PhysicalValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EVSEPresentVoltage = obj_
            obj_.original_tagname_ = 'EVSEPresentVoltage'
        super(WeldingDetectionResType, self)._buildChildren(child_, node, nodeName_, True)
# end class WeldingDetectionResType


class DigestValueType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "ds"
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DigestValueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DigestValueType.subclass:
            return DigestValueType.subclass(*args_, **kwargs_)
        else:
            return DigestValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_DigestValueType_impl(self, value):
        result = True
        # Validate type DigestValueType_impl, a restriction on base64Binary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            pass
        return result
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DigestValueType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DigestValueType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DigestValueType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DigestValueType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DigestValueType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DigestValueType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DigestValueType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class DigestValueType


GDSClassesMapping = {
    'AC_EVChargeParameter': AC_EVChargeParameterType,
    'AC_EVSEChargeParameter': AC_EVSEChargeParameterType,
    'AC_EVSEStatus': AC_EVSEStatusType,
    'AuthorizationReq': AuthorizationReqType,
    'AuthorizationRes': AuthorizationResType,
    'BodyElement': BodyBaseType,
    'CableCheckReq': CableCheckReqType,
    'CableCheckRes': CableCheckResType,
    'CanonicalizationMethod': CanonicalizationMethodType,
    'CertificateInstallationReq': CertificateInstallationReqType,
    'CertificateInstallationRes': CertificateInstallationResType,
    'CertificateUpdateReq': CertificateUpdateReqType,
    'CertificateUpdateRes': CertificateUpdateResType,
    'ChargeParameterDiscoveryReq': ChargeParameterDiscoveryReqType,
    'ChargeParameterDiscoveryRes': ChargeParameterDiscoveryResType,
    'ChargingStatusReq': ChargingStatusReqType,
    'ChargingStatusRes': ChargingStatusResType,
    'CurrentDemandReq': CurrentDemandReqType,
    'CurrentDemandRes': CurrentDemandResType,
    'DC_EVChargeParameter': DC_EVChargeParameterType,
    'DC_EVPowerDeliveryParameter': DC_EVPowerDeliveryParameterType,
    'DC_EVSEChargeParameter': DC_EVSEChargeParameterType,
    'DC_EVSEStatus': DC_EVSEStatusType,
    'DC_EVStatus': DC_EVStatusType,
    'DSAKeyValue': DSAKeyValueType,
    'DigestMethod': DigestMethodType,
    'DigestValue': DigestValueType,
    'EVChargeParameter': EVChargeParameterType,
    'EVPowerDeliveryParameter': EVPowerDeliveryParameterType,
    'EVSEChargeParameter': EVSEChargeParameterType,
    'EVSEStatus': EVSEStatusType,
    'EVStatus': EVStatusType,
    'Entry': EntryType,
    'KeyInfo': KeyInfoType,
    'KeyValue': KeyValueType,
    'Manifest': ManifestType,
    'MeteringReceiptReq': MeteringReceiptReqType,
    'MeteringReceiptRes': MeteringReceiptResType,
    'Object': ObjectType,
    'PGPData': PGPDataType,
    'PMaxScheduleEntry': PMaxScheduleEntryType,
    'PaymentDetailsReq': PaymentDetailsReqType,
    'PaymentDetailsRes': PaymentDetailsResType,
    'PaymentServiceSelectionReq': PaymentServiceSelectionReqType,
    'PaymentServiceSelectionRes': PaymentServiceSelectionResType,
    'PowerDeliveryReq': PowerDeliveryReqType,
    'PowerDeliveryRes': PowerDeliveryResType,
    'PreChargeReq': PreChargeReqType,
    'PreChargeRes': PreChargeResType,
    'RSAKeyValue': RSAKeyValueType,
    'Reference': ReferenceType,
    'RelativeTimeInterval': RelativeTimeIntervalType,
    'RetrievalMethod': RetrievalMethodType,
    'SAScheduleList': SAScheduleListType,
    'SASchedules': SASchedulesType,
    'SPKIData': SPKIDataType,
    'SalesTariffEntry': SalesTariffEntryType,
    'ServiceDetailReq': ServiceDetailReqType,
    'ServiceDetailRes': ServiceDetailResType,
    'ServiceDiscoveryReq': ServiceDiscoveryReqType,
    'ServiceDiscoveryRes': ServiceDiscoveryResType,
    'SessionSetupReq': SessionSetupReqType,
    'SessionSetupRes': SessionSetupResType,
    'SessionStopReq': SessionStopReqType,
    'SessionStopRes': SessionStopResType,
    'Signature': SignatureType,
    'SignatureMethod': SignatureMethodType,
    'SignatureProperties': SignaturePropertiesType,
    'SignatureProperty': SignaturePropertyType,
    'SignatureValue': SignatureValueType,
    'SignedInfo': SignedInfoType,
    'TimeInterval': IntervalType,
    'Transform': TransformType,
    'Transforms': TransformsType,
    'WeldingDetectionReq': WeldingDetectionReqType,
    'WeldingDetectionRes': WeldingDetectionResType,
    'X509Data': X509DataType,
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    prefix_tag = TagNamePrefix + tag
    rootClass = GDSClassesMapping.get(prefix_tag)
    if rootClass is None:
        rootClass = globals().get(prefix_tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'V2G_Message'
        rootClass = V2G_Message
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 5, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, reverse_mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'V2G_Message'
        rootClass = V2G_Message
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if mapping is None:
        mapping = {}
    if reverse_mapping is None:
        reverse_mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping,
        reverse_mapping_=reverse_mapping, nsmap_=nsmap)
    reverse_node_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_node_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'V2G_Message'
        rootClass = V2G_Message
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'V2G_Message'
        rootClass = V2G_Message
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from msgDef1 import *\n\n')
        sys.stdout.write('import msgDef1 as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {'http://www.w3.org/2000/09/xmldsig#': [('CryptoBinary',
                                         'xmldsig-core-schema.xsd',
                                         'ST'),
                                        ('DigestValueType',
                                         'xmldsig-core-schema.xsd',
                                         'ST'),
                                        ('HMACOutputLengthType',
                                         'xmldsig-core-schema.xsd',
                                         'ST'),
                                        ('SignatureType',
                                         'xmldsig-core-schema.xsd',
                                         'CT'),
                                        ('SignatureValueType',
                                         'xmldsig-core-schema.xsd',
                                         'CT'),
                                        ('SignedInfoType',
                                         'xmldsig-core-schema.xsd',
                                         'CT'),
                                        ('CanonicalizationMethodType',
                                         'xmldsig-core-schema.xsd',
                                         'CT'),
                                        ('SignatureMethodType',
                                         'xmldsig-core-schema.xsd',
                                         'CT'),
                                        ('ReferenceType',
                                         'xmldsig-core-schema.xsd',
                                         'CT'),
                                        ('TransformsType',
                                         'xmldsig-core-schema.xsd',
                                         'CT'),
                                        ('TransformType',
                                         'xmldsig-core-schema.xsd',
                                         'CT'),
                                        ('DigestMethodType',
                                         'xmldsig-core-schema.xsd',
                                         'CT'),
                                        ('KeyInfoType',
                                         'xmldsig-core-schema.xsd',
                                         'CT'),
                                        ('KeyValueType',
                                         'xmldsig-core-schema.xsd',
                                         'CT'),
                                        ('RetrievalMethodType',
                                         'xmldsig-core-schema.xsd',
                                         'CT'),
                                        ('X509DataType',
                                         'xmldsig-core-schema.xsd',
                                         'CT'),
                                        ('X509IssuerSerialType',
                                         'xmldsig-core-schema.xsd',
                                         'CT'),
                                        ('PGPDataType',
                                         'xmldsig-core-schema.xsd',
                                         'CT'),
                                        ('SPKIDataType',
                                         'xmldsig-core-schema.xsd',
                                         'CT'),
                                        ('ObjectType',
                                         'xmldsig-core-schema.xsd',
                                         'CT'),
                                        ('ManifestType',
                                         'xmldsig-core-schema.xsd',
                                         'CT'),
                                        ('SignaturePropertiesType',
                                         'xmldsig-core-schema.xsd',
                                         'CT'),
                                        ('SignaturePropertyType',
                                         'xmldsig-core-schema.xsd',
                                         'CT'),
                                        ('DSAKeyValueType',
                                         'xmldsig-core-schema.xsd',
                                         'CT'),
                                        ('RSAKeyValueType',
                                         'xmldsig-core-schema.xsd',
                                         'CT')],
 'urn:iso:15118:2:2013:MsgBody': [('BodyType', 'V2G_CI_MsgBody.xsd', 'CT'),
                                  ('BodyBaseType', 'V2G_CI_MsgBody.xsd', 'CT'),
                                  ('SessionSetupReqType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('SessionSetupResType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('ServiceDiscoveryReqType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('ServiceDiscoveryResType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('ServiceDetailReqType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('ServiceDetailResType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('PaymentServiceSelectionReqType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('PaymentServiceSelectionResType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('PaymentDetailsReqType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('PaymentDetailsResType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('AuthorizationReqType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('AuthorizationResType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('ChargeParameterDiscoveryReqType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('ChargeParameterDiscoveryResType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('PowerDeliveryReqType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('PowerDeliveryResType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('MeteringReceiptReqType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('MeteringReceiptResType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('SessionStopReqType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('SessionStopResType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('CertificateUpdateReqType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('CertificateUpdateResType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('CertificateInstallationReqType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('CertificateInstallationResType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('ChargingStatusReqType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('ChargingStatusResType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('CableCheckReqType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('CableCheckResType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('PreChargeReqType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('PreChargeResType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('CurrentDemandReqType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('CurrentDemandResType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('WeldingDetectionReqType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT'),
                                  ('WeldingDetectionResType',
                                   'V2G_CI_MsgBody.xsd',
                                   'CT')],
 'urn:iso:15118:2:2013:MsgDataTypes': [('percentValueType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('faultMsgType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('EVSEProcessingType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('EVSENotificationType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('chargeProgressType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('chargingSessionType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('serviceNameType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('serviceCategoryType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('serviceScopeType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('maxNumPhasesType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('valueType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('meterStatusType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('EnergyTransferModeType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('genChallengeType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('certificateType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('dHpublickeyType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('privateKeyType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('sigMeterReadingType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('sessionIDType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('evccIDType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('evseIDType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('serviceIDType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('eMAIDType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('meterIDType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('SAIDType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('tariffDescriptionType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('costKindType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('paymentOptionType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('faultCodeType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('responseCodeType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('unitMultiplierType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('unitSymbolType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('DC_EVSEStatusCodeType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('isolationLevelType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('DC_EVErrorCodeType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'ST'),
                                       ('ServiceType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('ServiceListType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('SelectedServiceListType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('SelectedServiceType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('ServiceParameterListType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('ParameterSetType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('ParameterType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('ChargeServiceType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('SupportedEnergyTransferModeType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('ContractSignatureEncryptedPrivateKeyType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('DiffieHellmanPublickeyType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('EMAIDType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('CertificateChainType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('SubCertificatesType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('ListOfRootCertificateIDsType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('MeterInfoType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('PhysicalValueType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('NotificationType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('SASchedulesType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('SAScheduleListType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('SAScheduleTupleType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('SalesTariffType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('PMaxScheduleType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('EntryType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('SalesTariffEntryType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('PMaxScheduleEntryType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('IntervalType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('RelativeTimeIntervalType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('ConsumptionCostType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('CostType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('EVSEStatusType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('AC_EVSEStatusType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('EVStatusType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('DC_EVSEStatusType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('DC_EVStatusType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('EVChargeParameterType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('AC_EVChargeParameterType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('DC_EVChargeParameterType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('EVSEChargeParameterType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('AC_EVSEChargeParameterType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('DC_EVSEChargeParameterType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('EVPowerDeliveryParameterType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('DC_EVPowerDeliveryParameterType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('ChargingProfileType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('ProfileEntryType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT'),
                                       ('PaymentOptionListType',
                                        'V2G_CI_MsgDataTypes.xsd',
                                        'CT')],
 'urn:iso:15118:2:2013:MsgDef': [],
 'urn:iso:15118:2:2013:MsgHeader': [('MessageHeaderType',
                                     'V2G_CI_MsgHeader.xsd',
                                     'CT')]}

__all__ = [
    "AC_EVChargeParameterType",
    "AC_EVSEChargeParameterType",
    "AC_EVSEStatusType",
    "AuthorizationReqType",
    "AuthorizationResType",
    "BodyBaseType",
    "BodyType",
    "CableCheckReqType",
    "CableCheckResType",
    "CanonicalizationMethodType",
    "CertificateChainType",
    "CertificateInstallationReqType",
    "CertificateInstallationResType",
    "CertificateUpdateReqType",
    "CertificateUpdateResType",
    "ChargeParameterDiscoveryReqType",
    "ChargeParameterDiscoveryResType",
    "ChargeServiceType",
    "ChargingProfileType",
    "ChargingStatusReqType",
    "ChargingStatusResType",
    "ConsumptionCostType",
    "ContractSignatureEncryptedPrivateKeyType",
    "CostType",
    "CurrentDemandReqType",
    "CurrentDemandResType",
    "DC_EVChargeParameterType",
    "DC_EVPowerDeliveryParameterType",
    "DC_EVSEChargeParameterType",
    "DC_EVSEStatusType",
    "DC_EVStatusType",
    "DSAKeyValueType",
    "DiffieHellmanPublickeyType",
    "DigestMethodType",
    "DigestValueType",
    "EMAIDType",
    "EVChargeParameterType",
    "EVPowerDeliveryParameterType",
    "EVSEChargeParameterType",
    "EVSEStatusType",
    "EVStatusType",
    "EntryType",
    "IntervalType",
    "KeyInfoType",
    "KeyValueType",
    "ListOfRootCertificateIDsType",
    "ManifestType",
    "MessageHeaderType",
    "MeterInfoType",
    "MeteringReceiptReqType",
    "MeteringReceiptResType",
    "NotificationType",
    "ObjectType",
    "PGPDataType",
    "PMaxScheduleEntryType",
    "PMaxScheduleType",
    "ParameterSetType",
    "ParameterType",
    "PaymentDetailsReqType",
    "PaymentDetailsResType",
    "PaymentOptionListType",
    "PaymentServiceSelectionReqType",
    "PaymentServiceSelectionResType",
    "PhysicalValueType",
    "PowerDeliveryReqType",
    "PowerDeliveryResType",
    "PreChargeReqType",
    "PreChargeResType",
    "ProfileEntryType",
    "RSAKeyValueType",
    "ReferenceType",
    "RelativeTimeIntervalType",
    "RetrievalMethodType",
    "SAScheduleListType",
    "SAScheduleTupleType",
    "SASchedulesType",
    "SPKIDataType",
    "SalesTariffEntryType",
    "SalesTariffType",
    "SelectedServiceListType",
    "SelectedServiceType",
    "ServiceDetailReqType",
    "ServiceDetailResType",
    "ServiceDiscoveryReqType",
    "ServiceDiscoveryResType",
    "ServiceListType",
    "ServiceParameterListType",
    "ServiceType",
    "SessionSetupReqType",
    "SessionSetupResType",
    "SessionStopReqType",
    "SessionStopResType",
    "SignatureMethodType",
    "SignaturePropertiesType",
    "SignaturePropertyType",
    "SignatureType",
    "SignatureValueType",
    "SignedInfoType",
    "SubCertificatesType",
    "SupportedEnergyTransferModeType",
    "TransformType",
    "TransformsType",
    "V2G_Message",
    "WeldingDetectionReqType",
    "WeldingDetectionResType",
    "X509DataType",
    "X509IssuerSerialType"
]

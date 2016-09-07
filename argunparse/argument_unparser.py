# Copyright 2016  Mateusz Bysiek  http://mbdev.pl/
# This file is part of argunparse.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
class: ArgumentUnparser
"""

import collections
import logging
import typing

if __debug__:
    _LOG = logging.getLogger(__name__)

class ArgumentUnparser:
    """
    For performing reverse operation to what argparse.ArgumentParser does.
    """

    def __init__(
        self, short_arg: str='-', long_arg: str='--', arg_value='=',
        begin_delim: str='"', end_delim: str='"') -> None:

        assert isinstance(short_arg, str)
        assert isinstance(long_arg, str)
        assert isinstance(arg_value, str)
        assert isinstance(begin_delim, str)
        assert isinstance(end_delim, str)

        self._short_arg = short_arg
        self._long_arg = long_arg
        self._arg_value = arg_value
        self._begin_delim = begin_delim
        self._end_delim = end_delim

    def _unparse_arg(self, arg: str) -> str:

        assert isinstance(arg, str), arg

        if ' ' in arg:
            return '{}{}{}'.format(self._begin_delim, arg, self._end_delim)
        return arg
    
    def _unparse_flag(self, key: str, value: typing.Optional[str]) -> str:

        assert isinstance(key, str) and len(key) > 0, key
        assert value is None or (isinstance(value, str) and len(value) > 0), value

        return '{}{}{}'.format(
            self._long_arg if len(key) > 1 else self._short_arg, key,
            '' if value is None else (self._arg_value + self._unparse_arg(value)))

    def unparse_args(
            self, flags: typing.Mapping[str, typing.Union[bool, int, float, str]]={},
            args: typing.Sequence[str]=[]) -> str:
        """
        Convert dictionary and list to command-line args.

        This process is a reverse of what built-in argparse module does with parse_args() method.
        """

        assert isinstance(flags, collections.abc.Mapping)
        assert isinstance(args, collections.abc.Iterable)

        unparsed = []

        if __debug__:
            _LOG.debug('unparing flags: %s and arguments: %s', flags, args)

        for key, value in flags.items():
            if isinstance(value, bool):
                if value is True:
                    unparsed.append(self._unparse_flag(key, None))
            else:
                unparsed.append(self._unparse_flag(key, value))

        for arg in args:
            unparsed.append(self._unparse_arg(arg))

        if __debug__:
            _LOG.debug('unparsed flags and arguments into: %s', unparsed)
        return ' '.join(unparsed)

"""class: ArgumentUnparser"""

import collections
import logging
import typing as t

if __debug__:
    _LOG = logging.getLogger(__name__)

class ArgumentUnparser:

    """For performing reverse operation to what argparse.ArgumentParser does."""

    def __init__(
            self, short_opt: str = '-', long_opt: str = '--', opt_value: str = '=',
            begin_delim: str = '"', end_delim: str = '"') -> None:

        assert isinstance(short_opt, str)
        assert isinstance(long_opt, str)
        assert isinstance(opt_value, str)
        assert isinstance(begin_delim, str)
        assert isinstance(end_delim, str)

        self._short_opt = short_opt
        self._long_opt = long_opt
        self._opt_value = opt_value
        self._begin_delim = begin_delim
        self._end_delim = end_delim

    def unparse_arg(self, arg: t.Any) -> str:
        if not isinstance(arg, str):
            arg = str(arg)
        if ' ' in arg:
            return '{}{}{}'.format(self._begin_delim, arg, self._end_delim)
        return arg

    def unparse_args(
            self, options: t.Mapping[str, t.Union[bool, int, float, str]]={},
            args: t.Sequence[str]=[]) -> str:
        """Convert dictionary and list to command-line args.

        This process is a reverse of what built-in argparse module does with parse_args() method.
        """
        assert isinstance(options, collections.abc.Mapping)
        assert isinstance(args, collections.abc.Iterable)

        unparsed = []

        if __debug__:
            _LOG.debug('unparsing options: %s and arguments: %s', options, args)

        unparsed.append(self.unparse_options(options))

        for arg in args:
            unparsed.append(self.unparse_arg(arg))

        if __debug__:
            _LOG.debug('unparsed flags and arguments into: %s', unparsed)
        return ' '.join(unparsed)

    def unparse_option(self, key: str, value: t.Optional[str]) -> str:
        assert isinstance(key, str) and len(key) > 0, key
        assert value is None or (isinstance(value, str) and len(value) > 0), value

        return '{}{}{}'.format(
            self._long_opt if len(key) > 1 else self._short_opt, key,
            '' if value is None else (self._opt_value + self.unparse_arg(value)))

    def unparse_options(self, options: t.Mapping[str, t.Any]) -> str:
        unparsed = []
        for key, value in options.items():
            if isinstance(value, bool):
                if value is True:
                    unparsed.append(self.unparse_option(key, None))
            else:
                unparsed.append(self.unparse_option(key, value))
        return ' '.join(unparsed)

    def unparse(self, *args, **kwargs):
        """Unparse given args and kwargs adapting the approach depending on their values."""
        raise NotImplementedError()

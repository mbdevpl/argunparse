"""Argument unparser."""

import logging
import typing as t

_LOG = logging.getLogger(__name__)


def treat_as_option_with_no_value(value: t.Any) -> bool:
    """Determine if an option should be treated as a flag with no value."""
    return value is True


def option_should_be_skipped(value: t.Any) -> bool:
    """Determine if an option should be skipped."""
    return value is False or value is None


class ArgumentUnparser:
    """For performing reverse operation to what argparse.ArgumentParser does."""

    # pylint: disable = too-many-arguments, too-many-positional-arguments
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

    def unparse_arg(self, arg: t.Any) -> str:  # pylint: disable = no-self-use
        """Convert an object into a string that can be used as a command-line argument."""
        if not isinstance(arg, str):
            arg = str(arg)
        if ' ' in arg:
            arg = repr(arg)
        if not arg:
            arg = '""'
        return arg

    def unparse_args_to_list(self, arguments: t.Sequence[t.Any]) -> list[str]:
        """Convert list of objects to a list of command-line args."""
        unparsed_list = []
        for arg in arguments:
            unparsed_list.append(self.unparse_arg(arg))
        _LOG.debug('%s: unparsed args to %s', self, unparsed_list)
        return unparsed_list

    def unparse_args(self, arguments: t.Sequence[t.Any]) -> str:
        """Convert list to string of command-line args."""
        unparsed = ' '.join(self.unparse_args_to_list(arguments))
        _LOG.debug('%s: converted unparsed args to string "%s"', self, unparsed)
        return unparsed

    def unparse_option_to_list(self, key: str, value: t.Any) -> list[str]:
        """Convert a key-value pair into a short list to be used as a command-line option."""
        if option_should_be_skipped(value):
            return []
        unparsed_key = f'{self._long_opt if len(key) > 1 else self._short_opt}{key}'
        if treat_as_option_with_no_value(value):
            return [unparsed_key]
        unparsed_value = self.unparse_arg(value)
        if self._opt_value == ' ':
            return [unparsed_key, unparsed_value]
        return [f'{unparsed_key}{self._opt_value}{unparsed_value}']

    def unparse_option(self, key: str, value: t.Any) -> str:
        """Convert a key-value pair into a string that can be used as a command-line option."""
        if option_should_be_skipped(value):
            return ''
        unparsed = ' '.join(self.unparse_option_to_list(key, value))
        return unparsed

    def unparse_options_to_list(self, options: t.Mapping[str, t.Any]) -> list[str]:
        """Convert dictionary to a list of command-line args."""
        unparsed_list: t.List[str] = []
        for key, value in options.items():
            if option_should_be_skipped(value):
                continue
            unparsed_list += self.unparse_option_to_list(key, value)
        _LOG.debug('%s: unparsed options to %s', self, unparsed_list)
        return unparsed_list

    def unparse_options(self, options: t.Mapping[str, t.Any]) -> str:
        """Convert dictionary to string of command-line args."""
        unparsed = ' '.join(self.unparse_options_to_list(options))
        _LOG.debug('%s: converted unparsed options to string "%s"', self, unparsed)
        return unparsed

    def unparse_options_and_args_to_list(
            self, options: t.Mapping[str, t.Any], arguments: t.Sequence[t.Any]) -> list[str]:
        """Convert dictionary and list to a list of command-line args."""
        unparsed_options = [] if options is None else self.unparse_options_to_list(options)
        unparsed_args = [] if arguments is None else self.unparse_args_to_list(arguments)
        return unparsed_options + unparsed_args

    def unparse_options_and_args(
            self, options: t.Mapping[str, t.Any], arguments: t.Sequence[t.Any]) -> str:
        """Convert dictionary and list to string of command-line args."""
        return ' '.join(self.unparse_options_and_args_to_list(options, arguments))

    def unparse_to_list(self, *args, **kwargs) -> list:
        """Unparse given args as command-line arguments and kwargs as command-line options.

        Output is a list of strings.

        This process is a reverse of what built-in argparse module does with parse_args() method.
        """
        return self.unparse_options_and_args_to_list(kwargs, args)

    def unparse(self, *args, **kwargs) -> str:
        """Unparse given args as command-line arguments and kwargs as command-line options.

        This process is a reverse of what built-in argparse module does with parse_args() method.
        """
        return self.unparse_options_and_args(kwargs, args)

    def __str__(self):
        return f'{type(self).__name__}(short="{self._short_opt}",long="{self._long_opt}",' \
            f'value="{self._opt_value}")'

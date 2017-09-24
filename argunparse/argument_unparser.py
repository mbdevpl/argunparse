"""class: ArgumentUnparser"""

import collections
import typing as t


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
        """Convert an object into a string that can be used as a command-line argument."""
        if not isinstance(arg, str):
            arg = str(arg)
        if ' ' in arg:
            arg = repr(arg)
        return arg

    def unparse_args(
            self, arguments: t.Sequence[t.Any]) -> str:
        """Convert list to string of command-line args."""
        unparsed = []
        for arg in arguments:
            unparsed.append(self.unparse_arg(arg))
        return ' '.join(unparsed)

    def unparse_option(self, key: str, value: t.Optional[str]) -> str:
        """Convert a key-value pair into a string that can be used as a command-line option."""
        return '{}{}{}'.format(
            self._long_opt if len(key) > 1 else self._short_opt, key,
            '' if value is None else (self._opt_value + self.unparse_arg(value)))

    def unparse_options(self, options: t.Mapping[str, t.Any]) -> str:
        """Convert dictionary to string of command-line args."""
        unparsed = []
        for key, value in options.items():
            if isinstance(value, bool):
                if value:
                    unparsed.append(self.unparse_option(key, None))
            else:
                unparsed.append(self.unparse_option(key, value))
        return ' '.join(unparsed)

    def unparse_options_and_args(
            self, options: t.Mapping[str, t.Any], arguments: t.Sequence[t.Any]) -> str:
        """Convert dictionary and list to string of command-line args."""
        unparsed = []
        if options is not None:
            unparsed.append(self.unparse_options(options))
        if arguments is not None:
            unparsed.append(self.unparse_args(arguments))
        return ' '.join(unparsed)

    def unparse(self, *args, **kwargs):
        """Unparse given args as command-line arguments and kwargs as command-line options.

        This process is a reverse of what built-in argparse module does with parse_args() method.
        """
        return self.unparse_options_and_args(kwargs, args)

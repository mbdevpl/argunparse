"""class: ArgumentUnparser"""

import typing as t


def treat_as_option_with_no_value(value: t.Any) -> bool:
    return value is True


def option_should_be_skipped(value: t.Any) -> bool:
    return value is False or value is None


class ArgumentUnparser:

    """For performing reverse operation to what argparse.ArgumentParser does."""

    # pylint: disable=too-many-arguments
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
        if not arg:
            arg = '""'
        return arg

    def unparse_args(self, arguments: t.Sequence[t.Any],
                     *, to_list: bool = False) -> t.Union[str, t.List[str]]:
        """Convert list to string of command-line args."""
        unparsed = []
        for arg in arguments:
            unparsed.append(self.unparse_arg(arg))
        if to_list:
            return unparsed
        return ' '.join(unparsed)

    def unparse_option(self, key: str, value: t.Any,
                       *, to_list: bool = False) -> t.Union[str, t.List[str]]:
        """Convert a key-value pair into a string that can be used as a command-line option."""
        if option_should_be_skipped(value):
            return [] if to_list else ''
        unparsed_key = '{}{}'.format(self._long_opt if len(key) > 1 else self._short_opt, key)
        if not treat_as_option_with_no_value(value):
            unparsed_value = self.unparse_arg(value)
        if to_list and (self._opt_value == ' ' or treat_as_option_with_no_value(value)):
            if treat_as_option_with_no_value(value):
                return [unparsed_key]
            return [unparsed_key, unparsed_value]
        if not treat_as_option_with_no_value(value):
            unparsed_option = '{}{}{}'.format(unparsed_key, self._opt_value, unparsed_value)
        if to_list:
            return [unparsed_option]
        if treat_as_option_with_no_value(value):
            return unparsed_key
        return unparsed_option

    def unparse_options(self, options: t.Mapping[str, t.Any],
                        *, to_list: bool = False) -> t.Union[str, t.List[str]]:
        """Convert dictionary to string of command-line args."""
        unparsed = []
        for key, value in options.items():
            if option_should_be_skipped(value):
                continue
            unparsed_option = self.unparse_option(key, value, to_list=to_list)
            if to_list:
                unparsed += unparsed_option
            else:
                unparsed.append(unparsed_option)
        if to_list:
            return unparsed
        return ' '.join(unparsed)

    def unparse_options_and_args(self, options: t.Mapping[str, t.Any], arguments: t.Sequence[t.Any],
                                 *, to_list: bool = False) -> t.Union[str, t.List[str]]:
        """Convert dictionary and list to string of command-line args."""
        if options is None:
            unparsed_options = [] if to_list else ''
        else:
            unparsed_options = self.unparse_options(options, to_list=to_list)
        if arguments is None:
            unparsed_args = [] if to_list else ''
        else:
            unparsed_args = self.unparse_args(arguments, to_list=to_list)
        if to_list:
            return unparsed_options + unparsed_args
        unparsed = []
        if unparsed_options:
            unparsed.append(unparsed_options)
        if unparsed_args:
            unparsed.append(unparsed_args)
        return ' '.join(unparsed)

    def unparse_to_list(self, *args, **kwargs) -> list:
        """Unparse given args as command-line arguments and kwargs as command-line options.

        Output is a list of strings.

        This process is a reverse of what built-in argparse module does with parse_args() method.
        """
        return self.unparse_options_and_args(kwargs, args, to_list=True)

    def unparse(self, *args, **kwargs) -> str:
        """Unparse given args as command-line arguments and kwargs as command-line options.

        This process is a reverse of what built-in argparse module does with parse_args() method.
        """
        return self.unparse_options_and_args(kwargs, args)


import argparse
import shlex


class AdaptingArgumentParser(argparse.ArgumentParser):

    """An argument parser that adapts to all given arguments."""

    autoadded_arg_prefix = 'AUTOADDED_ARG_'

    def parse_args(self, args=None, namespace=None):
        known, unknown = self.parse_known_args(args=args, namespace=namespace)

        if not unknown:
            return known

        added_args = 0

        for arg in unknown:
            if arg[0] in self.prefix_chars:
                if '=' in arg:
                    arg = arg[:arg.index('=')]
                    self.add_argument(arg, help='automatically added option "{}"'.format(arg))
                else:
                    self.add_argument(arg, action='store_true',
                                      help='automatically added flag "{}"'.format(arg))
            else:
                added_args += 1
                self.add_argument('{}{}'.format(self.autoadded_arg_prefix, added_args),
                                  help='automatically added argument no.{}'.format(added_args))

        parsed_args = super().parse_args(args=args, namespace=namespace)
        return parsed_args


def _unescape(text: str):
    if not isinstance(text, str):
        return text
    shl = shlex.shlex(text)
    lst = list(shl)
    # if not lst:
    return ''.join(lst)
    # assert len(lst) == 1, (text, lst)
    # return lst[0]


def namespace_to_options_and_args(namespace: argparse.Namespace):
    """Convert Namespace object from argparse into correct input for argunparse"""
    options = {k: _unescape(v) for k, v in vars(namespace).items()
               if not k.startswith(AdaptingArgumentParser.autoadded_arg_prefix)}
    args = [_unescape(v) for k, v in vars(namespace).items()
            if k.startswith(AdaptingArgumentParser.autoadded_arg_prefix)]
    # args = [_unescape(_) if _.startswith('"') and _.endswith('"') else _
    #        for _ in args]
    # if any(isinstance(_, str) and _.startswith('"')
    #       for _ in itertools.chain(args, options.values())):
    #    _LOG.warning('options: %s args: %s', options, args)
    # _LOG.debug('options: %s args: %s', options, args)
    return options, args

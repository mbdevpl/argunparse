
import argparse
import logging

_LOG = logging.getLogger(__name__)


class DynamicArgumentParser(argparse.ArgumentParser):

    """Parser that dynamically adds parsing rules when unknown arguments are encountered."""

    def __init__(self):
        super().__init__(add_help=False, allow_abbrev=False)

    def parse_args(
            self, args=None, namespace=None, prefix_chars: str = '-_', opt_value: str = '='):
        self.prefix_chars = prefix_chars
        parsed, unknown = self.parse_known_args(args, namespace)
        if parsed:
            _LOG.error('parsed: %s', parsed)
        _LOG.debug('unknown: %s', unknown)
        for i, arg in enumerate(unknown):
            add_arg_kwargs = {}
            is_option = any(arg.startswith(_) for _ in prefix_chars)
            value_in_arg = opt_value in arg
            has_value = value_in_arg # or i < len(unknown) - 1 and not any(unknown[i + 1].startswith(_) for _ in prefix_chars)
            if has_value and value_in_arg:
                arg, _, value = arg.partition(opt_value)
                _LOG.warning('what to do with the value of %s? %s', arg, value)
            if is_option and not has_value:
                add_arg_kwargs['action'] = 'store_true'
            if is_option:
                self.add_argument(arg, **add_arg_kwargs)
            else:
                self.add_argument('n{}'.format(i))
        new_parsed = super().parse_args(args, namespace)
        _LOG.debug('new parsed: %s', new_parsed)
        return new_parsed


def main():
    return DynamicArgumentParser().parse_args()


if __name__ == '__main__':
    #print(main())
    #argparse.Namespace
    #exit(1)
    print(vars(main()))

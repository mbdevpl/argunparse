
import logging
import unittest

from argunparse.argument_unparser import ArgumentUnparser
from .examples import \
    OPTIONS_EXAMPLES, OPTIONS_VARIANTS, ARGUMENTS_EXAMPLES, ARGUMENTS_VARIANTS, \
    OPTIONS_AND_ARGUMENTS_VARIANTS

_LOG = logging.getLogger(__name__)


class Tests(unittest.TestCase):

    def assert_unparsed_correctly(self, options, arguments, result):
        _LOG.debug('validating unparsing of options: %s and arguments: %s', options, arguments)
        self.assertIsInstance(result, str, msg=(options, arguments, result))

    def test_construct(self):
        unparser = ArgumentUnparser()
        self.assertIsInstance(unparser, ArgumentUnparser)

    def test_options(self):
        unparser = ArgumentUnparser()
        for key, value in OPTIONS_EXAMPLES.items():
            result = unparser.unparse_option(key, value)
            self.assert_unparsed_correctly({key: value}, None, result)

    def test_option_sets(self):
        unparser = ArgumentUnparser()
        for example in OPTIONS_VARIANTS:
            result = unparser.unparse_options(example)
            self.assert_unparsed_correctly(example, None, result)
            result = unparser.unparse_options_and_args(example, None)
            self.assert_unparsed_correctly(example, None, result)

    def test_args(self):
        unparser = ArgumentUnparser()
        for arg in ARGUMENTS_EXAMPLES:
            result = unparser.unparse_arg(arg)
            self.assert_unparsed_correctly(None, [arg], result)

    def test_arg_sets(self):
        unparser = ArgumentUnparser()
        for example in ARGUMENTS_VARIANTS:
            result = unparser.unparse_args(example)
            self.assert_unparsed_correctly(None, example, result)
            result = unparser.unparse_options_and_args(None, example)
            self.assert_unparsed_correctly(None, example, result)

    def test_options_and_args(self):
        unparser = ArgumentUnparser()
        for example_options, example_arguments in OPTIONS_AND_ARGUMENTS_VARIANTS:
            result = unparser.unparse_options_and_args(example_options, example_arguments)
            self.assert_unparsed_correctly(example_options, example_arguments, result)

    def test_unparse(self):
        unparser = ArgumentUnparser()
        for example_options, example_arguments in OPTIONS_AND_ARGUMENTS_VARIANTS:
            result = unparser.unparse(*example_arguments, **example_options)
            self.assert_unparsed_correctly(example_options, example_arguments, result)

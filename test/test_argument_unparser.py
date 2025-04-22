
"""Tests for ArgumentUnparser class."""

import itertools
import logging
import unittest

from argunparse.argument_unparser import ArgumentUnparser
from .examples import \
    OPTIONS, OPTIONS_VARIANTS, OPTIONS_SKIPPED, OPTIONS_SKIPPED_VARIANTS, \
    ARGUMENTS, ARGUMENTS_VARIANTS, OPTIONS_AND_ARGUMENTS_VARIANTS

_LOG = logging.getLogger(__name__)


class Tests(unittest.TestCase):

    def test_construct(self):
        unparser = ArgumentUnparser()
        self.assertIsInstance(unparser, ArgumentUnparser)

    def test_option(self):
        unparser = ArgumentUnparser()
        for reference, option in OPTIONS.items():
            with self.subTest(option=option):
                key, value = list(*itertools.chain(option.items()))
                list_result = unparser.unparse_option_to_list(key, value)
                self.assertListEqual([reference], list_result)
                result = unparser.unparse_option(key, value)
                self.assertEqual(reference, result)

    def test_option_skipped(self):
        unparser = ArgumentUnparser()
        for option in OPTIONS_SKIPPED.items():
            with self.subTest(option=option):
                key, value = option
                list_result = unparser.unparse_option_to_list(key, value)
                self.assertListEqual(list_result, [])
                result = unparser.unparse_option(key, value)
                self.assertEqual(result, '')

    def test_option_space(self):
        unparser = ArgumentUnparser(opt_value=' ')
        for reference, option in OPTIONS.items():
            with self.subTest(option=option):
                key, value = list(*itertools.chain(option.items()))
                list_result = unparser.unparse_option_to_list(key, value)
                self.assertListEqual(reference.split('='), list_result)
                result = unparser.unparse_option(key, value)
                self.assertEqual(reference.replace('=', ' '), result)

    def test_options(self):
        _LOG.debug('testing %i option variants...',
                   len(OPTIONS_VARIANTS) + len(OPTIONS_SKIPPED_VARIANTS))
        unparser = ArgumentUnparser()
        for reference, options in itertools.chain(OPTIONS_VARIANTS, OPTIONS_SKIPPED_VARIANTS):
            with self.subTest(options=options):
                list_result = unparser.unparse_options_to_list(options)
                self.assertListEqual(reference, list_result)
                result = unparser.unparse_options(options)
                self.assertEqual(' '.join(reference), result)

    def test_options_space(self):
        _LOG.debug('testing %i option variants...',
                   len(OPTIONS_VARIANTS) + len(OPTIONS_SKIPPED_VARIANTS))
        unparser = ArgumentUnparser(opt_value=' ')
        for reference, options in itertools.chain(OPTIONS_VARIANTS, OPTIONS_SKIPPED_VARIANTS):
            with self.subTest(options=options):
                result = unparser.unparse_options(options)
                self.assertEqual(' '.join(reference).replace('=', ' '), result)
                list_result = unparser.unparse_options_to_list(options)
                fixed_reference = list(itertools.chain.from_iterable(
                    [_.split('=') if '=' in _ else [_] for _ in reference]))
                self.assertListEqual(fixed_reference, list_result)

    def test_arg(self):
        unparser = ArgumentUnparser()
        for reference, arg in ARGUMENTS:
            with self.subTest(arg=arg):
                result = unparser.unparse_arg(arg)
                self.assertEqual(reference, result)

    def test_args(self):
        unparser = ArgumentUnparser()
        for reference, args in ARGUMENTS_VARIANTS:
            with self.subTest(args=args):
                list_result = unparser.unparse_args_to_list(args)
                self.assertListEqual(reference, list_result)
                result = unparser.unparse_args(args)
                self.assertEqual(' '.join(reference), result)

    def test_options_and_args(self):
        unparser = ArgumentUnparser()
        for (reference_options, options), (reference_args, args) in OPTIONS_AND_ARGUMENTS_VARIANTS:
            with self.subTest(options=options, args=args):
                list_result = unparser.unparse_options_and_args_to_list(None, args)
                self.assertListEqual(reference_args, list_result)
                result = unparser.unparse_options_and_args(None, args)
                self.assertEqual(' '.join(reference_args), result)

                list_result = unparser.unparse_options_and_args_to_list(options, None)
                self.assertListEqual(reference_options, list_result)
                result = unparser.unparse_options_and_args(options, None)
                self.assertEqual(' '.join(reference_options), result)

                list_result = unparser.unparse_options_and_args_to_list(options, args)
                self.assertListEqual(reference_options + reference_args, list_result)
                result = unparser.unparse_options_and_args(options, args)
                self.assertEqual(
                    ' '.join(itertools.chain(reference_options, reference_args)), result)

    def test_unparse(self):
        unparser = ArgumentUnparser()
        for (reference_options, options), (reference_args, args) in OPTIONS_AND_ARGUMENTS_VARIANTS:
            with self.subTest(options=options, args=args):
                result = unparser.unparse(*args, **options)
                for item in itertools.chain(reference_options, reference_args):
                    self.assertIn(item, result)
                self.assertEqual(
                    ' '.join(itertools.chain(reference_options, reference_args)), result)
                list_result = unparser.unparse_to_list(*args, **options)
                self.assertSetEqual(set(reference_options + reference_args), set(list_result))
                self.assertListEqual(reference_options + reference_args, list_result)

    def test_unparse_nothing(self):
        unparser = ArgumentUnparser()
        _LOG.debug('testing unparsing nothing for: %s', unparser)
        self.assertEqual(unparser.unparse(), '')
        self.assertEqual(unparser.unparse_to_list(), [])

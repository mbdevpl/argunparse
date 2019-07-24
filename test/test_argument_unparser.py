
"""Tests for ArgumentUnparser class."""

import itertools
import logging
import sys
import unittest

from argunparse.argument_unparser import ArgumentUnparser
from .examples import \
    OPTIONS, OPTIONS_VARIANTS, OPTIONS_SKIPPED, OPTIONS_SKIPPED_VARIANTS, \
    ARGUMENTS, ARGUMENTS_VARIANTS, OPTIONS_AND_ARGUMENTS_VARIANTS
from .adapting_argparse import AdaptingArgumentParser, namespace_to_options_and_args

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
                result = unparser.unparse_option(key, value)
                self.assertEqual(reference, result)
                list_result = unparser.unparse_option(key, value, to_list=True)
                self.assertListEqual([reference], list_result)

    def test_option_skipped(self):
        unparser = ArgumentUnparser()
        for option in OPTIONS_SKIPPED.items():
            with self.subTest(option=option):
                key, value = option
                result = unparser.unparse_option(key, value)
                self.assertEqual(result, '')
                list_result = unparser.unparse_option(key, value, to_list=True)
                self.assertListEqual(list_result, [])

    def test_option_space(self):
        unparser = ArgumentUnparser(opt_value=' ')
        for reference, option in OPTIONS.items():
            with self.subTest(option=option):
                key, value = list(*itertools.chain(option.items()))
                result = unparser.unparse_option(key, value)
                self.assertEqual(reference.replace('=', ' '), result)
                list_result = unparser.unparse_option(key, value, to_list=True)
                self.assertListEqual(reference.split('='), list_result)

    def test_options(self):
        unparser = ArgumentUnparser()
        for reference, options in itertools.chain(OPTIONS_VARIANTS, OPTIONS_SKIPPED_VARIANTS):
            with self.subTest(options=options):
                result = unparser.unparse_options(options)
                self.assertEqual(' '.join(reference), result)
                list_result = unparser.unparse_options(options, to_list=True)
                self.assertListEqual(reference, list_result)

    def test_options_space(self):
        unparser = ArgumentUnparser(opt_value=' ')
        for reference, options in itertools.chain(OPTIONS_VARIANTS, OPTIONS_SKIPPED_VARIANTS):
            with self.subTest(options=options):
                result = unparser.unparse_options(options)
                self.assertEqual(' '.join(reference).replace('=', ' '), result)
                list_result = unparser.unparse_options(options, to_list=True)
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
                result = unparser.unparse_args(args)
                self.assertEqual(' '.join(reference), result)
                list_result = unparser.unparse_args(args, to_list=True)
                self.assertListEqual(reference, list_result)

    def test_options_and_args(self):
        unparser = ArgumentUnparser()
        for (reference_options, options), (reference_args, args) in OPTIONS_AND_ARGUMENTS_VARIANTS:
            with self.subTest(options=options, args=args):
                result = unparser.unparse_options_and_args(None, args)
                self.assertEqual(' '.join(reference_args), result)
                list_result = unparser.unparse_options_and_args(None, args, to_list=True)
                self.assertListEqual(reference_args, list_result)

                result = unparser.unparse_options_and_args(options, None)
                self.assertEqual(' '.join(reference_options), result)
                list_result = unparser.unparse_options_and_args(options, None, to_list=True)
                self.assertListEqual(reference_options, list_result)

                result = unparser.unparse_options_and_args(options, args)
                self.assertEqual(
                    ' '.join(itertools.chain(reference_options, reference_args)), result)
                list_result = unparser.unparse_options_and_args(options, args, to_list=True)
                self.assertListEqual(reference_options + reference_args, list_result)

    def test_unparse(self):
        unparser = ArgumentUnparser()
        for (reference_options, options), (reference_args, args) in OPTIONS_AND_ARGUMENTS_VARIANTS:
            with self.subTest(options=options, args=args):
                result = unparser.unparse(*args, **options)
                for item in itertools.chain(reference_options, reference_args):
                    self.assertIn(item, result)
                if sys.version_info[:2] >= (3, 6):
                    self.assertEqual(
                        ' '.join(itertools.chain(reference_options, reference_args)), result)
                list_result = unparser.unparse_to_list(*args, **options)
                self.assertSetEqual(set(reference_options + reference_args), set(list_result))
                if sys.version_info[:2] >= (3, 6):
                    self.assertListEqual(reference_options + reference_args, list_result)

    def test_unparse_nothing(self):
        unparser = ArgumentUnparser()
        self.assertEqual(unparser.unparse(), '')
        self.assertEqual(unparser.unparse_to_list(), [])

    def test_incorrectly_escaped(self):
        unparser = ArgumentUnparser()
        unparsed = unparser.unparse_arg('''" please"escape "''')
        self.assertEqual(unparsed, '''"\\" please\\"escape \\""''')
        unparsed = unparser.unparse_arg('''" please\\"escape "''')
        self.assertEqual(unparsed, '''"\\" please\\\\"escape \\""''')
        unparsed = unparser.unparse_arg('''\\ please\\"keep\\ ''')
        self.assertEqual(unparsed, '''\\ please\\"keep\\ ''')

    def test_roundtrip(self):
        unparser = ArgumentUnparser()
        for (_, options), (_, args) in OPTIONS_AND_ARGUMENTS_VARIANTS:
                parser = AdaptingArgumentParser(add_help=False)
            #with self.subTest(options=options, args=args):
                list_result = unparser.unparse_to_list(*args, **options)
                if any('has_newline' in _ for _ in list_result):
                    continue
                namespace = parser.parse_args(list_result)
                new_options, new_args = namespace_to_options_and_args(namespace)
                # self.assertCountEqual(new_args, args)
                # self.assertDictEqual(new_options, options)
                new_result = unparser.unparse_to_list(*new_args, **new_options)
                self.assertCountEqual(new_result, list_result)

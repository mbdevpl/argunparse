
import sys

from adapting_argparse import AdaptingArgumentParser, namespace_to_options_and_args
from argunparse import ArgumentUnparser

print(sys.argv)

parsed = AdaptingArgumentParser().parse_args()
print(parsed)

options, args = namespace_to_options_and_args(parsed)
print(options)
print(args)

unparsed = ArgumentUnparser().unparse(*args, **options)
print(unparsed)

"""Examples for tests of argunparse."""

import itertools
import pathlib

_UNPARSER_INIT_ARGS_EXAMPLES = [
    ('short_opt', {'-', '--', '_', '__'}),
    ('long_opt', {'-', '--', '_', '__'}),
    ('opt_value', {'=', ' ', ''})]

OPTIONS_EXAMPLES = {
    'h': True, 'help': True, 'v': True, 'version': True, 'verbosity': 100, 'output': 'stdout',
    'DEFINE': 'NDEBUG', 'long-flag': True, 'o': 'out_file.txt', 'log': 'log_file.txt',
    'what': 'is that', 'skipped': False}

ARGUMENTS_EXAMPLES = {
    'my_output_file.txt', 'C:\\Users\\user\\', '/home/user/Desktop', 'install', 'read', 'OutFile',
    0, 3.1415, True, False, None, pathlib.Path('tmp', 'file'),
    'in_file.txt', -123456790, 2**16, 'x', 'y', 'z', 'hello world'}

OPTIONS_VARIANTS = list(dict(_) for _ in itertools.permutations(OPTIONS_EXAMPLES.items(), 2))

ARGUMENTS_VARIANTS = list(itertools.permutations(ARGUMENTS_EXAMPLES, 2))

OPTIONS_AND_ARGUMENTS_VARIANTS = list(itertools.product(OPTIONS_VARIANTS, ARGUMENTS_VARIANTS))

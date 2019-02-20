"""Examples for tests of argunparse."""

import collections
import itertools
import pathlib

_UNPARSER_INIT_ARGS_EXAMPLES = [
    ('short_opt', {'-', '--', '_', '__'}),
    ('long_opt', {'-', '--', '_', '__'}),
    ('opt_value', {'=', ' ', ''})]

OPTIONS = {
    '-h': {'h': True}, '--verbosity=100': {'verbosity': 100},
    '--DEFINE=NDEBUG': {'DEFINE': 'NDEBUG'},
    '--long_flag': {'long_flag': True}, '-o=out_file.txt': {'o': 'out_file.txt'},
    '--log=log_file.txt': {'log': 'log_file.txt'}, "--what='is that'": {'what': 'is that'},
    '''--extra_args="ok 'well' yeah"''': {'extra_args': "ok 'well' yeah"}}

OPTIONS_VARIANTS = [
    ([ref1, ref2], collections.OrderedDict(itertools.chain(opt1.items(), opt2.items())))
    for ((ref1, opt1), (ref2, opt2)) in itertools.permutations(OPTIONS.items(), 2)]

OPTIONS_SKIPPED = {'skipped': False, 'e': False}

OPTIONS_SKIPPED_VARIANTS = [
    (['-v'], collections.OrderedDict([('v', True), ('skipped', None), ('e', False)])),
    (['--help'], collections.OrderedDict([('skipped', False), ('help', True), ('e', False)])),
    ([], collections.OrderedDict([('skipped', False), ('e', None)]))]

ARGUMENTS = {
    ('my_output_file.txt', 'my_output_file.txt'), ('C:\\Users\\user\\', 'C:\\Users\\user\\'),
    ('/home/user/Desktop', '/home/user/Desktop'), ('0', 0), ('""', ''),
    ('3.1415', 3.1415), ('True', True), ('False', False), ('None', None),
    (str(pathlib.Path('tmp', 'file')), pathlib.Path('tmp', 'file')), ('in_file.txt', 'in_file.txt'),
    ('-123456790', -123456790), (str(2**16), 2**16), ('x', 'x'), ('y', 'y'), ('z', 'z'),
    (repr('hello world'), 'hello world')}

ARGUMENTS_SKIPPED = {}

ARGUMENTS_VARIANTS = [([ref1, ref2], [arg1, arg2])
                      for ((ref1, arg1), (ref2, arg2)) in itertools.permutations(ARGUMENTS, 2)]

OPTIONS_AND_ARGUMENTS_VARIANTS = list(itertools.product(OPTIONS_VARIANTS, ARGUMENTS_VARIANTS))

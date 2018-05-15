# Based on the ttypager and supporting functions from pydoc, under the Python
# license, with various improvements.

import bits
import bits.input
import contextlib
import itertools
import os
import os.path
import pager
import redirect
import string
import sys
import textwrap
from cStringIO import StringIO

def getpager():
    return ttypager

def plain(text):
    """Remove boldface formatting from text."""
    import re
    return re.sub('.\b', '', text)

def ttypager(text):
    """Page through text on a text terminal."""
    try:
        import efi
        import readline
        efi_options = ["f to write file"]
    except ImportError as e:
        efi_options = []
    lines = string.split(plain(text), '\n')
    if redirect.state != redirect.NOLOG_STATE:
        with redirect.logonly():
            sys.stdout.write(string.join(lines, '\n') + '\n')
        if redirect.state == redirect.LOGONLY_STATE:
            return
    with pager.nopager():
        with redirect.nolog():
            height = min(bits.get_width_height(term)[1] for term in range(bits.get_term_count()))
            r = inc = height - 1
            sys.stdout.write(string.join(lines[:inc], '\n') + '\n')
            while True:
                if lines[r:]:
                    advance = ['any key to advance']
                else:
                    advance = ['END']
                if r > inc:
                    back = ["Up/PgUp to go back"]
                else:
                    back = []
                options = "; ".join(advance + back + efi_options + ["q to quit"])
                prompt = '-- {} --'.format(options)
                prompt_len = len(prompt)
                sys.stdout.write(prompt)
                c = bits.input.get_key()
                key = bits.input.key
                # Write the spaces one at a time to defeat word-wrap
                sys.stdout.write('\r')
                for i in range(prompt_len):
                    sys.stdout.write(' ')
                sys.stdout.write('\r')
                if efi_options and c in (key('f'), key('F')):
                    ttydir = efi.get_boot_fs()
                    filepath = os.path.normpath(str.strip(readline._readline("filename: "), "\n"))
                    basepath, fname = os.path.split(filepath)
                    for dirname in str.split(basepath, os.sep):
                        if dirname is not "":
                            ttydir = ttydir.mkdir(dirname)
                    print "Saving {}...".format(filepath),
                    ttydir.create(fname).write(string.join(lines, '\n') + '\n')
                    print "Done"
                    print "Hit any key to continue..."
                    c = bits.input.get_key()
                if c in (key('q'), key('Q')):
                    break
                elif c in (key('\r'), key('\n'), key(bits.input.KEY_DOWN), key('n', ctrl=True)):
                    if lines[r:]:
                        sys.stdout.write(lines[r] + '\n')
                        r = r + 1
                    continue
                if c == key(bits.input.KEY_HOME):
                    bits.clear_screen()
                    r = 0
                if c == key(bits.input.KEY_END):
                    bits.clear_screen()
                    r = len(lines) - inc
                    if r < 0:
                        r = 0
                if c in (key(bits.input.KEY_UP), key('p', ctrl=True)):
                    bits.clear_screen()
                    r = r - 1 - inc
                    if r < 0:
                        r = 0
                if c in (key(bits.input.KEY_PAGE_UP), key('b'), key('B')):
                    bits.clear_screen()
                    r = r - inc - inc
                    if r < 0:
                        r = 0
                if lines[r:]:
                    sys.stdout.write(string.join(lines[r:r+inc], '\n') + '\n')
                    r = r + inc
                    if not lines[r:]:
                        r = len(lines)

_wrapper = textwrap.TextWrapper(width=77, subsequent_indent='  ')
_wrapper_indentall = textwrap.TextWrapper(width=77, initial_indent='  ', subsequent_indent='  ')

def _wrap(str, indent=True):
    def __wrap():
        wrapper = _wrapper
        for line in str.split("\n"):
            # Preserve blank lines, for which wrapper emits an empty list
            if not line:
                yield ""
            for wrapped_line in wrapper.wrap(line):
                yield wrapped_line
            if indent:
                wrapper = _wrapper_indentall
    return '\n'.join(__wrap())

def ttypager_wrap(text, indent=True):
    ttypager(_wrap(text, indent))

class ProgressStringIO(object):
    def __init__(self):
        self.progress = itertools.cycle('|/-\\')
        self.gathering = 'Gathering output...'
        with pager.nopager():
            with redirect.nolog():
                sys.stdout.write('\r' + self.gathering)
        self.sio = StringIO()

    def write(self, s):
        with pager.nopager():
            with redirect.nolog():
                sys.stdout.write('\r' + self.gathering + self.progress.next())
        self.sio.write(s)

    def getvalue(self):
        with pager.nopager():
            with redirect.nolog():
                sys.stdout.write('\r' + ' ' * (len(self.gathering) + 1) + '\r')
        return self.sio.getvalue()

    def __getattr__(self, name):
        return getattr(self.sio, name)

@contextlib.contextmanager
def page():
    """Capture output to stdout/stderr, and send it through ttypager when done"""
    out = ProgressStringIO()
    with redirect._redirect_stdout(out):
        with redirect._redirect_stderr(out):
            try:
                yield
                output = out.getvalue()
            except:
                import traceback
                output = (traceback.format_exc()
                         + "\nOutput produced before exception:\n\n"
                         + out.getvalue())
    ttypager_wrap(output, indent=False)

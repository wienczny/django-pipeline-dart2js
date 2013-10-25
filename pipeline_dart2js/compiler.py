from os.path import dirname

from django.conf import settings
from pipeline.compilers import SubProcessCompiler

class Dart2jsCompiler(SubProcessCompiler):
    output_extension = 'js'

    def match_file(self, filename):
        return filename.endswith('.dart')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        if not outdated and not force:
            return  # No need to recompiled file
        
        command = "%s %s --out=%s %s" % (
            getattr(settings, 'PIPELINE_DART2JS_BINARY', '/usr/bin/env dart2js'),
            getattr(settings, 'PIPELINE_DART2JS_ARGUMENTS', ''),
            outfile,
            infile,
        )
        print(command)
        return self.execute_command(command, cwd=dirname(infile))


import os
import tempfile

from behave import step
from behaving.web.steps.downloads import *


@given(u'a manifest file with contents')
def create_manifest_file_with_contents(context):
    (manifest_file_handle, manifest_file_path) = tempfile.mkstemp(text=True)
    os.write(manifest_file_handle, context.text.encode())
    os.close(manifest_file_handle)
    context.manifest_file_path = manifest_file_path

@when(u'I run earthdatagrab')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I run earthdatagrab')

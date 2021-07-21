load("@rules_python//python:defs.bzl", "py_runtime_pair")
load(":label_flags.bzl", "print_output_files", "no_op_rule")

py_runtime(
    name = "py_runtime",
    files = glob(
        [".venv/**"],
        exclude = [
            # This is needed because the setuptools package contains file names with spaces,
            # And Bazel has problems with copying such files.
            # See https://github.com/bazelbuild/bazel/issues/4327
            # See https://github.com/pypa/setuptools/issues/134
            ".venv/**/setuptools/command/launcher manifest.xml",
            ".venv/**/setuptools/*.tmpl",
            ]
        ),
    interpreter = ".venv/bin/python",
    python_version = "PY3",
)

py_runtime_pair(
    name = "my_py_runtime_pair",
    py2_runtime = None,
    py3_runtime = ":py_runtime",
)

toolchain(
    name = "my_py_toolchain",
    toolchain = ":my_py_runtime_pair",
    toolchain_type = "@bazel_tools//tools/python:toolchain_type",
)

no_op_rule(name = "no-op")

label_flag(name = 'selected-target', build_setting_default = ":no-op")

print_output_files(name = "print-outputs")

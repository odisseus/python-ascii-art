load("@rules_python//python:defs.bzl", "py_runtime_pair")

py_runtime(
    name = "py_runtime",
    files = glob([".venv/**"]),
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

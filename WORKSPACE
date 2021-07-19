load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

git_repository(
    name = "rules_python",
    remote = "https://github.com/bazelbuild/rules_python.git",
    commit = "922702b18da2409d4bd9b838f575fa381ec400d4",
    shallow_since = "1624424560 +1000"
)

register_toolchains("//:my_py_toolchain")

load("@rules_python//python:pip.bzl", "pip_install")

pip_install(
    name = "my_deps",
    requirements = "//:python-deps.txt",
)
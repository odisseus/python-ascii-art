load("@my_deps//:requirements.bzl", "requirement")

py_library(
    name = "ascii_gen",
    srcs = ["python/ascii_gen.py"],
    visibility = ["//visibility:public"],
    imports = ["."],
    data = [":resources/roboto-mono.ttf"],
    deps = [requirement("Pillow")],
)

py_binary(
   name = "cli",
   srcs = ["python/cli.py"],
   main = "python/cli.py",
   deps = [":ascii_gen"],
)

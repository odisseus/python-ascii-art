py_library(
    name = "ascii_gen",
    srcs = ["python/ascii_gen.py"],
    visibility = ["//visibility:public"],
    imports = ["."],
    data = [":resources/roboto-mono.ttf"],
)

py_binary(
   name = "cli",
   srcs = ["python/cli.py"],
   main = "python/cli.py",
   deps = [":ascii_gen"],
)

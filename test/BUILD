load("@my_deps//:requirements.bzl", "requirement")
load("//:py_package_requirements.bzl", "py_package_requirements_rule")

filegroup(
    name = "test_data_set",
    srcs = glob([
        "resources/*.png",
        "resources/*.txt",
    ]),
)

py_library(
    name = "test_utils",
)

py_test(
    name = "ascii_art_generator_tests",
    srcs = glob(["python/*tests.py"]),
    main = "tests.py",
    size = "small",
    data = [":test_data_set"],
    deps = [
        "//src:ascii_gen",
        ":test_utils",
        requirement("pytest"),
        ],
    testonly = False,
)

py_package_requirements_rule(
    name = "python-requirements.txt",
    deps = ["ascii_art_generator_tests"]
)

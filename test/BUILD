filegroup(
    name = "test_data_set",
    srcs = glob([
        "resources/*.png",
        "resources/*.txt",
    ]),
)

py_test(
    name = "ascii_art_generator_tests",
    srcs = glob(["python/*.py"]),
    main = "tests.py",
    size = "small",
    data = [":test_data_set"],
    deps = ["//src:ascii_gen"],
)

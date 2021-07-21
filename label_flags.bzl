load("//:py_package_requirements.bzl", "py_package_requirements_rule")

def _print_output_files_impl(ctx):
    for f in ctx.attr._selected_target[DefaultInfo].files.to_list():
        print(f.path)
    return []

print_output_files = rule(
    implementation = _print_output_files_impl,
    attrs = {
        "_selected_target": attr.label(default = "//:selected-target"),
    },
)

def _no_op_rule_impl(ctx):
    print("This rule does nothing beside printing this message")
    return []

no_op_rule = rule(
    implementation = _no_op_rule_impl,
)

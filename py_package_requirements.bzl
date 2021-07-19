PyPackageDependencyInfo = provider(
    'Aggregate list of dependencies that look like Python targets',
    fields = {
        'count' : 'number of dependency entries',
        'names' : 'names and versions of dependencies'
    }
)

def _parse_metadata_file_label(file_label):
        #TODO parse the metadata itself?
        name_and_version = file_label[:file_label.index('.dist-info')]
        (py_name, dash, py_version) = name_and_version.rpartition('-')
        return struct(name = py_name, version = py_version)

def _py_package_requirements_aspect_impl(target, ctx):
    count = 0
    names = []
    for d in ctx.rule.attr.data:
        if d.label.name.endswith('/METADATA'):
            count = count + 1
            names.append(_parse_metadata_file_label(d.label.name))
            break
    for dep in ctx.rule.attr.deps:
        count = count + dep[PyPackageDependencyInfo].count
        names.extend(dep[PyPackageDependencyInfo].names)
    return [PyPackageDependencyInfo(count = count, names = names)]

py_package_requirements_aspect = aspect(
    implementation = _py_package_requirements_aspect_impl,
    attr_aspects = ['deps']
)

def _py_package_requirements_rule_impl(ctx):
    total_count = 0
    all_deps = []
    for dep in ctx.attr.deps:
        total_count = total_count + dep[PyPackageDependencyInfo].count
        all_deps.extend(dep[PyPackageDependencyInfo].names)
    out = ctx.actions.declare_file(ctx.label.name)
    ctx.actions.write(
        output = out,
        content = '\n'.join(['{} == {}'.format(dep.name, dep.version) for dep in all_deps])
    )
    return [DefaultInfo(files = depset([out]))]

py_package_requirements_rule = rule(
    implementation = _py_package_requirements_rule_impl,
    attrs = {
        'deps' : attr.label_list(aspects = [py_package_requirements_aspect])
    }
)
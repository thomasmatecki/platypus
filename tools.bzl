"""
Build Tools
"""

def _my_repo_rule_impl(repository_ctx):
    repository_ctx.file(
        "Foo.txt",
        """
Foo
""",
    )

    repository_ctx.file("BUILD", """filegroup(
    name = "files",
    srcs = ["Foo.txt"],
    visibility = ["//visibility:public"],
)""")
    print("YO!")

    return None

my_repo_rule = repository_rule(
    implementation = _my_repo_rule_impl,
    attrs = {},
)

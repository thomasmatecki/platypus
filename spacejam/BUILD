load("@python_deps//:requirements.bzl", "entry_point", "requirement")
load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")
load("@npm//tailwindcss:index.bzl", "tailwindcss")

filegroup(
    name="templates",
    srcs=glob(["**/jinja2/**/*.jinja"]),
)

tailwindcss(
    name="tailwind",
    args=[
        "-c",
        "$(location tailwind.config.js)",
        "-i",
        "$(location input.css)",
        "--content",
        "**/jinja2/**/*.jinja",
        "-o",
        "$(@D)/main.css",
    ],
    data=["input.css", "tailwind.config.js", "@npm//daisyui", ":templates"],
    output_dir=True,
)

py_binary(
    name="manage",
    srcs=glob(["**/*.py"]),
    deps=[
        requirement("django"),
        requirement("jinja2"),
        requirement("djangorestframework"),
        requirement("dj_database_url"),
        requirement("psycopg2"),
        requirement("pillow"),
    ],
    env={
        "CSS_DIRECTORY": "$(location :tailwind)",
    },
    data=[":tailwind", ":templates"],
)

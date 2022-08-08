load("@python_deps//:requirements.bzl", "requirement")
load("@npm//tailwindcss:index.bzl", "tailwindcss")

filegroup(
    name = "templates",
    srcs = glob(["**/jinja2/**/*.jinja"]),
)

tailwindcss(
    name = "tailwind",
    args = [
        "-c",
        "$(location tailwind.config.js)",
        "-i",
        "$(location input.css)",
        "--content",
        "**/jinja2/**/*.jinja",
        "-o",
        "$(@D)/main.css",
    ],
    data = [
        "input.css",
        "tailwind.config.js",
        ":templates",
        "@npm//daisyui",
    ],
    output_dir = True,
)

py_binary(
    name = "manage",
    srcs = glob(["**/*.py"]),
    data = [
        ":tailwind",
        ":templates",
        "@my_repo//:files",
    ],
    env = {
        "CSS_DIRECTORY": "$(location :tailwind)",
    },
    deps = [
        # All of these are added to PYTHONPATH
        requirement("django"),
        requirement("django-filter"),
        requirement("jinja2"),
        requirement("djangorestframework"),
        requirement("dj_database_url"),
        requirement("psycopg2"),
        requirement("pillow"),
    ],
)

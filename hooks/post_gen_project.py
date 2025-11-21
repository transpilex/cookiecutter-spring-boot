import json
from pathlib import Path

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "


def remove_gulp_files():
    file_names = ["gulpfile.js"]
    for file_name in file_names:
        Path(file_name).unlink()


def remove_vite_files():
    file_names = ["vite.config.js"]
    for file_name in file_names:
        Path(file_name).unlink()


def remove_packagejson_file():
    file_names = ["package.json"]
    for file_name in file_names:
        Path(file_name).unlink()


def update_package_json(remove_dev_deps=None, remove_keys=None, scripts=None):
    remove_dev_deps = remove_dev_deps or []
    remove_keys = remove_keys or []
    scripts = scripts or {}
    package_json = Path("package.json")
    content = json.loads(package_json.read_text())
    for package_name in remove_dev_deps:
        content["devDependencies"].pop(package_name)
    for key in remove_keys:
        content.pop(key)
    content["scripts"].update(scripts)
    updated_content = json.dumps(content, ensure_ascii=False, indent=2) + "\n"
    package_json.write_text(updated_content)


def handle_js_runner(frontend_pipeline, ui_library):
    if frontend_pipeline == "Gulp":
        if ui_library == "Tailwind":
            scripts = {"dev": "gulp", "build": "gulp build"}
            remove_dev_deps = [
                "@tailwindcss/vite",
                "glob",
                "path",
                "vite",
                "sass",
                "gulp-sass",
                "gulp-uglify-es",
                "node-sass-tilde-importer",
                "gulp-rtlcss",
            ]
        else:
            scripts = {
                "dev": "gulp",
                "build": "gulp build",
                "rtl": "gulp rtl",
                "rtl-build": "gulp rtlBuild",
            }
            remove_dev_deps = [
                "@tailwindcss/postcss",
                "@tailwindcss/vite",
                "glob",
                "path",
                "vite",
            ]
        update_package_json(remove_dev_deps=remove_dev_deps, scripts=scripts)
        remove_vite_files()
    elif frontend_pipeline == "Vite":
        scripts = {"dev": "vite", "build": "vite build"}
        if ui_library == "Tailwind":
            remove_dev_deps = [
                "@tailwindcss/postcss",
                "autoprefixer",
                "cssnano",
                "gulp",
                "gulp-concat",
                "gulp-plumber",
                "gulp-npm-dist",
                "gulp-postcss",
                "gulp-rename",
                "gulp-replacegulp-rtlcss",
                "gulp-sass",
                "gulp-uglify-es",
                "node-sass-tilde-importer",
                "pixrem",
                "postcss",
                "sass",
            ]
        else:
            remove_dev_deps = [
                "@tailwindcss/postcss",
                "@tailwindcss/vite",
                "autoprefixer",
                "cssnano",
                "gulp",
                "gulp-concat",
                "gulp-plumber",
                "gulp-npm-dist",
                "gulp-postcss",
                "gulp-rename",
                "gulp-replacegulp-rtlcss",
                "gulp-sass",
                "gulp-uglify-es",
                "node-sass-tilde-importer",
                "pixrem",
                "postcss",
            ]

        update_package_json(remove_dev_deps=remove_dev_deps, scripts=scripts)
        remove_gulp_files()


def main():
    if "{{ cookiecutter.frontend_pipeline }}" in ["None"]:
        remove_gulp_files()
        remove_vite_files()
        remove_packagejson_file()
    else:
        handle_js_runner(
            "{{ cookiecutter.frontend_pipeline }}", "{{ cookiecutter.ui_library }}"
        )

    print(SUCCESS + "Project initialized, keep up the good work!" + TERMINATOR)


if __name__ == "__main__":
    main()

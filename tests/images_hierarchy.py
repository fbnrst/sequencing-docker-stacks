# Copyright (c) Jupyter Development Team.
# Copyright (c) 2025-, Fabian Rost
# Distributed under the terms of the Modified BSD License.
from pathlib import Path

THIS_DIR = Path(__file__).parent.resolve()

ALL_IMAGES = {
    "rnaseq-notebook": None,
}


def get_test_dirs(
    short_image_name: str | None,
) -> list[Path]:
    if short_image_name is None:
        return []

    test_dirs = get_test_dirs(ALL_IMAGES[short_image_name])
    if (current_image_tests_dir := THIS_DIR / short_image_name).exists():
        test_dirs.append(current_image_tests_dir)
    return test_dirs

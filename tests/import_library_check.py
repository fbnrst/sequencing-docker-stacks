# Copyright (c) 2025-, Fabian Rost
# Distributed under the terms of the Modified BSD License.
import logging

from tests.conftest import TrackedContainer

LOGGER = logging.getLogger(__name__)


def import_library(container: TrackedContainer, library: str) -> None:
    """Check whether library \"{library}\" can be loaded"""
    LOGGER.info(f"Test that library \"{library}\" can be loaded ...")
    expected_string = f"Library \\\"{library}\\\" successfully loaded."
    command = ["python", "-c", f"import {library}; print(\"{expected_string}\")"]
    logs = container.run_and_wait(
        timeout=10,
        tty=True,
        command=command,
    )
    LOGGER.debug(f"{logs=}")
    assert expected_string in logs, f"Loading library \"{library}\" failed: {logs=}"

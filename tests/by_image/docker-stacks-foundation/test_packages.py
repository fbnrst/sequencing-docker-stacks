# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

"""
test_packages
~~~~~~~~~~~~~~~
This test module tests if the R and Python packages installed can be imported.
It's a basic test aiming to prove that the package is working properly.

The goal is to detect import errors that can be caused by incompatibilities between packages, for example:

- #1012: issue importing `sympy`
- #966: issue importing `pyarrow`

This module checks dynamically, through the `CondaPackageHelper`,
only the requested packages i.e. packages requested by `mamba install` in the `Dockerfile`s.
This means that it does not check dependencies.
This choice is a tradeoff to cover the main requirements while achieving a reasonable test duration.
However, it could be easily changed (or completed) to cover dependencies as well.
Use `package_helper.installed_packages` instead of `package_helper.requested_packages`.
"""

import logging
from collections.abc import Callable

import pytest  # type: ignore

from tests.utils.conda_package_helper import CondaPackageHelper
from tests.utils.tracked_container import TrackedContainer

LOGGER = logging.getLogger(__name__)

# Mapping between package and module name
PACKAGE_MAPPING = {
    # Python
    "beautifulsoup4": "bs4",
    "biopython": "Bio",
    "decoupler-py": "decoupler",
    "jupyter-pluto-proxy": "jupyter_pluto_proxy",
    "matplotlib-base": "matplotlib",
    "napari-spatialdata": "napari_spatialdata",
    "opencv": "cv2",
    "pytables": "tables",
    "python-igraph": "igraph",
    "scikit-image": "skimage",
    "scikit-learn": "sklearn",
    "scikit-misc": "skmisc",
    "scvi-tools": "scvi",
    "session-info": "session_info",
    "spatial-image": "spatial_image",
    "spatialdata-io": "spatialdata_io",
    "spatialdata-plot": "spatialdata_plot",
    "tangram-sc": "tangram",
    # R
    "biocparallel": "BiocParallel",
    "biomart": "biomaRt",
    "clusterprofiler": "clusterProfiler",
    "complexheatmap": "ComplexHeatmap",
    "deseq2": "DESeq2",
    "ggally": "GGally",
    "glmgampoi": "glmGamPoi",
    "gseabase": "GSEABase",
    "gsva": "GSVA",
    "gviz": "Gviz",
    "loomexperiment": "LoomExperiment",
    "mast": "MAST",
    "milor": "miloR",
    "mofa2": "MOFA2",
    "org.hs.eg.db": "org.Hs.eg.db",
    "org.mm.eg.db": "org.Mm.eg.db",
    "paralleldist": "parallelDist",
    "randomforest": "randomForest",
    "rcurl": "RCurl",
    "reactomepa": "ReactomePA",
    "robustrankaggreg": "RobustRankAggreg",
    "rodbc": "RODBC",
    "rsqlite": "DBI",
    "seurat": "Seurat",
    "singlecellexperiment": "SingleCellExperiment",
    "variancepartition": "variancePartition",
}

# List of packages that cannot be tested in a standard way
EXCLUDED_PACKAGES = [
    "bzip2",
    "ca-certificates",
    "conda-forge::blas=*",
    "grpcio-status",
    "grpcio",
    "hdf5",
    "jupyter-server-proxy",
    "jupyterhub-singleuser",
    "jupyterlab_execute_time",
    "jupyterlab-git",
    "mamba",
    "notebook>",
    "openssl",
    "protobuf",
    "pyqt",
    "python",
    "r-irkernel",
    "unixodbc",
]


def is_r_package(package: str) -> bool:
    """Check if a package is an R package"""
    return package.startswith("r-") or package.startswith("bioconductor-")


def get_package_import_name(package: str) -> str:
    """Perform a mapping between the package name and the name used for the import"""
    if is_r_package(package):
        if package.startswith("r-"):
            package = package[2:]
        elif package.startswith("bioconductor-"):
            package = package[13:]

    if "<" in package:
        package = package.split("<")[0]
    elif ">" in package:
        package = package.split(">")[0]
    elif "=" in package:
        package = package.split("=")[0]
    return PACKAGE_MAPPING.get(package, package)


def check_import_python_package(container: TrackedContainer, package: str) -> None:
    """Try to import a Python package from the command line"""
    container.exec_cmd(f'python -c "import {package}"')


def check_import_r_package(container: TrackedContainer, package: str) -> None:
    """Try to import an R package from the command line"""
    container.exec_cmd(f"R --slave -e library({package})")


def _check_import_packages(
    container: TrackedContainer,
    packages_to_check: list[str],
    check_function: Callable[[TrackedContainer, str], None],
) -> None:
    """Test if packages can be imported"""
    failed_imports = []
    LOGGER.info("Testing the import of packages ...")
    for package in packages_to_check:
        LOGGER.info(f"Trying to import {package}")
        try:
            check_function(container, package)
        except AssertionError as err:
            failed_imports.append(package)
            LOGGER.error(f"Failed to import package: {package}, output:\n  {err}")
    if failed_imports:
        pytest.fail(f"following packages are not import-able: {failed_imports}")


def get_r_packages(package_helper: CondaPackageHelper) -> list[str]:
    """Return a list of R packages"""
    return [
        get_package_import_name(pkg)
        for pkg in package_helper.requested_packages
        if is_r_package(pkg) and pkg not in EXCLUDED_PACKAGES
    ]


def test_r_packages(container: TrackedContainer) -> None:
    """Test the import of specified R packages"""
    r_packages = get_r_packages(CondaPackageHelper(container))
    _check_import_packages(container, r_packages, check_import_r_package)


def get_python_packages(package_helper: CondaPackageHelper) -> list[str]:
    """Return a list of Python packages"""
    return [
        get_package_import_name(pkg)
        for pkg in package_helper.requested_packages
        if not is_r_package(pkg) and pkg not in EXCLUDED_PACKAGES
    ]


def test_python_packages(container: TrackedContainer) -> None:
    """Test the import of specified python packages"""
    python_packages = get_python_packages(CondaPackageHelper(container))
    _check_import_packages(container, python_packages, check_import_python_package)

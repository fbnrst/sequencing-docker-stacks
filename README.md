# Sequencing Jupyter Docker Stacks

[![GitHub Actions Badge](https://github.com/fbnrst/sequencing-docker-stacks/actions/workflows/docker.yml/badge.svg)](https://github.com/fbnrst/sequencing-docker-stacks/actions/workflows/docker.yml?query=branch%3Amain "Docker image build status")
[![Read the Docs Badge](https://img.shields.io/readthedocs/sequencing-docker-stacks.svg)](https://sequencing-docker-stacks.readthedocs.io/en/latest/ "Documentation build status")
[![Run Pre-Commit Hooks](https://github.com/fbnrst/sequencing-docker-stacks/actions/workflows/pre-commit.yml/badge.svg?branch=main)](https://github.com/fbnrst/sequencing-docker-stacks/actions/workflows/pre-commit.yml)
[![Binder Badge](https://static.mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fbnrst/sequencing-docker-stacks/main?urlpath=lab/tree/README.ipynb "Launch a quay.io/jupyter/base-notebook container on mybinder.org")

**Sequencing Docker Stacks** provide ready-to-run [Docker images](https://quay.io/user/fbnrst/) tailored for sequencing data analysis.
They are built upon the [jupyter/docker-stacks](https://github.com/jupyter/docker-stacks) and the [Singularity Single Cell container](https://gitlab.hrz.tu-chemnitz.de/dcgc-bfx/singularity/singularity-single-cell).

## Available Containers

- **`rnaseq-notebook`**: Supports bulk RNA-seq analysis, powered by [DESeq2](https://bioconductor.org/packages/release/bioc/html/DESeq2.html).
- **`singlecell-notebook`**: Enables single-cell RNA-seq analysis, incorporating [Scanpy](https://scanpy.readthedocs.io/en/stable/) and [Seurat](https://satijalab.org/seurat/).
- **`spatial-notebook`**: Facilitates spatial transcriptomics, featuring [Squidpy](https://squidpy.readthedocs.io/en/stable/) and [SpatialData](https://spatialdata.scverse.org/en/stable/).
- **`multiomics-notebook`**: Designed for multi-omics analysis, including [MOFA2](https://biofam.github.io/MOFA2/) and [muon](https://github.com/scverse/muon).

Complete build manifests detailing the software stack are available in the [wiki](https://github.com/fbnrst/sequencing-docker-stacks/wiki).

## Quick Start

For a smooth start, consider exploring [jupyter/docker-stacks](https://github.com/jupyter/docker-stacks) first.
There, working with Jupyter docker images is explained in detail, including how to run a Jupyter Server and access it via a web browser.

If you [have Docker installed](https://docs.docker.com/get-started/get-docker/), and know which image suits your needs, you can launch a single Jupyter application in a container.

### Example

Run the following command to pull the `singlecell-notebook` image (tagged `latest`) from Quay.io. It starts a container running a Jupyter Server with the JupyterLab frontend, exposing port `8888`:

```bash
docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work quay.io/fbnrst/singlecell-notebook:latest
```

## CPU Architectures

- Containers are available for both `x86_64` and `aarch64` platforms.
- Single-platform images use architecture-specific tag prefixes, such as:
  `quay.io/fbnrst/rnaseq-notebook:aarch64-python-3.12.10`

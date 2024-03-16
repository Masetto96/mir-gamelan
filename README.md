# Computational Analysis of Gamelan Gong Kebyar Tuning for Geographic Classification

## Description

Pitch detection algorithms have not been extensively explored for non-eurogenetic musical traditions, despite the rich theoretical foundation provided by ethnomusicology. In an effort to address this gap, our research takes a practical approach by examining contemporary pitch detec- tion methods and applying them to a case study. We propose a pitch detection tool for gamelan gong kebyar, a traditional Balinese ensemble. By focusing on this particular case study, we hope to provide insights that can be applied to develop tools for other music traditions.

## Installation

We used Python `3.11.7`. You can run `pip install -r requirements.txt` to install the dependencies. We recommend using a virtual environment to avoid conflicts with other projects.

## Usage

### Pipeline

`pipeline.ipynb`: This notebook implements a pipeline described in a report. It takes an audio file as input, extracts a gamelan tuning vector, compares it with three different theory-based tuning vectors, and predicts the regency of the gamelan.

### Experiments

`experiments.ipynb`: This notebook contains several attempts that haven't produced promising results and have thus not been included in the main pipeline.

### Helpers

`helpers.py`: This file contains helpers functions used in the implementation of the main pipeline (e.g. find_stable_regions, find_scale).

### Analysis

`gamelan_tuning_analysis.ipynb`: This notebook contains the analysis and visualization of the distribution of the data in the Toth spreasheets. It also extracts the pemade tunings and stores them in a pickle file.

# Profile-Based Subgroup Discovery (PSD)

This repository corresponds to the Master's thesis in Artificial Intelligence by Dionne Gantzert, at University of Amsterdam, 2024. This research is part of a project on Bias Identification methods initiated by Rhite and has been guided and supervised by Rhite and the University of Amsterdam.

The research introduces Profile-Based Subgroup Discovery, and compares it to two other subgroup discovery techniques: DFS and VLSD.

**⚠️ Note on Code Quality**

Please note that this code was developed as part of a thesis project and, due to time constraints, has not undergone extensive optimization or formal quality checks. While it serves the primary purpose of supporting the research findings, it may not meet industry standards in terms of performance, maintainability, security or robustness.

Users are welcome to use and explore the code, but we recommend careful consideration and further testing before applying it in any production environment. Contributions for improvements or optimizations are also encouraged.

Since this research is based on [PEBAM](https://github.com/mcwilms/PEBAM), we continued the work in notebooks as well. 

If you want to see just the results, we refer to `Results Comparison/Visualize_results.ipynb`.

For each of the methods, you will find their descriptive process in the following files:
- PSD: `PSD_descriptions.ipynb` and `PSD_results.ipynb`
- DFS: `pysubgroup/DFS_GermanCredit.py` and `process_DFS_descriptions.ipynb`
- VLSD: `VLSD.ipynb` and `VLSD_results.ipynb`

We would have liked to introduce a better pipeline, but due to time constraints we were not able to convert everything to python files.

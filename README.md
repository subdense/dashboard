# Subdense collaborative dashboard

This github project aims at [modeling building changes](https://doi.org/10.3390/ijgi14040155) in urban functional areas. Building changes can be for example apparition of built up areas, or roof-stacking of existing buildings. Changes are detected either using data natively adapted to diachronic analysis or by comparing vintages of regional or national surveys and analysing the source documentation to evaluate what changes in data are explained by changes in the survey process, and what changes are explained by a change in reality. Detected changes are then stylised, possibly processed, to produce legible maps of building changes on specific timelaps and territories. 

Such comparative maps of building changes are dedicated to 1) scientific studies to grasp local variations in different phenomena 2) more open debate about these changes with all involved stakeholders, incl. inhabitants and scientists. 

Please feel free to use this project maps and tools, published on the [website](http://subdense.github.io/dashboard/) or to contribute to it.

## How to contribute

- Publish the study of a new area or new time period : create a Study file to scope the study, then use available resource to conduct the study and share your results
- Share your expertise related to a datasource : either in the Data folder or within a specific Study
- Share your expertise related to a process : either in the Processes folder or within a specific Study
- Share metadata about produced datasets or maps : either in the Data and Maps folders or within a specific Study
- Share your expertise related to concepts : clarifying them or proposing new materials for evidence-based discussions

## How to synchronize the dashboard website

1. Every time you add a new Markdown file (.md) as a tab on the website, you must create a symbolic link inside the docs directory pointing to your original file. Run the following commands from your project root:

```bash
cd docs
ln -s ../<path-to-original-file> <link-name>.md
```

2. Update the website configuration: open main.yml and add your new page to the navigation list so it appears on the website.

The dashboard is named after the ORA7 [SUBDENSE](https://bbv.raumplanung.tu-dortmund.de/research/projects/subdense/) 2023-25 project. This work has been funded by the french ANR grant ANR-22-ORAR-0004-04, the german DFG grant 502663987 and by the british ESRC grant ES/X008290/1.

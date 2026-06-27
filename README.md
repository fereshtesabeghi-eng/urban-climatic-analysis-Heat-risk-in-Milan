# Heat Risk in Milan: Urban Climatic Analysis

## 📖 Project Background

This research addresses the escalating urban heat crisis in Milan, Italy, by evaluating the spatial distribution of heat-related risks. The study was motivated by the documented increase in frequency and intensity of heat waves and the aggravating effect of the Urban Heat Island (UHI) phenomenon on public health, particularly for vulnerable populations such as the elderly. The primary aim was to identify which of Milan's 88 Nuclei di Identità Locale (NIL) sub-districts are most susceptible to extreme heat.

![Historical Climate Trend](assets/historical_climate_trend.jpg)

## ⚙️ The Research Process

The project followed a rigorous multi-stage analytical framework to operationalize "heat risk" as a function of hazard, exposure, and vulnerability.

### 1. Data Acquisition & Preprocessing

* **Meteorological Data**: Extracted hourly ERA5 reanalysis variables—including air temperature, dew point, wind speed, and solar radiation—from the Copernicus Climate Data Store (CDS).
* **Demographic Data**: Sourced from the Municipality of Milan’s open data portal, specifically the "Caratteristiche Demografiche Territoriali Quartiere" dataset, to determine population density and the percentage of senior citizens per NIL.
* **Environmental Data**: Utilized regional Geoportal vector layers for building footprints and DTMs, alongside Copernicus Urban Atlas land cover data to assign emissivity and albedo values.

### 2. Microclimate Simulation

* **Temporal Selection**: Through Python-based analysis of multi-dimensional datasets, July 2012 was selected as the study period, with July 27th identified as the peak thermally stressful day.

![UTCI Temporal Analysis](assets/milan_utci_temporal_analysis.jpg)

* **SOLWEIG Modeling**: Used the SOLWEIG module within the QGIS UMEP toolbox to simulate complex radiation fluxes.
* **High-Resolution Modeling**: Generated surface models (Ground & Building DSM, Tree Canopy DSM) to calculate critical parameters like the Sky View Factor (SVF), wall height, and wall aspect, which dictate urban microclimates.

### 3. Composite Index Development

* **Normalization**: Standardized all variables (UTCI, population density, senior citizen percentages) using the Min-Max normalization method.
* **HRI Calculation**: Applied an expression-based formula in a GIS environment to integrate these standardized layers into a final Heat Risk Index (HRI).

## 📊 Key Results & Findings

The research produced high-resolution spatial snapshots of thermal stress and risk levels across Milan.

* **Spatial Inequality**: Significant spatial variations in heat risk were identified across the 88 NILs.

![Demographic Vulnerability](assets/milan_demographic_vulnerability.jpg)

* **Priority Intervention Zones**: High-risk areas characterized by the convergence of high population density, aging demographics, and high UTCI values include San Siro, Loreto, and Trenno.
* **Protective Landscapes**: Areas such as Parco delle Abbazie, Parco Forlanini-Cavriano, and Parco Sempione showed lower risk indices due to higher vegetation coverage and more favorable microclimatic conditions.

![UTCI Map Milano](assets/utci_map_milano_2012.jpg)

* **Methodological Contribution**: The study demonstrates that relying on Land Surface Temperature (LST) is insufficient for urban health assessment. Instead, we advocate for composite indices that integrate biometeorological factors like air temperature, relative humidity, and solar radiation, which more accurately reflect human thermal discomfort in dense urban environments.

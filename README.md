# Data Visualization Project

## Description

This project involves reading data from multiple files, each containing temperature data represented in different number systems (binary, quaternary, and octal). The data is converted to decimal format, visualized using **Matplotlib**,**Numpy** and optionally smoothed using spline interpolation from **SciPy**. Additionally, the project offers functionality to plot specific sections of the data on the x-axis.

## Features

- **Data Reading and Conversion**: Read temperature data from files in different number systems and convert them to decimal format.
- **Plotting Functions**: Two main plotting functions are available: `defaultExecute` for default plotting settings and `executeWithOptions` for customizable plot parameters.
- **Spline Interpolation**: Smooth the plotted curves using spline interpolation to enhance visualization.
- **Plot Specific Sections**: Utilize the `plot_section_of_time` function to plot specific sections of the data on the x-axis.

## Installation

Clone the repository:

```bash
git clone https://github.com/Aziz-fer/txt-data-analysis.git
```
Install the required dependencies:
```bash
pip install numpy matplotlib scipy
```
## Usage
Run defaultExecute() to generate default plots with default settings.

![data_binary](https://github.com/Aziz-fer/txt-data-analysis/assets/64703046/76886f39-623e-4630-9640-ff2a000640e7)

Alternatively, customize the plotting settings by calling executeWithOptions(grid: bool, dpi2: int, dotcolor: str).

![data_quad](https://github.com/Aziz-fer/txt-data-analysis/assets/64703046/c980fb83-9458-4d37-ab9b-daf6f3af9c87)
![data_octal](https://github.com/Aziz-fer/txt-data-analysis/assets/64703046/81ff468e-6829-4b7d-ad8f-6ea748aa1b71)

For plotting specific sections of the data, use plot_section_of_time(file_name, system, time_interval).

![Screenshot 2024-04-24 130630](https://github.com/Aziz-fer/txt-data-analysis/assets/64703046/5a05f99e-0e19-446b-9fa8-576a3e26e82e) 

We can see that this plots temperature in only the interval of the first 1000 hours-

## File Structure
- **data**: Contains input data files in different number systems (binary,octal,quad).
- **README.md**: Documentation for the project.
- **data_analysis of txt files.py**: Main Python script containing data processing and visualization functions.
## Contributions
Contributions to this project are welcome! Please fork the repository, make your changes, and submit a pull request.


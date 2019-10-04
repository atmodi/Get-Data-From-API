# Get Data From API

## Requirement: 

There was a need to download the data via API instead of manually extracting the data from the dashboard. The vendor provided the API to extract the data in batches.

A script is designed to download the data by changing multiple paramenters and having offset functionality.

## Sanitization:

Sincet the API url and the keys are for personal use they have been santizied.

## Input:

The input file is a csv file with two columns:
- Countries
- PID

The PID is passed to the UDF and the Countries is added by broadcasting.

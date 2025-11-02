# ICS_Labs

## Overview
ICS_Labs is a collection of hands-on machine learning and network security exercises focused on intrusion detection for Industrial Control Systems, featuring dataset analysis, flow generation, custom distance metrics, and an unsupervised stacked denoising autoencoder pipeline

## Structure
- `Brute_forcing/` - cryptanalysis examples and brute force experiments relevant to feature robustness in ML models  
- `Buffer_over_Flow/` - exploitation labs that demonstrate memory corruption, used to generate adversarial samples for IDS evaluation  
- `MD5_PDF_Collision/` - practical MD5 collision artifacts and scripts for studying data integrity attacks and their impact on ML-based detection  
- `Man_in_the_Middle/` - ARP poisoning and TCP payload modification experiments for creating realistic attack traffic for supervised and unsupervised models  
- `TryhackmeLabs/` - curated exercises for network security fundamentals and threat modeling  
- `Web-Vulnralibilities/` - web attack patterns useful for feature engineering in intrusion detection systems

## Key Components
- **Data processing**: PCAP parsing and flow generation for fixed time windows, extraction of packet size, direction, and inter-arrival time for ML feature vectors  
- **Similarity analysis**: custom Chebyshev distance implementation for flows and raw packets, histogram generation without external helper functions, and t-SNE visualizations for dataset comparison and domain shift analysis  
- **Unsupervised detection**: Stacked Denoising Autoencoder implementations with configurable layer types and activation functions, hyperparameter search for reconstruction error thresholding, and feature export for downstream classifiers  
- **Evaluation**: statistical summaries, CDF plots for header and payload sizes, and ROC/precision recall metrics for threshold-based anomaly detection

## How to Use
1. prepare dataset PCAPs for Electra and QUT S7comm and place them in the `data/` folder  
2. run the flow generator to create 2, 4, and 6 minute flows and export feature matrices for normal and attacked flows  
3. execute the Chebyshev and histogram scripts to compare distributions across files and label sets  
4. train the SDA models on normal-only data, export encoded features, and evaluate reconstruction error against a user-defined gamma threshold for attack detection

## Dependencies
- python 3, numpy, pandas, matplotlib, scikit-learn, and a DL framework like tensorflow or pytorch, and tshark or pyshark for pcap extraction

## Notes
All scripts are designed to support reproducible experiments in intrusion detection and adversarial robustness, and users should consult the task sheet for exact evaluation and submission requirements 

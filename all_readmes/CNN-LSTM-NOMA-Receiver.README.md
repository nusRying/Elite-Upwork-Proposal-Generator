name:	nusRying/CNN-LSTM-NOMA-Receiver
description:	
--
# Deep Learning Based NOMA Receiver (CNN-BiLSTM)

This project implements an advanced Deep Learning based receiver for **Non-Orthogonal Multiple Access (NOMA)** systems using a hybrid **CNN-BiLSTM** architecture in MATLAB.

## Project Overview

Non-Orthogonal Multiple Access (NOMA) is a key technology for future wireless communications, allowing multiple users to share the same frequency and time resources by using different power levels. Traditionally, these signals are separated using **Successive Interference Cancellation (SIC)**.

This project explores an alternative approach: using a Deep Neural Network to directly detect user symbols from the combined signal, potentially outperforming SIC in high-noise or non-linear environments.

## Architecture

The project utilizes a hybrid neural network designed to extract both spatial features (using CNN) and temporal dependencies (using BiLSTM) from signal sequences:

- **Input**: I/Q components (Real/Imaginary) of the combined NOMA signal + Normalized SNR feature.
- **CNN Layers**: 1D Convolutional layers for short-term signal feature extraction and denoising.
- **BiLSTM Layers**: Bidirectional Long Short-Term Memory layers to capture temporal correlation across the symbol stream.
- **Output**: Multi-class classification of joint signal states (detecting User 1 and User 2 symbols simultaneously).

## File Structure

- `noma_cnnlstm_dataset.m`: Generates the training and validation dataset by simulating a downlink NOMA channel with AWGN.
- `cnn_lstm_noma_training.m`: Defines the network architecture, configures training options, and trains the model.
- `evaluate_cnnlstm_vs_sic.m`: Evaluation script that compares the Bit Error Rate (BER) performance of the Deep Learning model against the traditional SIC receiver.
- `USERGUIDE.txt`: Quick start instructions.

## How to Run

1.  **Generate Data**: Run `noma_cnnlstm_dataset.m` to create the simulated NOMA signal dataset.
2.  **Train Model**: Run `cnn_lstm_noma_training.m`. This will save a `trained_noma_model.mat` file.
3.  **Evaluate**: Run `evaluate_cnnlstm_vs_sic.m` to generate BER comparison plots and performance metrics.

## Performance Analysis

Initial analysis indicates that applying Deep Learning to joint symbol detection allows the receiver to bypass the error propagation issues common in SIC, especially at lower SNR ranges.

---

> [!NOTE]
> This project is designed for MATLAB's Deep Learning Toolbox. Ensure you have a compatible version installed with support for Sequence-to-Scalar and Sequence-to-Sequence training.


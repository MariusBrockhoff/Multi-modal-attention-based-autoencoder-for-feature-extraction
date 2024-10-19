## Work in progress

Developing a model to extract features from multi-modal data with a Perceiver-based autoencoder. 

The model idea is using two separate Perceiver models for encoding and decoding, respectively. Feature can be extracted in mutltiple ways, either isolating learned features of the encoder model (IxC matrix shown in green) or - similar to classic autoencoder model - latent array produced by a small dense bootleneck layer (as shown below in red). Graphic shows case for inputting sequence data, shall be able to handle all kinds of input data (multi-modal).
![Figure_6_AutoPerceiver](https://github.com/user-attachments/assets/f3205bfe-76b4-4fec-96e8-0faffbe8acb5)

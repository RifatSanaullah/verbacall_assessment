import torch
stt_settings = {
    "stt_config":{
        "model_name": "facebook/wav2vec2-large-960h-lv60-self",
        "device": "cuda" if torch.cuda.is_available() else "cpu"
    },

    "noise_reduce_config": {
        "sr": 16000,
        "stationary": True,
        "prop_decrease": 0.9,
        "n_fft": 1024,
        "win_length": 512,
        "n_std_thresh_stationary": 1.5
    }
}


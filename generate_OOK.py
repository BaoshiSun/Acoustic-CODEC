# %%
import numpy as np
import wave
import struct


# %%
# Parameters
sample_rate = 44100    
carrier_freq = 3000
bit_depth = 16
amplitude = 2**15 - 1

bitrate = 1000      
duration_per_bit = 1 / bitrate  
duration_in_seconds = 10

# genearte 10 seconds of random binary data
num_bits = duration_in_seconds * bitrate  
data = np.random.randint(0, 2, num_bits)  

# %%
# Generate carrier
def generate_carrier(frequency, duration, sampling_rate,amplitude):
    
    time = np.linspace(0, duration,int(sampling_rate * duration), endpoint=False) 
    return amplitude * np.sin(2 * np.pi * frequency * time)

# %%
def ook_modulation(data, carrier_freq, duration, sampling_rate, amplitude):
    signal = np.array([])
    for bit in data:
        if bit == 1:
            carrier = generate_carrier(carrier_freq, duration, sample_rate, amplitude)
        else:
            carrier = np.zeros(int(sample_rate * duration))

        signal = np.concatenate((signal, carrier))
    return signal  

# %%
modulated_signal = ook_modulation(data, carrier_freq, duration, sampling_rate, amplitude)
# write wav file
output_file = "ook_modulated_signal.wav"
with wave.open(output_file, 'w') as wav_file:
    wav_file.setnchannels(1)  # 单声道
    wav_file.setsampwidth(2)  # 每个样本2字节（16位）
    wav_file.setframerate(sample_rate)
    
    # 将信号转换为WAV格式
    for sample in modulated_signal:
        wav_file.writeframes(struct.pack('<h', int(sample)))

print(f"OOK调制后的信号已保存为 {output_file}")

# %%




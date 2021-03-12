import numpy as np
import matplotlib.pyplot as plotter
n = 20
w = 5000
N = 264

def generate_signal(amplitude, phase, frequency, time):
    return amplitude * np.sin(frequency * time + phase)  # Press Ctrl+F8 to toggle the breakpoint.


def signal_generator(harmonics, frequency_max, samples_amount):
    signal_collection = np.zeros(samples_amount)
    for f in range(1, harmonics + 1):
        phase = np.random.uniform((-np.pi / 2), (np.pi / 2))
        amplitude = np.random.uniform(0, 1)
        frequency = (f * frequency_max) / harmonics
        for time in range(samples_amount):
            signal_collection[time] += generate_signal(amplitude, phase, frequency, time)
    return signal_collection


def  autocorrelation(signal, samples_amount, t_shift):
    collection = np.zeros(samples_amount - t_shift)
  
    for f in range(samples_amount - t_shift):
        collection[f] = signal[f] * signal[f + t_shift]

    expected_value = np.average(signal)
    sigma= np.sqrt(np.var(signal))
    covariation = np.average(collection) - expected_value * expected_value

    return covariation / sigma / sigma


def  autocorrelation_tau(signal, samples_amount):
    collection = np.zeros(int(samples_amount / 2))
    for tau in range(int(samples_amount / 2)):
      collection[tau] = autocorrelation(signal, samples_amount, tau)
    return collection


def  correlation_t(signal1, signal2, samples_amount, t_shift):
    collection = np.zeros(samples_amount - t_shift)
  
    for f in range(samples_amount - t_shift):
        collection[f] = signal1[f] * signal2[f + t_shift]

    covariation = np.average(collection) - np.average(signal1) *np.average(signal2)

    return covariation / np.sqrt(np.var(signal1)) / np.sqrt(np.var(signal2))

def  correlation_tau(signal1, signal2, samples_amount):
    collection = np.zeros(int(samples_amount / 2))
    for tau in range(int(samples_amount / 2)):
        collection[tau] = correlation_t(signal1, signal2, samples_amount, tau)
    return collection

signal = signal_generator(n, w, N)
signal_2 = signal_generator(n, w, N)

expected_value = np.average(signal)
variance = np.var(signal)
sigma= np.sqrt(variance)
autocorrelation_t = autocorrelation(signal, n, 7)

expected_value_2 = np.average(signal_2)
variance_2 = np.var(signal_2)
sigma_2= np.sqrt(variance_2)

# correlation = correlation(signal, signal_2, n)

plotter.plot(signal)
plotter.title('Signal 1')
plotter.show()

print('Expected Value for Signal 1 is', np.average(signal))
print('Variance for Signal 1 is', np.var(signal))
print('Autocorrelation for Signal 1 is', autocorrelation_t)


plotter.plot(signal)
plotter.title('Signal 2')
plotter.show()

print('Expected Value for Signal 2 is', expected_value_2)
print('Variance for Signal 2 is', variance_2)

autocorrelation_eachtau = autocorrelation_tau(signal, n)

plotter.plot(autocorrelation_eachtau)
plotter.title('Autocorrelation on tau (0...n/2) ')
plotter.show()

correlation_eachtau = correlation_tau(signal, signal_2, n)

plotter.plot(correlation_eachtau)
plotter.title('Correlation for Signal 1 and Signal 2 on tau (0...n/2) ')
plotter.show()

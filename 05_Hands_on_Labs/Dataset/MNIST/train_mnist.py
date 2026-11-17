# coding: utf-8
import matplotlib.pyplot as plt
from load_mnist import load_mnist
from util import smooth_curve
from multi_layer_net import MultiLayerNet
from optimizer import *



(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True)

train_size = x_train.shape[0]
batch_size = 128
max_iterations = 1000



optimizers = {}
optimizers['SGD'] = SGD()
optimizers['Momentum'] = Momentum()
optimizers['AdaGrad'] = AdaGrad()
optimizers['Adam'] = Adam()


networks = {}
train_loss = {}
for key in optimizers.keys():
    networks[key] = MultiLayerNet(
        input_size=784, hidden_size_list=[100, 100, 100, 100],
        output_size=10)
    train_loss[key] = []    



for i in range(max_iterations):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    
    for key in optimizers.keys():
        grads = networks[key].gradient(x_batch, t_batch)
        optimizers[key].update(networks[key].params, grads)
    
        loss = networks[key].loss(x_batch, t_batch)
        train_loss[key].append(loss)
    
    if i % 100 == 0:
        print( "===========" + "iteration:" + str(i) + "===========")
        for key in optimizers.keys():
            loss = networks[key].loss(x_batch, t_batch)
            print(key + ":" + str(loss))



markers = {"SGD": "o", "Momentum": "x", "AdaGrad": "s", "Adam": "D"}
x = np.arange(max_iterations)
for key in optimizers.keys():
    plt.plot(x, smooth_curve(train_loss[key]), marker=markers[key], markevery=100, label=key)
plt.xlabel("iterations")
plt.ylabel("loss")
plt.ylim(0, 1)
plt.legend()
plt.show()
import matplotlib.pyplot as plt

# Pick a random sample from test set
sample_idx = 0  # Change this to test different images (0 to 9999)
sample_img = x_test[sample_idx]
sample_label = t_test[sample_idx]

# Predict using Adam network (or any optimizer)
predicted = networks['Adam'].predict(sample_img.reshape(1, -1))
predicted_digit = np.argmax(predicted)
true_digit = sample_label if sample_label.ndim == 1 else np.argmax(sample_label)

print(f"True Label: {true_digit}")
print(f"Predicted:  {predicted_digit}")
print(f"Confidence: {np.max(predicted) * 100:.2f}%")

# Show the image
plt.imshow(sample_img.reshape(28, 28), cmap='gray')
plt.title(f"True: {true_digit} | Predicted: {predicted_digit}")
plt.axis('off')
plt.show()
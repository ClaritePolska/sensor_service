# Sensor Service

## 1. Build (base) first image
Use Dockerfile with path: `Docker_base\Dockerfile`
```
 sudo podman build -t quay.io/repository/$nameOfUser/sensorservice-base-aarch64:base .
```
```
sudo podman push [IMEAGE ID] quay.io/$nameOfUser/sensorservice-base-aarch64:base
```
## 2. Build image with Sensor Service

Use Dockerfile with path: `Docker_program\Dockerfile`
```
 sudo podman build -t quay.io/repository/$nameOfUser/sensorservice-aarch64:stable .
 clarite_qiot .

```
```
sudo podman push [IMEAGE ID] quay.io/repository/$nameOfUser/sensorservice-aarch64:stable
```
## 3. Run image
```
sudo podman run -it -v /var/qiot/input/GAS:/var/qiot/input/GAS -v /var/qiot/input/POLLUTION:/var/qiot/input/POLLUTION --rm --privileged --name qiot-sensor-service quay.io/repository/$nameOfUser/sensorservice-aarch64:stable /bin/bash
```
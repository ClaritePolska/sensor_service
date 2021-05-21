FROM quay.io/clarite_qiot/sensorservice-base-aarch64:base
RUN dnf -y install git && \
	git clone https://github.com/ClaritePolska/sensor_service && \
	dnf clean all && \
	chmod +x /sensor_service/main/gas.py /sensor_service/main/pollution.py && \
	echo "#!/bin/bash" >> /sensor_service/entrypoint && \
	echo "python3 sensor_service/main/gas.py & python3 sensor_service/main/pollution.py" >> /sensor_service/entrypoint && \
	chmod +x /sensor_service/entrypoint
ENTRYPOINT ["/sensor_service/entrypoint"]
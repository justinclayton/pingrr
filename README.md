# pingrr

Just me debugging my home mesh network. Small script that just runs a ping forever and sends a local macOS notification if the latency gets high.

# Install Requirements

```
pip3 install -r requirements.txt
```

# Usage

```
usage: pingrr.py [--threshold <threshold_ms>] [--target <ping_target>]
        --threshold: time (in ms) for a ping reply to trigger the notification>] (default: 100)
        --target: DNS name or IP to ping (default: google.com)
```

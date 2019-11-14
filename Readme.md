# Install

`todo`

## How to run

This project needs a config file called `config.yaml` at the root of this directory.

Copy the `config.yaml.dist` file:

```
cp config.yaml.dist config.yaml
```

Then edit it, to correctly set the pin number to which the motor is plugged to.

When you are done, run:

```
python door.py
```

## Config options

### Required
- Map the pin from your gpio connection to the motor

```
pins: [15, 16, 37, 38]
```

### Optional

**Note, for each config option described below, the value is the default one.**

- The motor run twice. Once clockwise, and once counter clockwise. This option set the time to wait before to run the second time.

```
wait_time: 1
```

- Define the number of steps for a rotation sequence.

```
nb_steps: 2048
```

- You can allow only a restricted device by their mac addresses. Restrict them by setting:

```
allowed_mac_addresses: []
```

_Not defining this option, or setting it to an empty list will not restrict any mac address._


**For an example of a full configuration, please look at the _config.yaml.dist_ file**
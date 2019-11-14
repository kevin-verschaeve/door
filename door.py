import yaml
from runner import Runner
from bluedot import BlueDot
from signal import pause

config = yaml.safe_load(open("config.yaml", 'r'))

bd = BlueDot()
runner = Runner(bd, config)

bd.when_client_connects = runner.check_mac_addresses
bd.when_pressed = runner.rotate

pause()
